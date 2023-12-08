from django.views.generic import TemplateView, DetailView
from django.shortcuts import render

from main.models import Factory, Article

class AboutPage(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = Article.objects.first()
        return context


class FactoryPage(DetailView):
    template_name = "main/factory.html"
    queryset = Factory.objects.all()
    context_object_name = "factory"
    pk_url_kwarg = 'factory_id'


def MapPage(request):
    factories = Factory.objects.all()

    return render(request, "main/map.html", {"factories": factories, "redirectTo": "/factory/"})


class ArticlePage(DetailView):
    template_name = "main/article.html"
    queryset = Article.objects.all()
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev"] = Article.objects.filter(next=self.get_object()).first()
        return context
