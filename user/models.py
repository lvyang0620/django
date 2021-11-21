from django.db import models

# Create your models here.
#身份证模型
class IdCard(models.Model):
    code = models.CharField(max_length=18)

    def __str__(self):
        return self.code

#用户模型
class Person(models.Model):
    name = models.CharField(max_length=20,default='')
    age = models.IntegerField(null=True)
    id_card= models.OneToOneField(IdCard,on_delete=models.CASCADE)

    def __str__(self):
        return self.name