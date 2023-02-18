# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\fishing\fishing_tests.py
# Compiled at: 2021-03-10 04:06:57
# Size of source mod 2**32: 2452 bytes
from caches import cached_test
from event_testing.results import TestResult
from event_testing.test_base import BaseTest
from interactions import ParticipantTypeObject
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableVariant, TunableEnumEntry, Tunable

class FishingTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):

    class _HasFish(HasTunableSingletonFactory):

        def __call__(self, target, tooltip=None):
            fishing_location_component = target.fishing_location_component
            if fishing_location_component is None:
                return TestResult(False, 'Target {} has no fishing location component.', target, tooltip=tooltip)
            else:
                fishing_data = fishing_location_component.fishing_data
                return any(fishing_data.get_possible_fish_gen()) or TestResult(False, 'Target {} has no fish.', target, tooltip=tooltip)
            return TestResult.TRUE

    FACTORY_TUNABLES = {'test':TunableVariant(description='\n            The test to run.\n            ',
       has_fish=_HasFish.TunableFactory(),
       default='has_fish'), 
     'target':TunableEnumEntry(description='\n            The target to test against.\n            ',
       tunable_type=ParticipantTypeObject,
       default=ParticipantTypeObject.Object), 
     'negate':Tunable(description='\n            If checked, the test will be negated. \n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'targets': self.target}

    @cached_test
    def __call__(self, targets=None):
        target = next(iter(targets), None)
        if target is None:
            return TestResult(False, 'Target is none', tooltip=(self.tooltip))
        result = self.test(target, tooltip=(self.tooltip))
        if self.negate:
            if result:
                return TestResult(False, 'Test passed but negate is checked', tooltip=(self.tooltip))
            return TestResult.TRUE
        return result
# okay decompiling data/sims4-not-yet-decompiled/simulation/fishing/fishing_tests.pyc
