# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\carry\carry_tuning.py
# Compiled at: 2017-04-17 20:28:51
# Size of source mod 2**32: 788 bytes
from sims4.tuning.tunable import TunableReference
import services, sims4.resources

class CarryPostureStaticTuning:
    POSTURE_CARRY_NOTHING = TunableReference(description='\n            Reference to the posture that represents carrying nothing\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.POSTURE)),
      class_restrictions='CarryingNothing')
    POSTURE_CARRY_OBJECT = TunableReference(description='\n        Reference to the posture that represents carrying an Object\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.POSTURE)),
      class_restrictions='CarryingObject')
# okay decompiling data/sims4-not-yet-decompiled/simulation/carry/carry_tuning.pyc
