from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=40)

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
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
    content = models.TextField(null=True)

class Example(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    content_type = models.BooleanField()
    example_1 = models.TextField(null=True)
    example_2 = models.TextField(null=True)
    example_3 = models.TextField(null=True)
    example_4 = models.TextField(null=True)
    example_5 = models.TextField(null=True)


