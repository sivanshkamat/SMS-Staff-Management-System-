from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    phone_no= models.IntegerField(null=True)
    is_phone_no_verified= models.BooleanField( default=False)
    
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class BaseModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no=models.IntegerField()
    city=models.CharField(max_length=20)
    
    class Meta:
        abstract=True

class  StudentModel(BaseModel):
    roll=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name


class TeacherModel(BaseModel):
    experience=models.IntegerField()
    def __str__(self):
        return self.name
    
class SubjectModel(models.Model):
    sub=models.CharField(max_length=20)
    score=models.IntegerField()
    grade=models.CharField(max_length=2)
    
    def __str__(self):
        return self.sub