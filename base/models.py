from django.db import models

# Create your models here.
class Users(models.Model):
    employeeID = models.CharField(max_length=100)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    userType = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=100, blank=True, null=True)

    
    class Meta:
        db_table = 'users_table'