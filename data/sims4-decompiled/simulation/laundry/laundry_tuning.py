# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\laundry\laundry_tuning.py
# Compiled at: 2018-07-27 22:16:25
# Size of source mod 2**32: 9150 bytes
from event_testing.tests import TunableTestSet
from objects.components.state import TunableStateValueReference, TunableStateTypeReference
from sims.outfits.outfit_enums import OutfitCategory
from sims4.tuning.tunable import TunableReference, TunableEnumWithFilter, TunableTuple, TunablePercent, TunableSimMinute, TunableList, TunableSet, TunableEnumEntry, TunableMapping, TunablePackSafeReference
from tag import TunableTags, Tag
import services, sims4.log
logger = sims4.log.Logger('Laundry', default_owner='mkartika')

class LaundryTuning:
    GENERATE_CLOTHING_PILE = TunableTuple(description='\n        The tunable to generate clothing pile on the lot. This will be called\n        when we find laundry hero objects on the lot and there is no hamper\n        available.\n        ',
      loot_to_apply=TunableReference(description='\n            Loot to apply for generating clothing pile.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      class_restrictions=('LootActions', ),
      pack_safe=True),
      naked_outfit_category=TunableSet(description="\n            Set of outfits categories which is considered naked.\n            When Sim switches FROM these outfits, it won't generate the pile.\n            When Sim switches TO these outfits, it won't apply laundry reward\n            or punishment.\n            ",
      tunable=TunableEnumEntry(tunable_type=OutfitCategory,
      default=(OutfitCategory.EVERYDAY),
      invalid_enums=(
     OutfitCategory.CURRENT_OUTFIT,))),
      no_pile_outfit_category=TunableSet(description="\n            Set of outfits categories which will never generate the pile.\n            When Sim switches FROM or TO these outfits, it won't generate the\n            pile.\n            \n            Laundry reward or punishment will still be applied to the Sim when \n            switching FROM or TO these outfits.\n            ",
      tunable=TunableEnumEntry(tunable_type=OutfitCategory,
      default=(OutfitCategory.EVERYDAY),
      invalid_enums=(
     OutfitCategory.CURRENT_OUTFIT,))),
      no_pile_interaction_tag=TunableEnumWithFilter(description='\n            If interaction does spin clothing change and has this tag, it will\n            generate no clothing pile.\n            ',
      tunable_type=Tag,
      default=(Tag.INVALID),
      filter_prefixes=('interaction', )))
    HAMPER_OBJECT_TAGS = TunableTags(description='\n        Tags that considered hamper objects.\n        ',
      filter_prefixes=('func', ))
    LAUNDRY_HERO_OBJECT_TAGS = TunableTags(description='\n        Tags of laundry hero objects. Placing any of these objects on the lot\n        will cause the service to generate clothing pile for each Sims on the\n        household after spin clothing change.\n        ',
      filter_prefixes=('func', ))
    NOT_DOING_LAUNDRY_PUNISHMENT = TunableTuple(description='\n        If no Sim in the household unload completed laundry in specific\n        amount of time, the negative loot will be applied to Sim household \n        on spin clothing change to engage them doing laundry.\n        ',
      timeout=TunableSimMinute(description="\n            The amount of time in Sim minutes, since the last time they're \n            finishing laundry, before applying the loot.\n            ",
      default=2880,
      minimum=1),
      loot_to_apply=TunableReference(description='\n            Loot defined here will be applied to the Sim in the household\n            on spin clothing change if they are not doing laundry for \n            a while.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      class_restrictions=('LootActions', ),
      pack_safe=True))
    PUT_AWAY_FINISHED_LAUNDRY = TunableTuple(description='\n        The tunable to update laundry service on Put Away finished laundry\n        interaction.\n        ',
      interaction_tag=TunableEnumWithFilter(description='\n            Tag that represent the put away finished laundry interaction which \n            will update Laundry Service data.\n            ',
      tunable_type=Tag,
      default=(Tag.INVALID),
      filter_prefixes=('interaction', )),
      laundry_condition_states=TunableTuple(description='\n            This is the state type of completed laundry object condition \n            which will aggregate the data to the laundry service.\n            ',
      condition_states=TunableList(description='\n                A list of state types to be stored on laundry service.\n                ',
      tunable=TunableStateTypeReference(pack_safe=True),
      unique_entries=True),
      excluded_states=TunableList(description='\n                A list of state values of Condition States which will not \n                be added to the laundry service.\n                ',
      tunable=TunableStateValueReference(pack_safe=True),
      unique_entries=True)),
      laundry_condition_timeout=TunableSimMinute(description='\n            The amount of time in Sim minutes that the individual laundry\n            finished conditions will be kept in the laundry conditions \n            aggregate data.\n            ',
      default=1440,
      minimum=0),
      conditions_and_rewards_map=TunableMapping(description='\n            Mapping of laundry conditions and loot rewards.\n            ',
      key_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
      pack_safe=True),
      value_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      class_restrictions=('LootActions', ),
      pack_safe=True)))
    PUT_CLOTHING_PILE_ON_HAMPER = TunableTuple(description='\n        The Tunable to directly put generated clothing pile in the hamper.\n        ',
      chance=TunablePercent(description='\n            The chance that a clothing pile will be put directly in the hamper. \n            Tune the value in case putting clothing pile in hamper every \n            spin-outfit-change feeling excessive.\n            ',
      default=100),
      clothing_pile=TunableTuple(description="\n            Clothing pile object that will be created and put into the hamper \n            automatically. \n            \n            You won't see the object on the lot since it will go directly to \n            the hamper. We create it because we need to transfer all of the \n            commodities data and average the values into the hamper precisely.\n            ",
      definition=TunablePackSafeReference(description='\n                Reference to clothing pile object definition.\n                ',
      manager=(services.definition_manager())),
      initial_states=TunableList(description='\n                A list of states to apply to the clothing pile as soon as it \n                is created.\n                ',
      tunable=TunableTuple(description='\n                    The state to apply and optional to decide if the state \n                    should be applied.\n                    ',
      state=TunableStateValueReference(pack_safe=True),
      tests=(TunableTestSet())))),
      full_hamper_state=TunableStateValueReference(description='\n            The state of full hamper which make the hamper is unavailable to \n            add new clothing pile in it.\n            ',
      pack_safe=True),
      loots_to_apply=TunableList(description='\n            Loots to apply to the hamper when clothing pile is being put.\n            ',
      tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      class_restrictions=('LootActions', ),
      pack_safe=True)),
      tests=TunableTestSet(description='\n            The test to run on the Sim that must pass in order for putting\n            clothing pile automatically to the hamper. These tests will only \n            be run when we have available hamper on the lot.\n            '))
# okay decompiling data/sims4-not-yet-decompiled/simulation/laundry/laundry_tuning.pyc
