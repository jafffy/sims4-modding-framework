# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\postures\posture_graph.py
# Compiled at: 2022-06-18 00:22:04
# Size of source mod 2**32: 414588 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
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
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
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
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict_comp ::= LOAD_DICTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
dict_comp ::= LOAD_DICTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
dict_comp ::= LOAD_DICTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
dict_comp ::= LOAD_DICTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
dict_comp ::= LOAD_DICTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
dict_comp ::= LOAD_DICTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= dict_comp . 
expr ::= get_iter . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
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
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
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
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
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
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 506       128  LOAD_CLOSURE             'source_body_target'
                 130  BUILD_TUPLE_1         1 
->               132  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                 134  LOAD_STR                 'SegmentedPath.__init__.<locals>.<dictcomp>'
                 136  MAKE_FUNCTION_8          'closure'
                 138  LOAD_FAST                'destination_specs'
                 140  LOAD_METHOD              items
                 142  CALL_METHOD_0         0  '0 positional arguments'
                 144  GET_ITER         
                 146  CALL_FUNCTION_1       1  '1 positional argument'
                 148  STORE_FAST               'destination_specs'
               150_0  COME_FROM           114  '114'
               150_1  COME_FROM            86  '86'
               150_2  COME_FROM            56  '56'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
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
break ::= BREAK_LOOP . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr CALL_METHOD_5 . 
call ::= expr expr expr expr expr expr expr . CALL_METHOD_6
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_6
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP . JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
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
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
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
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK . 
iflaststmtl ::= testexprl c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK POP_BLOCK . 
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
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_absolute_else ::= jb_else . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts ::= returns . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
list_comp ::= BUILD_LIST_0 . list_iter
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9 . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
returns ::= _stmts return . 
returns ::= return . 
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
setup_loop ::= SETUP_LOOP _come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= try_except36 . 
stmt ::= whilestmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except36 ::= SETUP_EXCEPT . returns except_handler36 \e_opt_come_from_except
try_except36 ::= SETUP_EXCEPT . returns except_handler36 opt_come_from_except
try_except36 ::= SETUP_EXCEPT . suite_stmts
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
unpack ::= UNPACK_SEQUENCE_3 . store store store
unpack ::= UNPACK_SEQUENCE_3 store . store store
unpack ::= UNPACK_SEQUENCE_3 store store . store
unpack ::= UNPACK_SEQUENCE_3 store store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK \e__come_froms . POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK _come_froms . POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK _come_froms POP_BLOCK . else_suitel COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts COME_FROM . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK . COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . returns come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . 
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP . 
whilestmt ::= setup_loop testexpr l_stmts_opt come_froms . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1374      1126  LOAD_GLOBAL              TestResult
                1128  LOAD_ATTR                TRUE
                1130  RETURN_VALUE     
->            1132_0  COME_FROM_EXCEPT     30  '30'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
_lambda_body ::= lambda_body . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assert_invert ::= testtrue LOAD_GLOBAL . RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
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
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr expr . CALL_METHOD_6
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_6
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
comp_body ::= gen_comp_body . 
comp_for ::= expr . get_for_iter store comp_iter CONTINUE
comp_for ::= expr . get_for_iter store comp_iter JUMP_BACK
comp_if ::= expr . jmp_false comp_iter
comp_if ::= expr jmp_false . comp_iter
comp_if ::= expr jmp_false comp_iter . 
comp_if_not ::= expr . jmp_true comp_iter
comp_iter ::= comp_body . 
comp_iter ::= comp_if . 
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
continues ::= lastl_stmt . continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict_comp_body ::= expr . expr MAP_ADD
dict_comp_body ::= expr expr . MAP_ADD
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= _lambda_body . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= list . 
expr ::= or . 
expr ::= tuple . 
expr ::= yield . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jitop ::= expr JUMP_IF_TRUE_OR_POP . 
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_or_arg ::= expr . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_iter ::= \e__come_froms . FOR_ITER
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
function_def_deco ::= mkfuncdeco . store
function_def_deco ::= mkfuncdeco store . 
gen_comp_body ::= expr . YIELD_VALUE POP_TOP
gen_comp_body ::= expr YIELD_VALUE . POP_TOP
gen_comp_body ::= expr YIELD_VALUE POP_TOP . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1 . 
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK . _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms . 
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
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
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
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
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8 . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
list_comp ::= BUILD_LIST_0 . list_iter
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c _come_froms
list_if ::= expr . jmp_false list_iter
list_if ::= expr . jmp_false list_iter COME_FROM
list_if ::= expr . jmp_false37 list_iter
list_if_not ::= expr . jmp_true list_iter
list_if_not ::= expr . jmp_true list_iter COME_FROM
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR . LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR LOAD_STR . 
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_4
mkfunc ::= expr LOAD_CODE LOAD_STR MAKE_FUNCTION_1 . 
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 . CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 CALL_FUNCTION_1 . 
mkfuncdeco0 ::= mkfunc . 
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jitop . expr COME_FROM
or ::= expr_jitop expr . COME_FROM
or ::= expr_jitop expr COME_FROM . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP . return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond . COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM . 
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr ::= ret_or . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . 
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA LAMBDA_MARKER . 
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
set_comp_body ::= expr . SET_ADD
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= function_def_deco . 
stmt ::= genexpr_func . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= return_expr_lambda . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield ::= expr YIELD_VALUE . 
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1490        82  LOAD_FAST                'self'
                  84  LOAD_FAST                'transition_spec'
                  86  STORE_ATTR               _path_spec
                  88  JUMP_BACK            78  'to 78'
                  90  POP_BLOCK        
                92_0  COME_FROM_LOOP       70  '70'
                92_1  COME_FROM            68  '68'
                92_2  COME_FROM            52  '52'
->              92_3  COME_FROM_LOOP       18  '18'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
_come_froms ::= _come_froms COME_FROM_LOOP . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= COME_FROM c_stmts . come_froms
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
_ifstmts_jumpl ::= COME_FROM c_stmts JUMP_BACK . 
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
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
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_OR . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
cf_jump_back ::= COME_FROM JUMP_BACK . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
comp_body ::= gen_comp_body . 
comp_for ::= expr . get_for_iter store comp_iter CONTINUE
comp_for ::= expr . get_for_iter store comp_iter JUMP_BACK
comp_if ::= expr . jmp_false comp_iter
comp_if ::= or . jmp_false_cf comp_iter
comp_if_not ::= expr . jmp_true comp_iter
comp_iter ::= comp_body . 
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
continues ::= lastl_stmt . continue
delete ::= delete_subscript . 
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
delete_subscript ::= expr expr DELETE_SUBSCR . 
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict_comp_body ::= expr . expr MAP_ADD
dict_comp_body ::= expr expr . MAP_ADD
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitel ::= l_stmts . 
expr ::= LOAD_ASSERT . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= or . 
expr ::= subscript . 
expr ::= tuple . 
expr ::= yield . 
expr ::= yield_from . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jitop ::= expr JUMP_IF_TRUE_OR_POP . 
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP . JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
gen_comp_body ::= expr . YIELD_VALUE POP_TOP
gen_comp_body ::= expr YIELD_VALUE . POP_TOP
gen_comp_body ::= expr YIELD_VALUE POP_TOP . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK . _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms . 
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt cf_jump_back . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
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
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK . 
iflaststmtl ::= testexprl c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts JUMP_BACK . POP_BLOCK
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
inplace_op ::= INPLACE_OR . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt JUMP_BACK . come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_absolute_else ::= jb_else . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jitop . expr COME_FROM
or ::= expr_jitop expr . COME_FROM
or ::= expr_jitop expr COME_FROM . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP . return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond . COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM . 
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr ::= ret_or . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . 
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA LAMBDA_MARKER . 
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
set_comp_body ::= expr . SET_ADD
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign1 . 
stmt ::= call_stmt . 
stmt ::= delete . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= genexpr_func . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= return_expr_lambda . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield ::= expr YIELD_VALUE . 
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
yield_from ::= expr GET_YIELD_FROM_ITER . LOAD_CONST YIELD_FROM
yield_from ::= expr GET_YIELD_FROM_ITER LOAD_CONST . YIELD_FROM
yield_from ::= expr GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM . 
Instruction context:
   
 L.2968        96  LOAD_CLOSURE             'self'
                  98  BUILD_TUPLE_1         1 
->               100  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                 102  LOAD_STR                 'PostureGraph.get_matching_nodes_gen.<locals>.<dictcomp>'
                 104  MAKE_FUNCTION_8          'closure'
                 106  LOAD_FAST                'keys'
                 108  GET_ITER         
                 110  CALL_FUNCTION_1       1  '1 positional argument'
                 112  STORE_FAST               'subsets'

-- Stacks of completed symbols:
START ::= |- stmts . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
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
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr expr . CALL_METHOD_6
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_6
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10 . 
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= call_kw36 . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
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
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
starred ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
starred ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
stmt ::= assign . 
stmt ::= function_def . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.4572        54  LOAD_CLOSURE             'constraint'
                  56  LOAD_CLOSURE             'interaction'
                  58  LOAD_CLOSURE             'self'
                  60  LOAD_CLOSURE             'sim'
                  62  LOAD_CLOSURE             'var_map'
                  64  BUILD_TUPLE_5         5 
->                66  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  68  LOAD_STR                 'PostureGraphService._right_path_gen.<locals>.<dictcomp>'
                  70  MAKE_FUNCTION_8          'closure'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assert_invert ::= testtrue LOAD_GLOBAL . RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
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
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . expr expr expr expr expr expr expr CALL_METHOD_7
call ::= expr . expr expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr . expr expr expr expr expr expr CALL_METHOD_7
call ::= expr expr . expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr . expr expr expr expr expr CALL_METHOD_7
call ::= expr expr expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr . expr expr expr expr CALL_METHOD_7
call ::= expr expr expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . expr expr expr CALL_METHOD_7
call ::= expr expr expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr CALL_METHOD_4 . 
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . expr expr CALL_METHOD_7
call ::= expr expr expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr . CALL_METHOD_6
call ::= expr expr expr expr expr expr expr . expr CALL_METHOD_7
call ::= expr expr expr expr expr expr expr . expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr . CALL_METHOD_7
call ::= expr expr expr expr expr expr expr expr . expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr CALL_METHOD_7 . 
call ::= expr expr expr expr expr expr expr expr expr . expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr expr expr . expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr expr expr expr . expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr expr expr expr expr . CALL_METHOD_11
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_6
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_13
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
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
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
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
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
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
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
list_comp ::= BUILD_LIST_0 . list_iter
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
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
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
starred ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
starred ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr BUILD_TUPLE_3 . 
tuple ::= expr expr expr expr . BUILD_TUPLE_4
tuple ::= expr expr expr expr . expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr . expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr expr . expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr expr expr . BUILD_TUPLE_7
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_3 . store store store
unpack ::= UNPACK_SEQUENCE_3 store . store store
unpack ::= UNPACK_SEQUENCE_3 store store . store
unpack ::= UNPACK_SEQUENCE_3 store store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.6147       576  LOAD_FAST                'final_constraint'
                 578  LOAD_GLOBAL              PathType
                 580  LOAD_ATTR                MIDDLE_LEFT
                 582  LOAD_CONST               ('path_type',)
->             584_0  COME_FROM            86  '86'
                 584  CALL_FUNCTION_KW_11    11  '11 total positional and keyword args'
                 586  STORE_FAST               'blocking_obj_id'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
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
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
break ::= BREAK_LOOP . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . expr expr expr expr expr expr expr CALL_METHOD_7
call ::= expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr . expr expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr . expr expr expr expr expr expr CALL_METHOD_7
call ::= expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr . expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr . expr expr expr expr expr CALL_METHOD_7
call ::= expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr . expr expr expr expr CALL_METHOD_7
call ::= expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . expr expr expr CALL_METHOD_7
call ::= expr expr expr expr expr . expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . expr expr CALL_METHOD_7
call ::= expr expr expr expr expr expr . expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr . CALL_METHOD_6
call ::= expr expr expr expr expr expr expr . expr CALL_METHOD_7
call ::= expr expr expr expr expr expr expr . expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr . expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr CALL_METHOD_6 . 
call ::= expr expr expr expr expr expr expr expr . CALL_METHOD_7
call ::= expr expr expr expr expr expr expr expr . expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr . expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr expr expr expr . expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr expr . expr expr expr CALL_METHOD_11
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_6
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7 . 
call_kw36 ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= kvlist_0 . 
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . 
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY \e_come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_return
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_return
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts END_FINALLY . 
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms END_FINALLY . 
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_stmt ::= except_cond1 . except_suite \e_come_from_opt
except_stmt ::= except_cond1 . except_suite come_from_opt
except_stmt ::= except_cond1 except_suite . come_from_opt
except_stmt ::= except_cond1 except_suite \e_come_from_opt . 
except_stmt ::= except_cond1 except_suite come_from_opt . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt COME_FROM . POP_EXCEPT jump_except COME_FROM
except_suite ::= returns . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
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
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP . JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
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
inplace_op ::= INPLACE_ADD . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_2 ::= expr . expr expr expr BUILD_MAP_2
kvlist_2 ::= expr expr . expr expr BUILD_MAP_2
kvlist_2 ::= expr expr expr . expr BUILD_MAP_2
kvlist_2 ::= expr expr expr expr . BUILD_MAP_2
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr BUILD_LIST_6
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr BUILD_LIST_6
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr BUILD_LIST_6
list ::= expr expr expr expr . expr expr BUILD_LIST_6
list ::= expr expr expr expr expr . expr BUILD_LIST_6
list ::= expr expr expr expr expr expr . BUILD_LIST_6
list ::= expr expr expr expr expr expr BUILD_LIST_6 . 
list_comp ::= BUILD_LIST_0 . list_iter
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= COME_FROM_EXCEPT . 
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
returns ::= return . 
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
starred ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
starred ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
stmt ::= assign . 
stmt ::= aug_assign1 . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= tryelsestmtl3 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= store_subscript . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except . 
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler opt_come_from_except . 
try_except36 ::= SETUP_EXCEPT . returns except_handler36 \e_opt_come_from_except
try_except36 ::= SETUP_EXCEPT . returns except_handler36 opt_come_from_except
try_except36 ::= SETUP_EXCEPT . suite_stmts
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 . come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 come_from_opt . 
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite jump_excepts come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suitel come_from_except_clauses
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel . opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except . 
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr expr BUILD_TUPLE_6
tuple ::= expr . expr expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr . expr expr expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr . expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr . expr expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr . expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr . expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr . BUILD_TUPLE_4
tuple ::= expr expr expr expr . expr expr BUILD_TUPLE_6
tuple ::= expr expr expr expr . expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr . expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr . expr BUILD_TUPLE_6
tuple ::= expr expr expr expr expr . expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr . expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr expr . BUILD_TUPLE_6
tuple ::= expr expr expr expr expr expr . expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr expr . expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr expr BUILD_TUPLE_6 . 
tuple ::= expr expr expr expr expr expr expr . BUILD_TUPLE_7
tuple ::= expr expr expr expr expr expr expr . expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr expr expr expr . expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr expr expr expr expr . expr BUILD_TUPLE_10
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_10 . store store store store store store store store store store
unpack ::= UNPACK_SEQUENCE_10 store . store store store store store store store store store
unpack ::= UNPACK_SEQUENCE_10 store store . store store store store store store store store
unpack ::= UNPACK_SEQUENCE_10 store store store . store store store store store store store
unpack ::= UNPACK_SEQUENCE_10 store store store store . store store store store store store
unpack ::= UNPACK_SEQUENCE_10 store store store store store . store store store store store
unpack ::= UNPACK_SEQUENCE_10 store store store store store store . store store store store
unpack ::= UNPACK_SEQUENCE_10 store store store store store store store . store store store
unpack ::= UNPACK_SEQUENCE_10 store store store store store store store store . store store
unpack ::= UNPACK_SEQUENCE_10 store store store store store store store store store . store
unpack ::= UNPACK_SEQUENCE_10 store store store store store store store store store store . 
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.6417       628  LOAD_CLOSURE             'destination_handles'
                 630  BUILD_TUPLE_1         1 
->               632  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                 634  LOAD_STR                 'PostureGraphService.generate_connectivity_handles.<locals>.<dictcomp>'
                 636  MAKE_FUNCTION_8          'closure'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
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
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
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
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . expr expr expr expr expr expr expr CALL_METHOD_7
call ::= expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr . expr expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr . expr expr expr expr expr expr CALL_METHOD_7
call ::= expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr . expr expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr . expr expr expr expr expr CALL_METHOD_7
call ::= expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr . expr expr expr expr CALL_METHOD_7
call ::= expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr . expr expr CALL_METHOD_6
call ::= expr expr expr expr expr . expr expr expr CALL_METHOD_7
call ::= expr expr expr expr expr . expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_11
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr . expr CALL_METHOD_6
call ::= expr expr expr expr expr expr . expr expr CALL_METHOD_7
call ::= expr expr expr expr expr expr . expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_11
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_6
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_6
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_11
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_13
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= if_exp_not . 
expr ::= list . 
expr ::= listcomp . 
expr ::= or . 
expr ::= subscript . 
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
expr_stmt ::= expr POP_TOP . 
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP . JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
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
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr jump_forward_else . expr COME_FROM
if_exp_not ::= expr jmp_true expr jump_forward_else expr . COME_FROM
if_exp_not ::= expr jmp_true expr jump_forward_else expr COME_FROM . 
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else else_suitec . 
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else else_suitel . 
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK . 
iflaststmtl ::= testexprl c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK POP_BLOCK . 
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
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_absolute_else ::= jb_else . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_2 ::= expr . expr expr expr BUILD_MAP_2
kvlist_2 ::= expr expr . expr expr BUILD_MAP_2
kvlist_2 ::= expr expr expr . expr BUILD_MAP_2
kvlist_2 ::= expr expr expr expr . BUILD_MAP_2
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr expr expr BUILD_LIST_6
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr expr expr BUILD_LIST_6
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr expr expr BUILD_LIST_6
list ::= expr expr expr expr . expr expr BUILD_LIST_6
list ::= expr expr expr expr expr . expr BUILD_LIST_6
list ::= expr expr expr expr expr expr . BUILD_LIST_6
list_comp ::= BUILD_LIST_0 . list_iter
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_6
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_7
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_9
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
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
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . BUILD_SET_1
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
starred ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
starred ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr expr BUILD_TUPLE_6
tuple ::= expr . expr expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr . expr expr expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr . expr expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr . expr expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr . expr expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr . expr expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr . BUILD_TUPLE_4
tuple ::= expr expr expr expr . expr expr BUILD_TUPLE_6
tuple ::= expr expr expr expr . expr expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr . expr expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr . expr BUILD_TUPLE_6
tuple ::= expr expr expr expr expr . expr expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr . expr expr expr expr expr BUILD_TUPLE_10
tuple ::= expr expr expr expr expr expr . BUILD_TUPLE_6
tuple ::= expr expr expr expr expr expr . expr BUILD_TUPLE_7
tuple ::= expr expr expr expr expr expr . expr expr expr expr BUILD_TUPLE_10
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
unpack ::= UNPACK_SEQUENCE_6 . store store store store store store
unpack ::= UNPACK_SEQUENCE_6 store . store store store store store
unpack ::= UNPACK_SEQUENCE_6 store store . store store store store
unpack ::= UNPACK_SEQUENCE_6 store store store . store store store
unpack ::= UNPACK_SEQUENCE_6 store store store store . store store
unpack ::= UNPACK_SEQUENCE_6 store store store store store . store
unpack ::= UNPACK_SEQUENCE_6 store store store store store store . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.6857       824  LOAD_CLOSURE             'in_vehicle_posture'
                 826  LOAD_CLOSURE             'self'
                 828  BUILD_TUPLE_2         2 
->               830  LOAD_SETCOMP             '<code_object <setcomp>>'
                 832  LOAD_STR                 'PostureGraphService.get_best_path_between_handles.<locals>.<setcomp>'
                 834  MAKE_FUNCTION_8          'closure'
                 836  LOAD_FAST                'connectivity'
                 838  GET_ITER         
                 840  CALL_FUNCTION_1       1  '1 positional argument'
                 842  STORE_FAST               'vehicle_dest_handles'
from collections import OrderedDict, namedtuple, defaultdict
from contextlib import contextmanager
import collections, functools, itertools, operator, time, weakref, xml.etree
from caches import BarebonesCache
from event_testing.resolver import SingleActorAndObjectResolver
from objects.pools.pond_utils import PondUtils
from routing.path_planner.height_clearance_helper import get_required_height_clearance
from sims4 import reload
from sims4.callback_utils import CallableTestList
from sims4.collections import frozendict, enumdict
from sims4.geometry import test_point_in_compound_polygon, QtCircle
from sims4.log import Logger, StackVar
from sims4.repr_utils import standard_angle_repr, suppress_quotes
from sims4.service_manager import Service
from sims4.sim_irq_service import yield_to_irq
from sims4.tuning.geometric import TunableVector2
from sims4.tuning.tunable import Tunable, TunableReference, TunableList, TunableMapping, TunableEnumEntry
from sims4.utils import enumerate_reversed
from singletons import DEFAULT
import algos, caches, enum, sims4.geometry, sims4.math, sims4.reload
from animation.posture_manifest import SlotManifestEntry, AnimationParticipant
from animation.posture_manifest_constants import SWIM_AT_NONE_CONSTRAINT, STAND_AT_NONE_CONSTRAINT
from autonomy.autonomy_preference import AutonomyPreferenceType
from balloon.passive_balloons import PassiveBalloons
from element_utils import build_element, maybe
from event_testing.results import TestResult
from indexed_manager import CallbackTypes
from interactions import ParticipantType, constraints
from interactions.aop import AffordanceObjectPair
from interactions.constraints import create_transform_geometry, Anywhere, ANYWHERE, RequiredSlotSingle, create_constraint_set, Constraint, Nowhere
from interactions.context import InteractionContext, QueueInsertStrategy, InteractionSource
from interactions.interaction_finisher import FinishingType
from interactions.priority import Priority
from interactions.utils import routing_constants
from interactions.utils.interaction_liabilities import RESERVATION_LIABILITY, ReservationLiability
from interactions.utils.routing import FollowPath, get_route_element_for_path, SlotGoal
from interactions.utils.routing_constants import TransitionFailureReasons
from objects import ALL_HIDDEN_REASONS
from objects.definition import Definition
from objects.helpers.user_footprint_helper import push_route_away
from objects.object_enums import ResetReason
from objects.pools import pool_utils
from objects.proxy import ProxyObject
from postures import DerailReason
from postures.base_postures import create_puppet_postures
from postures.generic_posture_node import SimPostureNode
from postures.posture import Posture
from postures.posture_errors import PostureGraphError, PostureGraphMiddlePathError
from postures.posture_scoring import PostureScoring, may_reserve_posture_target
from postures.posture_specs import PostureSpecVariable, PostureSpec, PostureOperation, get_origin_spec, get_origin_spec_carry, with_caches, get_pick_up_spec_sequence, get_put_down_spec_sequence, destination_test, PostureAspectBody, PostureAspectSurface, _object_addition, PostureAspectBody_create
from postures.posture_state_spec import create_body_posture_state_spec
from postures.posture_tuning import PostureTuning
from relationships.global_relationship_tuning import RelationshipGlobalTuning
from reservation.reservation_handler_multi import ReservationHandlerMulti
from routing import SurfaceType, GoalFailureType
from routing.formation.formation_tuning import FormationTuning
from routing.formation.formation_type_base import FormationRoutingType
from sims.sim_info_types import Species
from world.ocean_tuning import OceanTuning
import build_buy, cython, debugvis, element_utils, elements, event_testing.test_utils, gsi_handlers.posture_graph_handlers, indexed_manager, interactions.utils.routing, postures, primitives.routing_utils, routing, services, terrain
if not cython.compiled:
    from postures.posture_specs import get_origin_spec, get_origin_spec_carry, PostureSpec, PostureAspectBody
    import cython_utils as cu
else:
    MAX_RIGHT_PATHS = 30
    NON_OPTIMAL_PATH_DESTINATION = 1000
    logger = Logger('PostureGraph')
    cython_log = Logger('CythonConfig')
    if cython.compiled:
        cython_log.always('CYTHON posture_graph is imported!', color=(sims4.log.LEVEL_WARN))
    else:
        cython_log.always('Pure Python posture_graph is imported!', color=(sims4.log.LEVEL_WARN))
with sims4.reload.protected(globals()):
    SIM_DEFAULT_POSTURE_TYPE = None
    SIM_DEFAULT_AOPS = None
    SIM_DEFAULT_OPERATION = None
    STAND_AT_NONE = None
    STAND_AT_NONE_CARRY = None
    STAND_AT_NONE_NODES = None
    SIM_SWIM_POSTURE_TYPE = None
    SIM_SWIM_AOPS = None
    SIM_SWIM_OPERATION = None
    SWIM_AT_NONE = None
    SWIM_AT_NONE_CARRY = None
    SWIM_AT_NONE_NODES = None
    _MOBILE_NODES_AT_NONE = None
    _MOBILE_NODES_AT_NONE_CARRY = None
    _DEFAULT_MOBILE_NODES = None
    enable_debug_goals_visualization = False
    on_transition_destinations_changed = sims4.callback_utils.CallableList()
InsertionIndexAndSpec = namedtuple('InsertionIndexAndSpec', ['index', 'spec'])

@cython.cfunc
@cython.exceptval(check=False)
def get_subset_keys(node_or_spec: PostureSpec) -> set:
    keys = set()
    posture_type = node_or_spec.get_body_posture()
    if posture_type is not None:
        keys.add(('posture_type', posture_type))
    carry_target = node_or_spec.get_carry_target()
    keys.add(('carry_target', carry_target))
    body_target = node_or_spec.body_target
    body_target = getattr(body_target, 'part_owner', None) or body_target
    if node_or_spec.surface is not None:
        original_surface_target = node_or_spec.get_surface_target()
        surface_target = getattr(original_surface_target, 'part_owner', None) or original_surface_target
        keys.add(('slot_target', node_or_spec.get_slot_target()))
        slot_type = node_or_spec.get_slot_type()
        if slot_type is not None:
            if slot_type != PostureSpecVariable.SLOT:
                keys.add(('slot_type', slot_type))
        if surface_target == PostureSpecVariable.CONTAINER_TARGET:
            surface_target = node_or_spec.get_body_target()
        if surface_target is None:
            if body_target is not None and not isinstance(body_target, PostureSpecVariable):
                if body_target.is_surface():
                    keys.add(('surface_target', body_target))
                    keys.add(('has_a_surface', True))
        else:
            keys.add(('has_a_surface', False))
    else:
        if surface_target not in (PostureSpecVariable.ANYTHING, PostureSpecVariable.SURFACE_TARGET):
            keys.add(('surface_target', surface_target))
            keys.add(('has_a_surface', True))
        else:
            if surface_target == PostureSpecVariable.SURFACE_TARGET:
                keys.add(('has_a_surface', True))
            else:
                if slot_type == PostureSpecVariable.SLOT:
                    if not isinstance(original_surface_target, PostureSpecVariable):
                        for slot_type in original_surface_target.get_provided_slot_types():
                            keys.add(('slot_type', slot_type))

                    else:
                        surface_target = None
                if posture_type is not None:
                    if body_target != PostureSpecVariable.ANYTHING:
                        keys.add(('body_target', body_target))
                        if body_target != PostureSpecVariable.BODY_TARGET_FILTERED:
                            keys.add(('body_target', PostureSpecVariable.BODY_TARGET_FILTERED))
                    elif surface_target is None:
                        if posture_type.mobile:
                            keys.add(('body_target', None))
                if ('body_target', None) in keys and ('slot_target', None) in keys:
                    keys.add(('body_target and slot_target', None))
            return keys


def set_transition_destinations(sim, source_goals, destination_goals, selected_source=None, selected_destination=None, preserve=False, draw_both_sets=False):
    if False:
        if on_transition_destinations_changed:
            transition_destinations = []
            transition_sources = []
            max_dest_cost = 0
            for slot_goal in source_goals:
                slot_transform = sims4.math.Transform(slot_goal.location.position, slot_goal.location.orientation)
                slot_constraint = interactions.constraints.Transform(slot_transform,
                  routing_surface=(slot_goal.routing_surface_id))
                if slot_goal is selected_source:
                    slot_constraint.was_selected = True
                else:
                    slot_constraint.was_selected = False
                transition_sources.append(slot_constraint)

            for slot_goal in destination_goals:
                if slot_goal.cost > max_dest_cost:
                    max_dest_cost = slot_goal.cost
                else:
                    slot_transform = sims4.math.Transform(slot_goal.location.position, slot_goal.location.orientation)
                    slot_constraint = interactions.constraints.Transform(slot_transform,
                      routing_surface=(slot_goal.routing_surface_id))
                    if slot_goal is selected_destination:
                        slot_constraint.was_selected = True
                    else:
                        slot_constraint.was_selected = False
                transition_destinations.append((slot_goal.path_id,
                 slot_constraint,
                 slot_goal.cost))

            on_transition_destinations_changed(sim, transition_destinations,
              transition_sources,
              max_dest_cost,
              preserve=preserve)


def _is_sim_carry(interaction, sim):
    if sim.parent is not None:
        return True
        if interaction.carry_target is sim:
            return True
        if interaction.is_putdown:
            if interaction.target is sim:
                return True
    elif interaction.is_social:
        if interaction.target is sim and interaction.sim is sim.parent:
            return True
    return False


class DistanceEstimator:

    def __init__(self, posture_service, sim, interaction, constraint):
        self.posture_service = posture_service
        self.sim = sim
        self.interaction = interaction
        preferred_objects = interaction.preferred_objects
        self.preferred_objects = preferred_objects
        self.constraint = constraint
        routing_context = sim.get_routing_context()

        @caches.BarebonesCache
        def estimate_connectivity_distance(locations):
            source_location, dest_location = locations
            source_locations = ((source_location.transform.translation, source_location.routing_surface),)
            dest_locations = ((dest_location.transform.translation, dest_location.routing_surface),)
            try:
                distance = primitives.routing_utils.estimate_distance_between_multiple_points(source_locations, dest_locations, routing_context)
            except Exception as e:
                try:
                    logger.warn('{}', e, owner='camilogarcia', trigger_breakpoint=True)
                    distance = None
                finally:
                    e = None
                    del e

            distance = cu.MAX_FLOAT if distance is None else distance
            return distance

        self.estimate_distance = estimate_distance = estimate_connectivity_distance

        @caches.BarebonesCache
        def get_preferred_object_cost(obj):
            return postures.posture_scoring.PostureScoring.get_preferred_object_cost((obj,), preferred_objects)

        self.get_preferred_object_cost = get_preferred_object_cost

        @caches.BarebonesCache
        def get_inventory_distance(sim_location_inv_node_location_and_mobile):
            cython.declare(node_body_posture_is_mobile=(cython.bint))
            sim_location, inv, node_location, node_body_posture_is_mobile = sim_location_inv_node_location_and_mobile
            min_dist = cu.MAX_FLOAT
            include_node_location = not node_body_posture_is_mobile or sim_location != node_location
            for owner in inv.owning_objects_gen():
                routing_position, _ = Constraint.get_validated_routing_position(owner)
                routing_location = routing.Location(routing_position, orientation=(owner.orientation),
                  routing_surface=(owner.routing_surface))
                distance = cython.cast(cython.double, estimate_distance((sim_location, routing_location)))
                if distance >= min_dist:
                    continue
                distance += cython.cast(cython.double, get_preferred_object_cost(owner))
                if distance >= min_dist:
                    continue
                if include_node_location:
                    distance += cython.cast(cython.double, estimate_distance((routing_location, node_location)))
                if distance < min_dist:
                    min_dist = distance

            return min_dist

        self.get_inventory_distance = get_inventory_distance

        @caches.BarebonesCache
        def estimate_location_distance(sim_location_and_target_location_and_mobile):
            sim_location, target_location, node_body_posture_is_mobile = sim_location_and_target_location_and_mobile
            if interaction.target is None:
                return estimate_distance((sim_location, target_location))
            carry_target = interaction.carry_target
            if carry_target is None:
                return estimate_distance((sim_location, target_location))
            inv = interaction.target.get_inventory()
            if inv is None:
                interaction_target_routing_location = interaction.target.routing_location
                if interaction_target_routing_location == target_location:
                    return estimate_distance((sim_location, target_location))
                elif interaction_target_routing_location.routing_surface.type == SurfaceType.SURFACETYPE_OBJECT:
                    interaction_target_world_routing_location = interaction_target_routing_location.get_world_surface_location()
                else:
                    interaction_target_world_routing_location = None
                if interaction.is_put_in_inventory:
                    if node_body_posture_is_mobile:
                        if sim_location == target_location:
                            distance = estimate_distance((sim_location, interaction_target_routing_location))
                            if interaction_target_world_routing_location is not None:
                                world_distance = estimate_distance((sim_location, interaction_target_world_routing_location))
                                distance = min(distance, world_distance)
                            return distance
                distance = estimate_distance((sim_location, interaction_target_routing_location)) + estimate_distance((interaction_target_routing_location, target_location))
                if interaction_target_world_routing_location is not None:
                    world_distance = estimate_distance((sim_location, interaction_target_world_routing_location)) + estimate_distance((interaction_target_world_routing_location, target_location))
                    distance = min(distance, world_distance)
                return distance
            if inv.owner.is_sim:
                if inv.owner is not sim:
                    return NON_OPTIMAL_PATH_DESTINATION
                return estimate_distance((sim_location, target_location))
            return get_inventory_distance((sim_location, inv, target_location, node_body_posture_is_mobile))

        self.estimate_location_distance = estimate_location_distance


class PathType(enum.Int, export=False):
    LEFT = 0
    MIDDLE_LEFT = 1
    MIDDLE_RIGHT = 2
    RIGHT = 3


class SegmentedPath:

    def __init__--- This code section failed: ---

 L. 482         0  LOAD_FAST                'posture_graph'
                2  LOAD_FAST                'self'
                4  STORE_ATTR               posture_graph

 L. 483         6  LOAD_FAST                'sim'
                8  LOAD_FAST                'self'
               10  STORE_ATTR               sim

 L. 484        12  LOAD_FAST                'interaction'
               14  LOAD_FAST                'self'
               16  STORE_ATTR               interaction

 L. 485        18  LOAD_FAST                'source'
               20  LOAD_FAST                'self'
               22  STORE_ATTR               source

 L. 486        24  LOAD_FAST                'valid_edge_test'
               26  LOAD_FAST                'self'
               28  STORE_ATTR               valid_edge_test

 L. 488        30  LOAD_FAST                'var_map'
               32  LOAD_FAST                'self'
               34  STORE_ATTR               var_map

 L. 489        36  LOAD_CONST               None
               38  LOAD_FAST                'self'
               40  STORE_ATTR               _var_map_resolved

 L. 491        42  LOAD_FAST                'constraint'
               44  LOAD_FAST                'self'
               46  STORE_ATTR               constraint

 L. 492        48  LOAD_FAST                'is_complete'
               50  LOAD_FAST                'self'
               52  STORE_ATTR               is_complete

 L. 493        54  LOAD_FAST                'is_complete'
               56  POP_JUMP_IF_FALSE   150  'to 150'

 L. 494        58  LOAD_GLOBAL              _is_sim_carry
               60  LOAD_FAST                'interaction'
               62  LOAD_FAST                'sim'
               64  CALL_FUNCTION_2       2  '2 positional arguments'
               66  STORE_FAST               'is_sim_carry'

 L. 497        68  LOAD_FAST                'source'
               70  LOAD_ATTR                body_target
               72  STORE_DEREF              'source_body_target'

 L. 498        74  LOAD_FAST                'is_sim_carry'
               76  POP_JUMP_IF_FALSE    88  'to 88'

 L. 499        78  LOAD_GLOBAL              dict
               80  LOAD_FAST                'destination_specs'
               82  CALL_FUNCTION_1       1  '1 positional argument'
               84  STORE_FAST               'destination_specs'
               86  JUMP_FORWARD        150  'to 150'
             88_0  COME_FROM            76  '76'

 L. 500        88  LOAD_DEREF               'source_body_target'
               90  LOAD_CONST               None
               92  COMPARE_OP               is
               94  POP_JUMP_IF_FALSE   116  'to 116'

 L. 501        96  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               98  LOAD_STR                 'SegmentedPath.__init__.<locals>.<dictcomp>'
              100  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              102  LOAD_FAST                'destination_specs'
              104  LOAD_METHOD              items
              106  CALL_METHOD_0         0  '0 positional arguments'
              108  GET_ITER         
              110  CALL_FUNCTION_1       1  '1 positional argument'
              112  STORE_FAST               'destination_specs'
              114  JUMP_FORWARD        150  'to 150'
            116_0  COME_FROM            94  '94'

 L. 504       116  LOAD_DEREF               'source_body_target'
              118  LOAD_ATTR                is_part
              120  POP_JUMP_IF_FALSE   128  'to 128'

 L. 505       122  LOAD_DEREF               'source_body_target'
              124  LOAD_ATTR                part_owner
              126  STORE_DEREF              'source_body_target'
            128_0  COME_FROM           120  '120'

 L. 506       128  LOAD_CLOSURE             'source_body_target'
              130  BUILD_TUPLE_1         1 
              132  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              134  LOAD_STR                 'SegmentedPath.__init__.<locals>.<dictcomp>'
              136  MAKE_FUNCTION_8          'closure'
              138  LOAD_FAST                'destination_specs'
              140  LOAD_METHOD              items
              142  CALL_METHOD_0         0  '0 positional arguments'
              144  GET_ITER         
              146  CALL_FUNCTION_1       1  '1 positional argument'
              148  STORE_FAST               'destination_specs'
            150_0  COME_FROM           114  '114'
            150_1  COME_FROM            86  '86'
            150_2  COME_FROM            56  '56'

 L. 508       150  LOAD_FAST                'destination_specs'
              152  POP_JUMP_IF_TRUE    162  'to 162'

 L. 509       154  LOAD_GLOBAL              ValueError
              156  LOAD_STR                 'Segmented paths need destinations.'
              158  CALL_FUNCTION_1       1  '1 positional argument'
              160  RAISE_VARARGS_1       1  'exception instance'
            162_0  COME_FROM           152  '152'

 L. 510       162  LOAD_FAST                'destination_specs'
              164  LOAD_FAST                'self'
              166  STORE_ATTR               destination_specs

 L. 511       168  LOAD_FAST                'destination_specs'
              170  LOAD_METHOD              keys
              172  CALL_METHOD_0         0  '0 positional arguments'
              174  LOAD_FAST                'self'
              176  STORE_ATTR               destinations

 L. 513       178  LOAD_FAST                'distance_estimator'
              180  LOAD_CONST               None
              182  COMPARE_OP               is
              184  POP_JUMP_IF_FALSE   206  'to 206'

 L. 514       186  LOAD_GLOBAL              DistanceEstimator
              188  LOAD_FAST                'self'
              190  LOAD_ATTR                posture_graph
              192  LOAD_FAST                'self'
              194  LOAD_ATTR                sim

 L. 515       196  LOAD_FAST                'self'
              198  LOAD_ATTR                interaction
              200  LOAD_FAST                'constraint'
              202  CALL_FUNCTION_4       4  '4 positional arguments'
              204  STORE_FAST               'distance_estimator'
            206_0  COME_FROM           184  '184'

 L. 516       206  LOAD_FAST                'distance_estimator'
              208  LOAD_FAST                'self'
              210  STORE_ATTR               _distance_estimator

Parse error at or near `LOAD_DICTCOMP' instruction at offset 132

    def teardown(self):
        pass

    @property
    def var_map_resolved(self):
        if self._var_map_resolved is None:
            return self.var_map
        return self._var_map_resolved

    @var_map_resolved.setter
    def var_map_resolved(self, value):
        self._var_map_resolved = value

    def check_validity(self, sim):
        source_spec = sim.posture_state.get_posture_spec(self.var_map)
        return source_spec == self.source

    def generate_left_paths(self):
        left_path_gen = self.posture_graph._left_path_gen((self.sim),
          (self.source), (self.destinations), (self.interaction),
          (self.constraint), (self.var_map), (self.valid_edge_test),
          is_complete=(self.is_complete))
        for path_left in left_path_gen:
            path_left.segmented_path = self
            yield path_left

    def generate_right_paths(self, sim, path_left):
        global STAND_AT_NONE_CARRY
        global STAND_AT_NONE_NODES
        if path_left[-1] in self.destinations:
            if len(self.destinations) == 1:
                cost = self.posture_graph._get_goal_cost(self.sim, self.interaction, self.constraint, self.var_map, path_left[-1])
                path_right = algos.Path([path_left[-1]], cost)
                path_right.segmented_path = self
                yield path_right
                return
        allow_carried = False
        if self.is_complete:
            left_destinations = (path_left[-1],)
        else:
            carry = self.var_map.get(PostureSpecVariable.CARRY_TARGET)
            if carry is sim:
                left_destinations = (
                 path_left[-1],)
                allow_carried = True
            else:
                if carry is not None:
                    if path_left[-1].carry_target is None:
                        for constraint in self.constraint:
                            if constraint.posture_state_spec is not None and carry is not self.sim and constraint.posture_state_spec.references_object(carry):
                                break
                        else:
                            carry = None

                if carry is None or isinstance(carry, Definition):
                    left_destinations = services.posture_graph_service().all_mobile_nodes_at_none_no_carry
                else:
                    if (carry.is_in_inventory() or carry.parent) not in (None, self.sim):
                        left_destinations = STAND_AT_NONE_NODES
                    else:
                        left_destinations = (
                         STAND_AT_NONE_CARRY,)
        self.left_destinations = left_destinations
        paths_right = self.posture_graph._right_path_gen((self.sim),
          (self.interaction), (self._distance_estimator), left_destinations, (self.destinations),
          (self.var_map), (self.constraint), (self.valid_edge_test), path_left,
          allow_carried=allow_carried)
        for path_right in paths_right:
            path_right.segmented_path = self
            yield path_right

    def generate_middle_paths(self, path_left, path_right):
        if self.is_complete:
            yield
            return
        middle_paths = self.posture_graph._middle_path_gen(path_left, path_right, self.sim, self.interaction, self._distance_estimator, self.var_map)
        for path_middle in middle_paths:
            if path_middle is not None:
                path_middle.segmented_path = self
            yield path_middle

    @property
    def _path(self):
        return algos.Path(list(getattr(self, '_path_left', ['...?'])) + list(getattr(self, '_path_middle', ['...', '...?']) or [])[1:] + list(getattr(self, '_path_right', ['...', '...?']))[1:])

    def __repr__(self):
        if self.is_complete:
            return 'CompleteSegmentedPath(...)'
        return 'SegmentedPath(...)'


class Connectivity:

    def __init__(self, best_complete_path, source_destination_sets, source_middle_sets, middle_destination_sets):
        self.best_complete_path = best_complete_path
        self.source_destination_sets = source_destination_sets
        self.source_middle_sets = source_middle_sets
        self.middle_destination_sets = middle_destination_sets

    def __repr__(self):
        return 'Connectivity%r' % (tuple(self),)

    def __bool__(self):
        return any(self)

    def __iter__(self):
        return iter((self.best_complete_path, self.source_destination_sets,
         self.source_middle_sets, self.middle_destination_sets))

    def __getitem__(self, i):
        return (
         self.best_complete_path, self.source_destination_sets,
         self.source_middle_sets, self.middle_destination_sets)[i]


class TransitionSequenceStage(enum.Int, export=False):
    EMPTY = ...
    TEMPLATES = ...
    PATHS = ...
    CONNECTIVITY = ...
    ROUTES = ...
    ACTOR_TARGET_SYNC = ...
    COMPLETE = ...


class SequenceId(enum.Int, export=False):
    DEFAULT = 0
    PICKUP = 1
    PUTDOWN = 2


_MobileNode = namedtuple('_MobileNode', ('graph_node', 'prev'))
COST_DELIMITER_STR = '----------------------------------'

def _shortest_path_gen(sim, sources, destinations, *args, **kwargs):
    if gsi_handlers.posture_graph_handlers.archiver.enabled:
        gsi_handlers.posture_graph_handlers.log_path_cost(sim, COST_DELIMITER_STR, COST_DELIMITER_STR, (COST_DELIMITER_STR,))
        gsi_handlers.posture_graph_handlers.add_heuristic_fn_score(sim, '', COST_DELIMITER_STR, COST_DELIMITER_STR, '')

    def is_destination(node):
        if isinstance(node, _MobileNode):
            node = node.graph_node
        return node in destinations

    fake_paths = (algos.shortest_path_gen)(sources, is_destination, *args, **kwargs)
    for fake_path in fake_paths:
        path = algos.Path([node.graph_node if isinstance(node, _MobileNode) else node for node in fake_path], fake_path.cost)
        yield path


def set_transition_failure_reason(sim, reason, target_id=None, transition_controller=None):
    if transition_controller is None:
        transition_controller = sim.transition_controller
    if transition_controller is not None:
        transition_controller.set_failure_target(sim, reason, target_id=target_id)


def _cache_global_sim_default_values():
    global SIM_DEFAULT_AOPS
    global SIM_DEFAULT_OPERATION
    global SIM_DEFAULT_POSTURE_TYPE
    global SIM_SWIM_AOPS
    global SIM_SWIM_OPERATION
    global SIM_SWIM_POSTURE_TYPE
    global STAND_AT_NONE
    global STAND_AT_NONE_CARRY
    global STAND_AT_NONE_NODES
    global SWIM_AT_NONE
    global SWIM_AT_NONE_CARRY
    global SWIM_AT_NONE_NODES
    global _DEFAULT_MOBILE_NODES
    global _MOBILE_NODES_AT_NONE
    global _MOBILE_NODES_AT_NONE_CARRY
    SIM_DEFAULT_POSTURE_TYPE = PostureGraphService.get_default_affordance(Species.HUMAN).provided_posture_type
    STAND_AT_NONE = get_origin_spec(SIM_DEFAULT_POSTURE_TYPE)
    STAND_AT_NONE_CARRY = get_origin_spec_carry(SIM_DEFAULT_POSTURE_TYPE)
    STAND_AT_NONE_NODES = (STAND_AT_NONE, STAND_AT_NONE_CARRY)
    SIM_DEFAULT_AOPS = enumdict(Species, {species: AffordanceObjectPair(affordance, None, affordance, None, force_inertial=True) for species, affordance in PostureGraphService.SIM_DEFAULT_AFFORDANCES.items()})
    SIM_DEFAULT_OPERATION = PostureOperation.BodyTransition(SIM_DEFAULT_POSTURE_TYPE, SIM_DEFAULT_AOPS)
    SIM_SWIM_POSTURE_TYPE = PostureGraphService.get_default_swim_affordance(Species.HUMAN).provided_posture_type
    SWIM_AT_NONE = get_origin_spec(SIM_SWIM_POSTURE_TYPE)
    SWIM_AT_NONE_CARRY = get_origin_spec_carry(SIM_SWIM_POSTURE_TYPE)
    SWIM_AT_NONE_NODES = (SWIM_AT_NONE, SWIM_AT_NONE_CARRY)
    SIM_SWIM_AOPS = enumdict(Species, {species: AffordanceObjectPair(affordance, None, affordance, None, force_inertial=True) for species, affordance in PostureGraphService.SWIM_DEFAULT_AFFORDANCES.items()})
    SIM_SWIM_OPERATION = PostureOperation.BodyTransition(SIM_SWIM_POSTURE_TYPE, SIM_SWIM_AOPS)
    _MOBILE_NODES_AT_NONE = {
     STAND_AT_NONE}
    _MOBILE_NODES_AT_NONE_CARRY = {STAND_AT_NONE_CARRY}
    _DEFAULT_MOBILE_NODES = {STAND_AT_NONE, STAND_AT_NONE_CARRY}
    for affordance in PostureGraphService.POSTURE_PROVIDING_AFFORDANCES:
        if affordance.provided_posture_type is not None and affordance.provided_posture_type.mobile:
            posture_type = affordance.provided_posture_type.skip_route or affordance.provided_posture_type
            mobile_node_at_none = get_origin_spec(posture_type)
            _MOBILE_NODES_AT_NONE.add(mobile_node_at_none)
            _DEFAULT_MOBILE_NODES.add(mobile_node_at_none)
            if posture_type._supports_carry:
                mobile_node_at_none_carry = get_origin_spec_carry(posture_type)
                _MOBILE_NODES_AT_NONE_CARRY.add(mobile_node_at_none_carry)
                _DEFAULT_MOBILE_NODES.add(mobile_node_at_none_carry)


def get_mobile_posture_constraint(posture=None, target=None):
    posture_manifests = []
    body_target = target
    if posture is not None:
        if posture is SIM_DEFAULT_POSTURE_TYPE:
            return STAND_AT_NONE_CONSTRAINT
        else:
            if posture is SIM_SWIM_POSTURE_TYPE:
                return SWIM_AT_NONE_CONSTRAINT
            posture.mobile or logger.error('Cannot create mobile posture constraint from non-mobile posture {}', posture)
            return Nowhere('Mobile posture override {} is not actually mobile.', posture)
        posture_manifests = [posture.get_provided_postures()]
    if (posture_manifests or target) is not None:
        for mobile_posture in target.provided_mobile_posture_types:
            posture_manifests.append(mobile_posture.get_provided_postures())
            if mobile_posture.unconstrained:
                body_target = None
            break

    else:
        if posture_manifests:
            if target is not None and target.routing_component is None:
                body_target = PostureSpecVariable.ANYTHING
    constraints = []
    for manifest in posture_manifests:
        posture_state_spec = create_body_posture_state_spec(manifest, body_target=body_target)
        constraint = Constraint(debug_name='MobilePosture@None', posture_state_spec=posture_state_spec)
        constraints.append(constraint)

    if constraints:
        return create_constraint_set(constraints, debug_name='MobilePostureConstraints')
    return STAND_AT_NONE_CONSTRAINT


def is_object_mobile_posture_compatible(obj):
    return any((posture_type.posture_objects is not None for posture_type in obj.provided_mobile_posture_types))


@contextmanager
def supress_posture_graph_build(rebuild=True):
    posture_graph_service = services.current_zone().posture_graph_service
    posture_graph_service.disable_graph_building()
    try:
        yield
    finally:
        posture_graph_service.enable_graph_building()
        if rebuild:
            posture_graph_service.rebuild()


def can_remove_blocking_sims(sim, interaction, required_targets):
    need_to_cancel = []
    blocking_sims = set()
    for obj in required_targets:
        obj_users = obj.get_users()
        if not obj_users:
            if obj.is_part:
                obj = obj.part_owner
                obj_users = obj.get_users()
        for blocking_sim in obj_users:
            if blocking_sim is sim:
                continue
            if not blocking_sim.is_sim:
                return (
                 False, need_to_cancel, blocking_sims)
                for blocking_si in blocking_sim.si_state:
                    if not obj.is_same_object_or_part(blocking_si.target):
                        continue
                    if not blocking_si.can_shoo or blocking_si.priority >= interaction.priority:
                        return (
                         False, need_to_cancel, blocking_sims)
                    need_to_cancel.append(blocking_si)
                    blocking_sims.add(blocking_sim)

    return (
     True, need_to_cancel, blocking_sims)


class TransitionSpec:
    DISTANCE_TO_FADE_SIM_OUT = Tunable(description='\n        Distance at which a Sim will start fading out if tuned as such.\n        ',
      tunable_type=float,
      default=5.0)


@cython.cfunc
@cython.exceptval(check=False)
def TransitionSpecCython_create(path_spec, posture_spec: PostureSpec, var_map, sequence_id=SequenceId.DEFAULT, portal_obj=None, portal_id=None) -> 'TransitionSpecCython':
    self = cython.declare(TransitionSpecCython, TransitionSpecCython.__new__(TransitionSpecCython))
    self.posture_spec = posture_spec
    self._path_spec = path_spec
    self.var_map = var_map
    self.path = None
    self.final_constraint = None
    self._transition_interactions = {}
    self.sequence_id = sequence_id
    self.locked_params = frozendict()
    self._additional_reservation_handlers = []
    self.handle_slot_reservations = False
    self._portal_ref = portal_obj.ref() if portal_obj is not None else None
    self.portal_id = portal_id
    self.created_posture_state = None
    return self


@cython.cclass
class TransitionSpecCython:
    posture_spec = cython.declare(PostureSpec, visibility='readonly')
    _path_spec = cython.declare(object, visibility='public')
    var_map = cython.declare(object, visibility='public')
    path = cython.declare(object, visibility='public')
    final_constraint = cython.declare(object, visibility='readonly')
    _transition_interactions = cython.declare(dict, visibility='readonly')
    sequence_id = cython.declare(object, visibility='readonly')
    locked_params = cython.declare(object, visibility='public')
    _additional_reservation_handlers: list
    handle_slot_reservations = cython.declare((cython.bint), visibility='public')
    _portal_ref: object
    portal_id = cython.declare(object, visibility='public')
    created_posture_state = cython.declare(object, visibility='public')

    @property
    def mobile(self):
        return self.posture_spec.body.posture_type.mobile

    @property
    def is_failure_path(self):
        return self._path_spec.is_failure_path

    @property
    def final_si(self):
        return self._path_spec._final_si

    @property
    def is_carry(self):
        return self.posture_spec.carry.target is not None

    @property
    def targets_empty_slot(self):
        surface_spec = self.posture_spec.surface
        if surface_spec.slot_type is not None:
            if surface_spec.slot_target is None:
                return True
        return False

    @property
    def portal_obj(self):
        if self._portal_ref is not None:
            return self._portal_ref()

    @portal_obj.setter
    def portal_obj(self, value):
        if value is None:
            self._portal_ref = None
        else:
            if issubclass(value.__class__, ProxyObject):
                self._portal_ref = value.ref()
            else:
                self._portal_ref = weakref.ref(value)

    def transition_interactions(self, sim):
        if sim in self._transition_interactions:
            return self._transition_interactions[sim]
        return []

    def test_transition_interactions(self, sim, interaction):
        if sim in self._transition_interactions:
            for si, _ in self._transition_interactions[sim]:
                if si is interaction:
                    continue
                if si is not None:
                    return si.aop.test(si.context) or False

        return True

    def get_multi_target_interaction(self, sim):
        final_si = self._path_spec._final_si
        if sim in self._transition_interactions:
            for si, _ in self._transition_interactions[sim]:
                if si is not final_si:
                    return si

    @cython.ccall
    @cython.exceptval(check=False)
    def set_path(self, path, final_constraint) -> cython.void:
        self.path = path
        if final_constraint is not None and final_constraint.tentative:
            logger.warn("TransitionSpec's final constraint is tentative, this will not work correctly so the constraint will be ignored. This may interfere with slot reservation.", owner='jpollak')
        else:
            self.final_constraint = final_constraint

    def transfer_route_to(self, other_spec):
        other_spec.path = self.path
        self.path = None

    def add_transition_interaction(self, sim, interaction, var_map):
        if interaction is not None:
            if not interaction.get_participant_type(sim) == ParticipantType.Actor:
                return
        if sim not in self._transition_interactions:
            self._transition_interactions[sim] = []
        self._transition_interactions[sim].append((interaction, var_map))

    def set_locked_params(self, locked_params):
        self.locked_params = locked_params

    def __repr__(self):
        args = [
         self.posture_spec]
        kwargs = {}
        if self.path is not None:
            args.append(suppress_quotes('has_route'))
        if self.locked_params:
            kwargs['locked_params'] = self.locked_params
        if self.final_constraint is not None:
            kwargs['final_constraint'] = self.final_constraint
        return standard_angle_repr(self, *args, **kwargs)

    def release_additional_reservation_handlers(self):
        for handler in self._additional_reservation_handlers:
            handler.end_reservation()

        self._additional_reservation_handlers.clear()

    def remove_props_created_to_reserve_slots(self, sim):
        if self._transition_interactions is not None:
            for reservation_si, _ in self._transition_interactions.get(sim, ()):
                if reservation_si is not None:
                    reservation_si.animation_context.clear_reserved_slots()

    def do_reservation--- This code section failed: ---

 L.1187         0  LOAD_CLOSURE             'reserve_object_handlers'
                2  BUILD_TUPLE_1         1 
                4  LOAD_CODE                <code_object cancel_reservations>
                6  LOAD_STR                 'TransitionSpecCython.do_reservation.<locals>.cancel_reservations'
                8  MAKE_FUNCTION_8          'closure'
               10  STORE_DEREF              'cancel_reservations'

 L.1191        12  LOAD_CONST               (False,)
               14  LOAD_CLOSURE             'cancel_reservations'
               16  LOAD_CLOSURE             'reserve_object_handlers'
               18  LOAD_CLOSURE             'sim'
               20  BUILD_TUPLE_3         3 
               22  LOAD_CODE                <code_object add_reservation>
               24  LOAD_STR                 'TransitionSpecCython.do_reservation.<locals>.add_reservation'
               26  MAKE_FUNCTION_9          'default, closure'
               28  STORE_FAST               'add_reservation'

 L.1207     30_32  SETUP_EXCEPT       1132  'to 1132'

 L.1210        34  LOAD_GLOBAL              set
               36  CALL_FUNCTION_0       0  '0 positional arguments'
               38  STORE_DEREF              'reserve_object_handlers'

 L.1212        40  BUILD_LIST_0          0 
               42  STORE_FAST               'reservations_sis'

 L.1213        44  LOAD_FAST                'self'
               46  STORE_FAST               'reservation_spec'

 L.1214        48  SETUP_LOOP          120  'to 120'
             50_0  COME_FROM           112  '112'
             50_1  COME_FROM           102  '102'
               50  LOAD_FAST                'reservation_spec'
               52  LOAD_CONST               None
               54  COMPARE_OP               is-not
               56  POP_JUMP_IF_FALSE   118  'to 118'

 L.1215        58  LOAD_DEREF               'sim'
               60  LOAD_FAST                'reservation_spec'
               62  LOAD_ATTR                _transition_interactions
               64  COMPARE_OP               in
               66  POP_JUMP_IF_FALSE    84  'to 84'

 L.1216        68  LOAD_FAST                'reservations_sis'
               70  LOAD_METHOD              extend
               72  LOAD_FAST                'reservation_spec'
               74  LOAD_ATTR                _transition_interactions
               76  LOAD_DEREF               'sim'
               78  BINARY_SUBSCR    
               80  CALL_METHOD_1         1  '1 positional argument'
               82  POP_TOP          
             84_0  COME_FROM            66  '66'

 L.1217        84  LOAD_FAST                'self'
               86  LOAD_ATTR                _path_spec
               88  LOAD_METHOD              get_next_transition_spec
               90  LOAD_FAST                'reservation_spec'
               92  CALL_METHOD_1         1  '1 positional argument'
               94  STORE_FAST               'reservation_spec'

 L.1220        96  LOAD_FAST                'reservation_spec'
               98  LOAD_CONST               None
              100  COMPARE_OP               is-not
              102  POP_JUMP_IF_FALSE    50  'to 50'
              104  LOAD_FAST                'reservation_spec'
              106  LOAD_ATTR                path
              108  LOAD_CONST               None
              110  COMPARE_OP               is-not
              112  POP_JUMP_IF_FALSE    50  'to 50'

 L.1221       114  BREAK_LOOP       
              116  JUMP_BACK            50  'to 50'
            118_0  COME_FROM            56  '56'
              118  POP_BLOCK        
            120_0  COME_FROM_LOOP       48  '48'

 L.1223       120  LOAD_FAST                'is_failure_path'
              122  POP_JUMP_IF_FALSE   132  'to 132'
              124  LOAD_FAST                'reservations_sis'
              126  POP_JUMP_IF_TRUE    132  'to 132'

 L.1224       128  LOAD_CONST               False
              130  RETURN_VALUE     
            132_0  COME_FROM           126  '126'
            132_1  COME_FROM           122  '122'

 L.1226   132_134  SETUP_LOOP          666  'to 666'
              136  LOAD_FAST                'reservations_sis'
              138  GET_ITER         
            140_0  COME_FROM           534  '534'
          140_142  FOR_ITER            664  'to 664'
              144  UNPACK_SEQUENCE_2     2 
              146  STORE_FAST               'si'
              148  STORE_FAST               '_'

 L.1227       150  LOAD_FAST                'si'
              152  LOAD_CONST               None
              154  COMPARE_OP               is
              156  POP_JUMP_IF_FALSE   160  'to 160'

 L.1228       158  CONTINUE            140  'to 140'
            160_0  COME_FROM           156  '156'

 L.1229       160  LOAD_FAST                'si'
              162  LOAD_ATTR                is_putdown
              164  POP_JUMP_IF_FALSE   196  'to 196'

 L.1230       166  LOAD_FAST                'si'
              168  LOAD_METHOD              get_target_si
              170  CALL_METHOD_0         0  '0 positional arguments'
              172  UNPACK_SEQUENCE_2     2 
              174  STORE_FAST               'target_si'
              176  STORE_FAST               '_'

 L.1231       178  LOAD_FAST                'target_si'
              180  LOAD_CONST               None
              182  COMPARE_OP               is-not
              184  POP_JUMP_IF_FALSE   196  'to 196'

 L.1232       186  LOAD_FAST                'target_si'
              188  STORE_FAST               'si'

 L.1233       190  LOAD_FAST                'si'
              192  LOAD_ATTR                sim
              194  STORE_DEREF              'sim'
            196_0  COME_FROM           184  '184'
            196_1  COME_FROM           164  '164'

 L.1234       196  LOAD_FAST                'si'
              198  LOAD_METHOD              get_liability
              200  LOAD_GLOBAL              RESERVATION_LIABILITY
              202  CALL_METHOD_1         1  '1 positional argument'
              204  LOAD_CONST               None
              206  COMPARE_OP               is-not
              208  POP_JUMP_IF_FALSE   212  'to 212'

 L.1236       210  CONTINUE            140  'to 140'
            212_0  COME_FROM           208  '208'

 L.1238       212  LOAD_FAST                'si'
              214  LOAD_ATTR                get_interaction_reservation_handler
              216  LOAD_DEREF               'sim'
              218  LOAD_CONST               ('sim',)
              220  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              222  STORE_FAST               'handler'

 L.1239       224  LOAD_FAST                'is_failure_path'
              226  POP_JUMP_IF_FALSE   238  'to 238'
              228  LOAD_FAST                'handler'
              230  LOAD_CONST               None
              232  COMPARE_OP               is
              234  POP_JUMP_IF_FALSE   238  'to 238'

 L.1240       236  CONTINUE            140  'to 140'
            238_0  COME_FROM           234  '234'
            238_1  COME_FROM           226  '226'

 L.1242       238  LOAD_FAST                'handler'
              240  LOAD_CONST               None
              242  COMPARE_OP               is-not
          244_246  POP_JUMP_IF_FALSE   516  'to 516'

 L.1243       248  BUILD_LIST_0          0 
              250  STORE_FAST               'handlers'

 L.1244       252  LOAD_FAST                'is_failure_path'
          254_256  POP_JUMP_IF_FALSE   272  'to 272'

 L.1248       258  LOAD_FAST                'add_reservation'
              260  LOAD_FAST                'handler'
              262  LOAD_CONST               True
              264  LOAD_CONST               ('test_only',)
              266  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              268  STORE_FAST               'reserve_result'
              270  JUMP_FORWARD        280  'to 280'
            272_0  COME_FROM           254  '254'

 L.1250       272  LOAD_FAST                'add_reservation'
              274  LOAD_FAST                'handler'
              276  CALL_FUNCTION_1       1  '1 positional argument'
              278  STORE_FAST               'reserve_result'
            280_0  COME_FROM           270  '270'

 L.1251       280  LOAD_FAST                'reserve_result'
          282_284  POP_JUMP_IF_TRUE    476  'to 476'

 L.1252       286  LOAD_FAST                'si'
              288  LOAD_ATTR                source
              290  LOAD_GLOBAL              InteractionSource
              292  LOAD_ATTR                BODY_CANCEL_AOP
              294  COMPARE_OP               ==
          296_298  POP_JUMP_IF_TRUE    314  'to 314'

 L.1253       300  LOAD_FAST                'si'
              302  LOAD_ATTR                source
              304  LOAD_GLOBAL              InteractionSource
              306  LOAD_ATTR                CARRY_CANCEL_AOP
              308  COMPARE_OP               ==
          310_312  POP_JUMP_IF_FALSE   334  'to 334'
            314_0  COME_FROM           296  '296'

 L.1258       314  LOAD_GLOBAL              logger
              316  LOAD_ATTR                warn
              318  LOAD_STR                 '{} failed to pass reservation tests as a cancel AOP. Result: {}'
              320  LOAD_FAST                'si'
              322  LOAD_FAST                'reserve_result'
              324  LOAD_STR                 'cgast'
              326  LOAD_CONST               ('owner',)
              328  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              330  POP_TOP          

 L.1259       332  CONTINUE            140  'to 140'
            334_0  COME_FROM           310  '310'

 L.1261       334  LOAD_FAST                'si'
              336  LOAD_ATTR                priority
              338  LOAD_GLOBAL              Priority
              340  LOAD_ATTR                Low
              342  COMPARE_OP               ==
          344_346  POP_JUMP_IF_FALSE   352  'to 352'

 L.1265       348  LOAD_CONST               False
              350  RETURN_VALUE     
            352_0  COME_FROM           344  '344'

 L.1270       352  LOAD_GLOBAL              can_remove_blocking_sims
              354  LOAD_DEREF               'sim'
              356  LOAD_FAST                'si'
              358  LOAD_FAST                'handler'
              360  LOAD_METHOD              get_targets
              362  CALL_METHOD_0         0  '0 positional arguments'
              364  CALL_FUNCTION_3       3  '3 positional arguments'
              366  UNPACK_SEQUENCE_3     3 
              368  STORE_FAST               'able_to_cancel_blockers'
              370  STORE_FAST               'need_to_cancel'
              372  STORE_FAST               'blocking_sims'

 L.1271       374  LOAD_FAST                'able_to_cancel_blockers'
          376_378  POP_JUMP_IF_TRUE    384  'to 384'

 L.1272       380  LOAD_CONST               False
              382  RETURN_VALUE     
            384_0  COME_FROM           376  '376'

 L.1274       384  LOAD_FAST                'need_to_cancel'
          386_388  POP_JUMP_IF_FALSE   472  'to 472'

 L.1275       390  SETUP_LOOP          416  'to 416'
              392  LOAD_FAST                'need_to_cancel'
              394  GET_ITER         
              396  FOR_ITER            414  'to 414'
              398  STORE_FAST               'blocking_si'

 L.1276       400  LOAD_FAST                'blocking_si'
              402  LOAD_METHOD              cancel_user
              404  LOAD_STR                 'Sim was kicked out by another Sim with a higher priority interaction.'
              406  CALL_METHOD_1         1  '1 positional argument'
              408  POP_TOP          
          410_412  JUMP_BACK           396  'to 396'
              414  POP_BLOCK        
            416_0  COME_FROM_LOOP      390  '390'

 L.1278       416  SETUP_LOOP          440  'to 440'
              418  LOAD_FAST                'blocking_sims'
              420  GET_ITER         
              422  FOR_ITER            438  'to 438'
              424  STORE_FAST               'blocking_sim'

 L.1279       426  LOAD_GLOBAL              push_route_away
              428  LOAD_FAST                'blocking_sim'
              430  CALL_FUNCTION_1       1  '1 positional argument'
              432  POP_TOP          
          434_436  JUMP_BACK           422  'to 422'
              438  POP_BLOCK        
            440_0  COME_FROM_LOOP      416  '416'

 L.1281       440  LOAD_DEREF               'sim'
              442  LOAD_ATTR                queue
              444  LOAD_ATTR                transition_controller
              446  LOAD_METHOD              add_blocked_si
              448  LOAD_FAST                'si'
              450  CALL_METHOD_1         1  '1 positional argument'
              452  POP_TOP          

 L.1282       454  LOAD_DEREF               'sim'
              456  LOAD_ATTR                queue
              458  LOAD_ATTR                transition_controller
              460  LOAD_METHOD              derail

 L.1283       462  LOAD_GLOBAL              DerailReason
              464  LOAD_ATTR                WAIT_FOR_BLOCKING_SIMS
              466  LOAD_DEREF               'sim'
              468  CALL_METHOD_2         2  '2 positional arguments'
              470  POP_TOP          
            472_0  COME_FROM           386  '386'

 L.1285       472  LOAD_CONST               False
              474  RETURN_VALUE     
            476_0  COME_FROM           282  '282'

 L.1287       476  LOAD_FAST                'is_failure_path'
          478_480  POP_JUMP_IF_FALSE   486  'to 486'

 L.1288       482  LOAD_CONST               False
              484  RETURN_VALUE     
            486_0  COME_FROM           478  '478'

 L.1290       486  LOAD_FAST                'handlers'
              488  LOAD_METHOD              append
              490  LOAD_FAST                'handler'
              492  CALL_METHOD_1         1  '1 positional argument'
              494  POP_TOP          

 L.1292       496  LOAD_GLOBAL              ReservationLiability
              498  LOAD_FAST                'handlers'
              500  CALL_FUNCTION_1       1  '1 positional argument'
              502  STORE_FAST               'liability'

 L.1293       504  LOAD_FAST                'si'
              506  LOAD_METHOD              add_liability
              508  LOAD_GLOBAL              RESERVATION_LIABILITY
              510  LOAD_FAST                'liability'
              512  CALL_METHOD_2         2  '2 positional arguments'
              514  POP_TOP          
            516_0  COME_FROM           244  '244'

 L.1297       516  LOAD_FAST                'self'
              518  LOAD_ATTR                _path_spec
              520  LOAD_METHOD              get_next_transition_spec
              522  LOAD_FAST                'self'
              524  CALL_METHOD_1         1  '1 positional argument'
              526  STORE_FAST               'next_spec'

 L.1298       528  LOAD_FAST                'next_spec'
              530  LOAD_CONST               None
              532  COMPARE_OP               is-not
              534  POP_JUMP_IF_FALSE   140  'to 140'

 L.1299       536  LOAD_GLOBAL              set
              538  CALL_FUNCTION_0       0  '0 positional arguments'
              540  STORE_FAST               'target_set'

 L.1300       542  LOAD_FAST                'target_set'
              544  LOAD_METHOD              add
              546  LOAD_FAST                'next_spec'
              548  LOAD_ATTR                posture_spec
              550  LOAD_ATTR                body_target
              552  CALL_METHOD_1         1  '1 positional argument'
              554  POP_TOP          

 L.1301       556  LOAD_FAST                'target_set'
              558  LOAD_METHOD              add
              560  LOAD_FAST                'next_spec'
              562  LOAD_ATTR                posture_spec
              564  LOAD_ATTR                surface_target
              566  CALL_METHOD_1         1  '1 positional argument'
              568  POP_TOP          

 L.1302       570  SETUP_LOOP          662  'to 662'
              572  LOAD_FAST                'target_set'
              574  GET_ITER         
            576_0  COME_FROM           640  '640'
            576_1  COME_FROM           586  '586'
              576  FOR_ITER            660  'to 660'
              578  STORE_FAST               'target'

 L.1303       580  LOAD_FAST                'target'
              582  LOAD_CONST               None
              584  COMPARE_OP               is
          586_588  POP_JUMP_IF_TRUE    576  'to 576'
              590  LOAD_FAST                'handler'
              592  LOAD_CONST               None
              594  COMPARE_OP               is-not
          596_598  POP_JUMP_IF_FALSE   618  'to 618'
              600  LOAD_FAST                'target'
              602  LOAD_FAST                'handler'
              604  LOAD_METHOD              get_targets
              606  CALL_METHOD_0         0  '0 positional arguments'
              608  COMPARE_OP               in
          610_612  POP_JUMP_IF_FALSE   618  'to 618'

 L.1304   614_616  CONTINUE            576  'to 576'
            618_0  COME_FROM           610  '610'
            618_1  COME_FROM           596  '596'

 L.1305       618  LOAD_GLOBAL              ReservationHandlerMulti
              620  LOAD_DEREF               'sim'
              622  LOAD_FAST                'target'
              624  LOAD_FAST                'si'
              626  LOAD_CONST               None
              628  LOAD_CONST               ('reservation_interaction', 'reservation_limit')
              630  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              632  STORE_FAST               'target_handler'

 L.1306       634  LOAD_FAST                'add_reservation'
              636  LOAD_FAST                'target_handler'
              638  CALL_FUNCTION_1       1  '1 positional argument'
          640_642  POP_JUMP_IF_FALSE   576  'to 576'

 L.1307       644  LOAD_FAST                'self'
              646  LOAD_ATTR                _additional_reservation_handlers
              648  LOAD_METHOD              append
              650  LOAD_FAST                'target_handler'
              652  CALL_METHOD_1         1  '1 positional argument'
              654  POP_TOP          
          656_658  JUMP_BACK           576  'to 576'
              660  POP_BLOCK        
            662_0  COME_FROM_LOOP      570  '570'
              662  JUMP_BACK           140  'to 140'
              664  POP_BLOCK        
            666_0  COME_FROM_LOOP      132  '132'

 L.1309       666  LOAD_FAST                'is_failure_path'
          668_670  POP_JUMP_IF_FALSE   676  'to 676'

 L.1310       672  LOAD_CONST               False
              674  RETURN_VALUE     
            676_0  COME_FROM           668  '668'

 L.1312       676  LOAD_DEREF               'sim'
              678  LOAD_ATTR                posture
              680  LOAD_ATTR                retrieve_objects_on_exit
              682  STORE_FAST               'retrieve_posture_objects'

 L.1313       684  LOAD_FAST                'retrieve_posture_objects'
              686  LOAD_CONST               None
              688  COMPARE_OP               is-not
          690_692  POP_JUMP_IF_FALSE   748  'to 748'

 L.1314       694  LOAD_FAST                'retrieve_posture_objects'
              696  LOAD_ATTR                transition_retrieval_affordance
              698  LOAD_CONST               None
              700  COMPARE_OP               is-not
          702_704  POP_JUMP_IF_FALSE   748  'to 748'

 L.1319       706  LOAD_GLOBAL              SingleActorAndObjectResolver
              708  LOAD_DEREF               'sim'

 L.1320       710  LOAD_DEREF               'sim'
              712  LOAD_ATTR                posture
              714  LOAD_ATTR                target

 L.1321       716  LOAD_STR                 'PostureScoring'
              718  LOAD_CONST               ('source',)
              720  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              722  STORE_FAST               'resolver'

 L.1322       724  LOAD_FAST                'retrieve_posture_objects'
              726  LOAD_ATTR                objects_to_retrieve
              728  LOAD_METHOD              get_objects
              730  LOAD_FAST                'resolver'
              732  CALL_METHOD_1         1  '1 positional argument'
              734  STORE_FAST               'objects_to_retrieve'

 L.1323       736  LOAD_FAST                'objects_to_retrieve'
          738_740  POP_JUMP_IF_FALSE   748  'to 748'

 L.1324       742  LOAD_CONST               False
              744  LOAD_FAST                'self'
              746  STORE_ATTR               handle_slot_reservations
            748_0  COME_FROM           738  '738'
            748_1  COME_FROM           702  '702'
            748_2  COME_FROM           690  '690'

 L.1327       748  LOAD_FAST                'self'
              750  LOAD_ATTR                handle_slot_reservations
          752_754  POP_JUMP_IF_FALSE  1126  'to 1126'

 L.1330       756  BUILD_LIST_0          0 
              758  STORE_FAST               'object_to_ignore'

 L.1331       760  SETUP_LOOP          866  'to 866'
              762  LOAD_FAST                'self'
              764  LOAD_ATTR                _transition_interactions
              766  LOAD_DEREF               'sim'
              768  BINARY_SUBSCR    
              770  GET_ITER         
            772_0  COME_FROM           842  '842'
            772_1  COME_FROM           800  '800'
            772_2  COME_FROM           788  '788'
              772  FOR_ITER            864  'to 864'
              774  UNPACK_SEQUENCE_2     2 
              776  STORE_FAST               'transition_si'
              778  STORE_FAST               '_'

 L.1332       780  LOAD_GLOBAL              hasattr
              782  LOAD_FAST                'transition_si'
              784  LOAD_STR                 'process'
              786  CALL_FUNCTION_2       2  '2 positional arguments'
          788_790  POP_JUMP_IF_FALSE   772  'to 772'

 L.1333       792  LOAD_FAST                'transition_si'
              794  LOAD_ATTR                process
              796  LOAD_CONST               None
              798  COMPARE_OP               is-not
          800_802  POP_JUMP_IF_FALSE   772  'to 772'

 L.1334       804  LOAD_FAST                'transition_si'
              806  LOAD_ATTR                process
              808  LOAD_ATTR                previous_ico
              810  LOAD_CONST               None
              812  COMPARE_OP               is-not
          814_816  POP_JUMP_IF_FALSE   832  'to 832'

 L.1335       818  LOAD_FAST                'object_to_ignore'
              820  LOAD_METHOD              append
              822  LOAD_FAST                'transition_si'
              824  LOAD_ATTR                process
              826  LOAD_ATTR                previous_ico
              828  CALL_METHOD_1         1  '1 positional argument'
              830  POP_TOP          
            832_0  COME_FROM           814  '814'

 L.1336       832  LOAD_FAST                'transition_si'
              834  LOAD_ATTR                process
              836  LOAD_ATTR                current_ico
              838  LOAD_CONST               None
              840  COMPARE_OP               is-not
          842_844  POP_JUMP_IF_FALSE   772  'to 772'

 L.1337       846  LOAD_FAST                'object_to_ignore'
              848  LOAD_METHOD              append
              850  LOAD_FAST                'transition_si'
              852  LOAD_ATTR                process
              854  LOAD_ATTR                current_ico
              856  CALL_METHOD_1         1  '1 positional argument'
              858  POP_TOP          
          860_862  JUMP_BACK           772  'to 772'
              864  POP_BLOCK        
            866_0  COME_FROM_LOOP      760  '760'

 L.1342       866  LOAD_FAST                'self'
              868  STORE_FAST               'cur_spec'

 L.1343       870  BUILD_LIST_0          0 
              872  STORE_FAST               'slot_manifest_entries'

 L.1344       874  SETUP_LOOP         1014  'to 1014'
              876  LOAD_FAST                'cur_spec'
              878  LOAD_CONST               None
              880  COMPARE_OP               is-not
          882_884  POP_JUMP_IF_FALSE  1012  'to 1012'

 L.1345       886  LOAD_FAST                'cur_spec'
              888  LOAD_FAST                'self'
              890  COMPARE_OP               is-not
          892_894  POP_JUMP_IF_FALSE   910  'to 910'
              896  LOAD_FAST                'cur_spec'
              898  LOAD_ATTR                path
              900  LOAD_CONST               None
              902  COMPARE_OP               is-not
          904_906  POP_JUMP_IF_FALSE   910  'to 910'

 L.1348       908  BREAK_LOOP       
            910_0  COME_FROM           904  '904'
            910_1  COME_FROM           892  '892'

 L.1350       910  LOAD_FAST                'cur_spec'
              912  LOAD_ATTR                handle_slot_reservations
          914_916  POP_JUMP_IF_FALSE   996  'to 996'

 L.1353       918  LOAD_GLOBAL              PostureSpecVariable
              920  LOAD_ATTR                SLOT
              922  LOAD_FAST                'cur_spec'
              924  LOAD_ATTR                var_map
              926  COMPARE_OP               in
          928_930  POP_JUMP_IF_FALSE   972  'to 972'

 L.1354       932  LOAD_FAST                'cur_spec'
              934  LOAD_ATTR                var_map
              936  LOAD_GLOBAL              PostureSpecVariable
              938  LOAD_ATTR                SLOT
              940  BINARY_SUBSCR    
              942  STORE_FAST               'slot_entry'

 L.1355       944  LOAD_FAST                'slot_entry'
              946  LOAD_CONST               None
              948  COMPARE_OP               is-not
          950_952  POP_JUMP_IF_FALSE   996  'to 996'

 L.1356       954  LOAD_FAST                'slot_manifest_entries'
              956  LOAD_METHOD              append
              958  LOAD_FAST                'slot_entry'
              960  CALL_METHOD_1         1  '1 positional argument'
              962  POP_TOP          

 L.1357       964  LOAD_CONST               False
              966  LOAD_FAST                'cur_spec'
              968  STORE_ATTR               handle_slot_reservations
              970  JUMP_FORWARD        996  'to 996'
            972_0  COME_FROM           928  '928'

 L.1359       972  LOAD_GLOBAL              logger
              974  LOAD_METHOD              error
              976  LOAD_STR                 'Trying to reserve a surface with no PostureSpecVariable.SLOT in the var_map.\n    Sim: {}\n    Spec: {}\n    Var_map: {}\n    Transition: {}'

 L.1360       978  LOAD_DEREF               'sim'
              980  LOAD_FAST                'cur_spec'
              982  LOAD_FAST                'cur_spec'
              984  LOAD_ATTR                var_map
              986  LOAD_FAST                'cur_spec'
              988  LOAD_ATTR                _path_spec
              990  LOAD_ATTR                path
              992  CALL_METHOD_5         5  '5 positional arguments'
              994  POP_TOP          
            996_0  COME_FROM           970  '970'
            996_1  COME_FROM           950  '950'
            996_2  COME_FROM           914  '914'

 L.1361       996  LOAD_FAST                'self'
              998  LOAD_ATTR                _path_spec
             1000  LOAD_METHOD              get_next_transition_spec
             1002  LOAD_FAST                'cur_spec'
             1004  CALL_METHOD_1         1  '1 positional argument'
             1006  STORE_FAST               'cur_spec'
         1008_1010  JUMP_BACK           876  'to 876'
           1012_0  COME_FROM           882  '882'
             1012  POP_BLOCK        
           1014_0  COME_FROM_LOOP      874  '874'

 L.1363      1014  LOAD_FAST                'slot_manifest_entries'
         1016_1018  POP_JUMP_IF_FALSE  1126  'to 1126'

 L.1364      1020  LOAD_FAST                'self'
             1022  LOAD_ATTR                final_si
             1024  LOAD_ATTR                animation_context
             1026  STORE_FAST               'final_animation_context'

 L.1365      1028  SETUP_LOOP         1126  'to 1126'
             1030  LOAD_FAST                'slot_manifest_entries'
             1032  GET_ITER         
           1034_0  COME_FROM          1056  '1056'
             1034  FOR_ITER           1124  'to 1124'
             1036  STORE_FAST               'slot_manifest_entry'

 L.1366      1038  LOAD_FAST                'final_animation_context'
             1040  LOAD_ATTR                update_reserved_slots
             1042  LOAD_FAST                'slot_manifest_entry'
             1044  LOAD_DEREF               'sim'

 L.1367      1046  LOAD_FAST                'object_to_ignore'
             1048  LOAD_CONST               ('objects_to_ignore',)
             1050  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
             1052  STORE_FAST               'slot_result'

 L.1368      1054  LOAD_FAST                'slot_result'
         1056_1058  POP_JUMP_IF_TRUE   1034  'to 1034'

 L.1369      1060  LOAD_GLOBAL              set_transition_failure_reason
             1062  LOAD_DEREF               'sim'
             1064  LOAD_GLOBAL              TransitionFailureReasons
             1066  LOAD_ATTR                RESERVATION

 L.1370      1068  LOAD_FAST                'slot_manifest_entry'
             1070  LOAD_ATTR                target
             1072  LOAD_CONST               None
             1074  COMPARE_OP               is-not
         1076_1078  POP_JUMP_IF_FALSE  1088  'to 1088'
             1080  LOAD_FAST                'slot_manifest_entry'
             1082  LOAD_ATTR                target
             1084  LOAD_ATTR                id
             1086  JUMP_FORWARD       1090  'to 1090'
           1088_0  COME_FROM          1076  '1076'
             1088  LOAD_CONST               None
           1090_0  COME_FROM          1086  '1086'
             1090  LOAD_CONST               ('target_id',)
             1092  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
             1094  POP_TOP          

 L.1371      1096  LOAD_DEREF               'cancel_reservations'
             1098  CALL_FUNCTION_0       0  '0 positional arguments'
             1100  POP_TOP          

 L.1372      1102  LOAD_GLOBAL              TestResult
             1104  LOAD_CONST               False
             1106  LOAD_STR                 'Slot Reservation Failed for {}'
             1108  LOAD_METHOD              format
             1110  LOAD_FAST                'self'
             1112  LOAD_ATTR                final_si
             1114  CALL_METHOD_1         1  '1 positional argument'
             1116  CALL_FUNCTION_2       2  '2 positional arguments'
             1118  RETURN_VALUE     
         1120_1122  JUMP_BACK          1034  'to 1034'
             1124  POP_BLOCK        
           1126_0  COME_FROM_LOOP     1028  '1028'
           1126_1  COME_FROM          1016  '1016'
           1126_2  COME_FROM           752  '752'

 L.1374      1126  LOAD_GLOBAL              TestResult
             1128  LOAD_ATTR                TRUE
             1130  RETURN_VALUE     
           1132_0  COME_FROM_EXCEPT     30  '30'

 L.1375      1132  POP_TOP          
             1134  POP_TOP          
             1136  POP_TOP          

 L.1376      1138  LOAD_DEREF               'cancel_reservations'
             1140  CALL_FUNCTION_0       0  '0 positional arguments'
             1142  POP_TOP          

 L.1377      1144  LOAD_GLOBAL              logger
             1146  LOAD_METHOD              exception
             1148  LOAD_STR                 'Exception reserving for transition: {}'
             1150  LOAD_FAST                'self'
             1152  CALL_METHOD_2         2  '2 positional arguments'
             1154  POP_TOP          

 L.1378      1156  RAISE_VARARGS_0       0  'reraise'
             1158  POP_EXCEPT       
             1160  JUMP_FORWARD       1164  'to 1164'
             1162  END_FINALLY      
           1164_0  COME_FROM          1160  '1160'

Parse error at or near `COME_FROM_EXCEPT' instruction at offset 1132_0

    def get_approaching_portal(self):
        next_transition_spec = self._path_spec.get_next_transition_spec(self)
        if next_transition_spec is not None:
            if next_transition_spec.portal_obj is not None:
                return (
                 next_transition_spec.portal_obj, next_transition_spec.portal_id)
        return (None, None)

    def get_transition_route(self, sim, fade_out, lock_out_socials, dest_posture):
        if self.path is None:
            return
        fade_sim_out = fade_out or sim.is_hidden()
        reserve = True
        fire_service = services.get_fire_service()

        def route_callback(distance_left):
            nonlocal fade_sim_out
            nonlocal reserve
            if not self.is_failure_path:
                if distance_left < FollowPath.DISTANCE_TO_RECHECK_STAND_RESERVATION:
                    if sim.routing_component.on_slot is not None:
                        transition_controller = sim.queue.transition_controller
                        excluded_sims = transition_controller.get_transitioning_sims() if transition_controller is not None else ()
                        violators = tuple((violator for violator in sim.routing_component.get_stand_slot_reservation_violators(excluded_sims=excluded_sims) if violator.parent not in excluded_sims))
                        if violators:
                            if transition_controller is not None:
                                transition_controller.derail(DerailReason.WAIT_FOR_BLOCKING_SIMS, sim)
                            return FollowPath.Action.CANCEL
                elif reserve and distance_left < FollowPath.DISTANCE_TO_RECHECK_INUSE:
                    reserve = False
                    portal_obj, portal_id = self.get_approaching_portal()
                    if portal_obj is not None:
                        portal_cost_override = portal_obj.get_portal_cost_override(portal_id)
                        if portal_cost_override == routing.PORTAL_USE_LOCK:
                            transition_controller = sim.queue.transition_controller
                            if transition_controller is not None:
                                transition_controller.derail(DerailReason.WAIT_FOR_BLOCKING_SIMS, sim)
                            return FollowPath.Action.CANCEL
                        if portal_obj.lock_portal_on_use(portal_id):
                            portal_obj.set_portal_cost_override(portal_id, (routing.PORTAL_USE_LOCK), sim=sim)
                    if not self.do_reservation(sim, is_failure_path=(self.is_failure_path)):
                        return FollowPath.Action.CANCEL
            elif not self.is_failure_path:
                if distance_left < TransitionSpec.DISTANCE_TO_FADE_SIM_OUT:
                    if fade_sim_out:
                        fade_sim_out = False
                        dest_posture.sim.fade_out()
                    if lock_out_socials:
                        sim.socials_locked = True
            time_now = services.time_service().sim_now
            if time_now > sim.next_passive_balloon_unlock_time:
                PassiveBalloons.request_passive_balloon(sim, time_now)
            if fire_service.check_for_catching_on_fire(sim):
                if sim.queue.running is not None:
                    sim.queue.running.route_fail_on_transition_fail = False
                return FollowPath.Action.CANCEL
            return FollowPath.Action.CONTINUE

        def should_fade_in():
            if not fade_sim_out:
                return self.path.length() > 0
            return False

        return build_element((maybe(should_fade_in, build_element((lambda _: dest_posture.sim.fade_in()))),
         get_route_element_for_path(sim, (self.path), interaction=(sim.queue.transition_controller.interaction), callback_fn=route_callback,
           handle_failure=True)))


class PathSpec:

    def __init__--- This code section failed: ---

 L.1482         0  LOAD_FAST                'path'
                2  LOAD_CONST               None
                4  COMPARE_OP               is-not
                6  POP_JUMP_IF_FALSE    54  'to 54'
                8  LOAD_FAST                'path_as_posture_specs'
               10  POP_JUMP_IF_FALSE    54  'to 54'

 L.1483        12  BUILD_LIST_0          0 
               14  LOAD_FAST                'self'
               16  STORE_ATTR               _path

 L.1484        18  SETUP_LOOP           92  'to 92'
               20  LOAD_FAST                'path'
               22  GET_ITER         
               24  FOR_ITER             50  'to 50'
               26  STORE_FAST               'posture_spec'

 L.1485        28  LOAD_FAST                'self'
               30  LOAD_ATTR                _path
               32  LOAD_METHOD              append
               34  LOAD_GLOBAL              TransitionSpecCython_create
               36  LOAD_FAST                'self'
               38  LOAD_FAST                'posture_spec'
               40  LOAD_FAST                'var_map'
               42  CALL_FUNCTION_3       3  '3 positional arguments'
               44  CALL_METHOD_1         1  '1 positional argument'
               46  POP_TOP          
               48  JUMP_BACK            24  'to 24'
               50  POP_BLOCK        
               52  JUMP_FORWARD         92  'to 92'
             54_0  COME_FROM            10  '10'
             54_1  COME_FROM             6  '6'

 L.1487        54  LOAD_FAST                'path'
               56  LOAD_FAST                'self'
               58  STORE_ATTR               _path

 L.1488        60  LOAD_FAST                'self'
               62  LOAD_ATTR                _path
               64  LOAD_CONST               None
               66  COMPARE_OP               is-not
               68  POP_JUMP_IF_FALSE    92  'to 92'

 L.1489        70  SETUP_LOOP           92  'to 92'
               72  LOAD_FAST                'self'
               74  LOAD_ATTR                _path
               76  GET_ITER         
               78  FOR_ITER             90  'to 90'
               80  STORE_FAST               'transition_spec'

 L.1490        82  LOAD_FAST                'self'
               84  LOAD_FAST                'transition_spec'
               86  STORE_ATTR               _path_spec
               88  JUMP_BACK            78  'to 78'
               90  POP_BLOCK        
             92_0  COME_FROM_LOOP       70  '70'
             92_1  COME_FROM            68  '68'
             92_2  COME_FROM            52  '52'
             92_3  COME_FROM_LOOP       18  '18'

 L.1492        92  LOAD_FAST                'path_cost'
               94  LOAD_FAST                'self'
               96  STORE_ATTR               cost

 L.1494        98  LOAD_FAST                'destination_spec'
              100  LOAD_FAST                'self'
              102  STORE_ATTR               destination_spec

 L.1498       104  LOAD_CONST               False
              106  LOAD_FAST                'self'
              108  STORE_ATTR               completed_path

 L.1501       110  LOAD_CONST               0
              112  LOAD_FAST                'self'
              114  STORE_ATTR               _path_progress

 L.1504       116  LOAD_FAST                'is_failure_path'
              118  LOAD_FAST                'self'
              120  STORE_ATTR               _is_failure_path

 L.1506       122  LOAD_FAST                'failed_path_type'
              124  LOAD_FAST                'self'
              126  STORE_ATTR               _failed_path_type

 L.1511       128  LOAD_FAST                'allow_tentative'
              130  POP_JUMP_IF_TRUE    168  'to 168'
              132  LOAD_FAST                'final_constraint'
              134  LOAD_CONST               None
              136  COMPARE_OP               is-not
              138  POP_JUMP_IF_FALSE   168  'to 168'
              140  LOAD_FAST                'final_constraint'
              142  LOAD_ATTR                tentative
              144  POP_JUMP_IF_FALSE   168  'to 168'

 L.1512       146  LOAD_GLOBAL              logger
              148  LOAD_ATTR                warn
              150  LOAD_STR                 "PathSpec's final constraint is tentative, this will not work correctly so the constraint will be ignored. This may interfere with slot reservation."

 L.1514       152  LOAD_STR                 'jpollak'
              154  LOAD_CONST               ('owner',)
              156  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              158  POP_TOP          

 L.1515       160  LOAD_CONST               None
              162  LOAD_FAST                'self'
              164  STORE_ATTR               _final_constraint
              166  JUMP_FORWARD        174  'to 174'
            168_0  COME_FROM           144  '144'
            168_1  COME_FROM           138  '138'
            168_2  COME_FROM           130  '130'

 L.1517       168  LOAD_FAST                'final_constraint'
              170  LOAD_FAST                'self'
              172  STORE_ATTR               _final_constraint
            174_0  COME_FROM           166  '166'

 L.1519       174  LOAD_FAST                'spec_constraint'
              176  LOAD_FAST                'self'
              178  STORE_ATTR               _spec_constraint

 L.1521       180  LOAD_CONST               None
              182  LOAD_FAST                'self'
              184  STORE_ATTR               _final_si

Parse error at or near `COME_FROM_LOOP' instruction at offset 92_3

    def __repr__(self):
        if self._path:
            posture_specs = ['({}{}{})'.format(transition_spec.posture_spec, '(R)' if transition_spec.path is not None else '', '(P)' if transition_spec.portal_obj is not None else '') for transition_spec in self._path]
            if self.is_failure_path:
                return 'FAILURE PATH: PathSpec[{}]'.format('->'.join(posture_specs))
            return 'PathSpec[{}]'.format('->'.join(posture_specs))
        return 'PathSpec[Empty]'

    def __bool__(self):
        return bool(self._path)

    @property
    def path(self):
        if self._path is not None:
            return [transition_spec.posture_spec for transition_spec in self._path]
        return []

    @property
    def transition_specs(self):
        return self._path

    @property
    def path_progress(self):
        return self._path_progress

    @property
    def total_cost(self):
        return self.cost + self.routing_cost

    @property
    def routing_cost(self):
        routing_cost = 0
        if self._path is not None:
            for trans_spec in self._path:
                if trans_spec.path is not None:
                    routing_cost += trans_spec.path.length()

        return routing_cost

    @property
    def var_map(self):
        if self._path is not None:
            return self._path[self._path_progress].var_map
        return [{}]

    @property
    def remaining_path(self):
        if self._path is not None:
            if not self.completed_path:
                return [transition_spec.posture_spec for transition_spec in self._path[self._path_progress:]]
        return []

    @property
    def is_failure_path(self):
        return self._is_failure_path

    @property
    def failed_path_type(self):
        return self._failed_path_type

    def remaining_original_transition_specs(self):
        original_transition_specs = []
        if self._path is not None:
            if not self.completed_path:
                for spec in self._path[self._path_progress:]:
                    if spec.sequence_id == SequenceId.DEFAULT:
                        original_transition_specs.append(spec)

        return original_transition_specs

    @property
    def previous_posture_spec(self):
        previous_progress = self._path_progress - 1
        if previous_progress < 0 or previous_progress >= len(self._path):
            return
        return self._path[previous_progress].posture_spec

    @property
    def previous_transition_spec(self):
        previous_progress = self._path_progress - 1
        if previous_progress < 0 or previous_progress >= len(self._path):
            return
        return self._path[previous_progress]

    @property
    def final_constraint(self):
        if self._final_constraint is not None:
            return self._final_constraint
        if self._path is None:
            return
        for transition_spec in reversed(self._path):
            if transition_spec.final_constraint is not None:
                return transition_spec.final_constraint

    @property
    def final_routing_location(self):
        for transition_spec in reversed(self._path):
            if transition_spec.path is not None:
                return transition_spec.path.final_location

    @property
    def spec_constraint(self):
        return self._spec_constraint

    def advance_path(self):
        new_progress = self._path_progress + 1
        if new_progress < len(self._path):
            self._path_progress = new_progress
        else:
            self.completed_path = True

    def get_spec(self):
        return self._path[self._path_progress].posture_spec

    def get_transition_spec(self):
        return self._path[self._path_progress]

    def get_transition_should_reserve(self):
        for i, transition_spec in enumerate_reversed(self._path):
            if transition_spec.path is not None:
                return self._path_progress >= i

        return True

    def get_next_transition_spec(self, transition_spec):
        if self._path is None:
            return
        for index, cur_transition_spec in enumerate(self._path):
            if cur_transition_spec is transition_spec:
                next_index = index + 1
                if next_index < len(self._path):
                    return self._path[next_index]

    def cleanup_path_spec(self, sim):
        transition_specs = self.transition_specs
        if transition_specs is None:
            return
        cleanup_portal_costs = not services.current_zone().is_zone_shutting_down
        for transition_spec in transition_specs:
            if transition_spec.created_posture_state is not None:
                for aspect in transition_spec.created_posture_state.aspects:
                    if aspect not in sim.posture_state.aspects:
                        aspect.reset()

                transition_spec.created_posture_state = None
            else:
                if transition_spec.path is not None:
                    transition_spec.path.remove_intended_location_from_quadtree()
                portal_obj = transition_spec.portal_obj
                if cleanup_portal_costs:
                    if portal_obj is not None and sim not in portal_obj.get_users():
                        portal_obj.clear_portal_cost_override((transition_spec.portal_id), sim=sim)
            for interaction, _ in transition_spec.transition_interactions(sim):
                if interaction is not None and interaction not in sim.queue and interaction not in sim.si_state:
                    interaction.release_liabilities()

    def insert_transition_specs_at_index(self, i, new_specs):
        self._path[i:i] = new_specs

    def combine(self, *path_specs):
        full_path = self._path
        cost = self.cost
        final_constraint = self.final_constraint
        spec_constraint = self.spec_constraint
        is_failure_path = False
        for path_spec in path_specs:
            if not path_spec._path:
                raise AssertionError('Trying to combine two paths when one of them is None!')
            else:
                if full_path[-1].posture_spec != path_spec._path[0].posture_spec:
                    raise AssertionError("Trying to combine two paths that don't have a common node on the ends {} != {}.\nThis may be caused by handles being generated for complete paths.".format(self.path[-1], path_spec.path[0]))
                if full_path[-1].mobile and path_spec._path[0].path is not None:
                    full_path = list(itertools.chain(full_path, path_spec._path))
                else:
                    if full_path[-1].locked_params:
                        path_spec._path[0].locked_params = full_path[-1].locked_params
                    if full_path[-1].portal_obj:
                        path_spec._path[0].portal_obj = full_path[-1].portal_obj
                        path_spec._path[0].portal_id = full_path[-1].portal_id
                    if full_path[-1].path is not None:
                        path_spec._path[0].path = full_path[-1].path
                full_path = list(itertools.chain(full_path[:-1], path_spec._path))
            cost = cost + path_spec.cost
            final_constraint = path_spec.final_constraint
            spec_constraint = path_spec.spec_constraint
            is_failure_path = is_failure_path or path_spec.is_failure_path

        return PathSpec(full_path, cost, None, (path_spec.destination_spec), final_constraint,
          spec_constraint, path_as_posture_specs=False, is_failure_path=is_failure_path)

    def get_carry_sim_merged_path_spec(self):
        if not any((n.body.target is not None and n.body.target.is_sim for n in self.path)):
            return self
        other_index = None
        for index, node in enumerate(self.path):
            node_target = node.body.target
            if node_target is None:
                continue
            for _other_index, other_node in enumerate(self.path[index + 1:]):
                if node == other_node:
                    other_index = _other_index + index + 1
                    break

            if other_index:
                break

        if other_index:
            full_path = self._path[:index] + self._path[other_index:]
            return PathSpec(full_path, (self.cost), (self.var_map), (self.destination_spec), (self.final_constraint), (self.spec_constraint),
              path_as_posture_specs=False, is_failure_path=(self._is_failure_path), failed_path_type=(self._failed_path_type))
        return self

    def get_stand_to_carry_sim_direct_path_spec(self):
        if self is EMPTY_PATH_SPEC or self.path[0].body.posture_type is not SIM_DEFAULT_POSTURE_TYPE:
            return self
        sim_stand_posture_index = 0
        sim_carried_posture_index = 0
        sim_carried_posture_type = PostureTuning.SIM_CARRIED_POSTURE
        for index, node in enumerate(self.path):
            node_posture_type = node.body.posture_type
            if node_posture_type is SIM_DEFAULT_POSTURE_TYPE:
                sim_stand_posture_index = index
            elif node_posture_type is sim_carried_posture_type:
                sim_carried_posture_index = index
                break

        if sim_carried_posture_index - sim_stand_posture_index > 1:
            full_path = self._path[:1] + self._path[sim_carried_posture_index:]
            return PathSpec(full_path, (self.cost), (self.var_map), (self.destination_spec), (self.final_constraint), (self.spec_constraint),
              path_as_posture_specs=False, is_failure_path=(self._is_failure_path), failed_path_type=(self._failed_path_type))
        return self

    def edge_exists(self, spec_a_type, spec_b_type):
        for cur_spec, next_spec in zip(self.path, self.path[1:]):
            cur_spec_type = cur_spec.body.posture_type
            next_spec_type = next_spec.body.posture_type
            if cur_spec_type == spec_a_type and next_spec_type == spec_b_type:
                return True

        return False

    def get_failure_reason_and_object_id(self):
        if self._path is not None:
            for trans_spec in self._path:
                if trans_spec.path is not None and trans_spec.path.is_route_fail():
                    return (
                     trans_spec.path.nodes.plan_failure_path_type,
                     trans_spec.path.nodes.plan_failure_object_id)

        return (None, None)

    def create_route_nodes(self, path, portal_obj=None, portal_id=None):
        final_node = self._path[-1]
        if not final_node.mobile:
            raise ValueError('PathSpec: Trying to turn a non-mobile node into a route: {}'.format(self._path))
        else:
            if portal_obj is None:
                posture_specs = (
                 final_node.posture_spec,)
            else:
                posture_spec_enter, posture_spec_exit = portal_obj.get_posture_change(portal_id, final_node.posture_spec)
                if posture_spec_enter is posture_spec_exit:
                    posture_specs = (posture_spec_enter,)
                else:
                    posture_specs = (
                     posture_spec_enter, posture_spec_exit)
            if len(posture_specs) == 1:
                new_transition_spec = TransitionSpecCython_create(self, posture_specs[0], final_node.var_map, SequenceId.DEFAULT, portal_obj, portal_id)
            else:
                new_transition_spec = TransitionSpecCython_create(self, posture_specs[0], final_node.var_map)
            new_transition_spec.set_path(path, None)
            prev_posture_type = cython.cast(TransitionSpecCython, self._path[-1]).posture_spec.body.posture_type
            next_posture_type = new_transition_spec.posture_spec.body.posture_type
            return prev_posture_type.is_available_transition(next_posture_type) or False
        self._path.append(new_transition_spec)
        for posture_spec in posture_specs[1:]:
            new_transition_spec = TransitionSpecCython_create(self, posture_spec, final_node.var_map, SequenceId.DEFAULT, portal_obj, portal_id)
            self._path.append(new_transition_spec)

        return True

    def attach_route_and_params(self, path, locked_params, final_constraint, reverse=False):
        if reverse:
            sequence = reversed(self._path)
        else:
            sequence = self._path
        previous_spec = None
        route_spec = None
        locked_param_spec = None
        carry_spec = None
        for transition_spec in sequence:
            if not transition_spec.posture_spec.body.posture_type.unconstrained:
                if route_spec is None:
                    route_spec = previous_spec if previous_spec is not None else transition_spec
                else:
                    if reverse:
                        if previous_spec is not None:
                            locked_param_spec = previous_spec
                        else:
                            locked_param_spec = transition_spec
                        break
                    elif carry_spec is None and transition_spec.is_carry:
                        carry_spec = transition_spec
                    if route_spec is None and not reverse:
                        if transition_spec.posture_spec.body.target is not None:
                            route_spec = previous_spec if previous_spec is not None else transition_spec
                        else:
                            if previous_spec is not None:
                                if (previous_spec.posture_spec.carry.target is not None) != (transition_spec.posture_spec.carry.target is not None):
                                    route_spec = previous_spec
                previous_spec = transition_spec

        if locked_param_spec is None:
            locked_param_spec = transition_spec
        if route_spec is None:
            route_spec = transition_spec
        route_spec.set_path(path, final_constraint)
        locked_param_spec.set_locked_params(locked_params)
        if carry_spec is not None:
            carry_spec.set_locked_params(locked_params)

    def adjust_route_for_sim_inventory(self):
        spec_to_destination = None
        spec_for_pick_up_route = None
        for transition_spec in reversed(self._path):
            if transition_spec.path is not None:
                if transition_spec.path.portal_obj is not None:
                    return
                    if spec_to_destination is None:
                        spec_to_destination = transition_spec
                else:
                    spec_for_pick_up_route = transition_spec
                    break

        if spec_to_destination is not None:
            if spec_for_pick_up_route is not None:
                if spec_to_destination.path.length_squared() > 0:
                    spec_to_destination.transfer_route_to(spec_for_pick_up_route)

    def unlock_portals(self, sim):
        if self._path is not None:
            for transition_spec in self._path:
                portal_obj = transition_spec.portal_obj
                if portal_obj is not None:
                    portal_obj.clear_portal_cost_override((transition_spec.portal_id), sim=sim)

    def finalize(self, sim):
        if self.path is not None:
            if len(self.path) > 0:
                final_destination = self.path[-1]
                final_var_map = self._path[-1].var_map
                interaction_target = final_var_map[PostureSpecVariable.INTERACTION_TARGET]
                if interaction_target is not None:
                    for path_node in self._path:
                        if PostureSpecVariable.INTERACTION_TARGET not in path_node.var_map:
                            continue
                        for obj in final_destination.get_core_objects():
                            if obj.id != interaction_target.id:
                                continue
                            new_interaction_target = interaction_target.resolve_retarget(obj)
                            path_node.var_map += {PostureSpecVariable.INTERACTION_TARGET: new_interaction_target}

                carry_target = final_var_map[PostureSpecVariable.CARRY_TARGET]
                if carry_target is not None:
                    if carry_target.is_in_sim_inventory(sim=sim):
                        self.adjust_route_for_sim_inventory()
                body_posture_target = sim.posture.target
                if body_posture_target is not None and sim.posture.mobile:
                    if self.path[0].body.target != body_posture_target:
                        start_spec = sim.posture_state.get_posture_spec(self.var_map)
                        self._path.insert(0, TransitionSpecCython_create(self, start_spec, self.var_map))

    def process_transitions(self, start_spec, get_new_sequence_fn):
        new_transitions = []
        transitions_len = len(self._path)
        prev_transition = None
        for i, transition in enumerate(self._path):
            k = i + 1
            next_transition = None
            if k < transitions_len:
                next_transition = self._path[k]
            new_sequence = get_new_sequence_fn(i, prev_transition, transition, next_transition)
            if self.validate_new_sequence(prev_transition, new_sequence, next_transition, get_new_sequence_fn, start_spec):
                if new_sequence:
                    new_transitions.extend(new_sequence)
                else:
                    new_transitions.append(transition)
                if len(new_transitions) >= 1:
                    prev_transition = new_transitions[-1]

        self._path = new_transitions

    def validate_new_sequence(self, prev_transition, new_sequence, next_transition, get_new_sequence_fn, start_spec):
        validate = services.current_zone().posture_graph_service._can_transition_between_nodes
        if new_sequence:
            if prev_transition is None:
                if not validate(start_spec, new_sequence[0].posture_spec):
                    self.handle_validate_error_msg(start_spec, new_sequence[0].posture_spec, get_new_sequence_fn, start_spec)
                    return False
        elif not validate(prev_transition.posture_spec, new_sequence[0].posture_spec):
            self.handle_validate_error_msg(prev_transition.posture_spec, new_sequence[0].posture_spec, get_new_sequence_fn, start_spec)
            return False
        if len(new_sequence) > 1:
            for curr_trans, next_trans in zip(new_sequence[0:], new_sequence[1:]):
                if not validate(curr_trans.posture_spec, next_trans.posture_spec):
                    self.handle_validate_error_msg(curr_trans.posture_spec, next_trans.posture_spec, get_new_sequence_fn, start_spec)
                    return False

        if next_transition:
            validate(new_sequence[-1].posture_spec, next_transition.posture_spec) or self.handle_validate_error_msg(new_sequence[-1].posture_spec or prev_transition.posture_spec, next_transition.posture_spec, get_new_sequence_fn, start_spec)
            return False
        else:
            if prev_transition is None:
                if next_transition:
                    if not validate(start_spec, next_transition.posture_spec):
                        self.handle_validate_error_msg(start_spec, next_transition.posture_spec, get_new_sequence_fn, start_spec)
                        return False
            if prev_transition:
                if next_transition:
                    if not validate(prev_transition.posture_spec, next_transition.posture_spec):
                        self.handle_validate_error_msg(prev_transition.posture_spec, next_transition.posture_spec, get_new_sequence_fn, start_spec)
                        return False
            return True

    def handle_validate_error_msg(self, posture_spec_a, posture_spec_b, mod_function, start_spec):
        logger.error('--- FAIL: validate_new_sequence({}) ---', mod_function.__name__)
        logger.error('Start Spec: {}', start_spec)
        logger.error('Full Path:')
        for index, posture_spec in enumerate(self.path):
            logger.error('    {}: {}', index, posture_spec)

        logger.error('Failure:', posture_spec_a, posture_spec_b)
        logger.error('    posture_spec_a: {}', posture_spec_a)
        logger.error('    posture_spec_b: {}', posture_spec_b)

    @staticmethod
    def remove_non_surface_to_surface_transitions(i, prev_transition_spec, transition_spec, next_transition_spec):
        prev_transition = prev_transition_spec.posture_spec if prev_transition_spec is not None else None
        transition = transition_spec.posture_spec
        next_transition = next_transition_spec.posture_spec if next_transition_spec is not None else None
        if next_transition is not None:
            if prev_transition is None or prev_transition.body.posture_type.mobile:
                if transition.surface.target is None:
                    if next_transition.body.posture_type.mobile:
                        if next_transition.surface.target is not None:
                            if prev_transition is None or prev_transition.carry == next_transition.carry or next_transition is None:
                                return ()
        return (
         transition_spec,)

    @staticmethod
    def remove_extra_mobile_transitions(i, prev_transition_spec, transition_spec, next_transition_spec):
        prev_transition = prev_transition_spec.posture_spec if prev_transition_spec is not None else None
        transition = transition_spec.posture_spec
        next_transition = next_transition_spec.posture_spec if next_transition_spec is not None else None
        if prev_transition is None or next_transition is None:
            return (
             transition_spec,)
        if prev_transition.carry == next_transition.carry:
            if prev_transition.surface == next_transition.surface:
                if prev_transition.body.target == next_transition.body.target:
                    if transition.body.posture_type == next_transition.body.posture_type:
                        return ()
        if prev_transition.surface.target != transition.surface.target or transition.surface.target != next_transition.surface.target:
            return (transition_spec,)
        if prev_transition.carry.target != transition.carry.target or transition.carry.target != next_transition.carry.target:
            return (transition_spec,)
        if not prev_transition.body.posture_type.mobile:
            if next_transition_spec.path is not None:
                return (
                 transition_spec,)
        if prev_transition.body.posture_type.mobile:
            if transition.body.posture_type.mobile:
                if next_transition.body.posture_type.mobile:
                    if services.current_zone().posture_graph_service._can_transition_between_nodes(prev_transition, next_transition):
                        return ()
        return (
         transition_spec,)

    def flag_slot_reservations(self):
        for prev_transition_spec, cur_transition_spec in zip(self._path, self._path[1:]):
            if prev_transition_spec.sequence_id != cur_transition_spec.sequence_id:
                continue
            else:
                if not cur_transition_spec.posture_spec.surface.target:
                    continue
                if prev_transition_spec.is_carry:
                    if not cur_transition_spec.is_carry:
                        prev_transition_spec.handle_slot_reservations = True
            if prev_transition_spec.targets_empty_slot or cur_transition_spec.targets_empty_slot:
                prev_transition_spec.handle_slot_reservations = True

    def generate_transition_interactions(self, sim, final_si, transition_success):
        if self._path is None:
            return True
            self._final_si = final_si
            transition_aops = OrderedDict()
            context = InteractionContext(sim, (InteractionContext.SOURCE_POSTURE_GRAPH),
              (final_si.priority),
              run_priority=(final_si.run_priority),
              insert_strategy=(QueueInsertStrategy.NEXT),
              must_run_next=True)
            preload_outfit_set = set()
            exit_change = sim.posture_state.body.saved_exit_clothing_change
            if exit_change is not None:
                preload_outfit_set.add(exit_change)
            posture_graph_service = services.posture_graph_service()
            for i, cur_transition_spec in enumerate((self._path[1:]), start=1):
                cur_posture_spec = cur_transition_spec.posture_spec
                outfit_change = cur_transition_spec.posture_spec.body.posture_type.outfit_change
                if outfit_change:
                    entry_change = outfit_change.get_on_entry_outfit(final_si, sim_info=(sim.sim_info))
                    if entry_change is not None:
                        preload_outfit_set.add(entry_change)
                portal_obj = cur_transition_spec.portal_obj
                if portal_obj is not None:
                    portal_id = cur_transition_spec.portal_id
                    portal_entry_outfit = portal_obj.get_on_entry_outfit(final_si, portal_id, sim_info=(sim.sim_info))
                    if portal_entry_outfit is not None:
                        preload_outfit_set.add(portal_entry_outfit)
                    portal_exit_outfit = portal_obj.get_on_exit_outfit(final_si, portal_id, sim_info=(sim.sim_info))
                    if portal_exit_outfit is not None:
                        preload_outfit_set.add(portal_exit_outfit)
                for prev_transition_spec in reversed(self._path[:i]):
                    if prev_transition_spec.sequence_id == cur_transition_spec.sequence_id:
                        prev_posture_spec = prev_transition_spec.posture_spec
                        break
                else:
                    prev_posture_spec = None

                aop_list = []
                var_map = cur_transition_spec.var_map
                edge_info = posture_graph_service.get_edge(prev_posture_spec, cur_posture_spec,
                  return_none_on_failure=True)
                aop = None
                if edge_info is not None:
                    for operation in edge_info.operations:
                        op_aop = operation.associated_aop(sim, var_map)
                        if op_aop is not None:
                            aop = op_aop

                if aop is not None:
                    aop_list.append((aop, var_map))
                transition_aops[i] = aop_list

            added_final_si = False
            for i, aops in reversed(list(transition_aops.items())):
                for aop, var_map in aops:
                    final_valid_combinables = final_si.get_combinable_interactions_with_safe_carryables()
                    existing_si_set = {final_si} if not final_valid_combinables else set(itertools.chain((final_si,), final_valid_combinables))
                    for existing_si in existing_si_set:
                        if added_final_si or aop.is_equivalent_to_interaction(existing_si):
                            si = existing_si
                            if existing_si is final_si:
                                added_final_si = True
                            break
                    else:
                        execute_result = aop.interaction_factory(context)
                        if not execute_result:
                            return False
                        si = execute_result.interaction

                    self._path[i].add_transition_interaction(sim, si, var_map)
                    si.add_preload_outfit_changes(preload_outfit_set)

                if not aops:
                    self._path[i].add_transition_interaction(sim, None, self._path[i].var_map)

            if not added_final_si:
                if transition_success:
                    self._path[-1].add_transition_interaction(sim, final_si, self._path[-1].var_map)
                    final_si.add_preload_outfit_changes(preload_outfit_set)
        else:
            current_position_on_active_lot = preload_outfit_set or services.active_lot().is_position_on_lot(sim.position)
            if current_position_on_active_lot:
                if not sim.is_outside:
                    level = sim.intended_location.routing_surface.secondary_id
                    if not sim.intended_position_on_active_lot or build_buy.is_location_outside(sim.intended_position, level):
                        sim.preload_outdoor_streetwear_change(final_si, preload_outfit_set)
        sim.set_preload_outfits(preload_outfit_set)
        return True


with reload.protected(globals()):
    EMPTY_PATH_SPEC = PathSpec(None, 0, {}, None, None, None)
    NO_CONNECTIVITY = Connectivity(EMPTY_PATH_SPEC, None, None, None)

@cython.cclass
class NodeData:
    __slots__ = ('canonical_node', 'predecessors', 'successors')

    def __init__(self, canonical_node, predecessors=(), successors=()):
        self.canonical_node = canonical_node
        self.predecessors = set(predecessors)
        self.successors = set(successors)


@cython.cfunc
@cython.exceptval(check=False)
def NodeData_create(canonical_node: PostureSpec) -> NodeData:
    res = cython.declare(NodeData, NodeData.__new__(NodeData))
    res.canonical_node = canonical_node
    res.predecessors = set()
    res.successors = set()
    return res


@cython.cclass
class PostureGraph:
    _nodes = cython.declare(dict, visibility='readonly')
    _subsets = cython.declare(object, visibility='readonly')
    _quadtrees = cython.declare(object, visibility='readonly')
    proxy_sim = cython.declare(object, visibility='public')
    cached_sim_nodes = cython.declare(object, visibility='readonly')
    cached_vehicle_nodes = cython.declare(set, visibility='readonly')
    cached_postures_to_object_ids = cython.declare(object, visibility='readonly')
    _mobile_nodes_at_none = cython.declare(set, visibility='readonly')
    _mobile_nodes_at_none_no_carry = cython.declare(set, visibility='readonly')
    _mobile_nodes_at_none_carry = cython.declare(set, visibility='readonly')

    def __init__(self):
        self._nodes = {}
        self._subsets = defaultdict(set)
        self._quadtrees = defaultdict(sims4.geometry.QuadTree)
        self.proxy_sim = None
        self.cached_sim_nodes = weakref.WeakKeyDictionary()
        self.cached_vehicle_nodes = set()
        self.cached_postures_to_object_ids = defaultdict(set)
        self._mobile_nodes_at_none = set()
        self._mobile_nodes_at_none_no_carry = set()
        self._mobile_nodes_at_none_carry = set()

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __bool__(self):
        return bool(self._nodes)

    def __contains__(self, key):
        logger.warn('Please call contains({0}) instead of [{0}] for optimal performance.', key, owner='jdimailig')
        return self.contains(key)

    def items(self):
        return self._nodes.items()

    @cython.cfunc
    @cython.inline
    @cython.exceptval(check=False)
    def get_node(self, key: PostureSpec) -> NodeData:
        key = self._get_transform_key(key)
        return self._nodes[key]

    @cython.cfunc
    @cython.inline
    def set_node(self, key: PostureSpec, value: NodeData):
        self._nodes[key] = value

    @cython.cfunc
    @cython.inline
    def contains(self, key: PostureSpec) -> cython.bint:
        key = self._get_transform_key(key)
        return key in self._nodes

    @cython.cfunc
    @cython.exceptval(check=False)
    def get(self, key: PostureSpec, default=None) -> NodeData:
        key = self._get_transform_key(key)
        if key in self._nodes:
            return self._nodes[key]
        return default

    @cython.cfunc
    @cython.exceptval(check=False)
    def _get_transform_key(self, key: PostureSpec) -> PostureSpec:
        body = key.body
        if body is not None:
            body_target = body.target
            if body_target is not None:
                if body_target.is_sim:
                    posture_type = body.posture_type
                    key = key.clone(body=(PostureAspectBody_create(posture_type, self.proxy_sim)))
        return key

    @property
    def nodes(self):
        return self._nodes.keys()

    @property
    def vehicle_nodes(self):
        return self.cached_vehicle_nodes

    def cache_global_mobile_nodes(self):
        self._mobile_nodes_at_none.update(_DEFAULT_MOBILE_NODES)
        self._mobile_nodes_at_none_no_carry.update(_MOBILE_NODES_AT_NONE)
        self._mobile_nodes_at_none_carry.update(_MOBILE_NODES_AT_NONE_CARRY)

    def setup_provided_mobile_nodes(self):
        object_manager = services.object_manager()
        for obj in object_manager.get_posture_providing_objects():
            self.add_mobile_posture_provider_nodes(obj)

    @property
    def all_mobile_nodes_at_none(self):
        return self._mobile_nodes_at_none

    @property
    def all_mobile_nodes_at_none_no_carry(self):
        return self._mobile_nodes_at_none_no_carry

    @property
    def all_mobile_nodes_at_none_carry(self):
        return self._mobile_nodes_at_none_carry

    @property
    def mobile_posture_providing_affordances(self):
        object_manager = services.object_manager()
        affordances = set()
        for obj in object_manager.get_posture_providing_objects():
            affordances.update(obj.provided_mobile_posture_affordances)

        return affordances

    @cython.cfunc
    @cython.exceptval(check=False)
    def get_canonical_node(self, node: PostureSpec) -> PostureSpec:
        node_data = self.get(node)
        if node_data is None:
            return node
        return node_data.canonical_node

    @cython.cfunc
    @cython.locals(successor=PostureSpec, predecessor=PostureSpec)
    def remove_node(self, node: PostureSpec):
        target = node.get_body_target() or node.get_surface_target()
        if target is not None:
            if target != PostureSpecVariable.ANYTHING:
                self.remove_from_quadtree(target, node)
                body_type = node.body.posture_type
                if body_type.is_vehicle:
                    self.cached_vehicle_nodes.remove(node)
        for key in get_subset_keys(node):
            if key in self._subsets:
                self._subsets[key].remove(node)
                if not self._subsets[key]:
                    del self._subsets[key]

        node_data = self.get_node(node)
        for successor in node_data.successors:
            self.get_node(successor).predecessors.remove(node)

        for predecessor in node_data.predecessors:
            self.get_node(predecessor).successors.remove(node)

        del self._nodes[node]

    def remove_from_quadtree(self, obj, node: PostureSpec):
        level = obj.level
        if level is None:
            return
        quadtree = self._quadtrees[level]
        quadtree.remove(node)

    @cython.cfunc
    def add_to_quadtree(self, obj, node: PostureSpec):
        level = obj.level
        if level is None:
            return
        bounding_box = obj.get_bounding_box()
        quadtree = self._quadtrees[level]
        quadtree.insert(node, bounding_box)

    @cython.cfunc
    def add_successor(self, node: PostureSpec, successor: PostureSpec):
        node = self.get_canonical_node(node)
        successor = self.get_canonical_node(successor)
        self._add_node(node)
        self.get_node(node).successors.add(successor)
        self._add_node(successor)
        self.get_node(successor).predecessors.add(node)

    @cython.cfunc
    def _add_node(self, node: PostureSpec):
        if self.contains(node):
            return
            self.set_node(node, NodeData_create(node))
            target = None
            body = node.body
            if body is not None:
                target = body.target
            if target is None:
                surface = node.surface
                if surface is not None:
                    target = surface.target
        elif target is not None:
            if target != PostureSpecVariable.ANYTHING:
                if not target.is_sim:
                    self.add_to_quadtree(target, node)
                    body_type = node.body.posture_type
                    if body_type.is_vehicle:
                        self.cached_vehicle_nodes.add(node)
        for key in get_subset_keys(node):
            self._subsets[key].add(node)

    @cython.ccall
    def get_successors(self, node: PostureSpec, default=DEFAULT):
        node_data = self.get(node)
        if node_data is not None:
            return node_data.successors
        if default is DEFAULT:
            raise KeyError('Node {} not in posture graph.'.format(node))
        return default

    @cython.ccall
    def get_predecessors(self, node: PostureSpec, default=DEFAULT):
        node_data = self.get(node)
        if node_data is not None:
            return node_data.predecessors
        if default is DEFAULT:
            raise KeyError('Node {} not in posture graph.'.format(node))
        return default

    @caches.cached(key=(lambda _, constraint: constraint))
    def nodes_matching_constraint_geometry(self, constraint):
        if any((sub_constraint.routing_surface is None or sub_constraint.geometry is None for sub_constraint in constraint)):
            return
        nodes = set()
        for sub_constraint in constraint:
            floor = sub_constraint.routing_surface.secondary_id
            quadtree = self._quadtrees[floor]
            for polygon in sub_constraint.geometry.polygon:
                lower_bound, upper_bound = polygon.bounds()
                bounding_box = sims4.geometry.QtRect(sims4.math.Vector2(lower_bound.x, lower_bound.z), sims4.math.Vector2(upper_bound.x, upper_bound.z))
                nodes.update(quadtree.query(bounding_box))

        nodes |= self._subsets[('body_target and slot_target', None)]
        return nodes

    def nodes_for_object_gen(self, obj):
        if obj.is_part:
            owner = obj.part_owner
            nodes = self._subsets.get(('body_target', owner), set()) | self._subsets.get(('surface_target', owner), set())
            for node in nodes:
                if node.body_target is obj or node.surface_target is obj:
                    yield node

        else:
            if obj.is_sim:
                obj = self.proxy_sim
            nodes = self._subsets.get(('body_target', obj), set()) | self._subsets.get(('surface_target', obj), set())
            yield from nodes

    def _get_nodes_internal_gen(self, nodes):
        for node in nodes:
            if node.body_target is not None and node.body_target.is_sim:
                yield from self.sim_carry_nodes_gen(node)
            else:
                yield node

    @cython.locals(spec=PostureSpec)
    def get_matching_nodes_gen--- This code section failed: ---

 L.2953         0  LOAD_GLOBAL              set
                2  CALL_FUNCTION_0       0  '0 positional arguments'
                4  STORE_FAST               'nodes'

 L.2954       6_8  SETUP_LOOP          314  'to 314'
               10  LOAD_FAST                'specs'
               12  GET_ITER         
            14_16  FOR_ITER            312  'to 312'
               18  STORE_FAST               'spec'

 L.2955        20  LOAD_FAST                'slot_types'
               22  POP_JUMP_IF_FALSE   156  'to 156'

 L.2956        24  LOAD_GLOBAL              set
               26  CALL_FUNCTION_0       0  '0 positional arguments'
               28  STORE_FAST               'spec_nodes'

 L.2960        30  SETUP_LOOP          234  'to 234'
               32  LOAD_FAST                'slot_types'
               34  GET_ITER         
               36  FOR_ITER            152  'to 152'
               38  STORE_FAST               'slot_type'

 L.2961        40  LOAD_GLOBAL              PostureAspectSurface
               42  LOAD_FAST                'spec'
               44  LOAD_METHOD              get_surface_target
               46  CALL_METHOD_0         0  '0 positional arguments'
               48  LOAD_FAST                'slot_type'
               50  LOAD_FAST                'spec'
               52  LOAD_METHOD              get_slot_target
               54  CALL_METHOD_0         0  '0 positional arguments'
               56  CALL_FUNCTION_3       3  '3 positional arguments'
               58  STORE_FAST               'surface'

 L.2962        60  LOAD_FAST                'spec'
               62  LOAD_ATTR                clone
               64  LOAD_GLOBAL              DEFAULT
               66  LOAD_GLOBAL              DEFAULT
               68  LOAD_FAST                'surface'
               70  LOAD_CONST               ('body', 'carry', 'surface')
               72  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               74  STORE_FAST               'slot_type_spec'

 L.2964        76  LOAD_GLOBAL              get_subset_keys
               78  LOAD_FAST                'slot_type_spec'
               80  CALL_FUNCTION_1       1  '1 positional argument'
               82  STORE_FAST               'keys'

 L.2965        84  LOAD_FAST                'keys'
               86  POP_JUMP_IF_TRUE     96  'to 96'

 L.2966        88  LOAD_ASSERT              AssertionError
               90  LOAD_STR                 'No keys returned for a specific slot type!'
               92  CALL_FUNCTION_1       1  '1 positional argument'
               94  RAISE_VARARGS_1       1  'exception instance'
             96_0  COME_FROM            86  '86'

 L.2968        96  LOAD_CLOSURE             'self'
               98  BUILD_TUPLE_1         1 
              100  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              102  LOAD_STR                 'PostureGraph.get_matching_nodes_gen.<locals>.<dictcomp>'
              104  MAKE_FUNCTION_8          'closure'
              106  LOAD_FAST                'keys'
              108  GET_ITER         
              110  CALL_FUNCTION_1       1  '1 positional argument'
              112  STORE_FAST               'subsets'

 L.2969       114  LOAD_GLOBAL              functools
              116  LOAD_METHOD              reduce
              118  LOAD_GLOBAL              operator
              120  LOAD_ATTR                and_
              122  LOAD_GLOBAL              sorted
              124  LOAD_FAST                'subsets'
              126  LOAD_METHOD              values
              128  CALL_METHOD_0         0  '0 positional arguments'
              130  LOAD_GLOBAL              len
              132  LOAD_CONST               ('key',)
              134  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              136  CALL_METHOD_2         2  '2 positional arguments'
              138  STORE_FAST               'intersection'

 L.2970       140  LOAD_FAST                'spec_nodes'
              142  LOAD_METHOD              update
              144  LOAD_FAST                'intersection'
              146  CALL_METHOD_1         1  '1 positional argument'
              148  POP_TOP          
              150  JUMP_BACK            36  'to 36'
              152  POP_BLOCK        
              154  JUMP_FORWARD        234  'to 234'
            156_0  COME_FROM            22  '22'

 L.2972       156  LOAD_GLOBAL              get_subset_keys
              158  LOAD_FAST                'spec'
              160  CALL_FUNCTION_1       1  '1 positional argument'
              162  STORE_FAST               'keys'

 L.2973       164  LOAD_FAST                'keys'
              166  POP_JUMP_IF_TRUE    186  'to 186'

 L.2975       168  LOAD_DEREF               'self'
              170  LOAD_METHOD              _get_nodes_internal_gen
              172  LOAD_DEREF               'self'
              174  LOAD_ATTR                nodes
              176  CALL_METHOD_1         1  '1 positional argument'
              178  GET_YIELD_FROM_ITER
              180  LOAD_CONST               None
              182  YIELD_FROM       
              184  POP_TOP          
            186_0  COME_FROM           166  '166'

 L.2977       186  LOAD_CLOSURE             'self'
              188  BUILD_TUPLE_1         1 
              190  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              192  LOAD_STR                 'PostureGraph.get_matching_nodes_gen.<locals>.<dictcomp>'
              194  MAKE_FUNCTION_8          'closure'
              196  LOAD_FAST                'keys'
              198  GET_ITER         
              200  CALL_FUNCTION_1       1  '1 positional argument'
              202  STORE_FAST               'subsets'

 L.2978       204  LOAD_GLOBAL              set
              206  LOAD_GLOBAL              functools
              208  LOAD_METHOD              reduce
              210  LOAD_GLOBAL              operator
              212  LOAD_ATTR                and_
              214  LOAD_GLOBAL              sorted
              216  LOAD_FAST                'subsets'
              218  LOAD_METHOD              values
              220  CALL_METHOD_0         0  '0 positional arguments'
              222  LOAD_GLOBAL              len
              224  LOAD_CONST               ('key',)
              226  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              228  CALL_METHOD_2         2  '2 positional arguments'
              230  CALL_FUNCTION_1       1  '1 positional argument'
              232  STORE_FAST               'spec_nodes'
            234_0  COME_FROM           154  '154'
            234_1  COME_FROM_LOOP       30  '30'

 L.2981       234  LOAD_FAST                'spec'
              236  LOAD_METHOD              get_body_target
              238  CALL_METHOD_0         0  '0 positional arguments'
              240  JUMP_IF_TRUE_OR_POP   248  'to 248'
              242  LOAD_FAST                'spec'
              244  LOAD_METHOD              get_surface_target
              246  CALL_METHOD_0         0  '0 positional arguments'
            248_0  COME_FROM           240  '240'
              248  STORE_FAST               'target'

 L.2982       250  LOAD_FAST                'target'
              252  LOAD_CONST               None
              254  LOAD_GLOBAL              PostureSpecVariable
              256  LOAD_ATTR                ANYTHING
              258  BUILD_TUPLE_2         2 
              260  COMPARE_OP               in
          262_264  POP_JUMP_IF_FALSE   300  'to 300'
              266  LOAD_FAST                'constraint'
          268_270  POP_JUMP_IF_FALSE   300  'to 300'

 L.2983       272  LOAD_DEREF               'self'
              274  LOAD_METHOD              nodes_matching_constraint_geometry
              276  LOAD_FAST                'constraint'
              278  CALL_METHOD_1         1  '1 positional argument'
              280  STORE_FAST               'quadtree_subset'

 L.2984       282  LOAD_FAST                'quadtree_subset'
              284  LOAD_CONST               None
              286  COMPARE_OP               is-not
          288_290  POP_JUMP_IF_FALSE   300  'to 300'

 L.2986       292  LOAD_FAST                'spec_nodes'
              294  LOAD_FAST                'quadtree_subset'
              296  INPLACE_AND      
              298  STORE_FAST               'spec_nodes'
            300_0  COME_FROM           288  '288'
            300_1  COME_FROM           268  '268'
            300_2  COME_FROM           262  '262'

 L.2988       300  LOAD_FAST                'nodes'
              302  LOAD_METHOD              update
              304  LOAD_FAST                'spec_nodes'
              306  CALL_METHOD_1         1  '1 positional argument'
              308  POP_TOP          
              310  JUMP_BACK            14  'to 14'
              312  POP_BLOCK        
            314_0  COME_FROM_LOOP        6  '6'

 L.2990       314  LOAD_DEREF               'self'
              316  LOAD_METHOD              _get_nodes_internal_gen
              318  LOAD_FAST                'nodes'
              320  CALL_METHOD_1         1  '1 positional argument'
              322  GET_YIELD_FROM_ITER
              324  LOAD_CONST               None
              326  YIELD_FROM       
              328  POP_TOP          

Parse error at or near `LOAD_DICTCOMP' instruction at offset 100

    def sim_carry_nodes_gen(self, carried_node):
        sim_info_manager = services.sim_info_manager()
        for sim in sim_info_manager.instanced_sims_gen():
            sim_node = self.cached_sim_nodes.get(sim)
            if sim_node is None:
                sim_node = carried_node.clone(body=(PostureAspectBody(carried_node.body_posture, sim)))
                self.cached_sim_nodes[sim] = sim_node
            yield sim_node

    def vehicle_nodes_gen(self):
        for node in self.cached_vehicle_nodes:
            yield node

    def add_mobile_posture_provider_nodes(self, new_obj):
        for mobile_posture in new_obj.provided_mobile_posture_types:
            add_nodes = False if self.cached_postures_to_object_ids[mobile_posture] else True
            if new_obj.id not in self.cached_postures_to_object_ids[mobile_posture]:
                self.cached_postures_to_object_ids[mobile_posture].add(new_obj.id)
            if add_nodes:
                mobile_node_at_none = mobile_posture.skip_route or get_origin_spec(mobile_posture)
                self._mobile_nodes_at_none.add(mobile_node_at_none)
                self._mobile_nodes_at_none_no_carry.add(mobile_node_at_none)
                if mobile_posture._supports_carry:
                    mobile_node_at_none_carry = get_origin_spec_carry(mobile_posture)
                    self._mobile_nodes_at_none.add(mobile_node_at_none_carry)
                    self._mobile_nodes_at_none_carry.add(mobile_node_at_none_carry)

    def remove_mobile_posture_provider_nodes(self, old_obj):
        for mobile_posture in old_obj.provided_mobile_posture_types:
            if old_obj.id in self.cached_postures_to_object_ids[mobile_posture]:
                self.cached_postures_to_object_ids[mobile_posture].remove(old_obj.id)
            remove_nodes = False if self.cached_postures_to_object_ids[mobile_posture] else True
            if remove_nodes:
                mobile_node_at_none = mobile_posture.skip_route or get_origin_spec(mobile_posture)
                self._mobile_nodes_at_none.remove(mobile_node_at_none)
                self._mobile_nodes_at_none_no_carry.remove(mobile_node_at_none)
                if mobile_posture._supports_carry:
                    mobile_node_at_none_carry = get_origin_spec_carry(mobile_posture)
                    self._mobile_nodes_at_none.remove(mobile_node_at_none_carry)
                    self._mobile_nodes_at_none_carry.remove(mobile_node_at_none_carry)

    def clear(self):
        self._nodes.clear()
        self._subsets.clear()
        self._quadtrees.clear()
        self.cached_vehicle_nodes.clear()
        self.cached_postures_to_object_ids.clear()
        self._mobile_nodes_at_none.clear()
        self._mobile_nodes_at_none_carry.clear()
        self._mobile_nodes_at_none_no_carry.clear()
        self.proxy_sim = None


class EdgeInfo(namedtuple('_EdgeInfo', ['operations', 'validate', 'species_to_cost_dict'])):
    __slots__ = ()

    def cost(self, species):
        if species in self.species_to_cost_dict:
            return self.species_to_cost_dict[species]
        return self.species_to_cost_dict[PostureOperation.DEFAULT_COST_KEY]


def _get_species_to_aop_tunable_mapping(*, description):
    return TunableMapping(description=description, key_type=TunableEnumEntry(description='\n            The species that this affordance is intended for.\n            ',
      tunable_type=Species,
      default=(Species.HUMAN),
      invalid_enums=(
     Species.INVALID,)),
      value_type=TunableReference(description='\n            The default interaction to push for Sims of this species.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
      pack_safe=True))


class PostureGraphService(Service):

    @staticmethod
    def _verify_tunable_callback(instance_class, tunable_name, source, value):
        for affordance in PostureGraphService.POSTURE_PROVIDING_AFFORDANCES:
            posture_type = affordance.provided_posture_type
            if posture_type.mobile and posture_type.unconstrained and affordance not in PostureGraphService.SIM_DEFAULT_AFFORDANCES:
                logger.error(' Posture Providing Affordance {} provides a\n                mobile, unconstrained, posture but is not tied to an object.\n                You likely want to add this to the Provided Mobile Posture\n                Affordances on the object this posture requires. For example,\n                Oceans and Pools provide swim and float postures.\n                ',
                  affordance, owner='rmccord')

    SIM_DEFAULT_AFFORDANCES = _get_species_to_aop_tunable_mapping(description="\n        The interactions for Sims' default postures. These interactions are used\n        to kickstart Sims; are pushed on them after resets, and are used as the\n        default cancel replacement interaction.\n        ")
    SWIM_DEFAULT_AFFORDANCES = _get_species_to_aop_tunable_mapping(description="\n        The interactions for Sims' default swimming postures. These interactions\n        are used as a Sim's default affordance while in a pool.\n        ")
    CARRIED_DEFAULT_AFFORDANCES = _get_species_to_aop_tunable_mapping(description='\n        The interactions for Sims\' default "Be Carried" postures. These\n        interactions are used whenever Sims are transitioning into such\n        postures.\n        ')
    POSTURE_PROVIDING_AFFORDANCES = TunableList(description='\n        Additional posture providing interactions that are not tuned on any\n        object. This allows us to add additional postures for sims to use.\n        Example: Kneel on floor.\n        ',
      tunable=TunableReference(description='\n            Interaction that provides a posture.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
      pack_safe=True),
      verify_tunable_callback=_verify_tunable_callback)
    INCREMENTAL_REBUILD_THRESHOLD = Tunable(description='\n        The posture graph will do a full rebuild when exiting build/buy if\n        there have been more than this number of modifications to the posture\n        graph. Otherwise, an incremental rebuild will be done, which is much\n        faster for small numbers of operations, but slower for large numbers.\n        Talk to a gameplay engineer before changing this value.\n        ',
      tunable_type=int,
      default=10)

    def __init__(self):
        self._graph = PostureGraph()
        self._edge_info = {}
        self._goal_costs = {}
        self._zone_loaded = False
        self._disable_graph_update_count = 0
        self._incremental_update_count = None
        self._mobile_posture_objects_quadtree = sims4.geometry.QuadTree()

    @property
    def has_built_for_zone_spin_up(self):
        return self._zone_loaded

    def _clear(self):
        self._graph.clear()
        self._edge_info.clear()

    def rebuild(self):
        if indexed_manager.capture_load_times:
            time_stamp = time.time()
        if self._disable_graph_update_count == 0:
            self._clear()
            self.build()
        if indexed_manager.capture_load_times:
            time_spent_rebuilding = time.time() - time_stamp
            indexed_manager.object_load_times['posture_graph'] = time_spent_rebuilding

    def disable_graph_building(self):
        self._disable_graph_update_count += 1

    def enable_graph_building(self):
        self._disable_graph_update_count -= 1

    @staticmethod
    def get_default_affordance(species):
        if species in PostureGraphService.SIM_DEFAULT_AFFORDANCES:
            return PostureGraphService.SIM_DEFAULT_AFFORDANCES[species]
        logger.warn("Requesting default affordance for {} and it doesn't exist in PostureGraphService.SIM_DEFAULT_AFFORDANCES, using human instead.", species)
        return PostureGraphService.SIM_DEFAULT_AFFORDANCES[Species.HUMAN]

    @staticmethod
    def get_default_aop(species):
        if SIM_DEFAULT_AOPS is None:
            _cache_global_sim_default_values()
        if species in SIM_DEFAULT_AOPS:
            return SIM_DEFAULT_AOPS[species]
        logger.warn("Requesting default aop for {} and it doesn't exist in PostureGraphService.SIM_DEFAULT_AOPS, using human instead.")
        return SIM_DEFAULT_AOPS[Species.HUMAN]

    @staticmethod
    def get_default_swim_affordance(species):
        if species in PostureGraphService.SWIM_DEFAULT_AFFORDANCES:
            return PostureGraphService.SWIM_DEFAULT_AFFORDANCES[species]
        logger.warn("Requesting default swim affordance for {} and it doesn't exist in PostureGraphService.SWIM_DEFAULT_AFFORDANCES, using human instead.", species)
        return PostureGraphService.SWIM_DEFAULT_AFFORDANCES[Species.HUMAN]

    @staticmethod
    def get_swim_aop(species):
        if SIM_SWIM_AOPS is None:
            _cache_global_sim_default_values()
        if species in SIM_SWIM_AOPS:
            return SIM_SWIM_AOPS[species]
        logger.warn("Requesting default swim aop for {} and it doesn't exist in PostureGraphService.SIM_SWIM_AOPS, using human instead.")
        return SIM_SWIM_AOPS[Species.HUMAN]

    def on_enter_buildbuy(self):
        self._incremental_update_count = 0

    def on_exit_buildbuy(self):
        if self._incremental_update_count is None:
            logger.warn('Posture graph incremental update count is None when exiting build/buy. This can only happen if there is a mismatch between calls to on_enter_buildbuy() and on_exit_buildbuy(). The posture graph will be rebuilt just to be cautious.', owner='bhill')
            self.rebuild()
        else:
            if self._incremental_update_count > self.INCREMENTAL_REBUILD_THRESHOLD:
                logger.info('Exiting build/buy and executing full posture graph rebuild.')
                self.rebuild()
            else:
                logger.info('Exiting build/buy and the incremental posture graph rebuild was good enough. (Only {} changes made)', self._incremental_update_count)
        self._incremental_update_count = None

    def start(self):
        self._clear()
        if SIM_DEFAULT_AOPS is None:
            _cache_global_sim_default_values()
        self.build()

    @contextmanager
    def __reload_context__(oldobj, newobj):
        try:
            yield
        finally:
            if isinstance(oldobj, PostureGraphService):
                _cache_global_sim_default_values()
                newobj._graph.cache_global_mobile_nodes()

    def on_teardown(self):
        self._zone_loaded = False
        object_manager = services.object_manager()
        object_manager.unregister_callback(CallbackTypes.ON_OBJECT_ADD, self._on_object_added)
        object_manager.unregister_callback(CallbackTypes.ON_OBJECT_REMOVE, self._on_object_deleted)

    def build_during_zone_spin_up(self):
        skip_cache = caches.skip_cache
        caches.skip_cache = False
        self._zone_loaded = True
        self.rebuild()
        object_manager = services.object_manager()
        object_manager.register_callback(CallbackTypes.ON_OBJECT_ADD, self._on_object_added)
        object_manager.register_callback(CallbackTypes.ON_OBJECT_REMOVE, self._on_object_deleted)
        caches.skip_cache = skip_cache

    def add_node(self, node: PostureSpec, operations):
        nodes = []
        next_node = node
        for operation in operations:
            nodes.append(next_node)
            next_node = operation.apply(next_node)
            if next_node is None:
                return

        if not PostureGraphService._validate_node_for_graph(next_node):
            return
        graph = cython.cast(PostureGraph, self._graph)
        if next_node in graph.get_successors(node, ()):
            return
        species_to_cost_dict = None
        validate = CallableTestList()
        for source_node, operation in zip(nodes, operations):
            if species_to_cost_dict is None:
                species_to_cost_dict = operation.cost(source_node)
            else:
                temp_cost_dict = operation.cost(source_node)
                current_default_cost = species_to_cost_dict[PostureOperation.DEFAULT_COST_KEY]
                new_default_cost = temp_cost_dict[PostureOperation.DEFAULT_COST_KEY]
                for species in species_to_cost_dict:
                    if species in temp_cost_dict:
                        species_to_cost_dict[species] += temp_cost_dict.pop(species)
                    else:
                        species_to_cost_dict[species] += new_default_cost

                for species in temp_cost_dict:
                    species_to_cost_dict[species] = current_default_cost + temp_cost_dict.pop(species)

            validate.append(operation.get_validator(source_node))

        edge_info = EdgeInfo(operations, validate, species_to_cost_dict)
        graph.add_successor(node, next_node)
        self._edge_info[(node, next_node)] = edge_info
        return next_node

    def update_generic_sim_carry_node(self, sim, from_init=False):
        if self._graph.proxy_sim is None:
            if from_init:
                if sim.is_selectable:
                    self._graph.proxy_sim = SimPostureNode(sim)
                    return True
            return False
        return True

    def _obj_triggers_posture_graph_update(self, obj):
        if obj.is_sim:
            return
        else:
            if self._disable_graph_update_count:
                return False
            return obj.is_valid_posture_graph_object or False
        if obj.parts == []:
            return False
        return True

    def on_mobile_posture_object_added_during_zone_spinup(self, new_obj):
        self._on_object_added(new_obj)

    @with_caches
    def _on_object_added(self, new_obj):
        if not new_obj.is_part:
            if not self._obj_triggers_posture_graph_update(new_obj):
                return
            if self._incremental_update_count is not None:
                self._incremental_update_count += 1
                if self._incremental_update_count > self.INCREMENTAL_REBUILD_THRESHOLD:
                    return
            objects = set()

            def add_object_to_build(obj_to_add):
                if obj_to_add.parts:
                    objects.update(obj_to_add.parts)
                else:
                    objects.add(obj_to_add)

            add_object_to_build(new_obj)
            for child in new_obj.children:
                if child.is_valid_posture_graph_object:
                    add_object_to_build(child)

            open_set = set()
            closed_set = set(self._graph.nodes)
            all_ancestors = (set().union)(*(obj.ancestry_gen() for obj in objects))
            for ancestor in all_ancestors:
                if not ancestor.parts:
                    open_set.update(self._graph.nodes_for_object_gen(ancestor))

            closed_set -= open_set
            if new_obj.is_sim:
                if self._graph.proxy_sim is None:
                    for closed_node in tuple(closed_set):
                        body_posture = closed_node.body.posture_type
                        body_target = closed_node.body.target
                        can_transition_to_carry = not body_posture.mobile or body_posture.mobile and body_target is None
                        if can_transition_to_carry and body_posture.is_available_transition(PostureTuning.SIM_CARRIED_POSTURE):
                            closed_set.discard(closed_node)

        else:
            for closed_node in tuple(closed_set):
                if closed_node.body.posture_type is PostureTuning.SIM_CARRIED_POSTURE:
                    closed_set.discard(closed_node)

        provided_posture_aops = []
        mobile_affordances_and_postures = [(affordance, affordance.provided_posture_type) for affordance in new_obj.provided_mobile_posture_affordances]
        for affordance, mobile_posture in mobile_affordances_and_postures:
            if len(self._graph.cached_postures_to_object_ids[mobile_posture]) == 1:
                provided_posture_aops.append(AffordanceObjectPair(affordance, None, affordance, None))

        if provided_posture_aops:
            body_operations_dict = PostureGraphService.get_body_operation_dict(provided_posture_aops)
            for source_posture_type, destination_posture_type in Posture._posture_transitions:
                body_operation = body_operations_dict.get(destination_posture_type)
                if body_operation is None:
                    continue
                if source_posture_type is not SIM_DEFAULT_POSTURE_TYPE:
                    if source_posture_type not in body_operations_dict:
                        continue
                    new_node = self.add_node(get_origin_spec(source_posture_type), (body_operation,))
                    if new_node is not None:
                        open_set.add(new_node)
                    if source_posture_type._supports_carry:
                        new_node = self.add_node(get_origin_spec_carry(source_posture_type), (body_operation,))
                        if new_node is not None:
                            open_set.add(new_node)

        for node, obj in itertools.product(self._graph.all_mobile_nodes_at_none, objects):
            ops = []
            self._expand_and_append_node_object(node, obj, ops)
            for operations in ops:
                new_node = self.add_node(node, operations)
                if new_node is not None and new_node not in closed_set:
                    open_set.add(new_node)

        with _object_addition(new_obj):
            self._build(open_set, closed_set)

    def get_proxied_sim(self):
        if self._graph.proxy_sim is None:
            return
        return self._graph.proxy_sim.sim_proxied

    @with_caches
    def _on_object_deleted(self, obj):
        if not self._obj_triggers_posture_graph_update(obj):
            return
        else:
            if not obj.remove_children_from_posture_graph_on_delete:
                return
            if self._incremental_update_count is not None:
                self._incremental_update_count += 1
                if self._incremental_update_count > self.INCREMENTAL_REBUILD_THRESHOLD:
                    return
        graph = cython.cast(PostureGraph, self._graph)
        for node in graph.nodes_for_object_gen(obj):
            for successor in graph.get_successors(node, ()):
                self._edge_info.pop((node, successor), None)

            for predecessor in graph.get_predecessors(node, ()):
                self._edge_info.pop((predecessor, node), None)

            graph.remove_node(node)

        for mobile_posture in obj.provided_mobile_posture_types:
            if len(graph.cached_postures_to_object_ids[mobile_posture]) == 1:
                mobile_node_at_none = get_origin_spec(mobile_posture)
                graph.remove_node(mobile_node_at_none)
                if mobile_posture._supports_carry:
                    mobile_node_at_none_carry = get_origin_spec_carry(mobile_posture)
                    graph.remove_node(mobile_node_at_none_carry)

    @contextmanager
    @with_caches
    def object_moving(self, obj):
        if not self._zone_loaded or obj.is_sim:
            yield
            return
        if obj.routing_component is not None:
            if obj.routing_component.is_moving:
                sims = obj.get_users(sims_only=True)
                for sim in sims:
                    posture_state = sim.posture_state
                    if posture_state is not None and posture_state.body.target is obj:
                        posture_state.body.invalidate_slot_constraints()

                yield
                return
        if obj.is_valid_posture_graph_object:
            self._on_object_deleted(obj)
        try:
            yield
        finally:
            if obj.is_valid_posture_graph_object:
                self._on_object_added(obj)

    def _expand_node(self, node: PostureSpec):
        ops = []
        for obj in node.get_relevant_objects():
            if not obj.is_valid_posture_graph_object:
                continue
            if obj.is_sim:
                self._expand_and_append_node_sim(node, obj, ops)
            else:
                self._expand_and_append_node_object(node, obj, ops)
            if obj.is_part and obj.routing_surface.type == SurfaceType.SURFACETYPE_OBJECT and obj.part_owner.provided_routing_surface is not None:
                for mobile_posture_operation in obj.part_owner.provided_mobile_posture_operations:
                    ops.append((mobile_posture_operation,))

        ops.append((SIM_DEFAULT_OPERATION,))
        if node.body_posture.supports_swim:
            ops.append((SIM_SWIM_OPERATION,))
        if node.surface is not None:
            ops.append((PostureOperation.FORGET_SURFACE_OP, SIM_DEFAULT_OPERATION))
            if node.body.posture_type.mobile:
                ops.append((PostureOperation.FORGET_SURFACE_OP,))
        if node.body.posture_type._supports_carry:
            ops.append((PostureOperation.STANDARD_PICK_UP_OP,))
        return ops

    @staticmethod
    def get_body_operation_dict(posture_aops):
        body_operations_dict = {}
        for aop in posture_aops:
            body_operation = aop.get_provided_posture_change()
            if body_operation is None:
                continue
            body_op_posture_type = body_operation.posture_type
            if body_op_posture_type in body_operations_dict:
                for species, aop in body_operation.all_associated_aops_gen():
                    body_operations_dict[body_op_posture_type].add_associated_aop(species, aop)

            else:
                body_operations_dict[body_operation.posture_type] = body_operation

        return body_operations_dict

    @caches.cached(maxsize=None)
    def _expand_object_surface(self, obj, surface):
        ops = []
        if surface is not None:
            put_down = PostureOperation.PutDownObjectOnSurface(PostureSpecVariable.POSTURE_TYPE_CARRY_NOTHING, surface, PostureSpecVariable.SLOT, PostureSpecVariable.CARRY_TARGET)
            ops.append((put_down,))
            surface_ops = self._expand_surface(surface)
            ops.extend(surface_ops)
        posture_aops = obj.get_posture_aops_gen()
        if obj.is_part:
            posture_aops = filter(obj.supports_affordance, posture_aops)
        body_operations_dict = self.get_body_operation_dict(posture_aops)
        for body_operation in body_operations_dict.values():
            if not obj.parts or body_operation.posture_type.unconstrained:
                ops.append((body_operation,))
                if surface is not None:
                    ops.extend(((body_operation,) + ops for ops in surface_ops))

        if obj.inventory_component is not None:
            at_surface = PostureOperation.TargetAlreadyInSlot(None, obj, None)
            ops.append((at_surface,))
        return ops

    def _expand_and_append_node_object(self, node, obj, out_ops):
        surface = None
        if obj.is_surface():
            surface = obj
        else:
            parent = obj.parent
            if parent is not None:
                if parent.is_surface():
                    surface = parent
            else:
                out_ops.extend(self._expand_object_surface(obj, surface))
                if surface is not obj:
                    return
                if node.body_target not in (None, obj):
                    return
                species_to_affordances = enumdict(Species)
                species_to_disallowed_ages = defaultdict(set)
                for species, affordance in self.SIM_DEFAULT_AFFORDANCES.items():
                    if obj.is_part:
                        if not obj.supports_posture_type(affordance.provided_posture_type):
                            continue
                    species_to_affordances[species] = AffordanceObjectPair(affordance, obj, affordance, None)
                    species_to_disallowed_ages[species] = event_testing.test_utils.get_disallowed_ages(affordance)

                return species_to_affordances or None
            body_operation = PostureOperation.BodyTransition(SIM_DEFAULT_POSTURE_TYPE,
              species_to_affordances,
              target=obj,
              disallowed_ages=species_to_disallowed_ages)
            out_ops.append((body_operation,))

    def _expand_and_append_node_sim(self, node, obj, out_ops):
        logger.assert_log(obj.is_sim, '_expand_and_append_node_sim can only be called with a Sim object')
        species_to_affordances = enumdict(Species)
        species_to_disallowed_ages = defaultdict(set)
        for species, affordance in self.CARRIED_DEFAULT_AFFORDANCES.items():
            if not obj.supports_posture_type(affordance.provided_posture_type):
                continue
            species_to_affordances[species] = AffordanceObjectPair(affordance, obj, affordance, None)
            species_to_disallowed_ages[species] = event_testing.test_utils.get_disallowed_ages(affordance)

        if not species_to_affordances:
            return
        else:
            if obj.age not in species_to_disallowed_ages[obj.species]:
                return
            return self.update_generic_sim_carry_node(obj, from_init=True) or None
        body_operation = PostureOperation.BodyTransition((PostureTuning.SIM_CARRIED_POSTURE), species_to_affordances,
          target=(self._graph.proxy_sim),
          disallowed_ages=species_to_disallowed_ages)
        out_ops.append((body_operation,))

    def _expand_surface(self, surface):
        ops = []
        existing_carryable_slotted_target = PostureOperation.TargetAlreadyInSlot(PostureSpecVariable.CARRY_TARGET, surface, PostureSpecVariable.SLOT)
        ops.append((existing_carryable_slotted_target,))
        existing_noncarryable_slotted_target = PostureOperation.TargetAlreadyInSlot(PostureSpecVariable.SLOT_TARGET, surface, PostureSpecVariable.SLOT)
        ops.append((existing_noncarryable_slotted_target,))
        empty_surface = PostureOperation.TargetAlreadyInSlot(None, surface, PostureSpecVariable.SLOT)
        ops.append((empty_surface,))
        at_surface = PostureOperation.TargetAlreadyInSlot(None, surface, None)
        ops.append((at_surface,))
        forget_surface = PostureOperation.FORGET_SURFACE_OP
        ops.append((forget_surface,))
        return ops

    def _validate_node_for_graph(node):
        target = node.body.target
        if target is not None:
            if not node.body.posture_type.mobile:
                surface = node.surface
                if surface is None or surface.target is None:
                    target_parent = target.parent
                    if target_parent is not None:
                        if not target.is_set_as_head:
                            parent_slot = target.parent_slot
                            if parent_slot:
                                if parent_slot.slot_types:
                                    if target.slot_type_set:
                                        possible_slot_types = parent_slot.slot_types.intersection(target.slot_type_set.slot_types)
                                        if not any((slot_type.implies_slotted_object_has_surface for slot_type in possible_slot_types)):
                                            return True
                            return False
                    if target_parent is None and target.is_surface():
                        return False
                elif surface is not None:
                    target_parent = target.parent
                    if target_parent:
                        if surface.target == target_parent:
                            parent_slot = target.parent_slot
                            if not ((parent_slot is None or parent_slot).slot_types and target.slot_type_set):
                                return False
                            possible_slot_types = parent_slot.slot_types.intersection(target.slot_type_set.slot_types)
                            if not any((slot_type.implies_slotted_object_has_surface for slot_type in possible_slot_types)):
                                return False
        return True

    _validate_node_for_graph = staticmethod(caches.cached(maxsize=4096)(_validate_node_for_graph))

    def _build(self, open_set, closed_set):
        while open_set:
            node = open_set.pop()
            closed_set.add(node)
            for operations in self._expand_node(node):
                new_node = self.add_node(node, operations)
                if new_node is not None and new_node not in closed_set:
                    open_set.add(new_node)

        caches.clear_all_caches()

    @with_caches
    def build(self):
        open_set = set(STAND_AT_NONE_NODES)
        closed_set = set()
        self._graph.cache_global_mobile_nodes()
        self._graph.setup_provided_mobile_nodes()
        self._edge_info[(STAND_AT_NONE, STAND_AT_NONE)] = EdgeInfo((SIM_DEFAULT_OPERATION,), (lambda *_, **__: True), 0)
        provided_posture_aops = [AffordanceObjectPair(affordance, None, affordance, None) for affordance in self.POSTURE_PROVIDING_AFFORDANCES]
        mobile_affordances = self._graph.mobile_posture_providing_affordances
        provided_posture_aops.extend([AffordanceObjectPair(affordance, None, affordance, None) for affordance in mobile_affordances])
        body_operations_dict = PostureGraphService.get_body_operation_dict(provided_posture_aops)
        for source_posture_type, destination_posture_type in Posture._posture_transitions:
            body_operation = body_operations_dict.get(destination_posture_type)
            if body_operation is None:
                continue
            if source_posture_type is not SIM_DEFAULT_POSTURE_TYPE:
                if source_posture_type not in body_operations_dict:
                    continue
            new_node = self.add_node(get_origin_spec(source_posture_type), (body_operation,))
            if new_node is not None:
                open_set.add(new_node)
            if source_posture_type._supports_carry:
                new_node = self.add_node(get_origin_spec_carry(source_posture_type), (body_operation,))
                if new_node is not None:
                    open_set.add(new_node)

        self._build(open_set, closed_set)

    def nodes_matching_constraint_geometry(self, constraint):
        return self._graph.nodes_matching_constraint_geometry(constraint)

    @property
    def all_mobile_nodes_at_none_no_carry(self):
        return self._graph.all_mobile_nodes_at_none_no_carry

    @property
    def all_mobile_nodes_at_none_carry(self):
        return self._graph.all_mobile_nodes_at_none_carry

    @property
    def all_mobile_nodes_at_none(self):
        return self._graph.all_mobile_nodes_at_none

    @property
    def mobile_posture_providing_affordances(self):
        return self._graph.mobile_posture_providing_affordances

    def add_mobile_posture_provider(self, obj):
        self._graph.add_mobile_posture_provider_nodes(obj)

    def remove_mobile_posture_provider(self, obj):
        self._graph.remove_mobile_posture_provider_nodes(obj)

    def distance_fn(self, sim, var_map, interaction, curr_node, next_node):
        if isinstance(curr_node, _MobileNode):
            curr_node = curr_node.graph_node
        elif isinstance(next_node, _MobileNode):
            next_node = next_node.graph_node
        else:
            if curr_node == next_node:
                return 0
                cost = 0
                next_body = next_node.body
                next_body_posture = next_node.body_posture
                next_body_target = next_body.target
                if gsi_handlers.posture_graph_handlers.archiver.enabled:
                    cost_str_list = []
                if next_body_target is not None:
                    if next_body_target.is_sim:
                        guaranteed_si_count = sum((1 for _ in next_body_target.si_state.all_guaranteed_si_gen()))
                        if guaranteed_si_count:
                            cost += guaranteed_si_count * PostureScoring.CARRYING_SIM_BUSY_PENALTY
                            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                                cost_str_list.append('CARRYING_SIM_BUSY_PENALTY: {}'.format(PostureScoring.CARRYING_SIM_BUSY_PENALTY))
                        relationship_tracker = next_body_target.relationship_tracker
                        if not relationship_tracker.has_bit(sim.sim_id, RelationshipGlobalTuning.CAREGIVER_RELATIONSHIP_BIT):
                            cost += PostureScoring.CARRYING_SIM_NON_CAREGIVER_PENALTY
                            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                                cost_str_list.append('CARRYING_SIM_NON_CAREGIVER_PENALTY: {}'.format(PostureScoring.CARRYING_SIM_NON_CAREGIVER_PENALTY))
                        if not relationship_tracker.has_bit(sim.sim_id, RelationshipGlobalTuning.HAS_MET_RELATIONSHIP_BIT):
                            cost += PostureScoring.CARRYING_SIM_HAS_NOT_MET_PENALTY
                            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                                cost_str_list.append('CARRYING_SIM_HAS_NOT_MET_PENALTY: {}'.format(PostureScoring.CARRYING_SIM_HAS_NOT_MET_PENALTY))
            else:
                may_reserve_posture_target(sim, next_body_posture, next_body_target) or cost += PostureScoring.OBJECT_RESERVED_PENALTY
            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                cost_str_list.append('OBJECT_RESERVED_PENALTY: {}'.format(PostureScoring.OBJECT_RESERVED_PENALTY))
        edge_info, _ = self._get_edge_info(curr_node, next_node)
        edge_cost = edge_info.cost(sim.species)
        cost += edge_cost
        if gsi_handlers.posture_graph_handlers.archiver.enabled:
            for operation in edge_info.operations:
                cost_str_list.append('OpCost({}): {}'.format(type(operation).__name__, edge_cost))
                operation_cost_str_list = operation.debug_cost_str_list
                if operation_cost_str_list is not None:
                    for operation_cost_str in operation_cost_str_list:
                        cost_str_list.append('\t' + operation_cost_str)

            cost_str_list.insert(0, 'Score: {}'.format(cost))
            logger.debug('Score: {}, curr_node: {}, next_node: {}', cost, curr_node, next_node)
            gsi_handlers.posture_graph_handlers.log_path_cost(sim, curr_node, next_node, cost_str_list)
        return cost

    def _get_edge_info(self, node, successor):
        original_node_body_target = None
        original_successor_body_target = None
        if node.body_target is not None:
            if node.body_target.is_sim:
                original_node_body_target = node.body_target
                node = node.clone(body=(PostureAspectBody(PostureTuning.SIM_CARRIED_POSTURE, self._graph.proxy_sim)))
        if successor.body_target is not None:
            if successor.body_target.is_sim:
                original_successor_body_target = successor.body_target
                successor = successor.clone(body=(PostureAspectBody(PostureTuning.SIM_CARRIED_POSTURE, self._graph.proxy_sim)))
        edge_info = self._edge_info[(node, successor)]
        if original_successor_body_target is not None:
            for operation in edge_info.operations:
                operation.set_target(original_successor_body_target)

        return (
         edge_info, original_node_body_target)

    def _adjacent_nodes_gen(self, sim, get_successors_fn, valid_edge_test, constraint, var_map, node, *, allow_pickups, allow_putdowns, allow_carried, reverse_path):
        if isinstance(node, _MobileNode):
            node = node.graph_node
        else:
            is_mobile_at_none = node.body_posture.mobile and node.body_target is None and node.surface_target is None
            is_routing_vehicle = False
            if not reverse_path:
                if node.body_posture.is_vehicle:
                    for sub_constraint in constraint:
                        if sub_constraint.posture_state_spec is None:
                            continue
                        posture_specs = [posture_spec for posture_spec, var_map in sub_constraint.posture_state_spec.get_posture_specs_gen() if posture_spec.body.posture_type == node.body.posture_type]
                        for spec in posture_specs:
                            if spec.body.target in PostureSpecVariable or node.body.target is spec.body.target:
                                is_routing_vehicle = True
                                break

            skip_adjacent = is_mobile_at_none or is_routing_vehicle
            if node.body_posture.mobile:
                if node.body_posture.skip_route:
                    skip_adjacent = False
            if not allow_carried:
                if skip_adjacent:
                    return

        def _edge_validation(forward_nodes, successor_node):
            if valid_edge_test is not None:
                if not valid_edge_test(*forward_nodes):
                    return
            else:
                edge_info, node_body_target = (self._get_edge_info)(*forward_nodes)
                if not edge_info.validate(sim, var_map, original_body_target=node_body_target):
                    return
                if successor_node.body_target is not None and successor_node.body_target.is_disabled():
                    return
            if successor_node.body_posture.mobile:
                return _MobileNode(successor_node, node)
            return successor_node

        for successor in get_successors_fn(node):
            body_target = successor.body_target
            if skip_adjacent:
                if not (body_target is None or body_target.is_sim):
                    continue
            forward_nodes = (successor, node) if reverse_path else (node, successor)
            first, second = forward_nodes
            if (allow_pickups or first.carry_target) is None:
                if second.carry_target is not None:
                    continue
            if (allow_putdowns or first.carry_target) is not None:
                if second.carry_target is None:
                    continue
                if body_target is not None and body_target.is_sim:
                    for carry_succesor in self._graph.sim_carry_nodes_gen(successor):
                        if node.body_target is carry_succesor.body_target:
                            continue
                        carry_forward_nodes = (carry_succesor, node) if reverse_path else (node, carry_succesor)
                        first_carry, second_carry = carry_forward_nodes
                        if not allow_pickups:
                            if first_carry.carry_target is None:
                                if second_carry.carry_target is not None:
                                    continue
                        if (allow_putdowns or first_carry.carry_target) is not None:
                            if second_carry.carry_target is None:
                                continue
                            return_node = _edge_validation(carry_forward_nodes, carry_succesor)
                            if return_node is not None:
                                yield return_node

            else:
                return_node = _edge_validation(forward_nodes, successor)
                if return_node is not None:
                    yield return_node

    @staticmethod
    def _get_destination_locations_for_estimate(route_target, mobile_node):
        locations = route_target.get_position_and_routing_surface_for_posture(mobile_node)
        return locations

    def get_vehicle_destination_target(self, source, destinations):
        if source.body_target is None:
            return
        destination_body_target = None
        for dest in destinations:
            if not dest.body_posture.is_vehicle:
                return
                if destination_body_target is not None:
                    if destination_body_target != dest.body_target:
                        return
                destination_body_target = dest.body_target

        if destination_body_target is not None:
            if source.body_target.id == destination_body_target.id:
                return destination_body_target

    def _left_path_gen(self, sim, source, destinations, interaction, constraint, var_map, valid_edge_test, is_complete):
        carry_target = var_map.get(PostureSpecVariable.CARRY_TARGET)
        allow_carried = False
        sim_routing_context = sim.get_routing_context()
        if is_complete:
            if source.body.posture_type.mobile:
                if source.surface.target is None:
                    if not source.body.posture_type.is_vehicle:
                        if all((dest.body.target != source.body.target for dest in destinations)):
                            return
            else:
                search_destinations = set(destinations) - self._graph.all_mobile_nodes_at_none
                return search_destinations or None
        else:
            if carry_target is sim:
                destination_body = PostureAspectBody(PostureTuning.SIM_CARRIED_POSTURE, interaction.sim)
                destination_surface = PostureAspectSurface(None, None, None)
                search_destinations = {source.clone(body=destination_body, surface=destination_surface)}
                allow_carried = True
            else:
                search_destinations = set(STAND_AT_NONE_NODES)
                if sim.is_human:
                    search_destinations.update(self._graph.all_mobile_nodes_at_none_no_carry)
                    if source.body_posture.is_vehicle:
                        if source in destinations:
                            search_destinations.update(self._graph.vehicle_nodes)
                        else:
                            vehicle_destination_target = self.get_vehicle_destination_target(source, destinations)
                            if vehicle_destination_target is not None:
                                search_destinations.update(self._graph.nodes_for_object_gen(vehicle_destination_target))
                    else:
                        search_destinations.update(self._graph.all_mobile_nodes_at_none)
                else:
                    distance_fn = functools.partial(self.distance_fn, sim, var_map, interaction)
                    allow_pickups = False
                    if is_complete:
                        if carry_target is not None:
                            if carry_target.definition is not carry_target:
                                if carry_target.is_in_sim_inventory(sim=sim):
                                    allow_pickups = True
                                else:
                                    if carry_target.parent is not None:
                                        if carry_target.parent.is_same_object_or_part(sim.posture_state.surface_target) or carry_target.parent.is_same_object_or_part(sim):
                                            allow_pickups = True
                                if carry_target.routing_surface is not None:
                                    sim_constraint = interactions.constraints.Transform((sim.intended_transform), routing_surface=(sim.intended_routing_surface))
                                    carry_constraint = carry_target.get_carry_transition_constraint(sim, (carry_target.position), (carry_target.routing_surface), mobile=False)
                                    if sim_constraint.intersect(carry_constraint).valid:
                                        if carry_target.parent is not None:
                                            ignored_objects = (
                                             sim.posture_state.body_target, sim.posture_state.surface_target)
                                        else:
                                            ignored_objects = (
                                             sim.posture_state.body_target,)
                                        result, _ = carry_target.check_line_of_sight((sim.intended_transform), additional_ignored_objects=ignored_objects, for_carryable=True)
                                        if result:
                                            allow_pickups = True
                allow_putdowns = allow_pickups
                adjacent_nodes_gen = functools.partial((self._adjacent_nodes_gen),
                  sim, (self._graph.get_successors), valid_edge_test, constraint, var_map,
                  reverse_path=False, allow_pickups=allow_pickups, allow_putdowns=allow_putdowns, allow_carried=allow_carried)

                def left_distance_fn(curr_node, next_node):
                    if isinstance(curr_node, _MobileNode):
                        curr_node = curr_node.graph_node
                    if isinstance(next_node, _MobileNode):
                        next_node = next_node.graph_node
                    if next_node is None:
                        if curr_node in destinations:
                            return self._get_goal_cost(sim, interaction, constraint, var_map, curr_node)
                        return 0.0
                    return distance_fn(curr_node, next_node)

                def heuristic_fn_left(node):
                    is_mobile_node = isinstance(node, _MobileNode)
                    if is_mobile_node:
                        graph_node = node.graph_node
                        node = node.prev
                        heuristic = 0
                    else:
                        graph_node = node
                        heuristic = postures.posture_specs.PostureOperation.COST_STANDARD
                    if node.body_target is None or node.body_posture.is_vehicle:
                        return 0
                    if is_mobile_node:
                        if node.body_target.is_sim:
                            return 0
                    else:
                        locations = node.body_target.get_locations_for_posture(graph_node)
                        source_locations = ((source_location.transform.translation, source_location.routing_surface if source_location.routing_surface is not None else node.body_target.routing_surface) for source_location in locations)
                        destination_locations = []
                        carry_target = var_map[PostureSpecVariable.CARRY_TARGET]
                        if carry_target is None or carry_target.definition is carry_target:
                            needs_constraint_dests = False
                            for dest in destinations:
                                if dest.body_target is not None:
                                    destination_locations += self._get_destination_locations_for_estimate(dest.body_target, graph_node)
                                elif dest.surface_target is not None:
                                    destination_locations += self._get_destination_locations_for_estimate(dest.surface_target, graph_node)
                                else:
                                    needs_constraint_dests = True

                            if needs_constraint_dests and any((sub_constraint.geometry for sub_constraint in constraint)):
                                for sub_constraint in constraint:
                                    if not sub_constraint.geometry is None:
                                        if sub_constraint.routing_surface is None:
                                            continue
                                        for polygon in sub_constraint.geometry.polygon:
                                            for polygon_corner in polygon:
                                                destination_locations.append((polygon_corner, sub_constraint.routing_surface))

                        elif carry_target.is_in_inventory():
                            inv = carry_target.get_inventory()
                            if inv.owner is not None:
                                if inv.owner.is_sim:
                                    return heuristic
                            for owner in inv.owning_objects_gen():
                                destination_locations += self._get_destination_locations_for_estimate(owner, graph_node)

                        else:
                            destination_locations += self._get_destination_locations_for_estimate(carry_target, graph_node)
                    heuristic += primitives.routing_utils.estimate_distance_between_multiple_points(source_locations, destination_locations, sim_routing_context)
                    if gsi_handlers.posture_graph_handlers.archiver.enabled:
                        gsi_handlers.posture_graph_handlers.add_heuristic_fn_score(sim, 'left', node, graph_node, heuristic)
                    return heuristic

                paths = _shortest_path_gen(sim, (source,), search_destinations, adjacent_nodes_gen, left_distance_fn, heuristic_fn_left)
                for path in paths:
                    path = algos.Path(list(path), path.cost - left_distance_fn(path[-1], None))
                    yield path

    def clear_goal_costs(self):
        self._get_goal_cost.cache.clear()

    @caches.cached
    def _get_goal_cost(self, sim, interaction, constraint, var_map, dest):
        cost = self._goal_costs.get(dest, 0.0)
        node_target = dest.body_target
        if node_target is not None:
            if not dest.body.posture_type.is_vehicle:
                cost += constraint.constraint_cost(node_target.position, node_target.orientation)
        else:
            if not any((c.cost for c in constraint)):
                return cost
            if interaction.is_putdown:
                if not constraint.valid:
                    return cu.MAX_FLOAT
                if dest.surface_target is None or getattr(constraint, 'geometry', None):
                    cost += constraint.cost
                return cost
            participant_type = interaction.get_participant_type(sim)
            animation_resolver_fn = interaction.get_constraint_resolver(None)
            _, routing_data = self._get_locations_from_posture(sim,
              dest, var_map, interaction=interaction, participant_type=participant_type, animation_resolver_fn=animation_resolver_fn,
              final_constraint=constraint)
            final_constraint = routing_data[0]
            if final_constraint is None:
                final_constraint = constraint
            return final_constraint.valid or cu.MAX_FLOAT
        cost += final_constraint.cost
        return cost

    def _right_path_gen--- This code section failed: ---

 L.4563         0  LOAD_GLOBAL              functools
                2  LOAD_ATTR                partial

 L.4564         4  LOAD_DEREF               'self'
                6  LOAD_ATTR                _adjacent_nodes_gen
                8  LOAD_DEREF               'sim'
               10  LOAD_DEREF               'self'
               12  LOAD_ATTR                _graph
               14  LOAD_ATTR                get_predecessors
               16  LOAD_FAST                'valid_edge_test'
               18  LOAD_DEREF               'constraint'

 L.4565        20  LOAD_DEREF               'var_map'
               22  LOAD_CONST               True
               24  LOAD_CONST               False
               26  LOAD_CONST               True
               28  LOAD_FAST                'allow_carried'
               30  LOAD_CONST               ('reverse_path', 'allow_pickups', 'allow_putdowns', 'allow_carried')
               32  CALL_FUNCTION_KW_10    10  '10 total positional and keyword args'
               34  STORE_FAST               'adjacent_nodes_gen'

 L.4567        36  LOAD_CLOSURE             'interaction'
               38  LOAD_CLOSURE             'self'
               40  LOAD_CLOSURE             'sim'
               42  LOAD_CLOSURE             'var_map'
               44  BUILD_TUPLE_4         4 
               46  LOAD_CODE                <code_object reversed_distance_fn>
               48  LOAD_STR                 'PostureGraphService._right_path_gen.<locals>.reversed_distance_fn'
               50  MAKE_FUNCTION_8          'closure'
               52  STORE_FAST               'reversed_distance_fn'

 L.4572        54  LOAD_CLOSURE             'constraint'
               56  LOAD_CLOSURE             'interaction'
               58  LOAD_CLOSURE             'self'
               60  LOAD_CLOSURE             'sim'
               62  LOAD_CLOSURE             'var_map'
               64  BUILD_TUPLE_5         5 
               66  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               68  LOAD_STR                 'PostureGraphService._right_path_gen.<locals>.<dictcomp>'
               70  MAKE_FUNCTION_8          'closure'

 L.4573        72  LOAD_DEREF               'destinations'
               74  GET_ITER         
               76  CALL_FUNCTION_1       1  '1 positional argument'
               78  STORE_FAST               'weighted_sources'

 L.4576        80  SETUP_LOOP          140  'to 140'
               82  LOAD_GLOBAL              reversed
               84  LOAD_DEREF               'path_left'
               86  CALL_FUNCTION_1       1  '1 positional argument'
               88  GET_ITER         
             90_0  COME_FROM           118  '118'
             90_1  COME_FROM            98  '98'
               90  FOR_ITER            132  'to 132'
               92  STORE_FAST               'node'

 L.4577        94  LOAD_FAST                'node'
               96  LOAD_ATTR                body_target
               98  POP_JUMP_IF_FALSE    90  'to 90'

 L.4580       100  LOAD_FAST                'node'
              102  LOAD_ATTR                body_target
              104  LOAD_METHOD              get_locations_for_posture
              106  LOAD_DEREF               'path_left'
              108  LOAD_CONST               -1
              110  BINARY_SUBSCR    
              112  CALL_METHOD_1         1  '1 positional argument'
              114  STORE_FAST               'locations'

 L.4581       116  LOAD_FAST                'locations'
              118  POP_JUMP_IF_FALSE    90  'to 90'

 L.4582       120  LOAD_FAST                'locations'
              122  LOAD_CONST               0
              124  BINARY_SUBSCR    
              126  STORE_DEREF              'sim_location'

 L.4583       128  BREAK_LOOP       
              130  JUMP_BACK            90  'to 90'
              132  POP_BLOCK        

 L.4585       134  LOAD_DEREF               'sim'
              136  LOAD_ATTR                routing_location
              138  STORE_DEREF              'sim_location'
            140_0  COME_FROM_LOOP       80  '80'

 L.4587       140  LOAD_DEREF               'sim'
              142  LOAD_METHOD              get_routing_context
              144  CALL_METHOD_0         0  '0 positional arguments'
              146  STORE_DEREF              'sim_routing_context'

 L.4589       148  LOAD_GLOBAL              BarebonesCache
              150  LOAD_CLOSURE             'constraint'
              152  LOAD_CLOSURE             'destinations'
              154  LOAD_CLOSURE             'distance_estimator'
              156  LOAD_CLOSURE             'interaction'
              158  LOAD_CLOSURE             'path_left'
              160  LOAD_CLOSURE             'self'
              162  LOAD_CLOSURE             'sim'
              164  LOAD_CLOSURE             'sim_location'
              166  LOAD_CLOSURE             'sim_routing_context'
              168  BUILD_TUPLE_9         9 
              170  LOAD_CODE                <code_object heuristic_fn_right>
              172  LOAD_STR                 'PostureGraphService._right_path_gen.<locals>.heuristic_fn_right'
              174  MAKE_FUNCTION_8          'closure'
              176  CALL_FUNCTION_1       1  '1 positional argument'
              178  STORE_FAST               'heuristic_fn_right'

 L.4675       180  LOAD_GLOBAL              gsi_handlers
              182  LOAD_ATTR                posture_graph_handlers
              184  LOAD_ATTR                archiver
              186  LOAD_ATTR                enabled
              188  POP_JUMP_IF_FALSE   206  'to 206'

 L.4676       190  LOAD_GLOBAL              gsi_handlers
              192  LOAD_ATTR                posture_graph_handlers
              194  LOAD_METHOD              log_shortest_path_cost
              196  LOAD_DEREF               'sim'
              198  LOAD_FAST                'weighted_sources'
              200  LOAD_FAST                'heuristic_fn_right'
              202  CALL_METHOD_3         3  '3 positional arguments'
              204  POP_TOP          
            206_0  COME_FROM           188  '188'

 L.4678       206  LOAD_GLOBAL              _shortest_path_gen
              208  LOAD_DEREF               'sim'

 L.4679       210  LOAD_FAST                'weighted_sources'
              212  LOAD_GLOBAL              set
              214  LOAD_FAST                'left_destinations'
              216  CALL_FUNCTION_1       1  '1 positional argument'
              218  LOAD_FAST                'adjacent_nodes_gen'

 L.4680       220  LOAD_FAST                'reversed_distance_fn'
              222  LOAD_FAST                'heuristic_fn_right'
              224  CALL_FUNCTION_6       6  '6 positional arguments'
              226  STORE_FAST               'paths_reversed'

 L.4681       228  SETUP_LOOP          266  'to 266'
              230  LOAD_FAST                'paths_reversed'
              232  GET_ITER         
              234  FOR_ITER            264  'to 264'
              236  STORE_FAST               'path'

 L.4682       238  LOAD_GLOBAL              algos
              240  LOAD_METHOD              Path
              242  LOAD_GLOBAL              reversed
              244  LOAD_FAST                'path'
              246  CALL_FUNCTION_1       1  '1 positional argument'
              248  LOAD_FAST                'path'
              250  LOAD_ATTR                cost
              252  CALL_METHOD_2         2  '2 positional arguments'
              254  STORE_FAST               'path'

 L.4683       256  LOAD_FAST                'path'
              258  YIELD_VALUE      
              260  POP_TOP          
              262  JUMP_BACK           234  'to 234'
              264  POP_BLOCK        
            266_0  COME_FROM_LOOP      228  '228'

Parse error at or near `LOAD_DICTCOMP' instruction at offset 66

    def _middle_path_gen(self, path_left, path_right, sim, interaction, distance_estimator, var_map):
        if path_left[-1].carry == path_right[0].carry:
            yield
            return
            carry_target = var_map[PostureSpecVariable.CARRY_TARGET]
            if carry_target is None:
                raise ValueError('Interaction requires a carried object in its animation but has no carry_target: {} {}', interaction, var_map)
            if isinstance(carry_target, Definition):
                return
            pickup_cost = PostureOperation.PickUpObject.get_pickup_cost(path_left[-1])
            if carry_target.is_sim:
                surface_target = carry_target.posture_state.surface_target
                if surface_target is not None:
                    pickup_path = self.get_pickup_path(surface_target, interaction)
                    pickup_path.cost += pickup_cost
                    yield pickup_path
                    return
                else:
                    parent_slot = carry_target.parent_slot
                    if parent_slot is not None:
                        if parent_slot.owner is not sim:
                            if parent_slot.owner.is_sim:
                                return []
                            surface_target = parent_slot.owner
                            if not surface_target.is_surface():
                                raise ValueError('Cannot pick up an object: {} from an invalid surface: {}'.format(carry_target, surface_target))
                            pickup_path = self.get_pickup_path(surface_target, interaction)
                            pickup_path.cost += pickup_cost
                            yield pickup_path
                            return
                carry_target_inventory = carry_target.get_inventory()
                if carry_target_inventory is None or carry_target.is_in_sim_inventory():
                    carry_routing_surface = carry_target.routing_surface
                    if carry_routing_surface is not None and carry_routing_surface.type == routing.SurfaceType.SURFACETYPE_POOL:
                        yield algos.Path([SWIM_AT_NONE, SWIM_AT_NONE_CARRY], pickup_cost)
            else:
                yield algos.Path([STAND_AT_NONE, STAND_AT_NONE_CARRY], pickup_cost)
        else:
            return
            if interaction is not None:
                obj_with_inventory = interaction.object_with_inventory
                if obj_with_inventory is not None:
                    if not obj_with_inventory.can_access_for_pickup(sim):
                        return
                    pickup_path = self.get_pickup_path(obj_with_inventory, interaction)
                    pickup_path.cost += pickup_cost
                    yield pickup_path
                    return
            inv_objects = list(carry_target_inventory.owning_objects_gen())
            inv_objects or logger.warn('Attempt to plan a middle path for an inventory with no owning objects: {} on interaction: {}', carry_target_inventory,
              interaction, owner='bhill')
            return
        for node in path_right:
            if not node.body_target:
                if node.surface_target:
                    pass
                right_target = node.body_target or node.surface_target
                break
        else:
            right_target = None

        def inv_owner_dist(owner):
            routing_position, _ = Constraint.get_validated_routing_position(owner)
            routing_location = routing.Location(routing_position, orientation=(owner.orientation),
              routing_surface=(owner.routing_surface))
            dist = distance_estimator.estimate_distance((sim.location, routing_location))
            dist += distance_estimator.get_preferred_object_cost(owner)
            if right_target:
                right_target_position, _ = Constraint.get_validated_routing_position(right_target)
                right_target_location = routing.Location(right_target_position, orientation=(right_target.orientation),
                  routing_surface=(right_target.routing_surface))
                dist += distance_estimator.estimate_distance((routing_location, right_target_location))
            return dist

        inv_objects.sort(key=inv_owner_dist)
        for inv_object in inv_objects:
            if not inv_object.can_access_for_pickup(sim):
                continue
            pickup_path = self.get_pickup_path(inv_object, interaction)
            pickup_path.cost += pickup_cost
            yield pickup_path

    def _get_all_paths(self, sim, source, destinations, var_map, constraint, valid_edge_test, interaction=None, allow_complete=True):
        distance_estimator = DistanceEstimator(self, sim, interaction, constraint)
        segmented_paths = []
        stand_path = SegmentedPath(self,
          sim, source, destinations, var_map, constraint, valid_edge_test,
          interaction, is_complete=False, distance_estimator=distance_estimator)
        segmented_paths.append(stand_path)
        if allow_complete:
            complete = SegmentedPath(self,
              sim, source, destinations, var_map, constraint, valid_edge_test,
              interaction, is_complete=True, distance_estimator=distance_estimator)
            segmented_paths.append(complete)
        return segmented_paths

    def get_pickup_path(self, surface_target, interaction):
        cost_pickup = 0
        path_pickup = [STAND_AT_NONE]
        sequence_pickup = get_pick_up_spec_sequence(STAND_AT_NONE, surface_target)
        path_pickup.extend(sequence_pickup)
        path_pickup.append(STAND_AT_NONE_CARRY)
        if interaction is not None:
            preferred_objects = interaction.preferred_objects
            cost_pickup += postures.posture_scoring.PostureScoring.get_preferred_object_cost((
             surface_target,), preferred_objects)
        return algos.Path(path_pickup, cost_pickup)

    def any_template_passes_destination_test(self, templates, si, sim, node):
        if not node.body_posture._supports_carry:
            return False
        for template in templates.values():
            for dest_spec, var_map in template:
                if postures.posture_specs.destination_test(sim, node, (dest_spec,), var_map, None, si):
                    return True

        return False

    def get_segmented_paths(self, sim, posture_dest_list, additional_template_list, interaction, participant_type, valid_destination_test, valid_edge_test, preferences, final_constraint, included_sis):
        possible_destinations = []
        all_segmented_paths = []
        self._goal_costs.clear()
        if gsi_handlers.posture_graph_handlers.archiver.enabled:
            gsi_templates = [(ds, vm, c) for c, value in posture_dest_list.items() for ds, vm in iter(value)]
            gsi_handlers.posture_graph_handlers.add_templates_to_gsi(sim, gsi_templates)
        guaranteed_sis = list(sim.si_state.all_guaranteed_si_gen(interaction.priority, interaction.group_id))
        excluded_objects = interaction.excluded_posture_destination_objects()
        interaction_sims = set(interaction.get_participants(ParticipantType.AllSims))
        interaction_sims.discard(interaction.sim)
        relationship_bonuses = None
        if interaction.use_relationship_bonuses:
            relationship_bonuses = PostureScoring.build_relationship_bonuses(sim, (interaction.sim_affinity_posture_scoring_data),
              (interaction.sim_affinity_use_current_position_for_none),
              sims_to_consider=interaction_sims)
        main_group = sim.get_main_group()
        if main_group is not None and main_group.constraint_initialized:
            group_constraint = main_group.is_solo or main_group.get_constraint(sim)
        else:
            group_constraint = None
        found_destination_node = False
        for constraint, templates in posture_dest_list.items():
            destination_nodes = {}
            var_map_all = DEFAULT
            destination_specs = set()
            slot_types = set()
            for destination_spec, var_map in templates:
                destination_specs.add(destination_spec)
                slot = var_map.get(PostureSpecVariable.SLOT)
                if slot is not None:
                    slot_types.update(slot.slot_types)
                if var_map_all is DEFAULT:
                    var_map_all = var_map
                if gsi_handlers.posture_graph_handlers.archiver.enabled:
                    possible_destinations.append(destination_spec)

            slot_all = var_map_all.get(PostureSpecVariable.SLOT)
            if slot_all is not None:
                new_slot_manifest = slot_all.with_overrides(slot=(frozenset(slot_types)))
                var_map_all = frozendict(var_map_all, {PostureSpecVariable.SLOT: new_slot_manifest})
            source_spec = cython.declare(PostureSpec, sim.posture_state.get_posture_spec(var_map_all))
            if source_spec is None:
                continue
            if source_spec.body_posture.mobile:
                if source_spec.body_posture.unconstrained:
                    if source_spec.body_target is not None and not source_spec.body_target.is_part:
                        if source_spec.body_target.parts:
                            new_body = PostureAspectBody(source_spec.body_posture, None)
                            new_surface = PostureAspectSurface(None, None, None)
                            source_spec = source_spec.clone(body=new_body, carry=DEFAULT, surface=new_surface)
            graph = cython.declare(PostureGraph, self._graph)
            if not graph.contains(source_spec):
                if services.current_zone().is_zone_shutting_down:
                    return []
                    raise AssertionError('Source spec not in the posture graph: {} for interaction: {}'.format(source_spec, interaction))
                else:
                    source_node = source_spec
                    if gsi_handlers.posture_graph_handlers.archiver.enabled:
                        gsi_handlers.posture_graph_handlers.add_source_or_dest(sim, (source_spec,), var_map_all, 'source', source_node)
                    distance_estimator = DistanceEstimator(self, sim, interaction, constraint)
                    same_mobile_body_target = source_node.body_posture.mobile
                    if same_mobile_body_target:
                        if source_node.body_target is not None and source_node.body_target.is_part:
                            adjacent_source_parts = source_node.body_target.adjacent_parts_gen()
                        else:
                            adjacent_source_parts = ()
                    body_target_node_distances = None
                    matching_node_constraint = constraint if interaction.is_putdown else final_constraint
                    for node in graph.get_matching_nodes_gen(destination_specs, slot_types,
                      constraint=matching_node_constraint):
                        if node.get_core_objects() & excluded_objects:
                            continue
                        elif not destination_test(sim, node, destination_specs, var_map_all, valid_destination_test, interaction):
                            continue
                        else:
                            if included_sis and node.body.target is not None:
                                if any((not node.body.target.supports_affordance(si.affordance) for si in included_sis)):
                                    continue
                                if interaction.context.source == InteractionContext.SOURCE_AUTONOMY and interaction.autonomy_preference is not None and node.body_target is not None:
                                    preference_target = node.body_target
                                    if preference_target.is_part:
                                        if not preference_target.restrict_autonomy_preference:
                                            preference_target = preference_target.part_owner
                                    preference_type = sim.get_autonomy_preference_type(interaction.autonomy_preference.preference.tag, preference_target, False)
                                    if preference_type == AutonomyPreferenceType.DISALLOWED:
                                        continue
                            elif same_mobile_body_target:
                                if node.body.target is not None:
                                    if node.body.target is not source_node.body_target and node.body.target not in adjacent_source_parts:
                                        same_mobile_body_target = False
                            if interaction.is_putdown:
                                obj = node.body_target
                                if obj is not None:
                                    if obj.is_part:
                                        obj = obj.part_owner
                                    valid, distance = interaction.evaluate_putdown_distance(obj, distance_estimator)
                                    if not valid:
                                        continue
                                    if distance is not None:
                                        if body_target_node_distances is None:
                                            body_target_node_distances = {}
                                        body_target_node_distances[node] = distance
                        if additional_template_list and not interaction.is_putdown:
                            compatible = True
                            for carry_si, additional_templates in additional_template_list.items():
                                if carry_si not in guaranteed_sis:
                                    continue
                                compatible = self.any_template_passes_destination_test(additional_templates, carry_si, sim, node)
                                if compatible:
                                    break

                            if not compatible:
                                continue
                            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                                gsi_handlers.posture_graph_handlers.add_source_or_dest(sim, destination_specs, var_map_all, 'destination', node)
                            destination_nodes[node] = destination_specs

                    if interaction.is_putdown:
                        if body_target_node_distances is not None:
                            nodes_to_remove = interaction.get_distant_nodes_to_remove(body_target_node_distances)
                            if nodes_to_remove:
                                for distant_node in nodes_to_remove:
                                    del destination_nodes[distant_node]

                    if destination_nodes:
                        found_destination_node = True
                    else:
                        logger.debug('No destination_nodes found for destination_specs: {}', destination_specs)
                        continue
                    PostureScoring.build_destination_costs(self._goal_costs, destination_nodes, sim, interaction, var_map_all, preferences, included_sis, additional_template_list, relationship_bonuses, constraint, group_constraint)
                    allow_complete = not source_node.body_posture.mobile or same_mobile_body_target
                    if allow_complete:
                        if source_node.body_target is None:
                            current_constraint = constraints.Transform((sim.transform), routing_surface=(sim.routing_surface))
                            intersection = current_constraint.intersect(constraint)
                            if not intersection.valid:
                                allow_complete = False
                    interaction_outfit_changes = interaction.get_tuned_outfit_changes(include_exit_changes=False)
                    if interaction_outfit_changes:
                        for outfit_change in interaction_outfit_changes:
                            if not sim.sim_info.is_wearing_outfit(outfit_change):
                                allow_complete = False

                    is_sim_carry = _is_sim_carry(interaction, sim)
                    if allow_complete:
                        source_body_target = source_node.body_target
                        if is_sim_carry:
                            complete_destinations = destination_nodes
                        else:
                            if source_body_target is None:
                                complete_destinations = [dest_node for dest_node in destination_nodes if dest_node.body_target is None]
                            else:
                                if source_body_target.is_part:
                                    source_body_target = source_body_target.part_owner
                                complete_destinations = [dest_node for dest_node in destination_nodes if source_body_target.is_same_object_or_part(dest_node.body_target)]
                        if not is_sim_carry:
                            for dest_node in complete_destinations:
                                outfit_change = dest_node.body.posture_type.outfit_change
                                if outfit_change:
                                    entry_change_outfit = outfit_change.get_on_entry_outfit(interaction, sim_info=(sim.sim_info))
                                    if entry_change_outfit is not None:
                                        if not sim.sim_info.is_wearing_outfit(entry_change_outfit):
                                            continue
                                allow_complete = True
                                break
                            else:
                                allow_complete = False

                segmented_paths = self._get_all_paths(sim,
                  source_node, destination_nodes, var_map_all, constraint, valid_edge_test,
                  interaction=interaction, allow_complete=allow_complete)
                all_segmented_paths.extend(segmented_paths)

        if self._goal_costs:
            lowest_goal_cost = min(self._goal_costs.values())
            for goal_node, cost in self._goal_costs.items():
                self._goal_costs[goal_node] = cost - lowest_goal_cost

        elif not all_segmented_paths:
            if not found_destination_node:
                set_transition_failure_reason(sim, (TransitionFailureReasons.NO_DESTINATION_NODE), transition_controller=(interaction.transition))
            else:
                set_transition_failure_reason(sim, (TransitionFailureReasons.NO_PATH_FOUND), transition_controller=(interaction.transition))
        return all_segmented_paths

    def handle_additional_pickups_and_putdowns(self, best_path_spec, additional_template_list, sim, can_defer_putdown=True):
        included_sis = set()
        return best_path_spec.transition_specs and additional_template_list or included_sis
        best_transition_specs = best_path_spec.transition_specs
        final_transition_spec = best_transition_specs[-1]
        final_node = final_transition_spec.posture_spec
        final_var_map = final_transition_spec.var_map
        final_hand = final_var_map[PostureSpecVariable.HAND]
        final_spec_constraint = best_path_spec.spec_constraint
        final_carry_target = final_var_map[PostureSpecVariable.CARRY_TARGET]
        slot_manifest_entry = final_var_map.get(PostureSpecVariable.SLOT)
        additional_template_added = False
        for carry_si, additional_templates in additional_template_list.items():
            carry_si_carryable = carry_si.carry_target
            if carry_si_carryable is None:
                if carry_si.target is not None:
                    if carry_si.target.carryable_component is not None:
                        carry_si_carryable = carry_si.target
            if carry_si_carryable is final_carry_target:
                included_sis.add(carry_si)
                additional_template_added = True
                continue
            valid_additional_intersection = False
            for destination_spec_additional, var_map_additional, constraint_additional in [(ds, vm, c) for c, value in additional_templates.items() for ds, vm in iter(value)]:
                additional_hand = var_map_additional[PostureSpecVariable.HAND]
                if final_hand == additional_hand:
                    continue
                if additional_template_added:
                    continue
                valid_destination = destination_test(sim, final_node, (destination_spec_additional,), var_map_additional, None, carry_si)
                valid_intersection = constraint_additional.intersect(final_spec_constraint).valid
                if not valid_intersection:
                    continue
                valid_additional_intersection = True
                if not valid_destination:
                    continue
                carry_target = var_map_additional[PostureSpecVariable.CARRY_TARGET]
                container = carry_target.parent
                if final_node.surface.target is container:
                    included_sis.add(carry_si)
                    continue
                additional_slot_manifest_entry = var_map_additional.get(PostureSpecVariable.SLOT)
                if additional_slot_manifest_entry is not None:
                    if slot_manifest_entry is not None:
                        if slot_manifest_entry.slot_types.intersection(additional_slot_manifest_entry.slot_types):
                            continue
                if container is not sim:
                    insertion_index = 0
                    fallback_insertion_index_and_spec = None
                    original_spec = best_transition_specs[0].posture_spec
                    if original_spec.surface.target is container:
                        fallback_insertion_index_and_spec = InsertionIndexAndSpec(insertion_index, original_spec)
                    for prev_transition_spec, transition_spec in zip(best_transition_specs, best_transition_specs[1:]):
                        insertion_index += 1
                        if transition_spec.sequence_id != prev_transition_spec.sequence_id:
                            continue
                        spec = transition_spec.posture_spec
                        if fallback_insertion_index_and_spec is None:
                            if spec.surface.target is container:
                                fallback_insertion_index_and_spec = InsertionIndexAndSpec(insertion_index, spec)
                            if prev_transition_spec.posture_spec.carry.target is None:
                                if spec.carry.target is not None:
                                    if spec.surface.target is not container:
                                        continue
                                break
                    else:
                        if fallback_insertion_index_and_spec is not None:
                            insertion_index = fallback_insertion_index_and_spec.index
                            spec = fallback_insertion_index_and_spec.spec
                        else:
                            continue
                        pick_up_sequence = get_pick_up_spec_sequence(spec,
                          container,
                          body_target=(spec.body.target))
                        slot_var_map = {PostureSpecVariable.SLOT: SlotManifestEntry(carry_target, container, carry_target.parent_slot)}
                        var_map_additional_updated = frozendict(var_map_additional, slot_var_map)
                        new_specs = []
                        for pick_up_spec in pick_up_sequence:
                            new_specs.append(TransitionSpecCython_create(best_path_spec, pick_up_spec, var_map_additional_updated,
                              sequence_id=(SequenceId.PICKUP)))

                        best_path_spec.insert_transition_specs_at_index(insertion_index, new_specs)
                final_surface_target = final_node.surface.target if final_node.surface is not None else None
                if final_surface_target is not None:
                    if PostureSpecVariable.SLOT in var_map_additional:
                        _slot_manifest_entry = var_map_additional[PostureSpecVariable.SLOT]
                        overrides = {}
                        if isinstance(_slot_manifest_entry.target, PostureSpecVariable):
                            overrides['target'] = final_surface_target
                        else:
                            interaction_target = final_var_map[PostureSpecVariable.INTERACTION_TARGET]
                            if interaction_target is not None:
                                relative_position = interaction_target.position
                            else:
                                relative_position = final_surface_target.position
                        chosen_slot = self._get_best_slot(final_surface_target, _slot_manifest_entry.slot_types, carry_target, relative_position)
                        if chosen_slot is None:
                            continue
                        overrides['slot'] = chosen_slot
                        _slot_manifest_entry = (_slot_manifest_entry.with_overrides)(**overrides)
                        slot_var_map = {PostureSpecVariable.SLOT: _slot_manifest_entry}
                        var_map_additional = frozendict(var_map_additional, slot_var_map)
                if additional_slot_manifest_entry is not None:
                    insertion_index = 0
                    fallback_insertion_index_and_spec = None
                    original_spec = best_transition_specs[0].posture_spec
                    if original_spec.surface.target is slot_manifest_entry.actor.parent:
                        fallback_insertion_index_and_spec = InsertionIndexAndSpec(insertion_index, original_spec)
                    for prev_transition_spec, transition_spec in zip(best_transition_specs, best_transition_specs[1:]):
                        insertion_index += 1
                        if transition_spec.sequence_id != prev_transition_spec.sequence_id:
                            continue
                        spec = transition_spec.posture_spec
                        if fallback_insertion_index_and_spec is None:
                            if spec.surface.target is slot_manifest_entry.actor.parent:
                                fallback_insertion_index_and_spec = InsertionIndexAndSpec(insertion_index, spec)
                            if prev_transition_spec.posture_spec.carry.target is not None and spec.carry.target is None:
                                break
                    else:
                        if fallback_insertion_index_and_spec is not None:
                            insertion_index = fallback_insertion_index_and_spec.index
                            spec = fallback_insertion_index_and_spec.spec
                        else:
                            continue
                        put_down_sequence = get_put_down_spec_sequence((spec.body.posture_type),
                          (spec.surface.target),
                          body_target=(spec.body.target))
                        new_specs = []
                        for put_down_spec in put_down_sequence:
                            new_specs.append(TransitionSpecCython_create(best_path_spec, put_down_spec, var_map_additional,
                              sequence_id=(SequenceId.PUTDOWN)))

                        best_path_spec.insert_transition_specs_at_index(insertion_index + 1, new_specs)

                    included_sis.add(carry_si)
                    additional_template_added = True
                    break
            else:
                if valid_additional_intersection or can_defer_putdown:
                    if carry_si_carryable.carryable_component.defer_putdown:
                        sim.transition_controller.has_deferred_putdown = True
                carry_si.cancel((FinishingType.TRANSITION_FAILURE), cancel_reason_msg='Posture Graph. No valid intersections for additional constraint.')

        return included_sis

    @staticmethod
    def is_valid_complete_path(sim, path, interaction):
        for posture_spec in path:
            target = posture_spec.body.target
            if target is not None:
                if target is interaction.target:
                    reservation_handler = interaction.get_interaction_reservation_handler(sim=sim)
                    if reservation_handler is None or reservation_handler.may_reserve():
                        continue
                    else:
                        reservation_handler = interaction.get_interaction_reservation_handler(sim=sim, target=target)
                        if reservation_handler is None or reservation_handler.may_reserve():
                            continue
                    can_remove, _, _ = can_remove_blocking_sims(sim, interaction, (target,))
                    if can_remove:
                        continue
                    if target.usable_by_transition_controller(sim.queue.transition_controller):
                        continue
                return False

        return True

    def get_sim_position_routing_data(self, sim):
        if sim.parent is not None:
            if sim.parent.is_sim or sim.posture_state.body.is_vehicle:
                return self.get_sim_position_routing_data(sim.parent)
        sim_position_constraint = interactions.constraints.Transform((sim.intended_transform),
          routing_surface=(sim.intended_routing_surface),
          debug_name='SimCurrentPosition')
        return (sim_position_constraint, None, None)

    @staticmethod
    def _get_new_goal_error_info():
        if False:
            if gsi_handlers.posture_graph_handlers.archiver.enabled:
                return []

    @staticmethod
    def _goal_failure_set(goals):
        return set([goal.failure_reason.name for goal in goals])

    @staticmethod
    def append_handles(sim, handle_dict, invalid_handle_dict, invalid_los_dict, routing_data, target_path, var_map, dest_spec, cur_path_id, final_constraint, entry=True, path_type=PathType.LEFT, goal_height_limit=None, perform_los_check=True):
        routing_constraint, locked_params, target = routing_data
        if routing_constraint is None:
            return
        carry_target = var_map.get(PostureSpecVariable.CARRY_TARGET)
        for_carryable = carry_target is not None
        reference_pt, top_level_parent = Constraint.get_los_reference_point(target, is_carry_target=(target is carry_target))
        if path_type == PathType.RIGHT:
            if target is carry_target:
                goal_height_limit = None
                if top_level_parent is not sim:
                    reference_pt, top_level_parent = (None, None)
        if not perform_los_check:
            reference_pt = None
        blocking_obj_id = None
        if sim.routing_master is not None and sim.routing_master.get_routing_slave_data_count(FormationRoutingType.FOLLOW):
            target_reference_override = sim.routing_master
            goal_height_limit = FormationTuning.GOAL_HEIGHT_LIMIT
        else:
            target_reference_override = None
        for sub_constraint in routing_constraint:
            if not sub_constraint.valid:
                continue
            elif sub_constraint.routing_surface is not None:
                routing_surface = sub_constraint.routing_surface
            else:
                if target is not None:
                    routing_surface = target.routing_surface
                else:
                    routing_surface = None
            connectivity_handles = sub_constraint.get_connectivity_handles(sim=sim,
              routing_surface_override=routing_surface,
              locked_params=locked_params,
              los_reference_point=reference_pt,
              entry=entry,
              target=target)
            for connectivity_handle in connectivity_handles:
                connectivity_handle.path = target_path
                connectivity_handle.var_map = var_map
                existing_data = handle_dict.get(connectivity_handle)
                if existing_data is not None:
                    if target_path.cost >= existing_data[1]:
                        continue
                if connectivity_handle.los_reference_point is None or test_point_in_compound_polygon(connectivity_handle.los_reference_point, connectivity_handle.geometry.polygon):
                    single_goal_only = True
                else:
                    single_goal_only = False
                for_source = path_type == PathType.LEFT and len(target_path) == 1
                goal_error_info = PostureGraphService._get_new_goal_error_info()
                routing_goals = connectivity_handle.get_goals(relative_object=target, for_source=for_source,
                  single_goal_only=single_goal_only,
                  for_carryable=for_carryable,
                  goal_height_limit=goal_height_limit,
                  target_reference_override=target_reference_override,
                  perform_los_check=perform_los_check,
                  out_result_info=goal_error_info,
                  check_height_clearance=False)
                if not routing_goals:
                    if gsi_handlers.posture_graph_handlers.archiver.enabled:
                        gsi_handlers.posture_graph_handlers.log_transition_handle(sim, connectivity_handle, connectivity_handle.polygons, target_path, str(goal_error_info), path_type)
                        continue
                    yield_to_irq()
                    valid_goals = []
                    invalid_goals = []
                    invalid_los_goals = []
                    ignore_los_for_vehicle = sim.posture.is_vehicle and sim.posture.target is target
                    for goal in routing_goals:
                        if not single_goal_only:
                            if goal.requires_los_check and target is not None:
                                if (target.is_sim or ignore_los_for_vehicle or goal.failure_reason) != GoalFailureType.NoError and blocking_obj_id is not None:
                                    if goal.failure_reason == GoalFailureType.LOSBlocked:
                                        invalid_los_goals.append(goal)
                            else:
                                invalid_goals.append(goal)
                                continue
                            result, blocking_obj_id = target.check_line_of_sight((goal.location.transform),
                              verbose=True, for_carryable=for_carryable, use_standard_ignored_objects=True)
                            if result == routing.RAYCAST_HIT_TYPE_IMPASSABLE:
                                invalid_goals.append(goal)
                                continue
                            else:
                                if result == routing.RAYCAST_HIT_TYPE_LOS_IMPASSABLE:
                                    invalid_los_goals.append(goal)
                                    continue
                                goal.path_id = cur_path_id
                                valid_goals.append(goal)

                    if gsi_handlers.posture_graph_handlers.archiver.enabled and not invalid_goals:
                        if invalid_los_goals:
                            failure_set = PostureGraphService._goal_failure_set(invalid_goals)
                            failure_set.union(PostureGraphService._goal_failure_set(invalid_los_goals))
                            gsi_handlers.posture_graph_handlers.log_transition_handle(sim, connectivity_handle, connectivity_handle.polygons, target_path, str(failure_set), path_type)
                    if invalid_goals:
                        invalid_handle_dict[connectivity_handle] = (
                         target_path, target_path.cost, var_map, dest_spec,
                         invalid_goals, routing_constraint, final_constraint)
                    if invalid_los_goals:
                        invalid_los_dict[connectivity_handle] = (
                         target_path, target_path.cost, var_map, dest_spec,
                         invalid_los_goals, routing_constraint, final_constraint)
                    if not valid_goals:
                        continue
                    if gsi_handlers.posture_graph_handlers.archiver.enabled:
                        valid_str = '{} usable, {}'.format(len(valid_goals), PostureGraphService._goal_failure_set(valid_goals))
                        if goal_error_info:
                            valid_str += '; rejected {}, {}'.format(len(goal_error_info), goal_error_info)
                        gsi_handlers.posture_graph_handlers.log_transition_handle(sim, connectivity_handle, connectivity_handle.polygons, target_path, valid_str, path_type)
                    handle_dict[connectivity_handle] = (target_path, target_path.cost, var_map,
                     dest_spec, valid_goals, routing_constraint,
                     final_constraint)

            if gsi_handlers.posture_graph_handlers.archiver.enabled and not connectivity_handles:
                if sub_constraint.geometry is not None:
                    gsi_handlers.posture_graph_handlers.log_transition_handle(sim, None, sub_constraint.geometry, target_path, True, path_type)

        return blocking_obj_id or None

    @staticmethod
    def copy_handles(sim, destination_handles, path, var_map):
        existing_data = destination_handles.get(DEFAULT)
        if existing_data is not None:
            existing_cost = existing_data[1]
            if path.cost >= existing_cost:
                return
        destination_spec = path.segmented_path.destination_specs.get(path[-1])
        destination_handles[DEFAULT] = (path, path.cost,
         var_map, destination_spec, [],
         Anywhere(), Anywhere())

    def _get_resolved_var_map(self, path, var_map):
        final_spec = path[-1]
        target = final_spec.body.target
        surface_target = final_spec.surface.target
        updates = {}
        if target is not None:
            original_target = var_map.get(PostureSpecVariable.INTERACTION_TARGET)
            if original_target == PostureSpecVariable.BODY_TARGET_FILTERED:
                original_target = target
            if original_target is not None:
                if original_target.id == target.id:
                    updates[PostureSpecVariable.INTERACTION_TARGET] = target
            original_carry_target = var_map.get(PostureSpecVariable.CARRY_TARGET)
            if original_carry_target is not None:
                if original_carry_target.id == target.id:
                    updates[PostureSpecVariable.CARRY_TARGET] = target
        if surface_target is not None:
            slot_manifest_entry = var_map.get(PostureSpecVariable.SLOT)
            if slot_manifest_entry is not None:
                if slot_manifest_entry.target is not None:
                    if isinstance(slot_manifest_entry.target, PostureSpecVariable) or slot_manifest_entry.target.id == surface_target.id:
                        slot_manifest_entry = SlotManifestEntry(slot_manifest_entry.actor, surface_target, slot_manifest_entry.slot)
                        updates[PostureSpecVariable.SLOT] = slot_manifest_entry
        return frozendict(var_map, updates)

    def _generate_left_handles(self, sim, interaction, participant_type, left_path, var_map, destination_spec, final_constraint, unique_id, sim_position_routing_data):
        left_handles = {}
        invalid = {}
        invalid_los = {}
        blocking_obj_ids = []
        if not left_path[0].body.posture_type.use_containment_slot_for_exit:
            blocking_obj_id = self.append_handles(sim,
              left_handles, invalid, invalid_los, sim_position_routing_data, left_path,
              var_map, destination_spec, unique_id, final_constraint, path_type=(PathType.LEFT))
            if blocking_obj_id is not None:
                blocking_obj_ids.append(blocking_obj_id)
        else:
            exit_spec, _, _ = self.find_exit_posture_spec(sim, left_path, var_map)
            transition_posture_name = left_path[-1].body_posture.name
            if exit_spec == left_path[0] and sim.posture.is_puppet:
                with create_puppet_postures(sim):
                    use_previous_position, routing_data = self._get_locations_from_posture(sim,
                      exit_spec, var_map, participant_type=participant_type, transition_posture_name=transition_posture_name)
            else:
                use_previous_position, routing_data = self._get_locations_from_posture(sim,
                  exit_spec, var_map, mobile_posture_spec=(left_path[-1]), participant_type=participant_type,
                  transition_posture_name=transition_posture_name,
                  left_most_spec=(left_path[0]))
            if use_previous_position:
                routing_data = sim_position_routing_data
            blocking_obj_id = self.append_handles(sim,
              left_handles, invalid, invalid_los, routing_data, left_path, var_map,
              destination_spec, unique_id, final_constraint, entry=False, path_type=(PathType.LEFT))
            if blocking_obj_id is not None:
                blocking_obj_ids.append(blocking_obj_id)
            return (left_handles, invalid, invalid_los, blocking_obj_ids)

    def _generate_right_handles(self, sim, interaction, participant_type, right_path, var_map, destination_spec, final_constraint, unique_id, animation_resolver_fn):
        right_handles = {}
        invalid = {}
        invalid_los = {}
        blocking_obj_ids = []
        first_spec = right_path[0]
        if first_spec.body.posture_type.mobile:
            entry_spec, constrained_edge, _ = first_spec.body.target is None or first_spec.body.posture_type.unconstrained or self.find_entry_posture_spec(sim, right_path, var_map)
            final_spec = right_path[-1]
            relevant_interaction = interaction if entry_spec is final_spec else None
            right_var_map = self._get_resolved_var_map(right_path, right_path.segmented_path.var_map)
            right_path.segmented_path.var_map_resolved = right_var_map
            transition_posture_name = first_spec.body_posture.name
            use_previous_pos, routing_data = self._get_locations_from_posture(sim,
              entry_spec, right_var_map, interaction=relevant_interaction,
              mobile_posture_spec=first_spec,
              participant_type=participant_type,
              constrained_edge=constrained_edge,
              animation_resolver_fn=animation_resolver_fn,
              final_constraint=final_constraint,
              transition_posture_name=transition_posture_name)
            if use_previous_pos:
                self.copy_handles(sim, right_handles, right_path, right_var_map)
        elif routing_data[0].valid:
            perform_los_check = interaction.should_perform_routing_los_check
            blocking_obj_id = self.append_handles(sim,
              right_handles, invalid, invalid_los, routing_data, right_path,
              right_var_map, destination_spec, unique_id, final_constraint,
              path_type=(PathType.RIGHT), goal_height_limit=(interaction.goal_height_limit),
              perform_los_check=perform_los_check)
            if blocking_obj_id is not None:
                blocking_obj_ids.append(blocking_obj_id)
        else:
            if first_spec.body_target is not None:
                if first_spec.body_target.is_sim:
                    right_var_map = self._get_resolved_var_map(right_path, right_path.segmented_path.var_map)
                    right_path.segmented_path.var_map_resolved = right_var_map
                    self.copy_handles(sim, right_handles, right_path, right_var_map)
        return (
         right_handles, invalid, invalid_los, blocking_obj_ids)

    def _generate_middle_handles--- This code section failed: ---

 L.5994         0  BUILD_MAP_0           0 
                2  STORE_FAST               'middle_handles'

 L.5995         4  BUILD_MAP_0           0 
                6  STORE_FAST               'invalid'

 L.5996         8  BUILD_MAP_0           0 
               10  STORE_FAST               'invalid_los'

 L.5998        12  BUILD_LIST_0          0 
               14  STORE_FAST               'blocking_obj_ids'

 L.6003        16  LOAD_FAST                'self'
               18  LOAD_METHOD              find_entry_posture_spec
               20  LOAD_DEREF               'sim'
               22  LOAD_FAST                'middle_path'
               24  LOAD_FAST                'var_map'
               26  CALL_METHOD_3         3  '3 positional arguments'
               28  UNPACK_SEQUENCE_3     3 
               30  STORE_FAST               'entry_spec'
               32  STORE_FAST               'constrained_edge'
               34  STORE_FAST               'carry_spec'

 L.6005        36  LOAD_FAST                'var_map'
               38  LOAD_GLOBAL              PostureSpecVariable
               40  LOAD_ATTR                CARRY_TARGET
               42  BINARY_SUBSCR    
               44  STORE_DEREF              'carry_target'

 L.6007        46  LOAD_FAST                'constrained_edge'
               48  LOAD_CONST               None
               50  COMPARE_OP               is
               52  POP_JUMP_IF_FALSE   130  'to 130'

 L.6008        54  LOAD_DEREF               'carry_target'
               56  LOAD_CONST               None
               58  COMPARE_OP               is-not
               60  POP_JUMP_IF_FALSE    88  'to 88'
               62  LOAD_DEREF               'carry_target'
               64  LOAD_METHOD              is_in_sim_inventory
               66  CALL_METHOD_0         0  '0 positional arguments'
               68  POP_JUMP_IF_FALSE    88  'to 88'

 L.6012        70  LOAD_FAST                'self'
               72  LOAD_METHOD              copy_handles
               74  LOAD_DEREF               'sim'
               76  LOAD_FAST                'middle_handles'
               78  LOAD_FAST                'middle_path'
               80  LOAD_FAST                'var_map'
               82  CALL_METHOD_4         4  '4 positional arguments'
               84  POP_TOP          
               86  JUMP_FORWARD        626  'to 626'
             88_0  COME_FROM            68  '68'
             88_1  COME_FROM            60  '60'

 L.6024        88  LOAD_GLOBAL              PostureGraphMiddlePathError

 L.6035        90  LOAD_STR                 '\n                   Have a middle path to pick up an object that is not in the\n                   inventory and we cannot generate a constrained_edge:\n                    \n                   carry target: {}\n                   interaction: {}\n                   final constraint: {}\n                   dest spec: {}\n                   entry spec: {}\n                   sim location: {}\n                   carry target location: {}\n                   '
               92  LOAD_METHOD              format
               94  LOAD_DEREF               'carry_target'
               96  LOAD_FAST                'interaction'
               98  LOAD_FAST                'final_constraint'

 L.6036       100  LOAD_FAST                'destination_spec'
              102  LOAD_FAST                'entry_spec'
              104  LOAD_DEREF               'sim'
              106  LOAD_ATTR                location

 L.6037       108  LOAD_DEREF               'carry_target'
              110  POP_JUMP_IF_FALSE   118  'to 118'
              112  LOAD_DEREF               'carry_target'
              114  LOAD_ATTR                location
              116  JUMP_FORWARD        120  'to 120'
            118_0  COME_FROM           110  '110'
              118  LOAD_STR                 'NO CARRY TARGET'
            120_0  COME_FROM           116  '116'
              120  CALL_METHOD_7         7  '7 positional arguments'
              122  CALL_FUNCTION_1       1  '1 positional argument'
              124  RAISE_VARARGS_1       1  'exception instance'
          126_128  JUMP_FORWARD        626  'to 626'
            130_0  COME_FROM            52  '52'

 L.6042       130  LOAD_FAST                'constrained_edge'
              132  LOAD_METHOD              get_constraint
              134  LOAD_DEREF               'sim'
              136  LOAD_FAST                'carry_spec'
              138  LOAD_FAST                'var_map'
              140  CALL_METHOD_3         3  '3 positional arguments'
              142  STORE_FAST               'carry_transition_constraint'

 L.6044       144  LOAD_DEREF               'carry_target'
              146  LOAD_CONST               None
              148  COMPARE_OP               is-not
              150  POP_JUMP_IF_FALSE   178  'to 178'
              152  LOAD_DEREF               'carry_target'
              154  LOAD_ATTR                is_sim
              156  POP_JUMP_IF_FALSE   178  'to 178'

 L.6045       158  LOAD_FAST                'animation_resolver_fn'
              160  STORE_DEREF              '_animation_resolver_fn'

 L.6060       162  LOAD_CLOSURE             '_animation_resolver_fn'
              164  LOAD_CLOSURE             'carry_target'
              166  LOAD_CLOSURE             'sim'
              168  BUILD_TUPLE_3         3 
              170  LOAD_CODE                <code_object animation_resolver_fn>
              172  LOAD_STR                 'PostureGraphService._generate_middle_handles.<locals>.animation_resolver_fn'
              174  MAKE_FUNCTION_8          'closure'
              176  STORE_FAST               'animation_resolver_fn'
            178_0  COME_FROM           156  '156'
            178_1  COME_FROM           150  '150'

 L.6070       178  LOAD_FAST                'carry_transition_constraint'
              180  LOAD_CONST               None
              182  COMPARE_OP               is-not
          184_186  POP_JUMP_IF_FALSE   358  'to 358'

 L.6071       188  BUILD_LIST_0          0 
              190  STORE_FAST               'carry_transition_constraints'

 L.6072       192  SETUP_LOOP          350  'to 350'
              194  LOAD_FAST                'carry_transition_constraint'
              196  GET_ITER         
              198  FOR_ITER            348  'to 348'
              200  STORE_FAST               'carry_transition_sub_constraint'

 L.6073       202  LOAD_DEREF               'carry_target'
              204  LOAD_CONST               None
              206  COMPARE_OP               is-not
          208_210  POP_JUMP_IF_FALSE   288  'to 288'
              212  LOAD_DEREF               'carry_target'
              214  LOAD_ATTR                is_sim
          216_218  POP_JUMP_IF_FALSE   288  'to 288'

 L.6077       220  LOAD_FAST                'interaction'
              222  LOAD_ATTR                transition
              224  LOAD_METHOD              add_on_target_location_changed_callback
              226  LOAD_DEREF               'carry_target'
              228  CALL_METHOD_1         1  '1 positional argument'
              230  POP_TOP          

 L.6079       232  LOAD_FAST                'carry_transition_sub_constraint'
              234  LOAD_ATTR                posture_state_spec
              236  LOAD_CONST               None
              238  COMPARE_OP               is-not
          240_242  POP_JUMP_IF_FALSE   288  'to 288'

 L.6080       244  LOAD_FAST                'carry_transition_sub_constraint'
              246  LOAD_ATTR                posture_state_spec
              248  LOAD_ATTR                body_target
              250  STORE_FAST               'carry_body_target'

 L.6081       252  LOAD_FAST                'carry_body_target'
              254  LOAD_CONST               None
              256  COMPARE_OP               is-not
          258_260  POP_JUMP_IF_FALSE   288  'to 288'

 L.6089       262  LOAD_GLOBAL              PostureAspectBody
              264  LOAD_FAST                'carry_spec'
              266  LOAD_ATTR                body
              268  LOAD_ATTR                posture_type
              270  LOAD_FAST                'carry_body_target'
              272  CALL_FUNCTION_2       2  '2 positional arguments'
              274  STORE_FAST               'body_aspect'

 L.6090       276  LOAD_FAST                'carry_spec'
              278  LOAD_ATTR                clone
              280  LOAD_FAST                'body_aspect'
              282  LOAD_CONST               ('body',)
              284  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              286  STORE_FAST               'carry_spec'
            288_0  COME_FROM           258  '258'
            288_1  COME_FROM           240  '240'
            288_2  COME_FROM           216  '216'
            288_3  COME_FROM           208  '208'

 L.6093       288  LOAD_GLOBAL              postures
              290  LOAD_ATTR                posture_state
              292  LOAD_ATTR                PostureState
              294  LOAD_DEREF               'sim'
              296  LOAD_CONST               None
              298  LOAD_FAST                'carry_spec'

 L.6094       300  LOAD_FAST                'var_map'
              302  LOAD_CONST               True
              304  LOAD_CONST               ('invalid_expected',)
              306  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              308  STORE_FAST               'target_posture_state'

 L.6099       310  LOAD_FAST                'interaction'
              312  LOAD_ATTR                transition
              314  LOAD_METHOD              add_relevant_object
              316  LOAD_FAST                'target_posture_state'
              318  LOAD_ATTR                body_target
              320  CALL_METHOD_1         1  '1 positional argument'
              322  POP_TOP          

 L.6101       324  LOAD_FAST                'carry_transition_sub_constraint'
              326  LOAD_METHOD              apply_posture_state

 L.6102       328  LOAD_FAST                'target_posture_state'
              330  LOAD_FAST                'animation_resolver_fn'
              332  CALL_METHOD_2         2  '2 positional arguments'
              334  STORE_FAST               'carry_transition_sub_constraint'

 L.6103       336  LOAD_FAST                'carry_transition_constraints'
              338  LOAD_METHOD              append
              340  LOAD_FAST                'carry_transition_sub_constraint'
              342  CALL_METHOD_1         1  '1 positional argument'
              344  POP_TOP          
              346  JUMP_BACK           198  'to 198'
              348  POP_BLOCK        
            350_0  COME_FROM_LOOP      192  '192'

 L.6104       350  LOAD_GLOBAL              create_constraint_set
              352  LOAD_FAST                'carry_transition_constraints'
              354  CALL_FUNCTION_1       1  '1 positional argument'
              356  STORE_FAST               'carry_transition_constraint'
            358_0  COME_FROM           184  '184'

 L.6106       358  LOAD_FAST                'carry_transition_constraint'
              360  LOAD_CONST               None
              362  COMPARE_OP               is-not
          364_366  POP_JUMP_IF_FALSE   626  'to 626'

 L.6107       368  LOAD_GLOBAL              any
              370  LOAD_GENEXPR             '<code_object <genexpr>>'
              372  LOAD_STR                 'PostureGraphService._generate_middle_handles.<locals>.<genexpr>'
              374  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              376  LOAD_FAST                'carry_transition_constraint'
              378  GET_ITER         
              380  CALL_FUNCTION_1       1  '1 positional argument'
              382  CALL_FUNCTION_1       1  '1 positional argument'
              384  STORE_FAST               'constraint_has_geometry'

 L.6108       386  LOAD_FAST                'constraint_has_geometry'
          388_390  POP_JUMP_IF_TRUE    448  'to 448'

 L.6114       392  LOAD_GLOBAL              services
              394  LOAD_METHOD              current_zone
              396  CALL_METHOD_0         0  '0 positional arguments'
              398  LOAD_ATTR                posture_graph_service
              400  STORE_FAST               'posture_graph_service'

 L.6115       402  LOAD_FAST                'posture_graph_service'
              404  LOAD_METHOD              get_compatible_mobile_posture_target
              406  LOAD_DEREF               'sim'
              408  CALL_METHOD_1         1  '1 positional argument'
              410  STORE_FAST               'posture_object'

 L.6116       412  LOAD_FAST                'posture_object'
              414  LOAD_CONST               None
              416  COMPARE_OP               is-not
          418_420  POP_JUMP_IF_FALSE   448  'to 448'

 L.6117       422  LOAD_FAST                'posture_object'
              424  LOAD_ATTR                get_edge_constraint
              426  LOAD_DEREF               'sim'
              428  LOAD_CONST               ('sim',)
              430  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              432  STORE_FAST               'edge_constraint'

 L.6118       434  LOAD_FAST                'carry_transition_constraint'
              436  LOAD_METHOD              intersect
              438  LOAD_FAST                'edge_constraint'
              440  CALL_METHOD_1         1  '1 positional argument'
              442  STORE_FAST               'carry_transition_constraint'

 L.6119       444  LOAD_CONST               True
              446  STORE_FAST               'constraint_has_geometry'
            448_0  COME_FROM           418  '418'
            448_1  COME_FROM           388  '388'

 L.6123       448  LOAD_FAST                'carry_spec'
              450  LOAD_ATTR                surface
              452  STORE_FAST               'carry_spec_surface_spec'

 L.6124       454  LOAD_FAST                'carry_spec_surface_spec'
              456  LOAD_CONST               None
              458  COMPARE_OP               is-not
          460_462  POP_JUMP_IF_FALSE   472  'to 472'

 L.6125       464  LOAD_FAST                'carry_spec_surface_spec'
              466  LOAD_ATTR                target
              468  STORE_FAST               'relative_object'
              470  JUMP_FORWARD        476  'to 476'
            472_0  COME_FROM           460  '460'

 L.6127       472  LOAD_CONST               None
              474  STORE_FAST               'relative_object'
            476_0  COME_FROM           470  '470'

 L.6128       476  LOAD_FAST                'relative_object'
              478  LOAD_CONST               None
              480  COMPARE_OP               is
          482_484  POP_JUMP_IF_FALSE   494  'to 494'

 L.6129       486  LOAD_FAST                'carry_spec'
              488  LOAD_ATTR                body
              490  LOAD_ATTR                target
              492  STORE_FAST               'relative_object'
            494_0  COME_FROM           482  '482'

 L.6130       494  LOAD_FAST                'relative_object'
              496  LOAD_CONST               None
              498  COMPARE_OP               is
          500_502  POP_JUMP_IF_FALSE   534  'to 534'

 L.6131       504  LOAD_FAST                'entry_spec'
              506  LOAD_ATTR                carry
              508  LOAD_ATTR                target
              510  STORE_FAST               'relative_object'

 L.6132       512  LOAD_GLOBAL              isinstance
              514  LOAD_FAST                'relative_object'
              516  LOAD_GLOBAL              PostureSpecVariable
              518  CALL_FUNCTION_2       2  '2 positional arguments'
          520_522  POP_JUMP_IF_FALSE   534  'to 534'

 L.6133       524  LOAD_FAST                'var_map'
              526  LOAD_METHOD              get
              528  LOAD_FAST                'relative_object'
              530  CALL_METHOD_1         1  '1 positional argument'
              532  STORE_FAST               'relative_object'
            534_0  COME_FROM           520  '520'
            534_1  COME_FROM           500  '500'

 L.6141       534  LOAD_FAST                'constraint_has_geometry'
          536_538  POP_JUMP_IF_FALSE   610  'to 610'

 L.6142       540  LOAD_FAST                'carry_transition_constraint'
              542  LOAD_METHOD              generate_single_surface_constraints
              544  CALL_METHOD_0         0  '0 positional arguments'
              546  STORE_FAST               'carry_transition_constraint'

 L.6143       548  LOAD_FAST                'self'
              550  LOAD_ATTR                append_handles

 L.6144       552  LOAD_DEREF               'sim'
              554  LOAD_FAST                'middle_handles'
              556  LOAD_FAST                'invalid'
              558  LOAD_FAST                'invalid_los'

 L.6145       560  LOAD_FAST                'carry_transition_constraint'
              562  LOAD_CONST               None
              564  LOAD_FAST                'relative_object'
              566  BUILD_TUPLE_3         3 

 L.6146       568  LOAD_FAST                'middle_path'
              570  LOAD_FAST                'var_map'
              572  LOAD_FAST                'destination_spec'
              574  LOAD_FAST                'unique_id'

 L.6147       576  LOAD_FAST                'final_constraint'
              578  LOAD_GLOBAL              PathType
              580  LOAD_ATTR                MIDDLE_LEFT
              582  LOAD_CONST               ('path_type',)
            584_0  COME_FROM            86  '86'
              584  CALL_FUNCTION_KW_11    11  '11 total positional and keyword args'
              586  STORE_FAST               'blocking_obj_id'

 L.6148       588  LOAD_FAST                'blocking_obj_id'
              590  LOAD_CONST               None
              592  COMPARE_OP               is-not
          594_596  POP_JUMP_IF_FALSE   626  'to 626'

 L.6149       598  LOAD_FAST                'blocking_obj_ids'
              600  LOAD_METHOD              append
              602  LOAD_FAST                'blocking_obj_id'
              604  CALL_METHOD_1         1  '1 positional argument'
              606  POP_TOP          
              608  JUMP_FORWARD        626  'to 626'
            610_0  COME_FROM           536  '536'

 L.6151       610  LOAD_FAST                'self'
              612  LOAD_METHOD              copy_handles
              614  LOAD_DEREF               'sim'
              616  LOAD_FAST                'middle_handles'
              618  LOAD_FAST                'middle_path'
              620  LOAD_FAST                'var_map'
              622  CALL_METHOD_4         4  '4 positional arguments'
              624  POP_TOP          
            626_0  COME_FROM           608  '608'
            626_1  COME_FROM           594  '594'
            626_2  COME_FROM           364  '364'
            626_3  COME_FROM           126  '126'

 L.6152       626  LOAD_FAST                'middle_handles'
              628  LOAD_FAST                'invalid'
              630  LOAD_FAST                'invalid_los'
              632  LOAD_FAST                'blocking_obj_ids'
              634  BUILD_TUPLE_4         4 
              636  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 584_0

    def _get_segmented_path_connectivity_handles(self, sim, segmented_path, interaction, participant_type, animation_resolver_fn, sim_position_routing_data):
        blocking_obj_ids = []
        searched = {PathType.LEFT: set(), PathType.RIGHT: set()}
        middle_handles, invalid_middles, invalid_los_middles = {}, {}, {}
        destination_handles, invalid_destinations, invalid_los_destinations = {}, {}, {}
        source_handles, invalid_sources, invalid_los_sources = {}, {}, {}
        for path_left in segmented_path.generate_left_paths():
            final_left_node = path_left[-1]
            if final_left_node in searched[PathType.LEFT]:
                continue
            source_handles, invalid_sources, invalid_los_sources, blockers = self._generate_left_handles(sim, interaction, participant_type, path_left, segmented_path.var_map, None, segmented_path.constraint, id(segmented_path), sim_position_routing_data)
            blocking_obj_ids += blockers
            if not source_handles:
                continue
            searched[PathType.LEFT].add(final_left_node)
            for path_right in segmented_path.generate_right_paths(sim, path_left):
                entry_node, _, _ = self.find_entry_posture_spec(sim, path_right, segmented_path.var_map)
                if entry_node is not None:
                    if entry_node.body_target in searched[PathType.RIGHT]:
                        continue
                    else:
                        final_right_node = path_right[-1]
                        destination_spec = segmented_path.destination_specs[final_right_node]
                        destination_handles, invalid_destinations, invalid_los_destinations, blockers = self._generate_right_handles(sim, interaction, participant_type, path_right, segmented_path.var_map, destination_spec, segmented_path.constraint, id(segmented_path), animation_resolver_fn)
                        blocking_obj_ids += blockers
                        if not destination_handles:
                            continue
                        final_body_target = final_right_node.body_target
                        final_body_posture = final_right_node.body_posture
                        if final_body_target is not None:
                            if not final_body_posture.is_vehicle or final_body_posture is not final_left_node.body_posture:
                                posture = postures.create_posture(final_body_posture, sim,
                                  final_body_target, is_throwaway=True)
                                slot_constraint = posture.slot_constraint_simple
                                if slot_constraint is not None:
                                    geometry_constraint = segmented_path.constraint.generate_geometry_only_constraint()
                                    if not slot_constraint.intersect(geometry_constraint).valid:
                                        continue
                    if entry_node is not None:
                        searched[PathType.RIGHT].add(entry_node.body_target)
                    for path_middle in segmented_path.generate_middle_paths(path_left, path_right):
                        if path_middle is None:
                            return (
                             source_handles, {}, destination_handles,
                             invalid_sources, {}, invalid_destinations,
                             invalid_los_sources, {}, invalid_los_destinations,
                             blocking_obj_ids)
                            middle_handles, invalid_middles, invalid_los_middles, blockers = self._generate_middle_handles(sim, interaction, participant_type, path_middle, segmented_path.var_map_resolved, destination_spec, segmented_path.constraint, id(segmented_path), animation_resolver_fn)
                            blocking_obj_ids += blockers
                            if middle_handles:
                                return (
                                 source_handles, middle_handles, destination_handles,
                                 invalid_sources, invalid_middles, invalid_destinations,
                                 invalid_los_sources, invalid_los_middles, invalid_los_destinations,
                                 blocking_obj_ids)

                    if all((dest in searched[PathType.RIGHT] for dest in segmented_path.left_destinations)) or len(searched[PathType.RIGHT]) >= MAX_RIGHT_PATHS:
                        break

        return (
         source_handles, {}, {},
         invalid_sources, invalid_middles, invalid_destinations,
         invalid_los_sources, invalid_los_middles, invalid_los_destinations,
         blocking_obj_ids)

    def generate_connectivity_handles--- This code section failed: ---

 L.6283         0  LOAD_GLOBAL              len
                2  LOAD_FAST                'segmented_paths'
                4  CALL_FUNCTION_1       1  '1 positional argument'
                6  LOAD_CONST               0
                8  COMPARE_OP               ==
               10  POP_JUMP_IF_FALSE    16  'to 16'

 L.6284        12  LOAD_GLOBAL              NO_CONNECTIVITY
               14  RETURN_VALUE     
             16_0  COME_FROM            10  '10'

 L.6289        16  LOAD_GLOBAL              collections
               18  LOAD_METHOD              OrderedDict
               20  CALL_METHOD_0         0  '0 positional arguments'
               22  STORE_FAST               'source_destination_sets'

 L.6290        24  LOAD_GLOBAL              collections
               26  LOAD_METHOD              OrderedDict
               28  CALL_METHOD_0         0  '0 positional arguments'
               30  STORE_FAST               'source_middle_sets'

 L.6291        32  LOAD_GLOBAL              collections
               34  LOAD_METHOD              OrderedDict
               36  CALL_METHOD_0         0  '0 positional arguments'
               38  STORE_FAST               'middle_destination_sets'

 L.6292        40  LOAD_FAST                'self'
               42  LOAD_METHOD              get_sim_position_routing_data
               44  LOAD_FAST                'sim'
               46  CALL_METHOD_1         1  '1 positional argument'
               48  STORE_FAST               'sim_position_routing_data'

 L.6294        50  LOAD_GLOBAL              EMPTY_PATH_SPEC
               52  STORE_FAST               'best_complete_path'

 L.6297     54_56  SETUP_LOOP          452  'to 452'
               58  LOAD_FAST                'segmented_paths'
               60  GET_ITER         
            62_64  FOR_ITER            450  'to 450'
               66  STORE_FAST               'segmented_path'

 L.6298        68  LOAD_FAST                'segmented_path'
               70  LOAD_ATTR                is_complete
               72  POP_JUMP_IF_TRUE     76  'to 76'

 L.6299        74  CONTINUE             62  'to 62'
             76_0  COME_FROM            72  '72'

 L.6300     76_78  SETUP_LOOP          448  'to 448'
               80  LOAD_FAST                'segmented_path'
               82  LOAD_METHOD              generate_left_paths
               84  CALL_METHOD_0         0  '0 positional arguments'
               86  GET_ITER         
             88_0  COME_FROM           440  '440'
            88_90  FOR_ITER            446  'to 446'
               92  STORE_FAST               'left_path'

 L.6301     94_96  SETUP_LOOP          434  'to 434'
               98  LOAD_FAST                'segmented_path'
              100  LOAD_METHOD              generate_right_paths
              102  LOAD_FAST                'sim'
              104  LOAD_FAST                'left_path'
              106  CALL_METHOD_2         2  '2 positional arguments'
              108  GET_ITER         
          110_112  FOR_ITER            432  'to 432'
              114  STORE_FAST               'right_path'

 L.6303       116  LOAD_FAST                'left_path'
              118  LOAD_FAST                'right_path'
              120  BINARY_ADD       
              122  STORE_FAST               'complete_path'

 L.6304       124  LOAD_FAST                'self'
              126  LOAD_METHOD              is_valid_complete_path
              128  LOAD_FAST                'sim'
              130  LOAD_FAST                'complete_path'
              132  LOAD_FAST                'interaction'
              134  CALL_METHOD_3         3  '3 positional arguments'
              136  POP_JUMP_IF_TRUE    140  'to 140'

 L.6306       138  CONTINUE            110  'to 110'
            140_0  COME_FROM           136  '136'

 L.6308       140  LOAD_FAST                'best_complete_path'
              142  LOAD_GLOBAL              EMPTY_PATH_SPEC
              144  COMPARE_OP               is-not
              146  POP_JUMP_IF_FALSE   162  'to 162'

 L.6309       148  LOAD_FAST                'best_complete_path'
              150  LOAD_ATTR                cost
              152  LOAD_FAST                'complete_path'
              154  LOAD_ATTR                cost
              156  COMPARE_OP               <=
              158  POP_JUMP_IF_FALSE   162  'to 162'

 L.6313       160  BREAK_LOOP       
            162_0  COME_FROM           158  '158'
            162_1  COME_FROM           146  '146'

 L.6315       162  LOAD_FAST                'complete_path'
              164  LOAD_CONST               -1
              166  BINARY_SUBSCR    
              168  STORE_FAST               'final_node'

 L.6322       170  LOAD_FAST                'interaction'
              172  LOAD_ATTR                privacy
              174  LOAD_CONST               None
              176  COMPARE_OP               is-not
              178  POP_JUMP_IF_FALSE   202  'to 202'
              180  LOAD_GLOBAL              len
              182  LOAD_FAST                'complete_path'
              184  CALL_FUNCTION_1       1  '1 positional argument'
              186  LOAD_CONST               1
              188  COMPARE_OP               ==
              190  POP_JUMP_IF_FALSE   202  'to 202'

 L.6323       192  LOAD_FAST                'complete_path'
              194  LOAD_METHOD              append
              196  LOAD_FAST                'final_node'
              198  CALL_METHOD_1         1  '1 positional argument'
              200  POP_TOP          
            202_0  COME_FROM           190  '190'
            202_1  COME_FROM           178  '178'

 L.6325       202  LOAD_FAST                'segmented_path'
              204  LOAD_ATTR                destination_specs
              206  LOAD_FAST                'final_node'
              208  BINARY_SUBSCR    
              210  STORE_FAST               'destination_spec'

 L.6326       212  LOAD_FAST                'self'
              214  LOAD_METHOD              _get_resolved_var_map
              216  LOAD_FAST                'complete_path'
              218  LOAD_FAST                'segmented_path'
              220  LOAD_ATTR                var_map
              222  CALL_METHOD_2         2  '2 positional arguments'
              224  STORE_FAST               'var_map'

 L.6327       226  LOAD_FAST                'segmented_path'
              228  LOAD_ATTR                constraint
              230  STORE_FAST               'constraint'

 L.6329       232  LOAD_GLOBAL              len
              234  LOAD_FAST                'complete_path'
              236  CALL_FUNCTION_1       1  '1 positional argument'
              238  LOAD_CONST               1
              240  COMPARE_OP               ==
          242_244  POP_JUMP_IF_FALSE   310  'to 310'

 L.6333       246  LOAD_CONST               None
              248  STORE_FAST               'transform_constraint'

 L.6334       250  LOAD_FAST                'sim'
              252  LOAD_ATTR                posture
              254  LOAD_ATTR                mobile
          256_258  POP_JUMP_IF_TRUE    268  'to 268'

 L.6337       260  LOAD_FAST                'sim'
              262  LOAD_ATTR                posture
              264  LOAD_ATTR                slot_constraint
              266  STORE_FAST               'transform_constraint'
            268_0  COME_FROM           256  '256'

 L.6338       268  LOAD_FAST                'transform_constraint'
              270  LOAD_CONST               None
              272  COMPARE_OP               is
          274_276  POP_JUMP_IF_FALSE   298  'to 298'

 L.6340       278  LOAD_GLOBAL              interactions
              280  LOAD_ATTR                constraints
              282  LOAD_ATTR                Transform

 L.6341       284  LOAD_FAST                'sim'
              286  LOAD_ATTR                transform
              288  LOAD_FAST                'sim'
              290  LOAD_ATTR                routing_surface
              292  LOAD_CONST               ('routing_surface',)
              294  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              296  STORE_FAST               'transform_constraint'
            298_0  COME_FROM           274  '274'

 L.6343       298  LOAD_FAST                'constraint'
              300  LOAD_METHOD              intersect
              302  LOAD_FAST                'transform_constraint'
              304  CALL_METHOD_1         1  '1 positional argument'
              306  STORE_FAST               'final_constraint'
              308  JUMP_FORWARD        350  'to 350'
            310_0  COME_FROM           242  '242'

 L.6349       310  LOAD_FAST                'self'
              312  LOAD_ATTR                _get_locations_from_posture

 L.6350       314  LOAD_FAST                'sim'
              316  LOAD_FAST                'complete_path'
              318  LOAD_CONST               -1
              320  BINARY_SUBSCR    
              322  LOAD_FAST                'var_map'
              324  LOAD_FAST                'interaction'

 L.6351       326  LOAD_FAST                'participant_type'

 L.6352       328  LOAD_FAST                'animation_resolver_fn'

 L.6353       330  LOAD_FAST                'constraint'
              332  LOAD_CONST               ('interaction', 'participant_type', 'animation_resolver_fn', 'final_constraint')
              334  CALL_FUNCTION_KW_7     7  '7 total positional and keyword args'
              336  UNPACK_SEQUENCE_2     2 
              338  STORE_FAST               '_'
              340  STORE_FAST               'routing_data'

 L.6355       342  LOAD_FAST                'routing_data'
              344  LOAD_CONST               0
              346  BINARY_SUBSCR    
              348  STORE_FAST               'final_constraint'
            350_0  COME_FROM           308  '308'

 L.6357       350  LOAD_FAST                'final_constraint'
              352  LOAD_CONST               None
              354  COMPARE_OP               is-not
          356_358  POP_JUMP_IF_FALSE   370  'to 370'
              360  LOAD_FAST                'final_constraint'
              362  LOAD_ATTR                valid
          364_366  POP_JUMP_IF_TRUE    370  'to 370'

 L.6358       368  CONTINUE            110  'to 110'
            370_0  COME_FROM           364  '364'
            370_1  COME_FROM           356  '356'

 L.6359       370  LOAD_FAST                'final_constraint'
              372  LOAD_CONST               None
              374  COMPARE_OP               is
          376_378  POP_JUMP_IF_FALSE   384  'to 384'

 L.6360       380  LOAD_FAST                'constraint'
              382  STORE_FAST               'final_constraint'
            384_0  COME_FROM           376  '376'

 L.6361       384  LOAD_GLOBAL              PathSpec

 L.6362       386  LOAD_FAST                'complete_path'
              388  LOAD_FAST                'complete_path'
              390  LOAD_ATTR                cost
              392  LOAD_FAST                'var_map'
              394  LOAD_FAST                'destination_spec'

 L.6363       396  LOAD_FAST                'final_constraint'
              398  LOAD_FAST                'constraint'
              400  LOAD_CONST               True
              402  LOAD_CONST               ('allow_tentative',)
              404  CALL_FUNCTION_KW_7     7  '7 total positional and keyword args'
              406  STORE_FAST               'best_complete_path'

 L.6365       408  LOAD_FAST                'self'
              410  LOAD_ATTR                _generate_surface_and_slot_targets

 L.6366       412  LOAD_FAST                'best_complete_path'
              414  LOAD_CONST               None
              416  LOAD_FAST                'sim'
              418  LOAD_ATTR                routing_location
              420  LOAD_GLOBAL              DEFAULT
              422  LOAD_CONST               ('objects_to_ignore',)
              424  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              426  POP_TOP          

 L.6370       428  BREAK_LOOP       
              430  JUMP_BACK           110  'to 110'
              432  POP_BLOCK        
            434_0  COME_FROM_LOOP       94  '94'

 L.6374       434  LOAD_FAST                'best_complete_path'
              436  LOAD_GLOBAL              EMPTY_PATH_SPEC
              438  COMPARE_OP               is-not
              440  POP_JUMP_IF_FALSE    88  'to 88'

 L.6375       442  BREAK_LOOP       
              444  JUMP_BACK            88  'to 88'
              446  POP_BLOCK        
            448_0  COME_FROM_LOOP       76  '76'
              448  JUMP_BACK            62  'to 62'
              450  POP_BLOCK        
            452_0  COME_FROM_LOOP       54  '54'

 L.6378       452  BUILD_LIST_0          0 
              454  STORE_FAST               'blocking_obj_ids'

 L.6380   456_458  SETUP_LOOP          736  'to 736'
              460  LOAD_FAST                'segmented_paths'
              462  GET_ITER         
          464_466  FOR_ITER            734  'to 734'
              468  STORE_FAST               'segmented_path'

 L.6381       470  LOAD_FAST                'segmented_path'
              472  LOAD_ATTR                is_complete
          474_476  POP_JUMP_IF_FALSE   482  'to 482'

 L.6382   478_480  CONTINUE            464  'to 464'
            482_0  COME_FROM           474  '474'

 L.6384       482  SETUP_EXCEPT        508  'to 508'

 L.6385       484  LOAD_FAST                'self'
              486  LOAD_METHOD              _get_segmented_path_connectivity_handles

 L.6386       488  LOAD_FAST                'sim'
              490  LOAD_FAST                'segmented_path'
              492  LOAD_FAST                'interaction'
              494  LOAD_FAST                'participant_type'

 L.6387       496  LOAD_FAST                'animation_resolver_fn'
              498  LOAD_FAST                'sim_position_routing_data'
              500  CALL_METHOD_6         6  '6 positional arguments'
              502  STORE_FAST               'handles'
              504  POP_BLOCK        
              506  JUMP_FORWARD        530  'to 530'
            508_0  COME_FROM_EXCEPT    482  '482'

 L.6388       508  DUP_TOP          
              510  LOAD_GLOBAL              PostureGraphError
              512  COMPARE_OP               exception-match
          514_516  POP_JUMP_IF_FALSE   528  'to 528'
              518  POP_TOP          
              520  POP_TOP          
              522  POP_TOP          

 L.6389       524  LOAD_GLOBAL              NO_CONNECTIVITY
              526  RETURN_VALUE     
            528_0  COME_FROM           514  '514'
              528  END_FINALLY      
            530_0  COME_FROM           506  '506'

 L.6394       530  LOAD_FAST                'handles'
              532  UNPACK_SEQUENCE_10    10 
              534  STORE_FAST               'source_handles'
              536  STORE_FAST               'middle_handles'
              538  STORE_DEREF              'destination_handles'
              540  STORE_FAST               'invalid_sources'
              542  STORE_FAST               'invalid_middles'
              544  STORE_FAST               'invalid_destinations'
              546  STORE_FAST               'invalid_los_sources'
              548  STORE_FAST               'invalid_los_middles'
              550  STORE_FAST               'invalid_los_destinations'
              552  STORE_FAST               'blockers'

 L.6397       554  LOAD_FAST                'blocking_obj_ids'
              556  LOAD_FAST                'blockers'
              558  INPLACE_ADD      
              560  STORE_FAST               'blocking_obj_ids'

 L.6402       562  LOAD_FAST                'middle_handles'
          564_566  POP_JUMP_IF_FALSE   618  'to 618'

 L.6403       568  LOAD_FAST                'source_handles'
              570  LOAD_FAST                'middle_handles'

 L.6404       572  BUILD_MAP_0           0 
              574  BUILD_MAP_0           0 

 L.6405       576  LOAD_FAST                'invalid_middles'
              578  LOAD_FAST                'invalid_los_middles'
              580  BUILD_TUPLE_6         6 
              582  STORE_FAST               'value'

 L.6406       584  LOAD_FAST                'value'
              586  LOAD_FAST                'source_middle_sets'
              588  LOAD_FAST                'segmented_path'
              590  STORE_SUBSCR     

 L.6408       592  LOAD_CONST               None
              594  LOAD_DEREF               'destination_handles'
              596  LOAD_FAST                'invalid_middles'

 L.6409       598  LOAD_FAST                'invalid_los_middles'
              600  LOAD_FAST                'invalid_destinations'

 L.6410       602  LOAD_FAST                'invalid_los_destinations'
              604  BUILD_LIST_6          6 
              606  STORE_FAST               'value'

 L.6411       608  LOAD_FAST                'value'
              610  LOAD_FAST                'middle_destination_sets'
              612  LOAD_FAST                'segmented_path'
              614  STORE_SUBSCR     
              616  JUMP_BACK           464  'to 464'
            618_0  COME_FROM           564  '564'

 L.6416       618  LOAD_GLOBAL              DEFAULT
              620  LOAD_DEREF               'destination_handles'
              622  COMPARE_OP               in
          624_626  POP_JUMP_IF_FALSE   706  'to 706'

 L.6417       628  LOAD_CLOSURE             'destination_handles'
              630  BUILD_TUPLE_1         1 
              632  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              634  LOAD_STR                 'PostureGraphService.generate_connectivity_handles.<locals>.<dictcomp>'
              636  MAKE_FUNCTION_8          'closure'

 L.6418       638  LOAD_FAST                'source_handles'
              640  GET_ITER         
              642  CALL_FUNCTION_1       1  '1 positional argument'
              644  STORE_FAST               'default_values'

 L.6419       646  SETUP_LOOP          690  'to 690'
              648  LOAD_FAST                'default_values'
              650  LOAD_METHOD              items
              652  CALL_METHOD_0         0  '0 positional arguments'
              654  GET_ITER         
              656  FOR_ITER            688  'to 688'
              658  UNPACK_SEQUENCE_2     2 
              660  STORE_FAST               'dest_handle'
              662  UNPACK_SEQUENCE_7     7 
              664  STORE_FAST               'dest_path'
              666  STORE_FAST               '_'
              668  STORE_FAST               '_'
              670  STORE_FAST               '_'
              672  STORE_FAST               '_'
              674  STORE_FAST               '_'
              676  STORE_FAST               '_'

 L.6420       678  LOAD_FAST                'dest_path'
              680  LOAD_FAST                'dest_handle'
              682  STORE_ATTR               path
          684_686  JUMP_BACK           656  'to 656'
              688  POP_BLOCK        
            690_0  COME_FROM_LOOP      646  '646'

 L.6421       690  LOAD_DEREF               'destination_handles'
              692  LOAD_GLOBAL              DEFAULT
              694  DELETE_SUBSCR    

 L.6422       696  LOAD_DEREF               'destination_handles'
              698  LOAD_METHOD              update
              700  LOAD_FAST                'default_values'
              702  CALL_METHOD_1         1  '1 positional argument'
              704  POP_TOP          
            706_0  COME_FROM           624  '624'

 L.6423       706  LOAD_FAST                'source_handles'
              708  LOAD_DEREF               'destination_handles'

 L.6424       710  BUILD_MAP_0           0 
              712  BUILD_MAP_0           0 

 L.6425       714  LOAD_FAST                'invalid_destinations'
              716  LOAD_FAST                'invalid_los_destinations'
              718  BUILD_TUPLE_6         6 
              720  STORE_FAST               'value'

 L.6426       722  LOAD_FAST                'value'
              724  LOAD_FAST                'source_destination_sets'
              726  LOAD_FAST                'segmented_path'
              728  STORE_SUBSCR     
          730_732  JUMP_BACK           464  'to 464'
              734  POP_BLOCK        
            736_0  COME_FROM_LOOP      456  '456'

 L.6428       736  LOAD_FAST                'best_complete_path'
              738  LOAD_GLOBAL              EMPTY_PATH_SPEC
              740  COMPARE_OP               is
          742_744  POP_JUMP_IF_FALSE   814  'to 814'

 L.6429       746  LOAD_FAST                'source_destination_sets'
          748_750  POP_JUMP_IF_TRUE    814  'to 814'
              752  LOAD_FAST                'source_middle_sets'
          754_756  POP_JUMP_IF_FALSE   764  'to 764'
              758  LOAD_FAST                'middle_destination_sets'
          760_762  POP_JUMP_IF_TRUE    814  'to 814'
            764_0  COME_FROM           754  '754'

 L.6430       764  LOAD_FAST                'blocking_obj_ids'
          766_768  POP_JUMP_IF_FALSE   796  'to 796'

 L.6431       770  LOAD_GLOBAL              set_transition_failure_reason
              772  LOAD_FAST                'sim'
              774  LOAD_GLOBAL              TransitionFailureReasons
              776  LOAD_ATTR                BLOCKING_OBJECT

 L.6432       778  LOAD_FAST                'blocking_obj_ids'
              780  LOAD_CONST               0
              782  BINARY_SUBSCR    

 L.6433       784  LOAD_FAST                'interaction'
              786  LOAD_ATTR                transition
              788  LOAD_CONST               ('target_id', 'transition_controller')
              790  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              792  POP_TOP          
              794  JUMP_FORWARD        814  'to 814'
            796_0  COME_FROM           766  '766'

 L.6435       796  LOAD_GLOBAL              set_transition_failure_reason
              798  LOAD_FAST                'sim'
              800  LOAD_GLOBAL              TransitionFailureReasons
              802  LOAD_ATTR                NO_VALID_INTERSECTION

 L.6436       804  LOAD_FAST                'interaction'
              806  LOAD_ATTR                transition
              808  LOAD_CONST               ('transition_controller',)
              810  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              812  POP_TOP          
            814_0  COME_FROM           794  '794'
            814_1  COME_FROM           760  '760'
            814_2  COME_FROM           748  '748'
            814_3  COME_FROM           742  '742'

 L.6438       814  LOAD_GLOBAL              Connectivity
              816  LOAD_FAST                'best_complete_path'
              818  LOAD_FAST                'source_destination_sets'

 L.6439       820  LOAD_FAST                'source_middle_sets'
              822  LOAD_FAST                'middle_destination_sets'
              824  CALL_FUNCTION_4       4  '4 positional arguments'
              826  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_DICTCOMP' instruction at offset 632

    def find_best_path_pair(self, interaction, sim, connectivity, timeline):
        best_complete_path, source_destination_sets, source_middle_sets, middle_destination_sets = connectivity
        success, best_non_complete_path = yield from self._find_best_path_pair(interaction, sim, source_destination_sets, source_middle_sets, middle_destination_sets, timeline)
        if best_complete_path is EMPTY_PATH_SPEC:
            if success == False:
                return (
                 success, best_non_complete_path)
        best_non_complete_path = best_non_complete_path.get_carry_sim_merged_path_spec()
        best_non_complete_path = best_non_complete_path.get_stand_to_carry_sim_direct_path_spec()
        if best_complete_path is EMPTY_PATH_SPEC:
            return (
             success, best_non_complete_path)
        if best_non_complete_path is EMPTY_PATH_SPEC:
            return (True, best_complete_path)
        force_complete = False
        if interaction.is_putdown and sim in (interaction.target, interaction.carry_target):
            force_complete = True
        else:
            for node in best_complete_path.path:
                if node.body_target is not None:
                    if node.body_target.is_sim:
                        for other_node in best_non_complete_path.path[1:]:
                            if node == other_node:
                                force_complete = True
                                break

                if force_complete:
                    break

        if not success or force_complete or best_complete_path.cost <= best_non_complete_path.total_cost:
            best_non_complete_path.cleanup_path_spec(sim)
            return (True, best_complete_path)
        return (success, best_non_complete_path)
        if False:
            yield None

    def _find_best_path_pair(self, interaction, sim, source_destination_sets, source_middle_sets, middle_destination_sets, timeline):
        source_dest_success = False
        source_dest_path_spec = EMPTY_PATH_SPEC
        source_dest_cost = cu.MAX_FLOAT
        middle_success = False
        middle_path_spec = EMPTY_PATH_SPEC
        middle_cost = cu.MAX_FLOAT
        if source_destination_sets:
            source_dest_success, source_dest_path_spec, _ = yield from self.get_best_path_between_handles(interaction, sim, source_destination_sets, timeline)
            source_dest_cost = source_dest_path_spec.total_cost
        elif middle_destination_sets:
            middle_success, middle_path_spec, selected_goal = yield from self.get_best_path_between_handles(interaction, sim, source_middle_sets, timeline, path_type=(PathType.MIDDLE_LEFT))
            if middle_path_spec.is_failure_path:
                if source_dest_success:
                    return (
                     source_dest_success, source_dest_path_spec)
                return (
                 middle_success, middle_path_spec)
            if middle_success:
                geometry = create_transform_geometry(selected_goal.location.transform)
                middle_handle = selected_goal.connectivity_handle.clone(routing_surface_override=(selected_goal.routing_surface_id),
                  geometry=geometry)
                middle_handle.path = middle_path = algos.Path(middle_path_spec.path[-1:])
                middle_path.segmented_path = selected_goal.connectivity_handle.path.segmented_path
                middle_handle.var_map = middle_path.segmented_path.var_map_resolved
                selected_goal.connectivity_handle = middle_handle
                middle_handle_set = {middle_handle: (middle_path,
                                 0, middle_path_spec.var_map,
                                 None,
                                 [
                                  selected_goal],
                                 None, None)}
                for middle_dest_set in middle_destination_sets.values():
                    middle_dest_set[0] = middle_handle_set

                middle_success, best_right_path_spec, _ = yield from self.get_best_path_between_handles(interaction, sim, middle_destination_sets, timeline, path_type=(PathType.MIDDLE_RIGHT))
                if middle_success:
                    middle_path_spec = middle_path_spec.combine(best_right_path_spec)
                    middle_cost = middle_path_spec.total_cost
                if source_dest_success == middle_success:
                    if source_dest_cost <= middle_cost:
                        result_success, result_path_spec = source_dest_success, source_dest_path_spec
            else:
                result_success, result_path_spec = middle_success, middle_path_spec
        else:
            if source_dest_success:
                result_success, result_path_spec = source_dest_success, source_dest_path_spec
            else:
                result_success, result_path_spec = middle_success, middle_path_spec
        return (
         result_success, result_path_spec)
        if False:
            yield None

    def _get_best_slot(self, slot_target, slot_types, obj, location, objects_to_ignore=DEFAULT):
        runtime_slots = tuple(slot_target.get_runtime_slots_gen(slot_types=slot_types))
        if not runtime_slots:
            return
        chosen_slot = None
        closest_distance = None
        for runtime_slot in runtime_slots:
            if runtime_slot.is_valid_for_placement(obj=obj, objects_to_ignore=objects_to_ignore):
                transform = runtime_slot.transform
                slot_routing_location = routing.Location(transform.translation, transform.orientation, runtime_slot.routing_surface)
                distance = (location - slot_routing_location.position).magnitude_2d_squared()
                if closest_distance is None or distance < closest_distance:
                    chosen_slot = runtime_slot
                    closest_distance = distance

        return chosen_slot

    def _generate_surface_and_slot_targets(self, path_spec_right, path_spec_left, final_sim_routing_location, objects_to_ignore):
        slot_var = path_spec_right.var_map.get(PostureSpecVariable.SLOT)
        if slot_var is None:
            return True
        slot_target = slot_var.target
        if isinstance(slot_target, PostureSpecVariable):
            return False
        chosen_slot = self._get_best_slot(slot_target, slot_var.slot_types, slot_var.actor, final_sim_routing_location.position, objects_to_ignore)
        if chosen_slot is None:
            return False
        path_spec_right._final_constraint = path_spec_right.final_constraint.generate_constraint_with_slot_info(slot_var.actor, slot_target, chosen_slot)
        path_spec_right._spec_constraint = path_spec_right.spec_constraint.generate_constraint_with_slot_info(slot_var.actor, slot_target, chosen_slot)

        def get_frozen_manifest_entry():
            for constraint in path_spec_right.spec_constraint:
                if constraint.posture_state_spec is not None:
                    for manifest_entry in constraint.posture_state_spec.slot_manifest:
                        return manifest_entry

            raise AssertionError('Spec constraint with no manifest entries: {}'.format(path_spec_right.spec_constraint))

        frozen_manifest_entry = get_frozen_manifest_entry()

        def replace_var_map_for_path_spec(path_spec):
            for spec in path_spec.transition_specs:
                if PostureSpecVariable.SLOT in spec.var_map:
                    new_var_map = {}
                    new_var_map[PostureSpecVariable.SLOT] = frozen_manifest_entry
                    spec.var_map = frozendict(spec.var_map, new_var_map)

        replace_var_map_for_path_spec(path_spec_right)
        if path_spec_left is not None:
            replace_var_map_for_path_spec(path_spec_left)
        return True

    def _valid_vehicle_dest_handle(self, dest, cost, in_vehicle_posture):
        if not sims4.math.almost_equal(cost, 0.0):
            return False
        else:
            if len(dest.path) < 1:
                return in_vehicle_posture
            next_posture = dest.path[0].body_posture
            if next_posture is None:
                return in_vehicle_posture
            return in_vehicle_posture or next_posture.is_vehicle
        return next_posture.is_vehicle or not next_posture.mobile

    def get_best_path_between_handles--- This code section failed: ---

 L.6728         0  BUILD_LIST_0          0 
                2  STORE_FAST               'non_suppressed_source_goals'

 L.6729         4  BUILD_LIST_0          0 
                6  STORE_FAST               'non_suppressed_goals'

 L.6734         8  BUILD_LIST_0          0 
               10  STORE_FAST               'suppressed_source_goals'

 L.6735        12  BUILD_LIST_0          0 
               14  STORE_FAST               'suppressed_goals'

 L.6737        16  LOAD_FAST                'interaction'
               18  LOAD_ATTR                carry_target
               20  LOAD_CONST               None
               22  COMPARE_OP               is-not
               24  STORE_FAST               'for_carryable'

 L.6746        26  LOAD_CONST               False
               28  STORE_FAST               'carry_object_at_pool'

 L.6747        30  LOAD_FAST                'for_carryable'
               32  POP_JUMP_IF_FALSE    68  'to 68'
               34  LOAD_FAST                'interaction'
               36  LOAD_ATTR                carry_target
               38  LOAD_ATTR                routing_surface
               40  LOAD_CONST               None
               42  COMPARE_OP               is-not
               44  POP_JUMP_IF_FALSE    68  'to 68'
               46  LOAD_FAST                'interaction'
               48  LOAD_ATTR                carry_target
               50  LOAD_ATTR                routing_surface
               52  LOAD_ATTR                type
               54  LOAD_GLOBAL              routing
               56  LOAD_ATTR                SurfaceType
               58  LOAD_ATTR                SURFACETYPE_POOL
               60  COMPARE_OP               ==
               62  POP_JUMP_IF_FALSE    68  'to 68'

 L.6748        64  LOAD_CONST               True
               66  STORE_FAST               'carry_object_at_pool'
             68_0  COME_FROM            62  '62'
             68_1  COME_FROM            44  '44'
             68_2  COME_FROM            32  '32'

 L.6750        68  LOAD_FAST                'sim'
               70  LOAD_ATTR                location
               72  LOAD_ATTR                routing_surface
               74  LOAD_CONST               None
               76  COMPARE_OP               is-not
               78  POP_JUMP_IF_FALSE    90  'to 90'
               80  LOAD_FAST                'sim'
               82  LOAD_ATTR                location
               84  LOAD_ATTR                routing_surface
               86  LOAD_ATTR                type
               88  JUMP_FORWARD         92  'to 92'
             90_0  COME_FROM            78  '78'
               90  LOAD_CONST               None
             92_0  COME_FROM            88  '88'
               92  STORE_FAST               'sim_surface_type'

 L.6752        94  LOAD_CONST               None
               96  STORE_FAST               'target_reference_override'

 L.6753        98  LOAD_FAST                'interaction'
              100  LOAD_ATTR                goal_height_limit
              102  STORE_FAST               'interaction_goal_height_limit'

 L.6757       104  LOAD_FAST                'sim'
              106  LOAD_ATTR                routing_master
              108  LOAD_CONST               None
              110  COMPARE_OP               is-not
              112  POP_JUMP_IF_FALSE   140  'to 140'
              114  LOAD_FAST                'sim'
              116  LOAD_ATTR                routing_master
              118  LOAD_METHOD              get_routing_slave_data_count
              120  LOAD_GLOBAL              FormationRoutingType
              122  LOAD_ATTR                FOLLOW
              124  CALL_METHOD_1         1  '1 positional argument'
              126  POP_JUMP_IF_FALSE   140  'to 140'

 L.6760       128  LOAD_FAST                'sim'
              130  LOAD_ATTR                routing_master
              132  STORE_FAST               'target_reference_override'

 L.6761       134  LOAD_GLOBAL              FormationTuning
              136  LOAD_ATTR                GOAL_HEIGHT_LIMIT
              138  STORE_FAST               'interaction_goal_height_limit'
            140_0  COME_FROM           126  '126'
            140_1  COME_FROM           112  '112'

 L.6763   140_142  SETUP_LOOP          546  'to 546'
              144  LOAD_FAST                'source_destination_sets'
              146  LOAD_METHOD              values
              148  CALL_METHOD_0         0  '0 positional arguments'
              150  GET_ITER         
          152_154  FOR_ITER            544  'to 544'
              156  UNPACK_SEQUENCE_6     6 
              158  STORE_FAST               'source_handles'
              160  STORE_FAST               '_'
              162  STORE_FAST               '_'
              164  STORE_FAST               '_'
              166  STORE_FAST               '_'
              168  STORE_FAST               '_'

 L.6764   170_172  SETUP_LOOP          542  'to 542'
              174  LOAD_FAST                'source_handles'
              176  GET_ITER         
          178_180  FOR_ITER            540  'to 540'
              182  STORE_FAST               'source_handle'

 L.6765       184  LOAD_FAST                'source_handle'
              186  LOAD_GLOBAL              DEFAULT
              188  COMPARE_OP               is
              190  POP_JUMP_IF_FALSE   196  'to 196'

 L.6766       192  LOAD_GLOBAL              AssertionError
              194  RAISE_VARARGS_1       1  'exception instance'
            196_0  COME_FROM           190  '190'

 L.6767       196  LOAD_FAST                'source_handles'
              198  LOAD_FAST                'source_handle'
              200  BINARY_SUBSCR    
              202  LOAD_CONST               1
              204  BINARY_SUBSCR    
              206  STORE_FAST               'path_cost'

 L.6769       208  LOAD_FAST                'source_handle'
              210  LOAD_ATTR                get_goals
              212  LOAD_FAST                'source_handle'
              214  LOAD_ATTR                target
              216  LOAD_FAST                'for_carryable'
              218  LOAD_CONST               True
              220  LOAD_CONST               ('relative_object', 'for_carryable', 'for_source')
              222  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              224  STORE_FAST               'source_goals'

 L.6771       226  LOAD_CONST               True
              228  STORE_FAST               'same_interaction_source_target'

 L.6772       230  LOAD_FAST                'interaction'
              232  LOAD_ATTR                target
              234  LOAD_CONST               None
              236  COMPARE_OP               is-not
          238_240  POP_JUMP_IF_FALSE   276  'to 276'
              242  LOAD_FAST                'source_handle'
              244  LOAD_ATTR                target
              246  LOAD_CONST               None
              248  COMPARE_OP               is-not
          250_252  POP_JUMP_IF_FALSE   276  'to 276'
              254  LOAD_FAST                'interaction'
              256  LOAD_ATTR                target
              258  LOAD_ATTR                id
              260  LOAD_FAST                'source_handle'
              262  LOAD_ATTR                target
              264  LOAD_ATTR                id
              266  COMPARE_OP               !=
          268_270  POP_JUMP_IF_FALSE   276  'to 276'

 L.6779       272  LOAD_CONST               False
              274  STORE_FAST               'same_interaction_source_target'
            276_0  COME_FROM           268  '268'
            276_1  COME_FROM           250  '250'
            276_2  COME_FROM           238  '238'

 L.6780   276_278  SETUP_LOOP          538  'to 538'
              280  LOAD_FAST                'source_goals'
              282  GET_ITER         
              284  FOR_ITER            536  'to 536'
              286  STORE_FAST               'source_goal'

 L.6781       288  LOAD_CONST               True
              290  STORE_FAST               'source_is_valid'

 L.6783       292  LOAD_FAST                'path_type'
              294  LOAD_GLOBAL              PathType
              296  LOAD_ATTR                MIDDLE_RIGHT
              298  COMPARE_OP               !=
          300_302  POP_JUMP_IF_FALSE   370  'to 370'

 L.6784       304  LOAD_FAST                'same_interaction_source_target'
          306_308  POP_JUMP_IF_FALSE   370  'to 370'

 L.6785       310  LOAD_FAST                'sim_surface_type'
              312  LOAD_CONST               None
              314  COMPARE_OP               is-not
          316_318  POP_JUMP_IF_FALSE   370  'to 370'

 L.6786       320  LOAD_FAST                'sim_surface_type'
              322  LOAD_GLOBAL              routing
              324  LOAD_ATTR                SurfaceType
              326  LOAD_ATTR                SURFACETYPE_POOL
              328  COMPARE_OP               !=
          330_332  POP_JUMP_IF_FALSE   370  'to 370'

 L.6787       334  LOAD_FAST                'source_goal'
              336  LOAD_ATTR                routing_surface_id
              338  LOAD_ATTR                type
              340  LOAD_GLOBAL              routing
              342  LOAD_ATTR                SurfaceType
              344  LOAD_ATTR                SURFACETYPE_POOL
              346  COMPARE_OP               !=
          348_350  POP_JUMP_IF_FALSE   370  'to 370'

 L.6788       352  LOAD_FAST                'sim_surface_type'
              354  LOAD_FAST                'source_goal'
              356  LOAD_ATTR                routing_surface_id
              358  LOAD_ATTR                type
              360  COMPARE_OP               !=
          362_364  POP_JUMP_IF_FALSE   370  'to 370'

 L.6802   366_368  CONTINUE            284  'to 284'
            370_0  COME_FROM           362  '362'
            370_1  COME_FROM           348  '348'
            370_2  COME_FROM           330  '330'
            370_3  COME_FROM           316  '316'
            370_4  COME_FROM           306  '306'
            370_5  COME_FROM           300  '300'

 L.6804       370  LOAD_FAST                'source_goal'
              372  LOAD_ATTR                requires_los_check
          374_376  POP_JUMP_IF_FALSE   498  'to 498'

 L.6805       378  LOAD_FAST                'source_handle'
              380  LOAD_ATTR                target
              382  LOAD_CONST               None
              384  COMPARE_OP               is-not
          386_388  POP_JUMP_IF_FALSE   498  'to 498'
              390  LOAD_FAST                'source_handle'
              392  LOAD_ATTR                target
              394  LOAD_ATTR                is_sim
          396_398  POP_JUMP_IF_TRUE    498  'to 498'

 L.6806       400  LOAD_FAST                'source_goal'
              402  LOAD_ATTR                location
              404  LOAD_ATTR                routing_surface
              406  STORE_FAST               'goal_routing_surface'

 L.6807       408  LOAD_FAST                'source_goal'
              410  LOAD_ATTR                location
              412  LOAD_ATTR                transform
              414  STORE_FAST               'goal_transform'

 L.6808       416  LOAD_GLOBAL              routing
              418  LOAD_METHOD              test_point_placement_in_navmesh
              420  LOAD_FAST                'goal_routing_surface'
              422  LOAD_FAST                'goal_transform'
              424  LOAD_ATTR                translation
              426  CALL_METHOD_2         2  '2 positional arguments'
          428_430  POP_JUMP_IF_FALSE   494  'to 494'

 L.6809       432  LOAD_FAST                'sim'
              434  LOAD_METHOD              validate_location
              436  LOAD_GLOBAL              sims4
              438  LOAD_ATTR                math
              440  LOAD_METHOD              Location
              442  LOAD_FAST                'goal_transform'
              444  LOAD_FAST                'goal_routing_surface'
              446  CALL_METHOD_2         2  '2 positional arguments'
              448  CALL_METHOD_1         1  '1 positional argument'
          450_452  POP_JUMP_IF_FALSE   494  'to 494'

 L.6810       454  LOAD_FAST                'source_handle'
              456  LOAD_ATTR                target
              458  LOAD_ATTR                check_line_of_sight
              460  LOAD_FAST                'goal_transform'

 L.6811       462  LOAD_CONST               True
              464  LOAD_FAST                'for_carryable'
              466  LOAD_CONST               ('verbose', 'for_carryable')
              468  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              470  UNPACK_SEQUENCE_2     2 
              472  STORE_FAST               'result'
              474  STORE_FAST               '_'

 L.6812       476  LOAD_FAST                'result'
              478  LOAD_GLOBAL              routing
              480  LOAD_ATTR                RAYCAST_HIT_TYPE_NONE
              482  COMPARE_OP               !=
          484_486  POP_JUMP_IF_FALSE   498  'to 498'

 L.6813       488  LOAD_CONST               False
              490  STORE_FAST               'source_is_valid'
              492  JUMP_FORWARD        498  'to 498'
            494_0  COME_FROM           450  '450'
            494_1  COME_FROM           428  '428'

 L.6815       494  LOAD_CONST               False
              496  STORE_FAST               'source_is_valid'
            498_0  COME_FROM           492  '492'
            498_1  COME_FROM           484  '484'
            498_2  COME_FROM           396  '396'
            498_3  COME_FROM           386  '386'
            498_4  COME_FROM           374  '374'

 L.6817       498  LOAD_FAST                'path_cost'
              500  LOAD_FAST                'source_goal'
              502  STORE_ATTR               path_cost

 L.6819       504  LOAD_FAST                'source_is_valid'
          506_508  POP_JUMP_IF_FALSE   522  'to 522'

 L.6820       510  LOAD_FAST                'non_suppressed_source_goals'
              512  LOAD_METHOD              append
              514  LOAD_FAST                'source_goal'
              516  CALL_METHOD_1         1  '1 positional argument'
              518  POP_TOP          
              520  JUMP_BACK           284  'to 284'
            522_0  COME_FROM           506  '506'

 L.6822       522  LOAD_FAST                'suppressed_source_goals'
              524  LOAD_METHOD              append
              526  LOAD_FAST                'source_goal'
              528  CALL_METHOD_1         1  '1 positional argument'
              530  POP_TOP          
          532_534  JUMP_BACK           284  'to 284'
              536  POP_BLOCK        
            538_0  COME_FROM_LOOP      276  '276'
              538  JUMP_BACK           178  'to 178'
              540  POP_BLOCK        
            542_0  COME_FROM_LOOP      170  '170'
              542  JUMP_BACK           152  'to 152'
              544  POP_BLOCK        
            546_0  COME_FROM_LOOP      140  '140'

 L.6827       546  LOAD_FAST                'sim'
              548  LOAD_ATTR                routing_context
              550  STORE_FAST               'routing_context'

 L.6828       552  LOAD_FAST                'interaction'
              554  LOAD_METHOD              min_height_clearance
              556  LOAD_FAST                'routing_context'
              558  CALL_METHOD_1         1  '1 positional argument'
              560  STORE_FAST               'required_height_clearance'

 L.6829       562  LOAD_FAST                'sim'
              564  STORE_FAST               'routing_agent'

 L.6830       566  LOAD_FAST                'sim'
              568  LOAD_ATTR                posture
              570  LOAD_ATTR                target
              572  STORE_FAST               'current_posture_target'

 L.6831       574  LOAD_FAST                'current_posture_target'
              576  LOAD_CONST               None
              578  COMPARE_OP               is
          580_582  POP_JUMP_IF_FALSE   588  'to 588'
              584  LOAD_CONST               False
              586  JUMP_FORWARD        596  'to 596'
            588_0  COME_FROM           580  '580'
              588  LOAD_FAST                'current_posture_target'
              590  LOAD_ATTR                vehicle_component
              592  LOAD_CONST               None
              594  COMPARE_OP               is-not
            596_0  COME_FROM           586  '586'
              596  STORE_FAST               'in_vehicle'

 L.6832       598  LOAD_FAST                'sim'
              600  LOAD_ATTR                posture
              602  LOAD_ATTR                is_vehicle
              604  STORE_DEREF              'in_vehicle_posture'

 L.6833       606  LOAD_CONST               False
              608  STORE_FAST               'force_vehicle_route'

 L.6834       610  BUILD_LIST_0          0 
              612  STORE_FAST               'vehicle_dest_handles'

 L.6835       614  LOAD_FAST                'in_vehicle'
          616_618  POP_JUMP_IF_TRUE    624  'to 624'
              620  LOAD_CONST               None
              622  JUMP_FORWARD        626  'to 626'
            624_0  COME_FROM           616  '616'
              624  LOAD_FAST                'current_posture_target'
            626_0  COME_FROM           622  '622'
              626  STORE_FAST               'vehicle'

 L.6836       628  LOAD_FAST                'vehicle'
              630  LOAD_CONST               None
              632  COMPARE_OP               is-not
          634_636  POP_JUMP_IF_FALSE   894  'to 894'
              638  LOAD_FAST                'vehicle'
              640  LOAD_ATTR                vehicle_component
              642  LOAD_CONST               None
              644  COMPARE_OP               is-not
          646_648  POP_JUMP_IF_FALSE   894  'to 894'

 L.6839       650  LOAD_FAST                'vehicle'
              652  LOAD_ATTR                routing_component
              654  LOAD_ATTR                pathplan_context
              656  STORE_FAST               'vehicle_pathplan_context'

 L.6840       658  LOAD_CONST               None
              660  STORE_FAST               'connectivity'

 L.6841       662  LOAD_FAST                'non_suppressed_source_goals'
              664  STORE_FAST               'vehicle_source_goals'

 L.6842       666  LOAD_FAST                'non_suppressed_source_goals'
          668_670  POP_JUMP_IF_FALSE   680  'to 680'
              672  LOAD_FAST                'non_suppressed_source_goals'
              674  LOAD_CONST               0
              676  BINARY_SUBSCR    
              678  JUMP_FORWARD        682  'to 682'
            680_0  COME_FROM           668  '668'
              680  LOAD_CONST               None
            682_0  COME_FROM           678  '678'
              682  STORE_FAST               'source_goal'

 L.6843       684  LOAD_FAST                'source_goal'
              686  LOAD_CONST               None
              688  COMPARE_OP               is
          690_692  POP_JUMP_IF_FALSE   716  'to 716'

 L.6846       694  LOAD_FAST                'suppressed_source_goals'
              696  STORE_FAST               'vehicle_source_goals'

 L.6847       698  LOAD_FAST                'suppressed_source_goals'
          700_702  POP_JUMP_IF_FALSE   712  'to 712'
              704  LOAD_FAST                'suppressed_source_goals'
              706  LOAD_CONST               0
              708  BINARY_SUBSCR    
              710  JUMP_FORWARD        714  'to 714'
            712_0  COME_FROM           700  '700'
              712  LOAD_CONST               None
            714_0  COME_FROM           710  '710'
              714  STORE_FAST               'source_goal'
            716_0  COME_FROM           690  '690'

 L.6848       716  LOAD_FAST                'source_goal'
              718  LOAD_CONST               None
              720  COMPARE_OP               is-not
          722_724  POP_JUMP_IF_FALSE   814  'to 814'

 L.6849       726  BUILD_LIST_0          0 
              728  STORE_FAST               'dest_handles'

 L.6850       730  SETUP_LOOP          786  'to 786'
              732  LOAD_FAST                'source_destination_sets'
              734  LOAD_METHOD              values
              736  CALL_METHOD_0         0  '0 positional arguments'
              738  GET_ITER         
              740  FOR_ITER            784  'to 784'
              742  UNPACK_SEQUENCE_6     6 
              744  STORE_FAST               '_'
              746  STORE_FAST               'destination_handles'
              748  STORE_FAST               '_'
              750  STORE_FAST               '_'
              752  STORE_FAST               '_'
              754  STORE_FAST               '_'

 L.6851       756  LOAD_FAST                'dest_handles'
              758  LOAD_METHOD              extend
              760  LOAD_LISTCOMP            '<code_object <listcomp>>'
              762  LOAD_STR                 'PostureGraphService.get_best_path_between_handles.<locals>.<listcomp>'
              764  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              766  LOAD_FAST                'destination_handles'
              768  LOAD_METHOD              keys
              770  CALL_METHOD_0         0  '0 positional arguments'
              772  GET_ITER         
              774  CALL_FUNCTION_1       1  '1 positional argument'
              776  CALL_METHOD_1         1  '1 positional argument'
              778  POP_TOP          
          780_782  JUMP_BACK           740  'to 740'
              784  POP_BLOCK        
            786_0  COME_FROM_LOOP      730  '730'

 L.6852       786  LOAD_FAST                'dest_handles'
          788_790  POP_JUMP_IF_FALSE   814  'to 814'

 L.6853       792  LOAD_GLOBAL              routing
              794  LOAD_ATTR                test_connectivity_batch
              796  LOAD_FAST                'source_goal'
              798  LOAD_ATTR                connectivity_handle
              800  BUILD_TUPLE_1         1 
              802  LOAD_FAST                'dest_handles'

 L.6854       804  LOAD_FAST                'vehicle_pathplan_context'

 L.6855       806  LOAD_CONST               True
              808  LOAD_CONST               ('routing_context', 'compute_cost')
              810  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              812  STORE_FAST               'connectivity'
            814_0  COME_FROM           788  '788'
            814_1  COME_FROM           722  '722'

 L.6856       814  LOAD_FAST                'connectivity'
              816  LOAD_CONST               None
              818  COMPARE_OP               is-not
          820_822  POP_JUMP_IF_FALSE   894  'to 894'

 L.6857       824  LOAD_CLOSURE             'in_vehicle_posture'
              826  LOAD_CLOSURE             'self'
              828  BUILD_TUPLE_2         2 
              830  LOAD_SETCOMP             '<code_object <setcomp>>'
              832  LOAD_STR                 'PostureGraphService.get_best_path_between_handles.<locals>.<setcomp>'
              834  MAKE_FUNCTION_8          'closure'
              836  LOAD_FAST                'connectivity'
              838  GET_ITER         
              840  CALL_FUNCTION_1       1  '1 positional argument'
              842  STORE_FAST               'vehicle_dest_handles'

 L.6858       844  LOAD_FAST                'vehicle_dest_handles'
          846_848  POP_JUMP_IF_FALSE   894  'to 894'

 L.6859       850  LOAD_CONST               True
              852  STORE_FAST               'force_vehicle_route'

 L.6862       854  LOAD_FAST                'vehicle'
              856  STORE_FAST               'routing_agent'

 L.6863       858  LOAD_FAST                'vehicle_pathplan_context'
              860  STORE_FAST               'routing_context'

 L.6865       862  SETUP_LOOP          894  'to 894'
              864  LOAD_FAST                'vehicle_source_goals'
              866  GET_ITER         
              868  FOR_ITER            892  'to 892'
              870  STORE_FAST               'goal'

 L.6866       872  LOAD_FAST                'goal'
              874  LOAD_ATTR                connectivity_handle
              876  LOAD_ATTR                clone
              878  LOAD_FAST                'vehicle'
              880  LOAD_CONST               ('sim',)
              882  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              884  LOAD_FAST                'goal'
              886  STORE_ATTR               connectivity_handle
          888_890  JUMP_BACK           868  'to 868'
              892  POP_BLOCK        
            894_0  COME_FROM_LOOP      862  '862'
            894_1  COME_FROM           846  '846'
            894_2  COME_FROM           820  '820'
            894_3  COME_FROM           646  '646'
            894_4  COME_FROM           634  '634'

 L.6870       894  LOAD_FAST                'path_type'
              896  LOAD_CONST               None
              898  COMPARE_OP               is-not
          900_902  JUMP_IF_FALSE_OR_POP   912  'to 912'
              904  LOAD_FAST                'path_type'
              906  LOAD_GLOBAL              PathType
              908  LOAD_ATTR                MIDDLE_LEFT
              910  COMPARE_OP               ==
            912_0  COME_FROM           900  '900'
              912  STORE_FAST               'middle_path_pickup'

 L.6872   914_916  SETUP_LOOP         1596  'to 1596'
              918  LOAD_FAST                'source_destination_sets'
              920  LOAD_METHOD              values
              922  CALL_METHOD_0         0  '0 positional arguments'
              924  GET_ITER         
          926_928  FOR_ITER           1594  'to 1594'
              930  UNPACK_SEQUENCE_6     6 
              932  STORE_FAST               '_'
              934  STORE_FAST               'destination_handles'
              936  STORE_FAST               '_'
              938  STORE_FAST               '_'
              940  STORE_FAST               '_'
              942  STORE_FAST               '_'

 L.6873   944_946  SETUP_LOOP         1590  'to 1590'
              948  LOAD_FAST                'destination_handles'
              950  LOAD_METHOD              items
              952  CALL_METHOD_0         0  '0 positional arguments'
              954  GET_ITER         
          956_958  FOR_ITER           1588  'to 1588'
              960  UNPACK_SEQUENCE_2     2 
              962  STORE_FAST               'destination_handle'
              964  UNPACK_SEQUENCE_7     7 
              966  STORE_FAST               'right_path'
              968  STORE_FAST               'path_cost'
              970  STORE_FAST               'var_map'
              972  STORE_FAST               'dest_spec'
              974  STORE_FAST               '_'
              976  STORE_FAST               '_'
              978  STORE_FAST               '_'

 L.6874       980  BUILD_LIST_0          0 
              982  STORE_FAST               'additional_dest_handles'

 L.6875       984  LOAD_FAST                'destination_handle'
              986  LOAD_GLOBAL              DEFAULT
              988  COMPARE_OP               is
          990_992  POP_JUMP_IF_FALSE  1060  'to 1060'

 L.6876       994  SETUP_LOOP         1102  'to 1102'
              996  LOAD_FAST                'source_destination_sets'
              998  LOAD_METHOD              values
             1000  CALL_METHOD_0         0  '0 positional arguments'
             1002  GET_ITER         
             1004  FOR_ITER           1056  'to 1056'
             1006  UNPACK_EX_1+0           
             1008  STORE_FAST               'source_handles'
             1010  STORE_FAST               '_'

 L.6877      1012  SETUP_LOOP         1052  'to 1052'
             1014  LOAD_FAST                'source_handles'
             1016  GET_ITER         
             1018  FOR_ITER           1050  'to 1050'
             1020  STORE_FAST               'source_handle'

 L.6878      1022  LOAD_FAST                'source_handle'
             1024  LOAD_METHOD              clone
             1026  CALL_METHOD_0         0  '0 positional arguments'
             1028  STORE_FAST               'destination_handle'

 L.6879      1030  LOAD_FAST                'right_path'
             1032  LOAD_FAST                'destination_handle'
             1034  STORE_ATTR               path

 L.6880      1036  LOAD_FAST                'additional_dest_handles'
             1038  LOAD_METHOD              append
             1040  LOAD_FAST                'destination_handle'
             1042  CALL_METHOD_1         1  '1 positional argument'
             1044  POP_TOP          
         1046_1048  JUMP_BACK          1018  'to 1018'
             1050  POP_BLOCK        
           1052_0  COME_FROM_LOOP     1012  '1012'
         1052_1054  JUMP_BACK          1004  'to 1004'
             1056  POP_BLOCK        
             1058  JUMP_FORWARD       1102  'to 1102'
           1060_0  COME_FROM           990  '990'

 L.6881      1060  LOAD_FAST                'force_vehicle_route'
         1062_1064  POP_JUMP_IF_FALSE  1096  'to 1096'

 L.6884      1066  LOAD_FAST                'destination_handle'
             1068  LOAD_FAST                'vehicle_dest_handles'
             1070  COMPARE_OP               in
         1072_1074  POP_JUMP_IF_FALSE  1102  'to 1102'

 L.6887      1076  LOAD_FAST                'destination_handle'
             1078  LOAD_ATTR                clone
             1080  LOAD_FAST                'routing_agent'
             1082  LOAD_CONST               ('sim',)
             1084  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
             1086  STORE_FAST               'destination_handle'

 L.6888      1088  LOAD_FAST                'destination_handle'
             1090  BUILD_LIST_1          1 
             1092  STORE_FAST               'additional_dest_handles'
             1094  JUMP_FORWARD       1102  'to 1102'
           1096_0  COME_FROM          1062  '1062'

 L.6890      1096  LOAD_FAST                'destination_handle'
             1098  BUILD_LIST_1          1 
             1100  STORE_FAST               'additional_dest_handles'
           1102_0  COME_FROM          1094  '1094'
           1102_1  COME_FROM          1072  '1072'
           1102_2  COME_FROM          1058  '1058'
           1102_3  COME_FROM_LOOP      994  '994'

 L.6892  1102_1104  SETUP_LOOP         1584  'to 1584'
             1106  LOAD_FAST                'additional_dest_handles'
             1108  GET_ITER         
         1110_1112  FOR_ITER           1582  'to 1582'
             1114  STORE_FAST               'dest_handle'

 L.6895      1116  LOAD_FAST                'interaction_goal_height_limit'
             1118  STORE_FAST               'height_limit'

 L.6896      1120  LOAD_FAST                'target_reference_override'
             1122  LOAD_CONST               None
             1124  COMPARE_OP               is
         1126_1128  POP_JUMP_IF_FALSE  1148  'to 1148'
             1130  LOAD_FAST                'interaction'
             1132  LOAD_ATTR                carry_target
             1134  LOAD_FAST                'dest_handle'
             1136  LOAD_ATTR                target
             1138  COMPARE_OP               is
         1140_1142  POP_JUMP_IF_FALSE  1148  'to 1148'

 L.6897      1144  LOAD_CONST               None
             1146  STORE_FAST               'height_limit'
           1148_0  COME_FROM          1140  '1140'
           1148_1  COME_FROM          1126  '1126'

 L.6898      1148  LOAD_FAST                'dest_handle'
             1150  LOAD_ATTR                get_goals
             1152  LOAD_FAST                'dest_handle'
             1154  LOAD_ATTR                target

 L.6899      1156  LOAD_FAST                'for_carryable'

 L.6900      1158  LOAD_FAST                'height_limit'

 L.6901      1160  LOAD_FAST                'target_reference_override'

 L.6902      1162  LOAD_CONST               False
             1164  LOAD_CONST               ('relative_object', 'for_carryable', 'goal_height_limit', 'target_reference_override', 'check_height_clearance')
             1166  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
             1168  STORE_FAST               'dest_goals'

 L.6904      1170  LOAD_FAST                'dest_handle'
             1172  LOAD_ATTR                target
             1174  LOAD_CONST               None
             1176  COMPARE_OP               is-not
         1178_1180  JUMP_IF_FALSE_OR_POP  1198  'to 1198'
             1182  LOAD_FAST                'dest_handle'
             1184  LOAD_ATTR                constraint
             1186  LOAD_ATTR                restricted_on_slope
         1188_1190  JUMP_IF_FALSE_OR_POP  1198  'to 1198'

 L.6905      1192  LOAD_FAST                'interaction'
             1194  LOAD_ATTR                ignore_slope_restrictions
             1196  UNARY_NOT        
           1198_0  COME_FROM          1188  '1188'
           1198_1  COME_FROM          1178  '1178'
             1198  STORE_FAST               'slope_restricted'

 L.6906  1200_1202  SETUP_LOOP         1578  'to 1578'
             1204  LOAD_FAST                'dest_goals'
             1206  GET_ITER         
         1208_1210  FOR_ITER           1576  'to 1576'
             1212  STORE_FAST               'dest_goal'

 L.6907      1214  LOAD_FAST                'middle_path_pickup'
         1216_1218  POP_JUMP_IF_FALSE  1248  'to 1248'
             1220  LOAD_FAST                'carry_object_at_pool'
         1222_1224  POP_JUMP_IF_FALSE  1248  'to 1248'

 L.6908      1226  LOAD_FAST                'dest_goal'
             1228  LOAD_ATTR                routing_surface_id
             1230  LOAD_ATTR                type
             1232  LOAD_GLOBAL              routing
             1234  LOAD_ATTR                SurfaceType
             1236  LOAD_ATTR                SURFACETYPE_POOL
             1238  COMPARE_OP               !=
         1240_1242  POP_JUMP_IF_FALSE  1248  'to 1248'

 L.6916  1244_1246  CONTINUE           1208  'to 1208'
           1248_0  COME_FROM          1240  '1240'
           1248_1  COME_FROM          1222  '1222'
           1248_2  COME_FROM          1216  '1216'

 L.6917      1248  LOAD_CONST               True
             1250  STORE_FAST               'dest_is_valid'

 L.6918      1252  LOAD_FAST                'path_cost'
             1254  LOAD_FAST                'dest_goal'
             1256  STORE_ATTR               path_cost

 L.6927      1258  LOAD_FAST                'slope_restricted'
         1260_1262  POP_JUMP_IF_FALSE  1380  'to 1380'
             1264  LOAD_FAST                'dest_goal'
             1266  LOAD_ATTR                routing_surface_id
             1268  LOAD_ATTR                type
             1270  LOAD_GLOBAL              routing
             1272  LOAD_ATTR                SurfaceType
             1274  LOAD_ATTR                SURFACETYPE_WORLD
             1276  COMPARE_OP               ==
         1278_1280  POP_JUMP_IF_FALSE  1380  'to 1380'

 L.6928      1282  LOAD_FAST                'dest_goal'
             1284  LOAD_ATTR                position
             1286  LOAD_ATTR                y
             1288  LOAD_GLOBAL              routing_constants
             1290  LOAD_ATTR                INVALID_TERRAIN_HEIGHT
             1292  COMPARE_OP               !=
         1294_1296  POP_JUMP_IF_FALSE  1380  'to 1380'

 L.6932      1298  LOAD_FAST                'dest_handle'
             1300  LOAD_ATTR                target
             1302  LOAD_METHOD              get_parenting_root
             1304  CALL_METHOD_0         0  '0 positional arguments'
             1306  STORE_FAST               'positional_target'

 L.6933      1308  LOAD_FAST                'positional_target'
             1310  LOAD_ATTR                is_part
         1312_1314  POP_JUMP_IF_FALSE  1324  'to 1324'
             1316  LOAD_FAST                'positional_target'
             1318  LOAD_ATTR                part_owner
             1320  LOAD_ATTR                position
             1322  JUMP_FORWARD       1328  'to 1328'
           1324_0  COME_FROM          1312  '1312'
             1324  LOAD_FAST                'positional_target'
             1326  LOAD_ATTR                position
           1328_0  COME_FROM          1322  '1322'
             1328  STORE_FAST               'target_position'

 L.6934      1330  LOAD_GLOBAL              abs
             1332  LOAD_FAST                'target_position'
             1334  LOAD_ATTR                y
             1336  LOAD_FAST                'dest_goal'
             1338  LOAD_ATTR                position
             1340  LOAD_ATTR                y
             1342  BINARY_SUBTRACT  
             1344  CALL_FUNCTION_1       1  '1 positional argument'
             1346  STORE_FAST               'height_difference'

 L.6935      1348  LOAD_FAST                'height_difference'
             1350  LOAD_GLOBAL              PostureTuning
             1352  LOAD_ATTR                CONSTRAINT_HEIGHT_TOLERANCE
             1354  COMPARE_OP               >
         1356_1358  POP_JUMP_IF_FALSE  1380  'to 1380'

 L.6936      1360  LOAD_GLOBAL              set_transition_failure_reason
             1362  LOAD_FAST                'sim'
             1364  LOAD_GLOBAL              TransitionFailureReasons
             1366  LOAD_ATTR                GOAL_ON_SLOPE
             1368  CALL_FUNCTION_2       2  '2 positional arguments'
             1370  POP_TOP          

 L.6937      1372  LOAD_CONST               False
             1374  STORE_FAST               'dest_is_valid'

 L.6938  1376_1378  CONTINUE           1208  'to 1208'
           1380_0  COME_FROM          1356  '1356'
           1380_1  COME_FROM          1294  '1294'
           1380_2  COME_FROM          1278  '1278'
           1380_3  COME_FROM          1260  '1260'

 L.6942      1380  LOAD_FAST                'required_height_clearance'
             1382  LOAD_FAST                'dest_goal'
             1384  LOAD_ATTR                height_clearance
             1386  COMPARE_OP               >
         1388_1390  POP_JUMP_IF_FALSE  1412  'to 1412'

 L.6943      1392  LOAD_GLOBAL              set_transition_failure_reason
             1394  LOAD_FAST                'sim'
             1396  LOAD_GLOBAL              TransitionFailureReasons
             1398  LOAD_ATTR                INSUFFICIENT_HEAD_CLEARANCE
             1400  CALL_FUNCTION_2       2  '2 positional arguments'
             1402  POP_TOP          

 L.6944      1404  LOAD_CONST               False
             1406  STORE_FAST               'dest_is_valid'

 L.6945  1408_1410  CONTINUE           1208  'to 1208'
           1412_0  COME_FROM          1388  '1388'

 L.6951      1412  LOAD_FAST                'dest_goal'
             1414  LOAD_ATTR                requires_los_check
         1416_1418  POP_JUMP_IF_FALSE  1544  'to 1544'

 L.6952      1420  LOAD_FAST                'dest_handle'
             1422  LOAD_ATTR                target
             1424  LOAD_CONST               None
             1426  COMPARE_OP               is-not
         1428_1430  POP_JUMP_IF_FALSE  1544  'to 1544'
             1432  LOAD_FAST                'dest_handle'
             1434  LOAD_ATTR                target
             1436  LOAD_ATTR                is_sim
         1438_1440  POP_JUMP_IF_TRUE   1544  'to 1544'

 L.6953      1442  LOAD_FAST                'in_vehicle'
         1444_1446  POP_JUMP_IF_FALSE  1460  'to 1460'
             1448  LOAD_FAST                'current_posture_target'
             1450  LOAD_FAST                'dest_handle'
             1452  LOAD_ATTR                target
             1454  COMPARE_OP               is
         1456_1458  POP_JUMP_IF_TRUE   1544  'to 1544'
           1460_0  COME_FROM          1444  '1444'

 L.6954      1460  LOAD_FAST                'dest_handle'
             1462  LOAD_ATTR                target
             1464  LOAD_ATTR                check_line_of_sight
             1466  LOAD_FAST                'dest_goal'
             1468  LOAD_ATTR                location
             1470  LOAD_ATTR                transform

 L.6955      1472  LOAD_CONST               True
             1474  LOAD_FAST                'for_carryable'

 L.6956      1476  LOAD_CONST               True
             1478  LOAD_CONST               ('verbose', 'for_carryable', 'use_standard_ignored_objects')
             1480  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
             1482  UNPACK_SEQUENCE_2     2 
             1484  STORE_FAST               'result'
             1486  STORE_FAST               'blocking_obj_id'

 L.6960      1488  LOAD_FAST                'result'
             1490  LOAD_GLOBAL              routing
             1492  LOAD_ATTR                RAYCAST_HIT_TYPE_IMPASSABLE
             1494  COMPARE_OP               ==
         1496_1498  POP_JUMP_IF_FALSE  1512  'to 1512'
             1500  LOAD_FAST                'blocking_obj_id'
             1502  LOAD_CONST               0
             1504  COMPARE_OP               ==
         1506_1508  POP_JUMP_IF_FALSE  1512  'to 1512'

 L.6961      1510  JUMP_FORWARD       1544  'to 1544'
           1512_0  COME_FROM          1506  '1506'
           1512_1  COME_FROM          1496  '1496'

 L.6962      1512  LOAD_FAST                'result'
             1514  LOAD_GLOBAL              routing
             1516  LOAD_ATTR                RAYCAST_HIT_TYPE_NONE
             1518  COMPARE_OP               !=
         1520_1522  POP_JUMP_IF_FALSE  1544  'to 1544'

 L.6964      1524  LOAD_GLOBAL              set_transition_failure_reason
             1526  LOAD_FAST                'sim'
             1528  LOAD_GLOBAL              TransitionFailureReasons
             1530  LOAD_ATTR                BLOCKING_OBJECT
             1532  LOAD_FAST                'blocking_obj_id'
             1534  LOAD_CONST               ('target_id',)
             1536  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
             1538  POP_TOP          

 L.6965      1540  LOAD_CONST               False
             1542  STORE_FAST               'dest_is_valid'
           1544_0  COME_FROM          1520  '1520'
           1544_1  COME_FROM          1510  '1510'
           1544_2  COME_FROM          1456  '1456'
           1544_3  COME_FROM          1438  '1438'
           1544_4  COME_FROM          1428  '1428'
           1544_5  COME_FROM          1416  '1416'

 L.6967      1544  LOAD_FAST                'dest_is_valid'
         1546_1548  POP_JUMP_IF_FALSE  1562  'to 1562'

 L.6968      1550  LOAD_FAST                'non_suppressed_goals'
             1552  LOAD_METHOD              append
             1554  LOAD_FAST                'dest_goal'
             1556  CALL_METHOD_1         1  '1 positional argument'
             1558  POP_TOP          
             1560  JUMP_BACK          1208  'to 1208'
           1562_0  COME_FROM          1546  '1546'

 L.6970      1562  LOAD_FAST                'suppressed_goals'
             1564  LOAD_METHOD              append
             1566  LOAD_FAST                'dest_goal'
             1568  CALL_METHOD_1         1  '1 positional argument'
             1570  POP_TOP          
         1572_1574  JUMP_BACK          1208  'to 1208'
             1576  POP_BLOCK        
           1578_0  COME_FROM_LOOP     1200  '1200'
         1578_1580  JUMP_BACK          1110  'to 1110'
             1582  POP_BLOCK        
           1584_0  COME_FROM_LOOP     1102  '1102'
         1584_1586  JUMP_BACK           956  'to 956'
             1588  POP_BLOCK        
           1590_0  COME_FROM_LOOP      944  '944'
         1590_1592  JUMP_BACK           926  'to 926'
             1594  POP_BLOCK        
           1596_0  COME_FROM_LOOP      914  '914'

 L.6972      1596  LOAD_FAST                'non_suppressed_source_goals'
         1598_1600  POP_JUMP_IF_TRUE   1606  'to 1606'

 L.6977      1602  LOAD_FAST                'suppressed_source_goals'
             1604  STORE_FAST               'non_suppressed_source_goals'
           1606_0  COME_FROM          1598  '1598'

 L.6978      1606  LOAD_FAST                'non_suppressed_source_goals'
             1608  STORE_FAST               'all_source_goals'

 L.6979      1610  LOAD_FAST                'non_suppressed_goals'
         1612_1614  JUMP_IF_TRUE_OR_POP  1618  'to 1618'
             1616  LOAD_FAST                'suppressed_goals'
           1618_0  COME_FROM          1612  '1612'
             1618  STORE_FAST               'all_dest_goals'

 L.6981      1620  LOAD_FAST                'all_source_goals'
         1622_1624  POP_JUMP_IF_FALSE  1632  'to 1632'
             1626  LOAD_FAST                'all_dest_goals'
         1628_1630  POP_JUMP_IF_TRUE   1668  'to 1668'
           1632_0  COME_FROM          1622  '1622'

 L.6982      1632  LOAD_DEREF               'self'
             1634  LOAD_ATTR                _get_failure_path_spec_gen
             1636  LOAD_FAST                'timeline'
             1638  LOAD_FAST                'sim'
             1640  LOAD_FAST                'source_destination_sets'
             1642  LOAD_FAST                'interaction'
             1644  LOAD_FAST                'path_type'
             1646  LOAD_CONST               ('interaction', 'failed_path_type')
             1648  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
             1650  GET_YIELD_FROM_ITER
             1652  LOAD_CONST               None
             1654  YIELD_FROM       
             1656  STORE_FAST               'failure_path'

 L.6983      1658  LOAD_CONST               False
             1660  LOAD_FAST                'failure_path'
             1662  LOAD_CONST               None
             1664  BUILD_TUPLE_3         3 
             1666  RETURN_VALUE     
           1668_0  COME_FROM          1628  '1628'

 L.6986      1668  SETUP_LOOP         1708  'to 1708'
             1670  LOAD_GLOBAL              itertools
             1672  LOAD_METHOD              chain
             1674  LOAD_FAST                'all_source_goals'
             1676  LOAD_FAST                'all_dest_goals'
             1678  CALL_METHOD_2         2  '2 positional arguments'
             1680  GET_ITER         
             1682  FOR_ITER           1706  'to 1706'
             1684  STORE_FAST               'goal'

 L.6987      1686  LOAD_FAST                'goal'
             1688  DUP_TOP          
             1690  LOAD_ATTR                cost
             1692  LOAD_FAST                'goal'
             1694  LOAD_ATTR                path_cost
             1696  INPLACE_ADD      
             1698  ROT_TWO          
             1700  STORE_ATTR               cost
         1702_1704  JUMP_BACK          1682  'to 1682'
             1706  POP_BLOCK        
           1708_0  COME_FROM_LOOP     1668  '1668'

 L.7002      1708  LOAD_GLOBAL              gsi_handlers
             1710  LOAD_ATTR                posture_graph_handlers
             1712  LOAD_ATTR                archiver
             1714  LOAD_ATTR                enabled
         1716_1718  POP_JUMP_IF_FALSE  1816  'to 1816'

 L.7003      1720  SETUP_LOOP         1768  'to 1768'
             1722  LOAD_FAST                'all_source_goals'
             1724  GET_ITER         
             1726  FOR_ITER           1766  'to 1766'
             1728  STORE_FAST               'source_goal'

 L.7004      1730  LOAD_GLOBAL              gsi_handlers
             1732  LOAD_ATTR                posture_graph_handlers
             1734  LOAD_METHOD              log_possible_goal

 L.7005      1736  LOAD_FAST                'sim'
             1738  LOAD_FAST                'source_goal'
             1740  LOAD_ATTR                connectivity_handle
             1742  LOAD_ATTR                path
             1744  LOAD_FAST                'source_goal'

 L.7006      1746  LOAD_FAST                'source_goal'
             1748  LOAD_ATTR                cost
             1750  LOAD_STR                 'Source'
             1752  LOAD_GLOBAL              id
             1754  LOAD_FAST                'source_destination_sets'
             1756  CALL_FUNCTION_1       1  '1 positional argument'
             1758  CALL_METHOD_6         6  '6 positional arguments'
             1760  POP_TOP          
         1762_1764  JUMP_BACK          1726  'to 1726'
             1766  POP_BLOCK        
           1768_0  COME_FROM_LOOP     1720  '1720'

 L.7007      1768  SETUP_LOOP         1816  'to 1816'
             1770  LOAD_FAST                'all_dest_goals'
             1772  GET_ITER         
             1774  FOR_ITER           1814  'to 1814'
             1776  STORE_FAST               'dest_goal'

 L.7008      1778  LOAD_GLOBAL              gsi_handlers
             1780  LOAD_ATTR                posture_graph_handlers
             1782  LOAD_METHOD              log_possible_goal

 L.7009      1784  LOAD_FAST                'sim'
             1786  LOAD_FAST                'dest_goal'
             1788  LOAD_ATTR                connectivity_handle
             1790  LOAD_ATTR                path
             1792  LOAD_FAST                'dest_goal'

 L.7010      1794  LOAD_FAST                'dest_goal'
             1796  LOAD_ATTR                cost
             1798  LOAD_STR                 'Dest'
             1800  LOAD_GLOBAL              id
             1802  LOAD_FAST                'source_destination_sets'
             1804  CALL_FUNCTION_1       1  '1 positional argument'
             1806  CALL_METHOD_6         6  '6 positional arguments'
             1808  POP_TOP          
         1810_1812  JUMP_BACK          1774  'to 1774'
             1814  POP_BLOCK        
           1816_0  COME_FROM_LOOP     1768  '1768'
           1816_1  COME_FROM          1716  '1716'

 L.7013      1816  LOAD_DEREF               'self'
             1818  LOAD_METHOD              normalize_goal_costs
             1820  LOAD_FAST                'all_source_goals'
             1822  CALL_METHOD_1         1  '1 positional argument'
             1824  POP_TOP          

 L.7014      1826  LOAD_DEREF               'self'
             1828  LOAD_METHOD              normalize_goal_costs
             1830  LOAD_FAST                'all_dest_goals'
             1832  CALL_METHOD_1         1  '1 positional argument'
             1834  POP_TOP          

 L.7016      1836  LOAD_GLOBAL              routing
             1838  LOAD_ATTR                Route
             1840  LOAD_FAST                'all_source_goals'
             1842  LOAD_CONST               0
             1844  BINARY_SUBSCR    
             1846  LOAD_ATTR                location
             1848  LOAD_FAST                'all_dest_goals'

 L.7017      1850  LOAD_FAST                'all_source_goals'

 L.7018      1852  LOAD_FAST                'routing_context'
             1854  LOAD_CONST               ('additional_origins', 'routing_context')
             1856  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
             1858  STORE_FAST               'route'

 L.7020      1860  LOAD_FAST                'all_dest_goals'
             1862  LOAD_FAST                'suppressed_goals'
             1864  COMPARE_OP               is
             1866  STORE_FAST               'is_failure_path'

 L.7021      1868  LOAD_GLOBAL              interactions
             1870  LOAD_ATTR                utils
             1872  LOAD_ATTR                routing
             1874  LOAD_ATTR                PlanRoute

 L.7022      1876  LOAD_FAST                'route'
             1878  LOAD_FAST                'routing_agent'

 L.7023      1880  LOAD_FAST                'is_failure_path'

 L.7024      1882  LOAD_FAST                'interaction'
             1884  LOAD_CONST               ('is_failure_route', 'interaction')
             1886  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
             1888  STORE_FAST               'plan_primitive'

 L.7026      1890  LOAD_GLOBAL              element_utils
             1892  LOAD_METHOD              run_child
             1894  LOAD_FAST                'timeline'
             1896  LOAD_GLOBAL              elements
             1898  LOAD_METHOD              MustRunElement
             1900  LOAD_FAST                'plan_primitive'
             1902  CALL_METHOD_1         1  '1 positional argument'
             1904  CALL_METHOD_2         2  '2 positional arguments'
             1906  GET_YIELD_FROM_ITER
             1908  LOAD_CONST               None
             1910  YIELD_FROM       
             1912  STORE_FAST               'result'

 L.7027      1914  LOAD_FAST                'result'
         1916_1918  POP_JUMP_IF_TRUE   1928  'to 1928'

 L.7028      1920  LOAD_GLOBAL              RuntimeError
             1922  LOAD_STR                 'Unknown error when trying to run PlanRoute.run()'
             1924  CALL_FUNCTION_1       1  '1 positional argument'
             1926  RAISE_VARARGS_1       1  'exception instance'
           1928_0  COME_FROM          1916  '1916'

 L.7030      1928  LOAD_FAST                'is_failure_path'
         1930_1932  POP_JUMP_IF_FALSE  1982  'to 1982'
             1934  LOAD_FAST                'plan_primitive'
             1936  LOAD_ATTR                path
             1938  LOAD_ATTR                nodes
         1940_1942  POP_JUMP_IF_FALSE  1982  'to 1982'
             1944  LOAD_FAST                'plan_primitive'
             1946  LOAD_ATTR                path
             1948  LOAD_ATTR                nodes
             1950  LOAD_ATTR                plan_failure_object_id
         1952_1954  POP_JUMP_IF_FALSE  1982  'to 1982'

 L.7031      1956  LOAD_FAST                'plan_primitive'
             1958  LOAD_ATTR                path
             1960  LOAD_ATTR                nodes
             1962  LOAD_ATTR                plan_failure_object_id
             1964  STORE_FAST               'failure_obj_id'

 L.7032      1966  LOAD_GLOBAL              set_transition_failure_reason
             1968  LOAD_FAST                'sim'
             1970  LOAD_GLOBAL              TransitionFailureReasons
             1972  LOAD_ATTR                BLOCKING_OBJECT
             1974  LOAD_FAST                'failure_obj_id'
             1976  LOAD_CONST               ('target_id',)
             1978  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
             1980  POP_TOP          
           1982_0  COME_FROM          1952  '1952'
           1982_1  COME_FROM          1940  '1940'
           1982_2  COME_FROM          1930  '1930'

 L.7036      1982  LOAD_FAST                'is_failure_path'
         1984_1986  POP_JUMP_IF_TRUE   2000  'to 2000'
             1988  LOAD_FAST                'plan_primitive'
             1990  LOAD_ATTR                path
             1992  LOAD_ATTR                nodes
             1994  LOAD_ATTR                plan_success
         1996_1998  POP_JUMP_IF_FALSE  2010  'to 2010'
           2000_0  COME_FROM          1984  '1984'

 L.7037      2000  LOAD_FAST                'plan_primitive'
             2002  LOAD_ATTR                path
             2004  LOAD_ATTR                nodes
         2006_2008  POP_JUMP_IF_TRUE   2044  'to 2044'
           2010_0  COME_FROM          1996  '1996'

 L.7038      2010  LOAD_DEREF               'self'
             2012  LOAD_ATTR                _get_failure_path_spec_gen
             2014  LOAD_FAST                'timeline'
             2016  LOAD_FAST                'sim'
             2018  LOAD_FAST                'source_destination_sets'
             2020  LOAD_FAST                'path_type'
             2022  LOAD_CONST               ('failed_path_type',)
             2024  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
             2026  GET_YIELD_FROM_ITER
             2028  LOAD_CONST               None
             2030  YIELD_FROM       
             2032  STORE_FAST               'failure_path'

 L.7039      2034  LOAD_CONST               False
             2036  LOAD_FAST                'failure_path'
             2038  LOAD_CONST               None
             2040  BUILD_TUPLE_3         3 
             2042  RETURN_VALUE     
           2044_0  COME_FROM          2006  '2006'

 L.7042      2044  LOAD_FAST                'plan_primitive'
             2046  LOAD_ATTR                path
             2048  LOAD_ATTR                selected_start
             2050  STORE_FAST               'origin'

 L.7043      2052  LOAD_FAST                'origin'
             2054  LOAD_ATTR                connectivity_handle
             2056  LOAD_ATTR                path
             2058  STORE_FAST               'origin_path'

 L.7044      2060  LOAD_FAST                'plan_primitive'
             2062  LOAD_ATTR                path
             2064  LOAD_ATTR                selected_goal
             2066  STORE_FAST               'dest'

 L.7045      2068  LOAD_FAST                'plan_primitive'
             2070  LOAD_ATTR                path
             2072  LOAD_ATTR                final_location
             2074  LOAD_FAST                'dest'
             2076  STORE_ATTR               location

 L.7046      2078  LOAD_FAST                'dest'
             2080  LOAD_ATTR                connectivity_handle
             2082  LOAD_ATTR                path
             2084  STORE_FAST               'dest_path'

 L.7048      2086  LOAD_GLOBAL              set_transition_destinations
             2088  LOAD_FAST                'sim'
             2090  LOAD_FAST                'all_source_goals'
             2092  LOAD_FAST                'all_dest_goals'
             2094  LOAD_FAST                'origin'
             2096  LOAD_FAST                'dest'
             2098  LOAD_CONST               True
             2100  LOAD_CONST               True
             2102  LOAD_CONST               ('preserve', 'draw_both_sets')
             2104  CALL_FUNCTION_KW_7     7  '7 total positional and keyword args'
             2106  POP_TOP          

 L.7050      2108  LOAD_FAST                'origin_path'
             2110  LOAD_ATTR                segmented_path
             2112  LOAD_ATTR                destination_specs
             2114  LOAD_METHOD              get
             2116  LOAD_FAST                'dest_path'
             2118  LOAD_CONST               -1
             2120  BINARY_SUBSCR    
             2122  CALL_METHOD_1         1  '1 positional argument'
             2124  STORE_FAST               'destination_spec'

 L.7052      2126  LOAD_GLOBAL              PathSpec
             2128  LOAD_FAST                'origin_path'
             2130  LOAD_FAST                'origin'
             2132  LOAD_ATTR                path_cost

 L.7053      2134  LOAD_FAST                'origin'
             2136  LOAD_ATTR                connectivity_handle
             2138  LOAD_ATTR                var_map

 L.7054      2140  LOAD_CONST               None

 L.7055      2142  LOAD_FAST                'origin'
             2144  LOAD_ATTR                connectivity_handle
             2146  LOAD_ATTR                constraint

 L.7056      2148  LOAD_FAST                'origin_path'
             2150  LOAD_ATTR                segmented_path
             2152  LOAD_ATTR                constraint

 L.7057      2154  LOAD_FAST                'is_failure_path'
             2156  LOAD_CONST               ('is_failure_path',)
             2158  CALL_FUNCTION_KW_7     7  '7 total positional and keyword args'
             2160  STORE_FAST               'left_path_spec'

 L.7061      2162  LOAD_FAST                'origin'
             2164  LOAD_ATTR                has_slot_params
         2166_2168  POP_JUMP_IF_FALSE  2176  'to 2176'
             2170  LOAD_FAST                'origin'
             2172  LOAD_ATTR                slot_params
             2174  JUMP_FORWARD       2180  'to 2180'
           2176_0  COME_FROM          2166  '2166'
             2176  LOAD_GLOBAL              frozendict
             2178  CALL_FUNCTION_0       0  '0 positional arguments'
           2180_0  COME_FROM          2174  '2174'
             2180  STORE_FAST               'o_locked_params'

 L.7062      2182  LOAD_FAST                'left_path_spec'
             2184  LOAD_ATTR                attach_route_and_params
             2186  LOAD_CONST               None

 L.7063      2188  LOAD_FAST                'o_locked_params'
             2190  LOAD_CONST               None
             2192  LOAD_CONST               True
             2194  LOAD_CONST               ('reverse',)
             2196  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
             2198  POP_TOP          

 L.7067      2200  LOAD_GLOBAL              sims4
             2202  LOAD_ATTR                math
             2204  LOAD_METHOD              Transform
             2206  LOAD_GLOBAL              sims4
             2208  LOAD_ATTR                math
             2210  LOAD_ATTR                Vector3
             2212  LOAD_FAST                'dest'
             2214  LOAD_ATTR                location
             2216  LOAD_ATTR                position
             2218  CALL_FUNCTION_EX      0  'positional arguments only'

 L.7068      2220  LOAD_GLOBAL              sims4
             2222  LOAD_ATTR                math
             2224  LOAD_ATTR                Quaternion
             2226  LOAD_FAST                'dest'
             2228  LOAD_ATTR                location
             2230  LOAD_ATTR                orientation
             2232  CALL_FUNCTION_EX      0  'positional arguments only'
             2234  CALL_METHOD_2         2  '2 positional arguments'
             2236  STORE_FAST               'selected_dest_transform'

 L.7069      2238  LOAD_GLOBAL              isinstance
             2240  LOAD_FAST                'dest'
             2242  LOAD_GLOBAL              SlotGoal
             2244  CALL_FUNCTION_2       2  '2 positional arguments'
         2246_2248  POP_JUMP_IF_FALSE  2274  'to 2274'
             2250  LOAD_FAST                'dest_path'
             2252  LOAD_CONST               -1
             2254  BINARY_SUBSCR    
             2256  LOAD_ATTR                body
             2258  LOAD_ATTR                posture_type
             2260  LOAD_ATTR                mobile
         2262_2264  POP_JUMP_IF_TRUE   2274  'to 2274'

 L.7070      2266  LOAD_FAST                'dest'
             2268  LOAD_ATTR                containment_transform
             2270  STORE_FAST               'selected_dest_containment_transform'
             2272  JUMP_FORWARD       2278  'to 2278'
           2274_0  COME_FROM          2262  '2262'
           2274_1  COME_FROM          2246  '2246'

 L.7072      2274  LOAD_FAST                'selected_dest_transform'
             2276  STORE_FAST               'selected_dest_containment_transform'
           2278_0  COME_FROM          2272  '2272'

 L.7074      2278  LOAD_GLOBAL              interactions
             2280  LOAD_ATTR                constraints
             2282  LOAD_ATTR                Transform
             2284  LOAD_FAST                'selected_dest_containment_transform'

 L.7075      2286  LOAD_FAST                'dest'
             2288  LOAD_ATTR                routing_surface_id
             2290  LOAD_CONST               ('routing_surface',)
             2292  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
             2294  STORE_FAST               'selected_dest_constraint'

 L.7076      2296  LOAD_FAST                'dest'
             2298  LOAD_ATTR                connectivity_handle
             2300  LOAD_ATTR                constraint
             2302  STORE_FAST               'constraint'

 L.7077      2304  LOAD_FAST                'constraint'
             2306  LOAD_METHOD              apply
             2308  LOAD_FAST                'selected_dest_constraint'
             2310  CALL_METHOD_1         1  '1 positional argument'
             2312  STORE_FAST               'd_route_constraint'

 L.7082      2314  LOAD_FAST                'd_route_constraint'
             2316  LOAD_ATTR                multi_surface
         2318_2320  POP_JUMP_IF_FALSE  2334  'to 2334'

 L.7083      2322  LOAD_FAST                'd_route_constraint'
             2324  LOAD_METHOD              get_single_surface_version
             2326  LOAD_FAST                'dest'
             2328  LOAD_ATTR                routing_surface_id
             2330  CALL_METHOD_1         1  '1 positional argument'
             2332  STORE_FAST               'd_route_constraint'
           2334_0  COME_FROM          2318  '2318'

 L.7089      2334  LOAD_FAST                'd_route_constraint'
             2336  LOAD_ATTR                valid
         2338_2340  POP_JUMP_IF_TRUE   2346  'to 2346'

 L.7090      2342  LOAD_FAST                'constraint'
             2344  STORE_FAST               'd_route_constraint'
           2346_0  COME_FROM          2338  '2338'

 L.7093      2346  LOAD_GLOBAL              PathSpec
             2348  LOAD_FAST                'dest_path'
             2350  LOAD_FAST                'dest'
             2352  LOAD_ATTR                path_cost

 L.7094      2354  LOAD_FAST                'dest_path'
             2356  LOAD_ATTR                segmented_path
             2358  LOAD_ATTR                var_map_resolved

 L.7095      2360  LOAD_FAST                'destination_spec'

 L.7096      2362  LOAD_FAST                'd_route_constraint'

 L.7097      2364  LOAD_FAST                'dest_path'
             2366  LOAD_ATTR                segmented_path
             2368  LOAD_ATTR                constraint

 L.7098      2370  LOAD_FAST                'is_failure_path'
             2372  LOAD_CONST               ('is_failure_path',)
             2374  CALL_FUNCTION_KW_7     7  '7 total positional and keyword args'
             2376  STORE_FAST               'right_path_spec'

 L.7102      2378  LOAD_FAST                'dest_path'
             2380  LOAD_ATTR                segmented_path
             2382  LOAD_ATTR                constraint
             2384  LOAD_CONST               None
             2386  COMPARE_OP               is-not
         2388_2390  POP_JUMP_IF_FALSE  2448  'to 2448'

 L.7103      2392  LOAD_FAST                'interaction'
             2394  LOAD_ATTR                carry_target
             2396  LOAD_CONST               None
             2398  COMPARE_OP               is-not
         2400_2402  POP_JUMP_IF_FALSE  2414  'to 2414'

 L.7104      2404  LOAD_FAST                'interaction'
             2406  LOAD_ATTR                carry_target
             2408  BUILD_TUPLE_1         1 
             2410  STORE_FAST               'objects_to_ignore'
             2412  JUMP_FORWARD       2418  'to 2418'
           2414_0  COME_FROM          2400  '2400'

 L.7106      2414  LOAD_GLOBAL              DEFAULT
             2416  STORE_FAST               'objects_to_ignore'
           2418_0  COME_FROM          2412  '2412'

 L.7107      2418  LOAD_DEREF               'self'
             2420  LOAD_METHOD              _generate_surface_and_slot_targets
             2422  LOAD_FAST                'right_path_spec'

 L.7108      2424  LOAD_FAST                'left_path_spec'
             2426  LOAD_FAST                'dest'
             2428  LOAD_ATTR                location
             2430  LOAD_FAST                'objects_to_ignore'
             2432  CALL_METHOD_4         4  '4 positional arguments'
         2434_2436  POP_JUMP_IF_TRUE   2448  'to 2448'

 L.7109      2438  LOAD_CONST               False
             2440  LOAD_GLOBAL              EMPTY_PATH_SPEC
             2442  LOAD_CONST               None
             2444  BUILD_TUPLE_3         3 
             2446  RETURN_VALUE     
           2448_0  COME_FROM          2434  '2434'
           2448_1  COME_FROM          2388  '2388'

 L.7112      2448  LOAD_FAST                'dest'
             2450  LOAD_ATTR                has_slot_params
         2452_2454  POP_JUMP_IF_FALSE  2462  'to 2462'
             2456  LOAD_FAST                'dest'
             2458  LOAD_ATTR                slot_params
             2460  JUMP_FORWARD       2466  'to 2466'
           2462_0  COME_FROM          2452  '2452'
             2462  LOAD_GLOBAL              frozendict
             2464  CALL_FUNCTION_0       0  '0 positional arguments'
           2466_0  COME_FROM          2460  '2460'
             2466  STORE_FAST               'd_locked_params'

 L.7116      2468  LOAD_FAST                'plan_primitive'
             2470  LOAD_ATTR                path
             2472  STORE_FAST               'cur_path'

 L.7117      2474  SETUP_LOOP         2610  'to 2610'
             2476  LOAD_FAST                'cur_path'
             2478  LOAD_ATTR                next_path
             2480  LOAD_CONST               None
             2482  COMPARE_OP               is-not
         2484_2486  POP_JUMP_IF_FALSE  2608  'to 2608'

 L.7118      2488  LOAD_FAST                'cur_path'
             2490  LOAD_ATTR                portal_obj
             2492  STORE_FAST               'portal_obj'

 L.7119      2494  LOAD_FAST                'cur_path'
             2496  LOAD_ATTR                portal_id
             2498  STORE_FAST               'portal_id'

 L.7123      2500  LOAD_FAST                'left_path_spec'
             2502  LOAD_ATTR                create_route_nodes
             2504  LOAD_FAST                'cur_path'
             2506  LOAD_FAST                'portal_obj'
             2508  LOAD_FAST                'portal_id'
             2510  LOAD_CONST               ('portal_obj', 'portal_id')
             2512  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
         2514_2516  POP_JUMP_IF_TRUE   2548  'to 2548'

 L.7127      2518  LOAD_DEREF               'self'
             2520  LOAD_METHOD              _get_failure_path_spec_gen
             2522  LOAD_FAST                'timeline'
             2524  LOAD_FAST                'sim'
             2526  LOAD_FAST                'source_destination_sets'
             2528  CALL_METHOD_3         3  '3 positional arguments'
             2530  GET_YIELD_FROM_ITER
             2532  LOAD_CONST               None
             2534  YIELD_FROM       
             2536  STORE_FAST               'failure_path'

 L.7128      2538  LOAD_CONST               False
             2540  LOAD_FAST                'failure_path'
             2542  LOAD_CONST               None
             2544  BUILD_TUPLE_3         3 
             2546  RETURN_VALUE     
           2548_0  COME_FROM          2514  '2514'

 L.7133      2548  LOAD_FAST                'portal_obj'
             2550  LOAD_CONST               None
             2552  COMPARE_OP               is-not
         2554_2556  POP_JUMP_IF_FALSE  2576  'to 2576'

 L.7134      2558  LOAD_FAST                'portal_obj'
             2560  LOAD_ATTR                set_portal_cost_override
             2562  LOAD_FAST                'portal_id'
             2564  LOAD_GLOBAL              routing
             2566  LOAD_ATTR                PORTAL_PLAN_LOCK
             2568  LOAD_FAST                'sim'
             2570  LOAD_CONST               ('sim',)
             2572  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
             2574  POP_TOP          
           2576_0  COME_FROM          2554  '2554'

 L.7136      2576  LOAD_FAST                'cur_path'
             2578  LOAD_ATTR                next_path
             2580  STORE_FAST               'cur_path'

 L.7141      2582  LOAD_FAST                'cur_path'
             2584  LOAD_ATTR                selected_goal
             2586  STORE_FAST               'dest'

 L.7142      2588  LOAD_FAST                'cur_path'
             2590  LOAD_ATTR                final_location
             2592  LOAD_FAST                'dest'
             2594  STORE_ATTR               location

 L.7147      2596  LOAD_FAST                'cur_path'
             2598  LOAD_METHOD              add_destination_to_quad_tree
             2600  CALL_METHOD_0         0  '0 positional arguments'
             2602  POP_TOP          
         2604_2606  JUMP_BACK          2476  'to 2476'
           2608_0  COME_FROM          2484  '2484'
             2608  POP_BLOCK        
           2610_0  COME_FROM_LOOP     2474  '2474'

 L.7149      2610  LOAD_FAST                'left_path_spec'
             2612  LOAD_ATTR                _path
             2614  LOAD_CONST               -1
             2616  BINARY_SUBSCR    
             2618  LOAD_ATTR                posture_spec
             2620  LOAD_FAST                'right_path_spec'
             2622  LOAD_ATTR                _path
             2624  LOAD_CONST               0
             2626  BINARY_SUBSCR    
             2628  LOAD_ATTR                posture_spec
             2630  COMPARE_OP               !=
         2632_2634  POP_JUMP_IF_FALSE  2750  'to 2750'

 L.7153      2636  LOAD_GLOBAL              TransitionSpecCython_create
             2638  LOAD_FAST                'right_path_spec'
             2640  LOAD_FAST                'left_path_spec'
             2642  LOAD_ATTR                _path
             2644  LOAD_CONST               -1
             2646  BINARY_SUBSCR    
             2648  LOAD_ATTR                posture_spec

 L.7154      2650  LOAD_FAST                'right_path_spec'
             2652  LOAD_ATTR                _path
             2654  LOAD_CONST               0
             2656  BINARY_SUBSCR    
             2658  LOAD_ATTR                var_map
             2660  LOAD_GLOBAL              SequenceId
             2662  LOAD_ATTR                DEFAULT

 L.7155      2664  LOAD_FAST                'right_path_spec'
             2666  LOAD_ATTR                _path
             2668  LOAD_CONST               0
             2670  BINARY_SUBSCR    
             2672  LOAD_ATTR                portal_obj

 L.7156      2674  LOAD_FAST                'right_path_spec'
             2676  LOAD_ATTR                _path
             2678  LOAD_CONST               0
             2680  BINARY_SUBSCR    
             2682  LOAD_ATTR                portal_id
             2684  CALL_FUNCTION_6       6  '6 positional arguments'
             2686  STORE_FAST               'right_first_spec'

 L.7162      2688  LOAD_FAST                'right_first_spec'
             2690  LOAD_ATTR                portal_obj
             2692  LOAD_CONST               None
             2694  COMPARE_OP               is-not
         2696_2698  POP_JUMP_IF_FALSE  2716  'to 2716'

 L.7163      2700  LOAD_FAST                'right_path_spec'
             2702  LOAD_ATTR                _path
             2704  LOAD_METHOD              insert
             2706  LOAD_CONST               0
             2708  LOAD_FAST                'right_first_spec'
             2710  CALL_METHOD_2         2  '2 positional arguments'
             2712  POP_TOP          
             2714  JUMP_FORWARD       2726  'to 2726'
           2716_0  COME_FROM          2696  '2696'

 L.7165      2716  LOAD_FAST                'right_first_spec'
             2718  LOAD_FAST                'right_path_spec'
             2720  LOAD_ATTR                _path
             2722  LOAD_CONST               0
             2724  STORE_SUBSCR     
           2726_0  COME_FROM          2714  '2714'

 L.7167      2726  LOAD_FAST                'right_first_spec'
             2728  LOAD_METHOD              set_path
             2730  LOAD_FAST                'cur_path'
             2732  LOAD_FAST                'd_route_constraint'
             2734  CALL_METHOD_2         2  '2 positional arguments'
             2736  POP_TOP          

 L.7168      2738  LOAD_FAST                'right_first_spec'
             2740  LOAD_METHOD              set_locked_params
             2742  LOAD_FAST                'd_locked_params'
             2744  CALL_METHOD_1         1  '1 positional argument'
             2746  POP_TOP          
             2748  JUMP_FORWARD       2764  'to 2764'
           2750_0  COME_FROM          2632  '2632'

 L.7170      2750  LOAD_FAST                'right_path_spec'
             2752  LOAD_METHOD              attach_route_and_params
             2754  LOAD_FAST                'cur_path'

 L.7171      2756  LOAD_FAST                'd_locked_params'
             2758  LOAD_FAST                'd_route_constraint'
             2760  CALL_METHOD_3         3  '3 positional arguments'
             2762  POP_TOP          
           2764_0  COME_FROM          2748  '2748'

 L.7173      2764  LOAD_FAST                'left_path_spec'
             2766  LOAD_METHOD              combine
             2768  LOAD_FAST                'right_path_spec'
             2770  CALL_METHOD_1         1  '1 positional argument'
             2772  STORE_FAST               'path_spec'

 L.7174      2774  LOAD_CONST               True
             2776  LOAD_FAST                'path_spec'
             2778  LOAD_FAST                'dest'
             2780  BUILD_TUPLE_3         3 
             2782  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_SETCOMP' instruction at offset 830

    def normalize_goal_costs(self, all_goals):
        min_cost = sims4.math.MAX_UINT16
        for goal in all_goals:
            if goal.cost < min_cost:
                min_cost = goal.cost

        if min_cost == 0:
            return
        for goal in all_goals:
            goal.cost -= min_cost

    def _get_failure_path_spec_gen(self, timeline, sim, source_destination_sets, interaction=None, failed_path_type=None):
        all_sources = {}
        all_destinations = {}
        all_invalid_sources = {}
        all_invalid_los_sources = {}
        all_invalid_destinations = {}
        all_invalid_los_destinations = {}
        for source_handles, destination_handles, invalid_sources, invalid_los_sources, invalid_destinations, invalid_los_destinations in source_destination_sets.values():
            all_sources.update(source_handles)
            all_destinations.update(destination_handles)
            all_invalid_sources.update(invalid_sources)
            all_invalid_los_sources.update(invalid_los_sources)
            all_invalid_destinations.update(invalid_destinations)
            all_invalid_los_destinations.update(invalid_los_destinations)

        set_transition_failure_reason(sim, TransitionFailureReasons.PATH_PLAN_FAILED)
        failure_sources = all_sources or all_invalid_sources or all_invalid_los_sources
        if not failure_sources:
            if sim.posture.is_vehicle:
                sim.posture.source_interaction.cancel(FinishingType.TRANSITION_FAILURE, 'Canceled Vehicle Posture from Failure Path.')
        else:
            return EMPTY_PATH_SPEC
            best_left_data = None
            best_left_cost = sims4.math.MAX_UINT32
            for source_handle, (_, path_cost, _, _, _, _, _) in failure_sources.items():
                if path_cost < best_left_cost:
                    best_left_cost = path_cost
                    best_left_data = failure_sources[source_handle]
                    best_left_goal = best_left_data[4][0]

            fail_left_path_spec = PathSpec((best_left_data[0]), (best_left_data[1]), (best_left_data[2]),
              (best_left_data[3]), (best_left_data[5]),
              (best_left_data[6]), is_failure_path=True,
              failed_path_type=failed_path_type)
            if best_left_goal is not None:
                if best_left_goal.has_slot_params:
                    if best_left_goal.slot_params:
                        fail_left_path_spec.attach_route_and_params(None,
                          (best_left_goal.slot_params), None, reverse=True)
            failure_destinations = all_destinations or all_invalid_destinations or all_invalid_los_destinations
            return failure_destinations or EMPTY_PATH_SPEC
        height_clearance_override_tuning = interaction.min_height_clearance if interaction is not None else None
        required_height_clearance = get_required_height_clearance(sim, override_tuning=height_clearance_override_tuning)
        all_destination_goals = []
        for _, _, _, _, dest_goals, _, _ in failure_destinations.values():
            all_destination_goals.extend(dest_goals)
            for goal in dest_goals:
                if required_height_clearance > goal.height_clearance:
                    all_destination_goals.remove(goal)
                    continue

        if all_destination_goals:
            route = routing.Route((best_left_goal.location), all_destination_goals, routing_context=(sim.routing_context))
            plan_element = interactions.utils.routing.PlanRoute(route, sim, interaction=interaction)
            result = yield from element_utils.run_child(timeline, plan_element)
            if not result:
                raise RuntimeError('Failed to generate a failure path.')
            if plan_element.path.nodes:
                if len(plan_element.path.nodes) > 1:
                    first_node = plan_element.path.nodes[0]
                    min_water_depth, max_water_depth = OceanTuning.make_depth_bounds_safe_for_surface_and_sim(first_node.routing_surface_id, sim)
                    for node in list(plan_element.path.nodes)[1:]:
                        depth = terrain.get_water_depth(node.position[0], node.position[2], node.routing_surface_id.secondary_id)
                        if min_water_depth is not None:
                            if depth < min_water_depth:
                                return EMPTY_PATH_SPEC
                            if max_water_depth is not None and max_water_depth < depth:
                                return EMPTY_PATH_SPEC

                fail_left_path_spec.create_route_nodes(plan_element.path)
                destinations = {goal.connectivity_handle.path[-1] for goal in all_destination_goals}
                if len(destinations) > 1:
                    logger.warn('Too many destinations: {}', destinations, trigger_breakpoint=True)
                fail_left_path_spec.destination_spec = next(iter(destinations))
                return fail_left_path_spec
        return EMPTY_PATH_SPEC
        if False:
            yield None

    def handle_teleporting_path(self, segmented_paths):
        best_left_path = None
        best_cost = None
        for segmented_path in segmented_paths:
            for left_path in segmented_path.generate_left_paths():
                cost = left_path.cost
                if best_left_path is None or cost < best_cost:
                    best_left_path = left_path
                    best_cost = cost
                    if left_path[-1] in segmented_path.destination_specs:
                        dest_spec = segmented_path.destination_specs[left_path[-1]]
                    else:
                        dest_spec = left_path[-1]
                    var_map = segmented_path.var_map_resolved
                else:
                    break

        if best_left_path is None:
            raise ValueError('No left paths found for teleporting path.')
        return PathSpec(best_left_path, (best_left_path.cost), var_map, dest_spec,
          None, None, path_as_posture_specs=True)

    def update_sim_node_caches(self, sim):
        if sim in self._graph.cached_sim_nodes:
            del self._graph.cached_sim_nodes[sim]
        zone = services.current_zone()
        if zone is None:
            return
        active_household = services.active_household()
        if active_household is None:
            return
        if zone.is_zone_shutting_down:
            self._graph.proxy_sim = None
            return
        from_init = self._graph.proxy_sim is None
        if from_init or self._graph.proxy_sim.sim_proxied is sim:
            for instanced_sim in active_household.instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS):
                if instanced_sim.sim_info.is_teen_or_older and instanced_sim is not sim:
                    self.update_generic_sim_carry_node(instanced_sim, from_init=from_init)
                    return

            sim_info_manager = services.sim_info_manager()
            for instanced_sim in sim_info_manager.instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS):
                if instanced_sim.sim_info.is_teen_or_older and instanced_sim is not sim:
                    self.update_generic_sim_carry_node(instanced_sim, from_init=from_init)
                    return

            self._graph.proxy_sim = None

    def _find_first_constrained_edge(self, sim, path, var_map, reverse=False):
        if not path:
            return (None, None, None)
        elif reverse:
            sequence = reversed(path)
        else:
            sequence = path
        for posture_spec in sequence:
            if not posture_spec.body.posture_type.unconstrained:
                return (
                 posture_spec, None, None)

        if len(path) > 1:
            sequence = zip(path, path[1:])
            if reverse:
                sequence = reversed(list(sequence))
            for spec_a, spec_b in sequence:
                edge_info = self.get_edge(spec_a, spec_b)
                if edge_info is not None:
                    for op in edge_info.operations:
                        constraint = op.get_constraint(sim, spec_a, var_map)
                        if constraint is not None and constraint is not ANYWHERE:
                            return (
                             posture_spec, op, spec_a)

        return (
         posture_spec, None, None)

    def find_entry_posture_spec(self, sim, path, var_map):
        return self._find_first_constrained_edge(sim, path, var_map)

    def find_exit_posture_spec(self, sim, path, var_map):
        return self._find_first_constrained_edge(sim, path, var_map, reverse=True)

    def _get_locations_from_posture(self, sim, posture_spec, var_map, interaction=None, participant_type=None, constrained_edge=None, mobile_posture_spec=None, animation_resolver_fn=None, final_constraint=None, transition_posture_name='stand', left_most_spec=None):
        body_target = posture_spec.body.target
        body_posture_type = posture_spec.body.posture_type
        body_unconstrained = body_posture_type.unconstrained
        should_add_vehicle_slot_constraint = mobile_posture_spec is None or posture_spec != mobile_posture_spec
        should_add_vehicle_slot_constraint |= left_most_spec is not None and left_most_spec != posture_spec
        if interaction is not None:
            if interaction.transition is not None:
                interaction.transition.add_relevant_object(body_target)
                interaction.transition.add_relevant_object(interaction.target)
        body_posture = postures.create_posture(body_posture_type, sim,
          body_target, is_throwaway=True)
        if not (body_posture.unconstrained or body_posture).is_vehicle or should_add_vehicle_slot_constraint:
            constraint_intersection = body_posture.slot_constraint
            if constraint_intersection is None:
                return (
                 True, (None, None, body_target))
                if final_constraint is not None:
                    if constraint_intersection.valid:
                        if not isinstance(final_constraint, RequiredSlotSingle):
                            constraint_geometry_only = final_constraint.generate_geometry_only_constraint()
                            constraint_intersection = constraint_intersection.intersect(constraint_geometry_only)
            else:
                if interaction is None:
                    return (True, (None, None, body_target))
                    target_posture_state = postures.posture_state.PostureState(sim,
                      None, posture_spec, var_map, invalid_expected=True, body_state_spec_only=True,
                      is_throwaway=True)
                    if any((constraint.posture_state_spec.is_filtered_target() for constraint in final_constraint if constraint.posture_state_spec is not None)):
                        base_object = body_target
                    else:
                        base_object = None
                    target = interaction.target
                    with interaction.override_var_map(sim, var_map):
                        interaction_constraint = interaction.apply_posture_state_and_interaction_to_constraint(target_posture_state,
                          final_constraint, sim=sim,
                          target=(base_object or target),
                          participant_type=participant_type,
                          base_object=base_object)
                        target_posture_state.add_constraint(self, interaction_constraint)
                    constraint_intersection = target_posture_state.constraint_intersection
                elif body_unconstrained and animation_resolver_fn is not None and constrained_edge is not None:
                    if constraint_intersection.valid:
                        edge_constraint = constrained_edge.get_constraint(sim, posture_spec, var_map)
                        edge_constraint_resolved = edge_constraint.apply_posture_state(target_posture_state, animation_resolver_fn)
                        edge_constraint_resolved_geometry_only = edge_constraint_resolved.generate_geometry_only_constraint()
                        constraint_intersection = constraint_intersection.intersect(edge_constraint_resolved_geometry_only)
                else:
                    if not constraint_intersection.valid:
                        return (
                         False, (constraint_intersection.generate_single_surface_constraints(), None, body_target))
                    for constraint in constraint_intersection:
                        if constraint.geometry is not None:
                            break
                    else:
                        return (
                         True, (None, None, body_target))

                    constraint_intersection = constraint_intersection.generate_single_surface_constraints()
                    locked_params = frozendict()
                    if body_target is not None:
                        target_name = posture_spec.body.posture_type.get_target_name(sim=sim, target=body_target)
                        if target_name is not None:
                            anim_overrides = body_target.get_anim_overrides(target_name)
                            if anim_overrides is not None:
                                locked_params += anim_overrides.params
            routing_target = None
            if body_target is not None:
                routing_target = body_target
        if interaction.target is not None:
            routing_target = posture_spec.requires_carry_target_in_hand or posture_spec.requires_carry_target_in_slot or interaction.target
        else:
            if interaction.target.parent is not sim:
                routing_target = interaction.target
            else:
                if interaction is not None:
                    if interaction.transition is not None:
                        interaction.transition.add_relevant_object(routing_target)
                locked_params += sim.get_sim_locked_params()
                if interaction is not None:
                    if interaction.is_super and body_posture_type is not None:
                        actor_name = body_posture_type.get_actor_name(sim=sim, target=body_target)
                        target_name = body_posture_type.get_target_name(sim=sim, target=body_target)
                        locked_params += interaction.get_interaction_locked_params(actor_name, target_name)
            locked_params += body_posture.get_slot_offset_locked_params()
            posture_locked_params = locked_params + {'transitionPosture': transition_posture_name}
            return (False, (constraint_intersection, posture_locked_params, routing_target))

    def get_compatible_mobile_posture_target(self, sim):
        posture_object = None
        compatible_postures_and_targets = self.get_compatible_mobile_postures_and_targets(sim)
        if compatible_postures_and_targets:
            posture_type = sim.posture_state.body.posture_type
            for target, compatible_postures in compatible_postures_and_targets.items():
                if posture_type.is_vehicle or posture_type in compatible_postures:
                    posture_object = target
                    break
            else:
                posture_object, _ = next(iter(compatible_postures_and_targets.items()))

        return posture_object

    def get_compatible_mobile_postures_and_targets(self, sim):
        mobile_postures = {}
        found_objects = self._query_quadtree_for_mobile_posture_objects(sim, test_footprint=True)
        for found_obj in found_objects:
            mobile_posture_types = found_obj.provided_mobile_posture_types
            if mobile_posture_types:
                if found_obj.has_posture_portals():
                    posture_entry, _ = found_obj.get_nearest_posture_change(sim)
            if posture_entry is not None:
                if posture_entry.body.posture_type in mobile_posture_types:
                    mobile_postures[found_obj] = (
                     posture_entry.body.posture_type,)
                    continue
                mobile_postures[found_obj] = mobile_posture_types

        return mobile_postures

    def _query_quadtree_for_mobile_posture_objects(self, sim, test_footprint=False):
        if self._mobile_posture_objects_quadtree is None:
            return []
        else:
            pathplan_context = sim.get_routing_context()
            quadtree_polygon = pathplan_context.get_quadtree_polygon()
            if not isinstance(quadtree_polygon, QtCircle):
                lower_bound, upper_bound = quadtree_polygon.bounds()
                quadtree_polygon = sims4.geometry.QtRect(sims4.math.Vector2(lower_bound.x, lower_bound.z), sims4.math.Vector2(upper_bound.x, upper_bound.z))
            query = sims4.geometry.SpatialQuery(quadtree_polygon, [
             self._mobile_posture_objects_quadtree])
            found_objs = query.run()
            found_objs = [posture_obj for posture_obj in found_objs if posture_obj.level == sim.level]
            special_obj = None
            if sim.in_pool:
                special_obj = pool_utils.get_pool_by_block_id(sim.block_id)
            else:
                if sim.routing_surface.type == SurfaceType.SURFACETYPE_POOL:
                    special_obj = services.terrain_service.ocean_object()
        if not test_footprint:
            if special_obj is not None:
                found_objs.append(special_obj)
            return found_objs
        mobile_posture_objects = []
        sim_pos = sim.position
        for mobile_obj in found_objs:
            polygon = mobile_obj.get_polygon_from_footprint_name_hashes(mobile_obj.placement_footprint_hash_set)
            if not polygon is None:
                if not test_point_in_compound_polygon(sim_pos, polygon):
                    continue
                mobile_posture_objects.append(mobile_obj)

        if special_obj is not None:
            mobile_posture_objects.append(special_obj)
        return mobile_posture_objects

    def add_object_to_mobile_posture_quadtree(self, obj):
        if not is_object_mobile_posture_compatible(obj):
            return
        location = sims4.math.Vector2(obj.position.x, obj.position.z)
        if obj.is_in_inventory():
            if location == TunableVector2.DEFAULT_ZERO:
                return
        if self._mobile_posture_objects_quadtree is None:
            self._mobile_posture_objects_quadtree = sims4.geometry.QuadTree()
        polygon = obj.get_polygon_from_footprint_name_hashes(obj.placement_footprint_hash_set)
        if polygon is None:
            return
        lower_bound, upper_bound = polygon.bounds()
        bounding_box = sims4.geometry.QtRect(sims4.math.Vector2(lower_bound.x, lower_bound.z), sims4.math.Vector2(upper_bound.x, upper_bound.z))
        self._mobile_posture_objects_quadtree.insert(obj, bounding_box)

    def remove_object_from_mobile_posture_quadtree(self, obj):
        if self._mobile_posture_objects_quadtree is None:
            return
        self._mobile_posture_objects_quadtree.remove(obj)

    def _query_mobile_posture_objects_for_reset(self, posture_obj=None, test_footprint=False):
        sims = set()
        for sim in services.sim_info_manager().instanced_sims_gen():
            if not sim.is_on_active_lot():
                continue
            found_objs = tuple(self._query_quadtree_for_mobile_posture_objects(sim, test_footprint=test_footprint))
            if posture_obj is not None:
                if posture_obj not in found_objs:
                    continue
            if found_objs:
                sims.add(sim)

        return sims

    def mobile_posture_object_location_changed(self, obj, *_, **__):
        zone = services.current_zone()
        if zone.is_zone_loading:
            return
        before_sims = self._query_mobile_posture_objects_for_reset(obj)
        self.remove_object_from_mobile_posture_quadtree(obj)
        self.add_object_to_mobile_posture_quadtree(obj)
        after_sims = self._query_mobile_posture_objects_for_reset(obj, test_footprint=True)
        affected_sims = before_sims.difference(after_sims) | after_sims
        services.get_reset_and_delete_service().trigger_batch_reset(tuple((sim for sim in affected_sims)), ResetReason.RESET_EXPECTED, obj, 'Mobile posture object moved.')

    def _can_transition_between_nodes(self, source_spec, destination_spec):
        if self.get_edge(source_spec, destination_spec, return_none_on_failure=True) is None:
            return False
        return True

    def get_edge(self, spec_a, spec_b, return_none_on_failure=False):
        try:
            edge_info, _ = self._get_edge_info(spec_a, spec_b)
            if edge_info is None:
                if spec_a.body.posture_type != spec_b.body.posture_type or spec_a.carry != spec_b.carry:
                    if not return_none_on_failure:
                        raise KeyError('Edge not found in posture graph: [{:s}] -> [{:s}]'.format(spec_a, spec_b))
                    return
                return EdgeInfo((), None, 0)
            return edge_info
        except:
            pass

    def print_summary(self, _print=logger.always):
        num_nodes = len(self._graph)
        num_edges = len(self._edge_info)
        object_totals = collections.defaultdict(collections.Counter)
        for node, node_data in self._graph.items():
            objects = {o for o in (node.body_target, node.surface_target) if o is not None}
            if objects:
                for obj in objects:
                    object_totals[obj.definition]['nodes'] += 1
                    object_totals[obj.definition]['edges'] += len(node_data.successors)

            else:
                object_totals['Untargeted']['nodes'] += 1
                object_totals['Untargeted']['edges'] += len(node_data.successors)

        unique_objects = collections.defaultdict(set)
        for node in self._graph:
            objects = {o for o in (node.body_target, node.surface_target) if o is not None}
            for obj in objects:
                unique_objects[obj.definition].add(obj.id)
                object_totals[obj.definition]['parts'] = len(obj.part_owner.parts or (1, )) if obj.is_part else 1

        for definition, instances in unique_objects.items():
            object_totals[definition]['instances'] = len(instances)

        object_totals['Untargeted']['instances'] = 1
        _print('Posture Graph Summary\n====================================================\nTotal node count = {}\nTotal edge count = {}\n\nObjects:\n===================================================\n'.format(num_nodes, num_edges))
        for definition, data in sorted((list(object_totals.items())), reverse=True, key=(lambda x: x[1]['nodes'])):
            if hasattr(definition, 'name'):
                if definition.name is None:
                    def_display = definition.id
                else:
                    def_display = definition.name
            else:
                def_display = definition
            line = ('{:<42} : {instances:>5} instances   {nodes:>5} nodes   {edges:>5} edges'.format)(
             def_display, **data)
            line += '   {:>3} parts/instance   {:>5.4} nodes/instance   {:>5.4} edges/instance'.format(data['parts'], data['nodes'] / data['instances'], data['edges'] / data['instances'])
            _print(line)

    def get_nodes_and_edges(self):
        return (
         len(self._graph), len(self._edge_info))

    def export(self, filename='posture_graph'):
        graph = cython.cast(PostureGraph, self._graph)
        edge_info = self._edge_info
        attribute_indexes = {}
        w = xml.etree.ElementTree.TreeBuilder()
        w.start('gexf', {
         'xmlns': "'http://www.gexf.net/1.2draft'", 
         'xmlns:xsi': "'http://www.w3.org/2001/XMLSchema-instance'", 
         'xsi:schemaLocation': "'http://www.gexf.net/1.2draft/gexf.xsd'", 
         'version': "'1.2'"})
        w.start('meta', {})
        w.start('creator', {})
        w.data('Electronic Arts')
        w.end('creator')
        w.start('description', {})
        w.data('Tuning topology')
        w.end('description')
        w.end('meta')
        w.start('graph', {'defaultedgetype':'directed', 
         'mode':'static'})
        TYPE_MAPPING = {str: 'string', 
         int: 'float', 
         float: 'float'}
        w.start('attributes', {'class': 'node'})
        attribute_index = 0
        for attribute_name, attribute_type in PostureSpec._attribute_definitions:
            attribute_indexes[attribute_name] = str(attribute_index)
            w.start('attribute', {'id':str(attribute_index), 
             'title':attribute_name.strip('_').title().replace('_', ' '), 
             'type':TYPE_MAPPING[attribute_type]})
            w.end('attribute')
            attribute_index += 1

        w.end('attributes')
        nodes = set()
        edge_nodes = set()
        w.start('nodes', {})
        for node in sorted((graph.nodes), key=repr):
            nodes.add(hash(node))
            w.start('node', {'id':str(hash(node)), 
             'label':str(node)})
            w.start('attvalues', {})
            for attribute_name, attribute_type in PostureSpec._attribute_definitions:
                attr_value = getattr(node, attribute_name)
                w.start('attvalue', {'for':attribute_indexes[attribute_name], 
                 'value':str(attr_value)})
                w.end('attvalue')

            w.end('attvalues')
            w.end('node')

        w.end('nodes')
        w.start('edges', {})
        edge_id = 0
        for node in sorted((graph.nodes), key=repr):
            for connected_node in sorted((graph.get_successors(node)), key=repr):
                edge_nodes.add(hash(node))
                edge_nodes.add(hash(connected_node))
                w.start('edge', {'id':str(edge_id), 
                 'label':', '.join((str(operation) for operation in edge_info[(node, connected_node)].operations)), 
                 'source':str(hash(node)), 
                 'target':str(hash(connected_node))})
                w.end('edge')
                edge_id += 1

        w.end('edges')
        w.end('graph')
        w.end('gexf')
        tree = w.close()

        def indent(elem, level=0):
            i = '\n' + level * '  '
            if len(elem):
                if not (elem.text and elem.text.strip()):
                    elem.text = i + '  '
                if not (elem.tail and elem.tail.strip()):
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)

                elem.tail = elem.tail and elem.tail.strip() or i
            else:
                if level:
                    elem.tail = elem.tail and elem.tail.strip() or i

        indent(tree)
        from os.path import expanduser
        path = expanduser('~')
        file = open('{}\\Desktop\\{}.gexf'.format(path, filename), 'wb')
        file.write(xml.etree.ElementTree.tostring(tree))
        file.close()
        print('DONE!')
