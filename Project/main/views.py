from django.views.generic import TemplateView, ListView

from main.models import Factory


class AboutPage(TemplateView):
    template_name = "main/about.html"


class MapPage(ListView):
    template_name = "main/map.html"
    queryset = Factory.objects.all()
    context_object_name = "factories"
