from django.contrib import admin
from .models import Question, Student

# Register your models here.
@admin.register(Question )
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'available']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created']

