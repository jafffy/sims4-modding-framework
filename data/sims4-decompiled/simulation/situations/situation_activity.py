# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\situation_activity.py
# Compiled at: 2021-09-29 22:40:31
# Size of source mod 2**32: 1489 bytes
from holidays.holiday_tradition import HolidayTradition, TraditionType
from sims4.tuning.instances import lock_instance_tunables

class SituationActivity(HolidayTradition):
    REMOVE_INSTANCE_TUNABLES = ('pre_holiday_buffs', 'pre_holiday_buff_reason', 'holiday_buffs',
                                'holiday_buff_reason', 'drama_nodes_to_score', 'drama_nodes_to_run',
                                'additional_walkbys', 'preference', 'preference_reward_buff',
                                'lifecycle_actions', 'events', 'core_object_tags',
                                'deco_object_tags', 'business_cost_multiplier')
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/situation_activity.pyc
