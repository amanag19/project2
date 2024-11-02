from django.shortcuts import render , redirect
from Register.models import Muser
from Core.models import RentVehichle
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def inside(request):
 user = request.user
 if user is not None:
    muser = Muser.objects.get(muser=user)
    if muser.status == 1:
        m = RentVehichle.objects.all().order_by()[::-1] 
        context = {'med':m}
        return render(request,'shome.html',context)
    else:
        print(request, user)
        data=RentVehichle.objects.all().order_by()[::-1] 
        return render(request, 'mainpage.html',{"messages": data})

def sellrreg(request):
    if request.method == 'GET':
        if request.session.has_key('is_logged'):
            return render(request, 'sellerregis.html')
        else:
            return redirect('/login')
    elif request.method=='POST':
        ownname=request.POST['oname'] 
        sname=request.POST['sname']              
        address=request.POST['saddress']
        wano=request.POST['wano'] 
        hdstatus=request.POST['hdstatus'] 

        vehichle_regis=request.FILES['vregis'] 
        vehichle_img=request.FILES['myfile']
         
        #fs = FileSystemStorage()
        #filename = fs.save(vehichle_regis.name, vehichle_regis) 

        login_user=User.objects.get(username=request.user.username)
        new_rent=RentVehichle(username=login_user,ownername=ownname,shop_name=sname,
        address=address,whatsapp_no=wano,hdstatus=hdstatus,shop_registration=vehichle_regis,shop_photo=vehichle_img )
        new_rent.save()
        
    #return render(request,'mainpage.html')     
    return redirect('/inside')    
    #return render(request,'sellerregis.html')        
    

    #Admin

def checkAdmin(id):
    user = User.objects.get(id = id)
    muser = Muser.objects.get(muser = user)
    if muser.status == 1:
        return False
    else:
        return True

def shopDetails(request, shop_id):
    if not request.user.is_authenticated:
        return redirect('/music/login')
    else:
        if checkAdmin(request.user.id):
            return redirect('/music/login')

        rent = RentVehichle.objects.get(id=shop_id)
        return render(request, 'shopDetails.html',{'shop':rent})

def final(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        approve = request.POST.get('approve')
        reject = request.POST.get('reject')
        oname = RentVehichle.objects.get(id=aid)
        if approve==None:
            print(reject)
            oname.status = -1
            oname.save()
            # rejectMail(mail bhej dena yaha se)
            
        elif reject==None:
            print(approve)
            oname.status = 1
            oname.save()
            #acceptMail(mail bhej dena yaha se)
    return redirect('adminhome')
