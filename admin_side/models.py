from djongo import models

# Create your models here.
class Blocked(models.Model):
    id = models.AutoField(primary_key=True)
    Email= models.EmailField()

