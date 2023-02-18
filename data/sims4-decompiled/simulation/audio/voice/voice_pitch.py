# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\audio\voice\voice_pitch.py
# Compiled at: 2016-02-25 23:01:08
# Size of source mod 2**32: 2354 bytes
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, Tunable
import sims4.log
logger = sims4.log.Logger('VoicePitch', default_owner='rmccord')

class VoicePitchModifier(HasTunableFactory, AutoFactoryInit):

    @staticmethod
    def _verify_tunable_callback(instance_class, tunable_name, source, pitch_modifier=None, pitch_multiplier=None):
        if pitch_multiplier == 1.0:
            if pitch_modifier == 0.0:
                logger.error('Pitch Multiplier and Adder for {} in {} is set to do nothing.', instance_class, source, owner='rmccord')

    FACTORY_TUNABLES = {'pitch_modifier':Tunable(description="\n            An additive modifier for the Sim's pitch to override it.\n            ",
       default=0.0,
       tunable_type=float), 
     'pitch_multiplier':Tunable(description="\n            A multiplier for the Sim's pitch to override it.\n            ",
       default=1.0,
       tunable_type=float), 
     'verify_tunable_callback':_verify_tunable_callback}

    def __init__(self, target, **kwargs):
        (super().__init__)(**kwargs)
        self.target = target
        self.expected_override = None

    def start(self):
        if self.target.is_sim:
            if self.target.voice_pitch_override is not None:
                logger.warn('Applying multiple voice pitch overrides for {} which will override previous overrides.', (self.target), owner='rmccord')
            self.expected_override = self.target.sim_info.voice_pitch * self.pitch_multiplier + self.pitch_modifier
            self.target.voice_pitch_override = self.expected_override

    def stop(self, *_, **__):
        if self.target.is_sim:
            if self.expected_override is None or self.target.voice_pitch_override == self.expected_override:
                self.target.voice_pitch_override = None
# okay decompiling data/sims4-not-yet-decompiled/simulation/audio/voice/voice_pitch.pyc
