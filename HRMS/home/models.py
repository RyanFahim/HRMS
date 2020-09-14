from django.db import models


    
# new\
class Postion(models.Model):
    title = models.CharField(max_length=50)
        
    def __str__(self):
        return self.title

class Employee(models.Model):
    name= models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5)
    email = models.EmailField(max_length=100)
    position = models.ForeignKey(Postion, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField( max_length=50) 
    desc = models.TextField()

class Award(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title




