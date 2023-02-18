# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\autonomy\autonomy_liabilities.py
# Compiled at: 2017-06-08 23:33:37
# Size of source mod 2**32: 609 bytes
from interactions.liability import Liability

class AutonomousGetComfortableLiability(Liability):
    LIABILITY_TOKEN = 'AutonomousGetComfortable'

    def __init__(self, sim, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._sim = sim

    def release(self):
        self._sim.push_get_comfortable_interaction()
# okay decompiling data/sims4-not-yet-decompiled/simulation/autonomy/autonomy_liabilities.pyc
