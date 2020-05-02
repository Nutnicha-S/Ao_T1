from django.db import models
from django.db import models


class Userinfo(models.Model):
    # เก็บ username ไว้ใน name
    name = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# ให้เก็บข้อมูล วิชา หน่วยกิต เกรด ของแต่ละวิชา และเทอมเอาไว้
class Semister(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    term = models.CharField(max_length=255)

# เก็บ GPA ของทั้ง 8 เทอมไว้ ตามลำดับ    
class GPA(models.Model):
    GPA_1 = models.CharField(max_length=255)
    GPA_2 = models.CharField(max_length=255)
    GPA_3 = models.CharField(max_length=255)
    GPA_4 = models.CharField(max_length=255)
    GPA_5 = models.CharField(max_length=255)
    GPA_6 = models.CharField(max_length=255)
    GPA_7 = models.CharField(max_length=255)
    GPA_8 = models.CharField(max_length=255)

class GradeGPAX(models.Model):
    GPAX = models.CharField(max_length=255)