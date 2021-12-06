from django.contrib import admin
from django.urls import path, include
from cursos.urls import ROUTER

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('api/v2/', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
