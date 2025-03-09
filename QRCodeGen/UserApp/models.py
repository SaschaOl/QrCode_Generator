from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    subscription = models.CharField(default = 'free', max_length=100)
    subscription_expire_date = models.DateTimeField(null= True)
    


