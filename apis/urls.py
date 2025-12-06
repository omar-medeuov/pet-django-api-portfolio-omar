from django.urls import path

from apis.views import index

urlpatterns = [
    path("", index, name="index_view"),
]