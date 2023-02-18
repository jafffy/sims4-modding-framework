# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\occult\occult_commands.py
# Compiled at: 2017-01-09 23:09:01
# Size of source mod 2**32: 3189 bytes
from server_commands.argument_helpers import get_optional_target, OptionalTargetParam
from sims.occult.occult_enums import OccultType
from sims4.commands import CommandType
import sims4.commands

@sims4.commands.Command('occult.add_occult', command_type=(CommandType.Automation))
def add_occult_type(occult_type: str, sim_id: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(sim_id, _connection)
    if sim is not None:
        try:
            occult_type = OccultType(occult_type)
        except ValueError:
            sims4.commands.output('{} is not a valid occult type. Valid options: {}'.format(occult_type, ', '.join(OccultType.names)), _connection)
            return False
        else:
            occult_tracker = sim.sim_info.occult_tracker
            occult_tracker.add_occult_type(occult_type)
            return True
    return False


@sims4.commands.Command('occult.remove_occult')
def remove_occult_type(occult_type: str, sim_id: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(sim_id, _connection)
    if sim is not None:
        try:
            occult_type = OccultType(occult_type)
        except ValueError:
            sims4.commands.output('{} is not a valid occult type. Valid options: {}'.format(occult_type, ', '.join(OccultType.names)), _connection)
            return False
        else:
            occult_tracker = sim.sim_info.occult_tracker
            occult_tracker.remove_occult_type(occult_type)
            return True
    return False


@sims4.commands.Command('occult.switch_to_occult')
def switch_to_occult_type(occult_type: str, sim_id: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(sim_id, _connection)
    if sim is not None:
        try:
            occult_type = OccultType(occult_type)
        except ValueError:
            sims4.commands.output('{} is not a valid occult type. Valid options: {}'.format(occult_type, ', '.join(OccultType.names)), _connection)
            return False
        else:
            occult_tracker = sim.sim_info.occult_tracker
            occult_tracker.switch_to_occult_type(occult_type)
            return True
    return False


@sims4.commands.Command('occult.occult_form_available', command_type=(CommandType.Automation))
def occult_form_available(sim_id: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(sim_id, _connection)
    if sim is not None:
        occult_tracker = sim.sim_info.occult_tracker
        is_available = occult_tracker.is_occult_form_available
        sims4.commands.automation_output('OccultFormAvailable; Available:{}'.format(is_available), _connection)
        return True
    return False
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/occult/occult_commands.pyc
