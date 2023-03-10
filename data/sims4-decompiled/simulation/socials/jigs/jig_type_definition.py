# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\socials\jigs\jig_type_definition.py
# Compiled at: 2021-03-16 17:16:31
# Size of source mod 2**32: 3361 bytes
from interactions.utils.routing import fgl_and_get_two_person_transforms_for_jig
from routing import FootprintType
from sims4.geometry import PolygonFootprint
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableReference, OptionalTunable, TunableRange, TunableTuple
import placement, services

class SocialJigFromDefinition(AutoFactoryInit, HasTunableSingletonFactory):
    FACTORY_TUNABLES = {'jig_definition':TunableReference(description='\n            The jig to use for finding a place to do the social.\n            ',
       manager=services.definition_manager()), 
     'override_polygon_and_cost':OptionalTunable(description='\n            If disabled, uses a CompoundPolygon of the object as footprint polygon. \n            If enabled, uses the largest placement polygon of the object as footprint\n            polygon. Then we will be able to add footprint cost to the polygon. This \n            can be used to discourage other sims from entering this area.\n            ',
       tunable=TunableTuple(footprint_cost=TunableRange(description='\n                    Footprint cost of the jig, this can be used to discourage/block other\n                    sims from entering this area.\n                    ',
       tunable_type=int,
       default=20,
       minimum=1)))}

    def get_transforms_gen(self, actor, target, actor_slot_index=0, target_slot_index=1, fallback_routing_surface=None, fgl_kwargs=None, **kwargs):
        fgl_kwargs = fgl_kwargs if fgl_kwargs is not None else {}
        actor_transform, target_transform, routing_surface = fgl_and_get_two_person_transforms_for_jig(self.jig_definition, actor, actor_slot_index, target, target_slot_index, fallback_routing_surface=fallback_routing_surface, **fgl_kwargs)
        yield (actor_transform, target_transform, routing_surface, ())

    def get_footprint_polygon(self, sim_a, sim_b, sim_a_transform, sim_b_transform, routing_surface):
        if self.override_polygon_and_cost is not None:
            polygon = placement.get_placement_footprint_polygon(sim_b_transform.translation, sim_b_transform.orientation, routing_surface, self.jig_definition.get_footprint(0))
            return PolygonFootprint(polygon, routing_surface=routing_surface, cost=(self.override_polygon_and_cost.footprint_cost), footprint_type=(FootprintType.FOOTPRINT_TYPE_PATH),
              enabled=True)
        return placement.get_placement_footprint_compound_polygon(sim_b_transform.translation, sim_b_transform.orientation, routing_surface, self.jig_definition.get_footprint(0))
# okay decompiling data/sims4-not-yet-decompiled/simulation/socials/jigs/jig_type_definition.pyc
