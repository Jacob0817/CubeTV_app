#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-11-30
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $V1.0$

import os
from peewee import *

database = MySQLDatabase("wca_data", user="root", host="localhost", port=3306)


class UnknownField(object):

    def __init__(self, *_, **__): pass


class BaseModel(Model):

    class Meta:
        database = database


class Championships(BaseModel):
    championship_type = CharField()
    competition = CharField(column_name='competition_id')
    id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'championships'
        primary_key = False


class Competitions(BaseModel):
    cellname = CharField(column_name='cellName',
                         constraints=[SQL("DEFAULT ''")])
    cityname = CharField(column_name='cityName',
                         constraints=[SQL("DEFAULT ''")])
    countryid = CharField(column_name='countryId',
                          constraints=[SQL("DEFAULT ''")])
    day = IntegerField(constraints=[SQL("DEFAULT 0")])
    endday = IntegerField(column_name='endDay', constraints=[SQL("DEFAULT 0")])
    endmonth = IntegerField(column_name='endMonth',
                            constraints=[SQL("DEFAULT 0")])
    eventspecs = CharField(column_name='eventSpecs', null=True)
    external_website = CharField(null=True)
    id = CharField(constraints=[SQL("DEFAULT ''")])
    information = TextField(null=True)
    latitude = IntegerField(null=True)
    longitude = IntegerField(null=True)
    month = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    organiser = TextField(null=True)
    venue = CharField(constraints=[SQL("DEFAULT ''")])
    venueaddress = CharField(column_name='venueAddress', null=True)
    venuedetails = CharField(column_name='venueDetails', null=True)
    wcadelegate = TextField(column_name='wcaDelegate', null=True)
    year = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'competitions'
        primary_key = False


class Continents(BaseModel):
    id = CharField(constraints=[SQL("DEFAULT ''")])
    latitude = IntegerField(constraints=[SQL("DEFAULT 0")])
    longitude = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    recordname = CharField(column_name='recordName',
                           constraints=[SQL("DEFAULT ''")])
    zoom = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'continents'
        primary_key = False


class Countries(BaseModel):
    continentid = CharField(column_name='continentId',
                            constraints=[SQL("DEFAULT ''")])
    id = CharField(constraints=[SQL("DEFAULT ''")])
    iso2 = CharField(null=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'countries'
        primary_key = False


class EligibleCountryIso2SForChampionship(BaseModel):
    championship_type = CharField()
    eligible_country_iso2 = CharField()
    id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'eligible_country_iso2s_for_championship'
        primary_key = False


class Events(BaseModel):
    cellname = CharField(column_name='cellName',
                         constraints=[SQL("DEFAULT ''")])
    format = CharField(constraints=[SQL("DEFAULT ''")])
    id = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'events'
        primary_key = False


class Formats(BaseModel):
    expected_solve_count = IntegerField()
    id = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    sort_by = CharField()
    sort_by_second = CharField()
    trim_fastest_n = IntegerField()
    trim_slowest_n = IntegerField()

    class Meta:
        table_name = 'formats'
        primary_key = False


class Persons(BaseModel):
    countryid = CharField(column_name='countryId',
                          constraints=[SQL("DEFAULT ''")])
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    id = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(null=True)
    subid = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'persons'
        primary_key = False


class Ranksaverage(BaseModel):
    best = IntegerField(constraints=[SQL("DEFAULT 0")])
    continentrank = IntegerField(
        column_name='continentRank', constraints=[SQL("DEFAULT 0")])
    countryrank = IntegerField(
        column_name='countryRank', constraints=[SQL("DEFAULT 0")])
    eventid = CharField(column_name='eventId', constraints=[SQL("DEFAULT ''")])
    personid = CharField(column_name='personId',
                         constraints=[SQL("DEFAULT ''")])
    worldrank = IntegerField(column_name='worldRank',
                             constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'ranksaverage'
        primary_key = False


class Rankssingle(BaseModel):
    best = IntegerField(constraints=[SQL("DEFAULT 0")])
    continentrank = IntegerField(
        column_name='continentRank', constraints=[SQL("DEFAULT 0")])
    countryrank = IntegerField(
        column_name='countryRank', constraints=[SQL("DEFAULT 0")])
    eventid = CharField(column_name='eventId', constraints=[SQL("DEFAULT ''")])
    personid = CharField(column_name='personId',
                         constraints=[SQL("DEFAULT ''")])
    worldrank = IntegerField(column_name='worldRank',
                             constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'rankssingle'
        primary_key = False


class Results(BaseModel):
    average = IntegerField(constraints=[SQL("DEFAULT 0")])
    best = IntegerField(constraints=[SQL("DEFAULT 0")])
    competitionid = CharField(
        column_name='competitionId', constraints=[SQL("DEFAULT ''")])
    eventid = CharField(column_name='eventId', constraints=[SQL("DEFAULT ''")])
    formatid = CharField(column_name='formatId',
                         constraints=[SQL("DEFAULT ''")])
    personcountryid = CharField(column_name='personCountryId', null=True)
    personid = CharField(column_name='personId',
                         constraints=[SQL("DEFAULT ''")])
    personname = CharField(column_name='personName', null=True)
    pos = IntegerField(constraints=[SQL("DEFAULT 0")])
    regionalaveragerecord = CharField(
        column_name='regionalAverageRecord', null=True)
    regionalsinglerecord = CharField(
        column_name='regionalSingleRecord', null=True)
    roundtypeid = CharField(column_name='roundTypeId',
                            constraints=[SQL("DEFAULT ''")])
    value1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    value2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    value3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    value4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    value5 = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'results'
        primary_key = False


class Rounds(BaseModel):
    sorry_message = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'rounds'
        primary_key = False


class Roundtypes(BaseModel):
    cellname = CharField(column_name='cellName',
                         constraints=[SQL("DEFAULT ''")])
    final = IntegerField()
    id = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'roundtypes'
        primary_key = False


class Scrambles(BaseModel):
    competitionid = CharField(column_name='competitionId')
    eventid = CharField(column_name='eventId')
    groupid = CharField(column_name='groupId')
    isextra = IntegerField(column_name='isExtra')
    roundtypeid = CharField(column_name='roundTypeId')
    scramble = TextField()
    scrambleid = IntegerField(column_name='scrambleId',
                              constraints=[SQL("DEFAULT 0")])
    scramblenum = IntegerField(column_name='scrambleNum')

    class Meta:
        table_name = 'scrambles'
        primary_key = False
