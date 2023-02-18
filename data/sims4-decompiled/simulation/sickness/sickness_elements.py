# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sickness\sickness_elements.py
# Compiled at: 2017-05-16 19:02:08
# Size of source mod 2**32: 2044 bytes
from interactions.utils.interaction_elements import XevtTriggeredElement
from sickness.sickness_enums import SicknessDiagnosticActionType, DiagnosticActionResultType
from sims4.tuning.tunable import TunableEnumEntry

class TrackDiagnosticAction(XevtTriggeredElement):
    FACTORY_TUNABLES = {'action_type':TunableEnumEntry(description="\n            Type of the action being tracked.\n            \n            The affordance of the interaction running this element\n            will be tracked in the target's sickness tracker.\n            ",
       tunable_type=SicknessDiagnosticActionType,
       default=SicknessDiagnosticActionType.EXAM), 
     'result_type':TunableEnumEntry(description='\n            Result of the interaction.\n            \n            This will trigger loots as applicable in sickness tuning\n            if the target is sick.\n            ',
       tunable_type=DiagnosticActionResultType,
       default=DiagnosticActionResultType.DEFAULT)}

    def _do_behavior(self):
        interaction = self.interaction
        target = interaction.target.sim_info
        if self.result_type != DiagnosticActionResultType.FAILED_TOO_STRESSED:
            if self.action_type == SicknessDiagnosticActionType.EXAM:
                target.track_examination(interaction.affordance)
            else:
                if self.action_type == SicknessDiagnosticActionType.TREATMENT:
                    target.track_treatment(interaction.affordance)
        if target.has_sickness_tracking():
            target.current_sickness.apply_loots_for_action(self.action_type, self.result_type, interaction)
# okay decompiling data/sims4-not-yet-decompiled/simulation/sickness/sickness_elements.pyc
