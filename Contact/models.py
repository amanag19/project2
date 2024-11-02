from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=400)

    def __str__(self):
        return self.firstname