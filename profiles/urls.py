from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("up/", views.UserProfileView.as_view()),
]
