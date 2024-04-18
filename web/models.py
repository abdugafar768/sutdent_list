from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    father_name = models.CharField(max_length = 50)
    date_of_birth = models.CharField(max_length = 50)
    adress = models.CharField(max_length=100)
    bio = models.TextField()
    is_merried = models.BooleanField()
    

    def __str__(self):
        return self.first_name + " " + self.last_name
# Create your models here.
