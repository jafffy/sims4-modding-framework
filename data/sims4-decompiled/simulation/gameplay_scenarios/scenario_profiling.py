# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gameplay_scenarios\scenario_profiling.py
# Compiled at: 2022-07-14 10:18:37
# Size of source mod 2**32: 2457 bytes
from sims4 import math

class ScenarioPhaseProfileRecord:

    def __init__(self):
        self._time_records = dict()
        self._final_time = 0
        self._perf_percentage_list = []

    def generate_percentage_list(self):
        sorted_records = dict(sorted(self._time_records.items()))
        total_occurrence = 0
        for time, occurrence in sorted_records.items():
            total_occurrence += occurrence

        STEP_SIZE_PERCENTAGE = 10
        step_size = math.floor(total_occurrence / STEP_SIZE_PERCENTAGE)
        current_occurrence = 0
        for time, occurrence in sorted_records.items():
            current_occurrence += occurrence
            while current_occurrence >= step_size:
                self._perf_percentage_list.append(time)
                current_occurrence -= step_size

        self._time_records.clear()

    @property
    def perf_percentage_list(self):
        return self._perf_percentage_list

    def get_final_time(self):
        return self._final_time

    def update(self, time):
        record = self._time_records.get(time)
        if record is None:
            self._time_records[time] = 1
        else:
            self._time_records[time] += 1


def record_scenario_profile_metrics(profile, phase_name, sim_debt_time):
    record = profile.get(phase_name)
    if record is None:
        record = ScenarioPhaseProfileRecord()
        profile[phase_name] = record
    record.update(sim_debt_time)


def should_record_scenario_profile_metrics(profile, phase_name):
    record = profile.get(phase_name)
    if record is None:
        return True
    return len(record.perf_percentage_list) == 0


def scenario_profile_on_phase_end(profile, phase_name, final_time):
    record = profile.get(phase_name)
    if record is not None:
        record.generate_percentage_list()
        record._final_time = final_time
# okay decompiling data/sims4-not-yet-decompiled/simulation/gameplay_scenarios/scenario_profiling.pyc
