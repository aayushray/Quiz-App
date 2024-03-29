import email
from django.db import models

# Create your models here.

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self): 
        return self.question

class Score(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    correct = models.IntegerField(null=True)
    total_questions = models.IntegerField(null=True)

    def __str__(self):
        return self.username