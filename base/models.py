from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser):
    employeeID = models.CharField(max_length=100)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    userType = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsersManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users_table'




# from django.db import models

# # Create your models here.
# class Users(models.Model):
#     employeeID = models.CharField(max_length=100)
#     firstName= models.CharField(max_length=100)
#     lastName= models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100, blank=True, null=True)
#     userType = models.CharField(max_length=100, blank=True, null=True)
#     otp = models.CharField(max_length=100, blank=True, null=True)

#     REQUIRED_FIELDS = [ 'password']
#     USERNAME_FIELD = 'email'
#     is_anonymous = 'False'
#     is_authenticated = 'True'
    
#     class Meta:
#         db_table = 'users_table'