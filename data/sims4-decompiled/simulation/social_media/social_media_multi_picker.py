# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\social_media\social_media_multi_picker.py
# Compiled at: 2022-06-15 00:14:35
# Size of source mod 2**32: 3129 bytes
from interactions.base.multi_picker_interaction import MultiPickerInteraction
from ui.ui_dialog_multi_picker import UiMultiPicker
from ui.ui_dialog_picker import SimPickerRow
from social_media import SocialMediaPostType, SocialMediaNarrative
from sims4.tuning.tunable import TunableEnumEntry
from sims4.tuning.tunable_base import GroupNames
import services, sims4.log
logger = sims4.log.Logger('SocialMediaMultiPicker', default_owner='mbilello')

class UiSocialMediaMultiPicker(UiMultiPicker):
    FACTORY_TUNABLES = {'post_type': TunableEnumEntry(description='\n            A SocialMediaPostType enum entry.\n            ',
                    tunable_type=SocialMediaPostType,
                    default=(SocialMediaPostType.DEFAULT),
                    tuning_group=(GroupNames.PICKERTUNING))}

    def multi_picker_result(self, response_proto):
        social_media_service = services.get_social_media_service()
        if social_media_service is None:
            return
        narrative = SocialMediaNarrative.FRIENDLY
        post_type = self.post_type
        target_sim_id = None
        context_post = None
        for picker_result in response_proto.picker_responses:
            if picker_result.picker_id in self._picker_dialogs:
                dialog = self._picker_dialogs[picker_result.picker_id]
                choices = picker_result.choices
                if not choices:
                    logger.error('Failed to get choices in UiSocialMediaMultiPicker')
                    return
                for index, row in enumerate(dialog.picker_rows):
                    if isinstance(row, SimPickerRow):
                        target_sim_id = choices[0]
                        break
                    elif int(row.tag.narrative) in choices:
                        if not hasattr(row.tag, 'context_post'):
                            narrative = row.tag.narrative
                            break
                    if int(row.tag.narrative) in choices and hasattr(row.tag, 'context_post'):
                        context_post = row.tag.context_post
                        break

        sim_id = self.target.sim_info.sim_id if self.target is not None else None
        if sim_id is None:
            sim_id = self.target_sim.id if self.target_sim is not None else None
        if sim_id is not None:
            social_media_service.create_post(post_type, sim_id, target_sim_id, narrative, context_post)


class SocialMediaMultiPickerInteraction(MultiPickerInteraction):
    INSTANCE_TUNABLES = {'picker_dialog': UiSocialMediaMultiPicker.TunableFactory(description='\n            The Social Media multi picker dialog.\n            ',
                        tuning_group=(GroupNames.PICKERTUNING))}
# okay decompiling data/sims4-not-yet-decompiled/simulation/social_media/social_media_multi_picker.pyc
