# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\narrative\narrative_aware_component.py
# Compiled at: 2018-10-10 17:41:54
# Size of source mod 2**32: 2190 bytes
from objects.components import Component
from objects.components.state import TunableStateValueReference
from objects.components.types import NARRATIVE_AWARE_COMPONENT
from sims4.resources import Types
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, TunableMapping, TunableReference, TunableList
import services

class NarrativeAwareComponent(Component, HasTunableFactory, AutoFactoryInit, component_name=NARRATIVE_AWARE_COMPONENT):
    FACTORY_TUNABLES = {'narrative_state_mapping': TunableMapping(description='\n            A tunable mapping linking a narrative to the states the component\n            owner should have.\n            ',
                                  key_type=TunableReference(description='\n                The narrative we are interested in.\n                ',
                                  manager=(services.get_instance_manager(Types.NARRATIVE))),
                                  value_type=TunableList(description='\n                A tunable list of states to apply to the owning object of\n                this component when this narrative is active.\n                ',
                                  tunable=TunableStateValueReference(pack_safe=True)))}

    def on_add(self):
        self.on_narratives_set(services.narrative_service().active_narratives)

    def on_finalize_load(self):
        self.on_narratives_set(services.narrative_service().active_narratives)

    def on_narratives_set(self, narratives):
        for narrative in narratives:
            if narrative in self.narrative_state_mapping:
                for state_value in self.narrative_state_mapping[narrative]:
                    self.owner.set_state(state_value.state, state_value)
# okay decompiling data/sims4-not-yet-decompiled/simulation/narrative/narrative_aware_component.pyc
