from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=30)

class City(models.Model):
    city = models.CharField(max_length=30)

class Student(models.Model):
    GENDER_CHOICES = (
        ('m','male'),
        ('f','female'),
    )
    student_f_name = models.CharField(max_length=30)
    student_m_name = models.CharField(max_length=30)
    student_l_name = models.CharField(max_length=30)
    student_state = models.ForeignKey(State,on_delete=models.CASCADE)
    student_city = models.ForeignKey(City, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)