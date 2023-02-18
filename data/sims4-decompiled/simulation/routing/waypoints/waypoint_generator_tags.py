# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\waypoints\waypoint_generator_tags.py
# Compiled at: 2021-02-25 05:37:04
# Size of source mod 2**32: 808 bytes
from routing.waypoints.waypoint_generator_object_mixin import _WaypointGeneratorMultipleObjectMixin
from tag import TunableTags
import services

class _WaypointGeneratorMultipleObjectByTag(_WaypointGeneratorMultipleObjectMixin):
    FACTORY_TUNABLES = {'object_tags': TunableTags(description='\n            Find all of the objects based on these tags.\n            ',
                      filter_prefixes=('func', ))}

    def _get_objects(self):
        return services.object_manager().get_objects_matching_tags((self.object_tags), match_any=True)
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/waypoints/waypoint_generator_tags.pyc
