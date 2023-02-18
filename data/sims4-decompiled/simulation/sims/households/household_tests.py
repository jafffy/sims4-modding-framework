# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\households\household_tests.py
# Compiled at: 2020-11-12 15:43:20
# Size of source mod 2**32: 1391 bytes
from event_testing.results import TestResult
from event_testing.test_base import BaseTest
from caches import cached_test
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory
import services

class PlayerPopulationTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):

    def get_expected_args(self):
        return {}

    @cached_test
    def __call__(self):
        culling_service = services.get_culling_service()
        max_player_population = culling_service.get_max_player_population()
        if max_player_population:
            household_manager = services.household_manager()
            player_population = sum((len(household) for household in household_manager.values() if household.is_player_household))
            if player_population >= max_player_population:
                return TestResult(False, 'Over the maximum player population ({}/{})', player_population, max_player_population, tooltip=(lambda *_, **__: self.tooltip(player_population, max_player_population)))
        return TestResult.TRUE
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/households/household_tests.pyc
