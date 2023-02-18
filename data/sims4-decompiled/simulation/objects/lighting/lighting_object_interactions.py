# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\lighting\lighting_object_interactions.py
# Compiled at: 2020-04-17 00:47:04
# Size of source mod 2**32: 1327 bytes
from objects.lighting.lighting_interactions import SwitchLightImmediateInteraction
from objects.object_state_utils import ObjectStateHelper
import sims4
logger = sims4.log.Logger('LightingAndObjectState', default_owner='mkartika')

class SwitchLightAndStateImmediateInteraction(SwitchLightImmediateInteraction):
    INSTANCE_TUNABLES = {'state_settings': ObjectStateHelper.TunableFactory(description='\n            Find objects in the same room or lot based on the tags and \n            set state to the desired state.\n            ')}

    def _run_interaction_gen(self, timeline):
        yield from super()._run_interaction_gen(timeline)
        self.state_settings.execute_helper(self.target)
        if False:
            yield None
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/lighting/lighting_object_interactions.pyc
