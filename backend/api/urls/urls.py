from django.urls import path, include
from api.urls import (
    breads_url,
)

app_name = 'api'

urlpatterns = [
    path('', include(breads_url)),
]
