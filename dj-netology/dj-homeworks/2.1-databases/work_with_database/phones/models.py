from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
