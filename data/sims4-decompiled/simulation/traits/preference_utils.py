# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\traits\preference_utils.py
# Compiled at: 2021-07-13 10:54:00
# Size of source mod 2**32: 701 bytes
import services, sims4.resources
from traits.preference_enums import PreferenceTypes

def preferences_gen():
    trait_manager = services.get_instance_manager(sims4.resources.Types.TRAIT)
    if trait_manager is None:
        return
    for trait in trait_manager.types.values():
        if trait.is_preference_trait:
            yield trait


def get_preferences_by_category(category):
    return [p for p in preferences_gen() if p.preference_category is category]
# okay decompiling data/sims4-not-yet-decompiled/simulation/traits/preference_utils.pyc
