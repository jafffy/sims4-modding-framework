# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\object_enums.py
# Compiled at: 2019-07-25 23:23:33
# Size of source mod 2**32: 2130 bytes
import enum
from sims4.tuning.dynamic_enum import DynamicEnum

class ResetReason(enum.Int, export=False):
    NONE = ...
    RESET_EXPECTED = ...
    RESET_ON_ERROR = ...
    BEING_DESTROYED = ...


class ItemLocation(enum.Int):
    INVALID_LOCATION = 0
    ON_LOT = 1
    SIM_INVENTORY = 2
    HOUSEHOLD_INVENTORY = 3
    OBJECT_INVENTORY = 4
    FROM_WORLD_FILE = 5
    FROM_OPEN_STREET = 6
    FROM_CONDITIONAL_LAYER = 7


class PersistenceType(enum.Int):
    FULL = 0
    BUILDBUY = 1
    NONE = 2


class ObjectClaimStatus(enum.Int, export=False):
    UNCLAIMED = 0
    CLAIMED = 1


class ObjectRoutingBehaviorTrackingCategory(DynamicEnum):
    NONE = 0
    BOT = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/object_enums.pyc
