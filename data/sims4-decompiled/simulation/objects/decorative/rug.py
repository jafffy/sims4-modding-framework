# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\decorative\rug.py
# Compiled at: 2018-09-30 23:45:12
# Size of source mod 2**32: 1004 bytes
from fire.flammability import ObjectFootprintFlammability
from objects.game_object import GameObject
from sims4.tuning.instances import lock_instance_tunables
import distributor.fields, distributor.ops

class Rug(GameObject):
    INSTANCE_TUNABLES = {'flammable_area': ObjectFootprintFlammability.TunableFactory()}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._sort_order = 0

    @distributor.fields.Field(op=(distributor.ops.SetSortOrder))
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value


lock_instance_tunables(Rug, provides_terrain_interactions=False)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/decorative/rug.pyc
