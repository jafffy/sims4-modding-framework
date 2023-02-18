# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\crafting\food_restrictions_utils.py
# Compiled at: 2021-02-22 17:43:26
# Size of source mod 2**32: 576 bytes
import services, sims4
from sims4.localization import TunableLocalizedStringFactory
from sims4.tuning.dynamic_enum import DynamicEnum
from sims4.tuning.tunable import TunableReference, TunableEnumEntry, TunableMapping
logger = sims4.log.Logger('Food Restrictions')

class FoodRestrictionUtils:

    class FoodRestrictionEnum(DynamicEnum):
        INVALID = 0
# okay decompiling data/sims4-not-yet-decompiled/simulation/crafting/food_restrictions_utils.pyc
