# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\statistic_types.py
# Compiled at: 2014-01-17 22:08:32
# Size of source mod 2**32: 964 bytes
from sims4.tuning.tunable import Tunable

class StatisticComponentGlobalTuning:
    DEFAULT_RADIUS_TO_CONSIDER_OFF_LOT_OBJECTS = Tunable(description='\n        The radius from the Sim that an off-lot object must be for a Sim to consider it.\n        If the object is not on the active lot and outside of this radius, the Sim will \n        ignore it.\n        ',
      tunable_type=float,
      default=20)
    DEFAULT_OFF_LOT_TOLERANCE = Tunable(description="\n        The tolerance for when a Sim is considered off the lot.  If a Sim is off the \n        lot but within this tolerance, he will be considered on the lot from autonomy's \n        perspective.  Note that this only effects autonomy, nothing else. \n        ",
      tunable_type=float,
      default=5)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/statistic_types.pyc
