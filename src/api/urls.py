from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('ping', views.PingView.as_view(), name="ping"),
]
