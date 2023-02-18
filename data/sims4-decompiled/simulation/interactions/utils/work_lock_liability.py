# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\work_lock_liability.py
# Compiled at: 2016-11-09 19:43:03
# Size of source mod 2**32: 1026 bytes
from interactions.liability import Liability

class WorkLockLiability(Liability):
    LIABILITY_TOKEN = 'MasterControllerLockLiability'

    def __init__(self, *args, sim, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._sim = sim

    def on_add(self, interaction):
        self._sim.add_work_lock(self)

    def merge(self, interaction, key, new_liability):
        self.release()
        return super().merge(interaction, key, new_liability)

    def release(self):
        self._sim.remove_work_lock(self)
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/utils/work_lock_liability.pyc
