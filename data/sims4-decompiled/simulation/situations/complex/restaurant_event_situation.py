# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\complex\restaurant_event_situation.py
# Compiled at: 2016-02-19 19:02:09
# Size of source mod 2**32: 1617 bytes
from situations.situation import Situation
from situations.situation_complex import SituationComplexCommon, CommonSituationState, SituationStateData

class _SimpleState(CommonSituationState):
    pass


class RestaurantEventSituation(SituationComplexCommon):
    INSTANCE_TUNABLES = {'simple_state': _SimpleState.TunableFactory(description='\n            The basic state that all Sims in this situation will be in during\n            this situation.\n            ')}
    REMOVE_INSTANCE_TUNABLES = Situation.SITUATION_EVENT_REMOVE_INSTANCE_TUNABLES

    @classmethod
    def _states(cls):
        return [SituationStateData(1, _SimpleState, factory=(cls.simple_state))]

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return list(cls.simple_state._tuned_values.job_and_role_changes.items())

    @classmethod
    def default_job(cls):
        pass

    def start_situation(self):
        super().start_situation()
        self._change_state(self.simple_state())
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/complex/restaurant_event_situation.pyc
