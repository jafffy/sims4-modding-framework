# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\situation_phase.py
# Compiled at: 2015-08-17 16:34:22
# Size of source mod 2**32: 1310 bytes


class SituationPhase:

    def __init__(self, job_list, exit_conditions, duration):
        self._job_list = job_list
        self._exit_conditions = exit_conditions
        self._duration = duration

    def jobs_gen(self):
        for job, role in self._job_list.items():
            yield (
             job, role)

    def exit_conditions_gen(self):
        for ec in self._exit_conditions:
            yield ec

    def get_duration(self):
        return self._duration
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/situation_phase.pyc
