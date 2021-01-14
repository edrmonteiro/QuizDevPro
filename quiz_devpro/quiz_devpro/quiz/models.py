from django.db import models

# Create your models here.

class Question (models.Model):
    title = models.TextField()
    options = models.JSONField()
    available = models.BooleanField(default=False)
    answer = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])

class Student(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email

class Ranking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'question'], name='unique_answer')
        ]
