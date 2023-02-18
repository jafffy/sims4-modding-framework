# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\bucks\bucks_enums.py
# Compiled at: 2016-08-02 01:02:05
# Size of source mod 2**32: 567 bytes
from sims4.tuning.dynamic_enum import DynamicEnumLocked
import enum

class BucksType(DynamicEnumLocked, partitioned=True):
    INVALID = 0


class BucksTrackerType(enum.Int):
    HOUSEHOLD = 0
    CLUB = 1
    SIM = 2
# okay decompiling data/sims4-not-yet-decompiled/simulation/bucks/bucks_enums.pyc
