# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\narrative\narrative_enums.py
# Compiled at: 2020-05-20 17:18:13
# Size of source mod 2**32: 2115 bytes
from sims4.tuning.dynamic_enum import DynamicEnum, DynamicEnumLocked
from weather.weather_enums import WeatherEffectType, CloudType
import enum

class NarrativeGroup(DynamicEnum, partitioned=True):
    INVALID = 0


class NarrativeEvent(DynamicEnum, partitioned=True):
    INVALID = 0


class NarrativeProgressionEvent(DynamicEnumLocked, partitioned=True):
    INVALID = 0


class NarrativeSituationShiftType(DynamicEnum, partitioned=True):
    INVALID = 0


class NarrativeEnvironmentParams(enum.Int):
    StrangerVille_Act = WeatherEffectType.STRANGERVILLE_ACT
    BatuuFactionState_RES = WeatherEffectType.STARWARS_RESISTANCE
    BatuuFactionState_FO = WeatherEffectType.STARWARS_FIRST_ORDER
    StrangerVille_Strange_Skybox = CloudType.STRANGE
    StrangerVille_VeryStrange_Skybox = CloudType.VERY_STRANGE
# okay decompiling data/sims4-not-yet-decompiled/simulation/narrative/narrative_enums.pyc
