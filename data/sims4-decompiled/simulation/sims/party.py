# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\party.py
# Compiled at: 2014-06-07 21:16:44
# Size of source mod 2**32: 779 bytes
from interactions import ParticipantType
from sims4.tuning.tunable import TunableList
from statistics.statistic_ops import TunableStatisticChange

class Party:
    RALLY_FALSE_ADS = TunableList(description=' \n        A list of false advertisement for rallyable interactions. Use this\n        tunable to entice Sims to autonomously choose rallyable over non-\n        rallyable interactions.\n        ',
      tunable=TunableStatisticChange(locked_args={'subject':ParticipantType.Actor,  'advertise':True}))
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/party.pyc
