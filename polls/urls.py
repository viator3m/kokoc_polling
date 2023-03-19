from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('solved/', views.solved, name='solved'),
    path('polls/clear/<int:poll_id>/<int:question_id>/', views.clear,
         name='clear'),
    path('polls/finish/<int:poll_id>/', views.finish, name='finish'),
    path('polls/<int:poll_id>/<int:question_id>/', views.polling,
         name='polling'),
]
