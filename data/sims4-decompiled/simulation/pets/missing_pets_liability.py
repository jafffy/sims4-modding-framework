# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\pets\missing_pets_liability.py
# Compiled at: 2017-09-13 20:11:07
# Size of source mod 2**32: 1539 bytes
from interactions import ParticipantType
from interactions.liability import Liability
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, TunableEnumEntry
MISSING_PET_LIABILITY = 'MissingPetLiability'

class MissingPetLiability(Liability, HasTunableFactory, AutoFactoryInit):
    LIABILITY_TOKEN = MISSING_PET_LIABILITY
    FACTORY_TUNABLES = {'participant': TunableEnumEntry(description='\n            The participant of the interaction that is going missing.\n            ',
                      tunable_type=ParticipantType,
                      default=(ParticipantType.Actor))}

    def __init__(self, interaction, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._interaction = interaction

    def should_transfer(self, continuation):
        return False

    def on_run(self):
        participant = self._interaction.get_participant(self.participant)
        participant.sim_info.household.missing_pet_tracker.run_away_succeeded(participant.sim_info)

    def release(self):
        participant = self._interaction.get_participant(self.participant)
        participant.sim_info.household.missing_pet_tracker.run_away_interaction_released(participant.sim_info)
# okay decompiling data/sims4-not-yet-decompiled/simulation/pets/missing_pets_liability.pyc
