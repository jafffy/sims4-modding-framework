# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\object_liabilities.py
# Compiled at: 2020-01-03 19:18:04
# Size of source mod 2**32: 2345 bytes
import sims4
from interactions import ParticipantTypeObject
from interactions.liability import Liability
from sims4.tuning.tunable import TunableEnumEntry, HasTunableFactory, AutoFactoryInit
logger = sims4.log.Logger('Object Liabilities', default_owner='skorman')

class TemporaryHiddenInventoryTransferLiability(Liability, HasTunableFactory, AutoFactoryInit):
    LIABILITY_TOKEN = 'TemporaryHiddenInventoryTransferLiability'
    FACTORY_TUNABLES = {'object': TunableEnumEntry(description='\n            The object that will be temporarily moved from an inventory to its \n            associated hidden inventory.\n            ',
                 tunable_type=ParticipantTypeObject,
                 default=(ParticipantTypeObject.PickedObject))}

    def __init__(self, interaction, **kwargs):
        (super().__init__)(**kwargs)
        self._obj = interaction.get_participant(self.object)

    def should_transfer(self, continuation):
        return False

    def _return_obj(self):
        inventory = self._obj.get_inventory()
        if inventory is not None:
            inventory.try_move_hidden_object_to_inventory(self._obj)

    def on_add(self, interaction):
        if self._obj is None:
            return
        else:
            inventory = self._obj.get_inventory()
            if inventory is None:
                logger.error('Object {} is not in an inventory, so it cannot be moved to the hidden inventory', self._obj)
                return
            inventory.try_move_object_to_hidden_inventory(self._obj) or logger.error('Tried moving object {} to hidden inventory, but failed.', self._obj)

    def on_reset(self):
        self._return_obj()

    def release(self):
        self._return_obj()
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/object_liabilities.pyc
