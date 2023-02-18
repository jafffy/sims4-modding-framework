# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\aging\aging_statistic.py
# Compiled at: 2019-08-14 00:53:17
# Size of source mod 2**32: 1871 bytes
from sims.sim_info_lod import SimInfoLODLevel
from sims4.utils import classproperty
from statistics.continuous_statistic import ContinuousStatistic
import date_and_time, sims4.math

class AgeProgressContinuousStatistic(ContinuousStatistic):
    _default_convergence_value = sims4.math.POS_INFINITY
    decay_modifier = 1
    delayed_decay_rate = None

    def __init__(self, tracker, initial_value):
        self.min_lod_value = SimInfoLODLevel.BACKGROUND
        super().__init__(tracker, initial_value)

    @classproperty
    def max_value(cls):
        return cls.default_value

    @classproperty
    def min_value(cls):
        return 0.0

    @classproperty
    def best_value(cls):
        return cls.max_value

    @classproperty
    def persisted(cls):
        return True

    @classmethod
    def set_modifier(cls, modifier):
        cls.decay_modifier = modifier

    @property
    def base_decay_rate(self):
        return self.decay_modifier / (date_and_time.HOURS_PER_DAY * date_and_time.MINUTES_PER_HOUR)
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/aging/aging_statistic.pyc
