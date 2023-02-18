# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\cas\cas_preference_category.py
# Compiled at: 2021-09-13 22:15:21
# Size of source mod 2**32: 1442 bytes
import services, sims4
from interactions.utils.display_mixin import get_display_mixin
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import HasTunableReference, TunableReference, Tunable
from sims4.tuning.tunable_base import ExportModes
CasPreferenceDisplayMixin = get_display_mixin(has_description=True, has_icon=True, has_tooltip=True, use_string_tokens=True,
  has_secondary_icon=True,
  export_modes=(ExportModes.ClientBinary),
  enabled_by_default=True)

class CasPreferenceCategory(CasPreferenceDisplayMixin, HasTunableReference, metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.CAS_PREFERENCE_CATEGORY)):
    INSTANCE_TUNABLES = {'decorator_preference': Tunable(description='\n            If True, the preference category will be used by the GP10 Decorator\n            Career as a source of preferences to create performance benchmarks for\n            a Decorator Gig.\n\n            If False, this preference will not be used by the Decorator Gig.\n            ',
                               tunable_type=bool,
                               default=False)}
# okay decompiling data/sims4-not-yet-decompiled/simulation/cas/cas_preference_category.pyc
