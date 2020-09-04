from django.db import models
from django.db import models
import datetime 

class Notice(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)
    des = models.TextField()

    def __str__(self):
        return self.title
    
