from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Muser
from django.core.mail import EmailMessage

def registerUser(request): 
     if request.method=='GET':
        return render(request , 'register.html')
     elif request.method=='POST':
        uname=request.POST['name']
        u_email=request.POST['email']
        passw=request.POST['password']
        conf_pass=request.POST['re_password']
        if passw==conf_pass:

            if User.objects.filter(username=uname).exists():
                messages.info(request,'User Taken')
                return redirect('/')

            elif User.objects.filter(email=u_email).exists():
                messages.info(request,'E-mail Taken')
                return redirect('/')


            else:
                user = User.objects.create_user(username=uname,email=u_email,password=passw)
                muser = Muser(muser=user)
                user.save()
                muser.save()
                #sendmail
                email = EmailMessage(
                'Welcome '+uname+' to our platform',
                'Welcome to Findmyride the only platform where you can book a self-driven vehichle to explore any city or outstation',
                 'agrawal.aman49@gmail.com',
                [u_email],
                
                )
                email.send(fail_silently=False)
                #endmail
                return redirect('/login')
                
            
        else:
            print('user not saved')
            return redirect('/registerUser')