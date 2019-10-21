from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    dream_univ = models.CharField(max_length=20)  # 대학교, 학과
    curriculum = models.CharField(max_length=3)  # 문과, 이과, 예체능, 실업계 등
    elective_subject1 = models.CharField(max_length=10)  # 선택과목 1
    elective_subject2 = models.CharField(max_length=10)  # 선택과목 2
    second_foreign_lang = models.CharField(max_length=5)  # 제2외국어