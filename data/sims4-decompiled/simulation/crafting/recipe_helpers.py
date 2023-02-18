# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\crafting\recipe_helpers.py
# Compiled at: 2021-08-23 17:23:11
# Size of source mod 2**32: 642 bytes
from _collections import defaultdict
import services, sims4
with sims4.reload.protected(globals()):
    RECIPE_TAG_TO_TUNING_ID_MAP = defaultdict(set)

def get_recipes_matching_tag(tag):
    manager = services.get_instance_manager(sims4.resources.Types.RECIPE)
    recipe_guids = RECIPE_TAG_TO_TUNING_ID_MAP.get(tag)
    if recipe_guids:
        return list((manager.get(recipe_guid) for recipe_guid in recipe_guids))
    return []
# okay decompiling data/sims4-not-yet-decompiled/simulation/crafting/recipe_helpers.pyc
