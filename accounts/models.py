from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

#Custom models for superadmin.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Please provide a valid email address.')
        
        if not username:
            raise ValueError('Please provide a valid username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    #Function for creating superusers
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
        #setting the superuser permissions.
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



#Basic fields required for creating custom user model.
class account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(blank=False)
    avatar = models.ImageField(upload_to='photos/account', default=None)
    slug = models.SlugField(max_length=200, null = True)
    intro = models.TextField(max_length=300, null=True)
    position = models.CharField(max_length=200, null=True)
    education = models.TextField(max_length=300, null=True)
    
    
    
    #Required fields
    
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    #setting the login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    
    
    #defining the mandatory methods
    def has_perm(self, perm, object=None):
        return self.is_admin
    
    
    def has_module_perms(self, add_label=True):
        return True
    
    
    