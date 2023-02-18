# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\attractor_point_interaction.py
# Compiled at: 2016-03-27 22:26:26
# Size of source mod 2**32: 2250 bytes
import random
from event_testing import results
from interactions.base.super_interaction import SuperInteraction
from sims4.tuning.tunable import TunableEnumWithFilter
from sims4.tuning.tunable_base import GroupNames
from tag import Tag
import services

class AttractorPointInteraction(SuperInteraction):
    INSTANCE_TUNABLES = {'_attractor_point_identifier':TunableEnumWithFilter(description='\n            The identifier that will be used to select which attractor points\n            we will use.\n            ',
       tunable_type=Tag,
       default=Tag.INVALID,
       invalid_enums=(
      Tag.INVALID,),
       filter_prefixes=('AtPo', ),
       tuning_group=GroupNames.PICKERTUNING), 
     '_attractor_point_interaction':SuperInteraction.TunableReference(description='\n            The affordance that we will push on the Sim once the attractor\n            point selection has been made.\n            ',
       tuning_group=GroupNames.PICKERTUNING)}

    @classmethod
    def _test(cls, target, context, **interaction_parameters):
        attractor_points = list(services.object_manager().get_objects_with_tag_gen(cls._attractor_point_identifier))
        if not attractor_points:
            return results.TestResult(False, 'No attractor points with tag {} found.', cls._attractor_point_identifier)
        return (super()._test)(target, context, **interaction_parameters)

    def _run_interaction_gen(self, timeline):
        attractor_points = list(services.object_manager().get_objects_with_tag_gen(self._attractor_point_identifier))
        chosen_point = random.choice(attractor_points)
        context = self.context.clone_for_continuation(self)
        self.sim.push_super_affordance(self._attractor_point_interaction, chosen_point, context)
        return True
        if False:
            yield None
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/attractor_point_interaction.pyc
