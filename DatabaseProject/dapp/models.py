from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.FloatField()
    image = models.ImageField(upload_to='employees/',blank=True, null=True)

    def __str__(self):
        return f"Employee :{self.name}"