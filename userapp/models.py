from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=200,null=True)
    DOB=models.DateField(auto_now=False,name=None)
    Contact=models.IntegerField()
    Nationality=models.CharField(max_length=200,null=True)
    Education=models.CharField(max_length=200,null=True)
    Skills=models.CharField(max_length=400,null=True)

    def __str__(self):
        return '{}'.format(self.name,self.Nationality,self.Education,self.Skills)


class Portfolio(models.Model):
    Education_1= models.CharField(max_length=200, null=True)
    College = models.CharField(max_length=200, null=True)
    Education_2 = models.CharField(max_length=200, null=True,blank=True)
    College_2 = models.CharField(max_length=200, null=True,blank=True)
    Work_1=models.CharField(max_length=500,null=True)
    Work_2 = models.CharField(max_length=500, null=True,blank=True)
    Work_3 = models.CharField(max_length=500, null=True,blank=True)
    Project_1=models.CharField(max_length=500,null=True)
    Project_2 = models.CharField(max_length=500, null=True,blank=True)
    Project_3 = models.CharField(max_length=500, null=True,blank=True)
    Project_4 = models.CharField(max_length=500, null=True,blank=True)
    Project_5 = models.CharField(max_length=500, null=True,blank=True)
    Project_6 = models.CharField(max_length=500, null=True,blank=True)
    Certification_1=models.CharField(max_length=400,null=True)
    Certification_2 = models.CharField(max_length=400, null=True,blank=True)
    Certification_3 = models.CharField(max_length=400, null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.Education_1,self.Education_2,self.College,self.College_2,self.Work_1,self.Work_2,self.Work_3,self.Project_1,self.Project_2,self.Project_3,self.Project_4,self.Project_5,self.Project_6,self.Certification_1,self.Certification_2,self.Certification_3)

class Project(models.Model):
    Project_Name= models.CharField(max_length=500)
    image=models.ImageField(upload_to='media/',blank=True)
    Description = models.TextField(max_length=2000)
    Link = models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.Description,self.Link,self.Project_Name)

# models.py

from django.db import models
from django.contrib.auth.models import User

class UserID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.identifier}"
