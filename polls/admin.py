from django.contrib import admin
from  .models import Question, Choise
# Register your models here.
#注册模型
admin.site.register(Question)
admin.site.register(Choise)
