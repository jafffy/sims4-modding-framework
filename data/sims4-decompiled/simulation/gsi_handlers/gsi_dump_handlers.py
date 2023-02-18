# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gsi_handlers\gsi_dump_handlers.py
# Compiled at: 2015-01-28 01:20:32
# Size of source mod 2**32: 1167 bytes
from gsi_handlers.gameplay_archiver import GameplayArchiver
from sims4.gsi.schema import GsiGridSchema
from sims4.log import generate_message_with_callstack
import services
gsi_dump_schema = GsiGridSchema(label='GSI Dump Log')
gsi_dump_schema.add_field('game_time', label='Game Time')
gsi_dump_schema.add_field('gsi_filename', label='Filename')
gsi_dump_schema.add_field('error_log_or_exception', label='Error', width=4)
gsi_dump_schema.add_field('callstack', label='Callstack', width=4)
gsi_dump_archiver = GameplayArchiver('gsi_dump_log', gsi_dump_schema, add_to_archive_enable_functions=True)

def archive_gsi_dump(filename_str, error_str):
    callstack = generate_message_with_callstack('GSI Dump')
    archive_data = {'game_time':str(services.time_service().sim_now),  'gsi_filename':filename_str, 
     'error_log_or_exception':error_str, 
     'callstack':callstack}
    gsi_dump_archiver.archive(data=archive_data)
# okay decompiling data/sims4-not-yet-decompiled/simulation/gsi_handlers/gsi_dump_handlers.pyc
