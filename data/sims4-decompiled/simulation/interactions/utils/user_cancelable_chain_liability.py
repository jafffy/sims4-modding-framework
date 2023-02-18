# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\user_cancelable_chain_liability.py
# Compiled at: 2016-08-18 23:31:48
# Size of source mod 2**32: 2199 bytes
from interactions.liability import ReplaceableLiability
from sims4.tuning.tunable import AutoFactoryInit, HasTunableFactory
import sims4
logger = sims4.log.Logger('UserCancelableChainLiability')

class UserCancel:

    def __init__(self):
        self.requested = False


class UserCancelableChainLiability(ReplaceableLiability, HasTunableFactory, AutoFactoryInit):
    LIABILITY_TOKEN = 'UserCancelableChainLiability'

    def __init__(self, interaction, **kwargs):
        (super().__init__)(**kwargs)
        self._user_cancel = UserCancel()

    def merge(self, interaction, key, new_liability):
        interaction.remove_liability(key)
        new_liability._user_cancel = self._user_cancel
        return new_liability

    @property
    def was_user_cancel_requested(self):
        return self._user_cancel.requested

    def set_user_cancel_requested(self):
        self._user_cancel.requested = True

    def gsi_text(self):
        return str.format('{} : user_cancel.requested={}', super().gsi_text(), self._user_cancel.requested)
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/utils/user_cancelable_chain_liability.pyc
