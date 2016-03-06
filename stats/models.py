# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    place = models.ForeignKey('Place')
    code = models.CharField(max_length=255, blank=True, null=True)
    alt_names = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('Country')
    region = models.ForeignKey('Region', blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    pop = models.IntegerField(blank=True, null=True)
    popm = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    m = models.BooleanField()
    c = models.BooleanField()
    d = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'
        verbose_name_plural = 'cities'
        
    def __unicode__(self):
        return self.name


class Continent(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=255)
    place = models.ForeignKey('Place')
    alt_names = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'continents'
        
    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=255)
    place_id = models.IntegerField()
    code = models.CharField(unique=True, max_length=255)
    alt_names = models.CharField(max_length=255, blank=True, null=True)
    pop = models.IntegerField()
    area = models.IntegerField()
    continent = models.ForeignKey('Continent', blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    s = models.BooleanField()
    c = models.BooleanField()
    d = models.BooleanField()
    motor = models.CharField(max_length=255, blank=True, null=True)
    iso2 = models.CharField(max_length=255, blank=True, null=True)
    iso3 = models.CharField(max_length=255, blank=True, null=True)
    fifa = models.CharField(max_length=255, blank=True, null=True)
    net = models.CharField(max_length=255, blank=True, null=True)
    wikipedia = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name_plural = 'countries'
        
    def __unicode__(self):
        return self.name


class Event(models.Model):
    key = models.CharField(unique=True, max_length=255)
    league = models.ForeignKey('League')
    season = models.ForeignKey('Season')
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    team3 = models.BooleanField()
    sources = models.CharField(max_length=255, blank=True, null=True)
    config = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'

    def __unicode__(self):
        return self.key

class EventsTeam(models.Model):
    event = models.ForeignKey('Event')
    team = models.ForeignKey('Team')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_teams'
        unique_together = (('event', 'team'),)


class Game(models.Model):
    key = models.CharField(unique=True, max_length=255, blank=True, null=True)
    round = models.ForeignKey('Round')
    pos = models.IntegerField()
    group = models.ForeignKey('Group', blank=True, null=True)
    team1 = models.ForeignKey('Team', related_name='team1',)
    team2 = models.ForeignKey('Team', related_name='team2',)
    play_at = models.DateTimeField()
    postponed = models.BooleanField()
    play_at_v2 = models.DateTimeField(blank=True, null=True)
    play_at_v3 = models.DateTimeField(blank=True, null=True)
    ground_id = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('City', blank=True, null=True)
    knockout = models.BooleanField()
    home = models.BooleanField()
    score1 = models.IntegerField(blank=True, null=True)
    score2 = models.IntegerField(blank=True, null=True)
    score1et = models.IntegerField(blank=True, null=True)
    score2et = models.IntegerField(blank=True, null=True)
    score1p = models.IntegerField(blank=True, null=True)
    score2p = models.IntegerField(blank=True, null=True)
    score1i = models.IntegerField(blank=True, null=True)
    score2i = models.IntegerField(blank=True, null=True)
    score1ii = models.IntegerField(blank=True, null=True)
    score2ii = models.IntegerField(blank=True, null=True)
    next_game_id = models.IntegerField(blank=True, null=True)
    prev_game_id = models.IntegerField(blank=True, null=True)
    winner = models.IntegerField(blank=True, null=True)
    winner90 = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'
        
    def __unicode__(self):
        return '{0} - {1}'.format(self.team1, self.team2)

        
class Group(models.Model):
    event = models.ForeignKey('Event')
    title = models.CharField(max_length=255)
    pos = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'
    
    def __unicode__(self):
        return self.title


class GroupsTeam(models.Model):
    group = models.ForeignKey('Group')
    team = models.ForeignKey('Team')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups_teams'
        unique_together = (('group', 'team'),)


class League(models.Model):
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    country = models.ForeignKey('Country', blank=True, null=True)
    club = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'
        
    def __unicode__(self):
        return self.title



class Place(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'
        
    def __unicode__(self):
        return self.name


class Prop(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'props'


class Region(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    place = models.ForeignKey('Place')
    code = models.CharField(max_length=255, blank=True, null=True)
    abbr = models.CharField(max_length=255, blank=True, null=True)
    iso = models.CharField(max_length=255, blank=True, null=True)
    nuts = models.CharField(max_length=255, blank=True, null=True)
    alt_names = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('Country')
    pop = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'
        unique_together = (('key', 'country'),)
        
    def __unicode__(self):
        return self.name

        
class Round(models.Model):
    event = models.ForeignKey('Event')
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    pos = models.IntegerField()
    knockout = models.BooleanField()
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    auto = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rounds'
        
    def __unicode__(self):
        return self.title


class Season(models.Model):
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons'
        
    def __unicode__(self):
        return self.title


class Tagging(models.Model):
    tag_id = models.IntegerField()
    taggable_id = models.IntegerField()
    taggable_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taggings'
        unique_together = (('taggable_id', 'taggable_type', 'tag_id'),)


class Tag(models.Model):
    key = models.CharField(unique=True, max_length=255)
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'
        
    def __unicode__(self):
        return self.name


class Team(models.Model):
    key = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    synonyms = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('Country')
    city = models.ForeignKey('City', blank=True, null=True)
    club = models.BooleanField()
    since = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    national = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

    def __unicode__(self):
        return self.title