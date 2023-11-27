from django.urls import path
import main.views as views

app_name = "main"

urlpatterns = [
    path("", views.AboutPage.as_view(), name="about"),
    path("map/", views.MapPage.as_view(), name="map"),
]
