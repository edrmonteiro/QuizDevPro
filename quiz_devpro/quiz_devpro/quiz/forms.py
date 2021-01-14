from django.forms import ModelForm
from .models import Game

class StudentForm(Modelform):
    class Meta:
        model = Aluno
        fiels = ['nome', 'email']