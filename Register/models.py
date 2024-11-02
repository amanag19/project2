from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Muser(models.Model):
    muser = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.muser.username