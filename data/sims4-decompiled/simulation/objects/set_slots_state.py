# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\set_slots_state.py
# Compiled at: 2022-03-31 17:01:58
# Size of source mod 2**32: 1792 bytes
from sims4.tuning.tunable import AutoFactoryInit, HasTunableFactory, TunableSet
from sims4.tuning.tunable_hash import TunableStringHash32

class SetSlotsState(HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'enabled_slot_hashes':TunableSet(description='\n            The names of the slots to enable. These slots will be disabled \n            when the state is removed.\n            ',
       tunable=TunableStringHash32(description='\n                The name of the slot to enable.\n                ',
       default='_ctnm_')), 
     'disabled_slot_hashes':TunableSet(description='\n            The names of the slots to disable. These slots will be enabled \n            when the state is removed.\n            ',
       tunable=TunableStringHash32(description='\n                The name of the slot to disable.\n                ',
       default='_ctnm_'))}

    def __init__(self, target, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._target = target

    def start(self, *args, **kwargs):
        self._target.enable_slots(self.enabled_slot_hashes)
        self._target.disable_slots(self.disabled_slot_hashes)

    def stop(self, *args, **kwargs):
        self._target.enable_slots(self.disabled_slot_hashes)
        self._target.disable_slots(self.enabled_slot_hashes)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/set_slots_state.pyc
