# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\cas\cas_stories_answer.py
# Compiled at: 2019-05-08 20:23:02
# Size of source mod 2**32: 2428 bytes
import services, sims4
from aspirations.aspiration_tuning import AspirationTrack
from cas.cas_stories_trait_chooser import CasStoriesTraitChooser
from sims4.localization import TunableLocalizedStringFactory
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import HasTunableReference, TunableList, TunableTuple, TunableVariant, Tunable, TunableReference
from sims4.tuning.tunable_base import ExportModes, GroupNames
from traits.traits import Trait

class CasStoriesAnswer(HasTunableReference, metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.CAS_STORIES_ANSWER)):
    INSTANCE_TUNABLES = {'text':TunableLocalizedStringFactory(description='\n            The text of this answer.\n            ',
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'weightings':TunableList(description='\n            A list of objects to apply weightings to if this answer is \n            selected. Weight is the weight that shoudld be added to the chance \n            to receive this object.  In the latter case a trait will be \n            selected from the trait chooser based on its cumulative weighting \n            throughout the CAS Stories survey.\n            ',
       tunable=TunableTuple(weighted_object=TunableVariant(trait=(Trait.TunableReference()),
       trait_chooser=(CasStoriesTraitChooser.TunableReference()),
       aspiration_track=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ASPIRATION_TRACK))),
       default='trait'),
       weight=Tunable(tunable_type=float,
       default=0.0),
       export_class_name='CASAnswerWeightings'),
       export_modes=ExportModes.ClientBinary)}
# okay decompiling data/sims4-not-yet-decompiled/simulation/cas/cas_stories_answer.pyc
