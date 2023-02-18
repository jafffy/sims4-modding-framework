# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\calendar_commands.py
# Compiled at: 2021-06-07 23:47:06
# Size of source mod 2**32: 610 bytes
from server_commands.argument_helpers import TunableInstanceParam
import sims4.commands, services

@sims4.commands.Command('calendar.set_favorite_calendar_entry', command_type=(sims4.commands.CommandType.Live))
def set_favorite_calendar_entry(event_id: int, is_favorite: bool=False, _connection=None):
    services.calendar_service().set_favorited_calendar_entry(event_id, is_favorite)
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/calendar_commands.pyc
