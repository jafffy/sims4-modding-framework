# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\fire\set_fire_state.py
# Compiled at: 2019-02-08 23:10:31
# Size of source mod 2**32: 1120 bytes
import random
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, TunablePercent
import services

class SetFireState(HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'chance': TunablePercent(description='\n            Chance that the fire will trigger\n            ',
                 default=100)}

    def __init__(self, target, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.target = target

    def start(self, *_, **__):
        if random.random() < self.chance:
            fire_service = services.get_fire_service()
            fire_service.spawn_fire_at_object(self.target)

    def stop(self, *_, **__):
        pass
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/fire/set_fire_state.pyc
