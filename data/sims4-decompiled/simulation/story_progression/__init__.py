# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\story_progression\__init__.py
# Compiled at: 2022-01-19 00:24:13
# Size of source mod 2**32: 1014 bytes
import enum

class StoryProgressionFlags(enum.IntFlags, export=False):
    DISABLED = 0
    ALLOW_POPULATION_ACTION = 1
    ALLOW_INITIAL_POPULATION = 2
    SIM_INFO_FIREMETER = 4


class StoryProgressionArcSeedReason(enum.Int, export=False):
    SYSTEM = 0
    LOOT = 1


STORY_PROGRESSION_ARC_SEED_REASON_STRINGS = {StoryProgressionArcSeedReason.SYSTEM: 'SYSTEM', 
 StoryProgressionArcSeedReason.LOOT: 'LOOT'}
# okay decompiling data/sims4-not-yet-decompiled/simulation/story_progression/__init__.pyc
