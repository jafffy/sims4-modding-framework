# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\teleport\teleport_enums.py
# Compiled at: 2019-07-08 18:59:27
# Size of source mod 2**32: 651 bytes
from sims4.tuning.dynamic_enum import DynamicEnum
import enum

class TeleportStyle(DynamicEnum, partitioned=True):
    NONE = 0


class TeleportStyleSource(enum.Int, export=False):
    TUNED_LIABILITY = 0
    TELEPORT_STYLE_SUPER_INTERACTION = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/teleport/teleport_enums.pyc
