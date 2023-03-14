from django.db import models

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=300)
    post=models.CharField(max_length=400)
    image=models.ImageField(upload_to='media')
    comment=models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    logo =models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=50)
    subject=models.TextField(blank=True)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Information(models.Model):
    address1=models.CharField(max_length=300)
    address2=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    time=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)

    def __str__(self):
        return f"{self.address1} {self.address2}"
