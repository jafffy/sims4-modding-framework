# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\walkstyle\walkstyle_enums.py
# Compiled at: 2017-06-23 22:16:01
# Size of source mod 2**32: 943 bytes
import enum
from sims4.tuning.dynamic_enum import DynamicEnum

class WalkStyleRunAllowedFlags(enum.IntFlags):
    RUN_ALLOWED_INDOORS = 1
    RUN_ALLOWED_OUTDOORS = 2


class WalkstyleBehaviorOverridePriority(DynamicEnum):
    DEFAULT = 0


class WalkStylePriority(DynamicEnum):
    INVALID = 0
    COMBO = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/walkstyle/walkstyle_enums.pyc
