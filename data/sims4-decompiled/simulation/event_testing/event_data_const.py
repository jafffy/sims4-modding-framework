# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\event_testing\event_data_const.py
# Compiled at: 2020-04-20 16:44:12
# Size of source mod 2**32: 1164 bytes
import enum

class ObjectiveDataStorageType(enum.Int, export=False):
    CountData = ...
    IdData = ...


class DataType(enum.Int, export=False):
    RelationshipData = 1
    SimoleanData = 2
    TimeData = 3
    TravelData = 5
    ObjectiveCount = 6
    CareerData = 7
    TagData = 8
    RelativeStartingData = 9
    ClubBucks = 10
    TimeInClubGatherings = 11
    Mood = 12
    BucksData = 13


class RelationshipData(enum.Int, export=False):
    CurrentRelationships = 0
    TotalRelationships = 1


class SimoleonData(enum.Int):
    MoneyFromEvents = 0
    TotalMoneyEarned = 1


class TimeData(enum.Int, export=False):
    SimTime = 0
    ServerTime = 1


class TagData(enum.Int, export=False):
    SimoleonsEarned = 0
    TimeElapsed = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/event_testing/event_data_const.pyc
