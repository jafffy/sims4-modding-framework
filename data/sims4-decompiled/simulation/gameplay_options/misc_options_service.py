# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gameplay_options\misc_options_service.py
# Compiled at: 2022-03-10 00:58:13
# Size of source mod 2**32: 1834 bytes
from sims4.service_manager import Service

class MiscOptionsService(Service):

    def __init__(self):
        self._restrict_npc_werewolves = False
        self._npc_relationship_autonomy_enabled = True

    def save_options(self, options_proto):
        options_proto.restrict_npc_werewolves = self._restrict_npc_werewolves
        options_proto.npc_relationship_autonomy_enabled = self._npc_relationship_autonomy_enabled

    def load_options(self, options_proto):
        self._restrict_npc_werewolves = options_proto.restrict_npc_werewolves
        self._npc_relationship_autonomy_enabled = options_proto.npc_relationship_autonomy_enabled

    @property
    def restrict_npc_werewolves(self):
        return self._restrict_npc_werewolves

    def set_restrict_npc_werewolves(self, enabled: bool):
        self._restrict_npc_werewolves = enabled

    @property
    def npc_relationship_autonomy_enabled(self):
        return self._npc_relationship_autonomy_enabled

    def set_npc_relationship_autonomy_enabled(self, enabled: bool):
        self._npc_relationship_autonomy_enabled = enabled
# okay decompiling data/sims4-not-yet-decompiled/simulation/gameplay_options/misc_options_service.pyc
