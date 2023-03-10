# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\teleport\teleport_tests.py
# Compiled at: 2020-11-12 15:43:21
# Size of source mod 2**32: 1896 bytes
from event_testing import test_base
from event_testing.results import TestResult
from caches import cached_test
from interactions import ParticipantTypeActorTargetSim
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry
from teleport.teleport_enums import TeleportStyle

class TeleportCostTest(HasTunableSingletonFactory, AutoFactoryInit, test_base.BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The subject of this test.\n            ',
       tunable_type=ParticipantTypeActorTargetSim,
       default=ParticipantTypeActorTargetSim.Actor), 
     'teleport_type':TunableEnumEntry(description='\n            Teleport style to be tested against.\n            ',
       tunable_type=TeleportStyle,
       default=TeleportStyle.NONE,
       invalid_enums=(
      TeleportStyle.NONE,),
       pack_safe=True)}

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=None):
        if test_targets is None:
            return TestResult(False, 'Teleport cost test failed due no targets.', tooltip=(self.tooltip))
        for target_sim in test_targets:
            if not target_sim.can_trigger_teleport_style(self.teleport_type):
                return TestResult(False, 'Sim {} cannot triger the teleport style {}.', target_sim, (self.teleport_type), tooltip=(self.tooltip))

        return TestResult.TRUE
# okay decompiling data/sims4-not-yet-decompiled/simulation/teleport/teleport_tests.pyc
