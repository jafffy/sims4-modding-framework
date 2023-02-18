# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\reputation\reputation_tuning.py
# Compiled at: 2018-07-17 17:54:43
# Size of source mod 2**32: 901 bytes
from sims4.tuning.tunable import TunablePackSafeReference
from sims4.tuning.tunable_base import ExportModes
import services, sims4.resources

class ReputationTunables:
    REPUTATION_RANKED_STATISTIC = TunablePackSafeReference(description='\n        The ranked statistic that is to be used for tracking reputation progress.\n        \n        This should not need to be tuned at all. If you think you need to tune\n        this please speak with a GPE before doing so.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('RankedStatistic', ),
      export_modes=(
     ExportModes.ClientBinary,))
# okay decompiling data/sims4-not-yet-decompiled/simulation/reputation/reputation_tuning.pyc
