# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\ui\tested_ui_dialog_notification.py
# Compiled at: 2019-10-02 07:11:52
# Size of source mod 2**32: 1076 bytes
from event_testing.tests import TunableTestSet
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit
from snippets import define_snippet
from ui.ui_dialog_notification import UiDialogNotification

class TestedUiDialogNotification(UiDialogNotification):
    FACTORY_TUNABLES = {'tests': TunableTestSet(description='\n            The test(s) to decide whether the notification is to be shown.\n            ')}

    def show_dialog(self, **kwargs):
        if self.tests:
            test_result = self.tests.run_tests(self._resolver)
            if not test_result:
                return
        return (super().show_dialog)(**kwargs)


TunableTestedUiDialogNotificationReference, TunableTestedUiDialogNotificationSnippet = define_snippet('tested_notification', TestedUiDialogNotification.TunableFactory())
# okay decompiling data/sims4-not-yet-decompiled/simulation/ui/tested_ui_dialog_notification.pyc
