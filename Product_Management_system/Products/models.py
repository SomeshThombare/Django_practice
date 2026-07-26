from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    exp_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to= 'products/', default=None, null=False)
    def __str__(self):
        return f"Products : {self.name}"

