from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    descirption = models.TextField()

    def __str__(self):
        return self.name

class Products(models.Model):
    item = models.CharField(max_length=100)
    new_price = models.DecimalField(max_digits=10,decimal_places=2)
    old_price = models.DecimalField(max_digits=10,decimal_places=2)
    desciption = models.TextField()
    categories = models.ForeignKey(Categories, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.item
    
