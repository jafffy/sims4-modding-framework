# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\civic_policies\street_civic_policy_tests.py
# Compiled at: 2020-03-03 01:50:14
# Size of source mod 2**32: 1496 bytes
from civic_policies.base_civic_policy_tests import BaseCivicPolicyTest
import services
from civic_policies.street_civic_policy_tuning import StreetCivicPolicySelectorMixin

class StreetCivicPolicySelectorTestMixin(StreetCivicPolicySelectorMixin):

    def get_expected_args(self):
        if self.street is None or hasattr(self.street, 'civic_policy'):
            return {}
        return self.street.get_expected_args()

    def get_custom_event_registration_keys(self):
        return self.street is None or hasattr(self.street, 'civic_policy') or ()
        keys = []
        for test in self.civic_policy_tests:
            custom_keys = test.get_custom_event_keys(self.street)
            if not custom_keys:
                continue
            keys.extend(custom_keys)

        return keys


class StreetCivicPolicyTest(StreetCivicPolicySelectorTestMixin, BaseCivicPolicyTest):
    pass
# okay decompiling data/sims4-not-yet-decompiled/simulation/civic_policies/street_civic_policy_tests.pyc
