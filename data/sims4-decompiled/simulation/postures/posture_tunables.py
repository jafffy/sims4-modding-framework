# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\postures\posture_tunables.py
# Compiled at: 2016-02-19 00:17:07
# Size of source mod 2**32: 2003 bytes
from postures.posture_cost import TunablePostureCostVariant
from postures.posture_validators import TunablePostureValidatorVariant
from sims4.tuning.tunable import OptionalTunable, TunableTuple, TunableList

class TunableSupportedPostureTransitionData(OptionalTunable):

    def __init__(self, *args, **kwargs):
        (super().__init__)(args, tunable=TunableTuple(cost=(TunablePostureCostVariant()),
  validators=TunableList(description='\n                    Define under what circumstances this transition is valid.\n                    There are performance implications of adding tested edges to\n                    the posture graph. \n                    \n                    In general, this should be handled by testing posture-\n                    providing interactions altogether. This should really only\n                    be used to restrict the ability to go from a specific\n                    posture to another specific posture under certain\n                    circumstances.\n                    \n                    e.g. Prevent Squeamish Sims from sitting on dirty toilets.\n                     * Do not use this tuning. Instead, test out the interaction\n                     directly.\n                     \n                    e.g. Prevent Toddlers with low motor skill from entering the\n                    High Chair posture from stand. However, allow them to be\n                    placed on the High Chair from carry.\n                     * Use this tuning.\n                    ',
  tunable=(TunablePostureValidatorVariant()))), 
         enabled_by_default=True, **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/postures/posture_tunables.pyc
