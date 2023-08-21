from django.urls import path
from piece import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('pieces/', views.piece_list), 
    path('pieces/<int:id>',views.piece_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)