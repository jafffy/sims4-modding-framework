# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\complex\obstacle_course_situation.py
# Compiled at: 2021-07-08 09:03:34
# Size of source mod 2**32: 23505 bytes

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
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_stmts ::= _stmts . stmt
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
and ::= expr jmp_false expr jmp_false . 
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
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr BUILD_TUPLE_UNPACK_WITH_CALL_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr expr . CALL_METHOD_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw3 ::= expr build_tuple_unpack_with_call . expr CALL_FUNCTION_EX_KW
call_ex_kw3 ::= expr build_tuple_unpack_with_call expr . CALL_FUNCTION_EX_KW
call_ex_kw3 ::= expr build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW . 
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_10
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_16
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_10
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_16
dict ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_10
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_16
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_ex_kw3 . 
expr ::= compare . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
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
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jump_forward_else else_suitec
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
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
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
set ::= expr . BUILD_SET_1
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_DEREF . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 380        54  LOAD_CLOSURE             'object_manager'
                  56  BUILD_TUPLE_1         1 
->                58  LOAD_SETCOMP             '<code_object <setcomp>>'
                  60  LOAD_STR                 'ObstacleCourseSituation._on_add_sim_to_situation.<locals>.<setcomp>'
                  62  MAKE_FUNCTION_8          'closure'
                  64  LOAD_FAST                'self'
                  66  LOAD_ATTR                _obstacle_ids
                  68  GET_ITER         
                  70  CALL_FUNCTION_1       1  '1 positional argument'
                  72  STORE_FAST               'obstacles'
from autonomy.autonomy_modifier import UNLIMITED_AUTONOMY_RULE
from autonomy.settings import AutonomyRandomization
from date_and_time import DateAndTime
from event_testing.results import TestResult
from event_testing.test_events import TestEvent
from interactions.aop import AffordanceObjectPair
from interactions.interaction_finisher import FinishingType
from objects.components.state import ObjectStateValue
from sims4.tuning.instances import lock_instance_tunables
from sims4.tuning.tunable import TunableRange, TunableList, TunableReference, TunableTuple, TunableThreshold
from sims4.tuning.tunable_base import GroupNames
from sims4.utils import classproperty
from situations.bouncer.bouncer_types import BouncerExclusivityCategory
from situations.situation_complex import SituationComplexCommon, TunableSituationJobAndRoleState, CommonInteractionCompletedSituationState, SituationStateData, SituationState
from situations.situation_types import SituationCreationUIOption
from statistics.commodity import Commodity
from tag import TunableTags
from ui.ui_dialog_notification import UiDialogNotification
import autonomy, elements, enum, interactions, services, sims4.log, situations, tag
logger = sims4.log.Logger('Situations', default_owner='rmccord')
OBSTACLE_COURSE_START_TIME_TOKEN = 'course_start_time'
OBSTACLE_COURSE_END_TIME_TOKEN = 'course_end_time'

class ObstacleCourseProgress(enum.Int, export=False):
    NOT_STARTED = 0
    RUNNING = ...
    FINISHED = ...


class WaitForSimJobsState(SituationState):

    def on_activate(self, reader=None):
        super().on_activate(reader=reader)
        self.owner.setup_obstacle_course()


class RunCourseState(CommonInteractionCompletedSituationState):
    FACTORY_TUNABLES = {'obstacle_affordance_list': TunableList(description='\n            List of interactions we want to run autonomy with to find our next\n            obstacle.\n            ',
                                   tunable=TunableReference(description='\n                An interaction to traverse an obstacle.\n                ',
                                   manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION))))}

    def __init__(self, *args, obstacle_affordance_list=None, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.obstacle_affordance_list = obstacle_affordance_list
        self._autonomy_request_handle = None
        self._autonomy_request = None
        self._interaction_context = None

    def on_activate(self, reader=None):
        super().on_activate(reader=reader)
        if self.owner.course_progress < ObstacleCourseProgress.RUNNING:
            self.owner.start_course()
            self.owner.validate_obstacle_course()

    def on_deactivate(self):
        super().on_deactivate()

    def _additional_tests(self, sim_info, event, resolver):
        athlete = self.owner.get_athlete()
        return athlete is None or sim_info.id == athlete.id or False
        return True

    def _on_interaction_of_interest_complete(self, **kwargs):
        if self.owner.course_progress == ObstacleCourseProgress.RUNNING:
            self._schedule_obstacle_autonomy_request()
        else:
            if self.owner.course_progress == ObstacleCourseProgress.FINISHED:
                self.owner.finish_situation()

    def _schedule_obstacle_autonomy_request(self):
        if self._autonomy_request_handle is not None:
            logger.error('Obstacle Course Situation attempted to run autonomy request while a previous request is still being processed')
            return
        sim = self.owner.get_athlete()
        self._create_autonomy_request(sim)
        timeline = services.time_service().sim_timeline
        self._autonomy_request_handle = timeline.schedule(elements.GeneratorElement(self._run_obstacle_course_autonomy_request))

    def _run_obstacle_course_autonomy_request(self, timeline):
        try:
            selected_interaction = yield from services.autonomy_service().find_best_action_gen(timeline, (self._autonomy_request), randomization_override=(AutonomyRandomization.DISABLED))
        finally:
            self._autonomy_request_handle = None

        if self.owner is None:
            return False
        if selected_interaction is not None:
            selected_interaction.invalidate()
            affordance = selected_interaction.affordance
            aop = AffordanceObjectPair(affordance, selected_interaction.target, affordance, None)
            result = aop.test_and_execute(self._interaction_context)
            if not result:
                return result
            self.owner.continue_course()
            return True
        self.owner.finish_course()
        return True
        if False:
            yield None

    def _create_autonomy_request(self, sim, **kwargs):
        autonomy_service = services.autonomy_service()
        if autonomy_service is None:
            return (None, None)
        else:
            obstacles = []
            object_manager = services.object_manager()
            for obj_id in self.owner.obstacle_ids:
                obstacle = object_manager.get(obj_id)
                if obstacle is not None:
                    obstacles.append(obstacle)

            return obstacles or (None, None)
        self._interaction_context = interactions.context.InteractionContext(sim, (interactions.context.InteractionContext.SOURCE_SCRIPT), (interactions.priority.Priority.High), client=None, pick=None)
        commodity_list = []
        for affordance in self.obstacle_affordance_list:
            commodity_list.extend(affordance.commodity_flags)

        self._autonomy_request = (autonomy.autonomy_request.AutonomyRequest)(
 sim, commodity_list=commodity_list, 
         skipped_static_commodities=None, 
         object_list=obstacles, 
         affordance_list=self.obstacle_affordance_list, 
         channel=None, 
         context=self._interaction_context, 
         autonomy_mode=autonomy.autonomy_modes.FullAutonomy, 
         ignore_user_directed_and_autonomous=True, 
         is_script_request=True, 
         consider_scores_of_zero=True, 
         ignore_lockouts=True, 
         apply_opportunity_cost=False, 
         record_test_result=None, 
         distance_estimation_behavior=autonomy.autonomy_request.AutonomyDistanceEstimationBehavior.FINAL_PATH, 
         off_lot_autonomy_rule_override=UNLIMITED_AUTONOMY_RULE, 
         autonomy_mode_label_override='ObstacleCourse', **kwargs)


class ObstacleCourseSituation(SituationComplexCommon):
    INSTANCE_TUNABLES = {'coach_job_and_role_state':TunableSituationJobAndRoleState(description='\n            Job and Role State for the coach Sim. Pre-populated as\n            the actor of the Situation.\n            ',
       tuning_group=GroupNames.ROLES), 
     'athlete_job_and_role_state':TunableSituationJobAndRoleState(description='\n            Job and Role State for the athlete. Pre-populated as the\n            target of the Situation.\n            ',
       tuning_group=GroupNames.ROLES), 
     'run_course_state':RunCourseState.TunableFactory(tuning_group=GroupNames.STATE), 
     'obstacle_tags':TunableTags(description='\n            Tags to use when searching for obstacle course objects.\n            ',
       filter_prefixes=('Func_PetObstacleCourse', ),
       minlength=1), 
     'setup_obstacle_state_value':ObjectStateValue.TunableReference(description='\n            The state to setup obstacles before we run the course.\n            '), 
     'teardown_obstacle_state_value':ObjectStateValue.TunableReference(description='\n            The state to teardown obstacles after we run the course or when the\n            situation ends.\n            '), 
     'failure_commodity':Commodity.TunableReference(description='\n            The commodity we use to track how many times the athlete has failed\n            to overcome an obstacle.\n            '), 
     'obstacles_required':TunableRange(description='\n            The number of obstacles required for the situation to be available. \n            If the obstacles that the pet can route to drops below this number,\n            the situation is destroyed.\n            ',
       tunable_type=int,
       default=4,
       minimum=1), 
     'unfinished_notification':UiDialogNotification.TunableFactory(description='\n            The dialog for when the situation ends prematurely or the dog never\n            finishes the course.\n            Token 0: Athlete\n            Token 1: Coach\n            Token 2: Time\n            ',
       tuning_group=GroupNames.UI), 
     'finish_notifications':TunableList(description='\n            A list of thresholds and notifications to play given the outcome of\n            the course. We run through the thresholds until one passes, and\n            play the corresponding notification.\n            ',
       tuning_group=GroupNames.UI,
       tunable=TunableTuple(description='\n                A threshold and notification to play if the threshold passes.\n                ',
       threshold=TunableThreshold(description='\n                    A threshold to compare the number of failures from the\n                    failure commodity when the course is finished.\n                    '),
       notification=UiDialogNotification.TunableFactory(description='\n                    Notification to play when the situation ends.\n                    Token 0: Athlete\n                    Token 1: Coach\n                    Token 2: Failure Count\n                    Token 3: Time\n                    ')))}

    @classmethod
    def _states(cls):
        return (SituationStateData(0, WaitForSimJobsState),
         SituationStateData(1, RunCourseState, factory=(cls.run_course_state)))

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return [(cls.coach_job_and_role_state.job, cls.coach_job_and_role_state.role_state),
         (
          cls.athlete_job_and_role_state.job, cls.athlete_job_and_role_state.role_state)]

    @classmethod
    def default_job(cls):
        pass

    @classmethod
    def get_prepopulated_job_for_sims(cls, sim, target_sim_id=None):
        prepopulate = [(sim.id, cls.coach_job_and_role_state.job.guid64)]
        if target_sim_id is not None:
            prepopulate.append((target_sim_id, cls.athlete_job_and_role_state.job.guid64))
        return prepopulate

    @classmethod
    def get_obstacles(cls):
        object_manager = services.object_manager()
        found_objects = set()
        for tag in cls.obstacle_tags:
            found_objects.update(object_manager.get_objects_matching_tags({tag}))

        return found_objects

    @classmethod
    def is_situation_available(cls, *args, **kwargs):
        obstacles = cls.get_obstacles()
        if len(obstacles) < cls.obstacles_required:
            return TestResult(False, 'Not enough obstacles.')
        return (super().is_situation_available)(*args, **kwargs)

    @classproperty
    def situation_serialization_option(cls):
        return situations.situation_types.SituationSerializationOption.LOT

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        reader = self._seed.custom_init_params_reader
        if reader is not None:
            obstacles = self.get_obstacles()
            if not obstacles:
                self._self_destruct()
            self._obstacle_ids = {obstacle.id for obstacle in obstacles}
            self._course_start_time = DateAndTime(reader.read_uint64(OBSTACLE_COURSE_START_TIME_TOKEN, services.time_service().sim_now))
            self._course_end_time = DateAndTime(reader.read_uint64(OBSTACLE_COURSE_END_TIME_TOKEN, services.time_service().sim_now))
        else:
            self._obstacle_ids = set()
            self._course_start_time = None
            self._course_end_time = None
        self._course_progress = ObstacleCourseProgress.NOT_STARTED

    @property
    def course_progress(self):
        return self._course_progress

    @property
    def obstacle_ids(self):
        return self._obstacle_ids

    def _save_custom_situation(self, writer):
        super()._save_custom_situation(writer)
        if self._course_start_time is not None:
            writer.write_uint64(OBSTACLE_COURSE_START_TIME_TOKEN, int(self._course_start_time))
        if self._course_end_time is not None:
            writer.write_uint64(OBSTACLE_COURSE_END_TIME_TOKEN, int(self._course_end_time))

    def start_situation(self):
        super().start_situation()
        self._register_obstacle_course_events()
        self._change_state(WaitForSimJobsState())

    def _on_remove_sim_from_situation(self, sim):
        super()._on_remove_sim_from_situation(sim)
        self._self_destruct()

    def _on_add_sim_to_situation--- This code section failed: ---

 L. 376         0  LOAD_GLOBAL              super
                2  CALL_FUNCTION_0       0  '0 positional arguments'
                4  LOAD_ATTR                _on_add_sim_to_situation
                6  LOAD_FAST                'sim'
                8  LOAD_FAST                'job_type'
               10  BUILD_TUPLE_2         2 
               12  LOAD_FAST                'args'
               14  BUILD_TUPLE_UNPACK_WITH_CALL_2     2 
               16  LOAD_FAST                'kwargs'
               18  CALL_FUNCTION_EX_KW     1  'keyword and positional arguments'
               20  POP_TOP          

 L. 378        22  LOAD_FAST                'self'
               24  LOAD_METHOD              get_coach
               26  CALL_METHOD_0         0  '0 positional arguments'
               28  LOAD_CONST               None
               30  COMPARE_OP               is-not
               32  POP_JUMP_IF_FALSE   210  'to 210'
               34  LOAD_FAST                'self'
               36  LOAD_METHOD              get_athlete
               38  CALL_METHOD_0         0  '0 positional arguments'
               40  LOAD_CONST               None
               42  COMPARE_OP               is-not
               44  POP_JUMP_IF_FALSE   210  'to 210'

 L. 379        46  LOAD_GLOBAL              services
               48  LOAD_METHOD              object_manager
               50  CALL_METHOD_0         0  '0 positional arguments'
               52  STORE_DEREF              'object_manager'

 L. 380        54  LOAD_CLOSURE             'object_manager'
               56  BUILD_TUPLE_1         1 
               58  LOAD_SETCOMP             '<code_object <setcomp>>'
               60  LOAD_STR                 'ObstacleCourseSituation._on_add_sim_to_situation.<locals>.<setcomp>'
               62  MAKE_FUNCTION_8          'closure'
               64  LOAD_FAST                'self'
               66  LOAD_ATTR                _obstacle_ids
               68  GET_ITER         
               70  CALL_FUNCTION_1       1  '1 positional argument'
               72  STORE_FAST               'obstacles'

 L. 381        74  LOAD_GLOBAL              services
               76  LOAD_METHOD              sim_info_manager
               78  CALL_METHOD_0         0  '0 positional arguments'
               80  STORE_FAST               'sim_info_manager'

 L. 383        82  LOAD_FAST                'sim_info_manager'
               84  LOAD_METHOD              instanced_sims_gen
               86  CALL_METHOD_0         0  '0 positional arguments'
               88  STORE_FAST               'users'

 L. 384        90  SETUP_LOOP          196  'to 196'
               92  LOAD_FAST                'users'
               94  GET_ITER         
               96  FOR_ITER            194  'to 194'
               98  STORE_FAST               'user'

 L. 385       100  LOAD_FAST                'user'
              102  LOAD_FAST                'self'
              104  LOAD_ATTR                _situation_sims
              106  COMPARE_OP               in
              108  POP_JUMP_IF_FALSE   112  'to 112'

 L. 386       110  CONTINUE             96  'to 96'
            112_0  COME_FROM           108  '108'

 L. 387       112  SETUP_LOOP          192  'to 192'
              114  LOAD_FAST                'user'
              116  LOAD_METHOD              get_all_running_and_queued_interactions
              118  CALL_METHOD_0         0  '0 positional arguments'
              120  GET_ITER         
            122_0  COME_FROM           170  '170'
            122_1  COME_FROM           162  '162'
              122  FOR_ITER            190  'to 190'
              124  STORE_FAST               'interaction'

 L. 388       126  LOAD_FAST                'interaction'
              128  LOAD_ATTR                target
              130  STORE_FAST               'target'

 L. 389       132  LOAD_FAST                'target'
              134  LOAD_CONST               None
              136  COMPARE_OP               is-not
              138  POP_JUMP_IF_FALSE   152  'to 152'
              140  LOAD_FAST                'target'
              142  LOAD_ATTR                is_part
              144  POP_JUMP_IF_FALSE   152  'to 152'
              146  LOAD_FAST                'target'
              148  LOAD_ATTR                part_owner
              150  JUMP_FORWARD        154  'to 154'
            152_0  COME_FROM           144  '144'
            152_1  COME_FROM           138  '138'
              152  LOAD_FAST                'target'
            154_0  COME_FROM           150  '150'
              154  STORE_FAST               'target'

 L. 390       156  LOAD_FAST                'target'
              158  LOAD_CONST               None
              160  COMPARE_OP               is-not
              162  POP_JUMP_IF_FALSE   122  'to 122'
              164  LOAD_FAST                'target'
              166  LOAD_FAST                'obstacles'
              168  COMPARE_OP               in
              170  POP_JUMP_IF_FALSE   122  'to 122'

 L. 391       172  LOAD_FAST                'interaction'
              174  LOAD_ATTR                cancel
              176  LOAD_GLOBAL              FinishingType
              178  LOAD_ATTR                SITUATIONS
              180  LOAD_STR                 'Obstacle Course Starting'
              182  LOAD_CONST               ('cancel_reason_msg',)
              184  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              186  POP_TOP          
              188  JUMP_BACK           122  'to 122'
              190  POP_BLOCK        
            192_0  COME_FROM_LOOP      112  '112'
              192  JUMP_BACK            96  'to 96'
              194  POP_BLOCK        
            196_0  COME_FROM_LOOP       90  '90'

 L. 393       196  LOAD_FAST                'self'
              198  LOAD_METHOD              _change_state
              200  LOAD_FAST                'self'
              202  LOAD_METHOD              run_course_state
              204  CALL_METHOD_0         0  '0 positional arguments'
              206  CALL_METHOD_1         1  '1 positional argument'
              208  POP_TOP          
            210_0  COME_FROM            44  '44'
            210_1  COME_FROM            32  '32'

Parse error at or near `LOAD_SETCOMP' instruction at offset 58

    def _register_obstacle_course_events(self):
        services.get_event_manager().register_single_event(self, TestEvent.ObjectDestroyed)
        services.get_event_manager().register_single_event(self, TestEvent.OnExitBuildBuy)

    def _unregister_obstacle_course_events(self):
        services.get_event_manager().unregister_single_event(self, TestEvent.ObjectDestroyed)
        services.get_event_manager().unregister_single_event(self, TestEvent.OnExitBuildBuy)

    def handle_event(self, sim_info, event, resolver):
        super().handle_event(sim_info, event, resolver)
        if event == TestEvent.ObjectDestroyed:
            destroyed_object = resolver.get_resolved_arg('obj')
            if destroyed_object.id in self._obstacle_ids:
                self._obstacle_ids.remove(destroyed_object.id)
                if len(self._obstacle_ids) < self.obstacles_required:
                    self._self_destruct()
        elif event == TestEvent.OnExitBuildBuy:
            self.validate_obstacle_course()

    def on_remove(self):
        coach = self.get_coach()
        athlete = self.get_athlete()
        if coach is not None:
            if athlete is not None:
                if self.course_progress > ObstacleCourseProgress.NOT_STARTED:
                    if self.course_progress < ObstacleCourseProgress.FINISHED:
                        course_end_time = services.time_service().sim_now
                        course_time_span = course_end_time - self._course_start_time
                        unfinished_dialog = self.unfinished_notification(coach)
                        unfinished_dialog.show_dialog(additional_tokens=(athlete, coach, course_time_span))
                athlete.commodity_tracker.remove_statistic(self.failure_commodity)
        self.teardown_obstacle_course()
        self._unregister_obstacle_course_events()
        super().on_remove()

    def start_course(self):
        self._course_progress = ObstacleCourseProgress.RUNNING
        self._course_start_time = services.time_service().sim_now if self._course_start_time is None else self._course_start_time

    def continue_course(self):
        self._change_state(self.run_course_state())

    def finish_course(self):
        self._course_end_time = services.time_service().sim_now
        self._course_progress = ObstacleCourseProgress.FINISHED
        self._change_state(self.run_course_state())

    def finish_situation(self):
        course_time_span = self._course_end_time - self._course_start_time
        athlete = self.get_athlete()
        coach = self.get_coach()
        failures = athlete.commodity_tracker.get_value(self.failure_commodity)
        for threshold_notification in self.finish_notifications:
            if threshold_notification.threshold.compare(failures):
                dialog = threshold_notification.notification(coach)
                dialog.show_dialog(additional_tokens=(athlete, coach, failures, course_time_span))
                break
        else:
            logger.error("Obstacle Course Situation doesn't have a threshold, notification for failure count of {}", failures)

        self._self_destruct()

    def setup_obstacle_course(self):
        obstacles = self.get_obstacles()
        if len(obstacles) < self.obstacles_required:
            self._self_destruct()
        self._obstacle_ids = {obstacle.id for obstacle in obstacles}

    def validate_obstacle_course(self):
        athlete = self.get_athlete()
        if athlete is None:
            self._self_destruct()
            return
        else:
            all_obstacles = self.get_obstacles()
            if len(all_obstacles) < self.obstacles_required:
                self._self_destruct()
                return
                valid_obstacles = set()
                for obstacle in all_obstacles:
                    currentState = obstacle.get_state(self.setup_obstacle_state_value.state)
                    if obstacle.is_connected(athlete):
                        valid_obstacles.add(obstacle)
                        if currentState == self.teardown_obstacle_state_value:
                            obstacle.set_state((self.setup_obstacle_state_value.state), (self.setup_obstacle_state_value), immediate=True)
                        elif currentState == self.setup_obstacle_state_value:
                            obstacle.set_state((self.setup_obstacle_state_value.state), (self.teardown_obstacle_state_value), immediate=True)

                if len(valid_obstacles) < self.obstacles_required:
                    self._self_destruct()
            else:
                self._obstacle_ids = {obstacle.id for obstacle in valid_obstacles}

    def teardown_obstacle_course(self):
        obstacles = self.get_obstacles()
        for obstacle in obstacles:
            obstacle.set_state((self.teardown_obstacle_state_value.state), (self.teardown_obstacle_state_value), immediate=True)

    def get_coach(self):
        return next(iter(self.all_sims_in_job_gen(self.coach_job_and_role_state.job)), None)

    def get_athlete(self):
        return next(iter(self.all_sims_in_job_gen(self.athlete_job_and_role_state.job)), None)


lock_instance_tunables(ObstacleCourseSituation, exclusivity=(BouncerExclusivityCategory.NEUTRAL),
  creation_ui_option=(SituationCreationUIOption.NOT_AVAILABLE),
  _implies_greeted_status=False)
