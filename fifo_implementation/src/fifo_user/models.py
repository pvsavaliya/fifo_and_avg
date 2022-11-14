from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetail(AbstractUser):
    
    userID          = models.BigAutoField(primary_key=True, unique=True)
    # role            = models.CharField(max_length=128, null=True, blank=True)
    username        = models.CharField(max_length=128,unique=True, null=False)
    # first_name      = models.CharField(max_length=128, null=True)
    # last_name       = models.CharField(max_length=128, null=True)
    # dob             = models.DateField(max_length=128, null=True)
    email           = models.EmailField(max_length=128, null=False, unique=True)
    # userphone       = models.CharField(max_length=10, null=True)
    # useraddress     = models.CharField(max_length=200, null=True,blank=True)
    password        = models.CharField(max_length=255, null=False)
    isDeleted       = models.BooleanField(default = False,null=True)
    Token           = models.TextField(null=True)
    # Image           = models.FileField(upload_to='message/%Y/%m/%d/', null=True, blank=True)
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
