from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import main.views as views

app_name = "main"

urlpatterns = [
    path("", views.AboutPage.as_view(), name="about"),
    path("map/", views.MapPage.as_view(), name="map"),
    path("factory/<int:factory_id>/", views.FactoryPage.as_view(), name="factory"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
