from django.urls import path
from . import views

urlpatterns = [
  path('kekw/',views.getData),
]