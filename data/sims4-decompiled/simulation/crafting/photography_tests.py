# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\crafting\photography_tests.py
# Compiled at: 2020-11-12 15:43:18
# Size of source mod 2**32: 1561 bytes
from event_testing.resolver import SingleActorAndObjectResolver, PhotoResolver
from event_testing.test_events import TestEvent
from event_testing.tests import TunableTestSet
from interactions import ParticipantType
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit
from caches import cached_test
import event_testing

class TookPhotoTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    test_events = (
     TestEvent.PhotoTaken,)
    USES_EVENT_DATA = True
    FACTORY_TUNABLES = {'tests': TunableTestSet(description='\n            A set of tests that are run with the photographer as the actor,\n            and the photograph as the object and PhotographyTargets as the\n            subjects.\n            ')}

    def get_expected_args(self):
        return {'subject':ParticipantType.Actor, 
         'photo_object':event_testing.test_constants.FROM_EVENT_DATA, 
         'photo_targets':event_testing.test_constants.FROM_EVENT_DATA}

    @cached_test
    def __call__(self, photo_object=None, subject=None, photo_targets=None):
        resolver = PhotoResolver(subject, photo_object, photo_targets, source=self)
        return self.tests.run_tests(resolver)
# okay decompiling data/sims4-not-yet-decompiled/simulation/crafting/photography_tests.pyc
