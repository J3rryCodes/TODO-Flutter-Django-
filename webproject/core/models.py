from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserManager(BaseUserManager):
    """ Base user manager to create Email as Userneme user """

    def create_user(self,email,name,password):
        """ Create a normal user """

        email = email.lower()

        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self,email,name,password):
        """ Create super user """

        user = self.create_user(email=email,name=name,password=password)
        user.is_superuser = True
        user.is_staff(True)

        user.save()
        return user



class UserProfileModel(AbstractBaseUser,PermissionsMixin):
    """ User Model which can made with email,name & password """

    email = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
