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
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class Continent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class Country(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=255)
    place_id = models.IntegerField()
    code = models.CharField(unique=True, max_length=255)
    alt_names = models.CharField(max_length=255, blank=True, null=True)
    pop = models.IntegerField()
    area = models.IntegerField()
    continent_id = models.IntegerField(blank=True, null=True)
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


class Event(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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



class EventsTeam(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    event = models.ForeignKey('Event')
    team = models.ForeignKey('Team')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_teams'
        unique_together = (('event', 'team'),)


class Game(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(unique=True, max_length=255, blank=True, null=True)
    round_id = models.IntegerField()
    pos = models.IntegerField()
    group = models.ForeignKey('Group', blank=True, null=True)
    team1 = models.ForeignKey('Team', related_name='team1',)
    team2 = models.ForeignKey('Team', related_name='team2',)
    play_at = models.DateTimeField()
    postponed = models.BooleanField()
    play_at_v2 = models.DateTimeField(blank=True, null=True)
    play_at_v3 = models.DateTimeField(blank=True, null=True)
    ground_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
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

        
class Group(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    event = models.ForeignKey('Event')
    title = models.CharField(max_length=255)
    pos = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class GroupsTeam(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group_id = models.IntegerField()
    team_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups_teams'
        unique_together = (('group_id', 'team_id'),)


class League(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    country = models.ForeignKey('Country', blank=True, null=True)
    club = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'


class Log(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    msg = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    app = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    ts = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Place(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class Prop(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'props'


class Region(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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

        
class Round(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    event_id = models.IntegerField()
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


class Season(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons'


class Tagging(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class Team(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    synonyms = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)
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

