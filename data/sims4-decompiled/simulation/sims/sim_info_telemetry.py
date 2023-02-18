# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\sim_info_telemetry.py
# Compiled at: 2016-06-24 00:40:23
# Size of source mod 2**32: 2897 bytes
import alarms, clock, services, sims4, telemetry_helper
TELEMETRY_GROUP_STORY_PROGRESSION = 'STRY'
TELEMETRY_HOOK_SIMINFO_DAILY_COUNT = 'SIDC'
daily_sim_info_creation_COUNT_TIME_OF_DAY = 3
writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_STORY_PROGRESSION)

class SimInfoTelemetryManager:

    def __init__(self):
        self._daily_sim_info_creation_count = 0
        self._daily_sim_info_creation_count_telemetry_alarm = None

    def save(self, zone_data=None, open_street_data=None, **kwargs):
        save_game_data = services.get_persistence_service().get_save_game_data_proto()
        save_game_data.gameplay_data.daily_sim_info_creation_count = self._daily_sim_info_creation_count

    def load(self, zone_data=None):
        save_game_data = services.get_persistence_service().get_save_game_data_proto()
        self._daily_sim_info_creation_count = save_game_data.gameplay_data.daily_sim_info_creation_count
        self._create_daily_sim_info_creation_count_alarm()

    def _create_daily_sim_info_creation_count_alarm(self):
        if self._daily_sim_info_creation_count_telemetry_alarm:
            alarms.cancel_alarm(self._daily_sim_info_creation_count_telemetry_alarm)
        now = services.time_service().sim_now
        time_span_until = clock.time_until_hour_of_day(now, daily_sim_info_creation_COUNT_TIME_OF_DAY)
        self._daily_sim_info_creation_count_telemetry_alarm = alarms.add_alarm(self, time_span_until, (self._trigger_daily_sim_info_creation_count_telemetry),
          repeating=False)

    def _trigger_daily_sim_info_creation_count_telemetry(self, handle):
        ghost_player_sims = sum((1 for si in services.sim_info_manager().values() if si.is_player_sim if si.is_ghost))
        with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_SIMINFO_DAILY_COUNT) as (hook):
            hook.write_int('cont', self._daily_sim_info_creation_count)
            hook.write_int('pgho', ghost_player_sims)
        self._daily_sim_info_creation_count = 0
        self._create_daily_sim_info_creation_count_alarm()

    def on_sim_info_created(self):
        self._daily_sim_info_creation_count += 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/sim_info_telemetry.pyc
