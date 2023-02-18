# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\situation_goal_proxy.py
# Compiled at: 2020-09-17 01:28:49
# Size of source mod 2**32: 1069 bytes
from situations.situation_goal import SituationGoal

class SituationGoalProxy(SituationGoal):
    REMOVE_INSTANCE_TUNABLES = ('_post_tests', )

    def setup(self):
        super().setup()
        if self._situation is None:
            return
        self._situation._on_proxy_situation_goal_setup(self)

    def set_count(self, value):
        self._count = int(value)
        if self._count >= self._iterations:
            super()._on_goal_completed()
        else:
            self._on_iteration_completed()
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/situation_goal_proxy.pyc
