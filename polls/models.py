from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #发布时间
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choice',related_query_name='choices')
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text
