from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Min

from main.models import Factory, Picture

from django.shortcuts import render

class AboutPage(TemplateView):
    template_name = "main/about.html"


class MapPage(ListView):
    template_name = "main/map.html"
    queryset = Factory.objects.all()
    context_object_name = "factories"


class FactoryPage(DetailView):
    template_name = "main/factory.html"
    queryset = Factory.objects.all()
    context_object_name = "factory"
    pk_url_kwarg = 'factory_id'


def MapPage(request):
    factories = Factory.objects.all()

    return render(request, "main/map.html", {"factories": factories, "redirectTo": "/factory/"})
