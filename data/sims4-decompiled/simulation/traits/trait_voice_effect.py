# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\traits\trait_voice_effect.py
# Compiled at: 2016-03-18 00:22:56
# Size of source mod 2**32: 1283 bytes
from sims4.tuning.dynamic_enum import DynamicEnum
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableEnumEntry
from sims4.tuning.tunable_hash import TunableStringHash64

class VoiceEffectRequestPriority(DynamicEnum):
    INVALID = 0


class VoiceEffectRequest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'voice_effect':TunableStringHash64(description='\n            When set, this voice effect will be applied to the Sim when the\n            trait is added and removed when the trait is removed.\n            '), 
     'priority':TunableEnumEntry(description='\n            The requests priority.\n            ',
       tunable_type=VoiceEffectRequestPriority,
       default=VoiceEffectRequestPriority.INVALID)}
# okay decompiling data/sims4-not-yet-decompiled/simulation/traits/trait_voice_effect.pyc
