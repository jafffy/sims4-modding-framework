# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\audio\tunable_audio.py
# Compiled at: 2019-06-05 22:07:17
# Size of source mod 2**32: 648 bytes
from sims4.resources import Types
from sims4.tuning.tunable import TunablePackSafeResourceKey

class TunableAudioAllPacks(TunablePackSafeResourceKey):

    def __init__(self, *, description='The audio file.', **kwargs):
        (super().__init__)(None, resource_types=(Types.PROPX,), description=description, **kwargs)

    @property
    def validate_pack_safe(self):
        return False
# okay decompiling data/sims4-not-yet-decompiled/simulation/audio/tunable_audio.pyc
