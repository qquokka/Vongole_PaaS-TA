from django.db import models

# Create your models here.
class Subject(models.Model):
    pass

class Category(models.Model):
    pass

class Problem(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete = models.CASCADE,
        )

