# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\portal_locking_enums.py
# Compiled at: 2021-03-08 19:33:39
# Size of source mod 2**32: 1290 bytes
import enum

class LockPriority(enum.Int):
    PLAYER_LOCK = 0
    SYSTEM_LOCK = 1


class LockSide(enum.IntFlags):
    LOCK_FRONT = 1
    LOCK_BACK = 2
    LOCK_BOTH = LOCK_FRONT | LOCK_BACK


class LockType(enum.Int):
    LOCK_SIMINFO = 0
    LOCK_ALL_WITH_SIMID_EXCEPTION = 1
    LOCK_ALL_WITH_SITUATION_JOB_EXCEPTION = 2
    LOCK_ALL_WITH_CLUBID_EXCEPTION = 3
    INACTIVE_APARTMENT_DOOR = 4
    INDIVIDUAL_SIM = 5
    LOCK_ALL_WITH_GENUS_EXCEPTION = 6
    LOCK_RANK_STATISTIC = 7
    LOCK_ALL_WITH_BUFF_EXCEPTION = 8
    LOCK_CREATURE = 9


class ClearLock(enum.Int):
    CLEAR_ALL = 0
    CLEAR_OTHER_LOCK_TYPES = 1
    CLEAR_NONE = 2
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/portal_locking_enums.pyc
