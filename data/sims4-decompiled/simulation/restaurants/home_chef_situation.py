# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\restaurants\home_chef_situation.py
# Compiled at: 2016-03-17 02:34:00
# Size of source mod 2**32: 1407 bytes
from distributor.system import Distributor
from restaurants import restaurant_utils, restaurant_ui
from restaurants.chef_situation import ChefSituation
from restaurants.restaurant_tuning import MenuPresets, RestaurantTuning
from sims4.tuning.tunable import TunableEnumEntry
HOME_CHEF_GROUP = 'HomeChef'

class HomeChefSituation(ChefSituation):
    INSTANCE_TUNABLES = {'menu_preset': TunableEnumEntry(description='\n            The MenuPreset that this Chef should use.\n            ',
                      tunable_type=MenuPresets,
                      default=(MenuPresets.CUSTOMIZE),
                      invalid_enums=(
                     MenuPresets.CUSTOMIZE,),
                      tuning_group=HOME_CHEF_GROUP)}

    def show_menu(self, sim):
        menu_items = RestaurantTuning.MENU_PRESETS[self.menu_preset].recipe_map.items()
        show_menu_message = restaurant_utils.get_menu_message(menu_items, (
         sim.id,),
          chef_order=True)
        Distributor.instance().add_op_with_no_owner(restaurant_ui.ShowMenu(show_menu_message))
# okay decompiling data/sims4-not-yet-decompiled/simulation/restaurants/home_chef_situation.pyc
