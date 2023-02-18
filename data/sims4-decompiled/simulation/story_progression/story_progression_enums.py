# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\story_progression\story_progression_enums.py
# Compiled at: 2021-08-28 00:12:30
# Size of source mod 2**32: 916 bytes
import enum
from collections import namedtuple
CullImmunityInfo = namedtuple('CullImmunityInfo', ('telemetry_hook', 'gsi_reason'))

class CullingReasons:
    PLAYER = CullImmunityInfo('imsp', 'Player SimInfo')
    LIVES_IN_WORLD = CullImmunityInfo('imsw', 'Resident of some world')
    TRAIT_IMMUNE = CullImmunityInfo('imsa', 'Possess an immune trait')
    INSTANCED = CullImmunityInfo('imsn', 'Instanced in the game')
    IN_TRAVEL_GROUP = CullImmunityInfo('imst', 'Part of some travel group')
    ALL_CULLING_REASONS = [
     'PLAYER', 'LIVES_IN_WORLD', 'TRAIT_IMMUNE', 'INSTANCED', 'IN_TRAVEL_GROUP']


class StoryType(enum.Int, export=False):
    SIM_BASED = ...
    HOUSEHOLD_BASED = ...
# okay decompiling data/sims4-not-yet-decompiled/simulation/story_progression/story_progression_enums.pyc
