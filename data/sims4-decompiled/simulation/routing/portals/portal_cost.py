# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\portals\portal_cost.py
# Compiled at: 2017-10-12 00:00:35
# Size of source mod 2**32: 1719 bytes
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableRange, TunableVariant

class PortalCostTraversalLength(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'multiplier': TunableRange(tunable_type=float,
                     default=1,
                     minimum=0)}

    def __call__(self, start, end):
        if self.multiplier == 1:
            return -1
        cost = (start.position - end.position).magnitude() * self.multiplier
        return cost


class PortalCostFixed(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'cost': TunableRange(tunable_type=float,
               default=1,
               minimum=0,
               maximum=9999)}

    def __call__(self, *_, **__):
        return self.cost


class TunablePortalCostVariant(TunableVariant):

    def __init__(self, *args, **kwargs):
        return (super().__init__)(args, traversal_length=PortalCostTraversalLength.TunableFactory(), 
         fixed_cost=PortalCostFixed.TunableFactory(), 
         default='traversal_length', **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/portals/portal_cost.pyc
