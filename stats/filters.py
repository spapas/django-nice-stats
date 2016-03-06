import django_filters
from stats.models import Game, Team

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        #fields = ['name', 'price', 'manufacturer']
        

class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = ['country__continent']