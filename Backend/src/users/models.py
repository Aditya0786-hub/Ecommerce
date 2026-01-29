from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from cloudinary.models import CloudinaryField

# user manager to handle creation
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extrafield):
        if not email:
            raise ValueError("Email is requires")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extrafield)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    Role_Choices = (
        ('customer','Customer'),
        ('seller','Seller')
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=50,
        choices = Role_Choices
        )
    image = CloudinaryField(
        'profileImage',
        blank = True,
        null = True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    def __str__(self):
        return f"{self.email} ({self.role})"
