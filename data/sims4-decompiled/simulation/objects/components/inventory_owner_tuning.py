# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\inventory_owner_tuning.py
# Compiled at: 2015-02-14 23:12:46
# Size of source mod 2**32: 521 bytes
from objects.components.state import TunableStateValueReference
from sims4.tuning.tunable import TunableList

class InventoryTuning:
    INVALID_ACCESS_STATES = TunableList(TunableStateValueReference(description='\n        If an inventory owner is in any of the states tuned here, it will not\n        be available to grab objects out of.\n        ',
      pack_safe=True))
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/inventory_owner_tuning.pyc
