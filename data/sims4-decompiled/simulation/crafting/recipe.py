# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\crafting\recipe.py
# Compiled at: 2021-10-29 15:58:22
# Size of source mod 2**32: 83127 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_11
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_61
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_11
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_61
expr ::= LOAD_DEREF . 
expr ::= list . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_or_arg ::= expr . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for_iter ::= \e__come_froms . FOR_ITER
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_2 ::= expr . expr expr expr BUILD_MAP_2
kvlist_2 ::= expr expr . expr expr BUILD_MAP_2
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lc_body ::= expr . LIST_APPEND
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list_comp ::= BUILD_LIST_0 . list_iter
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c _come_froms
list_if ::= expr . jmp_false list_iter
list_if ::= expr . jmp_false list_iter COME_FROM
list_if ::= expr . jmp_false37 list_iter
list_if_not ::= expr . jmp_true list_iter
list_if_not ::= expr . jmp_true list_iter COME_FROM
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . expr BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1320         6  LOAD_CLOSURE             'cls'
                   8  BUILD_TUPLE_1         1 
->                10  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  12  LOAD_STR                 'Recipe._tuning_loaded_callback.<locals>.<dictcomp>'
                  14  MAKE_FUNCTION_8          'closure'
                  16  LOAD_DEREF               'cls'
                  18  LOAD_ATTR                _phases
                  20  LOAD_METHOD              items
                  22  CALL_METHOD_0         0  '0 positional arguments'
                  24  GET_ITER         
                  26  CALL_FUNCTION_1       1  '1 positional argument'
                  28  LOAD_DEREF               'cls'
                  30  STORE_ATTR               phases
import itertools
from animation.tunable_animation_overrides import TunableAnimationOverrides
from autonomy.content_sets import ContentSet
from balloon.tunable_balloon import TunableBalloon
from bucks.bucks_enums import BucksType
from crafting.crafting_ingredients import IngredientRequirementByTag, IngredientRequirementByDef, IngredientTooltipStyle
from crafting.crafting_tunable import CraftingTuning
from crafting.food_restrictions_utils import FoodRestrictionUtils
from crafting.genre import Genre
from crafting.recipe_enums import RecipeDifficulty
from crafting.recipe_helpers import RECIPE_TAG_TO_TUNING_ID_MAP
from event_testing.tests import TunableTestVariant, TunableTestSet
from interactions import ParticipantType
from interactions.base.picker_tunables import TunableBuffWeightMultipliers
from interactions.base.super_interaction import SuperInteraction
from interactions.utils.loot import LootActions
from interactions.utils.success_chance import SuccessChance
from objects.components.state import TunableStateValueReference, CommodityBasedObjectStateValue
from objects.hovertip import TooltipFields
from postures import PostureTrack
from sims.household_utilities.utility_types import Utilities, UtilityShutoffReasonPriority
from sims4.localization import TunableLocalizedString, TunableLocalizedStringFactory, LocalizationHelperTuning
from sims4.tuning.dynamic_enum import DynamicEnum
from sims4.tuning.instances import TunedInstanceMetaclass, HashedTunedInstanceMetaclass
from sims4.tuning.tunable import TunableList, Tunable, TunableReference, TunableMapping, TunableVariant, TunableTuple, TunableEnumEntry, OptionalTunable, TunableResourceKey, HasTunableReferenceFactory, HasTunableFactory, TunableInterval, TunableSet, TunableEntitlement, TunableThreshold, TunableEnumWithFilter, TunableOperator, TunablePackSafeReference, TunableRange, TunableCasPart
from sims4.tuning.tunable_base import ExportModes, GroupNames, EnumBinaryExportType
from sims4.utils import classproperty
from singletons import DEFAULT
from statistics.skill import TunableSkillLootData
from tag import Tag
from tunable_multiplier import TunableStatisticModifierCurve
from tunable_time import TunableTimeSpan
from ui.ui_dialog_notification import TunableUiDialogNotificationSnippet
import event_testing.tests, mtx, objects.components, services, sims4.log, sims4.resources, statistics.skill_tests, tag
logger = sims4.log.Logger('Recipe')
dump_logger = sims4.log.LoggerClass('Recipe')
debug_ingredient_requirements = True

class PhaseName(DynamicEnum):
    INVALID = 0
    START_PHASE = 1


class TunableQualityInfo(TunableTuple):

    def __init__(self, description='The quality adjustment info for final product.', **kwargs):
        (super().__init__)(base_quality=Tunable(description='\n                The base quality value for the final product.\n                ',
  tunable_type=float,
  default=0.0), 
         skill_adjustment=Tunable(description='\n                The quality value adjustment based on the effective skill\n                level. If the skill level is higher than the recipe\n                requirement, the adjustment value will be a bonus, otherwise it\n                would apply to the final object quality negatively.\n                ',
  tunable_type=float,
  default=0.0), 
         description=description, **kwargs)


class TunableRecipeObjectInfo(TunableTuple):

    def __init__(self, optional_create=True, description='An object definition and states to apply.', class_restrictions=(), **kwargs):
        definition = TunableReference(description='\n                An object to create.',
          manager=(services.definition_manager()),
          class_restrictions=class_restrictions)
        if optional_create:
            definition = OptionalTunable(definition)
        (super().__init__)(definition=definition, 
         carry_track=OptionalTunable(description='\n                Which hand to carry the object in.',
  tunable=TunableEnumEntry(PostureTrack, default=(PostureTrack.RIGHT))), 
         initial_states=TunableList(description='\n                A list of states to apply to the finished object as soon as it is created.\n                ',
  tunable=TunableStateValueReference(pack_safe=True)), 
         apply_states=TunableList(description='\n                A list of states to apply to the finished object.\n                ',
  tunable=TunableStateValueReference(pack_safe=True)), 
         apply_tags=TunableSet(description='\n                A list of category tags to apply to the finished product.\n                ',
  tunable=TunableEnumEntry((tag.Tag), (tag.Tag.INVALID), description='What tag to test for')), 
         conditional_apply_states=TunableList(description='\n                A list of states to apply to the finished object based on if the associated test passes.\n                ',
  tunable=TunableTuple(description='\n                    The test to pass for the given state to be applied.',
  test=(TunableTestVariant()),
  state=(TunableStateValueReference()))), 
         super_affordances=TunableList(description='\n                Affordances available on the finished product.\n                ',
  tunable=SuperInteraction.TunableReference(pack_safe=True)), 
         loot_list=TunableList(description='\n                A list of pre-defined loot operations to apply after crafting object creation.\n                ',
  tunable=LootActions.TunableReference(pack_safe=True)), 
         chef_loot_list=TunableList(description='\n                A list of pre-defined loot operations to apply after crafting\n                object creation on a restaurant lot by a chef.\n                ',
  tunable=LootActions.TunableReference(pack_safe=True)), 
         quality_adjustment=TunableQualityInfo(), 
         simoleon_value_modifiers_map=TunableMapping(description='\n                    The mapping of state values to Simolean value modifiers.\n                    The final value of a craftable is decided based on its\n                    retail value multiplied by the sum of all modifiers for\n                    states that apply to the final product. All modifiers are\n                    added together first, then the sum will be multiplied by\n                    the retail price.\n                    ',
  key_type=TunableStateValueReference(description='\n                        The quality state values. If this item has this state,\n                        then a random modifier between min_value and max_value\n                        will be multiplied to the retail price.'),
  value_type=TunableInterval(description='\n                        The maximum modifier multiplied to the retail price based on the provided state value\n                        ',
  tunable_type=float,
  default_lower=1,
  default_upper=1)), 
         stored_cas_parts=TunableList(description='\n                If tuned, cas parts which will be stored on the object. This\n                part can then be used later by systems like object rewards.\n                ',
  tunable=(TunableCasPart())), 
         simoleon_value_skill_curve=OptionalTunable(description='\n                If enabled, specify a skill-driven multiplier to adjust the\n                value of the final product.\n                ',
  tunable=TunableStatisticModifierCurve.TunableFactory(description="\n                    Allows you to adjust the final value of the object based on\n                    the Sim's level of a given skill.\n                    ",
  axis_name_overrides=('Skill Level', 'Simoleon Multiplier'),
  locked_args={'subject': ParticipantType.Actor})), 
         masterworks=OptionalTunable(TunableTuple(description='\n                    If the result of this recipe can be a masterwork (i.e. a\n                    masterpiece for paintings), this should be enabled.\n                    ',
  base_test=event_testing.tests.TunableTestSet(description="\n                        This is the initial gate for a recipe to result in a masterwork.\n                        If this test doesn't pass, we don't even attempt to be a masterwork.\n                        "),
  base_chance=Tunable(description='\n                        Once the Base Test passes, this will be the base chance\n                        that this recipe will result in a masterwork.\n                        0.0 is 0% chance\n                        1.0 is 100% chance\n                        ',
  tunable_type=float,
  default=0.25),
  multiplier_tests=(TunableList(TunableTuple(description='\n                        When deciding if this recipe will result in a masterwork, we run through each test in this list. IF the test passes, its multiplier will be applied to the Base Chance.\n                        ',
  multiplier=Tunable(description='\n                            This is the multiplier that will be applied to the Base Chance if these tests pass.\n                            ',
  tunable_type=float,
  default=1),
  tests=(event_testing.tests.TunableTestSet())))),
  skill_adjustment=Tunable(description="\n                        The masterwork chance adjustment based on the effective skill\n                        level. For each level higher than the requires skill of the recipe,\n                        the masterwork chance will be increased by this.\n                        There is no penalty if, somehow, the required skill is greater\n                        than the effective skill of the Sim.\n                        Example:\n                        Assume you're level 10 writing skill and you're crafting a\n                        book that requires level 4 writing skill. Also assume skill_adjustment\n                        is tuned to 0.05 and the base_chance is set to 0.25.\n                        The differences in skill is 10 (your skill) - 4 (required skill) = 6 \n                        Then, take this difference, 6 * 0.05 (skill_adjustment) = 0.3\n                        The base chance, 0.25 + 0.3 = 0.55. 55% chance of this being a masterwork.\n                        ",
  tunable_type=float,
  default=0.0),
  simoleon_value_multiplier=TunableInterval(description='\n                        The amount by which the final simoleon value of the object will be multiplied if it is a masterwork.\n                        The multiplier is a random number between the lower and upper bounds, inclusively.\n                        ',
  tunable_type=float,
  default_lower=1,
  default_upper=1))), 
         description=description, **kwargs)


class RecipeIngredients(TunableTuple):

    def __init__(self, description='Ingredients and how they are to be used in this recipe', **kwargs):
        (super().__init__)(all_ingredients_required=Tunable(description='\n                If checked recipe will not be available unless all \n                ingredients are found on the sim inventory or the fridge\n                inventory.\n                ',
  tunable_type=bool,
  default=False), 
         ingredient_list=TunableList(description='\n                List of ingredients the recipe can use\n                ',
  tunable=TunableVariant(description='\n                    Possible ingredient mapping by object definition of by \n                    catalog object Tag.\n                    ',
  ingredient_by_definition=IngredientRequirementByDef.TunableFactory(ingredient_override=(True, )),
  ingredient_by_tag=(IngredientRequirementByTag.TunableFactory()))), 
         missing_ingredient_tooltip_style=TunableEnumEntry(description='\n                Style of tooltip to display whenever the recipe its\n                missing its ingredients on the recipe picker. \n                Default will show the ingredient list with its ingredient\n                count.\n                This will only override the recipe picker tooltip, the \n                pie menu picker will display the ingredients as its the\n                only way to communicate the ingredient information.\n                ',
  tunable_type=IngredientTooltipStyle,
  default=(IngredientTooltipStyle.DEFAULT_MISSING_INGREDIENTS)), 
         ingredients_save=OptionalTunable(description='\n                If enabled, ingredients used in crafting will have chance to not be consumed.\n                It will also test against certain conditions\n                ',
  tunable=TunableTuple(save_chance=SuccessChance.TunableFactory(description='\n                        Percent chance that ALL ingredients will not be consumed.\n                        '),
  tests=TunableTestSet(description='\n                        A set of tests that must pass for ingredients save to be applied.\n                        '),
  notification=OptionalTunable(description='\n                        The notification to show when ingredients are not consumed.\n                        ',
  tunable=(TunableUiDialogNotificationSnippet())),
  balloon=OptionalTunable(description='\n                        The balloon to show when ingredients are not consumed.\n                        ',
  tunable=(TunableBalloon())))), 
         return_on_cancel=Tunable(description='\n                If checked, a cancelled crafting process will attempt to\n                return the ingredients back to the owner.  If the owner is\n                not available, nothing will be done.\n                ',
  tunable_type=bool,
  default=False), 
         description=description, **kwargs)


class Phase(HasTunableReferenceFactory, HasTunableFactory, metaclass=TunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.RECIPE)):
    debug_name = 'uninitialized'
    TURN_BASED = 'turn_based'
    PROGRESS_BASED = 'progress_based'
    INSTANCE_SUBCLASSES_ONLY = True
    INSTANCE_TUNABLES = {'super_affordance':SuperInteraction.TunableReference(description='\n            Super-affordance that manages this phase of the recipe.\n            ',
       allow_none=True), 
     'phase_interaction_name_override':OptionalTunable(description="\n            The localized name that will display in the UI instead of the\n            recipe's Phase Interaction Name property.\n            ",
       tunable=sims4.localization.TunableLocalizedStringFactory()), 
     'target_ico':Tunable(description="\n            This phase targets the last object created by the recipe, so don't\n            run autonomy to find it.\n            ",
       tunable_type=bool,
       default=False), 
     '_object_info':TunableVariant(description='\n            If this phase creates an object, use this definition.\n            ',
       locked_args={'none':None, 
      'use_final_product':DEFAULT},
       literal=TunableRecipeObjectInfo(description='\n                If this phase creates an object, use this definition.\n                '),
       default='none'), 
     '_anim_overrides':OptionalTunable(description='\n            Animation overrides that get passed to the Super Affordance tied to\n            this phase. Example: Each recipe may need to use a different prop\n            in a generic SI, such as roasting food on the campfire. This allows\n            us to tune the props, etc. on the recipe instead of the SI.\n            ',
       tunable=TunableAnimationOverrides()), 
     '_cancel_phase_name':TunableEnumEntry(description='\n            The name of the phase to run if the crafting process is canceled\n            during this phase.  May be None.\n            ',
       tunable_type=PhaseName,
       default=None), 
     'loop_by_orders':Tunable(description='\n            Should loop in the phase if multiple orders?\n            ',
       tunable_type=bool,
       default=False), 
     'point_of_no_return':Tunable(description='\n            When crafting get to this phase, the final product will be created\n            no matter cancel SI or not\n            ',
       tunable_type=bool,
       default=False), 
     'phase_display_name':OptionalTunable(description="\n            If enabled, display the phase's name in the interaction queue.\n            ",
       tunable=TunableLocalizedString(description="\n                The phase's display name in the interaction queue.\n                ")), 
     'is_visible':Tunable(description='\n            If this phase will show on crafting quality UI\n            ',
       tunable_type=bool,
       default=False), 
     'completion':TunableVariant(description="\n            Controls how the phase completes, either when turns have elapsed or\n            based on the crafting progress statistic maxing out.  If the super\n            interaction for the phase isn't looping or staging, this value is\n            ignored.\n            ",
       locked_args={TURN_BASED: TURN_BASED, 
      PROGRESS_BASED: PROGRESS_BASED},
       default=TURN_BASED)}
    FACTORY_TUNABLES = {'next_phases': TunableList(description='\n            The names of the phases that can come next.  If empty, this will be the\n            final phase.\n            ',
                      tunable=(TunableEnumEntry(PhaseName, None)))}
    FACTORY_TUNABLES.update(INSTANCE_TUNABLES)

    def __init__(self, *, recipe, phase_id, **kwargs):
        (super().__init__)(**kwargs)
        self.recipe = recipe
        self.id = phase_id

    def recipe_tuning_loaded(self):
        recipe = self.recipe
        next_phases = []
        for name in self.next_phases:
            if name in recipe.phases:
                next_phases.append(recipe.phases[name])
            else:
                logger.error("Unknown phase '{}' specified in next_phase_names for phase '{}' in '{}'.", name, self.id, recipe)

        self.next_phases = next_phases
        if self._cancel_phase_name is None:
            self.cancel_phase = None
        else:
            if self._cancel_phase_name in recipe.phases:
                self.cancel_phase = recipe.phases[self._cancel_phase_name]
            else:
                self.cancel_phase = None
                logger.error("Unknown phase '{}' specified for cancel_phase_name for phase '{}' in '{}'.", self._cancel_phase_name, self.id, recipe)

    @property
    def interaction_name(self):
        if self.phase_interaction_name_override is not None:
            return self.phase_interaction_name_override
        return self.recipe.phase_interaction_name

    @property
    def object_info(self):
        object_info = self._object_info
        if object_info is None:
            return
        if object_info is DEFAULT:
            return self.recipe.final_product
        return object_info

    @property
    def anim_overrides(self):
        return self._anim_overrides

    @property
    def object_info_is_final_product(self):
        return self._object_info is DEFAULT

    @property
    def num_turns(self):
        return self._num_turns

    @property
    def one_shot(self):
        return self.super_affordance.one_shot

    @property
    def turn_based(self):
        if self.one_shot:
            return False
        return self.completion == self.TURN_BASED

    @property
    def progress_based(self):
        if self.one_shot:
            return False
        return self.completion == self.PROGRESS_BASED

    def __repr__(self):
        return '<{} {}>'.format(type(self).__name__, self.id)

    @property
    def allows_multiple_orders(self):
        return False

    @property
    def repeat_on_resume(self):
        from crafting.crafting_interactions import CraftingPhaseSuperInteractionMixin
        if issubclass(self.super_affordance, CraftingPhaseSuperInteractionMixin):
            if self.super_affordance.advance_phase_on_resume:
                return False
        return True


class SimplePhase(Phase):
    content_set = None
    _num_turns = 0
    INSTANCE_TUNABLES = {'multiple_order_tuning': Tunable(description='\n            Sets whether a stage is compatible with multiple orders\n            ',
                                tunable_type=bool,
                                default=False)}
    FACTORY_TUNABLES = {}
    FACTORY_TUNABLES.update(INSTANCE_TUNABLES)

    @property
    def allows_multiple_orders(self):
        return self.multiple_order_tuning


class MultiStagePhase(Phase):
    INSTANCE_TUNABLES = {'multiple_order_tuning': OptionalTunable(TunableTuple(min_turns_required=Tunable(description='\n            Minimum pips needed for adding more orders.\n            ',
                                tunable_type=int,
                                default=0)))}
    FACTORY_TUNABLES = {'content_set':ContentSet.TunableFactory(description='\n        A list of interactions available to the player as recipe actions,\n        boosters, and flourishes.\n        ',
       locked_args={'phase_tuning': None}), 
     '_num_turns':Tunable(description='\n        Number of turns (number of mixer interactions that must be performed) for this phase.\n        ',
       tunable_type=int,
       default=3)}
    FACTORY_TUNABLES.update(INSTANCE_TUNABLES)

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self.content_set = self.content_set()
        num_phases = self.content_set.num_phases
        if num_phases > 0:
            self._num_turns = num_phases

    @property
    def turns(self):
        pass

    @property
    def allows_multiple_orders(self):
        return self.multiple_order_tuning is not None


class TunablePhaseVariant(TunableVariant):

    def __init__(self, description='The information for a single phase of a recipe.', **kwargs):
        (super().__init__)(description=description, simple_phase=SimplePhase.TunableFactory(), 
         simple_phase_ref=SimplePhase.TunableReferenceFactory(reload_dependent=True), 
         multi_stage_phase=MultiStagePhase.TunableFactory(), 
         multi_stage_phase_ref=MultiStagePhase.TunableReferenceFactory(reload_dependent=True), **kwargs)


GROUP_RESTAURANT = 'Restaurant'
GROUP_PROCESS = 'Crafting Process'

class Recipe(metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.RECIPE)):
    INSTANCE_TUNABLES = {'name':TunableLocalizedStringFactory(description='\n            The name of this recipe.\n            ',
       export_modes=ExportModes.All,
       tuning_group=GroupNames.CORE), 
     'recipe_description':TunableLocalizedStringFactory(description="\n            The recipe's description.\n            ",
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.CORE), 
     'final_product':TunableRecipeObjectInfo(description='\n            The final product of the crafting process.\n            ',
       optional_create=False,
       tuning_group=GroupNames.CORE), 
     'base_recipe':OptionalTunable(description='\n            If set, the single serving counterpart for this recipe\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.RECIPE))),
       tuning_group=GroupNames.CORE), 
     'phase_interaction_name':TunableLocalizedStringFactory(description="\n            The name of each phase's interaction.\n            ",
       tuning_group=GROUP_PROCESS), 
     '_first_phases':TunableList(description='\n            The names of the phases that can be done first.  This cannot be empty.\n            ',
       tunable=TunableEnumEntry(PhaseName, default=None),
       tuning_group=GROUP_PROCESS), 
     '_phases':TunableMapping(description='\n            The phases that make up this recipe.\n            ',
       key_type=TunableEnumEntry(PhaseName, None),
       value_type=TunablePhaseVariant(),
       tuning_group=GROUP_PROCESS), 
     'multiple_order_crafting_phase':OptionalTunable(description='\n            The phase to jump to if this recipe is ordered while the Sim is\n            already crafting something. This phase needs to be the same phase\n            that creates the final product or earlier.\n            ',
       tunable=TunableEnumEntry(description='\n                The phase, or earlier, when the Sim creates the final product.\n                ',
       tunable_type=PhaseName,
       default=None),
       tuning_group=GROUP_PROCESS), 
     'resume_affordance':OptionalTunable(description='\n            The interaction to use when resuming crafting this recipe.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
       class_restrictions=('CraftingResumeInteraction', )),
       tuning_group=GROUP_PROCESS), 
     'push_consume':Tunable(description='\n            Whether to push the consume after finish the recipe.\n            ',
       tunable_type=bool,
       default=True,
       tuning_group=GROUP_PROCESS), 
     'push_consume_threshold':OptionalTunable(description='\n            If Push Consume is checked and this threshold is enabled, the consume affordance will\n            only be pushed if the threshold is met.\n            ',
       tunable=TunableTuple(description='\n                The commodity/threshold pair.\n                ',
       commodity=TunableReference(description='\n                    The commodity to be tested.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
       class_restrictions='Commodity'),
       threshold=TunableThreshold(description='\n                    The threshold at which to remove this bit.\n                    ')),
       tuning_group=GROUP_PROCESS), 
     'resumable':Tunable(description='\n            If set to False, this recipe is not resumable, for example drinks made at bar.\n            ',
       tunable_type=bool,
       default=True,
       tuning_group=GROUP_PROCESS), 
     'resumable_by_different_sim':Tunable(description='\n            If set, this recipe can be resumed by a sim other than the one that started it\n            ',
       tunable_type=bool,
       default=False,
       tuning_group=GROUP_PROCESS), 
     '_quality_control_stat':OptionalTunable(description='\n            When set, this is the statistic governing the quality of the crafted object when completed when\n            skill adjustment is done on the final product.\n            If unset, the statistic used is the skill specified in the skill test, if there is one set.\n            ',
       tunable=TunableTuple(statistic=TunableReference(description='\n                    The statistic to use for quality control.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
       class_restrictions=('RankedStatistic', 'Skill')),
       base_level=TunableRange(description='\n                    The base level to start skill adjustment at.\n                    ',
       tunable_type=int,
       minimum=0,
       default=0))), 
     'use_ingredients':OptionalTunable(description='\n            If checked recipe will have the ability to use ingredients to \n            improve its quality when prepared.\n            ',
       tunable=RecipeIngredients(description='\n                Ingredient data for a recipe.\n                '),
       tuning_group=GROUP_PROCESS), 
     'ingredient_cost_only_ingredients':OptionalTunable(description="\n            If checked, and running a ingredient_cost_only interaction, this recipe will use\n            this list of ingredients instead of 'use_ingredients'\n            ",
       tunable=RecipeIngredients(description='\n                Ingredient data for a recipe.\n                '),
       tuning_group=GROUP_PROCESS), 
     'skill_test':OptionalTunable(description='\n            The skill level required to use this recipe.\n            ',
       tunable=statistics.skill_tests.SkillRangeTest.TunableFactory(),
       tuning_group=GroupNames.TESTS), 
     'additional_tests':event_testing.tests.TunableTestSetWithTooltip(tuning_group=GroupNames.TESTS), 
     'additional_tests_ignored_on_resume':Tunable(description='\n            If set, additional tests are ignored when testing to see if a recipe\n            can be resumed.\n            ',
       tunable_type=bool,
       default=False,
       tuning_group=GroupNames.TESTS), 
     'utility_info':OptionalTunable(description='\n            Tuning that specifies which utilities this recipe requires to\n            be made/cooked.\n            ',
       tunable=TunableMapping(key_type=TunableEnumEntry(description='\n                    The utility which requires to be run.\n                    ',
       tunable_type=Utilities,
       default=None),
       value_type=TunableTuple(description='\n                    Data associated with utility which requires to be run.\n                    ',
       shutoff_tooltip_override=TunableMapping(description="\n                        Override tooltip to show when recipe cannot be made/cooked due to \n                        utility being shutoff. Otherwise, it'll show generic tooltip.\n                        ",
       key_type=TunableEnumEntry(description='\n                            Utility shutoff reason which the tooltip will be overridden.\n                            ',
       tunable_type=UtilityShutoffReasonPriority,
       default=(UtilityShutoffReasonPriority.NO_REASON),
       invalid_enums=(
      UtilityShutoffReasonPriority.NO_REASON,)),
       value_type=TunableLocalizedStringFactory(description='\n                            An override tooltip to show.\n                            ')))),
       tuning_group=GroupNames.TESTS), 
     '_retail_price':Tunable(description='\n            Retail price of the recipe. \n            This is not the total price of the recipe.  The total price of the \n            recipe will be _retail_price+delta_ingredient_price\n            ',
       tunable_type=int,
       default=0,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.PRICE), 
     'restaurant_base_price':Tunable(description='\n            Restaurant base price of the recipe. If this recipe is chosen for\n            the daily item the final price of this recipe is \n            final price = restaunt_base_price * RestaurantTuning.DAILY_SPECIAL_DISCOUNT\n            ',
       tunable_type=int,
       default=1,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.PRICE), 
     'crafting_cost':TunableVariant(description='\n            This determines the amount of money the Sim will have to pay in\n            order to craft this recipe.\n            \n            Crafting Discount is multiplied by the Retail Price to determine the\n            amount of money the Sim must pay to craft this.\n            \n            Flat Fee is just a flat fee the Sim must pay to craft this.\n            ',
       discount=Tunable(description='\n                This number is multiplied by the Retail Price to to determine\n                the amount of money the Sim will have to pay in order to craft this.\n                ',
       tunable_type=float,
       default=0.8),
       flat_fee=Tunable(description='\n                This is a flat amount of simoleons that the Sim will have to pay\n                in order to craft this.\n                ',
       tunable_type=int,
       default=0),
       default='discount',
       tuning_group=GroupNames.PRICE), 
     'crafting_bucks_cost':TunableList(description='\n            This determines the amount of bucks the Sim will have to pay in\n            order to craft this recipe.\n            \n            Crafting Discount is multiplied by the Retail Price to determine the\n            amount of bucks the Sim must pay to craft this.\n            \n            Flat Fee is just a flat fee the Sim must pay to craft this.\n            ',
       tunable=TunableTuple(description='\n                ',
       bucks_type=TunableEnumEntry(description='\n                    The type of Bucks to use.\n                    ',
       tunable_type=BucksType,
       default=(BucksType.INVALID)),
       amount=TunableVariant(description='\n                    This determines the amount of bucks the Sim will have to pay in\n                    order to craft this recipe.\n                    \n                    Crafting Discount is multiplied by the Retail Price to determine the\n                    amount of money the Sim must pay to craft this.\n                    \n                    Flat Fee is just a flat fee the Sim must pay to craft this.\n                    ',
       discount=Tunable(description='\n                        This number is multiplied by the Retail Price to to determine\n                        the amount of bucks the Sim will have to pay in order to craft this.\n                        ',
       tunable_type=float,
       default=0.8),
       flat_fee=Tunable(description='\n                        This is a flat amount of bucks that the Sim will have to pay\n                        in order to craft this.\n                        ',
       tunable_type=int,
       default=0),
       default='discount'),
       refund_on_cancel=Tunable(description='\n                    If checked, a cancelled crafting process will attempt to\n                    return all buck costs back to the owner.  If the owner is\n                    not available, nothing will be done.\n                    ',
       tunable_type=bool,
       default=False)),
       tuning_group=GroupNames.PRICE), 
     'delta_ingredient_price':Tunable(description='\n            Delta price of a recipe will be a delta value that will increase\n            or decrease depending on how many ingredients for the recipe the \n            sim has.\n            e.g  For a 3 ingredient recipe:\n            - If no ingredient is found,  price will be retail_price + delta\n            - If 1 ingredient is found,  price will be retail_price + 2/3 of \n            delta\n            - If 2 ingredient is found,  price will be retail_price + 1/3 of \n            delta\n            - If 3 ingredient is found,  price will be retail_price\n            ',
       tunable_type=int,
       default=0,
       tuning_group=GroupNames.PRICE), 
     '_no_initial_charge':Tunable(description='\n            If set, there is no initial charge for making this recipe\n            ',
       tunable_type=bool,
       default=False,
       tuning_group=GroupNames.PRICE), 
     'icon_override':TunableResourceKey(description='\n            This will override the default icon for this recipe.\n            ',
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       export_modes=ExportModes.All,
       allow_none=True,
       tuning_group=GroupNames.UI), 
     'thumbnail_geo_state':Tunable(description='\n            The geo state name override for recipe picker thumbnail generation.\n            If empty, it will use default catalog thumbnail.\n            ',
       tunable_type=str,
       default='',
       allow_empty=True,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.UI), 
     'thumbnail_material_state':Tunable(description='\n            The material state name override for recipe picker thumbnail generation.\n            If empty, it will use default catalog thumbnail.\n            ',
       tunable_type=str,
       default='',
       allow_empty=True,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.UI), 
     'visible_as_subrow':Tunable(description='\n            If this recipe has base recipe, this boolean will decide whether or\n            not this recipe will show up in the subrow entry of the base\n            recipe.\n            ',
       tunable_type=bool,
       default=True,
       tuning_group=GroupNames.UI), 
     'linked_recipe_override':OptionalTunable(description='\n            If specified, overrides the linked recipe in the picker to use this\n            recipe instead of the base_recipe. \n            \n            Example: Wedding cakes have styles, where each style has variants. But the single serving\n            versions (used as the base_recipe) of the cake styles are different depending on the variant.\n            We still want to have all the cake variants to fall under one row vs having a row for each \n            single serving. \n            ',
       tunable=TunableReference(description='\n                Reference to the recipe you want to use as the linked recipe. \n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.RECIPE))),
       tuning_group=GroupNames.UI), 
     'multi_serving_name':OptionalTunable(description="\n            The string that shows up in the ObjectPicker when this recipe is a\n            multi_serving. Please use 'use_recipe_name' when it's a single\n            serving.\n            ",
       tunable=TunableLocalizedStringFactory(description='\n                The name of multiple serving to show in the sub row of ObjectPicker.\n                '),
       enabled_name='use_multi_serving_name',
       disabled_name='use_recipe_name',
       tuning_group=GroupNames.UI), 
     'masterwork_name':OptionalTunable(description='\n            If enabled, craftables of this type in the masterwork state will\n            have this text treatment.\n            ',
       tunable=TunableLocalizedString(description='\n                If this can be a masterwork, what should its masterwork state be\n                called? Usually this is just Masterpiece.\n                '),
       tuning_group=GroupNames.UI), 
     'hidden_until_unlock':Tunable(description="\n            If checked, this recipe will not show up in picker or piemenu if\n            it's not unlocked, either by skill up, or unlock outcome, or\n            entitlement.\n            ",
       tunable_type=bool,
       default=True,
       tuning_group=GroupNames.UI), 
     'crafted_by_text':TunableLocalizedStringFactory(description="\n            Text that describes who made it, e.g. 'Made By: <Sim>'. Loc\n            parameter 0 is the Sim crafter.\n            ",
       tuning_group=GroupNames.UI), 
     'fallback_crafted_by_text':OptionalTunable(description='\n            If enabled when a recipe is downloaded from the gallery and a \n            profane name is found on its name this text will replace the\n            crafted by text.\n            If disabled no crafted by will be displayed on the tooltip.\n            ',
       tunable=TunableLocalizedString(description="\n                Fallback text to describe who made this if a profanity is \n                found on the name.\n                e.g. 'Made By: John Doe'\n                "),
       tuning_group=GroupNames.UI), 
     'crafted_with_text':OptionalTunable(description='\n            If enabled  this text will be appended to the\n            crafted by text to show ingredients list.\n            If disabled no crafted with will be displayed on the tooltip.\n            ',
       tunable=TunableLocalizedStringFactory(description="\n                Text that describes ingredients use to make it,\n                e.g. 'Made with: <IngredientsList>'. Loc\n                parameter 0 is the Ingredients List.\n                "),
       tuning_group=GroupNames.UI), 
     'value_text':OptionalTunable(description="\n            If enabled, specify text for a tooltip line item for the item's\n            value.\n            ",
       tunable=TunableLocalizedStringFactory(description='\n                Text that describes the value in the tooltip. \n                e.g.\n                Value: {0.Money}\n                '),
       tuning_group=GroupNames.UI), 
     'time_until_spoiled_string_override':OptionalTunable(description='\n            If enabled, override the default until spoiled string\n            with this string.\n            ',
       tunable=TunableLocalizedString(),
       tuning_group=GroupNames.UI), 
     'show_spoiled_quality_description':Tunable(description='\n            Whether this item will display the quality description field in\n            the tooltip when spoiled.\n            ',
       tunable_type=bool,
       default=True,
       tuning_group=GroupNames.UI), 
     'spoil_time_commodity_override':OptionalTunable(description='\n            Override the commodity that is tracked for the spoil time in the tooltip instead of Freshness. Example, track\n            time until ready on the bbq pit.\n            ',
       tunable=TunableTuple(description='\n                Override state to track for the spoil time instead of normal freshness\n                ',
       state_to_track=TunableStateValueReference(description='\n                    The object state used to track spoil time instead of\n                    the state tuned in CraftingTuning.\n                    ',
       class_restrictions=CommodityBasedObjectStateValue),
       commodity_check_operator=TunableOperator(description="\n                    The operator to use for comparing the tuned commodity to the state's bounds to form the \n                    time calculation. Ie. greater than if the time should be how long it takes the commodity to count up to\n                    the state's bound.\n                    ",
       default=(sims4.math.Operator.LESS))),
       tuning_group=GroupNames.UI), 
     'subrow_sort_id':Tunable(description='\n            Number to sort the row by in the list of subrows if other sort criteria is the same.\n            ',
       tunable_type=int,
       default=0,
       tuning_group=GroupNames.UI), 
     'group_recipe_override':OptionalTunable(description='\n            Override the data for the RecipePicker that is displayed on the UI expandable button which displays linked recipes.\n            Linked recipes are recipes that have a specified a base recipe. This should be used on the base recipe.\n            ',
       tunable=TunableTuple(description='\n                Override details displayed on the button to expand to display more recipes\n                ',
       group_name=TunableLocalizedStringFactory(description='\n                    The name to display on the group button.\n                    '),
       group_skill_level=Tunable(description='\n                    Override to display a skill level on the group button.\n                    ',
       tunable_type=int,
       default=0),
       group_tooltip=TunableLocalizedStringFactory(description='\n                    Override the tooltip to display on the group button.\n                    ')),
       tuning_group=GroupNames.UI), 
     'available_in_restaurant':Tunable(description='\n            If checked, this recipe will show up in restaurant menu. \n            ',
       tunable_type=bool,
       default=True,
       export_modes=ExportModes.All,
       tuning_group=GROUP_RESTAURANT), 
     'restaurant_menu_icon_definition':TunableReference(description='\n            The object definition used to get thumbnail for menu icon. If\n            recipe is used for restaurant, either this or icon_override need to\n            be filled.\n            ',
       manager=services.definition_manager(),
       export_modes=ExportModes.All,
       tuning_group=GROUP_RESTAURANT,
       allow_none=True), 
     'food_poisoning_chance':OptionalTunable(description='\n            If enabled, a tunable chance that food will be contaminated with\n            food poisoning upon creation.\n            ',
       tunable=SuccessChance.TunableFactory(description='\n                Chance that the created food will be contaminated with food\n                poisoning.\n                '),
       tuning_group=GROUP_RESTAURANT), 
     'photo_definition':OptionalTunable(description='\n            If enabled, the final product created from this recipe, will create\n            the tuned catalog instance here while taken phote by special take\n            photo interaction. This is currently used by experimental food take\n            picture feature. \n            http://ears-simssql-vm.rws.ad.ea.com/Sims4/Design/DetailedView.aspx?designID=13389\n            ',
       tunable=TunableReference(description="\n                The object definition to use taking picture of this recipe's\n                final product\n                ",
       manager=(services.definition_manager())),
       tuning_group=GROUP_RESTAURANT), 
     'recipe_difficulty':TunableEnumEntry(description="\n            The difficulty of this recipe. This, along with the chef's skill level,\n            affects how well the food turns out.\n            ",
       tunable_type=RecipeDifficulty,
       default=RecipeDifficulty.NORMAL,
       binary_type=EnumBinaryExportType.EnumUint32,
       tuning_group=GROUP_RESTAURANT,
       export_modes=ExportModes.All), 
     'recipe_tags':TunableSet(description='\n            Tags for the recipe.\n            ',
       tunable=TunableEnumWithFilter(tunable_type=Tag,
       filter_prefixes=[
      'recipe'],
       default=(Tag.INVALID),
       invalid_enums=(
      Tag.INVALID,),
       pack_safe=True,
       binary_type=(EnumBinaryExportType.EnumUint32)),
       export_modes=ExportModes.All,
       tuning_group=GroupNames.TAG), 
     'use_active_household_as_owner':Tunable(description="\n            If enabled the ownership of this object will be given to the active\n            household instead of the crafter household.  This should be used\n            in cases where npc's are creating craftables on a player household\n            (like spooky party crafting), but the active househould should \n            still have all live drag and ownership restrictions over the \n            object.\n            ",
       tunable_type=bool,
       default=False), 
     'anim_overrides':OptionalTunable(description='\n            If enabled, specify animation overrides for this recipe.\n            ',
       tunable=TunableAnimationOverrides()), 
     'vfx_overrides':TunableMapping(description='\n            Mapping of VFX name-> VFX name to override the VFX played on a \n            craftable object by recipe.\n            ',
       key_type=Tunable(description='\n                The name of the effect be overwritten.\n                ',
       tunable_type=str,
       default=''),
       value_type=Tunable(description='\n                The name of the effect to play instead.\n                ',
       tunable_type=str,
       default='')), 
     'autonomy_weight':Tunable(description='\n            The relative weight for autonomy to choose to make or order this recipe\n            ',
       tunable_type=float,
       default=0), 
     'buff_weight_multipliers':TunableBuffWeightMultipliers(), 
     'base_recipe_category':OptionalTunable(description='\n            The pie menu category of the base recipe if the picker dialog to\n            choose recipes is tuned to use pie menu formation.\n            ',
       tunable=TunableReference(description='\n                Pie menu category for pie menu mixers.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.PIE_MENU_CATEGORY)))), 
     'skill_loot_data':TunableSkillLootData(description='\n            Loot Data for DynamicSkillLootOp. This will only be used if in the\n            loot list of the outcome there is a dynamic loot op.\n            '), 
     'entitlement':OptionalTunable(description='\n            If enabled, this recipe is locked by an entitlement. Otherwise, this\n            recipe is available to all players.\n            ',
       tunable=TunableEntitlement(description='\n                Entitlement required to use this recipe.\n                ')), 
     'mood_list':TunableList(description='\n            A list of possible moods this Recipe may associate with. Note that\n            this list is for coloring-purposes only. Interaction availability\n            testing is relegated to the individual mood tests on the\n            interaction. Future refactoring necessary.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.MOOD)))), 
     'linked_recipes_map':TunableMapping(description='\n            Mapping of grab serving affordance to the recipes it can generate.\n            If a multiserve recipe can create multiple recipes, the \n            affordances that generate those recipes need to be tuned here.\n            This tunable should only be tuned on multiserve recipes.\n            ',
       key_type=TunableReference(description='\n                The affordance that will trigger the linked recipe when\n                selected.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
       class_restrictions='GrabServingSuperInteraction',
       pack_safe=True),
       value_type=TunableReference(description='\n                Recipe to be generated by the crafting process when linked\n                affordance is selected.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.RECIPE)),
       pack_safe=True)), 
     'unlock_as_new':Tunable(description="\n            If set, this recipe gets marked as a new when unlocked.  This has very specific use cases and should only be\n            used if there is a system in place to unmark it, since it has implications on save data persistence.\n    \n            e.g. This is used for potions, because the spellbook implementation can mark a 'new' potion as viewed when  \n            the player opens the spellbook and views the new potion entry.\n            ",
       tunable_type=bool,
       default=False,
       tuning_group=GroupNames.SPECIAL_CASES), 
     'food_restriction_ingredients':TunableList(description="\n            The food restriction ingredients that this recipe is implied to use.\n            \n            Note that this is different from object based ingredients that are\n            consumed as part of the creation process (which is tuned via \n            'Use Ingredients' on this recipe).\n            ",
       tunable=TunableEnumEntry(tunable_type=(FoodRestrictionUtils.FoodRestrictionEnum),
       default=(FoodRestrictionUtils.FoodRestrictionEnum.INVALID),
       invalid_enums=(
      FoodRestrictionUtils.FoodRestrictionEnum.INVALID,)))}

    @classmethod
    def _tuning_loaded_callback--- This code section failed: ---

 L.1319         0  BUILD_LIST_0          0 
                2  LOAD_DEREF               'cls'
                4  STORE_ATTR               _visible_phase_sequence

 L.1320         6  LOAD_CLOSURE             'cls'
                8  BUILD_TUPLE_1         1 
               10  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               12  LOAD_STR                 'Recipe._tuning_loaded_callback.<locals>.<dictcomp>'
               14  MAKE_FUNCTION_8          'closure'
               16  LOAD_DEREF               'cls'
               18  LOAD_ATTR                _phases
               20  LOAD_METHOD              items
               22  CALL_METHOD_0         0  '0 positional arguments'
               24  GET_ITER         
               26  CALL_FUNCTION_1       1  '1 positional argument'
               28  LOAD_DEREF               'cls'
               30  STORE_ATTR               phases

 L.1322        32  BUILD_LIST_0          0 
               34  STORE_FAST               'first_phases'

 L.1323        36  SETUP_LOOP           94  'to 94'
               38  LOAD_DEREF               'cls'
               40  LOAD_ATTR                _first_phases
               42  GET_ITER         
               44  FOR_ITER             92  'to 92'
               46  STORE_FAST               'name'

 L.1324        48  LOAD_FAST                'name'
               50  LOAD_DEREF               'cls'
               52  LOAD_ATTR                phases
               54  COMPARE_OP               in
               56  POP_JUMP_IF_FALSE    76  'to 76'

 L.1325        58  LOAD_FAST                'first_phases'
               60  LOAD_METHOD              append
               62  LOAD_DEREF               'cls'
               64  LOAD_ATTR                phases
               66  LOAD_FAST                'name'
               68  BINARY_SUBSCR    
               70  CALL_METHOD_1         1  '1 positional argument'
               72  POP_TOP          
               74  JUMP_BACK            44  'to 44'
             76_0  COME_FROM            56  '56'

 L.1327        76  LOAD_GLOBAL              logger
               78  LOAD_METHOD              error
               80  LOAD_STR                 "Unknown phase '{}' specified in first_phases for recipe '{}'."
               82  LOAD_FAST                'name'
               84  LOAD_DEREF               'cls'
               86  CALL_METHOD_3         3  '3 positional arguments'
               88  POP_TOP          
               90  JUMP_BACK            44  'to 44'
               92  POP_BLOCK        
             94_0  COME_FROM_LOOP       36  '36'

 L.1328        94  LOAD_FAST                'first_phases'
               96  LOAD_DEREF               'cls'
               98  STORE_ATTR               first_phases

 L.1331       100  LOAD_CONST               0
              102  LOAD_CONST               ('ChooseDeliverySuperInteraction',)
              104  IMPORT_NAME_ATTR         crafting.serving_interactions
              106  IMPORT_FROM              ChooseDeliverySuperInteraction
              108  STORE_FAST               'ChooseDeliverySuperInteraction'
              110  POP_TOP          

 L.1332       112  LOAD_CONST               None
              114  LOAD_DEREF               'cls'
              116  STORE_ATTR               serve_affordance

 L.1333       118  SETUP_LOOP          176  'to 176'
              120  LOAD_DEREF               'cls'
              122  LOAD_ATTR                phases
              124  LOAD_METHOD              values
              126  CALL_METHOD_0         0  '0 positional arguments'
              128  GET_ITER         
            130_0  COME_FROM           162  '162'
            130_1  COME_FROM           150  '150'
              130  FOR_ITER            174  'to 174'
              132  STORE_FAST               'phase'

 L.1334       134  LOAD_FAST                'phase'
              136  LOAD_METHOD              recipe_tuning_loaded
              138  CALL_METHOD_0         0  '0 positional arguments'
              140  POP_TOP          

 L.1339       142  LOAD_FAST                'phase'
              144  LOAD_ATTR                super_affordance
              146  LOAD_CONST               None
              148  COMPARE_OP               is-not
              150  POP_JUMP_IF_FALSE   130  'to 130'
              152  LOAD_GLOBAL              issubclass
              154  LOAD_FAST                'phase'
              156  LOAD_ATTR                super_affordance
              158  LOAD_FAST                'ChooseDeliverySuperInteraction'
              160  CALL_FUNCTION_2       2  '2 positional arguments'
              162  POP_JUMP_IF_FALSE   130  'to 130'

 L.1340       164  LOAD_FAST                'phase'
              166  LOAD_ATTR                super_affordance
              168  LOAD_DEREF               'cls'
              170  STORE_ATTR               serve_affordance
              172  JUMP_BACK           130  'to 130'
              174  POP_BLOCK        
            176_0  COME_FROM_LOOP      118  '118'

 L.1343       176  LOAD_DEREF               'cls'
              178  LOAD_ATTR                first_phases
              180  POP_JUMP_IF_FALSE   198  'to 198'

 L.1344       182  LOAD_DEREF               'cls'
              184  LOAD_METHOD              _build_visible_phase_sequence
              186  LOAD_DEREF               'cls'
              188  LOAD_ATTR                first_phases
              190  LOAD_CONST               0
              192  BINARY_SUBSCR    
              194  CALL_METHOD_1         1  '1 positional argument'
              196  POP_TOP          
            198_0  COME_FROM           180  '180'

 L.1352       198  LOAD_DEREF               'cls'
              200  LOAD_ATTR                use_ingredients
              202  POP_JUMP_IF_FALSE   218  'to 218'
              204  LOAD_DEREF               'cls'
              206  LOAD_ATTR                use_ingredients
              208  LOAD_ATTR                ingredient_list
              210  POP_JUMP_IF_TRUE    218  'to 218'

 L.1353       212  LOAD_CONST               None
              214  LOAD_DEREF               'cls'
              216  STORE_ATTR               use_ingredients
            218_0  COME_FROM           210  '210'
            218_1  COME_FROM           202  '202'

 L.1359       218  LOAD_DEREF               'cls'
              220  LOAD_ATTR                use_ingredients
              222  POP_JUMP_IF_FALSE   246  'to 246'

 L.1360       224  LOAD_GLOBAL              sorted
              226  LOAD_DEREF               'cls'
              228  LOAD_ATTR                use_ingredients
              230  LOAD_ATTR                ingredient_list
              232  LOAD_LAMBDA              '<code_object <lambda>>'
              234  LOAD_STR                 'Recipe._tuning_loaded_callback.<locals>.<lambda>'
              236  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              238  LOAD_CONST               ('key',)
              240  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              242  LOAD_DEREF               'cls'
              244  STORE_ATTR               sorted_ingredient_requirements
            246_0  COME_FROM           222  '222'

 L.1362       246  LOAD_DEREF               'cls'
              248  LOAD_ATTR                ingredient_cost_only_ingredients
          250_252  POP_JUMP_IF_FALSE   276  'to 276'

 L.1363       254  LOAD_GLOBAL              sorted
              256  LOAD_DEREF               'cls'
              258  LOAD_ATTR                ingredient_cost_only_ingredients
              260  LOAD_ATTR                ingredient_list
              262  LOAD_LAMBDA              '<code_object <lambda>>'
              264  LOAD_STR                 'Recipe._tuning_loaded_callback.<locals>.<lambda>'
              266  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              268  LOAD_CONST               ('key',)
              270  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              272  LOAD_DEREF               'cls'
              274  STORE_ATTR               sorted_ingredients_only_requirements
            276_0  COME_FROM           250  '250'

 L.1365       276  SETUP_LOOP          310  'to 310'
              278  LOAD_DEREF               'cls'
              280  LOAD_ATTR                recipe_tags
              282  GET_ITER         
              284  FOR_ITER            308  'to 308'
              286  STORE_FAST               'tag'

 L.1366       288  LOAD_GLOBAL              RECIPE_TAG_TO_TUNING_ID_MAP
              290  LOAD_FAST                'tag'
              292  BINARY_SUBSCR    
              294  LOAD_METHOD              add
              296  LOAD_DEREF               'cls'
              298  LOAD_ATTR                guid64
              300  CALL_METHOD_1         1  '1 positional argument'
              302  POP_TOP          
          304_306  JUMP_BACK           284  'to 284'
              308  POP_BLOCK        
            310_0  COME_FROM_LOOP      276  '276'

Parse error at or near `LOAD_DICTCOMP' instruction at offset 10

    @classmethod
    def _verify_recipe_tuning_callback(cls):
        if cls.use_ingredients:
            for ingredient in cls.use_ingredients.ingredient_list:
                if ingredient is None:
                    logger.error('Recipe {} has unset ingredients', cls.__name__)

            if not cls.use_ingredients.ingredient_list:
                logger.error('Recipe {} has an empty ingredient list and its tuned to use ingredients.', cls.__name__)
            else:
                cls.name or logger.error('Recipe {} does not have a name set', cls.__name__)
            if not cls.phase_interaction_name:
                logger.error('Recipe {} does not have a phase interaction name set', cls.__name__)
        elif cls.available_in_restaurant:
            if cls.restaurant_menu_icon_definition is None and cls.icon_override is None:
                logger.error('{} is available in restaurant, but has no restaurant_menu_icon_definition or icon_override set for menu display', cls.__name__)
        cls._validate_final_product()
        services.get_instance_manager(sims4.resources.Types.RECIPE).add_on_load_complete(cls.validate_base_recipe)

    @classmethod
    def _verify_tuning_callback(cls):
        cls._verify_recipe_tuning_callback()

    @classmethod
    def _validate_final_product(cls):
        if cls.final_product_definition is None:
            return
        supported_states = objects.components.state.get_supported_state(cls.final_product.definition)
        unsupported_values = []
        for state_value in itertools.chain(cls.final_product.initial_states, cls.final_product.apply_states):
            if supported_states is None or state_value.state not in supported_states:
                unsupported_values.append(state_value)

        if unsupported_values:
            if supported_states is None:
                error = "\n    A recipe wants to set one or more state value on its final product, but that\n    object doesn't have a StateComponent.  The recipe shouldn't be trying to set\n    any state values, or the object's tuning should be updated to add these\n    states."
            else:
                error = "\n    A recipe wants to set a state value on its final product, but that object's\n    state component tuning doesn't have an entry for that state.  The recipe\n    shouldn't be trying to set these state values, or the object's tuning should\n    be updated to add these states."
            logger.error('Recipe tuning error:{}\n        Recipe: {}\n        Missing States: {}\n        Final Product: {} ({})'.format(error, cls.__name__, ', '.join(sorted({e.state.__name__ for e in unsupported_values})), cls.final_product.definition.name, cls.final_product.definition.cls.__name__))
        for sa in cls.final_product.super_affordances:
            if sa.consumes_object() or sa.contains_stat(CraftingTuning.CONSUME_STATISTIC):
                logger.error('Recipe: Interaction {} on {} is consume affordance, should tune on ConsumableComponent of the object.', (sa.__name__), (cls.__name__), owner='tastle/cjiang')

    @classmethod
    def validate_for_start_crafting(cls):
        if not cls.first_phases:
            logger.error('Recipe is tuned to be craftable but has no first phases defined: {}', cls)

    @classmethod
    def validate_base_recipe(cls, manager):
        base_recipe = cls.base_recipe
        if base_recipe is not None:
            if cls.hidden_until_unlock != base_recipe.hidden_until_unlock:
                logger.error("Recipe({})'s hidden_until_unlock({}) != base_recipe({})'s hidden_until_unlock({})", cls.__name__, cls.hidden_until_unlock, base_recipe.__name__, base_recipe.hidden_until_unlock)

    @classmethod
    def _build_visible_phase_sequence(cls, phase):
        if phase.is_visible:
            cls._visible_phase_sequence.append(phase)
        if phase.next_phases:
            next_phase = phase.next_phases[0]
            cls._build_visible_phase_sequence(next_phase)

    @classmethod
    def get_multiple_order_crafting_phase(cls):
        if cls.multiple_order_crafting_phase is not None:
            return cls.phases.get(cls.multiple_order_crafting_phase, None)

    @classproperty
    def all_ingredients_required(cls):
        if cls.use_ingredients is None:
            return False
        return cls.use_ingredients.all_ingredients_required and debug_ingredient_requirements

    @classproperty
    def final_product_definition(cls):
        return cls.final_product.definition

    @classproperty
    def final_product_definition_id(cls):
        return cls.final_product.definition.id

    @classproperty
    def has_final_product_definition(cls):
        return cls.final_product.definition is not None

    @classproperty
    def final_product_geo_hash(cls):
        if cls.thumbnail_geo_state:
            return sims4.hash_util.hash32(cls.thumbnail_geo_state)
        return cls.final_product_definition.thumbnail_geo_state_hash

    @classproperty
    def final_product_material_hash(cls):
        if cls.thumbnail_material_state:
            return sims4.hash_util.hash32(cls.thumbnail_material_state)
        return 0

    @classproperty
    def final_product_type(cls):
        return cls.final_product.definition.cls

    @classproperty
    def apply_tags(cls):
        obj_info = cls.final_product
        if obj_info is not None:
            return obj_info.apply_tags
        return set()

    @classmethod
    def get_final_product_quality_adjustment(cls, effective_skill):
        quality_adjustment = cls.final_product.quality_adjustment
        skill_delta = effective_skill - cls.base_quality_control_statistic_level
        quality_value = quality_adjustment.base_quality + skill_delta * quality_adjustment.skill_adjustment
        return quality_value

    @classmethod
    def setup_crafted_object(cls, crafted_object, crafter, is_final_product, random=None):
        cls._setup_crafted_object(crafted_object, crafter, is_final_product, random=random)

    @classmethod
    def _setup_crafted_object(cls, crafted_object, crafter, is_final_product, random=None):
        pass

    @classproperty
    def crafting_price(cls):
        if cls._no_initial_charge:
            return 0
        if isinstance(cls.crafting_cost, int):
            return cls.crafting_cost
        return int(cls._retail_price * cls.crafting_cost)

    @classmethod
    def all_ingredients_available(cls, candidate_ingredients, ingredient_cost_only=False):
        ingredients_requirements_to_use = None
        if ingredient_cost_only and cls.ingredient_cost_only_ingredients is not None:
            ingredients_requirements_to_use = cls.sorted_ingredients_only_requirements
        else:
            if cls.use_ingredients is not None:
                ingredients_requirements_to_use = cls.sorted_ingredient_requirements
            else:
                return True
        ingredients_used = {}
        ingredients_found_count = 0
        ingredients_needed_count = 0
        for tuned_ingredient_factory in ingredients_requirements_to_use:
            ingredient_requirement = tuned_ingredient_factory()
            ingredient_requirement.attempt_satisfy_ingredients(candidate_ingredients, ingredients_used)
            ingredients_found_count += ingredient_requirement.count_satisfied
            ingredients_needed_count += ingredient_requirement.count_required

        return ingredients_found_count >= ingredients_needed_count

    @classproperty
    def crafting_bucks_price(cls):
        costs = {}
        for buck_cost in cls.crafting_bucks_cost:
            amount = 0
            if isinstance(buck_cost.amount, int):
                amount = int(buck_cost.amount)
            else:
                amount = int(cls._retail_price * buck_cost.amount)
            if amount == 0:
                continue
            if buck_cost.bucks_type in costs:
                costs[buck_cost.bucks_type] += amount
            else:
                costs[buck_cost.bucks_type] = amount

        return costs

    @classproperty
    def crafting_bucks_refund_amounts(cls):
        bucks = {}
        for buck_cost in cls.crafting_bucks_cost:
            if buck_cost.amount > 0:
                bucks[buck_cost.bucks_type] = buck_cost.refund_on_cancel

        return bucks

    @classproperty
    def retail_price(cls):
        return cls._retail_price

    @classproperty
    def simoleon_value_modifiers(cls):
        return cls.final_product.simoleon_value_modifiers_map

    @classproperty
    def simoleon_value_skill_curve(cls):
        return cls.final_product.simoleon_value_skill_curve

    @classproperty
    def masterworks_data(cls):
        return cls.final_product.masterworks

    @classproperty
    def quality_control_statistic(cls):
        if cls._quality_control_stat is not None:
            return cls._quality_control_stat.statistic
        return cls.required_skill

    @classproperty
    def base_quality_control_statistic_level(cls):
        if cls._quality_control_stat is not None:
            return cls._quality_control_stat.base_level
        return cls.required_skill_level

    @classproperty
    def required_skill_level(cls):
        if cls.skill_test is not None:
            return cls.skill_test.skill_range_min
        return 0

    @classproperty
    def required_skill(cls):
        if cls.skill_test is not None:
            return cls.skill_test.skill

    @classmethod
    def get_base_recipe(cls):
        return cls.base_recipe or cls

    @classmethod
    def get_linked_recipe(cls, affordance):
        linked_recipe = cls.linked_recipes_map.get(affordance)
        if linked_recipe is None:
            logger.error('Recipe {} is trying to be linked to affordance {}.  This is probably caused by the affordance not tuned on linked recipes mapping on the recipe', cls, affordance, owner='camilogarcia')
            return cls.base_recipe or cls
        return linked_recipe

    @classmethod
    def get_recipe_picker_name(cls, *args):
        if cls.multi_serving_name is not None:
            return (cls.multi_serving_name)(*args)
        return (cls.name)(*args)

    @classmethod
    def get_recipe_name(cls, *args):
        return (cls.name)(*args)

    @classmethod
    def get_display_name(cls, *args):
        return (cls.name)(*args)

    @classmethod
    def get_price(cls, is_retail=False, ingredient_modifier=1, multiplier=1):
        if is_retail:
            if cls.retail_price != 0:
                original_price = cls.retail_price
            else:
                original_price = cls.crafting_price
            discounted_price = original_price * multiplier
            discounted_ingredients_price = discounted_price
        else:
            original_price = cls.crafting_price + cls.delta_ingredient_price
            discounted_price = (cls.crafting_price + cls.delta_ingredient_price) * multiplier
            discounted_ingredients_price = (cls.crafting_price + int(cls.delta_ingredient_price * ingredient_modifier)) * multiplier
        return (original_price, int(discounted_price), int(discounted_ingredients_price))

    @classmethod
    def get_bucks_prices(cls, is_retail=False, multipliers={}, order_count=1):
        bucks_prices = cls.crafting_bucks_price
        for buck, buck_price in bucks_prices.items():
            multiplier = multipliers.get(buck)
            if is_retail:
                if cls.retail_price != 0:
                    original_price = cls.retail_price
                else:
                    original_price = bucks_prices[buck]
                if multiplier is not None:
                    discounted_price = original_price * multiplier
                    bucks_prices[buck] = int(discounted_price)
                if order_count is not None:
                    bucks_prices[buck] *= order_count

        return bucks_prices

    @classmethod
    def calculate_autonomy_weight(cls, sim):
        total_weight = cls.autonomy_weight
        for buff, weight in cls.buff_weight_multipliers.items():
            if sim.has_buff(buff):
                total_weight *= weight

        return total_weight

    @classproperty
    def total_visible_phases(cls):
        return len(cls._visible_phase_sequence)

    @classmethod
    def get_visible_phase_index(cls, phase):
        if phase in cls._visible_phase_sequence:
            return cls._visible_phase_sequence.index(phase) + 1
        return 0

    @classproperty
    def is_single_phase_recipe(cls):
        return len(cls._phases) == 1

    @classproperty
    def tuning_tags(cls):
        return cls.recipe_tags

    @classmethod
    def update_hovertip(cls, owner, crafter=None):
        description = cls.recipe_description(crafter)
        genre = Genre.get_genre_localized_string(owner)
        if genre is not None:
            description = LocalizationHelperTuning.get_new_line_separated_strings(description, genre)
        if cls.value_text is not None:
            localized_value = cls.value_text(owner.current_value)
            description = LocalizationHelperTuning.get_new_line_separated_strings(description, localized_value)
        owner.update_tooltip_field((TooltipFields.recipe_description), description, should_update=True)

    @property
    def debug_name(self):
        return type(self).__name__

    @classmethod
    def debug_dump(cls, dump=dump_logger.warn):
        dump('Recipe Name: {}'.format(type(cls).__name__))
        dump('Phases: {}'.format(len(cls.phases)))
        for phase in cls.phases.values():
            dump('  Phase {}:'.format(phase.id))
            if phase.num_turns > 0:
                dump('    Turns: {}'.format(phase.turns))


class CraftingObjectType(metaclass=TunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.RECIPE)):
    INSTANCE_TUNABLES = {'unavailable_tooltip': TunableLocalizedStringFactory(description='Tooltip displayed when there are no objects of this type and one is required.')}


def destroy_unentitled_craftables():
    entitlement_map = {}
    objects_to_destroy = list()
    for obj in itertools.chain(services.object_manager().values(), services.inventory_manager().values()):
        crafting_component = obj.crafting_component
        if crafting_component is not None:
            recipe = crafting_component.get_recipe()
            if recipe is None:
                objects_to_destroy.append(obj)
                continue
        if recipe is not None:
            if recipe.entitlement:
                if recipe.entitlement in entitlement_map:
                    entitled = entitlement_map[recipe.entitlement]
                else:
                    entitled = mtx.has_entitlement(recipe.entitlement)
                    entitlement_map[recipe.entitlement] = entitled
            entitled or objects_to_destroy.append(obj)

    for obj in objects_to_destroy:
        obj.destroy(source=obj, cause='Destroying unentitled craftables.')
