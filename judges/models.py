from django.db import models

# Create your models here.
class Subject(models.Model):
    pass

class Category(models.Model):
    pass

class Problem(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category",
        on_delete = models.CASCADE,
        )
    q_date = models.DateField()
    q_org = models.CharField(max_length=35)
    q_num = models.IntegerField()
    correct_rate = models.FloatField()
    header = models.TextField()
    content = models.TextField()

class Example(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    content = models.TextField()