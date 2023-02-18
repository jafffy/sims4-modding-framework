# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\situation_goal_tracker_tuning.py
# Compiled at: 2021-10-08 02:05:04
# Size of source mod 2**32: 2887 bytes
from situations.dynamic_situation_goal_tracker import DynamicSituationGoalTracker, SimpleSituationGoalTracker
from situations.situation_goal_tracker import SituationGoalTracker
from situations.situation_serialization import GoalTrackerType
from sims4.tuning.tunable import TunableFactory, TunableVariant
FORCE_USER_FACING_GOAL_TRACKERS = [
 GoalTrackerType.SIMPLE_GOAL_TRACKER]

class TunableSituationGoalTracker(TunableFactory):

    @staticmethod
    def _get_situation_goal_tracker(situation=None):
        return (GoalTrackerType.STANDARD_GOAL_TRACKER, None if situation is None else SituationGoalTracker(situation))

    FACTORY_TYPE = _get_situation_goal_tracker


class TunableDynamicSituationGoalTracker(TunableFactory):

    @staticmethod
    def _get_dynamic_goal_tracker(situation=None):
        return (GoalTrackerType.DYNAMIC_GOAL_TRACKER, None if situation is None else DynamicSituationGoalTracker(situation))

    FACTORY_TYPE = _get_dynamic_goal_tracker


class TunableSimpleSituationGoalTracker(TunableFactory):

    @staticmethod
    def _get_simple_goal_tracker(situation=None):
        return (GoalTrackerType.SIMPLE_GOAL_TRACKER, None if situation is None else SimpleSituationGoalTracker(situation))

    FACTORY_TYPE = _get_simple_goal_tracker


class TunableSituationGoalTrackerVariant(TunableVariant):

    def __init__(self, *args, default='situation_goal_tracker', **kwargs):
        (super().__init__)(args, situation_goal_tracker=TunableSituationGoalTracker(description='\n                Standard goal tracker used by situations with chained major and minor goals.\n                '), 
         dynamic_situation_goal_tracker=TunableDynamicSituationGoalTracker(description='\n                Goal tracker that tracks a list of goals and associated preferences. Goals are\n                unchained, without major/minor structure.\n                \n                Primary use is for Holidays.\n                '), 
         simple_situation_goal_tracker=TunableSimpleSituationGoalTracker(description='\n                Goal tracker that tracks a list of goals. Goals are unchained, without major/minor\n                structure.\n                '), 
         default=default, **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/situation_goal_tracker_tuning.pyc
