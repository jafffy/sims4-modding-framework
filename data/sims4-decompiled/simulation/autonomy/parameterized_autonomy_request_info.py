# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\autonomy\parameterized_autonomy_request_info.py
# Compiled at: 2016-09-08 19:38:24
# Size of source mod 2**32: 3360 bytes


class ParameterizedAutonomyRequestInfo:

    def __init__(self, commodities, static_commodities, objects, retain_priority, retain_carry_target=True, objects_to_ignore=None, affordances=None, randomization_override=None, radius_to_consider=0, consider_scores_of_zero=False, test_connectivity_to_target=True, retain_context_source=False, ignore_user_directed_and_autonomous=False):
        self.commodities = commodities
        self.static_commodities = static_commodities
        self.objects = objects
        self.retain_priority = retain_priority
        self.objects_to_ignore = objects_to_ignore
        self.affordances = affordances
        self.retain_carry_target = retain_carry_target
        self.randomization_override = randomization_override
        self.radius_to_consider = radius_to_consider
        self.consider_scores_of_zero = consider_scores_of_zero
        self.test_connectivity_to_target = test_connectivity_to_target
        self.retain_context_source = retain_context_source
        self.ignore_user_directed_and_autonomous = ignore_user_directed_and_autonomous
# okay decompiling data/sims4-not-yet-decompiled/simulation/autonomy/parameterized_autonomy_request_info.pyc
