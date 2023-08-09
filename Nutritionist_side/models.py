from djongo import models

class Nutrition(models.Model):
    id = models.AutoField(primary_key=True)
    Title=models.CharField(max_length=30,default="")
    Name=models.CharField(max_length=30,default="")
    Bio=models.CharField(max_length=250,default="")
    Email=models.EmailField(max_length=250,default="")
    Phone=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    Experience=models.IntegerField(default=0)
    Skill1=models.CharField(max_length=20,default="")
    Skill2=models.CharField(max_length=20,default="")
    Skill3=models.CharField(max_length=20,default="")
    Skill4=models.CharField(max_length=20,default="")
    Rate_skill1=models.CharField(max_length=20,default="")
    Rate_skill2=models.CharField(max_length=20,default="")
    Rate_skill3=models.CharField(max_length=20,default="")
    Rate_skill4=models.CharField(max_length=20,default="")
    Days_of_Program=models.IntegerField(default=0)
    Customers=models.IntegerField(default=0)
    Sessions=models.IntegerField(default=0)
    link_Calendly=models.CharField(max_length=50,default="")

class Nutrition_Request(models.Model):
    id = models.AutoField(primary_key=True)
    First_name=models.CharField(max_length=30,default="")
    Last_name=models.CharField(max_length=30,default="")
    Country=models.CharField(max_length=25,default="")
    Email=models.EmailField(max_length=250,default="")
    Phone=models.IntegerField(default=0)
    Degree=models.CharField(max_length=15,default="")
    Gender=models.CharField(max_length=15,default="")
    Address=models.CharField(max_length=15,default="")
    Experience=models.IntegerField(default=0)
    Password=models.CharField(max_length=25,default="")
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default="")
    nutrition=models.EmailField(max_length=30,default="")
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.CharField(max_length=30)



