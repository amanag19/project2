from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def contact_form(request):
    if request.session.has_key('is_logged'):
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        subject=request.POST['subject']
        messagee=request.POST['message']
        login_user=User.objects.get(username=request.user.username)
        new_contact=Contact(username=login_user,firstname=fname,lastname=lname,email=email,subject=subject,message=messagee)
        new_contact.save()
        return redirect('/main')
    
    else:
         return redirect('/login')
        