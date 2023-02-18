# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\modular\sectional_sofa_tuning.py
# Compiled at: 2020-12-18 00:23:25
# Size of source mod 2**32: 488 bytes
import services
from sims4.resources import Types
from sims4.tuning.tunable import TunableReference

class SectionalSofaTuning:
    SECTIONAL_SOFA_OBJECT_DEF = TunableReference(description='\n        Catalog definition for the sectional sofa object.\n        ',
      manager=(services.get_instance_manager(Types.OBJECT)))
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/modular/sectional_sofa_tuning.pyc
