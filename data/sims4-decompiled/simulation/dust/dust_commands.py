# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\dust\dust_commands.py
# Compiled at: 2022-10-03 20:00:14
# Size of source mod 2**32: 984 bytes
import services, sims4
from event_testing.game_option_tests import TestableGameOptions
from event_testing.test_events import TestEvent
from sims4.common import Pack

@sims4.commands.Command('dust.set_dust_enabled', pack=(Pack.SP22), command_type=(sims4.commands.CommandType.Live))
def set_dust_enabled(enabled: bool=True, _connection=None):
    dust_service = services.dust_service()
    if dust_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return False
    dust_service.set_enabled(enabled)
    services.get_event_manager().process_event((TestEvent.TestedGameOptionChanged), custom_keys=(
     TestableGameOptions.DUST_SYSTEM_ENABLED,))
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/dust/dust_commands.pyc
