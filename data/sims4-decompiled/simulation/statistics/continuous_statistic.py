# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\statistics\continuous_statistic.py
# Compiled at: 2022-04-28 23:30:14
# Size of source mod 2**32: 58667 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
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
and ::= expr jmp_false expr jmp_false . 
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
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
expr_stmt ::= expr POP_TOP . 
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
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
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
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
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
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
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
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
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
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 108        64  LOAD_CONST               True
->                66  RETURN_VALUE     
import contextlib, math, operator
from date_and_time import DateAndTime, create_date_and_time
from event_testing.resolver import SingleSimResolver
from sims4.math import Threshold
from sims4.repr_utils import standard_repr
from sims4.tuning.tunable import TunableRange
from sims4.utils import classproperty, flexmethod
from singletons import UNSET, DEFAULT
from statistics.base_statistic import BaseStatistic
from statistics.base_statistic_listener import BaseStatisticCallbackListener
from statistics.statistic_enums import StatisticLockAction
import alarms, clock, date_and_time, enum, services, sims4.log, sims4.math
__unittest__ = 'test.statistics.continuous_statistic_tests'

class DelayedDecayStatus(enum.Int, export=False):
    ACTIVE = -1
    NOT_TUNED = -2
    NOT_TRACKED = -3


logger = sims4.log.Logger('SimStatistics')

class _ContinuousStatisticCallbackData(BaseStatisticCallbackListener):
    __slots__ = '_trigger_time'

    def __init__(self, stat, stat_type, threshold, callback, on_callback_alarm_reset=None, should_seed=True):
        super().__init__(stat, stat_type, threshold, callback, on_callback_alarm_reset, should_seed=should_seed)
        self._trigger_time = UNSET

    def __repr__(self):
        return standard_repr(self, stat=(self.statistic_type.__name__), threshold=(self._threshold), callback=(self._callback), trigger_time=(self._trigger_time))

    def __eq__(self, other):
        return super().__eq__(other) and self._trigger_time == other._trigger_time

    def reset_trigger_time(self, new_trigger_interval: float):
        if new_trigger_interval is not None and new_trigger_interval > 0:
            now = services.time_service().sim_now
            self._trigger_time = now + clock.interval_in_sim_minutes(new_trigger_interval)
        else:
            self._trigger_time = None
        if self._on_callback_alarm_reset is not None:
            self._on_callback_alarm_reset(self._stat, self._trigger_time)

    def destroy(self):
        self._trigger_time = UNSET

    def is_valid(self):
        return self._trigger_time is not UNSET

    def will_be_called_at_the_same_time_as--- This code section failed: ---

 L. 103         0  LOAD_FAST                'self'
                2  LOAD_ATTR                trigger_time
                4  LOAD_GLOBAL              UNSET
                6  COMPARE_OP               is
                8  POP_JUMP_IF_TRUE     40  'to 40'
               10  LOAD_FAST                'self'
               12  LOAD_ATTR                trigger_time
               14  LOAD_CONST               None
               16  COMPARE_OP               is
               18  POP_JUMP_IF_TRUE     40  'to 40'
               20  LOAD_FAST                'other'
               22  LOAD_ATTR                trigger_time
               24  LOAD_GLOBAL              UNSET
               26  COMPARE_OP               is
               28  POP_JUMP_IF_TRUE     40  'to 40'
               30  LOAD_FAST                'other'
               32  LOAD_ATTR                trigger_time
               34  LOAD_CONST               None
               36  COMPARE_OP               is
               38  POP_JUMP_IF_FALSE    44  'to 44'
             40_0  COME_FROM            28  '28'
             40_1  COME_FROM            18  '18'
             40_2  COME_FROM             8  '8'

 L. 104        40  LOAD_CONST               False
               42  RETURN_VALUE     
             44_0  COME_FROM            38  '38'

 L. 107        44  LOAD_FAST                'self'
               46  LOAD_ATTR                trigger_time
               48  LOAD_METHOD              absolute_ticks
               50  CALL_METHOD_0         0  '0 positional arguments'
               52  LOAD_FAST                'other'
               54  LOAD_ATTR                trigger_time
               56  LOAD_METHOD              absolute_ticks
               58  CALL_METHOD_0         0  '0 positional arguments'
               60  COMPARE_OP               ==
               62  POP_JUMP_IF_FALSE    68  'to 68'

 L. 108        64  LOAD_CONST               True
               66  RETURN_VALUE     
             68_0  COME_FROM            62  '62'

Parse error at or near `RETURN_VALUE' instruction at offset 66

    def calculate_next_trigger_time(self):
        if self._trigger_time is UNSET:
            logger.warn('Attempting to calculate the interval on a callback that was never inserted into the _callbacks list: {}', self)
            return
        if self._trigger_time == None:
            return
        now = services.time_service().sim_now
        delta = self._trigger_time - now
        return delta

    @property
    def trigger_time(self):
        return self._trigger_time

    def __lt__(self, other):
        if self._trigger_time is None:
            if other._trigger_time is None:
                return False
        if other._trigger_time is None:
            return True
        if self._trigger_time is None:
            return False
        return self._trigger_time < other._trigger_time

    def __gt__(self, other):
        if self._trigger_time is None:
            if other._trigger_time is None:
                return False
        if other._trigger_time is None:
            return False
        if self._trigger_time is None:
            return True
        return self._trigger_time > other._trigger_time


class ContinuousStatistic(BaseStatistic):
    SAVE_VALUE_MULTIPLE = TunableRange(description='\n        When saving the value of a continuous statistic, we force stats to the \n        nearest multiple of this tunable for save of inventory \n        items to increase the chance of stacking success.-Mike Duke\n        \n        EX: 95+ = 100, 85 to 94.9 = 90, ..., -5 to 5 = 0, ..., -95 to -100 = -100\n        ',
      tunable_type=int,
      minimum=1,
      default=10)
    decay_rate = 0
    _default_convergence_value = 0

    def __init__(self, tracker, initial_value):
        super().__init__(tracker, initial_value)
        self._decay_enabled = False
        self._decay_rate_override = UNSET
        self._delayed_decay_rate_override = UNSET
        self._initial_delay_override = UNSET
        self._final_delay_override = UNSET
        self._suppress_update_active_callbacks = False
        self._alarm_handle = None
        self._active_callback = None
        self._last_update = services.time_service().sim_now
        self._decay_rate_modifier = 1
        self._decay_rate_modifiers = None
        self._convergence_value = self._default_convergence_value
        if not (tracker is None or tracker.recovery_add_in_progress):
            if not tracker.should_suppress_calculations():
                self._recalculate_modified_decay_rate()
        self._delayed_decay_timer = None
        self._time_of_last_value_change = None
        self._delayed_decay_active = False
        self._decay_callback_handle = None

    def on_initial_startup(self):
        pass

    def start_low_level_simulation(self):
        pass

    def stop_low_level_simulation(self):
        pass

    def stop_regular_simulation(self):
        pass

    def on_zone_load(self):
        pass

    @classproperty
    def default_convergence_value(cls):
        return cls._default_convergence_value

    @classproperty
    def default_value(cls):
        return cls._default_convergence_value

    @classproperty
    def continuous(self):
        return True

    def on_add(self):
        super().on_add()
        if self._use_delayed_decay():
            self.restart_delayed_decay_timer()
        owner = self.tracker.owner
        if owner.is_locked(self):
            locked_reasons = owner.get_locked_reason_list(type(self))
            if locked_reasons:
                lock_reason, action_on_lock = locked_reasons[-1]
                self.on_lock(action_on_lock=action_on_lock)

    def on_recovery(self):
        super().on_recovery()
        if self.tracker is not None:
            if not self.tracker.should_suppress_calculations():
                self._recalculate_modified_decay_rate()

    @flexmethod
    def get_value(cls, inst):
        if inst is not None:
            inst._update_value()
        return super(ContinuousStatistic, inst if inst is not None else cls).get_value()

    def set_value(self, value, **kwargs):
        self._update_value()
        (super().set_value)(value, **kwargs)
        if self._use_delayed_decay():
            self.restart_delayed_decay_timer()

    def _get_minimum_decay_level(self):
        return self.min_value

    def _get_maximum_decay_level(self):
        return self.max_value

    def on_remove(self, on_destroy=False):
        super().on_remove(on_destroy=on_destroy)
        self._destroy_alarm()
        self._active_callback = None

    def create_callback_listener(self, threshold, callback, on_callback_alarm_reset=None, should_seed=True):
        self._update_value()
        callback_data = _ContinuousStatisticCallbackData(self, (self.stat_type), threshold, callback, on_callback_alarm_reset, should_seed=should_seed)
        return callback_data

    def create_callback_listener_seed(stat_type, threshold, callback, on_callback_alarm_reset=None):
        return _ContinuousStatisticCallbackData(None, stat_type, threshold, callback, on_callback_alarm_reset)

    def add_callback_listener(self, callback_listener, update_active_callback=True):
        super().add_callback_listener(callback_listener)
        if update_active_callback:
            if callback_listener is self._callback_queue_head:
                self._update_active_callback()

    def remove_callback_listener(self, callback_listener):
        listener_removed = super().remove_callback_listener(callback_listener)
        if listener_removed:
            if self._active_callback is callback_listener:
                self._update_active_callback()
        return listener_removed

    def _insert_callback_listener(self, callback_data: _ContinuousStatisticCallbackData):
        if self._tracker is not None:
            if self._tracker.suppress_callback_alarm_calculation:
                self._statistic_callback_listeners.append(callback_data)
                return
        self._update_value()
        trigger_interval = self._calculate_minutes_until_value_is_reached_through_decay(callback_data.threshold.value, callback_data.threshold)
        callback_data.reset_trigger_time(trigger_interval)
        try:
            insertion_index = self._find_insertion_point(0, len(self._statistic_callback_listeners), callback_data)
        except Exception:
            if self.tracker and self.tracker.owner and self.tracker.owner.is_sim:
                self.tracker.owner.log_sim_info((logger.error), additional_msg=('Failed to find insertion point for {}.'.format(self)))
            else:
                logger.error('Failed to find insertion point for {}.', self)
            raise

        self._statistic_callback_listeners.insert(insertion_index, callback_data)

    def fixup_callbacks_during_load(self):
        pass

    @property
    def decay_enabled(self):
        return self._decay_enabled

    @decay_enabled.setter
    def decay_enabled(self, value):
        if self._decay_enabled != value:
            logger.debug('Setting decay for {} to {}', self, value)
            self._update_value()
            self._decay_enabled = value
            self._update_callback_listeners()
            if value:
                sleep_time_now = services.time_service().sim_now
                if self._last_update is None or self._last_update < sleep_time_now:
                    self._last_update = sleep_time_now

    def get_decay_rate(self, use_decay_modifier=True):
        if self._decay_enabled:
            if self._get_change_rate_without_decay() == 0:
                start_value = self._value
                if use_decay_modifier:
                    decay_rate = self.base_decay_rate * self._decay_rate_modifier
                else:
                    decay_rate = self.base_decay_rate
                if start_value > self.convergence_value:
                    decay_sign = -1
                else:
                    if start_value < self.convergence_value:
                        decay_sign = 1
                    else:
                        decay_sign = 0
                return decay_rate * decay_sign
        return 0

    def has_decay_rate_modifier(self, value):
        return self._decay_rate_modifiers and value in self._decay_rate_modifiers

    def add_decay_rate_modifier(self, value):
        if value < 0:
            logger.error('Attempting to add negative decay rate modifier of {} to {}', value, self)
            return
        logger.debug('Adding decay rate modifier of {} to {}', value, self)
        self._update_value()
        if self._decay_rate_modifiers is None:
            self._decay_rate_modifiers = []
        self._decay_rate_modifiers.append(value)
        self._recalculate_modified_decay_rate()

    def clear_decay_rate_modifiers(self):
        self._decay_rate_modifiers = None

    def remove_decay_rate_modifier(self, value):
        if self._decay_rate_modifiers is None:
            return
        else:
            if value in self._decay_rate_modifiers:
                logger.debug('Removing decay rate modifier of {} from {}', value, self)
                self._update_value()
                self._decay_rate_modifiers.remove(value)
                self._recalculate_modified_decay_rate()
            self._decay_rate_modifiers = self._decay_rate_modifiers or None

    def get_decay_rate_modifier(self):
        return self._decay_rate_modifier

    @property
    def convergence_value(self):
        return self._convergence_value

    @convergence_value.setter
    def convergence_value(self, value):
        self._update_value()
        self._convergence_value = value
        self._update_callback_listeners()

    def reset_convergence_value(self):
        self._update_value()
        self._convergence_value = self._default_convergence_value
        self._update_callback_listeners()

    def is_at_convergence(self):
        return self.get_value() == self.convergence_value

    def get_decay_time(self, threshold, use_decay_modifier=True):
        self._update_value()
        return self._calculate_minutes_until_value_is_reached_through_decay((threshold.value), threshold, use_decay_modifier=use_decay_modifier)

    def get_change_rate(self):
        change_rate = self._get_change_rate_without_decay()
        if change_rate != 0:
            return change_rate
        return self.get_decay_rate()

    def get_change_rate_without_decay(self):
        return self._get_change_rate_without_decay()

    @property
    def base_decay_rate(self):
        if self._decay_rate_override is not UNSET:
            return self._decay_rate_override
        if self._delayed_decay_active:
            if self._use_delayed_decay():
                if self._delayed_decay_rate_override is not UNSET:
                    return self._delayed_decay_rate_override
                return self.delayed_decay_rate.delayed_decay_rate
        return self.decay_rate

    def _get_change_rate_without_decay(self):
        if self._statistic_modifier > 0:
            return self._statistic_modifier * self._statistic_multiplier_increase
        return self._statistic_modifier * self._statistic_multiplier_decrease

    def _update_value(self, minimum_decay_value=DEFAULT, maximum_decay_value=DEFAULT):
        tracker = self._tracker
        if tracker is not None:
            if tracker.should_suppress_calculations():
                return 0
        else:
            now = services.time_service().sim_now
            delta_time = now - self._last_update
            if delta_time <= date_and_time.TimeSpan.ZERO:
                return 0
            self._last_update = now
            local_time_delta = delta_time.in_minutes()
            start_value = self._value
            change_rate = self._get_change_rate_without_decay()
            decay_rate = self.get_decay_rate()
            new_value = None
            if change_rate == 0 and decay_rate != 0:
                time_to_convergence = self._calculate_minutes_until_value_is_reached_through_decay(self.convergence_value)
                if time_to_convergence is not None:
                    if local_time_delta > time_to_convergence:
                        new_value = self.convergence_value
                delta_rate = decay_rate
            else:
                if change_rate != 0:
                    if self._use_delayed_decay():
                        self._time_of_last_value_change = now
            delta_rate = change_rate
        if new_value is None:
            new_value = start_value + local_time_delta * delta_rate
        if minimum_decay_value is not DEFAULT:
            new_value = max(new_value, minimum_decay_value)
        if maximum_decay_value is not DEFAULT:
            new_value = min(new_value, maximum_decay_value)
        if new_value != self._value:
            if tracker is not None:
                tracker.notify_delta(self.stat_type, new_value - self._value)
        self._value = new_value
        self._clamp()
        return local_time_delta

    @contextlib.contextmanager
    def _suppress_update_active_callbacks_context_manager(self):
        if self._suppress_update_active_callbacks:
            yield
        else:
            self._suppress_update_active_callbacks = True
            try:
                yield
            finally:
                self._suppress_update_active_callbacks = False

    def _update_callback_listeners(self, old_value=0, new_value=0, resort_list=True):
        if not self._statistic_callback_listeners:
            return
        else:
            if self._tracker is not None:
                if self._tracker.suppress_callback_alarm_calculation:
                    return
            self._update_value()
            callback_tuple = None
            if old_value <= new_value:
                callback_tuple = tuple(self._statistic_callback_listeners)
            else:
                callback_tuple = tuple(reversed(self._statistic_callback_listeners))
        for callback_data in callback_tuple:
            if old_value != new_value:
                if callback_data.check_for_threshold(old_value, new_value):
                    callback_data.trigger_callback()
            if not self._tracker is None:
                trigger_interval = self._tracker.suppress_callback_setup_during_load or self._calculate_minutes_until_value_is_reached_through_decay(callback_data.threshold.value, callback_data.threshold)
                callback_data.reset_trigger_time(trigger_interval)

        if resort_list:
            self._statistic_callback_listeners.sort()
        self._update_active_callback()

    def _update_active_callback(self):
        if self._suppress_update_active_callbacks:
            return
        if self._tracker is not None:
            if self._tracker.suppress_callback_alarm_calculation:
                return
        if not self._statistic_callback_listeners:
            if self._active_callback is not None or self._alarm_handle:
                logger.debug('_callback list is empty; destroying alarm & active callback.  Last active callback was {}', self._active_callback)
                self._destroy_alarm()
                self._active_callback = None
            return
        self._destroy_alarm()
        while self._statistic_callback_listeners:
            callback_data = self._callback_queue_head
            next_trigger_time = callback_data.calculate_next_trigger_time()
            if next_trigger_time is None:
                self._active_callback = None
                break
            if next_trigger_time.in_ticks() <= 0:
                self._trigger_callback(callback_data)
                self._update_active_callback()
            else:
                if self._alarm_handle:
                    self._destroy_alarm()
                logger.debug('Creating alarm for callback: {}', callback_data)
                self._alarm_handle = alarms.add_alarm(self, next_trigger_time, self._alarm_callback)
                self._active_callback = callback_data
                break

    def _destroy_alarm(self):
        if self._alarm_handle is not None:
            alarms.cancel_alarm(self._alarm_handle)
            self._alarm_handle = None

    def _alarm_callback(self, handle):
        self._alarm_handle = None
        callbacks_to_call = [callback for callback in self._statistic_callback_listeners if self._active_callback.will_be_called_at_the_same_time_as(callback)]
        with self._suppress_update_active_callbacks_context_manager():
            for callback in callbacks_to_call:
                self._trigger_callback(callback)

        self._update_active_callback()

    def _trigger_callback(self, callback):
        if callback is None:
            logger.error('Attempting to trigger a None callback.')
            self._update_active_callback()
            return
        callback.trigger_callback()
        if self.remove_callback_listener(callback):
            self.add_callback_listener(callback, update_active_callback=False)

    def _find_insertion_point(self, start, end, callback_data):
        if start == end:
            return start
        else:
            index = int((start + end) / 2)
            if index == len(self._statistic_callback_listeners):
                return index
            if callback_data > self._statistic_callback_listeners[index]:
                return self._find_insertion_point(index + 1, end, callback_data)
            if index == 0 or callback_data < self._statistic_callback_listeners[index] and callback_data < self._statistic_callback_listeners[index - 1]:
                return self._find_insertion_point(start, end - 1, callback_data)
        return index

    def _find_nearest_threshold(self, interval, comparison):
        num_intervals = (self.get_value() - self.min_value) / interval
        if comparison is operator.ge or comparison is operator.gt:
            next_interval = math.floor(num_intervals) + 1
        else:
            next_interval = math.ceil(num_intervals) - 1
        threshold = next_interval * interval + self.min_value
        if threshold >= self.min_value:
            if threshold <= self.max_value:
                return threshold

    def _calculate_minutes_until_value_is_reached_through_decay(self, target_value, threshold=None, use_decay_modifier=True):
        if threshold is not None:
            if threshold.comparison is operator.gt:
                target_value = target_value + sims4.math.EPSILON
            else:
                if threshold.comparison is operator.lt:
                    target_value = target_value - sims4.math.EPSILON
                else:
                    current_value = self._value
                    if threshold is not None:
                        if threshold.compare(current_value):
                            return 0
                    if current_value == target_value:
                        return 0
                    if target_value < self._get_minimum_decay_level() <= current_value:
                        return
                    if target_value > self._get_maximum_decay_level() >= current_value:
                        return
                change_rate = self._get_change_rate_without_decay()
            if not (change_rate != 0):
                if change_rate < 0:
                    if target_value < current_value:
                        result = (target_value - current_value) / change_rate
                        return abs(result)
                return
                decay_rate = self.get_decay_rate(use_decay_modifier=use_decay_modifier)
                if not (decay_rate != 0):
                    if decay_rate > 0:
                        if target_value < current_value:
                            return
        else:
            if not current_value < self.convergence_value < target_value:
                if current_value > self.convergence_value > target_value:
                    return
            result = (target_value - current_value) / decay_rate
            return abs(result)

    def _recalculate_modified_decay_rate(self):
        old_decay_rate = self.get_decay_rate()
        self._decay_rate_modifier = 1
        if self._decay_rate_modifiers is not None:
            for val in self._decay_rate_modifiers:
                self._decay_rate_modifier *= val

        if self.tracker is not None:
            multiplier = self.get_skill_based_statistic_multiplier([self.tracker.owner], -1)
            self._decay_rate_modifier *= multiplier
        resort_callbacks = False
        if old_decay_rate == 0:
            if self.get_decay_rate() != 0:
                resort_callbacks = True
        self._update_callback_listeners(resort_list=resort_callbacks)

    def add_statistic_modifier(self, value):
        self._update_value()
        super().add_statistic_modifier(value)

    def remove_statistic_modifier(self, value):
        if self._statistic_modifiers is None:
            return
        if value in self._statistic_modifiers:
            self._update_value()
            super().remove_statistic_modifier(value)
            self._update_value()

    def _on_statistic_modifier_changed(self, notify_watcher=True):
        self._update_value()
        super()._on_statistic_modifier_changed(notify_watcher=notify_watcher)
        self._update_callback_listeners()

    @flexmethod
    def get_saved_value(cls, inst):
        cls_or_inst = inst if inst is not None else cls
        value = cls_or_inst.get_value()
        if inst is not None:
            owner = inst._tracker.owner
            if owner is not None:
                if owner.inventoryitem_component is not None:
                    if owner.inventoryitem_component.save_for_stack_compaction:
                        value = round(value / cls.SAVE_VALUE_MULTIPLE) * cls.SAVE_VALUE_MULTIPLE
        return value

    def unlocks_skills_on_max(self):
        return False

    @classmethod
    def send_commodity_update_message(cls, sim_info, old_value, new_value):
        pass

    def can_decay(self):
        return True

    def on_lock(self, action_on_lock):
        self.decay_enabled = False
        if action_on_lock == StatisticLockAction.USE_MAX_VALUE_TUNING:
            self.set_value(self.max_value)
        else:
            if action_on_lock == StatisticLockAction.USE_MIN_VALUE_TUNING:
                self.set_value(self.min_value)
            else:
                if action_on_lock == StatisticLockAction.USE_BEST_VALUE_TUNING:
                    self.set_value(self.best_value)
        self.send_commodity_progress_msg()

    def on_unlock(self, auto_satisfy=True):
        self.decay_enabled = True
        if self._use_delayed_decay():
            self._delayed_decay_active = False
            self._time_of_last_value_change = services.time_service().sim_now
            self._start_delayed_decay_timer()
        self.send_commodity_progress_msg()

    def needs_fixup_on_load(self):
        return False

    def needs_fixup_on_load_for_objects(self):
        return False

    def has_auto_satisfy_value(self):
        return False

    def _use_delayed_decay(self):
        if self.delayed_decay_rate is None:
            return False
        if not self.delayed_decay_rate.npc_decay:
            if self.tracker.owner.is_sim:
                if self.tracker.owner.is_npc:
                    return False
        return True

    def _start_delayed_decay_timer(self):
        self.refresh_threshold_callback()
        if self._delayed_decay_timer is not None:
            alarms.cancel_alarm(self._delayed_decay_timer)
            self._delayed_decay_timer = None
        else:
            initial_delay = self._get_initial_delay()
            final_delay = self._get_final_delay()
            now = services.time_service().sim_now
            time_passed = 0
            if self._time_of_last_value_change is not None:
                time_passed = now - self._time_of_last_value_change
                time_passed = time_passed.in_minutes()
            elif time_passed < initial_delay:
                length = date_and_time.create_time_span(minutes=(initial_delay - time_passed))
                self._delayed_decay_timer = alarms.add_alarm(self, length, self._display_decay_warning)
            else:
                if time_passed < initial_delay + final_delay:
                    time_into_final_delay = time_passed - initial_delay
                    length = date_and_time.create_time_span(minutes=(final_delay - time_into_final_delay))
                    self._delayed_decay_timer = alarms.add_alarm(self, length, self._start_delayed_decay)
                else:
                    self._start_delayed_decay(None)

    def _get_initial_delay(self):
        if self._initial_delay_override is UNSET:
            return self.delayed_decay_rate.initial_delay
        return self._initial_delay_override

    def _get_final_delay(self):
        if self._final_delay_override is UNSET:
            return self.delayed_decay_rate.final_delay
        return self._final_delay_override

    def _display_decay_warning(self, timeline):
        if self.should_start_delayed_decay():
            if self.should_display_delayed_decay_warning():
                sim = self.tracker.owner
                resolver = SingleSimResolver(sim)
                notification = self.delayed_decay_rate.decay_warning(sim, resolver)
                notification.show_dialog()
            self._start_delayed_decay_timer()

    def _start_delayed_decay(self, timeline):
        self._update_value()
        if not self.tracker.owner.is_locked(self):
            self._delayed_decay_active = True
            self.decay_enabled = True
        self.refresh_threshold_callback()
        self._update_callback_listeners(resort_list=False)
        self.send_commodity_progress_msg()

    def should_start_delayed_decay(self):
        if self.is_at_convergence():
            return False
        if self.tracker.owner.is_locked(self):
            return False
        return True

    def should_display_delayed_decay_warning(self):
        if self._decay_rate_modifier == 0 or self.delayed_decay_rate.decay_warning is None:
            return False
        return True

    def send_commodity_progress_msg(self, is_rate_change=True):
        pass

    def get_time_till_decay_starts(self):
        if self.delayed_decay_rate is None:
            return DelayedDecayStatus.NOT_TUNED
        if (self._time_of_last_value_change is None or self.tracker.owner).is_sim:
            if self.tracker.owner.is_npc:
                if not self.delayed_decay_rate.npc_decay:
                    return DelayedDecayStatus.NOT_TRACKED
        now = services.time_service().sim_now
        time_passed = now - self._time_of_last_value_change
        initial_delay = date_and_time.create_time_span(minutes=(self._get_initial_delay()))
        final_delay = date_and_time.create_time_span(minutes=(self._get_final_delay()))
        time_remaining = initial_delay + final_delay - time_passed
        if time_remaining < date_and_time.create_time_span(minutes=0):
            return DelayedDecayStatus.ACTIVE
        return time_remaining.in_minutes()

    @property
    def instance_required(self):
        if super().instance_required:
            return True
        if self._convergence_value != self._default_convergence_value:
            return True
        change_rate = self._get_change_rate_without_decay()
        decay_rate = self.get_decay_rate()
        return change_rate != 0 or decay_rate != 0

    def refresh_threshold_callback(self):
        pass

    @classmethod
    def load_statistic_data(cls, tracker, data):
        tracker.set_value(cls, (data.value), from_load=True)

    def load_time_of_last_value_change(self, data):
        if self.delayed_decay_rate is None:
            return
        else:
            if not data.time_of_last_value_change:
                return
            owner = self.tracker.owner
            if owner.is_sim:
                if not owner.is_npc or self.delayed_decay_rate.npc_decay:
                    last_save_time = services.current_zone().time_of_last_save()
                    timer_start_time = DateAndTime(data.time_of_last_value_change)
                    difference = timer_start_time - last_save_time
                    self._time_of_last_value_change = services.time_service().sim_now + difference
                    self._start_delayed_decay_timer()
                    return
        self._time_of_last_value_change = DateAndTime(data.time_of_last_value_change)

    def restart_delayed_decay_timer(self):
        self._update_value()
        self._time_of_last_value_change = services.time_service().sim_now
        self._delayed_decay_active = False
        self._start_delayed_decay_timer()
