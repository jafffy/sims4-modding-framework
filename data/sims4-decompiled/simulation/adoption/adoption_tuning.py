# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\adoption\adoption_tuning.py
# Compiled at: 2019-01-17 02:58:48
# Size of source mod 2**32: 1082 bytes
from sims.sim_info_types import Age, Gender, SpeciesExtended
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry

class _AdoptionSimData(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'age':TunableEnumEntry(description="\n            The adopted Sim's age.\n            ",
       tunable_type=Age,
       default=Age.BABY), 
     'gender':TunableEnumEntry(description="\n            The adopted Sim's gender.\n            ",
       tunable_type=Gender,
       default=Gender.FEMALE), 
     'species':TunableEnumEntry(description="\n            The adopted Sim's species.\n            ",
       tunable_type=SpeciesExtended,
       default=SpeciesExtended.HUMAN,
       invalid_enums=(
      SpeciesExtended.INVALID,))}
# okay decompiling data/sims4-not-yet-decompiled/simulation/adoption/adoption_tuning.pyc
