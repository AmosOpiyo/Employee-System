from django.db import models

# Create your models here.

class details(models.Model):
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    job_title=models.CharField(max_length=50)
    contract=models.CharField(max_length=50)
    salary=models.FloatField(max_length=50)
    date_joined=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
