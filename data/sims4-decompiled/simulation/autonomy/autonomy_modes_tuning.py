# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\autonomy\autonomy_modes_tuning.py
# Compiled at: 2020-06-19 23:17:49
# Size of source mod 2**32: 358 bytes
from sims4.tuning.tunable import TunableSimMinute

class AutonomyModesTuning:
    LOCKOUT_TIME = TunableSimMinute(description='\n        Number of sim minutes to lockout a failed interaction push or routing failure.\n        ',
      default=240)
# okay decompiling data/sims4-not-yet-decompiled/simulation/autonomy/autonomy_modes_tuning.pyc
