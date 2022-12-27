from django.db import models
from unittest.util import _MAX_LENGTH

class StuModel(models.Model):
    # sid = models.IntegerField(primary_key=True) 
    sname = models.CharField(max_length = 200)
    age = models.IntegerField()
    dob = models.DateField()
    grade = models.CharField(max_length = 2)
    cid = models.IntegerField()
    class Meta:
        db_table = "assignment4_stumodel"
    

class CorModel(models.Model):
    cid = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length = 200)
    course_hours = models.IntegerField()
    class Meta:
        db_table = "assignment4_cormodel"
    