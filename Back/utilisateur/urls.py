from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from utilisateur import views

urlpatterns =[
    path('profile/',views.ProfileView.as_view()),
    path('signup/', views.signup),
    path('api/auth/', views.CustomAuthToken.as_view()),   
]

urlpatterns = format_suffix_patterns(urlpatterns)