# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\event_testing\pie_menu_color_test.py
# Compiled at: 2022-04-22 18:48:59
# Size of source mod 2**32: 1012 bytes
from event_testing.tests import TestListLoadingMixin
from sims.sim_info_tests import MoodTest
from sims4.tuning.tunable import TunableVariant
import event_testing

class TunablePieMenuColorTestVariant(TunableVariant):

    def __init__(self, **kwargs):
        tunables = {'mood': MoodTest.TunableFactory()}
        kwargs.update(tunables)
        (super().__init__)(**kwargs)


class PieMenuColorTestList(event_testing.tests.TestListLoadingMixin):
    DEFAULT_LIST = event_testing.tests.TestList()

    def __init__(self, description=None):
        super().__init__(description=description, tunable=(TunablePieMenuColorTestVariant()))
# okay decompiling data/sims4-not-yet-decompiled/simulation/event_testing/pie_menu_color_test.pyc
