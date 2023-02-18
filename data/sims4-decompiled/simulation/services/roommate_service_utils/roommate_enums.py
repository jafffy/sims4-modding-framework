# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\services\roommate_service_utils\roommate_enums.py
# Compiled at: 2019-07-24 17:55:45
# Size of source mod 2**32: 561 bytes
from sims4.tuning.dynamic_enum import DynamicEnumLocked
import enum

class RoommateLeaveReason(DynamicEnumLocked):
    INVALID = 0
    OVERCAPACITY = 1


class LeaveReasonTestingTime(enum.Int):
    UNTESTED = 0
    HOUSEHOLD_ROOMMATES_ALL_LOTS = 1
    HOUSEHOLD_ROOMMATES_HOME_LOT = 2
    ALL_ROOMMATES = 3
# okay decompiling data/sims4-not-yet-decompiled/simulation/services/roommate_service_utils/roommate_enums.pyc
