from django.urls import path
from . import views

urlpatterns = [
    #比如：127.0.0.1/polls/
    path('',views.index,name='index'),
    #比如：127.0.0.1/polls/2/
    path('<int:question_id>/',views.detail,name='detail'),
    # 比如：127.0.0.1/polls/2/result
    path('<int:question_id>/result/', views.result, name='result'),
    # 比如：127.0.0.1/polls/2/votes
    path('<int:question_id>/votes/', views.votes, name='votes'),
]