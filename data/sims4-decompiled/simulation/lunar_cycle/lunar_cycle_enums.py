# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lunar_cycle\lunar_cycle_enums.py
# Compiled at: 2022-02-04 00:42:10
# Size of source mod 2**32: 902 bytes
import enum

class LunarPhaseType(enum.Int):
    NEW_MOON = 0
    WAXING_CRESCENT = 1
    FIRST_QUARTER = 2
    WAXING_GIBBOUS = 3
    FULL_MOON = 4
    WANING_GIBBOUS = 5
    THIRD_QUARTER = 6
    WANING_CRESCENT = 7


class LunarPhaseLockedOption(LunarPhaseType, export=False):
    NO_LUNAR_PHASE_LOCK = 8


class LunarCycleLengthOption(enum.Int):
    TWO_DAY = 0
    FOUR_DAY = 1
    FULL_LENGTH = 2
    DOUBLE_LENGTH = 3
    TRIPLE_LENGTH = 4
# okay decompiling data/sims4-not-yet-decompiled/simulation/lunar_cycle/lunar_cycle_enums.pyc
