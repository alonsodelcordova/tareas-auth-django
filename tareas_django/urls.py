from django.contrib import admin
from django.urls import path, include
from tareas_django.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.security.urls')),
    path('producto/', include('apps.product.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)