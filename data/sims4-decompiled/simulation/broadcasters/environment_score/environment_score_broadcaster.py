# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\broadcasters\environment_score\environment_score_broadcaster.py
# Compiled at: 2018-02-02 03:56:23
# Size of source mod 2**32: 1502 bytes
from broadcasters.broadcaster import Broadcaster
from broadcasters.broadcaster_effect import _BroadcasterEffect
from broadcasters.broadcaster_utils import BroadcasterClockType
from sims4.tuning.instances import lock_instance_tunables

class BroadcasterEffectEnvironmentScore(_BroadcasterEffect):

    def apply_broadcaster_effect(self, broadcaster, affected_object):
        if affected_object.is_sim:
            affected_object.add_environment_score_broadcaster(broadcaster)

    def remove_broadcaster_effect(self, broadcaster, affected_object):
        if affected_object.is_sim:
            affected_object.remove_environment_score_broadcaster(broadcaster)


class BroadcasterEnvironmentScore(Broadcaster):
    REMOVE_INSTANCE_TUNABLES = ('effects', )

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.effects = (BroadcasterEffectEnvironmentScore(),)


lock_instance_tunables(BroadcasterEnvironmentScore, clock_type=(BroadcasterClockType.REAL_TIME))
# okay decompiling data/sims4-not-yet-decompiled/simulation/broadcasters/environment_score/environment_score_broadcaster.pyc
