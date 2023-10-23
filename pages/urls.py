from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view()),
    path("about-us/", views.AboutPageView.as_view())
]