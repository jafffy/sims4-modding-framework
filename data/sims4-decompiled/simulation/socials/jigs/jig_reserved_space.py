# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\socials\jigs\jig_reserved_space.py
# Compiled at: 2019-01-17 03:03:11
# Size of source mod 2**32: 2010 bytes
from sims.sim_info_types import Species
from sims4.tuning.tunable import TunableMapping, TunableEnumEntry, TunableTuple, Tunable

class TunableReservedSpacePerSpecies(TunableMapping):

    def __init__(self, **kwargs):
        (super().__init__)(key_type=TunableEnumEntry(description='\n                Species these reserved spaces are intended for.\n                ',
  tunable_type=Species,
  default=(Species.HUMAN),
  invalid_enums=(
 Species.INVALID,)), 
         value_type=TunableReservedSpace(), **kwargs)


class TunableReservedSpace(TunableTuple):

    def __init__(self, **kwargs):
        (super().__init__)(front=Tunable(description='\n                Space to be reserved in front of the actor.\n                ',
  tunable_type=float,
  default=1.0), 
         back=Tunable(description='\n                Space to be reserved in back of the actor.\n                ',
  tunable_type=float,
  default=1.0), 
         left=Tunable(description='\n                Space to be reserved to the left of the actor.\n                ',
  tunable_type=float,
  default=1.0), 
         right=Tunable(description='\n                Space to be reserved to the right of the actor.\n                ',
  tunable_type=float,
  default=1.0), **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/socials/jigs/jig_reserved_space.pyc
