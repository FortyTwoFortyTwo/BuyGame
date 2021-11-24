from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Platform(models.Model):

    class Meta:
        verbose_name_plural = 'Platforms'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    platforms = models.ManyToManyField('Platform')
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    new = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2,
                                   null=True, blank=True,
                                   validators=[
                                       MaxValueValidator(1.0),
                                       MinValueValidator(0.0)
                                   ])
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_price(self):
        if self.discount:
            return round(self.price * (1 - self.discount), 2)
        else:
            return self.price

    def get_discount(self):
        return int(self.discount * 100)
