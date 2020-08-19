from django.db import models

# Create your models here.



class Category(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self):
        return self.cat

class Asset(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
        
    

    
