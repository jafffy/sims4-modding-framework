# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\body_type_level\body_type_level_commands.py
# Compiled at: 2021-11-24 18:28:53
# Size of source mod 2**32: 487 bytes
import services, sims4
from sims4.common import Pack

@sims4.commands.Command('body_type_level.set_acne_enabled', pack=(Pack.EP12), command_type=(sims4.commands.CommandType.Live))
def set_acne_enabled(enabled: bool=True, _connection=None):
    services.sim_info_manager().set_acne_enabled(enabled)
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/body_type_level/body_type_level_commands.pyc
