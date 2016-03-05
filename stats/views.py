from django.shortcuts import render
from django.views.generic import TemplateView

class StatsTemplateView(TemplateView):
    template_name = 'stats.html'
    
    def get_context_data(self, **kwargs):
        context = super(StatsTemplateView, self).get_context_data(**kwargs)
        
        return context