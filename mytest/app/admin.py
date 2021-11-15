from django.contrib import admin
from .models import State, City, Student

# Register your models here.
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_f_name','student_m_name','student_l_name','student_state','student_city','gender')