# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\crafting\photography.py
# Compiled at: 2022-01-26 22:31:44
# Size of source mod 2**32: 20840 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= \e_c_stmts_opt COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
compare ::= compare_single . 
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
compare_single ::= expr expr COMPARE_OP . 
continues ::= _stmts . lastl_stmt continue
dict ::= kvlist_1 . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= or . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
function_def_deco ::= mkfuncdeco . store
function_def_deco ::= mkfuncdeco store . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_1 ::= expr expr BUILD_MAP_1 . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 . CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 CALL_FUNCTION_1 . 
mkfuncdeco0 ::= mkfunc . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= function_def_deco . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr BUILD_TUPLE_1 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 256        74  LOAD_CONST               False
->                76  RETURN_VALUE     
from crafting.crafting_tunable import CraftingTuning
from crafting.photography_enums import CameraQuality, PhotoStyleType, CameraMode, PhotoOrientation, PhotoSize
from crafting.photography_loots import RotateTargetPhotoLoot
from event_testing import test_events
from event_testing.resolver import SingleSimResolver, DoubleSimAndObjectResolver
from interactions import ParticipantType
from objects import PaintingState
from objects.components.state import TunableStateValueReference
from objects.components.types import STORED_SIM_INFO_COMPONENT
from objects.system import create_object
from sims4.tuning.tunable import TunablePackSafeReference, TunableEnumEntry, TunableList, TunableReference, TunableInterval, TunableMapping, Tunable
from statistics.skill import Skill
from tunable_multiplier import TunableStatisticModifierCurve
import services, sims4, tag
logger = sims4.log.Logger('Photography', default_owner='rrodgers')

class Photography:
    SMALL_PORTRAIT_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a small portrait photo.\n        ',
      manager=(services.definition_manager()))
    SMALL_LANDSCAPE_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a small landscape photo.\n        ',
      manager=(services.definition_manager()))
    MEDIUM_PORTRAIT_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a medium portrait photo.\n        ',
      manager=(services.definition_manager()))
    MEDIUM_LANDSCAPE_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a medium landscape photo.\n        ',
      manager=(services.definition_manager()))
    LARGE_PORTRAIT_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a large portrait photo.\n        ',
      manager=(services.definition_manager()))
    LARGE_LANDSCAPE_OBJ_DEF = TunablePackSafeReference(description='\n        Object definition for a large landscape photo.\n        ',
      manager=(services.definition_manager()))
    PAINTING_INTERACTION_TAG = TunableEnumEntry(description='\n        Tag to specify a painting interaction.\n        ',
      tunable_type=(tag.Tag),
      default=(tag.Tag.INVALID))
    PHOTOGRAPHY_LOOT_LIST = TunableList(description='\n        A list of loot operations to apply to the photographer when photo mode exits.\n        ',
      tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      class_restrictions=('LootActions', ),
      pack_safe=True))
    FAIL_PHOTO_QUALITY_RANGE = TunableInterval(description='\n        The random quality statistic value that a failure photo will be\n        given between the min and max tuned values.\n        ',
      tunable_type=int,
      default_lower=0,
      default_upper=100)
    BASE_PHOTO_QUALITY_MAP = TunableMapping(description='\n        The mapping of CameraQuality value to an interval of quality values\n        that will be used to asign a random base quality value to a photo\n        as it is created.\n        ',
      key_type=TunableEnumEntry(description='\n            The CameraQuality value. If this photo has this CameraQuality,\n            value, then a random quality between the min value and max value\n            will be assigned to the photo.\n            ',
      tunable_type=CameraQuality,
      default=(CameraQuality.CHEAP)),
      value_type=TunableInterval(description='\n            The range of base quality values from which a random value will be\n            given to the photo.\n            ',
      tunable_type=int,
      default_lower=1,
      default_upper=100))
    QUALITY_MODIFIER_PER_SKILL_LEVEL = Tunable(description='\n        For each level of skill in Photography, this amount will be added to\n        the quality statistic.\n        ',
      tunable_type=float,
      default=0)
    PHOTO_VALUE_MODIFIER_MAP = TunableMapping(description='\n        The mapping of state values to Simoleon value modifiers.\n        The final value of a photo is decided based on its\n        current value multiplied by the sum of all modifiers for\n        states that apply to the photo. All modifiers are\n        added together first, then the sum will be multiplied by\n        the current price.\n        ',
      key_type=TunableStateValueReference(description='\n            The quality state values. If this photo has this state,\n            then a random modifier between min_value and max_value\n            will be multiplied to the current price.'),
      value_type=TunableInterval(description='\n            The maximum modifier multiplied to the current price based on the provided state value\n            ',
      tunable_type=float,
      default_lower=1,
      default_upper=1))
    PHOTO_VALUE_SKILL_CURVE = TunableStatisticModifierCurve.TunableFactory(description="\n        Allows you to adjust the final value of the photo based on the Sim's\n        level of a given skill.\n        ",
      axis_name_overrides=('Skill Level', 'Simoleon Multiplier'),
      locked_args={'subject': ParticipantType.Actor})
    PHOTOGRAPHY_SKILL = Skill.TunablePackSafeReference(description='\n        A reference to the photography skill.\n        ')
    EMOTION_STATE_MAP = TunableMapping(description="\n        The mapping of moods to states, used to give photo objects a mood\n        based state. These states are then used by the tooltip component to\n        display emotional content on the photo's tooltip.\n        ",
      key_type=TunableReference(description='\n            The mood to associate with a state.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.MOOD))),
      value_type=TunableStateValueReference(description='\n            The state that represents the mood for the purpose of displaying\n            emotional content in a tooltip.\n            '))
    PHOTO_OBJECT_LOOT_PER_TARGET = TunableList(description='\n        A list of loots which will be applied once PER target. The participants\n        for each application will be Actor: photographer, Target: photograph\n        target and Object: the Photograph itself. If a photo interaction has 2\n        target sims, this loot will be applied twice.\n        ',
      tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
      pack_safe=True))
    MOOD_PARAM_TO_MOOD_CATEGORY_STATE = TunableMapping(description='\n        If the player took a picture in a photo mode that supports mood\n        categories, we will perform a state change to the corresponding state\n        based on the mood that each picture was taken in.\n        ',
      key_type=Tunable(description='\n            The mood ASM parameter value to associate with a state.\n            ',
      tunable_type=str,
      default=None),
      value_type=TunableStateValueReference(description='\n            The state that represents the mood category.\n            '))
    GROUP_PHOTO_X_ACTOR_TAG = TunableEnumEntry(description='\n        Tag to specify the photo studio interaction that the photo target sim\n        who should be considered the x actor will run.\n        ',
      tunable_type=(tag.Tag),
      default=(tag.Tag.INVALID),
      invalid_enums=(
     tag.Tag.INVALID,))
    GROUP_PHOTO_Y_ACTOR_TAG = TunableEnumEntry(description='\n        Tag to specify the photo studio interaction that the photo target sim\n        who should be considered the y actor will run.\n        ',
      tunable_type=(tag.Tag),
      default=(tag.Tag.INVALID),
      invalid_enums=(
     tag.Tag.INVALID,))
    GROUP_PHOTO_Z_ACTOR_TAG = TunableEnumEntry(description='\n        Tag to specify the photo studio interaction that the photo target sim\n        who should be considered the z actor will run.\n        ',
      tunable_type=(tag.Tag),
      default=(tag.Tag.INVALID),
      invalid_enums=(
     tag.Tag.INVALID,))
    NUM_PHOTOS_PER_SESSION = Tunable(description='\n        Max possible photos that can be taken during one photo session. Once\n        this number has been reached, the photo session will exit.\n        ',
      tunable_type=int,
      default=5)

    @classmethod
    def _is_fail_photo--- This code section failed: ---

 L. 248         0  LOAD_FAST                'photo_style_type'
                2  LOAD_GLOBAL              PhotoStyleType
                4  LOAD_ATTR                EFFECT_GRAINY
                6  COMPARE_OP               ==
                8  POP_JUMP_IF_TRUE     70  'to 70'

 L. 249        10  LOAD_FAST                'photo_style_type'
               12  LOAD_GLOBAL              PhotoStyleType
               14  LOAD_ATTR                EFFECT_OVERSATURATED
               16  COMPARE_OP               ==
               18  POP_JUMP_IF_TRUE     70  'to 70'

 L. 250        20  LOAD_FAST                'photo_style_type'
               22  LOAD_GLOBAL              PhotoStyleType
               24  LOAD_ATTR                EFFECT_UNDERSATURATED
               26  COMPARE_OP               ==
               28  POP_JUMP_IF_TRUE     70  'to 70'

 L. 251        30  LOAD_FAST                'photo_style_type'
               32  LOAD_GLOBAL              PhotoStyleType
               34  LOAD_ATTR                PHOTO_FAIL_BLURRY
               36  COMPARE_OP               ==
               38  POP_JUMP_IF_TRUE     70  'to 70'

 L. 252        40  LOAD_FAST                'photo_style_type'
               42  LOAD_GLOBAL              PhotoStyleType
               44  LOAD_ATTR                PHOTO_FAIL_FINGER
               46  COMPARE_OP               ==
               48  POP_JUMP_IF_TRUE     70  'to 70'

 L. 253        50  LOAD_FAST                'photo_style_type'
               52  LOAD_GLOBAL              PhotoStyleType
               54  LOAD_ATTR                PHOTO_FAIL_GNOME
               56  COMPARE_OP               ==
               58  POP_JUMP_IF_TRUE     70  'to 70'

 L. 254        60  LOAD_FAST                'photo_style_type'
               62  LOAD_GLOBAL              PhotoStyleType
               64  LOAD_ATTR                PHOTO_FAIL_NOISE
               66  COMPARE_OP               ==
               68  POP_JUMP_IF_FALSE    74  'to 74'
             70_0  COME_FROM            58  '58'
             70_1  COME_FROM            48  '48'
             70_2  COME_FROM            38  '38'
             70_3  COME_FROM            28  '28'
             70_4  COME_FROM            18  '18'
             70_5  COME_FROM             8  '8'

 L. 255        70  LOAD_CONST               True
               72  RETURN_VALUE     
             74_0  COME_FROM            68  '68'

 L. 256        74  LOAD_CONST               False
               76  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 76

    @classmethod
    def _apply_quality_and_value_to_photo(cls, photographer_sim, photo_obj, photo_style, camera_quality):
        quality_stat = CraftingTuning.QUALITY_STATISTIC
        quality_stat_tracker = photo_obj.get_tracker(quality_stat)
        if cls._is_fail_photo(photo_style):
            final_quality = cls.FAIL_PHOTO_QUALITY_RANGE.random_int()
        else:
            quality_range = cls.BASE_PHOTO_QUALITY_MAP.get(camera_quality, None)
            if quality_range is None:
                logger.error('Photography tuning BASE_PHOTO_QUALITY_MAP does not have an expected quality value: []', str(camera_quality))
                return
            base_quality = quality_range.random_int()
            skill_quality_modifier = 0
            if cls.PHOTOGRAPHY_SKILL is not None:
                effective_skill_level = photographer_sim.get_effective_skill_level(cls.PHOTOGRAPHY_SKILL)
                if effective_skill_level:
                    skill_quality_modifier = effective_skill_level * cls.QUALITY_MODIFIER_PER_SKILL_LEVEL
            final_quality = base_quality + skill_quality_modifier
        quality_stat_tracker.set_value(quality_stat, final_quality)
        value_multiplier = 1
        for state_value, value_mods in cls.PHOTO_VALUE_MODIFIER_MAP.items():
            if photo_obj.has_state(state_value.state):
                actual_state_value = photo_obj.get_state(state_value.state)
                if state_value is actual_state_value:
                    value_multiplier *= value_mods.random_float()
                    break

        value_multiplier *= cls.PHOTO_VALUE_SKILL_CURVE.get_multiplier(SingleSimResolver(photographer_sim), photographer_sim)
        photo_obj.base_value = int(photo_obj.base_value * value_multiplier)

    @classmethod
    def _get_mood_sim_info_if_exists(cls, photographer_sim_info, target_sim_ids, camera_mode):
        if camera_mode is CameraMode.SELFIE_PHOTO:
            return photographer_sim_info
        num_target_sims = len(target_sim_ids)
        if num_target_sims == 1:
            sim_info_manager = services.sim_info_manager()
            target_sim_info = sim_info_manager.get(target_sim_ids[0])
            return target_sim_info

    @classmethod
    def _apply_mood_state_if_appropriate(cls, photographer_sim_info, target_sim_ids, camera_mode, photo_object):
        mood_sim_info = cls._get_mood_sim_info_if_exists(photographer_sim_info, target_sim_ids, camera_mode)
        if mood_sim_info:
            mood = mood_sim_info.get_mood()
            mood_state = cls.EMOTION_STATE_MAP.get(mood, None)
            if mood_state:
                photo_object.set_state(mood_state.state, mood_state)

    @classmethod
    def _apply_mood_category_state_if_appropriate(cls, selected_mood_param, camera_mode, photo_object):
        if camera_mode in (CameraMode.TRIPOD, CameraMode.SIM_PHOTO, CameraMode.PHOTO_STUDIO_PHOTO, CameraMode.TWO_SIM_SELFIE_PHOTO, CameraMode.SELFIE_PHOTO):
            mood_category_state = cls.MOOD_PARAM_TO_MOOD_CATEGORY_STATE.get(selected_mood_param, None)
            if mood_category_state:
                photo_object.set_state(mood_category_state.state, mood_category_state)

    @classmethod
    def create_photo_from_photo_data(cls, camera_mode, camera_quality, photographer_sim_id, target_obj_id, target_sim_ids, res_key, second_res_key, photo_style, photo_size, photo_orientation, photographer_sim_info, photographer_sim, time_stamp, selected_mood_param):
        photo_object = None
        is_craft_by_reference = camera_mode is CameraMode.PAINT_BY_REFERENCE or camera_mode is CameraMode.CROSSSTITCH_BY_REFERENCE
        if is_craft_by_reference:
            current_zone = services.current_zone()
            photo_object = current_zone.object_manager.get(target_obj_id)
            if photo_object is None:
                photo_object = current_zone.inventory_manager.get(target_obj_id)
        else:
            if photo_orientation == PhotoOrientation.LANDSCAPE:
                if photo_size == PhotoSize.LARGE:
                    photo_object_def = cls.LARGE_LANDSCAPE_OBJ_DEF
                elif photo_size == PhotoSize.MEDIUM:
                    photo_object_def = cls.MEDIUM_LANDSCAPE_OBJ_DEF
                elif photo_size == PhotoSize.SMALL:
                    photo_object_def = cls.SMALL_LANDSCAPE_OBJ_DEF
            elif photo_orientation == PhotoOrientation.PORTRAIT:
                if photo_size == PhotoSize.LARGE:
                    photo_object_def = cls.LARGE_PORTRAIT_OBJ_DEF
                else:
                    if photo_size == PhotoSize.MEDIUM:
                        photo_object_def = cls.MEDIUM_PORTRAIT_OBJ_DEF
                    else:
                        if photo_size == PhotoSize.SMALL:
                            photo_object_def = cls.SMALL_PORTRAIT_OBJ_DEF
                        else:
                            photo_object_def = cls.SMALL_LANDSCAPE_OBJ_DEF
            if photo_object_def is None:
                return
            photo_object = create_object(photo_object_def)
        if photo_object is None:
            logger.error('photo object could not be found.')
            return
        for target_sim_id in target_sim_ids:
            target_sim_info = services.sim_info_manager().get(target_sim_id)
            target_sim = target_sim_info.get_sim_instance()
            resolver = DoubleSimAndObjectResolver(photographer_sim, target_sim, photo_object, source=cls)
            for loot in cls.PHOTO_OBJECT_LOOT_PER_TARGET:
                loot.apply_to_resolver(resolver)

        photography_service = services.get_photography_service()
        loots = photography_service.get_loots_for_photo()
        for photoloot in loots:
            if photoloot._AUTO_FACTORY.FACTORY_TYPE is RotateTargetPhotoLoot:
                photographer_sim = photoloot.photographer
                photographer_sim_info = photographer_sim.sim_info
                break

        photography_service.run_callbacks(photo_object, photographer_sim, res_key, second_res_key)
        reveal_level = PaintingState.REVEAL_LEVEL_MIN if is_craft_by_reference else PaintingState.REVEAL_LEVEL_MAX
        painting_state = PaintingState.from_key(res_key, reveal_level, False, photo_style)
        photo_object.canvas_component.painting_state = painting_state
        photo_object.canvas_component.time_stamp = time_stamp
        photo_object.set_household_owner_id(photographer_sim.household_id)
        if selected_mood_param:
            cls._apply_mood_category_state_if_appropriate(selected_mood_param, camera_mode, photo_object)
        is_craft_by_reference or cls._apply_quality_and_value_to_photo(photographer_sim, photo_object, photo_style, camera_quality)
        cls._apply_mood_state_if_appropriate(photographer_sim_info, target_sim_ids, camera_mode, photo_object)
        photo_object.add_dynamic_component(STORED_SIM_INFO_COMPONENT, sim_id=(photographer_sim.id))
        photo_object.update_object_tooltip()
        if not (photographer_sim.inventory_component.can_add(photo_object) and photographer_sim.inventory_component.player_try_add_object(photo_object)):
            logger.error("photo object could not be put in the sim's inventory, deleting photo.")
            photo_object.destroy()
        photo_targets = [services.sim_info_manager().get(sim_id) for sim_id in target_sim_ids]
        if camera_mode == CameraMode.TWO_SIM_SELFIE_PHOTO:
            photo_targets.append(photographer_sim_info)
        photo_targets = frozenset(photo_targets)
        services.get_event_manager().process_event((test_events.TestEvent.PhotoTaken), sim_info=photographer_sim_info, photo_object=photo_object, photo_targets=photo_targets)
