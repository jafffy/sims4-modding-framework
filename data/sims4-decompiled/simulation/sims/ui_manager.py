# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\ui_manager.py
# Compiled at: 2021-03-09 01:50:10
# Size of source mod 2**32: 55973 bytes

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
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_slice2 ::= expr expr BUILD_SLICE_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
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
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
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
delete ::= delete_subscript . 
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
delete_subscript ::= expr expr DELETE_SUBSCR . 
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= build_slice2 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
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
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
starred ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
starred ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= delete . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
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
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr BUILD_TUPLE_1 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
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
   
 L. 544        46  LOAD_FAST                'self'
                  48  LOAD_METHOD              _remove_routing_interaction_info
                  50  LOAD_FAST                'int_info'
                  52  CALL_METHOD_1         1  '1 positional argument'
                  54  POP_TOP          
                  56  JUMP_FORWARD         58  'to 58'
->              58_0  COME_FROM            56  '56'
import itertools, weakref
from distributor.shared_messages import IconInfoData
from interactions import interaction_messages, ParticipantType
from interactions.si_state import SIState
from protocolbuffers import Sims_pb2
import enum, interactions.base.interaction, interactions.context, sims4.log, sims4.resources, sims4.tuning.tunable, tag, telemetry_helper
logger = sims4.log.Logger('UI_MANAGER', default_owner='msantander')
TELEMETRY_GROUP_INTERACTION = 'INTR'
TELEMETRY_HOOK_INTERACTION_QUEUE = 'QUEU'
TELEMETRY_HOOK_INTERACTION_CANCEL = 'CANC'
TELEMETRY_HOOK_OPTIONAL_ACTION = 'QUIC'
writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_INTERACTION)

class UIManager:

    class QueueType(enum.Int, export=False):
        Queue = 0
        Super = 1
        Continuation = 2

    def __init__(self, sim):
        self._sim_ref = sim.ref()
        self._queued_interactions = []
        self._super_interactions = []
        self._group_interactions = {}
        self._last_running_interaction_id = 0
        self._continuation_interactions = []
        self._si_skill_mapping = {}
        self._routing_info = InteractionInfo.create_routing_info()

    @property
    def _sim(self):
        return self._sim_ref()

    @property
    def _running_interactions(self):
        for int_info in (itertools.chain)(self._super_interactions, *self._group_interactions.values()):
            yield int_info

    def _add_running_interaction(self, int_info):
        if int_info.visual_group_tag is None:
            self._super_interactions.append(int_info)
            return
        running_infos = self._group_interactions.get(int_info.visual_group_tag, [])
        running_infos.append(int_info)
        running_infos.sort(key=(lambda x: x.visual_group_priority))
        self._group_interactions[int_info.visual_group_tag] = list(running_infos)
        return running_infos

    def _remove_running_interactions(self, int_info):
        if int_info.visual_group_tag is None:
            self._super_interactions.remove(int_info)
            return
        running_infos = self._group_interactions.get(int_info.visual_group_tag)
        running_infos.remove(int_info)
        if running_infos:
            self._group_interactions[int_info.visual_group_tag] = list(running_infos)
            return running_infos
        del self._group_interactions[int_info.visual_group_tag]

    def get_grouped_interaction_gen(self, interaction_id):
        int_info, queue_type = self._find_interaction(interaction_id)
        if queue_type == self.QueueType.Super:
            running_infos = self._group_interactions.get(int_info.visual_group_tag)
            if running_infos is not None:
                for running_info in running_infos:
                    yield running_info

    def _get_visible_grouped_interaction_id(self, interaction_id):
        int_info, _ = self._find_interaction(interaction_id)
        if int_info is None:
            return
        if int_info.visual_group_tag is None:
            return
        running_infos = self._group_interactions.get(int_info.visual_group_tag)
        if running_infos:
            return running_infos[-1].interaction_id

    def _get_super_id_for_mixer(self, super_id):
        int_info, queue_type = self._find_interaction(super_id)
        if int_info is not None:
            if queue_type == self.QueueType.Queue:
                return super_id
        return self._get_visible_grouped_interaction_id(super_id)

    def get_interactions_gen(self):
        return itertools.chain(self._queued_interactions, self._running_interactions)

    def add_queued_interaction(self, interaction, interaction_id_to_insert_after=None, notify_client=True):
        if interaction.visible:
            if interaction.visual_continuation_id is not None:
                if interaction.is_super:
                    interaction_info, _ = self._find_interaction(interaction.visual_continuation_id)
                    if interaction_info is not None:
                        if interaction_info.ui_state != Sims_pb2.IQ_QUEUED:
                            self.add_continuation_interaction(interaction)
                            return
            logger.debug('SimId:{}, Interaction added to queue:{}', self._sim.id, interaction)
            int_info = self._add_interaction(self._queued_interactions, interaction, interaction_id_to_insert_after, self.QueueType.Queue)
            if notify_client:
                interaction_messages.send_interactions_add_msg(self._sim, (int_info,), self._should_msg_be_immediate(self.QueueType.Queue))
                int_info.client_notified = True

    def add_continuation_interaction(self, interaction):
        if interaction.visible:
            logger.debug('SimId:{}, Interaction added to continuation:{}', self._sim.id, interaction)
            int_info = self._add_interaction(self._continuation_interactions, interaction, None, self.QueueType.Continuation)
            int_info.source_id = interaction.visual_continuation_id

    def add_running_mixer_interaction(self, si_id, mixer, icon_info, name):
        int_info = self._add_interaction(self._super_interactions, mixer, None, self.QueueType.Super)
        super_int_info_id = self._get_visible_grouped_interaction_id(si_id)
        int_info.super_id = super_int_info_id or si_id
        int_info.set_icon_info(icon_info)
        int_info.display_name = name
        int_info.ui_state = Sims_pb2.IQ_RUNNING
        interaction_messages.send_interactions_add_msg(self._sim, (int_info,), self._should_msg_be_immediate(self.QueueType.Super))

    def running_transition(self, interaction):
        if not interaction.visible:
            return
            interaction_id = interaction.id
            for int_info in self._continuation_interactions:
                if int_info.interaction_id != interaction_id:
                    continue
                int_info.ui_state = Sims_pb2.IQ_TRANSITIONING
                return

            int_info = None
            running_info_for_group = None
            previous_visible_group_info_id = None
            for i, int_info in enumerate(self._queued_interactions):
                if int_info.interaction_id != interaction_id:
                    continue
                int_info.ui_state = Sims_pb2.IQ_TRANSITIONING
                next_index = i + 1
                if next_index < len(self._queued_interactions):
                    self._queued_interactions[next_index].insert_after_id = 0
                previous_visible_group_info_id = self._get_visible_grouped_interaction_id(int_info.interaction_id)
                self._queued_interactions.remove(int_info)
                running_info_for_group = self._add_running_interaction(int_info)
                break
            else:
                logger.debug('SimId:{}, Interaction being marked as transitioning is not in queued interaction:{}', self._sim.id, interaction)
                return

            logger.debug('SimId:{}, Interaction being marked as transitioning:{}', self._sim.id, interaction)
            should_be_immediate = self._should_msg_be_immediate(self.QueueType.Super)
            if running_info_for_group is None or previous_visible_group_info_id is None:
                self._add_routing_interaction_info(int_info)
                if int_info.client_notified:
                    interaction_messages.send_interactions_update_msg(self._sim, (int_info,), should_be_immediate)
            else:
                interaction_messages.send_interactions_add_msg(self._sim, (int_info,), should_be_immediate)
                int_info.client_notified = True
        else:
            visible_int_info = running_info_for_group.pop()
            if int_info.client_notified:
                if visible_int_info is int_info:
                    self._update_mixers(previous_visible_group_info_id, visible_int_info.interaction_id)
                interaction_messages.send_interactions_remove_msg(self._sim, (int_info,), should_be_immediate)
        if visible_int_info is int_info:
            interaction_messages.send_interaction_replace_message(self._sim, previous_visible_group_info_id, int_info, should_be_immediate)
            int_info.client_notified = True

    def transferred_to_si_state(self, interaction):
        self._update_skillbar_info(interaction)
        if not interaction.visible:
            return
        int_info = None
        if interaction.is_super:
            for cur_info in self._running_interactions:
                if cur_info.interaction_id == interaction.id:
                    int_info = cur_info
                    break

        if int_info is None:
            for cur_info in self._queued_interactions:
                if cur_info.interaction_id != interaction.id:
                    continue
                if interaction.is_super:
                    self.running_transition(interaction)
                else:
                    self._queued_interactions.remove(cur_info)
                    if cur_info.super_id != 0:
                        cur_info.super_id = self._get_visible_grouped_interaction_id(cur_info.super_id) or cur_info.super_id
                    self._add_running_interaction(cur_info)
                int_info = cur_info
                break

        if int_info is None:
            logger.debug('SimId:{}, Interaction Transfer To SI State could not find interaction to update:{}', self._sim.id, interaction)
            return
        logger.debug('SimId:{}, Interaction Transfer To SI State being marked as running:{}', self._sim.id, interaction)
        int_info.ui_state = Sims_pb2.IQ_RUNNING
        int_info.ui_visual_type, visual_type_data = interaction.get_interaction_queue_visual_type()
        if visual_type_data.icon is not None:
            int_info.set_icon_info(IconInfoData(icon_resource=(visual_type_data.icon)))
        else:
            if visual_type_data.tooltip_text is not None:
                int_info.display_name = interaction.create_localized_string(visual_type_data.tooltip_text)
            force_remove = int_info.ui_visual_type == Sims_pb2.Interaction.POSTURE
            self._remove_routing_interaction_info(int_info, force_remove=force_remove)
            if int_info.visual_group_tag is None or self._get_visible_grouped_interaction_id(int_info.interaction_id) == int_info.interaction_id:
                if int_info.client_notified:
                    interaction_messages.send_interactions_update_msg(self._sim, (int_info,), False)
                else:
                    interaction_messages.send_interactions_add_msg(self._sim, (int_info,), False)
                    int_info.client_notified = True
        self._update_interaction_for_potential_cancel()

    def remove_queued_interaction(self, interaction):
        if not interaction.visible:
            return
        for index, cur_info in enumerate(self._queued_interactions):
            if interaction.id == cur_info.interaction_id:
                logger.debug('SimId:{}, Interaction Remove(from queue) is being removed from queued list:{}', self._sim.id, interaction)
                if interaction.user_canceled:
                    with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_INTERACTION_CANCEL, sim=(self._sim)) as (hook):
                        hook.write_int('idit', interaction.id)
                        hook.write_int('queu', index)
                int_info = self._queued_interactions.pop(index)
                interaction_messages.send_interactions_remove_msg(self._sim, (int_info,), int_info.ui_state == Sims_pb2.IQ_QUEUED)
                return

        for int_info in self._running_interactions:
            if interaction.id == int_info.interaction_id:
                if int_info.ui_state == Sims_pb2.IQ_TRANSITIONING:
                    previous_visible_group_info_id = self._get_visible_grouped_interaction_id(int_info.interaction_id)
                    group_interactions = self._remove_running_interactions(int_info)
                    self._remove_routing_interaction_info(int_info)
                    if group_interactions:
                        new_visible_interaction_info = group_interactions.pop()
                        if previous_visible_group_info_id == new_visible_interaction_info.interaction_id:
                            return
                            if new_visible_interaction_info.ui_state == Sims_pb2.IQ_RUNNING:
                                interaction_messages.send_interaction_replace_message(self._sim, int_info.interaction_id, new_visible_interaction_info, self._should_msg_be_immediate(self.QueueType.Super))
                        else:
                            interaction_messages.send_interactions_add_msg(self._sim, (new_visible_interaction_info,), self._should_msg_be_immediate(self.QueueType.Super))
                    else:
                        interaction_messages.send_interactions_remove_msg((self._sim), (int_info,), immediate=(interaction.collapsible))
                return

        if self._remove_continuation_interaction(interaction.id):
            logger.debug('SimId:{}, Interaction Remove(from si_state) is being removed from continuation list:{}', self._sim.id, interaction)
            return
        logger.debug('Interaction Remove(from Queue) requested on an interaction not in the ui_manager:{}', interaction)

    def remove_from_si_state(self, interaction):
        self._update_skillbar_info(interaction, from_remove=True)
        interaction_id = interaction.id
        if not interaction.visible:
            return
        logger.debug('SimId:{}, Interaction Remove From SI State attempting to remove:{}', self._sim.id, interaction)
        for cur_info in self._running_interactions:
            if interaction_id != cur_info.interaction_id:
                continue
            int_info = cur_info
            replace_id = self._get_visible_grouped_interaction_id(int_info.interaction_id) or int_info.interaction_id
            group_interactions = self._remove_running_interactions(int_info)
            continuation_info = self._find_continuation(int_info.interaction_id)
            if continuation_info:
                logger.debug('=== Continuation Replace In Remove: ({0} => {1})', int_info.interaction_id, continuation_info.interaction_id)
                if continuation_info.client_notified:
                    logger.error('Trying to replace an interaction that client is already notified. {}, {}', int_info, continuation_info)
                else:
                    if continuation_info.ui_state == Sims_pb2.IQ_TRANSITIONING:
                        self._add_running_interaction(continuation_info)
                    else:
                        self._queued_interactions.insert(0, continuation_info)
                    interaction = self._sim.queue.find_interaction_by_id(continuation_info.interaction_id)
                    if interaction is not None:
                        continuation_info.ui_state = interaction.get_sims_with_invalid_paths() or Sims_pb2.IQ_TRANSITIONING
                        interaction_messages.send_interaction_replace_message(self._sim, replace_id, continuation_info, self._should_msg_be_immediate(self.QueueType.Super))
                    else:
                        continuation_info.client_notified = True
                        for interaction_info in tuple(self._continuation_interactions):
                            if interaction_info.source_id == interaction_id:
                                if interaction_info.ui_state == Sims_pb2.IQ_TRANSITIONING:
                                    self._add_running_interaction(interaction_info)
                                else:
                                    self._queued_interactions.insert(0, interaction_info)
                                    interaction_info.ui_state = Sims_pb2.IQ_TRANSITIONING
                                self._continuation_interactions.remove(interaction_info)
                                interaction_messages.send_interactions_add_msg(self._sim, (interaction_info,), self._should_msg_be_immediate(self.QueueType.Super))
                                interaction_info.client_notified = True

            else:
                logger.debug('=== SimId:{}, Sending Remove MSG for:{}', self._sim.id, interaction)
                self._remove_routing_interaction_info(int_info)
                self._update_routing_interaction_info(int_info)
                if self._last_running_interaction_id == int_info.interaction_id:
                    self._last_running_interaction_id = 0
                interaction_messages.send_interactions_remove_msg(self._sim, (int_info,), self._should_msg_be_immediate(self.QueueType.Super))
                if group_interactions:
                    interaction_messages.send_interactions_add_msg(self._sim, (group_interactions.pop(),), self._should_msg_be_immediate(self.QueueType.Super))
            return

        if self._remove_continuation_interaction(interaction.id):
            logger.debug('SimId:{}, Interaction Remove(from si_state) is being removed from continuation list:{}', self._sim.id, interaction)
            return
        logger.debug('=== Interaction Remove(from SI state) requested on an interaction not in the running interaction list')

    def remove_all_interactions(self):
        del self._queued_interactions[:]
        del self._super_interactions[:]
        del self._continuation_interactions[:]
        self._group_interactions.clear()
        self._routing_info = InteractionInfo.create_routing_info()
        self._last_running_interaction_id = 0
        if self._sim is not None:
            interaction_messages.send_interactions_removeall_msg((self._sim), immediate=True)

    def refresh_ui_data(self):
        interaction_messages.send_interaction_queue_view_add_msg((self._sim), (self.get_interactions_gen()), immediate=True)

    def update_interaction_cancel_status(self, interaction):
        if not interaction.visible:
            return
        int_info, _ = self._find_interaction(interaction.id)
        if int_info is not None:
            int_info.canceled = interaction.is_finishing
            int_info.user_cancelable = interaction.user_cancelable
            interaction_messages.send_interactions_update_msg(self._sim, (int_info,), True)

    def set_interaction_canceled--- This code section failed: ---

 L. 540         0  LOAD_FAST                'self'
                2  LOAD_METHOD              _find_interaction
                4  LOAD_FAST                'int_id'
                6  CALL_METHOD_1         1  '1 positional argument'
                8  UNPACK_SEQUENCE_2     2 
               10  STORE_FAST               'int_info'
               12  STORE_FAST               '_'

 L. 541        14  LOAD_FAST                'int_info'
               16  LOAD_CONST               None
               18  COMPARE_OP               is-not
               20  POP_JUMP_IF_FALSE    58  'to 58'

 L. 542        22  LOAD_FAST                'value'
               24  LOAD_FAST                'int_info'
               26  STORE_ATTR               canceled

 L. 543        28  LOAD_GLOBAL              interaction_messages
               30  LOAD_METHOD              send_interactions_update_msg
               32  LOAD_FAST                'self'
               34  LOAD_ATTR                _sim
               36  LOAD_FAST                'int_info'
               38  BUILD_TUPLE_1         1 
               40  LOAD_CONST               True
               42  CALL_METHOD_3         3  '3 positional arguments'
               44  POP_TOP          

 L. 544        46  LOAD_FAST                'self'
               48  LOAD_METHOD              _remove_routing_interaction_info
               50  LOAD_FAST                'int_info'
               52  CALL_METHOD_1         1  '1 positional argument'
               54  POP_TOP          
               56  JUMP_FORWARD         58  'to 58'
             58_0  COME_FROM            56  '56'
             58_1  COME_FROM            20  '20'

Parse error at or near `COME_FROM' instruction at offset 58_0

    def set_interaction_icon_and_name(self, int_id, icon, name):
        int_info, queue_type = self._find_interaction(int_id)
        if int_info is not None:
            send_update = False
            if icon is not None:
                int_info.set_icon_info(icon)
                send_update = True
            if name is not None:
                int_info.display_name = name
                send_update = True
            if send_update:
                interaction_messages.send_interactions_update_msg(self._sim, (int_info,), self._should_msg_be_immediate(queue_type))

    def set_interaction_super_interaction(self, interaction, super_id):
        int_info, queue_type = self._find_interaction(interaction.id)
        if int_info is not None:
            int_info.super_id = self._get_super_id_for_mixer(super_id) or super_id
            interaction_messages.send_interactions_update_msg(self._sim, (int_info,), self._should_msg_be_immediate(queue_type))

    def get_routing_owner_id(self, id_to_find):
        if id_to_find == interactions.base.interaction.ROUTING_POSTURE_INTERACTION_ID:
            if self._routing_info.routing_owner_id is not None:
                return self._routing_info.routing_owner_id
        return id_to_find

    def _add_interaction(self, interaction_queue, interaction, interaction_id_to_insert_after, queue_type):
        skill = interaction.get_associated_skill()
        ui_visual_type, visual_group_data = interaction.get_interaction_queue_visual_type()
        participants = None
        social_group = interaction.social_group
        if social_group is not None:
            participants = list(social_group)
        if not participants:
            participants = interaction.get_participants(ParticipantType.TargetSim | ParticipantType.Listeners)
        else:
            int_info = InteractionInfo(interaction.id, interaction.user_facing_target, participants, interaction.is_finishing, interaction.user_cancelable, interaction.get_name(), interaction.get_icon_info(), interaction.context.insert_strategy, skill, ui_visual_type, Sims_pb2.IQ_QUEUED, visual_group_data.group_tag, visual_group_data.group_priority, interaction.priority, interaction.mood_list)
            if not interaction.is_super:
                super_interaction = interaction.super_interaction
                if super_interaction is not None and super_interaction is not interaction:
                    int_info.super_id = self._get_super_id_for_mixer(super_interaction.id) or super_interaction.id
                    super_interaction_info, _ = self._find_interaction(int_info.super_id)
                    sa_name = super_interaction_info.display_name if super_interaction_info is not None else None
                else:
                    sa_name = interaction.super_affordance.get_name(target=(interaction.target), context=(interaction.context))
                sa_icon_info = interaction.super_affordance.get_icon_info(target=(interaction.target), context=(interaction.context))
                int_info.set_super_icon_info(sa_name, sa_icon_info)
            if queue_type == self.QueueType.Queue:
                self._add_interaction_info_to_queue(interaction_queue, int_info, interaction, interaction_id_to_insert_after)
            else:
                interaction_queue.append(int_info)
        if interaction.context.source == interactions.context.InteractionSource.PIE_MENU:
            with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_INTERACTION_QUEUE, sim=(self._sim), record_position=True) as (hook):
                hook.write_guid('idix', interaction.guid64)
                hook.write_int('queu', interaction_queue.index(int_info))
                target = interaction.target
                definition_id = 0
                instance_id = 0
                if target is not None:
                    definition_id = target.definition.id if hasattr(target, 'definition') else 0
                    instance_id = target.id
                hook.write_int('trgt', definition_id)
                hook.write_int('tgid', instance_id)
                hook.write_enum('sage', self._sim.age)
        return int_info

    def _add_interaction_info_to_queue(self, interaction_queue, int_info, interaction, interaction_id_to_insert_after):
        queue_len = len(interaction_queue)
        int_info.insert_after_id = self._last_running_interaction_id
        int_info_is_super = int_info.ui_visual_type != Sims_pb2.Interaction.MIXER
        if not queue_len == 0:
            if not (int_info_is_super):
                interaction_queue.append(int_info)
        elif int_info.insert_strategy != interactions.context.QueueInsertStrategy.LAST:
            index_to_add = 0
            if interaction_id_to_insert_after is not None:
                for i, queue_info in enumerate(interaction_queue):
                    if queue_info.interaction_id == interaction_id_to_insert_after:
                        index_to_add = i + 1
                        break

            interaction_queue.insert(index_to_add, int_info)
        else:
            for index, cur_info in enumerate(interaction_queue):
                if cur_info.ui_visual_type != Sims_pb2.Interaction.MIXER and cur_info.insert_strategy == interactions.context.QueueInsertStrategy.LAST:
                    interaction_queue.insert(index, int_info)
                    break
            else:
                interaction_queue.append(int_info)

        index = interaction_queue.index(int_info)
        prev_index = index - 1
        next_index = index + 1
        if prev_index >= 0:
            int_info.insert_after_id = interaction_queue[prev_index].interaction_id
        if next_index < len(interaction_queue):
            interaction_queue[next_index].insert_after_id = int_info.interaction_id

    def _find_interaction(self, int_id):
        for cur_info in self._running_interactions:
            if int_id == cur_info.interaction_id:
                return (
                 cur_info, self.QueueType.Super)

        for cur_info in self._queued_interactions:
            if int_id == cur_info.interaction_id:
                return (
                 cur_info, self.QueueType.Queue)

        for cur_info in self._continuation_interactions:
            if int_id == cur_info.interaction_id:
                return (
                 cur_info, self.QueueType.Continuation)

        return (None, None)

    def _find_continuation(self, int_id):
        for index, cur_info in enumerate(self._continuation_interactions):
            if cur_info.source_id == int_id:
                return self._continuation_interactions.pop(index)

    def _remove_continuation_interaction(self, interaction_id):
        for index, cur_info in enumerate(self._continuation_interactions):
            if interaction_id == cur_info.interaction_id:
                self._continuation_interactions.pop(index)
                return True

        return False

    def _should_msg_be_immediate(self, queue_type):
        if queue_type == self.QueueType.Super:
            return False
        return True

    def _any_interaction_of_visual_type(self, visual_type):
        return any((int_info.is_visual_type_posture() for int_info in self.get_interactions_gen()))

    def _update_skillbar_info(self, interaction, from_remove=False):
        interaction_id = interaction.id
        is_super = interaction.is_super
        if not is_super:
            if interaction.super_interaction is not None:
                interaction_id = interaction.super_interaction.id
        elif self._sim is None:
            logger.error('UI manager sim ref is None for interaction {}, on Sim {} with Target {} with from_remove: {}', interaction, (interaction.sim), (interaction.target), from_remove, owner='camilogarcia')
            return
            sim_info = self._sim.sim_info
            if from_remove:
                if not is_super:
                    if not interaction.is_social:
                        return
                if interaction_id in self._si_skill_mapping:
                    if sim_info is not None:
                        if sim_info.current_skill_guid == self._si_skill_mapping[interaction_id]:
                            sim_info.current_skill_guid = 0
                    del self._si_skill_mapping[interaction_id]
        else:
            skill = interaction.get_associated_skill()
            if skill is not None:
                skill_id = skill.guid64
                self._si_skill_mapping[interaction_id] = skill_id
                if skill_id != self._sim.sim_info.current_skill_guid:
                    self._sim.sim_info.current_skill_guid = skill_id

    def _add_routing_interaction_info(self, routing_interaction_info):
        if self._routing_info.routing_owner_id is not None:
            return
        if self._any_interaction_of_visual_type(Sims_pb2.Interaction.POSTURE):
            return
        self._routing_info.routing_owner_id = routing_interaction_info.interaction_id
        self._routing_info.interactions_to_be_canceled.add(routing_interaction_info.interaction_id)
        self._add_running_interaction(self._routing_info)
        interaction_messages.send_interactions_add_msg(self._sim, (self._routing_info,), self._should_msg_be_immediate(self.QueueType.Super))

    def _remove_routing_interaction_info(self, removing_interaction_info, force_remove=False):
        if self._routing_info.routing_owner_id is None:
            return
        if not force_remove:
            if self._routing_info.routing_owner_id != removing_interaction_info.interaction_id:
                return
        self._remove_running_interactions(self._routing_info)
        interaction_messages.send_interactions_remove_msg(self._sim, (self._routing_info,), self._should_msg_be_immediate(self.QueueType.Super))
        self._routing_info.routing_owner_id = None
        self._routing_info.interactions_to_be_canceled = set()

    def _update_routing_interaction_info(self, interaction_info_removed):
        if not interaction_info_removed.is_visual_type_posture():
            return
        for interaction_info in self.get_interactions_gen():
            if interaction_info == self._routing_info:
                return
                if interaction_info.ui_state == Sims_pb2.IQ_TRANSITIONING:
                    self._add_routing_interaction_info(interaction_info)

    def _update_interaction_for_potential_cancel(self):
        interaction_infos_to_update = set()
        for cur_info in self._super_interactions:
            if cur_info.interaction_id == interactions.base.interaction.ROUTING_POSTURE_INTERACTION_ID:
                continue
            interaction = self._sim.find_interaction_by_id(cur_info.interaction_id)
            if interaction is None:
                continue
            potential_canceled = SIState.potential_canceled_interaction_ids(interaction)
            if not cur_info.interactions_to_be_canceled.symmetric_difference(potential_canceled):
                continue
            cur_info.interactions_to_be_canceled = potential_canceled
            interaction_infos_to_update.add(cur_info)

        if interaction_infos_to_update:
            interaction_messages.send_interactions_update_msg(self._sim, interaction_infos_to_update, self._should_msg_be_immediate(self.QueueType.Super))

    def _update_mixers(self, old_super_id, new_super_id):
        interaction_infos_to_update = []
        for int_info in self._queued_interactions:
            if int_info.super_id == 0:
                continue
            if int_info.super_id != old_super_id:
                continue
            if int_info.super_id == new_super_id:
                continue
            int_info.super_id = new_super_id
            interaction_infos_to_update.append(int_info)

        if interaction_infos_to_update:
            interaction_messages.send_interactions_update_msg(self._sim, interaction_infos_to_update, self._should_msg_be_immediate(self.QueueType.Super))


class InteractionInfo:
    ROUTING_DATA = sims4.tuning.tunable.TunableTuple(description='\n                       Display Name and icon that will be displayed in the\n                       posture area in the interaction queue while an\n                       interaction is transitioning.\n                       ',
      icon=sims4.tuning.tunable.TunableResourceKey(description='\n                            Icon to display in posture slot in UI while\n                            interaction is transitioning.\n                            ',
      default=None,
      resource_types=(sims4.resources.CompoundTypes.IMAGE)),
      routing_name=sims4.localization.TunableLocalizedString(description='\n                            Display name for icon when routing icon appears\n                            in posture slot of UI\n                            '))
    __slots__ = ('interaction_id', '_target_ref', 'participants', 'canceled', 'user_cancelable',
                 'display_name', '_icon', '_icon_info_data', 'ui_state', 'source_id',
                 'associated_skill', 'super_id', 'ui_visual_type', 'insert_after_id',
                 'insert_strategy', 'interactions_to_be_canceled', 'visual_group_tag',
                 'visual_group_priority', 'routing_owner_id', 'client_notified',
                 '_super_display_name', '_super_icon_info_data', 'mood_list', 'priority',
                 'interaction_weakref')

    def __init__(self, interaction_id, target, participants, canceled, user_cancelable, display_name, icon, insert_strategy, associated_skill, visual_type, ui_state, visual_group_tag, visual_group_priority, priority, mood_list):
        self.interaction_id = interaction_id
        self._target_ref = target.ref() if target is not None else None
        self.participants = participants
        self.canceled = canceled
        self.user_cancelable = user_cancelable
        self.display_name = display_name
        self._icon_info_data = None
        self.set_icon_info(icon)
        self.associated_skill = associated_skill.guid64 if associated_skill is not None else None
        self.ui_state = ui_state
        self.priority = priority
        self.source_id = 0
        self.super_id = 0
        self.ui_visual_type = visual_type
        self.visual_group_tag = visual_group_tag if visual_group_tag is not tag.Tag.INVALID else None
        self.visual_group_priority = visual_group_priority
        self.insert_strategy = insert_strategy
        self.routing_owner_id = None
        self.insert_after_id = 0
        self.interactions_to_be_canceled = set()
        self.client_notified = False
        self.mood_list = mood_list
        self._super_display_name = None
        self._super_icon_info_data = None

    @property
    def target(self):
        if self._target_ref:
            return self._target_ref()

    @property
    def icon_info(self):
        return self._icon_info_data

    def set_icon_info(self, icon_info):
        if icon_info is None:
            logger.error('Trying to set icon for interaction with display name:{}', self.display_name)
            return
        self._icon_info_data = icon_info

    def set_super_icon_info(self, name, icon_info):
        self._super_display_name = name
        self._super_icon_info_data = icon_info

    def get_super_icon_info(self):
        return (
         self._super_display_name, self._super_icon_info_data)

    @classmethod
    def create_routing_info(cls):
        routing_info = InteractionInfo(interactions.base.interaction.ROUTING_POSTURE_INTERACTION_ID, None, (), False, True, cls.ROUTING_DATA.routing_name, IconInfoData(icon_resource=(cls.ROUTING_DATA.icon)), None, None, Sims_pb2.Interaction.POSTURE, Sims_pb2.IQ_RUNNING, None, 0, interactions.priority.Priority.High, None)
        return routing_info

    def is_visual_type_posture(self):
        return self.ui_visual_type == Sims_pb2.Interaction.POSTURE

    def __repr__(self):
        if self.interaction_id == interactions.base.interaction.ROUTING_POSTURE_INTERACTION_ID:
            return 'Routing Interaction Info, canceled:{}'.format(self.canceled)
        return 'ID:{}, canceled:{}, ui_state:{}, visual_type:{}, super_id:{}, source_id:{}, insert_after_id:{}'.format(self.interaction_id, self.canceled, self.ui_state, self.ui_visual_type, self.super_id, self.source_id, self.insert_after_id)
