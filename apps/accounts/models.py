from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, second_name, third_name, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(
            first_name=first_name, 
            second_name=second_name, 
            third_name=third_name, 
            email=email, 
            **extra_fields
            )
        user.password = make_password(password)
        user
        user.save(using=self._db)
        return user

    def create_user(self, first_name, second_name, third_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(first_name, second_name, third_name, email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        first_name = second_name = third_name = "default"
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")

        return self._create_user(first_name, second_name, third_name, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=40, null=False, blank=False)
    second_name = models.CharField(max_length=40, null=False, blank=False)
    third_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def create_verification_code(self) -> None:
        from uuid import uuid4
        self.verification_code = str(uuid4())
    
    def __str__(self) -> str:
        return self.email