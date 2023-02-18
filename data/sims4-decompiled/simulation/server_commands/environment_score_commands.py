# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\environment_score_commands.py
# Compiled at: 2014-06-05 18:17:21
# Size of source mod 2**32: 781 bytes
import sims4.commands
from broadcasters.environment_score import environment_score_mixin

@sims4.commands.Command('environment_score.enable')
def environment_score_enable(_connection=None):
    environment_score_mixin.environment_score_enabled = True


@sims4.commands.Command('environment_score.disable')
def environment_score_disable(_connection=None):
    environment_score_mixin.environment_score_enabled = False
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/environment_score_commands.pyc
