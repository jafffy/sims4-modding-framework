# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\complex\guided_meditation_situation.py
# Compiled at: 2021-07-09 02:04:08
# Size of source mod 2**32: 2302 bytes
from sims4.tuning.tunable_base import GroupNames
from situations.complex.instructed_class_situation_mixin import InstructedClassSituationMixin, _PreClassState, _PostClassState
from situations.situation import Situation
from situations.situation_complex import SituationComplexCommon, CommonInteractionCompletedSituationState, SituationStateData

class _GuidedMeditationState(CommonInteractionCompletedSituationState):

    def _additional_tests(self, sim_info, event, resolver):
        return self.owner.is_sim_in_situation(sim_info.get_sim_instance())

    def _on_interaction_of_interest_complete(self, **kwargs):
        self.owner.advance_state()

    def timer_expired(self):
        self.owner.advance_state()


class GuidedMeditationSituation(InstructedClassSituationMixin, SituationComplexCommon):
    INSTANCE_TUNABLES = {'in_class_state': _GuidedMeditationState.TunableFactory(description="\n            In class state, where the 'meditation' portion of the class occurs.\n            ",
                         tuning_group=(GroupNames.STATE))}
    REMOVE_INSTANCE_TUNABLES = Situation.NON_USER_FACING_REMOVE_INSTANCE_TUNABLES

    @classmethod
    def _states(cls):
        return (
         SituationStateData(1, _PreClassState, factory=(cls.pre_class_state.situation_state)),
         SituationStateData(2, _GuidedMeditationState, factory=(cls.in_class_state)),
         SituationStateData(3, _PostClassState, factory=(cls.post_class_state.situation_state)))

    def get_next_class_state(self):
        current_state_type = type(self._cur_state)
        if current_state_type is self.pre_class_state.situation_state.factory:
            next_state = self.in_class_state
        else:
            next_state = self.post_class_state.situation_state
        return next_state
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/complex/guided_meditation_situation.pyc
