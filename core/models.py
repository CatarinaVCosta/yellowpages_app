from django.db import models

# Create your models here.

DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ' \
              'ligula eget dolor.'

CATEGORY_CHOICES = (
    ('Shoes', 'Shoes'),
    ('Restaurants', 'Restaurants'),
    ('Hairdressers', 'Hairdressers'),
    ('Pharmacies', 'Pharmacies'),
)


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    postal_code = models.TextField(max_length=8)
    district = models.CharField(max_length=200)
    url = models.URLField()
    photo = models.ImageField(upload_to='companies')
    description = models.TextField(default=DESCRIPTION)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='')
    nr_searches = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
