# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\teleport\teleport_type_liability.py
# Compiled at: 2019-07-11 01:03:42
# Size of source mod 2**32: 2174 bytes
from interactions.base.interaction_constants import InteractionQueuePreparationStatus
from interactions.liability import Liability, PreparationLiability
from sims4.tuning.tunable import AutoFactoryInit, HasTunableFactory, TunableEnumEntry
from teleport.teleport_enums import TeleportStyle, TeleportStyleSource

class TeleportStyleLiability(Liability, HasTunableFactory, AutoFactoryInit):
    LIABILITY_TOKEN = 'TeleportStyleLiability'
    FACTORY_TUNABLES = {'teleport_style': TunableEnumEntry(description='\n            Style to be used while the liability is active.\n            ',
                         tunable_type=TeleportStyle,
                         default=(TeleportStyle.NONE),
                         invalid_enums=(
                        TeleportStyle.NONE,),
                         pack_safe=True)}

    def __init__(self, interaction, source=TeleportStyleSource.TUNED_LIABILITY, **kwargs):
        (super().__init__)(**kwargs)
        self._sim_info = interaction.sim.sim_info
        self._source = source
        self._sim_info.add_teleport_style(self._source, self.teleport_style)

    def release(self):
        self._sim_info.remove_teleport_style(self._source, self.teleport_style)


class TeleportStyleInjectionLiability(Liability):
    LIABILITY_TOKEN = 'TeleportStyleInjectionLiability'

    def should_transfer(self, continuation):
        return False
# okay decompiling data/sims4-not-yet-decompiled/simulation/teleport/teleport_type_liability.pyc
