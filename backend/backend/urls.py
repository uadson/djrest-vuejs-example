from django.contrib import admin
from django.urls import path, include

from api.routers import routers


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('rest_framework.urls')),

    path('api/app/v1/', include(routers.router.urls)),
]
