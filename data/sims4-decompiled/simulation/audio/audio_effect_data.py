# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\audio\audio_effect_data.py
# Compiled at: 2018-07-17 01:27:57
# Size of source mod 2**32: 859 bytes


class AudioEffectData:

    def __init__(self, effect_id, track_flags=None):
        self._effect_id = effect_id
        self._track_flags = track_flags

    @property
    def effect_id(self):
        return self._effect_id

    @property
    def track_flags(self):
        return self._track_flags
# okay decompiling data/sims4-not-yet-decompiled/simulation/audio/audio_effect_data.pyc
