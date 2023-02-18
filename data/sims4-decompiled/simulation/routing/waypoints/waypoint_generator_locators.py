# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\waypoints\waypoint_generator_locators.py
# Compiled at: 2020-07-22 01:38:26
# Size of source mod 2**32: 1964 bytes
from routing.waypoints.tunable_waypoint_graph import TunableWaypointGraph
from routing.waypoints.waypoint_generator import _WaypointGeneratorBase

class LocatorIdToWaypointGenerator(_WaypointGeneratorBase):

    def __init__(self, locator_ids, constraint_radius, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._locator_ids = locator_ids
        self._constraint_radius = constraint_radius
        if locator_ids:
            self._start_constraint = TunableWaypointGraph.locator_to_waypoint_constraint(locator_ids[0], constraint_radius, self._routing_surface)
        else:
            self._start_constraint = None

    def get_start_constraint(self):
        return self._start_constraint

    def get_waypoint_constraints_gen(self, routing_agent, waypoint_count):
        for locator_id in self._locator_ids:
            if waypoint_count == 0:
                return
                constraint = TunableWaypointGraph.locator_to_waypoint_constraint(locator_id, self._constraint_radius, self._routing_surface)
                if constraint is not None:
                    yield constraint
                    waypoint_count -= 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/waypoints/waypoint_generator_locators.pyc
