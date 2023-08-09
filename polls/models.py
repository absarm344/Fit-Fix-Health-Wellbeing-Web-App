from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1,'user'),
        (2,'Nutritionist'),
        (3,'Admin'),
    )
    
    user_type = models.CharField(choices=USER,default=1,max_length=50) # type: ignore
    phone = models.CharField(max_length=15,default="",unique=True)
    profile_pic = models.TextField(blank=True)
    

    
class dietProfileSetting(models.Model):
    tagE = models.CharField(max_length=50)
    age = models.CharField(default='0',max_length = 3)
    gender = models.CharField(max_length=10)
    weight = models.CharField(default="0",max_length = 5)
    heightCm = models.CharField(default="0",max_length = 5)
    neckSize = models.CharField(default="0",max_length = 5)
    waistSize = models.CharField(default="0",max_length = 5)
    goal = models.CharField(default="healthy", max_length=30)
    activity = models.CharField(default="1.55", max_length=10)
    bfp = models.CharField(default= "0", max_length=10)

    def __str__(self):
        return self.tagE
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    bf = models.IntegerField()
    lu = models.IntegerField()
    di = models.IntegerField()
    cal = models.IntegerField()
    fat = models.IntegerField()
    pro = models.IntegerField()
    sug = models.IntegerField()
    imagepath= models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name

 #Subscription module
class subPlan(models.Model):
	title=models.CharField(max_length=150)
	price=models.IntegerField()
	feature1=models.CharField(max_length=300,default="Null")
	feature2=models.CharField(max_length=300,default="Null")
	feature3=models.CharField(max_length=300,default="Null")
	feature4=models.CharField(max_length=300,default="Null")
	feature5=models.CharField(max_length=300,default="Null")

	def __str__(self):
		return self.title

class exercises(models.Model):
	exercise=models.CharField(max_length=150)
	desc=models.CharField(max_length=500,default="Null")
	goal=models.CharField(max_length=100,default="Null")
	link=models.URLField()

	def __str__(self):
		return self.exercise

    