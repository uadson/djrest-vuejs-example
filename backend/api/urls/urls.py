from django.urls import path, include

from . import routers


app_name = 'api'

urlpatterns = [
    path('', include(routers)),
]
