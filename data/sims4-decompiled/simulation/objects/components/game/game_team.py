# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\game\game_team.py
# Compiled at: 2019-04-02 19:04:19
# Size of source mod 2**32: 1358 bytes
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory

class GameTeam(HasTunableSingletonFactory, AutoFactoryInit):

    def add_player(self, game, sim):
        raise NotImplementedError

    def can_be_on_same_team(self, target_a, target_b):
        return True

    def team_determines_part(self):
        return True

    def can_be_on_opposing_team(self, target_a, target_b):
        return True

    def remove_player(self, game, sim):
        raise NotImplementedError
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/game/game_team.pyc
