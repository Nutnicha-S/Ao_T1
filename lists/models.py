from django.db import models
from django.db import models


class Userinfo(models.Model):
    # เก็บ username ไว้ใน name
    name = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# ให้เก็บข้อมูล วิชา หน่วยกิต เกรด ของแต่ละวิชา และเทอมเอาไว้
class Semester(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    term = models.CharField(max_length=255)

# เก็บ GPA   
class GradeGPA(models.Model):
    GPA = models.CharField(max_length=255)
    gpa_term = models.CharField(max_length=255)

# เก็บ GPAX
class GradeGPAX(models.Model):
    GPAX = models.CharField(max_length=255)
