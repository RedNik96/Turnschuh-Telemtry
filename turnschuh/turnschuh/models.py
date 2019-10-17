from django.db import models
from django.contrib.auth.models import User 

class TransferFile(models.Model):
    path = models.FileField(upload_to="uploads/")
    user = models.ForeignKey(User)
    direction = models.BooleanField(choices=((True,"Upload"),(False,"Download")))
    transferTime = models.DateTimeField(auto_now=True)
    fileType = models.IntegerField(choices=((0,"TaskData"),(1,"Documents")), default=0)
    name= models.CharField(max_length=255, default=0)