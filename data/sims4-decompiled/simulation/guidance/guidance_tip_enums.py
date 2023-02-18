# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\guidance\guidance_tip_enums.py
# Compiled at: 2022-07-27 18:26:10
# Size of source mod 2**32: 1484 bytes
import enum

class GuidanceTipPlatformFilter(enum.Int):
    ALL_PLATFORMS = 0
    DESKTOP_ONLY = 1
    CONSOLE_ONLY = 2


class GuidanceTipGameState(enum.Int):
    GAMESTATE_NONE = 0
    LIVE_MODE = 270579719
    BUILD_BUY = 2919482169
    CAS = 983016380
    NEIGHBORHOOD_VIEW = 3640749201
    GALLERY = 1
    TRAVEL = 238138433
    MAIN_MENU = 1273744144


class GuidanceTipGroupConditionType(enum.Int):
    AND = 0
    OR = 1


class GuidanceTipRuleBoolen(enum.Int):
    NEVER = 0
    ALWAYS = 1


class GuidanceTipMode(enum.Int):
    DISABLED = 0
    STANDARD = 1


class GuidanceTipOptionType(enum.Int):
    STANDARD = 0
    EXPANDED = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/guidance/guidance_tip_enums.pyc
