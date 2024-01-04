from django.urls import path
#if the preceding url path matches '/polls' followin the domain name,
#the main urls.py file will strip the remainder of the path and send it here
from . import views


app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.DetailView.as_view(), name="detail"), # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),# ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
]