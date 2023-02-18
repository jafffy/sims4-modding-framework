# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\footprint_component.py
# Compiled at: 2022-06-28 21:29:43
# Size of source mod 2**32: 29061 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= COME_FROM c_stmts . come_froms
_ifstmts_jump ::= COME_FROM c_stmts come_froms . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= \e_c_stmts_opt COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt come_froms . 
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_BACK
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_FORWARD
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
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
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
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
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
continues ::= _stmts lastl_stmt . continue
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= or . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
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
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
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
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
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
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  80        60  LOAD_CLOSURE             'footprint_name_hashes'
                  62  BUILD_TUPLE_1         1 
->                64  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  66  LOAD_STR                 'HasFootprintComponent.get_polygon_from_footprint_name_hashes.<locals>.<dictcomp>'
                  68  MAKE_FUNCTION_8          'closure'
                  70  LOAD_FAST                'hashes'
                  72  GET_ITER         
                  74  CALL_FUNCTION_1       1  '1 positional argument'
                  76  STORE_FAST               'enabled_dict'
from collections import defaultdict
from element_utils import build_critical_section_with_finally
from objects.components import componentmethod
from objects.components.types import NativeComponent, FOOTPRINT_COMPONENT
from sims.sim_info_types import Species
from sims4.tuning.tunable import TunableFactory, TunableList, TunableTuple, Tunable
from sims4.tuning.tunable_hash import TunableStringHash32
import build_buy, caches, distributor.fields, distributor.ops, placement, routing, services, sims4.geometry, sims4.log, sims4.math, weakref
logger = sims4.log.Logger(FOOTPRINT_COMPONENT.class_attr)

class HasFootprintComponent:

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._routing_context = None
        self._raycast_context = None

    @property
    def footprint(self):
        footprint_component = self.get_component(FOOTPRINT_COMPONENT)
        if footprint_component is not None:
            return footprint_component.footprint

    @property
    def footprint_polygon(self):
        if self.footprint is None or self.routing_surface is None:
            return
        return placement.get_placement_footprint_compound_polygon(self.position, self.orientation, self.routing_surface, self.footprint)

    def get_fooptrint_polygon_bounds(self):
        footprint = self.footprint
        if footprint is not None:
            return placement.get_placement_footprint_bounds(footprint)
        return (None, None)

    def get_polygon_from_footprint_name_hashes--- This code section failed: ---

 L.  69         0  LOAD_FAST                'self'
                2  LOAD_ATTR                footprint
                4  LOAD_CONST               None
                6  COMPARE_OP               is
                8  POP_JUMP_IF_TRUE     20  'to 20'
               10  LOAD_FAST                'self'
               12  LOAD_ATTR                routing_surface
               14  LOAD_CONST               None
               16  COMPARE_OP               is
               18  POP_JUMP_IF_FALSE    24  'to 24'
             20_0  COME_FROM             8  '8'

 L.  70        20  LOAD_CONST               None
               22  RETURN_VALUE     
             24_0  COME_FROM            18  '18'

 L.  72        24  LOAD_FAST                'self'
               26  LOAD_ATTR                footprint_component
               28  LOAD_METHOD              get_footprint_id
               30  CALL_METHOD_0         0  '0 positional arguments'
               32  STORE_FAST               'footprint_id'

 L.  73        34  LOAD_FAST                'footprint_id'
               36  LOAD_CONST               None
               38  COMPARE_OP               is
               40  POP_JUMP_IF_FALSE    46  'to 46'

 L.  74        42  LOAD_CONST               None
               44  RETURN_VALUE     
             46_0  COME_FROM            40  '40'

 L.  77        46  LOAD_GLOBAL              routing
               48  LOAD_METHOD              get_footprint_polys
               50  LOAD_FAST                'footprint_id'
               52  CALL_METHOD_1         1  '1 positional argument'
               54  LOAD_METHOD              keys
               56  CALL_METHOD_0         0  '0 positional arguments'
               58  STORE_FAST               'hashes'

 L.  80        60  LOAD_CLOSURE             'footprint_name_hashes'
               62  BUILD_TUPLE_1         1 
               64  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               66  LOAD_STR                 'HasFootprintComponent.get_polygon_from_footprint_name_hashes.<locals>.<dictcomp>'
               68  MAKE_FUNCTION_8          'closure'
               70  LOAD_FAST                'hashes'
               72  GET_ITER         
               74  CALL_FUNCTION_1       1  '1 positional argument'
               76  STORE_FAST               'enabled_dict'

 L.  83        78  LOAD_GLOBAL              placement
               80  LOAD_METHOD              get_placement_footprint_compound_polygon
               82  LOAD_FAST                'self'
               84  LOAD_ATTR                position

 L.  84        86  LOAD_FAST                'self'
               88  LOAD_ATTR                orientation
               90  LOAD_FAST                'self'
               92  LOAD_ATTR                routing_surface
               94  LOAD_FAST                'self'
               96  LOAD_ATTR                footprint
               98  LOAD_FAST                'enabled_dict'
              100  CALL_METHOD_5         5  '5 positional arguments'
              102  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_DICTCOMP' instruction at offset 64

    @caches.cached(maxsize=None)
    def get_bounding_box(self):
        lower_bound, upper_bound = self.footprint_polygon.bounds
        bounding_box = sims4.geometry.QtRect(sims4.math.Vector2(lower_bound.x, lower_bound.z), sims4.math.Vector2(upper_bound.x, upper_bound.z))
        return bounding_box

    @property
    def routing_context(self):
        return self._routing_context

    def _create_routing_context(self):
        self._routing_context = routing.RoutingContext
        footprint_key = self.footprint
        self._routing_context.footprint_key = footprint_key
        if footprint_key is not None:
            self._routing_context.object_radius = max(self.footprint_polygon.radius, 0.001)
            self._routing_context.ignore_own_footprint = True

    def get_or_create_routing_context(self):
        if self._routing_context is None:
            self._create_routing_context
        return self._routing_context

    def get_raycast_root(self):
        if self.parent is None:
            return self
        raycast_parent = self
        while raycast_parent.parent is not None:
            if raycast_parent.parent.footprint_polygon is not None:
                if not raycast_parent.parent.footprint_polygon.contains(self.position):
                    return raycast_parent
            raycast_parent = raycast_parent.parent

        return raycast_parent

    def raycast_context(self, for_carryable=False):
        root = self.get_raycast_root
        try:
            if for_carryable:
                current_context = root._raycast_context
                try:
                    root._create_raycast_context(for_carryable=for_carryable)
                    carryable_context = root._raycast_context
                finally:
                    root._raycast_context = current_context

                return carryable_context
            if root._raycast_context is None:
                root._create_raycast_context
            return root._raycast_context
        except AttributeError as exc:
            try:
                raise AttributeError('Raycast Root: {}, of {}, has no raycast context\n {}'.format(root, self, exc))
            finally:
                exc = None
                del exc

    def _create_raycast_context(self, for_carryable=False):
        from sims.sim_info import SimInfo
        self._raycast_context = routing.PathPlanContext
        if self.is_sim:
            self._raycast_context.footprint_key = SimInfo.get_sim_definition(self.extended_species).get_footprint(0)
        else:
            self._raycast_context.footprint_key = SimInfo.get_sim_definition(Species.HUMAN).get_footprint(0)
        self._raycast_context.agent_id = self.id
        self._raycast_context.agent_radius = routing.get_default_agent_radius
        self._raycast_context.set_key_mask(routing.FOOTPRINT_KEY_ON_LOT | routing.FOOTPRINT_KEY_OFF_LOT)
        if self.is_sim:
            return
        if self.routing_context is not None:
            self_footprint_id = self.routing_context.object_footprint_id
            if self_footprint_id is not None:
                self._raycast_context.ignore_footprint_contour(self_footprint_id)
        owner_object = self.part_owner if self.is_part else self
        for obj in owner_object.children_recursive_gen(include_self=True):
            if obj is not owner_object:
                obj._raycast_context = None
            else:
                if obj.is_sim:
                    continue
                routing_context = obj.routing_context
                if routing_context is None and obj.is_part:
                    routing_context = obj.part_owner.routing_context
            if routing_context is None:
                continue
            if (for_carryable or self.footprint_polygon) is not None:
                if not self.footprint_polygon.contains(obj.position):
                    continue
                override_id = routing_context.object_footprint_id
                if override_id is not None:
                    self._raycast_context.ignore_footprint_contour(override_id)

    def clear_raycast_context(self):
        root = self.get_raycast_root
        root._raycast_context = None
        if not root.is_sim:
            root.clear_check_line_of_sight_cache


class FootprintComponent(NativeComponent, component_name=FOOTPRINT_COMPONENT, key=3355914538):
    _footprint = None
    _footprints_enabled = False
    _placement_footprint_added = False
    _toggle_placement_footprint = None
    _placement_footprint_count = None
    _footprint_tracker = None
    _TOGGLE_COUNT_INDEX = 0
    _ENABLED_COUNT_INDEX = 1
    _DISABLED_COUNT_INDEX = 2
    _enabled_dict = None
    _delayed_toggle_contour = None
    _registered_on_build_buy_exit_callback = None
    _finalized = False

    @distributor.fields.ComponentField(op=(distributor.ops.SetFootprint), priority=(distributor.fields.Field.Priority.HIGH))
    def footprint(self):
        return self._footprint

    @distributor.fields.ComponentField(op=(distributor.ops.UpdateFootprintStatus))
    def footprint_and_status(self):
        placement_footprint_enabled = self._footprints_enabled
        if placement_footprint_enabled:
            if self._toggle_placement_footprint is not None:
                placement_footprint_enabled = self._toggle_placement_footprint
        return (
         self._footprint, placement_footprint_enabled)

    _resend_footprint = footprint.get_resend
    _resend_footprint_status = footprint_and_status.get_resend

    @componentmethod
    def get_footprint(self):
        return self.footprint

    @property
    def footprints_enabled(self):
        return self._footprints_enabled

    @footprints_enabled.setter
    def footprints_enabled(self, value):
        self._footprints_enabled = value

    def _validate_object_footprint(self):
        footprint_id = self.get_footprint_id
        if footprint_id is None:
            logger.error('Cannot toggle footprint if the object ({}) has none.', (self.owner), owner='mduke')
            return False
        return True

    def update_placement_footprint(self, value):
        self._toggle_placement_footprint = value
        if self._finalized:
            self.update_footprint(update_placement_only=True)
            return

    def apply_definition(self, definition, obj_state=0):
        value = definition.get_footprint(obj_state)
        reenable = False
        if self.footprints_enabled:
            self.disable_footprint
            reenable = True
        self._footprint = value
        routing_context = self.owner.routing_context
        if routing_context is not None:
            routing_context.footprint_key = value
        self._resend_footprint
        if reenable:
            self.enable_footprint

    def on_add(self, *_, **__):
        self.footprints_enabled = True
        venue_game_service = services.venue_game_service
        venue_game_service_is_loading = venue_game_service is not None and venue_game_service.sub_venue_loading
        if services.zone_spin_up_service.is_finished:
            if not venue_game_service_is_loading:
                self._finalized = True

    def on_location_changed(self, *_, **__):
        if self.owner.routing_component is not None:
            if self.owner.routing_component.is_moving:
                return
            if self.owner.routing_component.routing_master is not None:
                if self.owner.routing_component.routing_master.is_moving:
                    return
        if self.owner.id:
            self.update_footprint

    def on_parent_change(self, parent):
        if parent is not None:
            if parent._disable_child_footprint_and_shadow:
                self.disable_footprint
                return
        self.enable_footprint

    def on_finalize_load(self):
        self._finalized = True
        self.update_footprint
        self._execute_delayed_toggle_contour

    def on_remove(self, *_, **__):
        self.disable_footprint(from_remove=True, force_disable=True)

    def on_added_to_inventory(self):
        self.disable_footprint(force_disable=True)

    def on_removed_from_inventory(self):
        self.enable_footprint

    @property
    def _footprints_should_be_enabled(self):
        if not self.footprints_enabled:
            return False
        if self.owner.parent is not None:
            if self.owner.parent._disable_child_footprint_and_shadow:
                return False
        if self.owner.routing_surface is None:
            return False
        return True

    def enable_footprint(self, from_remove=False, force_enable=False):
        if self._toggle_placement_footprint is False:
            if not force_enable:
                return
        self.footprints_enabled = True
        self.update_footprint(from_remove=from_remove)

    def disable_footprint(self, from_remove=False, force_disable=False):
        if self._toggle_placement_footprint is True:
            if not force_disable:
                return
        self.footprints_enabled = False
        self.update_footprint(from_remove=from_remove)

    def update_footprint(self, from_remove=False, update_placement_only=False):
        zone = services.current_zone
        if zone.is_zone_shutting_down:
            return
            if zone.is_zone_loading:
                return
            else:
                if self._footprints_should_be_enabled:
                    routing_context = self.owner.routing_context
                    if not update_placement_only:
                        if routing_context is not None and routing_context.object_footprint_id is not None:
                            routing.invalidate_footprint(routing_context.object_footprint_id, self._enabled_dict)
                            routing_context.connectivity_groups_need_rebuild = True
                else:
                    routing_context = self.owner.get_or_create_routing_context
                    object_footprint_id = routing.add_footprint(self.owner.id, self.footprint, self.owner.zone_id)
                    routing_context.object_footprint_id = object_footprint_id
                    self.owner.clear_raycast_context
                if self._toggle_placement_footprint is not False:
                    if self._placement_footprint_added:
                        placement.remove_placement_footprint(self.owner)
                    placement.add_placement_footprint(self.owner)
                    self._placement_footprint_added = True
                else:
                    if self._placement_footprint_added:
                        placement.remove_placement_footprint(self.owner)
                        self._placement_footprint_added = False
        else:
            routing_context = self.owner.routing_context
        if routing_context is not None:
            if routing_context.object_footprint_id is not None:
                routing.remove_footprint(routing_context.object_footprint_id)
                routing_context.object_footprint_id = None
        if self._placement_footprint_added:
            placement.remove_placement_footprint(self.owner)
            self._placement_footprint_added = False
        if not from_remove:
            self._resend_footprint_status

    def get_footprint_id(self):
        routing_context = self.owner.routing_context
        if routing_context is not None:
            return self.owner.routing_context.object_footprint_id

    def _refresh_enabled_dict(self):
        footprint_id = self.get_footprint_id
        self._enabled_dict = routing.get_footprint_polys(footprint_id)

    def _execute_delayed_toggle_contour(self):
        if self._delayed_toggle_contour is None:
            return
        else:
            return self._validate_object_footprint or None
        self._refresh_enabled_dict
        routing_footprints_updated = False
        for hash_name, enable in self._delayed_toggle_contour.items:
            routing_footprints_updated |= self.update_enabled_routing_footprints(hash_name, enable)

        if routing_footprints_updated:
            self.update_footprint
        self._delayed_toggle_contour = None
        if self._registered_on_build_buy_exit_callback is not None:
            build_buy.unregister_build_buy_exit_callback(self._registered_on_build_buy_exit_callback)
            self._registered_on_build_buy_exit_callback = None

    def toggle_contour_lazy(self, hash_name, enable):
        zone = services.current_zone
        if self._finalized:
            if not zone.is_in_build_buy:
                self.toggle_contour(hash_name, enable)
                return
        if self._delayed_toggle_contour is None:
            self._delayed_toggle_contour = dict()
        self._delayed_toggle_contour[hash_name] = enable
        if zone.is_in_build_buy:
            if self._registered_on_build_buy_exit_callback is None:
                weak_callback = weakref.WeakMethod(self._execute_delayed_toggle_contour)
                self._registered_on_build_buy_exit_callback = lambda: weak_callback() is None or weak_callback()()
                build_buy.register_build_buy_exit_callback(self._registered_on_build_buy_exit_callback)

    def update_enabled_routing_footprints(self, hash_name, enable):
        if hash_name not in self._enabled_dict:
            logger.error('Attempt to toggle a footprint ({}) that was not found on the object: {}.', hash_name, (self.owner),
              owner='mduke')
            return False
        curState = self._enabled_dict[hash_name]
        if curState != enable:
            self._enabled_dict[hash_name] = enable
            return True
        return False

    def toggle_contour(self, hash_name, enable):
        if not self._validate_object_footprint:
            return
        self._refresh_enabled_dict
        if self.update_enabled_routing_footprints(hash_name, enable):
            self.update_footprint

    def _get_enable_and_disable_counts(self, footprint_hash):
        if self._footprint_tracker is None:
            self._footprint_tracker = defaultdict((lambda: [0, 0, 0]))
        return self._footprint_tracker[footprint_hash]

    def start_toggle_footprint(self, enable, footprint_hash, set_placement_footprint=False):

        def trigger_toggle_footprint():
            if set_placement_footprint:
                self.update_placement_footprint(enable)
            else:
                self.toggle_contour_lazy(footprint_hash, enable=enable)

        if set_placement_footprint:
            if self._placement_footprint_count is None:
                self._placement_footprint_count = [
                 0, 0, 0]
            counts = self._placement_footprint_count
        else:
            counts = self._get_enable_and_disable_counts(footprint_hash)
        if enable:
            if counts[self._DISABLED_COUNT_INDEX] != 0:
                logger.error('Attempt to enable a footprint that is currently being disabled by another SI/State. Request will be ignored.', owner='mduke')
            else:
                if counts[self._ENABLED_COUNT_INDEX] == 0:
                    trigger_toggle_footprint()
            counts[self._ENABLED_COUNT_INDEX] += 1
        else:
            if counts[self._ENABLED_COUNT_INDEX] != 0:
                logger.error('Attempt to disable a footprint that is currently being enabled by another SI/State. Request will be ignored.', owner='mduke')
            else:
                if counts[self._DISABLED_COUNT_INDEX] == 0:
                    trigger_toggle_footprint()
            counts[self._DISABLED_COUNT_INDEX] += 1
        counts[self._TOGGLE_COUNT_INDEX] += 1

    def stop_toggle_footprint(self, enable, footprint_hash, set_placement_footprint=False):

        def trigger_stop_toggle_footprint():
            if set_placement_footprint:
                self.update_placement_footprint(None)
            else:
                self.toggle_contour_lazy(footprint_hash, enable=(not enable))

        if set_placement_footprint:
            if self._placement_footprint_count is None:
                self._placement_footprint_count = [
                 0, 0, 0]
            counts = self._placement_footprint_count
        else:
            counts = self._get_enable_and_disable_counts(footprint_hash)
        if counts[self._TOGGLE_COUNT_INDEX] == 0:
            logger.error('Tunable footprint error on book-keeping.  Stop called more times than start.', owner='mduke')
        else:
            counts[self._TOGGLE_COUNT_INDEX] -= 1
            if enable:
                counts[self._ENABLED_COUNT_INDEX] -= 1
                if counts[self._ENABLED_COUNT_INDEX] == 0:
                    trigger_stop_toggle_footprint()
            else:
                counts[self._DISABLED_COUNT_INDEX] -= 1
                if counts[self._DISABLED_COUNT_INDEX] == 0:
                    trigger_stop_toggle_footprint()


class TunableFootprintToggleElement(TunableFactory):

    @staticmethod
    def factory(interaction, toggles, sequence=(), **kwargs):
        target = interaction.target
        if target is None:
            logger.error('Attempt to toggle a footprint with no target')
            return sequence
        footprint_comp = target.get_component(FOOTPRINT_COMPONENT)
        if footprint_comp is None:
            logger.error('Attempt to toggle a footprint on a target ({}) with no footprint component.', target, owner='mduke')
            return sequence

        def start(*_, **__):
            for toggle in toggles:
                footprint_comp.start_toggle_footprint(toggle.enable, toggle.footprint_hash)

        def stop(*_, **__):
            for toggle in toggles:
                footprint_comp.stop_toggle_footprint(toggle.enable, toggle.footprint_hash)

        return build_critical_section_with_finally(start, sequence, stop)

    FACTORY_TYPE = factory

    def __init__(self, **kwargs):
        (super().__init__)(toggles=TunableList(TunableTuple(enable=Tunable(bool, True, description='If checked, we turn on the tuned footprint when the interaction begins, If not checked we turn off the tuned footprint when the interaction begins.'),
                    footprint_hash=TunableStringHash32(description='Name of the footprint to toggle')),
                    description='List of footprints to toggle during the Interaction.'), **kwargs)
