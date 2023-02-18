# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\venues\secret_lab_venue\secret_lab_commands.py
# Compiled at: 2018-11-26 18:43:38
# Size of source mod 2**32: 1358 bytes
from sims4.commands import CommandType
from venues.secret_lab_venue.secret_lab_zone_director import SecretLabCommand
import services, sims4.commands

@sims4.commands.Command('secret_lab.reveal_next_section', command_type=(sims4.commands.CommandType.Automation))
def reveal_next_section(_connection=None):
    zone_director = services.venue_service().get_zone_director()
    zone_director.handle_command(SecretLabCommand.RevealNextSection)


@sims4.commands.Command('secret_lab.reveal_all_sections', command_type=(sims4.commands.CommandType.Automation))
def reveal_all_sections(_connection=None):
    zone_director = services.venue_service().get_zone_director()
    zone_director.handle_command(SecretLabCommand.RevealAllSections)


@sims4.commands.Command('secret_lab.reset_lab', command_type=(sims4.commands.CommandType.Automation))
def reset_lab(_connection=None):
    zone_director = services.venue_service().get_zone_director()
    zone_director.handle_command(SecretLabCommand.ResetLab)
# okay decompiling data/sims4-not-yet-decompiled/simulation/venues/secret_lab_venue/secret_lab_commands.pyc
