# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\world\spawn_point_enums.py
# Compiled at: 2016-08-31 22:09:28
# Size of source mod 2**32: 627 bytes
from sims4.tuning.dynamic_enum import DynamicEnum
import enum

class SpawnPointPriority(DynamicEnum):
    DEFAULT = 0


class SpawnPointRequestReason(enum.Int):
    DEFAULT = 0
    SPAWN = 1
    LEAVE = 2
# okay decompiling data/sims4-not-yet-decompiled/simulation/world/spawn_point_enums.pyc
