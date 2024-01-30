from django.urls import re_path

from example.views import CheckUserConsumer

urlpatterns = [
    re_path(r'^ws/', CheckUserConsumer.as_asgi()),
]
