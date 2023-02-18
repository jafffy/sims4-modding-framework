# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\functools.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 33027 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST

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
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 . RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1 . 
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
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
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
continues ::= lastl_stmt . continue
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= call . 
expr ::= compare . 
expr ::= formatted_value1 . 
expr ::= joined_str . 
expr ::= or . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE COME_FROM . 
expr_stmt ::= expr . POP_TOP
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value1 ::= expr FORMAT_VALUE . 
get_iter ::= expr . GET_ITER
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr . expr expr expr BUILD_STRING_4
joined_str ::= expr . expr expr expr expr BUILD_STRING_5
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr . expr expr BUILD_STRING_4
joined_str ::= expr expr . expr expr expr BUILD_STRING_5
joined_str ::= expr expr BUILD_STRING_2 . 
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr . expr BUILD_STRING_4
joined_str ::= expr expr expr . expr expr BUILD_STRING_5
joined_str ::= expr expr expr expr . BUILD_STRING_4
joined_str ::= expr expr expr expr . expr BUILD_STRING_5
jump_absolute_else ::= come_froms . _jump COME_FROM
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr expr . BUILD_LIST_4
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . expr expr expr BUILD_SET_4
set ::= expr expr . expr expr BUILD_SET_4
set ::= expr expr expr . expr BUILD_SET_4
set ::= expr expr expr expr . BUILD_SET_4
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assert2 . 
stmt ::= assign . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
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
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= testfalse_not_and . 
testfalse ::= testfalse_not_or . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true COME_FROM . 
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
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr BUILD_TUPLE_5
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr BUILD_TUPLE_5
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr expr BUILD_TUPLE_5
tuple ::= expr expr expr expr . BUILD_TUPLE_4
tuple ::= expr expr expr expr . expr BUILD_TUPLE_5
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_4 . store store store store
unpack ::= UNPACK_SEQUENCE_4 store . store store store
unpack ::= UNPACK_SEQUENCE_4 store store . store store
unpack ::= UNPACK_SEQUENCE_4 store store store . store
unpack ::= UNPACK_SEQUENCE_4 store store store store . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 297       114  LOAD_GLOBAL              TypeError
                 116  LOAD_STR                 'invalid partial state'
                 118  CALL_FUNCTION_1       1  '1 positional argument'
                 120  RAISE_VARARGS_1       1  'exception instance'
->             122_0  COME_FROM           112  '112'
               122_1  COME_FROM           102  '102'
__all__ = [
 "'update_wrapper'", "'wraps'", "'WRAPPER_ASSIGNMENTS'", "'WRAPPER_UPDATES'", 
 "'total_ordering'", 
 "'cmp_to_key'", "'lru_cache'", "'reduce'", "'partial'", 
 "'partialmethod'", 
 "'singledispatch'"]
try:
    from _functools import reduce
except ImportError:
    pass

from abc import get_cache_token
from collections import namedtuple
from reprlib import recursive_repr
from _thread import RLock
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
WRAPPER_UPDATES = ('__dict__', )

def update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)

    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

    wrapper.__wrapped__ = wrapped
    return wrapper


def wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned,
      updated=updated)


def _gt_from_lt(self, other, NotImplemented=NotImplemented):
    op_result = self.__lt__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result and self != other


def _le_from_lt(self, other, NotImplemented=NotImplemented):
    op_result = self.__lt__(other)
    return op_result or self == other


def _ge_from_lt(self, other, NotImplemented=NotImplemented):
    op_result = self.__lt__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result


def _ge_from_le(self, other, NotImplemented=NotImplemented):
    op_result = self.__le__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result or self == other


def _lt_from_le(self, other, NotImplemented=NotImplemented):
    op_result = self.__le__(other)
    if op_result is NotImplemented:
        return op_result
    return op_result and self != other


def _gt_from_le(self, other, NotImplemented=NotImplemented):
    op_result = self.__le__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result


def _lt_from_gt(self, other, NotImplemented=NotImplemented):
    op_result = self.__gt__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result and self != other


def _ge_from_gt(self, other, NotImplemented=NotImplemented):
    op_result = self.__gt__(other)
    return op_result or self == other


def _le_from_gt(self, other, NotImplemented=NotImplemented):
    op_result = self.__gt__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result


def _le_from_ge(self, other, NotImplemented=NotImplemented):
    op_result = self.__ge__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result or self == other


def _gt_from_ge(self, other, NotImplemented=NotImplemented):
    op_result = self.__ge__(other)
    if op_result is NotImplemented:
        return op_result
    return op_result and self != other


def _lt_from_ge(self, other, NotImplemented=NotImplemented):
    op_result = self.__ge__(other)
    if op_result is NotImplemented:
        return op_result
    return not op_result


_convert = {'__lt__':[
  (
   '__gt__', _gt_from_lt),
  (
   '__le__', _le_from_lt),
  (
   '__ge__', _ge_from_lt)], 
 '__le__':[
  (
   '__ge__', _ge_from_le),
  (
   '__lt__', _lt_from_le),
  (
   '__gt__', _gt_from_le)], 
 '__gt__':[
  (
   '__lt__', _lt_from_gt),
  (
   '__ge__', _ge_from_gt),
  (
   '__le__', _le_from_gt)], 
 '__ge__':[
  (
   '__le__', _le_from_ge),
  (
   '__gt__', _gt_from_ge),
  (
   '__lt__', _lt_from_ge)]}

def total_ordering--- This code section failed: ---

 L. 189         0  LOAD_CLOSURE             'cls'
                2  BUILD_TUPLE_1         1 
                4  LOAD_SETCOMP             '<code_object <setcomp>>'
                6  LOAD_STR                 'total_ordering.<locals>.<setcomp>'
                8  MAKE_FUNCTION_8          'closure'
               10  LOAD_GLOBAL              _convert
               12  GET_ITER         
               14  CALL_FUNCTION_1       1  '1 positional argument'
               16  STORE_FAST               'roots'

 L. 190        18  LOAD_FAST                'roots'
               20  POP_JUMP_IF_TRUE     30  'to 30'

 L. 191        22  LOAD_GLOBAL              ValueError
               24  LOAD_STR                 'must define at least one ordering operation: < > <= >='
               26  CALL_FUNCTION_1       1  '1 positional argument'
               28  RAISE_VARARGS_1       1  'exception instance'
             30_0  COME_FROM            20  '20'

 L. 192        30  LOAD_GLOBAL              max
               32  LOAD_FAST                'roots'
               34  CALL_FUNCTION_1       1  '1 positional argument'
               36  STORE_FAST               'root'

 L. 193        38  SETUP_LOOP           86  'to 86'
               40  LOAD_GLOBAL              _convert
               42  LOAD_FAST                'root'
               44  BINARY_SUBSCR    
               46  GET_ITER         
             48_0  COME_FROM            62  '62'
               48  FOR_ITER             84  'to 84'
               50  UNPACK_SEQUENCE_2     2 
               52  STORE_FAST               'opname'
               54  STORE_FAST               'opfunc'

 L. 194        56  LOAD_FAST                'opname'
               58  LOAD_FAST                'roots'
               60  COMPARE_OP               not-in
               62  POP_JUMP_IF_FALSE    48  'to 48'

 L. 195        64  LOAD_FAST                'opname'
               66  LOAD_FAST                'opfunc'
               68  STORE_ATTR               __name__

 L. 196        70  LOAD_GLOBAL              setattr
               72  LOAD_DEREF               'cls'
               74  LOAD_FAST                'opname'
               76  LOAD_FAST                'opfunc'
               78  CALL_FUNCTION_3       3  '3 positional arguments'
               80  POP_TOP          
               82  JUMP_BACK            48  'to 48'
               84  POP_BLOCK        
             86_0  COME_FROM_LOOP       38  '38'

 L. 197        86  LOAD_DEREF               'cls'
               88  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `None' instruction at offset -1


def cmp_to_key(mycmp):

    class K(object):
        __slots__ = [
         'obj']

        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        __hash__ = None

    return K


try:
    from _functools import cmp_to_key
except ImportError:
    pass

class partial:
    __slots__ = ('func', 'args', 'keywords', '__dict__', '__weakref__')

    def __new__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__new__' of partial needs an argument")
        else:
            if len(args) < 2:
                raise TypeError("type 'partial' takes at least one argument")
            cls, func, *args = args
            assert callable(func), 'the first argument must be callable'
        args = tuple(args)
        if hasattr(func, 'func'):
            args = func.args + args
            tmpkw = func.keywords.copy()
            tmpkw.update(keywords)
            keywords = tmpkw
            del tmpkw
            func = func.func
        self = super(partial, cls).__new__(cls)
        self.func = func
        self.args = args
        self.keywords = keywords
        return self

    def __call__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        self, *args = args
        newkeywords = self.keywords.copy()
        newkeywords.update(keywords)
        return (self.func)(self.args, *args, **newkeywords)

    @recursive_repr()
    def __repr__(self):
        qualname = type(self).__qualname__
        args = [repr(self.func)]
        args.extend((repr(x) for x in self.args))
        args.extend((f"{k}={v!r}" for k, v in self.keywords.items()))
        if type(self).__module__ == 'functools':
            return f"functools.{qualname}({', '.join(args)})"
        return f"{qualname}({', '.join(args)})"

    def __reduce__(self):
        return (
         type(self), (self.func,),
         (self.func, self.args,
          self.keywords or None, self.__dict__ or None))

    def __setstate__--- This code section failed: ---

 L. 289         0  LOAD_GLOBAL              isinstance
                2  LOAD_FAST                'state'
                4  LOAD_GLOBAL              tuple
                6  CALL_FUNCTION_2       2  '2 positional arguments'
                8  POP_JUMP_IF_TRUE     18  'to 18'

 L. 290        10  LOAD_GLOBAL              TypeError
               12  LOAD_STR                 'argument to __setstate__ must be a tuple'
               14  CALL_FUNCTION_1       1  '1 positional argument'
               16  RAISE_VARARGS_1       1  'exception instance'
             18_0  COME_FROM             8  '8'

 L. 291        18  LOAD_GLOBAL              len
               20  LOAD_FAST                'state'
               22  CALL_FUNCTION_1       1  '1 positional argument'
               24  LOAD_CONST               4
               26  COMPARE_OP               !=
               28  POP_JUMP_IF_FALSE    48  'to 48'

 L. 292        30  LOAD_GLOBAL              TypeError
               32  LOAD_STR                 'expected 4 items in state, got '
               34  LOAD_GLOBAL              len
               36  LOAD_FAST                'state'
               38  CALL_FUNCTION_1       1  '1 positional argument'
               40  FORMAT_VALUE          0  ''
               42  BUILD_STRING_2        2 
               44  CALL_FUNCTION_1       1  '1 positional argument'
               46  RAISE_VARARGS_1       1  'exception instance'
             48_0  COME_FROM            28  '28'

 L. 293        48  LOAD_FAST                'state'
               50  UNPACK_SEQUENCE_4     4 
               52  STORE_FAST               'func'
               54  STORE_FAST               'args'
               56  STORE_FAST               'kwds'
               58  STORE_FAST               'namespace'

 L. 294        60  LOAD_GLOBAL              callable
               62  LOAD_FAST                'func'
               64  CALL_FUNCTION_1       1  '1 positional argument'
               66  POP_JUMP_IF_FALSE   114  'to 114'
               68  LOAD_GLOBAL              isinstance
               70  LOAD_FAST                'args'
               72  LOAD_GLOBAL              tuple
               74  CALL_FUNCTION_2       2  '2 positional arguments'
               76  POP_JUMP_IF_FALSE   114  'to 114'

 L. 295        78  LOAD_FAST                'kwds'
               80  LOAD_CONST               None
               82  COMPARE_OP               is-not
               84  POP_JUMP_IF_FALSE    96  'to 96'
               86  LOAD_GLOBAL              isinstance
               88  LOAD_FAST                'kwds'
               90  LOAD_GLOBAL              dict
               92  CALL_FUNCTION_2       2  '2 positional arguments'
               94  POP_JUMP_IF_FALSE   114  'to 114'
             96_0  COME_FROM            84  '84'

 L. 296        96  LOAD_FAST                'namespace'
               98  LOAD_CONST               None
              100  COMPARE_OP               is-not
              102  POP_JUMP_IF_FALSE   122  'to 122'
              104  LOAD_GLOBAL              isinstance
              106  LOAD_FAST                'namespace'
              108  LOAD_GLOBAL              dict
              110  CALL_FUNCTION_2       2  '2 positional arguments'
              112  POP_JUMP_IF_TRUE    122  'to 122'
            114_0  COME_FROM            94  '94'
            114_1  COME_FROM            76  '76'
            114_2  COME_FROM            66  '66'

 L. 297       114  LOAD_GLOBAL              TypeError
              116  LOAD_STR                 'invalid partial state'
              118  CALL_FUNCTION_1       1  '1 positional argument'
              120  RAISE_VARARGS_1       1  'exception instance'
            122_0  COME_FROM           112  '112'
            122_1  COME_FROM           102  '102'

 L. 299       122  LOAD_GLOBAL              tuple
              124  LOAD_FAST                'args'
              126  CALL_FUNCTION_1       1  '1 positional argument'
              128  STORE_FAST               'args'

 L. 300       130  LOAD_FAST                'kwds'
              132  LOAD_CONST               None
              134  COMPARE_OP               is
              136  POP_JUMP_IF_FALSE   144  'to 144'

 L. 301       138  BUILD_MAP_0           0 
              140  STORE_FAST               'kwds'
              142  JUMP_FORWARD        164  'to 164'
            144_0  COME_FROM           136  '136'

 L. 302       144  LOAD_GLOBAL              type
              146  LOAD_FAST                'kwds'
              148  CALL_FUNCTION_1       1  '1 positional argument'
              150  LOAD_GLOBAL              dict
              152  COMPARE_OP               is-not
              154  POP_JUMP_IF_FALSE   164  'to 164'

 L. 303       156  LOAD_GLOBAL              dict
              158  LOAD_FAST                'kwds'
              160  CALL_FUNCTION_1       1  '1 positional argument'
              162  STORE_FAST               'kwds'
            164_0  COME_FROM           154  '154'
            164_1  COME_FROM           142  '142'

 L. 304       164  LOAD_FAST                'namespace'
              166  LOAD_CONST               None
              168  COMPARE_OP               is
              170  POP_JUMP_IF_FALSE   176  'to 176'

 L. 305       172  BUILD_MAP_0           0 
              174  STORE_FAST               'namespace'
            176_0  COME_FROM           170  '170'

 L. 307       176  LOAD_FAST                'namespace'
              178  LOAD_FAST                'self'
              180  STORE_ATTR               __dict__

 L. 308       182  LOAD_FAST                'func'
              184  LOAD_FAST                'self'
              186  STORE_ATTR               func

 L. 309       188  LOAD_FAST                'args'
              190  LOAD_FAST                'self'
              192  STORE_ATTR               args

 L. 310       194  LOAD_FAST                'kwds'
              196  LOAD_FAST                'self'
              198  STORE_ATTR               keywords

Parse error at or near `COME_FROM' instruction at offset 122_0


try:
    from _functools import partial
except ImportError:
    pass

class partialmethod(object):

    def __init__(self, func, *args, **keywords):
        if not callable(func):
            if not hasattr(func, '__get__'):
                raise TypeError('{!r} is not callable or a descriptor'.format(func))
        elif isinstance(func, partialmethod):
            self.func = func.func
            self.args = func.args + args
            self.keywords = func.keywords.copy()
            self.keywords.update(keywords)
        else:
            self.func = func
            self.args = args
            self.keywords = keywords

    def __repr__(self):
        args = ', '.join(map(repr, self.args))
        keywords = ', '.join(('{}={!r}'.format(k, v) for k, v in self.keywords.items()))
        format_string = '{module}.{cls}({func}, {args}, {keywords})'
        return format_string.format(module=(self.__class__.__module__), cls=(self.__class__.__qualname__),
          func=(self.func),
          args=args,
          keywords=keywords)

    def _make_unbound_method(self):

        def _method(*args, **keywords):
            call_keywords = self.keywords.copy()
            call_keywords.update(keywords)
            cls_or_self, *rest = args
            call_args = (cls_or_self,) + self.args + tuple(rest)
            return (self.func)(*call_args, **call_keywords)

        _method.__isabstractmethod__ = self.__isabstractmethod__
        _method._partialmethod = self
        return _method

    def __get__(self, obj, cls):
        get = getattr(self.func, '__get__', None)
        result = None
        if get is not None:
            new_func = get(obj, cls)
            if new_func is not self.func:
                result = partial(new_func, *(self.args), **self.keywords)
                try:
                    result.__self__ = new_func.__self__
                except AttributeError:
                    pass

        if result is None:
            result = self._make_unbound_method().__get__(obj, cls)
        return result

    @property
    def __isabstractmethod__(self):
        return getattr(self.func, '__isabstractmethod__', False)


_CacheInfo = namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize'])

class _HashedSeq(list):
    __slots__ = 'hashvalue'

    def __init__(self, tup, hash=hash):
        self[:] = tup
        self.hashvalue = hash(tup)

    def __hash__(self):
        return self.hashvalue


def _make_key(args, kwds, typed, kwd_mark=(
 object(),), fasttypes={
 int, str, frozenset, type(None)}, tuple=tuple, type=type, len=len):
    key = args
    if kwds:
        key += kwd_mark
        for item in kwds.items():
            key += item

    elif typed:
        key += tuple((type(v) for v in args))
        if kwds:
            key += tuple((type(v) for v in kwds.values()))
    elif len(key) == 1:
        if type(key[0]) in fasttypes:
            return key[0]
    return _HashedSeq(key)


def lru_cache(maxsize=128, typed=False):
    if maxsize is not None:
        if not isinstance(maxsize, int):
            raise TypeError('Expected maxsize to be an integer or None')

    def decorating_function(user_function):
        wrapper = _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo)
        return update_wrapper(wrapper, user_function)

    return decorating_function


def _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo):
    sentinel = object()
    make_key = _make_key
    PREV, NEXT, KEY, RESULT = (0, 1, 2, 3)
    cache = {}
    hits = misses = 0
    full = False
    cache_get = cache.get
    cache_len = cache.__len__
    lock = RLock()
    root = []
    root[:] = [root, root, None, None]
    if maxsize == 0:

        def wrapper(*args, **kwds):
            nonlocal misses
            result = user_function(*args, **kwds)
            misses += 1
            return result

    else:
        if maxsize is None:

            def wrapper(*args, **kwds):
                nonlocal hits
                nonlocal misses
                key = make_key(args, kwds, typed)
                result = cache_get(key, sentinel)
                if result is not sentinel:
                    hits += 1
                    return result
                result = user_function(*args, **kwds)
                cache[key] = result
                misses += 1
                return result

        else:

            def wrapper(*args, **kwds):
                nonlocal full
                nonlocal hits
                nonlocal misses
                nonlocal root
                key = make_key(args, kwds, typed)
                with lock:
                    link = cache_get(key)
                    if link is not None:
                        link_prev, link_next, _key, result = link
                        link_prev[NEXT] = link_next
                        link_next[PREV] = link_prev
                        last = root[PREV]
                        last[NEXT] = root[PREV] = link
                        link[PREV] = last
                        link[NEXT] = root
                        hits += 1
                        return result
                result = user_function(*args, **kwds)
                with lock:
                    if key in cache:
                        pass
                    elif full:
                        oldroot = root
                        oldroot[KEY] = key
                        oldroot[RESULT] = result
                        root = oldroot[NEXT]
                        oldkey = root[KEY]
                        oldresult = root[RESULT]
                        root[KEY] = root[RESULT] = None
                        del cache[oldkey]
                        cache[key] = oldroot
                    else:
                        last = root[PREV]
                        link = [last, root, key, result]
                        last[NEXT] = root[PREV] = cache[key] = link
                        full = cache_len() >= maxsize
                    misses += 1
                return result

    def cache_info():
        with lock:
            return _CacheInfo(hits, misses, maxsize, cache_len())

    def cache_clear():
        nonlocal full
        nonlocal hits
        nonlocal misses
        with lock:
            cache.clear()
            root[:] = [root, root, None, None]
            hits = misses = 0
            full = False

    wrapper.cache_info = cache_info
    wrapper.cache_clear = cache_clear
    return wrapper


try:
    from _functools import _lru_cache_wrapper
except ImportError:
    pass

def _c3_merge(sequences):
    result = []
    while 1:
        sequences = [s for s in sequences if s]
        if not sequences:
            return result
        for s1 in sequences:
            candidate = s1[0]
            for s2 in sequences:
                if candidate in s2[1:]:
                    candidate = None
                    break
            else:
                break

        if candidate is None:
            raise RuntimeError('Inconsistent hierarchy')
        result.append(candidate)
        for seq in sequences:
            if seq[0] == candidate:
                del seq[0]


def _c3_mro(cls, abcs=None):
    for i, base in enumerate(reversed(cls.__bases__)):
        if hasattr(base, '__abstractmethods__'):
            boundary = len(cls.__bases__) - i
            break
    else:
        boundary = 0

    abcs = list(abcs) if abcs else []
    explicit_bases = list(cls.__bases__[:boundary])
    abstract_bases = []
    other_bases = list(cls.__bases__[boundary:])
    for base in abcs:
        if issubclass(cls, base):
            any((issubclass(b, base) for b in cls.__bases__)) or abstract_bases.append(base)

    for base in abstract_bases:
        abcs.remove(base)

    explicit_c3_mros = [_c3_mro(base, abcs=abcs) for base in explicit_bases]
    abstract_c3_mros = [_c3_mro(base, abcs=abcs) for base in abstract_bases]
    other_c3_mros = [_c3_mro(base, abcs=abcs) for base in other_bases]
    return _c3_merge([
     [
      cls]] + explicit_c3_mros + abstract_c3_mros + other_c3_mros + [explicit_bases] + [abstract_bases] + [other_bases])


def _compose_mro(cls, types):
    bases = set(cls.__mro__)

    def is_related(typ):
        return typ not in bases and hasattr(typ, '__mro__') and issubclass(cls, typ)

    types = [n for n in types if is_related(n)]

    def is_strict_base(typ):
        for other in types:
            if typ != other and typ in other.__mro__:
                return True

        return False

    types = [n for n in types if not is_strict_base(n)]
    type_set = set(types)
    mro = []
    for typ in types:
        found = []
        for sub in typ.__subclasses__():
            if sub not in bases and issubclass(cls, sub):
                found.append([s for s in sub.__mro__ if s in type_set])

        if not found:
            mro.append(typ)
            continue
        found.sort(key=len, reverse=True)
        for sub in found:
            for subcls in sub:
                if subcls not in mro:
                    mro.append(subcls)

    return _c3_mro(cls, abcs=mro)


def _find_impl(cls, registry):
    mro = _compose_mro(cls, registry.keys())
    match = None
    for t in mro:
        if match is not None:
            if t in registry:
                if t not in cls.__mro__:
                    if match not in cls.__mro__:
                        if not issubclass(match, t):
                            raise RuntimeError('Ambiguous dispatch: {} or {}'.format(match, t))
            break
        if t in registry:
            match = t

    return registry.get(match)


def singledispatch(func):
    import types, weakref
    registry = {}
    dispatch_cache = weakref.WeakKeyDictionary()
    cache_token = None

    def dispatch(cls):
        nonlocal cache_token
        if cache_token is not None:
            current_token = get_cache_token()
            if cache_token != current_token:
                dispatch_cache.clear()
                cache_token = current_token
        try:
            impl = dispatch_cache[cls]
        except KeyError:
            try:
                impl = registry[cls]
            except KeyError:
                impl = _find_impl(cls, registry)

            dispatch_cache[cls] = impl

        return impl

    def register(cls, func=None):
        nonlocal cache_token
        if func is None:
            if isinstance(cls, type):
                return (lambda f: register(cls, f))
            ann = getattr(cls, '__annotations__', {})
            if not ann:
                raise TypeError(f"Invalid first argument to `register()`: {cls!r}. Use either `@register(some_class)` or plain `@register` on an annotated function.")
            func = cls
            from typing import get_type_hints
            argname, cls = next(iter(get_type_hints(func).items()))
        registry[cls] = func
        if cache_token is None:
            if hasattr(cls, '__abstractmethods__'):
                cache_token = get_cache_token()
        dispatch_cache.clear()
        return func

    def wrapper(*args, **kw):
        return (dispatch(args[0].__class__))(*args, **kw)

    registry[object] = func
    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = types.MappingProxyType(registry)
    wrapper._clear_cache = dispatch_cache.clear
    update_wrapper(wrapper, func)
    return wrapper
