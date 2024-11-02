from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RentVehichle(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ownername= models.CharField(max_length=200)
    shop_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True)
    whatsapp_no=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
    hdstatus=models.CharField(max_length=200,null=True)
    shop_registration = models.FileField(upload_to='vehichle registration',default='')
    shop_photo = models.ImageField(upload_to='vehichle images',default='')
    
    def __str__(self):
        return self.ownername