from django.db import models

class Seed(models.Model):
    crop = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    altitude_zone = models.CharField(max_length=100)
    maturity = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)
    yield_per_acre = models.CharField(max_length=50)
    attributes = models.TextField()

    def __str__(self):
        return f"{self.crop} ({self.variety})"

