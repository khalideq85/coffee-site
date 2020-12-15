from django.db import models

# Create your models here.


class Coffee(models.Model):
    product_name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    current_price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
