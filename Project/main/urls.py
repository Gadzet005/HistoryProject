from django.urls import path

import main.views as views

app_name = "main"

urlpatterns = [
    path("", views.AboutPage.as_view(), name="about"),
    path("map/", views.MapPage, name="map"),
    path("factory/<int:factory_id>/", views.FactoryPage.as_view(), name="factory"),
    path("article/<int:article_id>/", views.ArticlePage.as_view(), name="article"),
]
