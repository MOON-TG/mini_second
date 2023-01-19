from django.db import models

# Create your models here.

class Info(models.Model):
   battery = models.CharField(max_length=20)
   color = models.CharField(max_length=20)

   def __str__(self):
      return f'[{self.pk}]{self.battery}{self.color}'

   