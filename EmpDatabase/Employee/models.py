from django.db import models

# Create your models here.
class EmpUser(models.Model):
    name = models.CharField(max_length= 50)
    age  = models.IntegerField()
    salary = models.FloatField()

    def __str__(self):
        return self.name

class EmpProfile(models.Model):
    m_no = models.CharField(max_length=13)
    city_name = models.CharField(max_length=100)
    user = models.OneToOneField(EmpUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    