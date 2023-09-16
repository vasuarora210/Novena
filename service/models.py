from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    mob_num = models.IntegerField()
    message = models.TextField(max_length=250)

class Department(models.Model):
    department_name=models.CharField(max_length=150)

    



