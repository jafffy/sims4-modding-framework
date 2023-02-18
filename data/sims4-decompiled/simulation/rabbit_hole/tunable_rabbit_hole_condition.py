# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\rabbit_hole\tunable_rabbit_hole_condition.py
# Compiled at: 2018-08-14 16:06:05
# Size of source mod 2**32: 918 bytes
from sims4.tuning.tunable import TunableVariant
from statistics.statistic_conditions import TunableStatisticCondition

class TunableRabbitHoleCondition(TunableVariant):

    def __init__(self, *args, **kwargs):
        (super().__init__)(args, stat_based=TunableStatisticCondition(description='\n                A condition based on the status of a statistic.\n                '), 
         default='stat_based', **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/rabbit_hole/tunable_rabbit_hole_condition.pyc
