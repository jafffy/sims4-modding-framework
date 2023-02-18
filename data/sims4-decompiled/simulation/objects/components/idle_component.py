# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\idle_component.py
# Compiled at: 2020-07-22 20:11:31
# Size of source mod 2**32: 13977 bytes

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
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
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
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= _lambda_body . 
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
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8 . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
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
returns ::= _stmts return . 
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
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
store ::= expr STORE_ATTR . 
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
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
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
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 221       178  LOAD_CONST               False
->               180  RETURN_VALUE     
import animation.asm, caches, distributor.ops, element_utils, services, sims4
from animation import AnimationContext
from animation.animation_utils import flush_all_animations
from collections import defaultdict
from distributor.system import Distributor
from element_utils import build_critical_section_with_finally, build_element
from objects.components import Component, types, componentmethod_with_fallback, componentmethod
from sims4.tuning.tunable import HasTunableFactory, TunableMapping, TunableReference, OptionalTunable, Tunable, AutoFactoryInit
from sims4.callback_utils import CallableList
from singletons import DEFAULT
from weakref import WeakKeyDictionary
logger = sims4.log.Logger('IdleComponent', default_owner='rmccord')

class IdleComponent(Component, HasTunableFactory, AutoFactoryInit, component_name=types.IDLE_COMPONENT):
    FACTORY_TUNABLES = {'idle_animation_map':TunableMapping(description='\n            The animations that the attached object can play.\n            ',
       key_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
       class_restrictions='ObjectStateValue'),
       value_type=TunableReference(description='\n                The animation to play when the object is in the specified state.\n                If you want the object to stop playing idles, you must tune an\n                animation element corresponding to an ASM state that requests a\n                stop on the object.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.ANIMATION)),
       class_restrictions='ObjectAnimationElement')), 
     'client_suppressed_state':OptionalTunable(description='\n            If enabled, set this object state whenever a client suppression is \n            triggered.\n            For example, when the retail system replaces an object when sold\n            all of its distributables are suppressed so we should stop all\n            animation, vfx, etc. \n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
       class_restrictions='ObjectStateValue')), 
     'parent_name':OptionalTunable(description='\n            If enabled, when the object is parented, its parent will be set as\n            this actor in whatever ASM is playing.\n            ',
       tunable=Tunable(tunable_type=str,
       default=None))}

    def __init__(self, owner, *args, **kwargs):
        (super().__init__)(owner, *args, **kwargs)
        self._asm_registry = WeakKeyDictionary()
        self._animation_context = AnimationContext()
        self._animation_context.add_ref(self)
        self._idle_animation_element = None
        self._current_idle_state_value = None
        self._component_suppressed = False
        self._wakeable_element = None
        self._scheduled_after_callbacks = defaultdict(CallableList)

    def get_asm(self, asm_key, actor_name, setup_asm_func=None, use_cache=True, animation_context=DEFAULT, cache_key=DEFAULT, **kwargs):
        if animation_context is DEFAULT:
            animation_context = self._animation_context
        else:
            if use_cache:
                asm_dict = self._asm_registry.setdefault(animation_context, {})
                asm = None
                if asm_key in asm_dict:
                    asm = asm_dict[asm_key]
                    if asm.current_state == 'exit':
                        asm = None
                if asm is None:
                    asm = animation.asm.create_asm(asm_key, context=animation_context)
                asm_dict[asm_key] = asm
            else:
                asm = animation.asm.create_asm(asm_key, context=animation_context)
            asm.set_actor(actor_name, self.owner)
            if self.parent_name is not None:
                parent = self.owner.parent
                if parent is not None:
                    asm.add_potentially_virtual_actor(actor_name, self.owner, self.parent_name, parent)
            if setup_asm_func is not None:
                result = setup_asm_func(asm)
                if not result:
                    logger.warn("Couldn't setup idle asm {} for {}. {}", asm, self.owner, result)
                    return
        return asm

    @componentmethod
    def get_idle_animation_context(self):
        return self._animation_context

    def add_scheduled_after_callback(self, state, func):
        self._scheduled_after_callbacks[state].register(func)

    def remove_scheduled_after_callback(self, state, func):
        self._scheduled_after_callbacks[state].unregister(func)

    def _refresh_active_idle(self):
        if self._current_idle_state_value is not None:
            if self._idle_animation_element is not None:
                self._trigger_idle_animation(self._current_idle_state_value.state, self._current_idle_state_value, False)

    def _stop_wakeable(self):
        if self._wakeable_element is not None:
            self._wakeable_element.trigger_soft_stop()
            self._wakeable_element = None

    def on_removed_from_inventory(self):
        self._refresh_active_idle()

    def on_state_changed(self, state, old_value, new_value, from_init):
        if not self._trigger_idle_animation(state, new_value, from_init):
            if new_value.anim_overrides is not None:
                if old_value != new_value:
                    self._refresh_active_idle()

    def _trigger_idle_animation--- This code section failed: ---

 L. 193         0  LOAD_DEREF               'self'
                2  LOAD_ATTR                _component_suppressed
                4  POP_JUMP_IF_FALSE    10  'to 10'

 L. 194         6  LOAD_CONST               None
                8  RETURN_VALUE     
             10_0  COME_FROM             4  '4'

 L. 196        10  LOAD_DEREF               'new_value'
               12  LOAD_DEREF               'self'
               14  LOAD_ATTR                idle_animation_map
               16  COMPARE_OP               in
               18  POP_JUMP_IF_FALSE   178  'to 178'

 L. 201        20  LOAD_GLOBAL              services
               22  LOAD_METHOD              current_zone
               24  CALL_METHOD_0         0  '0 positional arguments'
               26  STORE_FAST               'current_zone'

 L. 202        28  LOAD_FAST                'current_zone'
               30  LOAD_CONST               None
               32  COMPARE_OP               is
               34  POP_JUMP_IF_TRUE     46  'to 46'
               36  LOAD_FAST                'from_init'
               38  POP_JUMP_IF_FALSE    50  'to 50'
               40  LOAD_FAST                'current_zone'
               42  LOAD_ATTR                is_zone_loading
               44  POP_JUMP_IF_FALSE    50  'to 50'
             46_0  COME_FROM            34  '34'

 L. 203        46  LOAD_CONST               False
               48  RETURN_VALUE     
             50_0  COME_FROM            44  '44'
             50_1  COME_FROM            38  '38'

 L. 204        50  LOAD_DEREF               'self'
               52  LOAD_ATTR                idle_animation_map
               54  LOAD_DEREF               'new_value'
               56  BINARY_SUBSCR    
               58  STORE_FAST               'new_animation'

 L. 205        60  LOAD_DEREF               'self'
               62  LOAD_METHOD              _stop_animation_element
               64  CALL_METHOD_0         0  '0 positional arguments'
               66  POP_TOP          

 L. 206        68  LOAD_DEREF               'new_value'
               70  LOAD_DEREF               'self'
               72  STORE_ATTR               _current_idle_state_value

 L. 207        74  LOAD_FAST                'new_animation'
               76  LOAD_CONST               None
               78  COMPARE_OP               is-not
               80  POP_JUMP_IF_FALSE   178  'to 178'

 L. 208        82  LOAD_CONST               ()
               84  STORE_FAST               'sequence'

 L. 209        86  LOAD_FAST                'new_animation'
               88  LOAD_ATTR                repeat
               90  POP_JUMP_IF_FALSE   108  'to 108'

 L. 212        92  LOAD_GLOBAL              element_utils
               94  LOAD_METHOD              soft_sleep_forever
               96  CALL_METHOD_0         0  '0 positional arguments'
               98  LOAD_DEREF               'self'
              100  STORE_ATTR               _wakeable_element

 L. 213       102  LOAD_DEREF               'self'
              104  LOAD_ATTR                _wakeable_element
              106  STORE_FAST               'sequence'
            108_0  COME_FROM            90  '90'

 L. 214       108  LOAD_FAST                'new_animation'
              110  LOAD_DEREF               'self'
              112  LOAD_ATTR                owner
              114  LOAD_FAST                'sequence'
              116  LOAD_CONST               ('sequence',)
              118  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              120  STORE_FAST               'animation_element'

 L. 215       122  LOAD_GLOBAL              build_element
              124  LOAD_FAST                'animation_element'

 L. 216       126  LOAD_GLOBAL              flush_all_animations
              128  BUILD_TUPLE_2         2 
              130  CALL_FUNCTION_1       1  '1 positional argument'
              132  STORE_FAST               'core_idle_animation_element'

 L. 217       134  LOAD_GLOBAL              build_critical_section_with_finally
              136  LOAD_FAST                'core_idle_animation_element'

 L. 218       138  LOAD_CLOSURE             'new_value'
              140  LOAD_CLOSURE             'self'
              142  BUILD_TUPLE_2         2 
              144  LOAD_LAMBDA              '<code_object <lambda>>'
              146  LOAD_STR                 'IdleComponent._trigger_idle_animation.<locals>.<lambda>'
              148  MAKE_FUNCTION_8          'closure'
              150  CALL_FUNCTION_2       2  '2 positional arguments'
              152  LOAD_DEREF               'self'
              154  STORE_ATTR               _idle_animation_element

 L. 219       156  LOAD_GLOBAL              services
              158  LOAD_METHOD              time_service
              160  CALL_METHOD_0         0  '0 positional arguments'
              162  LOAD_ATTR                sim_timeline
              164  LOAD_METHOD              schedule
              166  LOAD_DEREF               'self'
              168  LOAD_ATTR                _idle_animation_element
              170  CALL_METHOD_1         1  '1 positional argument'
              172  POP_TOP          

 L. 220       174  LOAD_CONST               True
              176  RETURN_VALUE     
            178_0  COME_FROM            80  '80'
            178_1  COME_FROM            18  '18'

 L. 221       178  LOAD_CONST               False
              180  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 180

    @componentmethod_with_fallback((lambda *_, **__: None))
    def on_client_suppressor_added(self):
        if self.client_suppressed_state is not None:
            self.owner.set_state(self.client_suppressed_state.state, self.client_suppressed_state)
        self._component_suppressed = True

    @componentmethod_with_fallback((lambda *_, **__: None))
    def on_client_suppressor_removed(self, supressors_active):
        if supressors_active:
            return
        self._component_suppressed = False
        if self.client_suppressed_state is not None:
            if self._current_idle_state_value is not None:
                self.owner.set_state(self._current_idle_state_value.state, self._current_idle_state_value)

    def component_reset(self, _):
        self._stop_animation_element(hard_stop=True)

    def post_component_reset(self):
        self.reapply_idle_state()

    def reapply_idle_state(self):
        for current_value in self.idle_animation_map:
            if self.owner.state_value_active(current_value):
                self._trigger_idle_animation(current_value.state, current_value, False)
                return

    def _stop_animation_element(self, hard_stop=False):
        self._stop_wakeable()
        if self._idle_animation_element is not None:
            if hard_stop:
                self._idle_animation_element.trigger_hard_stop()
            else:
                self._idle_animation_element.trigger_soft_stop()
            self._idle_animation_element = None
        self._current_idle_state_value = None

    def on_remove_from_client(self, *_, **__):
        zone = services.current_zone()
        if zone is not None:
            if zone.is_in_build_buy:
                try:
                    reset_op = distributor.ops.ResetObject(self.owner.id)
                    dist = Distributor.instance()
                    dist.add_op(self.owner, reset_op)
                except:
                    logger.exception('Exception thrown sending reset op for {}', self)

    def on_remove(self, *_, **__):
        if self._animation_context is not None:
            self._animation_context.release_ref(self)
            self._animation_context = None
        self._stop_animation_element(hard_stop=True)
