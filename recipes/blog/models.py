from django.db import models

class Blog(models.Model):
    Name = models.CharField(max_length=30)
    Chief = models.CharField(max_length=200)
    Ingredients = models.CharField(max_length=300)

    class Meta:
        db_table = 'recipes'
