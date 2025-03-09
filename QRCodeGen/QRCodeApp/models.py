from django.db import models
from UserApp.models import Profile


# Create your models here.
class QRCode(models.Model):
    owner = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True)
    url = models.TextField()
    image = models.ImageField(upload_to= "images/", null = True)
    expire_date = models.DateTimeField()
    bg_color = models.CharField(max_length = 255, null= True)
    qrcode_color = models.CharField(max_length = 255, null= True)

