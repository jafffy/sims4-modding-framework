# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\story_progression\story_progression_rule_display_info.py
# Compiled at: 2021-08-24 02:23:35
# Size of source mod 2**32: 1428 bytes
import services
from interactions.utils.tunable_icon import TunableIcon
from sims4.localization import TunableLocalizedString
from sims4.resources import Types
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import HasTunableReference
from sims4.tuning.tunable_base import ExportModes

class StoryProgressionRuleDisplayInfo(HasTunableReference, metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(Types.USER_INTERFACE_INFO)):
    INSTANCE_TUNABLES = {'rule_name':TunableLocalizedString(description="\n            String to be displayed as this rule's name.\n            ",
       export_modes=ExportModes.ClientBinary), 
     'rule_description':TunableLocalizedString(description="\n            String to be displayed as this rule's description.\n            ",
       export_modes=ExportModes.ClientBinary), 
     'rule_icon':TunableIcon(description='\n            Icon to be displayed to represent this rule.\n            ',
       export_modes=ExportModes.ClientBinary)}
# okay decompiling data/sims4-not-yet-decompiled/simulation/story_progression/story_progression_rule_display_info.pyc
