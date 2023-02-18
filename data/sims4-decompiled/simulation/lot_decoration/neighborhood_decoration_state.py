# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lot_decoration\neighborhood_decoration_state.py
# Compiled at: 2018-01-26 01:37:58
# Size of source mod 2**32: 944 bytes
from lot_decoration.decoratable_lot import DecoratableLot

class NeighborhoodDecorationState:

    def __init__(self, world_id, zone_datas):
        self._zone_to_lot_decoration_data = {}
        self._world_id = world_id
        for lot_info in zone_datas:
            self._zone_to_lot_decoration_data[lot_info.zone_id] = DecoratableLot(lot_info)

    @property
    def lots(self):
        return self._zone_to_lot_decoration_data.values()

    @property
    def world_id(self):
        return self._world_id

    def get_deco_lot_by_zone_id(self, zone_id):
        return self._zone_to_lot_decoration_data[zone_id]
# okay decompiling data/sims4-not-yet-decompiled/simulation/lot_decoration/neighborhood_decoration_state.pyc
