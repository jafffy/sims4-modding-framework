# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\adoption\adoption_liability.py
# Compiled at: 2017-04-11 00:13:28
# Size of source mod 2**32: 793 bytes
from interactions.liability import Liability

class AdoptionLiability(Liability):
    LIABILITY_TOKEN = 'AdoptionLiability'

    def __init__(self, household, sim_ids, **kwargs):
        (super().__init__)(**kwargs)
        self._household = household
        self._sim_ids = sim_ids

    def on_add(self, interaction):
        for sim_id in self._sim_ids:
            self._household.add_adopting_sim(sim_id)

    def release(self):
        for sim_id in self._sim_ids:
            self._household.remove_adopting_sim(sim_id)
# okay decompiling data/sims4-not-yet-decompiled/simulation/adoption/adoption_liability.pyc
