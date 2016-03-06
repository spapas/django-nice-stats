from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from stats.models import Game, Team
from stats.filters import TeamFilter

class StatsTemplateView(TemplateView):
    template_name = 'stats.html'
    
    def get_context_data(self, **kwargs):
        context = super(StatsTemplateView, self).get_context_data(**kwargs)
        stats = {}
        all_teams = Team.objects.all()
        filter = TeamFilter(self.request.GET, all_teams)
        
        group_by_continent = filter.qs.order_by('country__continent__name').values('country__continent__name').annotate(count=Count('id'))
        
        group_by_games = filter.qs.annotate(count1=Count('team1'), count2=Count('team2'))
        
        
        stats['total'] = all_teams.count()
        stats['filtered_total'] = filter.qs.count()
        
        stats['group_by_continent'] = group_by_continent
        stats['group_by_games'] = group_by_games
        
        context['form'] = filter.form
        context['stats'] = stats
        return context