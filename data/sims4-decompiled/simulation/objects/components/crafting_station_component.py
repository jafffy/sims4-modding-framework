# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\crafting_station_component.py
# Compiled at: 2021-07-16 01:59:23
# Size of source mod 2**32: 8972 bytes
from objects.components import Component, types
from sims4.tuning.tunable import HasTunableFactory, TunableReference, Tunable, TunableList
import services, sims4.resources
from objects.components import componentmethod_with_fallback
from collections import Counter

class CraftingStationComponent(Component, HasTunableFactory, component_name=types.CRAFTING_STATION_COMPONENT):
    FACTORY_TUNABLES = {'crafting_station_types':TunableList(description='\n            Crafting Object Types that this object supports.\n            ',
       tunable=TunableReference(description='\n                This specifies the crafting object type that is satisfied by\n                this object.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.RECIPE)),
       class_restrictions=('CraftingObjectType', ))), 
     'children_invalidate_crafting_cache':Tunable(description="\n            If this is True, anything that is attached as a child of this\n            object will cause the crafting cache to be invalidated.  If\n            it's False, children will be ignored for the purposes of the\n            crafting cache.\n            ",
       tunable_type=bool,
       default=True)}

    def __init__(self, owner, *, crafting_station_types, children_invalidate_crafting_cache):
        super().__init__(owner)
        self.tuned_crafting_station_types = crafting_station_types
        self._children_invalidate_crafting_cache = children_invalidate_crafting_cache
        self._cached_user_directed = {}
        self._cached_for_autonomy = {}
        self._state_value_crafting_types = Counter()
        self._should_be_in_cache = True

    @property
    def crafting_station_types(self):
        return list(self.tuned_crafting_station_types) + list(self._state_value_crafting_types.keys())

    def on_add(self):
        if self.crafting_station_types:
            self.add_to_crafting_cache()
            self._add_state_changed_callback()

    def on_remove(self):
        if self.crafting_station_types:
            self.remove_from_crafting_cache()
            self._remove_state_changed_callback()

    def on_child_added(self, child, location):
        if self._children_invalidate_crafting_cache:
            if len(self.owner.children) == 1:
                self.remove_from_crafting_cache(user_directed=False)

    def on_child_removed(self, child, new_parent=None):
        if self._children_invalidate_crafting_cache:
            if len(self.owner.children) == 0:
                self.add_to_crafting_cache(user_directed=False)

    def on_added_to_inventory(self):
        self.remove_from_crafting_cache()

    def on_removed_from_inventory(self):
        self.add_to_crafting_cache()

    @componentmethod_with_fallback((lambda: None))
    def add_to_crafting_cache(self, user_directed=True, autonomy=True):
        if self.crafting_station_types:
            self._should_be_in_cache = True
            for crafting_type in self.crafting_station_types:
                self._add_crafting_type_to_cache(crafting_type, user_directed=user_directed, autonomy=autonomy)

    @componentmethod_with_fallback((lambda: None))
    def remove_from_crafting_cache(self, user_directed=True, autonomy=True):
        if self.crafting_station_types:
            self._should_be_in_cache = False
            for crafting_type in self.crafting_station_types:
                self._remove_crafting_type_from_cache(crafting_type, user_directed=user_directed, autonomy=autonomy)

    def _add_crafting_type_to_cache(self, crafting_type, user_directed=True, autonomy=True):
        user_directed &= not self._cached_user_directed.get(crafting_type, False)
        autonomy &= not self._cached_for_autonomy.get(crafting_type, False)
        services.object_manager().crafting_cache.add_type(crafting_type, user_directed=user_directed,
          autonomy=autonomy)
        if autonomy:
            self._cached_for_autonomy[crafting_type] = True
        if user_directed:
            self._cached_user_directed[crafting_type] = True

    def _remove_crafting_type_from_cache(self, crafting_type, user_directed=True, autonomy=True):
        user_directed &= self._cached_user_directed.get(crafting_type, False)
        autonomy &= self._cached_for_autonomy.get(crafting_type, False)
        services.object_manager().crafting_cache.remove_type(crafting_type, user_directed=user_directed,
          autonomy=autonomy)
        if autonomy:
            self._cached_for_autonomy[crafting_type] = False
        if user_directed:
            self._cached_user_directed[crafting_type] = False

    def _add_state_changed_callback(self):
        if self.owner.has_component(types.STATE_COMPONENT):
            self.owner.add_state_changed_callback(self._on_crafting_object_state_changed)

    def _remove_state_changed_callback(self):
        if self.owner.has_component(types.STATE_COMPONENT):
            self.owner.remove_state_changed_callback(self._on_crafting_object_state_changed)

    def _on_crafting_object_state_changed(self, owner, state, old_value, new_value):
        if (old_value.remove_from_crafting_cache or new_value).remove_from_crafting_cache:
            self._should_be_in_cache = False
            self.remove_from_crafting_cache()
        else:
            if old_value.remove_from_crafting_cache:
                if not new_value.remove_from_crafting_cache:
                    self._should_be_in_cache = True
                    self.add_to_crafting_cache()
        if old_value.crafting_types is not None:
            for crafting_type in old_value.crafting_types:
                self._state_value_crafting_types[crafting_type] -= 1
                if self._should_be_in_cache:
                    self._remove_crafting_type_from_cache(crafting_type)

        if new_value.crafting_types is not None:
            for crafting_type in new_value.crafting_types:
                self._state_value_crafting_types[crafting_type] += 1
                if self._should_be_in_cache:
                    self._add_crafting_type_to_cache(crafting_type)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/crafting_station_component.pyc
