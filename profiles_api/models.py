from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """ Manager for User profiles """

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('Users must have an email address')

        #normalize email address - make second half lower case
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #setting password in a hashed way (can't be stolen in clear)
        user.set_password(password)
        user.save(using=self._db) #using standard database (could use multiple)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """
        #Use the previously defined function
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True) #force uniqueness of emails in the database
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #user by default should be active
    is_staff = models.BooleanField(default=False) #Django admin user

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #overriding default, instead of username, email must be provided during AuthenticationMiddleware
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Return full name of user """
        return self.name

    def get_short_name(self):
        """ Return short name of user """
        return self.name

    def __str___(self):
        """ Return string representation of user """
        return self.email

class ProfileFeedItem(models.Model):
    """ Profile status updates """
    # Connect 2 models with foreign key, feed belongs to a specific user
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # foreign key Profile, in our case UserProfile
        on_delete=models.CASCADE #what happens when UserProfile is deleted, CASCADE - remove associated feed items
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True) #add automatically timestamp when feed is created

    def __str__(self):
        """ Return the model as a string """
        return self.status_text
