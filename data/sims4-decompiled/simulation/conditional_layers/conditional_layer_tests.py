# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\conditional_layers\conditional_layer_tests.py
# Compiled at: 2020-04-23 23:06:35
# Size of source mod 2**32: 2107 bytes
import services, sims4
from event_testing.results import TestResult
from event_testing.test_base import BaseTest
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableReference, Tunable

class ConditionalLayerLoadedTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'conditional_layer':TunableReference(description='\n            Which conditional layer to test.\n            ',
       manager=services.get_instance_manager(sims4.resources.Types.CONDITIONAL_LAYER)), 
     'consider_queued_requests':Tunable(description='\n            If checked then this test will consider the queued requests for this conditional layer.\n            ',
       tunable_type=bool,
       default=True), 
     'negate':Tunable(description='\n            If checked then this test will return True when not loaded.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {}

    def __call__(self, *args, **kwargs):
        conditional_layer_service = services.conditional_layer_service()
        if conditional_layer_service is None:
            return TestResult(False, 'No Conditional Layer Service available', tooltip=(self.tooltip))
            layer_loaded = conditional_layer_service.is_layer_loaded(self.conditional_layer, self.consider_queued_requests)
            if layer_loaded:
                if self.negate:
                    return TestResult(False, 'Conditional Layer loaded', tooltip=(self.tooltip))
        elif not self.negate:
            return TestResult(False, 'Conditional Layer not loaded', tooltip=(self.tooltip))
        return TestResult.TRUE
# okay decompiling data/sims4-not-yet-decompiled/simulation/conditional_layers/conditional_layer_tests.pyc
