# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\business\business_employee_manager.py
# Compiled at: 2017-05-09 00:24:53
# Size of source mod 2**32: 36696 bytes

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
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
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
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
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
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
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
returns ::= _stmts return . 
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= store_subscript . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
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
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= testfalse_not_or . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false COME_FROM . 
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
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
   
 L. 724       262  LOAD_FAST                'self'
                 264  LOAD_ATTR                _employee_uniform_data_female
                 266  LOAD_FAST                'employee_type'
                 268  BINARY_SUBSCR    
->               270  RETURN_VALUE     
from _collections import defaultdict
from collections import Counter
from math import floor
import itertools, math
from business.business_employee import BusinessEmployeeData
from date_and_time import DateAndTime
from distributor.rollback import ProtocolBufferRollback
from distributor.system import Distributor
from event_testing.test_events import TestEvent
from interactions.context import InteractionContext
from interactions.priority import Priority
from sims.outfits.outfit_enums import OutfitCategory
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims.sim_info_types import Gender
from sims.sim_info_utils import sim_info_auto_finder
from sims4.math import clamp
from singletons import DEFAULT
import services, sims4.log
logger = sims4.log.Logger('Business', default_owner='trevor')

class BusinessEmployeeManager:
    LEGACY_EMPLOYEE_TYPE = 1

    def __init__(self, business_manager):
        self._business_manager = business_manager
        self._employee_sim_ids = defaultdict(set)
        self._employees = {}
        self._daily_employee_wages = 0
        self._employee_payroll = {}
        self._employee_uniform_data_male = defaultdict()
        self._employee_uniform_data_female = defaultdict()

    @property
    def employee_count(self):
        return len(self._employees)

    def get_employee_types(self):
        return tuple((employee_type for employee_type in self._employee_sim_ids))

    def save_data(self, data):
        data.daily_employee_wages = self._daily_employee_wages
        if self._employee_sim_ids:
            for employee_type, employee_ids in self._employee_sim_ids.items():
                for employee_id in employee_ids:
                    with ProtocolBufferRollback(data.employee_data) as (employee_data):
                        employee_data.employee_type = employee_type
                        employee_data.employee_id = employee_id

        else:
            for employee_id, employee_info in self._employees.items():
                with ProtocolBufferRollback(data.employee_data) as (employee_data):
                    employee_data.employee_type = employee_info.employee_type
                    employee_data.employee_id = employee_id

        for employee_type, uniform_data_male in self._employee_uniform_data_male.items():
            with ProtocolBufferRollback(data.employee_uniforms_male) as (employee_uniforms_male):
                employee_uniforms_male.employee_type = employee_type
                employee_uniforms_male.employee_uniform_data.mannequin_id = uniform_data_male.sim_id
                uniform_data_male.save_sim_info(employee_uniforms_male.employee_uniform_data)

        for employee_type, uniform_data_female in self._employee_uniform_data_female.items():
            with ProtocolBufferRollback(data.employee_uniforms_female) as (employee_uniforms_female):
                employee_uniforms_female.employee_type = employee_type
                employee_uniforms_female.employee_uniform_data.mannequin_id = uniform_data_female.sim_id
                uniform_data_female.save_sim_info(employee_uniforms_female.employee_uniform_data)

        for sim_id, payroll_tuple in self._employee_payroll.items():
            with ProtocolBufferRollback(data.employee_payroll) as (employee_payroll):
                employee_payroll.sim_id = sim_id
                clock_in_time = payroll_tuple[0]
                if clock_in_time is not None:
                    employee_payroll.clock_in_time = clock_in_time
                payroll_entry = payroll_tuple[1]
                if payroll_entry is not None:
                    for career_level, hours_worked in payroll_entry.items():
                        with ProtocolBufferRollback(employee_payroll.payroll_data) as (payroll_data):
                            payroll_data.career_level_guid = career_level.guid64
                            payroll_data.hours_worked = hours_worked

    def _load_uniform_data(self, persistence_service, uniform_data, employee_type, gender):
        if gender == Gender.MALE:
            data_dictionary = self._employee_uniform_data_male
        else:
            data_dictionary = self._employee_uniform_data_female
        employee_uniform_data = uniform_data
        data_dictionary[employee_type] = self.get_employee_uniform_data(employee_type, gender, sim_id=(uniform_data.mannequin_id))
        if persistence_service is not None:
            persisted_data = persistence_service.get_mannequin_proto_buff(uniform_data.mannequin_id)
            if persisted_data is not None:
                employee_uniform_data = persisted_data
        data_dictionary[employee_type].load_sim_info(employee_uniform_data)
        self._send_employee_uniform_data(data_dictionary[employee_type])
        persistence_service.del_mannequin_proto_buff(uniform_data.mannequin_id)

    def _load_payroll_data(self, payroll_data):
        career_level_manager = services.get_instance_manager(sims4.resources.Types.CAREER_LEVEL)
        for payroll_msg in payroll_data.employee_payroll:
            payroll_data = Counter()
            for payroll_entry_msg in payroll_msg.payroll_data:
                career_level = career_level_manager.get(payroll_entry_msg.career_level_guid)
                if career_level is None:
                    continue
                payroll_data[career_level] = payroll_entry_msg.hours_worked

            if not payroll_data:
                continue
            clock_in_time = DateAndTime(payroll_msg.clock_in_time) if payroll_msg.clock_in_time else None
            self._employee_payroll[payroll_msg.sim_id] = (clock_in_time, payroll_data)

    def load_data(self, data):
        self._daily_employee_wages = data.daily_employee_wages
        for employee_data in data.employee_data:
            self._employee_sim_ids[employee_data.employee_type].add(employee_data.employee_id)

        persistence_service = services.get_persistence_service()
        for male_uniform in data.employee_uniforms_male:
            self._load_uniform_data(persistence_service, male_uniform.employee_uniform_data, male_uniform.employee_type, Gender.MALE)

        for female_uniform in data.employee_uniforms_female:
            self._load_uniform_data(persistence_service, female_uniform.employee_uniform_data, female_uniform.employee_type, Gender.FEMALE)

        self._load_payroll_data(data)

    def load_legacy_data(self, save_data):
        self._daily_employee_wages = save_data.daily_employee_wages
        for employee_id in save_data.employee_ids:
            self._employee_sim_ids[self.LEGACY_EMPLOYEE_TYPE].add(employee_id)

        persistence_service = services.get_persistence_service()
        if save_data.HasField('employee_uniform_data_male'):
            self._load_uniform_data(persistence_service, save_data.employee_uniform_data_male, self.LEGACY_EMPLOYEE_TYPE, Gender.MALE)
        if save_data.HasField('employee_uniform_data_female'):
            self._load_uniform_data(persistence_service, save_data.employee_uniform_data_female, self.LEGACY_EMPLOYEE_TYPE, Gender.FEMALE)
        self._load_payroll_data(save_data)

    def _try_reload_outfit_data(self, employee_uniform_dict, persistence_service, gender):
        for uniform_type, uniform_sim_info_wrapper in employee_uniform_dict.items():
            persisted_data = persistence_service.get_mannequin_proto_buff(uniform_sim_info_wrapper.id)
            if persisted_data is None:
                continue
            self._load_uniform_data(persistence_service, persisted_data, uniform_type, gender)

    def reload_employee_uniforms(self):
        persistence_service = services.get_persistence_service()
        if persistence_service is None:
            return
        self._try_reload_outfit_data(self._employee_uniform_data_male, persistence_service, Gender.MALE)
        self._try_reload_outfit_data(self._employee_uniform_data_female, persistence_service, Gender.FEMALE)

    def on_zone_load(self):
        sim_info_manager = services.sim_info_manager()
        for employee_type, employee_id_list in self._employee_sim_ids.items():
            for employee_id in employee_id_list:
                sim_info = sim_info_manager.get(employee_id)
                if sim_info is not None:
                    self._employees[sim_info.sim_id] = BusinessEmployeeData(self, sim_info, employee_type)

        self._employee_sim_ids.clear()
        self.update_employees(add_career_remove_callback=True)
        for employee_uniform in itertools.chain(self._employee_uniform_data_male.values(), self._employee_uniform_data_female.values()):
            self._send_employee_uniform_data(employee_uniform)

        services.get_event_manager().register_single_event(self, TestEvent.SkillLevelChange)
        if not self._business_manager.is_active_household_and_zone():
            return
        if self._business_manager.is_open:
            for sim_info in self.get_employees_on_payroll():
                if self.get_employee_career(sim_info) is None:
                    self.on_employee_clock_out(sim_info)
                clock_in_time, _ = self._employee_payroll[sim_info.sim_id]
                if clock_in_time is not None:
                    self._register_employee_callbacks(sim_info)
                    employee_data = self.get_employee_data(sim_info)
                    employee_data.add_career_buff()

    def on_client_disconnect(self):
        services.get_event_manager().unregister_single_event(self, TestEvent.SkillLevelChange)

    def handle_event(self, sim_info, event, resolver):
        if event == TestEvent.SkillLevelChange:
            employee_data = self._employees.get(sim_info.sim_id, None)
            if employee_data is not None:
                skill = resolver.event_kwargs['skill']
                if self._business_manager.is_valid_employee_skill(skill.stat_type, employee_data.employee_type):
                    employee_data.leveled_skill_up(skill.stat_type)
                    if self._business_manager.tuning_data.show_empolyee_skill_level_up_notification:
                        skill.force_show_level_notification(resolver.event_kwargs['new_level'])

    def open_business(self):
        if self._business_manager.is_owned_by_npc:
            return
        elif self._business_manager.business_zone_id == services.current_zone_id():
            zone_director = services.venue_service().get_zone_director()
            zone_director.start_employee_situations((self._employees), owned_by_npc=(not self._business_manager.is_owner_household_active))
        else:
            for employee_id in self._employees:
                employee_sim_info = services.sim_info_manager().get(employee_id)
                if employee_sim_info is not None:
                    self.on_employee_clock_in(employee_sim_info)

    def close_business(self):
        for sim_info in itertools.chain(self.get_employees_gen(), self.get_employees_on_payroll()):
            self.on_employee_clock_out(sim_info)

        self._daily_employee_wages = self.get_total_employee_wages()
        self._employee_payroll.clear()

    def _clear_state(self):
        self._daily_employee_wages = 0

    def get_employee_tuning_data_for_employee_type(self, employee_type):
        return self._business_manager.tuning_data.employee_data_map.get(employee_type, None)

    def get_employee_data(self, employee_sim_info):
        return self._employees.get(employee_sim_info.sim_id, None)

    def get_employee_career(self, employee_sim_info):
        employee_data = self.get_employee_data(employee_sim_info)
        if employee_data is None:
            return
        employee_type_tuning_data = self.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
        if employee_type_tuning_data is None:
            return
        return employee_sim_info.career_tracker.get_career_by_uid(employee_type_tuning_data.career.guid64)

    def get_employee_career_level(self, employee_sim_info):
        career = self.get_employee_career(employee_sim_info)
        if career is None:
            return
        return career.current_level_tuning

    def is_employee(self, sim_info):
        if self._employee_sim_ids:
            for employee_ids in self._employee_sim_ids.values():
                if sim_info.sim_id in employee_ids:
                    return True

            return False
        return sim_info.sim_id in self._employees

    def is_employee_clocked_in(self, sim_info):
        clock_in_time, _ = self._employee_payroll.get(sim_info.sim_id, (None, None))
        return clock_in_time is not None

    def on_employee_clock_in(self, employee_sim_info):
        self._register_employee_callbacks(employee_sim_info)
        clock_in_time = services.time_service().sim_now
        if employee_sim_info.sim_id not in self._employee_payroll:
            self._employee_payroll[employee_sim_info.sim_id] = (
             clock_in_time, Counter())
        else:
            _, payroll_data = self._employee_payroll[employee_sim_info.sim_id]
            career_level = self.get_employee_career_level(employee_sim_info)
            if career_level is None:
                logger.error('Employee {} trying to clock in with career level None for Business {}', employee_sim_info, self._business_manager)
            else:
                payroll_data[career_level] += 0
                self._employee_payroll[employee_sim_info.sim_id] = (clock_in_time, payroll_data)
            employee_data = self.get_employee_data(employee_sim_info)
            if employee_data is not None:
                employee_data.add_career_buff()
            else:
                logger.error('{} is being clocked in but not registered as an employee.', employee_sim_info)

    def on_employee_clock_out(self, employee_sim_info, career_level=DEFAULT):
        career = self.get_employee_career(employee_sim_info)
        if career is not None:
            if self.on_employee_career_promotion in career.on_promoted:
                career.on_promoted.unregister(self.on_employee_career_promotion)
            if self.on_employee_career_demotion in career.on_demoted:
                career.on_demoted.unregister(self.on_employee_career_demotion)
        if employee_sim_info.sim_id not in self._employee_payroll:
            return
        clock_in_time, payroll_data = self._employee_payroll[employee_sim_info.sim_id]
        if clock_in_time is not None:
            career_level = self.get_employee_career_level(employee_sim_info) if career_level is DEFAULT else career_level
            if career_level is not None:
                clock_out_time = services.time_service().sim_now
                payroll_data[career_level] += (clock_out_time - clock_in_time).in_hours()
        else:
            self._employee_payroll[employee_sim_info.sim_id] = (
             None, payroll_data)
            employee_data = self.get_employee_data(employee_sim_info)
            if employee_data is not None:
                employee_data.remove_career_buff()
            else:
                logger.error('{} is being clocked out but not registered as an employee.', employee_sim_info)

    def get_employee_wages(self, employee_sim_info):
        if not self._business_manager.is_open:
            return 0
        if employee_sim_info.sim_id not in self._employee_payroll:
            return 0
        clock_in_time, payroll_data = self._employee_payroll[employee_sim_info.sim_id]
        total_wages = sum((career_level.simoleons_per_hour * round(hours_worked) for career_level, hours_worked in payroll_data.items()))
        if clock_in_time is not None:
            hours_worked = (services.time_service().sim_now - clock_in_time).in_hours()
            total_wages += self.get_employee_career_level(employee_sim_info).simoleons_per_hour * round(hours_worked)
        return math.ceil(total_wages)

    def get_total_employee_wages_per_hour(self):
        total = 0
        for sim_info in self.get_employee_sim_infos():
            career_level = self.get_employee_career_level(sim_info)
            total += career_level.simoleons_per_hour

        return total

    def get_total_employee_wages(self):
        return sum((self.get_employee_wages(sim_info) for sim_info in self.get_employees_on_payroll()))

    def final_daily_wages(self):
        return self._daily_employee_wages

    def get_employee_wages_breakdown_gen(self, employee_sim_info):
        if employee_sim_info.sim_id not in self._employee_payroll:
            return
        clock_in_time, payroll_data = self._employee_payroll[employee_sim_info.sim_id]
        for career_level, hours_worked in payroll_data.items():
            if clock_in_time is not None:
                if career_level is self.get_employee_career_level(employee_sim_info):
                    hours_worked += (services.time_service().sim_now - clock_in_time).in_hours()
            yield (
             career_level, round(hours_worked))

    @sim_info_auto_finder
    def get_employees_gen(self):
        yield from self._employees
        if False:
            yield None

    def get_desired_career_level(self, sim_info, employee_type):
        employee_tuning_data = self.get_employee_tuning_data_for_employee_type(employee_type)
        skill_completion = 0
        for skill_type, skill_data in employee_tuning_data.employee_skills.items():
            skill_or_skill_type = sim_info.get_stat_instance(skill_type) or skill_type
            user_value = skill_or_skill_type.get_user_value()
            max_skill_level = skill_or_skill_type.max_level
            skill_completion += skill_data.weight * user_value / max_skill_level

        skill_completion = skill_completion / len(employee_tuning_data.employee_skills.keys())
        max_career_level = len(employee_tuning_data.career.start_track.career_levels) - 1
        career_level = clamp(0, floor(employee_tuning_data.weighted_skill_to_career_level_ratio * skill_completion * max_career_level), max_career_level)
        return career_level

    def add_employee(self, sim_info, employee_type, is_npc_employee=False):
        if self.is_employee(sim_info):
            logger.error('Trying to add a duplicate employee: {}. Trying to add as type: {}', sim_info, employee_type)
            return
        employee_tuning_data = self.get_employee_tuning_data_for_employee_type(employee_type)
        employee_career_type = employee_tuning_data.career
        if employee_career_type is None:
            logger.error('Trying to add an employee with an invalid type: {}.', employee_type)
            return
        employee_career = employee_career_type(sim_info)
        employee = BusinessEmployeeData(self, sim_info, employee_type)
        career_location = employee_career.get_career_location()
        career_location.set_zone_id(self._business_manager.business_zone_id)
        career_level = self.get_desired_career_level(sim_info, employee_type) + 1
        sim_info.career_tracker.add_career(employee_career, user_level_override=career_level)
        sim_info.add_statistic(employee_tuning_data.satisfaction_commodity, employee_tuning_data.satisfaction_commodity.initial_value)
        self._employees[sim_info.sim_id] = employee
        self._register_on_employee_career_removed_callback(sim_info, career=employee_career)
        if is_npc_employee:
            return
        zone_director = services.venue_service().get_zone_director()
        if zone_director is not None:
            zone_director.on_add_employee(sim_info, employee)

    def remove_employee(self, sim_info):
        employee_data = self.get_employee_data(sim_info)
        if employee_data is None:
            logger.error("Trying to remove an employee from a business but the employee doesn't belong to this business. {}", sim_info)
            return
        if self._business_manager.is_open:
            self.on_employee_clock_out(sim_info)
        if sim_info.sim_id in self._employee_payroll:
            del self._employee_payroll[sim_info.sim_id]
        employee_tuning_data = self.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
        self._unregister_on_employee_career_removed_callback(sim_info)
        sim_info.career_tracker.remove_career(employee_tuning_data.career.guid64)
        if self.is_employee(sim_info):
            del self._employees[sim_info.sim_id]

    def remove_invalid_employee(self, sim_id):
        if sim_id in self._employee_payroll:
            del self._employee_payroll[sim_id]
        if sim_id in self._employees:
            del self._employees[sim_id]

    def update_employees(self, add_career_remove_callback=False):
        for employee_data in tuple(self._employees.values()):
            employee_type_data = self.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
            employee_sim_info = employee_data.get_employee_sim_info()
            if employee_sim_info is None:
                self.remove_invalid_employee(employee_data.employee_sim_id)
                continue
            else:
                if employee_sim_info.career_tracker is None:
                    self.remove_employee(employee_sim_info)
                    continue
                career = employee_sim_info.career_tracker.get_career_by_uid(employee_type_data.career.guid64)
                if career is None:
                    self.remove_employee(employee_sim_info)
            if add_career_remove_callback:
                self._register_on_employee_career_removed_callback(employee_sim_info, career=career)

    @sim_info_auto_finder
    def get_employee_sim_infos(self):
        return self._employees

    @sim_info_auto_finder
    def get_employees_on_payroll(self):
        return self._employee_payroll

    def run_employee_interaction(self, affordance, target_sim):
        active_sim = services.get_active_sim()
        if active_sim is None:
            return False
        context = InteractionContext(active_sim, InteractionContext.SOURCE_PIE_MENU, Priority.High)
        return active_sim.push_super_affordance(affordance, None, context, picked_item_ids=(target_sim.sim_id,))

    def _register_employee_callbacks(self, employee_sim_info):
        career = self.get_employee_career(employee_sim_info)
        if career is None:
            logger.error('Employee {} does not have active business career', employee_sim_info)
            return
        if self.on_employee_career_promotion not in career.on_promoted:
            career.on_promoted.register(self.on_employee_career_promotion)
        if self.on_employee_career_demotion not in career.on_demoted:
            career.on_demoted.register(self.on_employee_career_demotion)

    def on_employee_career_promotion(self, sim_info):
        if not self._business_manager.is_open:
            return
        if sim_info.sim_id not in self._employee_payroll:
            return
        career = self.get_employee_career(sim_info)
        self.on_employee_clock_out(sim_info, career_level=(career.previous_level_tuning))
        self.on_employee_clock_in(sim_info)

    def on_employee_career_demotion(self, sim_info):
        if not self._business_manager.is_open:
            return
        if sim_info.sim_id not in self._employee_payroll:
            return
        career = self.get_employee_career(sim_info)
        self.on_employee_clock_out(sim_info, career_level=(career.next_level_tuning))
        self.on_employee_clock_in(sim_info)

    def _register_on_employee_career_removed_callback(self, employee_sim_info, career=None):
        if career is None:
            career = self.get_employee_career(employee_sim_info)
        if self.on_employee_career_removed not in career.on_career_removed:
            career.on_career_removed.append(self.on_employee_career_removed)

    def _unregister_on_employee_career_removed_callback(self, employee_sim_info):
        career = self.get_employee_career(employee_sim_info)
        if career is not None:
            if self.on_employee_career_removed in career.on_career_removed:
                career.on_career_removed.remove(self.on_employee_career_removed)

    def on_employee_career_removed(self, sim_info):
        if self.is_employee(sim_info):
            self.remove_employee(sim_info)
        return True

    def get_employee_uniform_data--- This code section failed: ---

 L. 703         0  LOAD_FAST                'self'
                2  LOAD_METHOD              get_employee_tuning_data_for_employee_type
                4  LOAD_FAST                'employee_type'
                6  CALL_METHOD_1         1  '1 positional argument'
                8  STORE_FAST               'employee_type_tuning_data'

 L. 704        10  LOAD_FAST                'employee_type_tuning_data'
               12  LOAD_CONST               None
               14  COMPARE_OP               is
               16  POP_JUMP_IF_FALSE    34  'to 34'

 L. 705        18  LOAD_GLOBAL              logger
               20  LOAD_METHOD              error
               22  LOAD_STR                 'Trying to get employee uniform data for an invalid employee type: {}.'
               24  LOAD_FAST                'employee_type'
               26  CALL_METHOD_2         2  '2 positional arguments'
               28  POP_TOP          

 L. 706        30  LOAD_CONST               None
               32  RETURN_VALUE     
             34_0  COME_FROM            16  '16'

 L. 707        34  LOAD_FAST                'gender'
               36  LOAD_GLOBAL              Gender
               38  LOAD_ATTR                MALE
               40  COMPARE_OP               ==
               42  POP_JUMP_IF_FALSE   150  'to 150'

 L. 708        44  LOAD_FAST                'self'
               46  LOAD_ATTR                _employee_uniform_data_male
               48  POP_JUMP_IF_FALSE    64  'to 64'
               50  LOAD_FAST                'self'
               52  LOAD_ATTR                _employee_uniform_data_male
               54  LOAD_FAST                'employee_type'
               56  BINARY_SUBSCR    
               58  LOAD_CONST               None
               60  COMPARE_OP               is
               62  POP_JUMP_IF_FALSE   140  'to 140'
             64_0  COME_FROM            48  '48'

 L. 709        64  LOAD_GLOBAL              SimInfoBaseWrapper
               66  LOAD_FAST                'sim_id'
               68  LOAD_CONST               ('sim_id',)
               70  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               72  LOAD_FAST                'self'
               74  LOAD_ATTR                _employee_uniform_data_male
               76  LOAD_FAST                'employee_type'
               78  STORE_SUBSCR     

 L. 710        80  LOAD_FAST                'self'
               82  LOAD_ATTR                _employee_uniform_data_male
               84  LOAD_FAST                'employee_type'
               86  BINARY_SUBSCR    
               88  LOAD_METHOD              load_from_resource
               90  LOAD_FAST                'employee_type_tuning_data'
               92  LOAD_ATTR                uniform_male
               94  CALL_METHOD_1         1  '1 positional argument'
               96  POP_TOP          

 L. 711        98  LOAD_FAST                'self'
              100  LOAD_ATTR                _employee_uniform_data_male
              102  LOAD_FAST                'employee_type'
              104  BINARY_SUBSCR    
              106  LOAD_METHOD              set_current_outfit
              108  LOAD_GLOBAL              OutfitCategory
              110  LOAD_ATTR                CAREER
              112  LOAD_CONST               0
              114  BUILD_TUPLE_2         2 
              116  CALL_METHOD_1         1  '1 positional argument'
              118  POP_TOP          

 L. 713       120  LOAD_FAST                'sim_id'
              122  POP_JUMP_IF_TRUE    140  'to 140'

 L. 714       124  LOAD_FAST                'self'
              126  LOAD_METHOD              _send_employee_uniform_data
              128  LOAD_FAST                'self'
              130  LOAD_ATTR                _employee_uniform_data_male
              132  LOAD_FAST                'employee_type'
              134  BINARY_SUBSCR    
              136  CALL_METHOD_1         1  '1 positional argument'
              138  POP_TOP          
            140_0  COME_FROM           122  '122'
            140_1  COME_FROM            62  '62'

 L. 715       140  LOAD_FAST                'self'
              142  LOAD_ATTR                _employee_uniform_data_male
              144  LOAD_FAST                'employee_type'
              146  BINARY_SUBSCR    
              148  RETURN_VALUE     
            150_0  COME_FROM            42  '42'

 L. 716       150  LOAD_FAST                'gender'
              152  LOAD_GLOBAL              Gender
              154  LOAD_ATTR                FEMALE
              156  COMPARE_OP               ==
          158_160  POP_JUMP_IF_FALSE   272  'to 272'

 L. 717       162  LOAD_FAST                'self'
              164  LOAD_ATTR                _employee_uniform_data_female
              166  POP_JUMP_IF_FALSE   184  'to 184'
              168  LOAD_FAST                'self'
              170  LOAD_ATTR                _employee_uniform_data_female
              172  LOAD_FAST                'employee_type'
              174  BINARY_SUBSCR    
              176  LOAD_CONST               None
              178  COMPARE_OP               is
          180_182  POP_JUMP_IF_FALSE   262  'to 262'
            184_0  COME_FROM           166  '166'

 L. 718       184  LOAD_GLOBAL              SimInfoBaseWrapper
              186  LOAD_FAST                'sim_id'
              188  LOAD_CONST               ('sim_id',)
              190  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              192  LOAD_FAST                'self'
              194  LOAD_ATTR                _employee_uniform_data_female
              196  LOAD_FAST                'employee_type'
              198  STORE_SUBSCR     

 L. 719       200  LOAD_FAST                'self'
              202  LOAD_ATTR                _employee_uniform_data_female
              204  LOAD_FAST                'employee_type'
              206  BINARY_SUBSCR    
              208  LOAD_METHOD              load_from_resource
              210  LOAD_FAST                'employee_type_tuning_data'
              212  LOAD_ATTR                uniform_female
              214  CALL_METHOD_1         1  '1 positional argument'
              216  POP_TOP          

 L. 720       218  LOAD_FAST                'self'
              220  LOAD_ATTR                _employee_uniform_data_female
              222  LOAD_FAST                'employee_type'
              224  BINARY_SUBSCR    
              226  LOAD_METHOD              set_current_outfit
              228  LOAD_GLOBAL              OutfitCategory
              230  LOAD_ATTR                CAREER
              232  LOAD_CONST               0
              234  BUILD_TUPLE_2         2 
              236  CALL_METHOD_1         1  '1 positional argument'
              238  POP_TOP          

 L. 722       240  LOAD_FAST                'sim_id'
          242_244  POP_JUMP_IF_TRUE    262  'to 262'

 L. 723       246  LOAD_FAST                'self'
              248  LOAD_METHOD              _send_employee_uniform_data
              250  LOAD_FAST                'self'
              252  LOAD_ATTR                _employee_uniform_data_female
              254  LOAD_FAST                'employee_type'
              256  BINARY_SUBSCR    
              258  CALL_METHOD_1         1  '1 positional argument'
              260  POP_TOP          
            262_0  COME_FROM           242  '242'
            262_1  COME_FROM           180  '180'

 L. 724       262  LOAD_FAST                'self'
              264  LOAD_ATTR                _employee_uniform_data_female
              266  LOAD_FAST                'employee_type'
              268  BINARY_SUBSCR    
              270  RETURN_VALUE     
            272_0  COME_FROM           158  '158'

Parse error at or near `RETURN_VALUE' instruction at offset 270

    def _send_employee_uniform_data(self, employee_uniform_data):
        employee_uniform_data.manager = services.sim_info_manager()
        Distributor.instance().add_object(employee_uniform_data)

    def get_number_of_employees_by_type(self, employee_type):
        return sum((1 for employee_data in self._employees.values() if employee_data.employee_type == employee_type))

    def get_employees_by_type(self, employee_type):
        return [employee for employee, employee_data in self._employees.items() if employee_data.employee_type == employee_type]
