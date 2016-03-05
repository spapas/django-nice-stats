from django.shortcuts import render
from django.views.generic import TemplateView

class StatsTemplateView(TemplateView):
    template_name = 'stats.html'