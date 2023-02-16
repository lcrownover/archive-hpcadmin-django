from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('add_user', views.add_user, name="add_user")
]
