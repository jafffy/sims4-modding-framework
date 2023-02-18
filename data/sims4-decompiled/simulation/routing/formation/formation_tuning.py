# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\formation\formation_tuning.py
# Compiled at: 2018-08-29 23:51:24
# Size of source mod 2**32: 715 bytes
from sims4.tuning.tunable import TunableRange

class FormationTuning:
    GOAL_HEIGHT_LIMIT = TunableRange(description='\n        Max value in meters between the height of the formation master and\n        the goals generated by a routing slave.\n        If the goals have a height different higher than this value, they\n        will be ignored even though the could be inside the valid constraint\n        around the master.\n        ',
      tunable_type=float,
      default=0.5,
      minimum=0)
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/formation/formation_tuning.pyc
