# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\world\lot_geom_utils.py
# Compiled at: 2020-11-06 00:51:46
# Size of source mod 2**32: 1437 bytes
import build_buy, services
from plex.plex_enums import INVALID_PLEX_ID
from sims4.geometry import Polygon, random_uniform_points_in_compound_polygon, CompoundPolygon

def get_random_points_on_floor(level_index, num=1):
    plex_service = services.get_plex_service()
    plex_id = plex_service.get_active_zone_plex_id() or INVALID_PLEX_ID
    polygons = []
    for poly_data, block_level_index in build_buy.get_all_block_polygons(plex_id).values():
        if block_level_index != level_index:
            continue
        for p in poly_data:
            polygon = Polygon(list(reversed(p)))
            polygon.normalize()
            if polygon.area() <= 0:
                continue
            polygons.append(polygon)

    if not polygons:
        return
    return random_uniform_points_in_compound_polygon((CompoundPolygon(polygons)), num=num)
# okay decompiling data/sims4-not-yet-decompiled/simulation/world/lot_geom_utils.pyc
