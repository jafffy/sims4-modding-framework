# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\ui\ui_dialog_notification_story_progression_discovery.py
# Compiled at: 2021-11-09 21:28:35
# Size of source mod 2**32: 990 bytes
import services
from singletons import DEFAULT
from ui.ui_dialog_notification import UiDialogNotification

class UIDialogNotificationStoryProgressionDiscovery(UiDialogNotification):

    def build_msg(self, additional_tokens=(), icon_override=DEFAULT, event_id=None, career_args=None, **kwargs):
        additional_tokens = list(additional_tokens)
        text_override, tokens = services.get_story_progression_service().get_discovery_string()
        additional_tokens = additional_tokens + tokens
        msg = (super().build_msg)(additional_tokens=tuple(additional_tokens), icon_override=icon_override, event_id=event_id, career_args=career_args, 
         text_override=text_override, **kwargs)
        return msg
# okay decompiling data/sims4-not-yet-decompiled/simulation/ui/ui_dialog_notification_story_progression_discovery.pyc
