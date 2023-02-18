# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\eco_footprint\eco_footprint_enums.py
# Compiled at: 2020-01-13 23:00:24
# Size of source mod 2**32: 460 bytes
import enum

class EcoFootprintStateType(enum.Int):
    GREEN = 0
    NEUTRAL = 1
    INDUSTRIAL = 2


class EcoFootprintDirection(enum.Int):
    TOWARD_GREEN = 0
    AT_CONVERGENCE = 1
    TOWARD_INDUSTRIAL = 2
# okay decompiling data/sims4-not-yet-decompiled/simulation/eco_footprint/eco_footprint_enums.pyc
