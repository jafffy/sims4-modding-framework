# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\locators\locator_tuning.py
# Compiled at: 2020-04-30 19:48:17
# Size of source mod 2**32: 528 bytes
import services, sims4
from sims4.tuning.tunable import TunableReference

class LocatorTuning:
    TARGET_LOCATOR_ID_STAT = TunableReference(description='\n        The stat name used to check for a target locator id on the routing object.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)))
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/locators/locator_tuning.pyc
