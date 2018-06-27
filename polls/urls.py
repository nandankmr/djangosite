from django.urls import path
from . import views

urlpatterns = [

    # polls/
    path('', views.index, name='index'),
    path('datetime/', views.date_time),
    #     polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]