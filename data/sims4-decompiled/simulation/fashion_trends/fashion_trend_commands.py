# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\fashion_trends\fashion_trend_commands.py
# Compiled at: 2022-04-12 23:40:51
# Size of source mod 2**32: 733 bytes
import sims4.commands
from sims4.common import Pack
import services

@sims4.commands.Command('fashion_trends.refresh_thrift_store_inventory', pack=(Pack.EP12), command_type=(sims4.commands.CommandType.DebugOnly))
def fashion_trends_refresh_thrift_store(_connection=None):
    fashion_trend_service = services.fashion_trend_service()
    if fashion_trend_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return
    fashion_trend_service.debug_randomize_thrift_store_inventory()
# okay decompiling data/sims4-not-yet-decompiled/simulation/fashion_trends/fashion_trend_commands.pyc
