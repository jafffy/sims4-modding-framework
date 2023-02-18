# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\clubs\club_picker_interactions.py
# Compiled at: 2017-08-21 20:12:51
# Size of source mod 2**32: 15256 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
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
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
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
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr BUILD_MAP_UNPACK_WITH_CALL_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr build_map_unpack_with_call . CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr build_map_unpack_with_call CALL_FUNCTION_EX_KW . 
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
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
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST BUILD_CONST_KEY_MAP_2 . 
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_ex_kw . 
expr ::= compare . 
expr ::= dict . 
expr ::= if_exp . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
if_exp_true ::= expr JUMP_FORWARD . expr COME_FROM
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
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms . else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite . come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
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
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
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
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= BUILD_TUPLE_0 . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= BUILD_TUPLE_0 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  70        58  LOAD_CLOSURE             'club_service'
                  60  BUILD_TUPLE_1         1 
->                62  LOAD_SETCOMP             '<code_object <setcomp>>'
                  64  LOAD_STR                 'ClubPickerSuperInteraction._ClubGenerateFromParticipant.get_clubs_gen.<locals>.<setcomp>'
                  66  MAKE_FUNCTION_8          'closure'
                  68  LOAD_FAST                'resolver'
                  70  LOAD_METHOD              get_participants
                  72  LOAD_FAST                'self'
                  74  LOAD_ATTR                subject
                  76  CALL_METHOD_1         1  '1 positional argument'
                  78  GET_ITER         
                  80  CALL_FUNCTION_1       1  '1 positional argument'
                  82  STORE_FAST               'clubs'
import itertools, math
from clubs.club_tuning import ClubSuperInteraction
from interactions import ParticipantType
from interactions.base.picker_interaction import PickerSuperInteraction, _TunablePieMenuOptionTuple
from interactions.base.super_interaction import SuperInteraction
from interactions.context import QueueInsertStrategy
from interactions.social.social_super_interaction import SocialSuperInteraction
from interactions.utils.tunable import TunableContinuation
from objects.components.game.game_transition_liability import GameTransitionDestinationNodeValidator
from objects.components.game_component import GameRules
from objects.components.portal_lock_data import LockAllWithClubException
from objects.components.portal_locking_enums import ClearLock
from sims4.tuning.instances import lock_instance_tunables
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableList, TunableVariant, TunableEnumEntry, OptionalTunable, Tunable
from sims4.tuning.tunable_base import GroupNames
from sims4.utils import flexmethod
from ui.ui_dialog_picker import BasePickerRow
from venues.venue_constants import NPCSummoningPurpose
import services

class ClubPickerSuperInteraction(PickerSuperInteraction):

    class _ClubGenerateFromParticipant(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'subject':TunableEnumEntry(description="\n                All Clubs this Sim is a member of will be generated, provided\n                they don't conflict with the tuned blacklist.\n                ",
           tunable_type=ParticipantType,
           default=ParticipantType.TargetSim), 
         'subject_blacklist':OptionalTunable(description='\n                If specified, some Clubs will not be generated.\n                ',
           tunable=TunableEnumEntry(description='\n                    No Clubs this Sim is a member of will be generated, even if\n                    the specified subject is a member.\n                    ',
           tunable_type=ParticipantType,
           default=(ParticipantType.Actor)))}

        def get_clubs_gen--- This code section failed: ---

 L.  63         0  LOAD_GLOBAL              services
                2  LOAD_METHOD              get_club_service
                4  CALL_METHOD_0         0  '0 positional arguments'
                6  STORE_DEREF              'club_service'

 L.  64         8  LOAD_DEREF               'club_service'
               10  LOAD_CONST               None
               12  COMPARE_OP               is
               14  POP_JUMP_IF_FALSE    20  'to 20'

 L.  65        16  LOAD_CONST               None
               18  RETURN_VALUE     
             20_0  COME_FROM            14  '14'

 L.  67        20  LOAD_FAST                'inst'
               22  LOAD_CONST               None
               24  COMPARE_OP               is-not
               26  POP_JUMP_IF_FALSE    32  'to 32'
               28  LOAD_FAST                'inst'
               30  JUMP_FORWARD         34  'to 34'
             32_0  COME_FROM            26  '26'
               32  LOAD_FAST                'cls'
             34_0  COME_FROM            30  '30'
               34  STORE_FAST               'inst_or_cls'

 L.  68        36  LOAD_FAST                'inst_or_cls'
               38  LOAD_ATTR                get_resolver
               40  BUILD_TUPLE_0         0 
               42  LOAD_FAST                'target'
               44  LOAD_FAST                'context'
               46  LOAD_CONST               ('target', 'context')
               48  BUILD_CONST_KEY_MAP_2     2 
               50  LOAD_FAST                'kwargs'
               52  BUILD_MAP_UNPACK_WITH_CALL_2     2 
               54  CALL_FUNCTION_EX_KW     1  'keyword and positional arguments'
               56  STORE_FAST               'resolver'

 L.  70        58  LOAD_CLOSURE             'club_service'
               60  BUILD_TUPLE_1         1 
               62  LOAD_SETCOMP             '<code_object <setcomp>>'
               64  LOAD_STR                 'ClubPickerSuperInteraction._ClubGenerateFromParticipant.get_clubs_gen.<locals>.<setcomp>'
               66  MAKE_FUNCTION_8          'closure'
               68  LOAD_FAST                'resolver'
               70  LOAD_METHOD              get_participants
               72  LOAD_FAST                'self'
               74  LOAD_ATTR                subject
               76  CALL_METHOD_1         1  '1 positional argument'
               78  GET_ITER         
               80  CALL_FUNCTION_1       1  '1 positional argument'
               82  STORE_FAST               'clubs'

 L.  71        84  LOAD_FAST                'self'
               86  LOAD_ATTR                subject_blacklist
               88  LOAD_CONST               None
               90  COMPARE_OP               is-not
               92  POP_JUMP_IF_FALSE   124  'to 124'

 L.  72        94  LOAD_FAST                'clubs'
               96  LOAD_CLOSURE             'club_service'
               98  BUILD_TUPLE_1         1 
              100  LOAD_SETCOMP             '<code_object <setcomp>>'
              102  LOAD_STR                 'ClubPickerSuperInteraction._ClubGenerateFromParticipant.get_clubs_gen.<locals>.<setcomp>'
              104  MAKE_FUNCTION_8          'closure'
              106  LOAD_FAST                'resolver'
              108  LOAD_METHOD              get_participants
              110  LOAD_FAST                'self'
              112  LOAD_ATTR                subject_blacklist
              114  CALL_METHOD_1         1  '1 positional argument'
              116  GET_ITER         
              118  CALL_FUNCTION_1       1  '1 positional argument'
              120  INPLACE_SUBTRACT 
              122  STORE_FAST               'clubs'
            124_0  COME_FROM            92  '92'

 L.  73       124  LOAD_FAST                'clubs'
              126  GET_YIELD_FROM_ITER
              128  LOAD_CONST               None
              130  YIELD_FROM       
              132  POP_TOP          

Parse error at or near `LOAD_SETCOMP' instruction at offset 62

    class _ClubGeneratorFromGatherings(HasTunableSingletonFactory, AutoFactoryInit):

        def get_clubs_gen(self, cls, inst, target, context, **kwargs):
            club_service = services.get_club_service()
            if club_service is None:
                return
            sim = context.sim if context is not None else inst.sim
            club_gathering = club_service.sims_to_gatherings_map.getsim
            if club_gathering is None:
                return
            for club in club_service.clubs_to_gatherings_map:
                if club is club_gathering.associated_club:
                    continue
                yield club

    class _ClubPickerActionChallenge(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'challenge_game':GameRules.TunableReference(description='\n                The game that the club is being challenged at. This is used to\n                determine how many Sims are required, per team.\n                '), 
         'challenge_social_interaction':SocialSuperInteraction.TunableReference(description='\n                Specify an interaction that the challenging Sim runs on a Sim in\n                the challenged club (usually the leader). Once this interaction\n                completes, the challenge executes.\n                '), 
         'challenge_interaction':SuperInteraction.TunableReference(description='\n                The interaction to push on the Sims being challenged.\n                ')}

        def on_choice_selected(self, interaction, picked_items, **kwargs):
            club_service = services.get_club_service()
            if club_service is None:
                return
            actor_club_gathering = club_service.sims_to_gatherings_map.getinteraction.sim
            if actor_club_gathering is None:
                return

            def _on_challenge_social_interaction_finished(challenge_social_interaction):
                if not challenge_social_interaction.is_finishing_naturally:
                    return
                minimum_players_per_team = math.ceil(self.challenge_game.players_per_game.lower_bound / self.challenge_game.teams_per_game.lower_bound)
                maximum_players_per_team = math.floor(self.challenge_game.players_per_game.upper_bound / self.challenge_game.teams_per_game.upper_bound)
                teams = []
                for _, club in zip(range(self.challenge_game.teams_per_game.upper_bound), itertools.chain((actor_club_gathering.associated_club,), picked_items)):
                    club_gathering = club_service.clubs_to_gatherings_map.getclub
                    if club_gathering is None:
                        continue
                    club_team = set()
                    challenger_sims = (interaction.sim,) if actor_club_gathering.associated_club is club else ()
                    for club_member in itertools.chain(challenger_sims, sorted((club_gathering.all_sims_in_situation_gen()), key=(lambda sim: sim.sim_info is not club.leader))):
                        club_team.addclub_member
                        if len(club_team) >= maximum_players_per_team:
                            break

                    if len(club_team) >= minimum_players_per_team:
                        teams.appendclub_team

                if len(teams) < self.challenge_game.teams_per_game.lower_bound:
                    return
                all_sims = tuple(itertools.chain.from_iterableteams)
                game_transition_destination_node_validator = GameTransitionDestinationNodeValidator((self.challenge_game), teams=teams)
                for sim in all_sims:
                    context = challenge_social_interaction.context.clone_for_sim(sim, group_id=(challenge_social_interaction.group_id), source_interaction_id=(challenge_social_interaction.id),
                      source_interaction_sim_id=(challenge_social_interaction.sim.sim_id),
                      insert_strategy=(QueueInsertStrategy.NEXT))
                    sim.push_super_affordance((self.challenge_interaction), (interaction.target), context, game_transition_destination_node_validator=game_transition_destination_node_validator)

            for club in picked_items:
                club_gathering = club_service.clubs_to_gatherings_map.getclub
                if club_gathering is None:
                    continue
                for club_member in sorted((club_gathering.all_sims_in_situation_gen()), key=(lambda sim: sim.sim_info is not club.leader)):
                    context = interaction.context.clone_from_immediate_contextinteraction
                    execute_result = interaction.sim.push_super_affordance(self.challenge_social_interaction, club_member, context)
                    if execute_result:
                        challenge_social_interaction = execute_result.interaction
                        challenge_social_interaction.register_on_finishing_callback_on_challenge_social_interaction_finished
                        break

    class _ClubPickerActionSummon(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'purpose': TunableEnumEntry(description='\n                The purpose/reason the NPC is being summoned.\n                ',
                      tunable_type=NPCSummoningPurpose,
                      default=(NPCSummoningPurpose.DEFAULT))}

        def on_choice_selected(self, interaction, picked_items, **kwargs):
            venue = services.get_current_venue()
            if venue is None:
                return
            sim_infos = {sim_info for sim_info in picked_items if sim_info.is_npc}
            venue.summon_npcs(sim_infos, self.purpose, interaction.sim.sim_info)

    class _ClubPickerActionLockPortal(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'club_lock':LockAllWithClubException.TunableFactory(description='\n                The Club lock to apply to the target portal.\n                '), 
         'replace_lock_type':Tunable(description='\n                If checked, then the specified Club lock replaces any existing\n                Club lock, i.e. the only allowed Club is the new Club. If\n                unchecked, then the operation is additive: any Clubs specified\n                for this lock are also allowed, alongside any Clubs previously\n                allowed.\n                ',
           tunable_type=bool,
           default=True), 
         'clear_existing_locks':TunableEnumEntry(description='\n                Which existing locks should be cleared before adding the new \n                Club lock.\n                ',
           tunable_type=ClearLock,
           default=ClearLock.CLEAR_ALL)}

        def on_choice_selected(self, interaction, picked_items, **kwargs):
            for club in picked_items:
                lock_data = self.club_lock()
                lock_data.setup_data(None, None, interaction.get_resolver(associated_club=club))
                interaction.target.add_lock_data(lock_data, replace_same_lock_type=(self.replace_lock_type),
                  clear_existing_locks=(self.clear_existing_locks))

    class _ClubPickerActionPushInteraction(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'continuation': TunableContinuation(description='\n                The interaction to push.\n                ',
                           class_restrictions=(
                          ClubSuperInteraction,))}

        def on_choice_selected(self, interaction, picked_items, **kwargs):
            for club in picked_items:
                interaction.push_tunable_continuation((self.continuation), associated_club=club)

    INSTANCE_TUNABLES = {'pie_menu_option':_TunablePieMenuOptionTuple(tuning_group=GroupNames.PICKERTUNING), 
     'club_generator':TunableVariant(description='\n            Define which Clubs are generated for this picker interaction.\n            ',
       from_participant=_ClubGenerateFromParticipant.TunableFactory(),
       from_gatherings=_ClubGeneratorFromGatherings.TunableFactory(),
       default='from_participant',
       tuning_group=GroupNames.PICKERTUNING), 
     'club_actions':TunableList(description='\n            A list of actions to perform, in order, on the selected Club.\n            ',
       tunable=TunableVariant(description='\n                An action to execute on the specified club.\n                ',
       challenge=(_ClubPickerActionChallenge.TunableFactory()),
       npc_summon=(_ClubPickerActionSummon.TunableFactory()),
       lock_portal=(_ClubPickerActionLockPortal.TunableFactory()),
       push_interaction=(_ClubPickerActionPushInteraction.TunableFactory()),
       default='challenge'),
       tuning_group=GroupNames.PICKERTUNING)}

    def _run_interaction_gen(self, timeline):
        self._show_picker_dialog((self.sim), target_sim=(self.sim), target=(self.target))
        return True
        if False:
            yield None

    @flexmethod
    def picker_rows_gen(cls, inst, target, context, **kwargs):
        for club in (cls.club_generator.get_clubs_gen)(cls, inst, target, context, **kwargs):
            yield BasePickerRow(name=(club.name), tag=club)

    def on_choice_selected(self, picked_item, **kwargs):
        for club_action in self.club_actions:
            club_action.on_choice_selected(self, (picked_item,))


lock_instance_tunables(ClubPickerSuperInteraction, picker_dialog=None)
