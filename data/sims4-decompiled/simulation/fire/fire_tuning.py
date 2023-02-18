# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\fire\fire_tuning.py
# Compiled at: 2017-04-21 19:24:14
# Size of source mod 2**32: 551 bytes
from sims4.tuning.tunable import TunableEnumWithFilter
from tag import Tag

class FireTuning:
    FLAMMABLE_TAG = TunableEnumWithFilter(description='\n        Define a tag that is automatically added to all objects that are\n        flammable.\n        ',
      tunable_type=Tag,
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      filter_prefixes=('Fire', ))
# okay decompiling data/sims4-not-yet-decompiled/simulation/fire/fire_tuning.pyc
