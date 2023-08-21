from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('public.urls')),
    path('accounts/', include('utilisateur.urls')),
    path('piece_list/',include('piece.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('car_parts/', include('api.urls')),
    path('panier_list/',include('panier.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  sdskfq
