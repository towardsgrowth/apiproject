from django.urls import path
from django.contrib import admin
from .views.users import SendEmailRegistrationApiView

urlpatterns = [
    path('sign up/', SendEmailRegistrationApiView.as_view()),

]