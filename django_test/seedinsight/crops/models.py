from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    altitude_zone = models.CharField(max_length=100)
    maturity = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    yield_amount = models.DecimalField(max_digits=5, decimal_places=2)
    attributes = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.variety}"
