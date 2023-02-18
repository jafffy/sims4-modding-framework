# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\__init__.py
# Compiled at: 2022-08-31 21:10:30
# Size of source mod 2**32: 985 bytes
from sims4.commands import CommandType
import paths, services, sims4.commands

def is_command_available(command_type: CommandType):
    if command_type >= CommandType.Live:
        return True
    else:
        if command_type >= CommandType.Cheat:
            cheat_service = services.get_cheat_service()
            cheats_enabled = cheat_service.cheats_enabled
            if cheats_enabled:
                return True
        if command_type >= CommandType.Automation and paths.AUTOMATION_MODE:
            return True
    return False


sims4.commands.is_command_available = is_command_available
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/__init__.pyc
