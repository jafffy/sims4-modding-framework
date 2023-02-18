# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gameplay_scenarios\scenario_enums.py
# Compiled at: 2022-04-05 20:03:30
# Size of source mod 2**32: 974 bytes
import enum
from sims4.tuning.dynamic_enum import DynamicEnum

class ScenarioEntryMethod(enum.IntFlags):
    NEW_HOUSEHOLD = 1
    EXISTING_HOUSEHOLD = 2


class ScenarioProperties(enum.IntFlags):
    ONBOARDING = 1


class ScenarioCategory(DynamicEnum):
    INVALID = 0


class ScenarioDifficultyCategory(DynamicEnum):
    INVALID = 0


class ScenarioTheme(DynamicEnum):
    INVALID = 0
# okay decompiling data/sims4-not-yet-decompiled/simulation/gameplay_scenarios/scenario_enums.pyc
