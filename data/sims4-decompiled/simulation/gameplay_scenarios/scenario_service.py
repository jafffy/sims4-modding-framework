# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gameplay_scenarios\scenario_service.py
# Compiled at: 2022-06-27 09:26:22
# Size of source mod 2**32: 707 bytes
import services
from sims4.service_manager import Service

class ScenarioService(Service):

    def update(self):
        active_household = services.active_household()
        if active_household is not None:
            scenario_tracker = active_household.scenario_tracker
            if scenario_tracker is not None:
                if scenario_tracker.active_scenario is not None:
                    scenario_tracker.active_scenario.update()
# okay decompiling data/sims4-not-yet-decompiled/simulation/gameplay_scenarios/scenario_service.pyc
