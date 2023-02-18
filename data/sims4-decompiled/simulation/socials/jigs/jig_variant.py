# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\socials\jigs\jig_variant.py
# Compiled at: 2017-03-10 20:36:03
# Size of source mod 2**32: 919 bytes
from sims4.tuning.tunable import TunableVariant
from socials.jigs.jig_type_animation import SocialJigAnimation
from socials.jigs.jig_type_definition import SocialJigFromDefinition
from socials.jigs.jig_type_explicit import SocialJigExplicit
from socials.jigs.jig_type_legacy import SocialJigLegacy

class TunableJigVariant(TunableVariant):

    def __init__(self, **kwargs):
        (super().__init__)(definition=SocialJigFromDefinition.TunableFactory(), 
         explicit=SocialJigExplicit.TunableFactory(), 
         legacy=SocialJigLegacy.TunableFactory(), 
         animation=SocialJigAnimation.TunableFactory(), 
         default='definition', **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/socials/jigs/jig_variant.pyc
