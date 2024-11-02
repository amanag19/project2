from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from Register.models import Muser
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginUser(request):

    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['pass']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            request.session['is_logged']=True
            if request.session.has_key('is_logged'):
                print("AAya")
            auth.login(request,user)
            return redirect('/inside')
        else:
            messages.info(request,'invalid user')
            return redirect('/registerUser')
        
@login_required        
def logout(request):
    if request.session.has_key('is_logged'):
        print("sesson del ")
        del request.session['is_logged']
    auth.logout(request)
    return redirect('/')