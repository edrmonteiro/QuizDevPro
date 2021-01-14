from django.contrib import admin
from .models import Game, Student

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'available']

admin.site.register(Game,GameAdmin )
admin.site.register(Student)