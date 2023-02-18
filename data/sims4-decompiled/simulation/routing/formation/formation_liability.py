# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\formation\formation_liability.py
# Compiled at: 2017-10-07 00:49:24
# Size of source mod 2**32: 727 bytes
from interactions.liability import ReplaceableLiability

class RoutingFormationLiability(ReplaceableLiability):
    LIABILITY_TOKEN = 'RoutingFormationLiability'

    def __init__(self, routing_formation_data, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._routing_formation_data = routing_formation_data

    def release(self):
        self._routing_formation_data.release_formation_data()
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/formation/formation_liability.pyc
