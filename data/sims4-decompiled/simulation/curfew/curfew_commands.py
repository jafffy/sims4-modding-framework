# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\curfew\curfew_commands.py
# Compiled at: 2017-02-02 22:18:28
# Size of source mod 2**32: 1164 bytes
from singletons import DEFAULT
import services, sims4

@sims4.commands.Command('curfew.set_curfew', command_type=(sims4.commands.CommandType.Live))
def set_curfew(time: int, zone_id=DEFAULT, _connection=None):
    if zone_id is DEFAULT:
        zone_id = services.current_zone_id()
    curfew_service = services.get_curfew_service()
    curfew_service.set_zone_curfew(zone_id, time)


@sims4.commands.Command('curfew.print_zones_curfew', command_type=(sims4.commands.CommandType.Live))
def print_zones_curfew(zone_id=DEFAULT, _connection=None):
    if zone_id is DEFAULT:
        zone_id = services.current_zone_id()
    curfew_service = services.get_curfew_service()
    curfew_setting = curfew_service.get_zone_curfew(zone_id)
    sims4.commands.output('The curfew setting for zone {} is {}'.format(zone_id, curfew_setting), _connection)
# okay decompiling data/sims4-not-yet-decompiled/simulation/curfew/curfew_commands.pyc
