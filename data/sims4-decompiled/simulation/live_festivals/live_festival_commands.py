# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\live_festivals\live_festival_commands.py
# Compiled at: 2021-06-30 21:48:18
# Size of source mod 2**32: 2270 bytes
import services, sims4.commands, world
from live_events.live_event_service import LiveEventType
from live_festivals import live_festival_tuning

@sims4.commands.Command('live_festival.close_businesses_in_live_festival_street', command_type=(sims4.commands.CommandType.Live))
def close_businesses_in_live_festival_street(_connection=None):
    live_event_service = services.get_live_event_service()
    if live_event_service is None:
        sims4.commands.output('Live Event service not loaded.', _connection)
        return False
    active_unique_festival = live_event_service.get_current_unique_live_event_of_type(LiveEventType.LIVE_FESTIVAL)
    if active_unique_festival is None:
        sims4.commands.output('There is no active live festival.', _connection)
        return False
    if active_unique_festival not in live_festival_tuning.LiveFestivalTuning.LIVE_FESTIVAL_EVENT_DATA:
        sims4.commands.output('Live festival {} does not have its tuning set in LiveFestivalTuning.'.format(active_unique_festival), _connection)
        return False
    festival_tuning = live_festival_tuning.LiveFestivalTuning.LIVE_FESTIVAL_EVENT_DATA[active_unique_festival]
    festival_street_instance = world.street.Street.WORLD_DESCRIPTION_TUNING_MAP.get(festival_tuning.street, None)
    zone_ids = world.street.get_zone_ids_from_street(festival_street_instance)
    if zone_ids is not None:
        business_service = services.business_service()
        for zone_id in zone_ids:
            business_manager = business_service.get_business_manager_for_zone(zone_id=zone_id)
            is_open_business = business_manager.is_open if business_manager is not None else False
            if is_open_business:
                business_manager.set_open(False)

    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/live_festivals/live_festival_commands.pyc
