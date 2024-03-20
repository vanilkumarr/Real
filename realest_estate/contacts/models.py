from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=100)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    

    def __str__(self) -> str:
        return self.name