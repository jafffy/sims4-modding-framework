# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\faction_reputation\faction_rep_tuning.py
# Compiled at: 2020-04-08 20:35:37
# Size of source mod 2**32: 1359 bytes
from sims4.tuning.tunable import TunablePackSafeReference, TunableColor
from sims4.tuning.tunable_base import ExportModes
import services, sims4.resources

class FactionRepModuleTuning:
    FIRST_ORDER_REPUTATION = TunablePackSafeReference(description='\n        Ranked statistic for first order reputation.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('RankedStatistic', ),
      export_modes=(ExportModes.All))
    RESISTANCE_REPUTATION = TunablePackSafeReference(description='\n        Ranked statistic for resistance reputation.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('RankedStatistic', ),
      export_modes=(ExportModes.All))
    SCOUNDREL_REPUTATION = TunablePackSafeReference(description='\n        Ranked statistic for scoundrel reputation.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('RankedStatistic', ),
      export_modes=(ExportModes.All))
# okay decompiling data/sims4-not-yet-decompiled/simulation/faction_reputation/faction_rep_tuning.pyc
