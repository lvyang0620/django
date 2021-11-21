from django.db import models

# Create your models here.
#教师模型
class Teacher(models.Model):
    #姓名
    name = models.CharField(max_length=20,default='')
    #生日
    birth = models.DateField()
    #性别
    gender_choices = [
        (0,'女'),
        (1, '男'),
    ]
    gender = models.IntegerField(choices=gender_choices)
    #是否结婚
    is_married_choices = [
        (0, '未婚'),
        (1, '已婚'),
    ]
    is_married = models.IntegerField(choices=is_married_choices)

    def __str__(self):
        return self.name

#学生模型
class Student(models.Model):
    #姓名
    name = models.CharField(max_length=20,default='')
    #生日
    birth = models.DateField()
    #性别
    gender_choices = [
        (0,'女'),
        (1, '男'),
    ]
    gender = models.IntegerField(choices=gender_choices)
    #学生和教师的多对多关系
    teacher= models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name