from django.urls import path
from panier import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('paniers/', views.panier_list),
    path('paniers/<int:pk>/', views.panier_detail),

    path('panierpieces/', views.panierpiece_list),
    path('panierpieces/<int:pk>/', views.panierpiece_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)