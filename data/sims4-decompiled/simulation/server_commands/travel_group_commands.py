# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\travel_group_commands.py
# Compiled at: 2021-06-09 06:08:30
# Size of source mod 2**32: 7388 bytes
from objects import ALL_HIDDEN_REASONS
import clock, services, sims4.log
logger = sims4.log.Logger('Commands')

@sims4.commands.Command('travel_groups.list')
def list_travel_groups(travel_group_id: int=None, _connection=None):
    travel_group_manager = services.travel_group_manager()
    output = sims4.commands.Output(_connection)
    output('Current Zone ID: {}'.format(services.current_zone_id()))
    output('Travel Group report:')
    if travel_group_id is not None:
        travel_groups = (
         travel_group_manager.get(travel_group_id),)
    else:
        travel_groups = travel_group_manager.get_all()
    for travel_group in travel_groups:
        output('ID: {}, {} Sims, ZoneID: {}'.format(travel_group.id, len(travel_group), travel_group.zone_id))
        for sim_info in travel_group:
            if sim_info.is_instanced(allow_hidden_flags=0):
                output('   Instanced: {}'.format(sim_info))
            elif sim_info.is_instanced(allow_hidden_flags=ALL_HIDDEN_REASONS):
                output('   Hidden: {}'.format(sim_info))
            else:
                output('   Off lot: {}'.format(sim_info))


@sims4.commands.Command('travel_groups.create')
def create_travel_group(duration: int=60, *sim_ids, _connection=None):
    output = sims4.commands.Output(_connection)
    if not sim_ids:
        output('Cannot create a travel group with 0 Sims.')
        return
    sim_info_manager = services.sim_info_manager()
    create_timestamp = services.time_service().sim_now
    end_timestamp = create_timestamp + clock.interval_in_sim_days(duration)
    sim_infos = []
    for sim_id in sim_ids:
        sim_info = sim_info_manager.get(int(sim_id, base=0))
        if sim_info is not None:
            sim_infos.append(sim_info)
        else:
            output('Cannot find Sim with id {}'.format(sim_id))

    travel_group_manager = services.travel_group_manager()
    travel_group_manager.create_travel_group_and_rent_zone(sim_infos=sim_infos, zone_id=(services.current_zone_id()), played=True, create_timestamp=create_timestamp, end_timestamp=end_timestamp)


@sims4.commands.Command('travel_groups.destroy')
def destroy_travel_group(travel_group_id: int=0, _connection=None):
    output = sims4.commands.Output(_connection)
    travel_group_manager = services.travel_group_manager()
    travel_group = travel_group_manager.get(travel_group_id)
    if travel_group is None:
        output('Please specify a valid travel group. Use |travel_groups.list to view all possible travel groups.')
        return
    travel_group_manager.destroy_travel_group_and_release_zone(travel_group)


@sims4.commands.Command('travel_groups.create_vacation', command_type=(sims4.commands.CommandType.Live))
def create_vacation(zone_id: int, duration: int=0, cost: int=0, *sim_ids, _connection=None):
    output = sims4.commands.Output(_connection)
    if not sim_ids:
        output('Cannot create a travel group with 0 Sims.')
        return
    sim_info_manager = services.sim_info_manager()
    create_timestamp = services.time_service().sim_now
    end_timestamp = create_timestamp + clock.interval_in_sim_days(duration) if duration else None
    sim_infos = []
    for sim_id in sim_ids:
        sim_info = sim_info_manager.get(int(sim_id, base=0))
        if sim_info is not None:
            sim_infos.append(sim_info)
        else:
            output('Cannot find Sim with id {}'.format(sim_id))

    travel_group_manager = services.travel_group_manager()
    travel_group_manager.create_travel_group_and_rent_zone(sim_infos=sim_infos, zone_id=zone_id, played=True, create_timestamp=create_timestamp, end_timestamp=end_timestamp, cost=cost)


@sims4.commands.Command('travel_groups.extend_vacation', command_type=(sims4.commands.CommandType.Live))
def extend_vacation(travel_group_id: int, duration_days: int=0, cost: int=0, _connection=None):
    output = sims4.commands.Output(_connection)
    travel_group_manager = services.travel_group_manager()
    travel_group = travel_group_manager.get(travel_group_id)
    if travel_group is None:
        output('Travel Group with id: {} does not exist.'.format(travel_group_id))
        return
    if travel_group.is_vacation_over and duration_days == 0:
        travel_group.end_vacation()
    else:
        travel_group.extend_vacation(duration_days, cost)


@sims4.commands.Command('travel_groups.show_extend_vacation', command_type=(sims4.commands.CommandType.Live))
def show_extend_vacation(_connection=None):
    active_sim = services.client_manager().get(_connection).active_sim
    if active_sim is None:
        return
    travel_group = active_sim.travel_group
    if travel_group is None:
        return
    travel_group.show_extend_vacation_dialog()


@sims4.commands.Command('travel_groups.end_vacation', command_type=(sims4.commands.CommandType.Live))
def end_vacation(travel_group_id: int, _connection=None):
    output = sims4.commands.Output(_connection)
    travel_group_manager = services.travel_group_manager()
    travel_group = travel_group_manager.get(travel_group_id)
    if travel_group is None:
        output('Travel Group with id: {} does not exist.'.format(travel_group_id))
        return
    travel_group.end_vacation()


@sims4.commands.Command('qa.travel_groups.end_vacation', command_type=(sims4.commands.CommandType.Automation))
def end_vacation(sim_id: int, _connection=None):
    if not sim_id:
        sims4.commands.automation_output('TravelEndVacationInfo; Status:Failed, Message:Sim Id required to end the vacation.', _connection)
        return
    sim_info_manager = services.sim_info_manager()
    sim_info = sim_info_manager.get(sim_id)
    if sim_info is None:
        sims4.commands.automation_output('TravelEndVacationInfo; Status:Failed, Message:Cannot find Sim with id {}'.format(sim_id), _connection)
    travel_group_manager = services.travel_group_manager()
    travel_group = travel_group_manager.get_travel_group_by_sim_info(sim_info)
    if travel_group is None:
        sims4.commands.automation_output('TravelEndVacationInfo; Status:Failed, Message:Travel Group does not exist with the given sim.'.format(sim_id), _connection)
        return
    travel_group.end_vacation()
    sims4.commands.automation_output('TravelEndVacationInfo; Status:Success', _connection)
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/travel_group_commands.pyc
