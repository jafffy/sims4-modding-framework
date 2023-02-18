# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\smtpd.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 35676 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
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
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
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
continues ::= _stmts . lastl_stmt continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_STR . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= if_exp . 
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
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
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
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
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
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
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
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_0 ::= BUILD_MAP_0 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= pos_arg . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
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
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
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
store ::= store_subscript . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
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
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true COME_FROM . 
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
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr BUILD_TUPLE_4
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 464        50  LOAD_FAST                'eq'
                  52  POP_JUMP_IF_FALSE    58  'to 58'
                  54  LOAD_FAST                'value'
                  56  JUMP_FORWARD         60  'to 60'
                58_0  COME_FROM            52  '52'
                  58  LOAD_CONST               True
                60_0  COME_FROM            56  '56'
                  60  LOAD_FAST                'result'
                  62  LOAD_FAST                'param'
                  64  STORE_SUBSCR     
                  66  JUMP_BACK            10  'to 10'
                  68  POP_BLOCK        
->              70_0  COME_FROM_LOOP        4  '4'
import sys, os, errno, getopt, time, socket, asyncore, asynchat, collections
from warnings import warn
from email._header_value_parser import get_addr_spec, get_angle_addr
__all__ = [
 "'SMTPChannel'", "'SMTPServer'", "'DebuggingServer'", "'PureProxy'", 
 "'MailmanProxy'"]
program = sys.argv[0]
__version__ = 'Python SMTP proxy version 0.3'

class Devnull:

    def write(self, msg):
        pass

    def flush(self):
        pass


DEBUGSTREAM = Devnull()
NEWLINE = '\n'
COMMASPACE = ', '
DATA_SIZE_DEFAULT = 33554432

def usage(code, msg=''):
    print((__doc__ % globals()), file=(sys.stderr))
    if msg:
        print(msg, file=(sys.stderr))
    sys.exit(code)


class SMTPChannel(asynchat.async_chat):
    COMMAND = 0
    DATA = 1
    command_size_limit = 512
    command_size_limits = collections.defaultdict(lambda x=command_size_limit: x)

    @property
    def max_command_size_limit(self):
        try:
            return max(self.command_size_limits.values())
        except ValueError:
            return self.command_size_limit

    def __init__(self, server, conn, addr, data_size_limit=DATA_SIZE_DEFAULT, map=None, enable_SMTPUTF8=False, decode_data=False):
        global DEBUGSTREAM
        asynchat.async_chat.__init__(self, conn, map=map)
        self.smtp_server = server
        self.conn = conn
        self.addr = addr
        self.data_size_limit = data_size_limit
        self.enable_SMTPUTF8 = enable_SMTPUTF8
        self._decode_data = decode_data
        if enable_SMTPUTF8:
            if decode_data:
                raise ValueError('decode_data and enable_SMTPUTF8 cannot be set to True at the same time')
        elif decode_data:
            self._emptystring = ''
            self._linesep = '\r\n'
            self._dotsep = '.'
            self._newline = NEWLINE
        else:
            self._emptystring = b''
            self._linesep = b'\r\n'
            self._dotsep = ord(b'.')
            self._newline = b'\n'
        self._set_rset_state()
        self.seen_greeting = ''
        self.extended_smtp = False
        self.command_size_limits.clear()
        self.fqdn = socket.getfqdn()
        try:
            self.peer = conn.getpeername()
        except OSError as err:
            try:
                self.close()
                if err.args[0] != errno.ENOTCONN:
                    raise
                return
            finally:
                err = None
                del err

        print('Peer:', (repr(self.peer)), file=DEBUGSTREAM)
        self.push('220 %s %s' % (self.fqdn, __version__))

    def _set_post_data_state(self):
        self.smtp_state = self.COMMAND
        self.mailfrom = None
        self.rcpttos = []
        self.require_SMTPUTF8 = False
        self.num_bytes = 0
        self.set_terminator(b'\r\n')

    def _set_rset_state(self):
        self._set_post_data_state()
        self.received_data = ''
        self.received_lines = []

    @property
    def __server(self):
        warn("Access to __server attribute on SMTPChannel is deprecated, use 'smtp_server' instead", DeprecationWarning, 2)
        return self.smtp_server

    @_SMTPChannel__server.setter
    def __server(self, value):
        warn("Setting __server attribute on SMTPChannel is deprecated, set 'smtp_server' instead", DeprecationWarning, 2)
        self.smtp_server = value

    @property
    def __line(self):
        warn("Access to __line attribute on SMTPChannel is deprecated, use 'received_lines' instead", DeprecationWarning, 2)
        return self.received_lines

    @_SMTPChannel__line.setter
    def __line(self, value):
        warn("Setting __line attribute on SMTPChannel is deprecated, set 'received_lines' instead", DeprecationWarning, 2)
        self.received_lines = value

    @property
    def __state(self):
        warn("Access to __state attribute on SMTPChannel is deprecated, use 'smtp_state' instead", DeprecationWarning, 2)
        return self.smtp_state

    @_SMTPChannel__state.setter
    def __state(self, value):
        warn("Setting __state attribute on SMTPChannel is deprecated, set 'smtp_state' instead", DeprecationWarning, 2)
        self.smtp_state = value

    @property
    def __greeting(self):
        warn("Access to __greeting attribute on SMTPChannel is deprecated, use 'seen_greeting' instead", DeprecationWarning, 2)
        return self.seen_greeting

    @_SMTPChannel__greeting.setter
    def __greeting(self, value):
        warn("Setting __greeting attribute on SMTPChannel is deprecated, set 'seen_greeting' instead", DeprecationWarning, 2)
        self.seen_greeting = value

    @property
    def __mailfrom(self):
        warn("Access to __mailfrom attribute on SMTPChannel is deprecated, use 'mailfrom' instead", DeprecationWarning, 2)
        return self.mailfrom

    @_SMTPChannel__mailfrom.setter
    def __mailfrom(self, value):
        warn("Setting __mailfrom attribute on SMTPChannel is deprecated, set 'mailfrom' instead", DeprecationWarning, 2)
        self.mailfrom = value

    @property
    def __rcpttos(self):
        warn("Access to __rcpttos attribute on SMTPChannel is deprecated, use 'rcpttos' instead", DeprecationWarning, 2)
        return self.rcpttos

    @_SMTPChannel__rcpttos.setter
    def __rcpttos(self, value):
        warn("Setting __rcpttos attribute on SMTPChannel is deprecated, set 'rcpttos' instead", DeprecationWarning, 2)
        self.rcpttos = value

    @property
    def __data(self):
        warn("Access to __data attribute on SMTPChannel is deprecated, use 'received_data' instead", DeprecationWarning, 2)
        return self.received_data

    @_SMTPChannel__data.setter
    def __data(self, value):
        warn("Setting __data attribute on SMTPChannel is deprecated, set 'received_data' instead", DeprecationWarning, 2)
        self.received_data = value

    @property
    def __fqdn(self):
        warn("Access to __fqdn attribute on SMTPChannel is deprecated, use 'fqdn' instead", DeprecationWarning, 2)
        return self.fqdn

    @_SMTPChannel__fqdn.setter
    def __fqdn(self, value):
        warn("Setting __fqdn attribute on SMTPChannel is deprecated, set 'fqdn' instead", DeprecationWarning, 2)
        self.fqdn = value

    @property
    def __peer(self):
        warn("Access to __peer attribute on SMTPChannel is deprecated, use 'peer' instead", DeprecationWarning, 2)
        return self.peer

    @_SMTPChannel__peer.setter
    def __peer(self, value):
        warn("Setting __peer attribute on SMTPChannel is deprecated, set 'peer' instead", DeprecationWarning, 2)
        self.peer = value

    @property
    def __conn(self):
        warn("Access to __conn attribute on SMTPChannel is deprecated, use 'conn' instead", DeprecationWarning, 2)
        return self.conn

    @_SMTPChannel__conn.setter
    def __conn(self, value):
        warn("Setting __conn attribute on SMTPChannel is deprecated, set 'conn' instead", DeprecationWarning, 2)
        self.conn = value

    @property
    def __addr(self):
        warn("Access to __addr attribute on SMTPChannel is deprecated, use 'addr' instead", DeprecationWarning, 2)
        return self.addr

    @_SMTPChannel__addr.setter
    def __addr(self, value):
        warn("Setting __addr attribute on SMTPChannel is deprecated, set 'addr' instead", DeprecationWarning, 2)
        self.addr = value

    def push(self, msg):
        asynchat.async_chat.push(self, bytes(msg + '\r\n', 'utf-8' if self.require_SMTPUTF8 else 'ascii'))

    def collect_incoming_data(self, data):
        limit = None
        if self.smtp_state == self.COMMAND:
            limit = self.max_command_size_limit
        else:
            if self.smtp_state == self.DATA:
                limit = self.data_size_limit
            else:
                if limit:
                    if self.num_bytes > limit:
                        return
                if limit:
                    self.num_bytes += len(data)
                if self._decode_data:
                    self.received_lines.append(str(data, 'utf-8'))
                else:
                    self.received_lines.append(data)

    def found_terminator(self):
        line = self._emptystring.join(self.received_lines)
        print('Data:', (repr(line)), file=DEBUGSTREAM)
        self.received_lines = []
        if self.smtp_state == self.COMMAND:
            sz, self.num_bytes = self.num_bytes, 0
            if not line:
                self.push('500 Error: bad syntax')
                return
            if not self._decode_data:
                line = str(line, 'utf-8')
            i = line.find(' ')
            if i < 0:
                command = line.upper()
                arg = None
            else:
                command = line[:i].upper()
                arg = line[i + 1:].strip()
            max_sz = self.command_size_limits[command] if self.extended_smtp else self.command_size_limit
            if sz > max_sz:
                self.push('500 Error: line too long')
                return
            method = getattr(self, 'smtp_' + command, None)
            if not method:
                self.push('500 Error: command "%s" not recognized' % command)
                return
            method(arg)
            return
        if self.smtp_state != self.DATA:
            self.push('451 Internal confusion')
            self.num_bytes = 0
            return
        if self.data_size_limit:
            if self.num_bytes > self.data_size_limit:
                self.push('552 Error: Too much mail data')
                self.num_bytes = 0
                return
        data = []
        for text in line.split(self._linesep):
            if text and text[0] == self._dotsep:
                data.append(text[1:])
            else:
                data.append(text)

        self.received_data = self._newline.join(data)
        args = (self.peer, self.mailfrom, self.rcpttos, self.received_data)
        kwargs = {}
        if not self._decode_data:
            kwargs = {'mail_options':self.mail_options,  'rcpt_options':self.rcpt_options}
        status = (self.smtp_server.process_message)(*args, **kwargs)
        self._set_post_data_state()
        if not status:
            self.push('250 OK')
        else:
            self.push(status)

    def smtp_HELO(self, arg):
        if not arg:
            self.push('501 Syntax: HELO hostname')
            return
        if self.seen_greeting:
            self.push('503 Duplicate HELO/EHLO')
            return
        self._set_rset_state()
        self.seen_greeting = arg
        self.push('250 %s' % self.fqdn)

    def smtp_EHLO(self, arg):
        if not arg:
            self.push('501 Syntax: EHLO hostname')
            return
        else:
            if self.seen_greeting:
                self.push('503 Duplicate HELO/EHLO')
                return
            self._set_rset_state()
            self.seen_greeting = arg
            self.extended_smtp = True
            self.push('250-%s' % self.fqdn)
            if self.data_size_limit:
                self.push('250-SIZE %s' % self.data_size_limit)
                self.command_size_limits['MAIL'] += 26
            self._decode_data or self.push('250-8BITMIME')
        if self.enable_SMTPUTF8:
            self.push('250-SMTPUTF8')
            self.command_size_limits['MAIL'] += 10
        self.push('250 HELP')

    def smtp_NOOP(self, arg):
        if arg:
            self.push('501 Syntax: NOOP')
        else:
            self.push('250 OK')

    def smtp_QUIT(self, arg):
        self.push('221 Bye')
        self.close_when_done()

    def _strip_command_keyword(self, keyword, arg):
        keylen = len(keyword)
        if arg[:keylen].upper() == keyword:
            return arg[keylen:].strip()
        return ''

    def _getaddr(self, arg):
        if not arg:
            return ('', '')
        else:
            if arg.lstrip().startswith('<'):
                address, rest = get_angle_addr(arg)
            else:
                address, rest = get_addr_spec(arg)
            return address or (
             address, rest)
        return (
         address.addr_spec, rest)

    def _getparams--- This code section failed: ---

 L. 459         0  BUILD_MAP_0           0 
                2  STORE_FAST               'result'

 L. 460         4  SETUP_LOOP           70  'to 70'
                6  LOAD_FAST                'params'
                8  GET_ITER         
               10  FOR_ITER             68  'to 68'
               12  STORE_FAST               'param'

 L. 461        14  LOAD_FAST                'param'
               16  LOAD_METHOD              partition
               18  LOAD_STR                 '='
               20  CALL_METHOD_1         1  '1 positional argument'
               22  UNPACK_SEQUENCE_3     3 
               24  STORE_FAST               'param'
               26  STORE_FAST               'eq'
               28  STORE_FAST               'value'

 L. 462        30  LOAD_FAST                'param'
               32  LOAD_METHOD              isalnum
               34  CALL_METHOD_0         0  '0 positional arguments'
               36  POP_JUMP_IF_FALSE    46  'to 46'
               38  LOAD_FAST                'eq'
               40  POP_JUMP_IF_FALSE    50  'to 50'
               42  LOAD_FAST                'value'
               44  POP_JUMP_IF_TRUE     50  'to 50'
             46_0  COME_FROM            36  '36'

 L. 463        46  LOAD_CONST               None
               48  RETURN_VALUE     
             50_0  COME_FROM            44  '44'
             50_1  COME_FROM            40  '40'

 L. 464        50  LOAD_FAST                'eq'
               52  POP_JUMP_IF_FALSE    58  'to 58'
               54  LOAD_FAST                'value'
               56  JUMP_FORWARD         60  'to 60'
             58_0  COME_FROM            52  '52'
               58  LOAD_CONST               True
             60_0  COME_FROM            56  '56'
               60  LOAD_FAST                'result'
               62  LOAD_FAST                'param'
               64  STORE_SUBSCR     
               66  JUMP_BACK            10  'to 10'
               68  POP_BLOCK        
             70_0  COME_FROM_LOOP        4  '4'

 L. 465        70  LOAD_FAST                'result'
               72  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM_LOOP' instruction at offset 70_0

    def smtp_HELP(self, arg):
        if arg:
            extended = ' [SP <mail-parameters>]'
            lc_arg = arg.upper()
            if lc_arg == 'EHLO':
                self.push('250 Syntax: EHLO hostname')
            elif lc_arg == 'HELO':
                self.push('250 Syntax: HELO hostname')
            elif lc_arg == 'MAIL':
                msg = '250 Syntax: MAIL FROM: <address>'
                if self.extended_smtp:
                    msg += extended
                self.push(msg)
            elif lc_arg == 'RCPT':
                msg = '250 Syntax: RCPT TO: <address>'
                if self.extended_smtp:
                    msg += extended
                self.push(msg)
            elif lc_arg == 'DATA':
                self.push('250 Syntax: DATA')
            elif lc_arg == 'RSET':
                self.push('250 Syntax: RSET')
            elif lc_arg == 'NOOP':
                self.push('250 Syntax: NOOP')
            elif lc_arg == 'QUIT':
                self.push('250 Syntax: QUIT')
            elif lc_arg == 'VRFY':
                self.push('250 Syntax: VRFY <address>')
            else:
                self.push('501 Supported commands: EHLO HELO MAIL RCPT DATA RSET NOOP QUIT VRFY')
        else:
            self.push('250 Supported commands: EHLO HELO MAIL RCPT DATA RSET NOOP QUIT VRFY')

    def smtp_VRFY(self, arg):
        if arg:
            address, params = self._getaddr(arg)
            if address:
                self.push('252 Cannot VRFY user, but will accept message and attempt delivery')
            else:
                self.push('502 Could not VRFY %s' % arg)
        else:
            self.push('501 Syntax: VRFY <address>')

    def smtp_MAIL(self, arg):
        if not self.seen_greeting:
            self.push('503 Error: send HELO first')
            return
            print('===> MAIL', arg, file=DEBUGSTREAM)
            syntaxerr = '501 Syntax: MAIL FROM: <address>'
            if self.extended_smtp:
                syntaxerr += ' [SP <mail-parameters>]'
            if arg is None:
                self.push(syntaxerr)
                return
            arg = self._strip_command_keyword('FROM:', arg)
            address, params = self._getaddr(arg)
            if not address:
                self.push(syntaxerr)
                return
            if not self.extended_smtp:
                if params:
                    self.push(syntaxerr)
                    return
            if self.mailfrom:
                self.push('503 Error: nested MAIL command')
                return
            self.mail_options = params.upper().split()
            params = self._getparams(self.mail_options)
            if params is None:
                self.push(syntaxerr)
                return
            if not self._decode_data:
                body = params.pop('BODY', '7BIT')
                if body not in ('7BIT', '8BITMIME'):
                    self.push('501 Error: BODY can only be one of 7BIT, 8BITMIME')
                    return
            if self.enable_SMTPUTF8:
                smtputf8 = params.pop('SMTPUTF8', False)
                if smtputf8 is True:
                    self.require_SMTPUTF8 = True
                else:
                    if smtputf8 is not False:
                        self.push('501 Error: SMTPUTF8 takes no arguments')
                        return
        else:
            size = params.pop('SIZE', None)
            if size:
                if not size.isdigit():
                    self.push(syntaxerr)
                    return
                if self.data_size_limit:
                    if int(size) > self.data_size_limit:
                        self.push('552 Error: message size exceeds fixed maximum message size')
                        return
        if len(params.keys()) > 0:
            self.push('555 MAIL FROM parameters not recognized or not implemented')
            return
        self.mailfrom = address
        print('sender:', (self.mailfrom), file=DEBUGSTREAM)
        self.push('250 OK')

    def smtp_RCPT(self, arg):
        if not self.seen_greeting:
            self.push('503 Error: send HELO first')
            return
        else:
            print('===> RCPT', arg, file=DEBUGSTREAM)
            if not self.mailfrom:
                self.push('503 Error: need MAIL command')
                return
            syntaxerr = '501 Syntax: RCPT TO: <address>'
            if self.extended_smtp:
                syntaxerr += ' [SP <mail-parameters>]'
            if arg is None:
                self.push(syntaxerr)
                return
            arg = self._strip_command_keyword('TO:', arg)
            address, params = self._getaddr(arg)
            if not address:
                self.push(syntaxerr)
                return
            if not self.extended_smtp:
                if params:
                    self.push(syntaxerr)
                    return
        self.rcpt_options = params.upper().split()
        params = self._getparams(self.rcpt_options)
        if params is None:
            self.push(syntaxerr)
            return
        if len(params.keys()) > 0:
            self.push('555 RCPT TO parameters not recognized or not implemented')
            return
        self.rcpttos.append(address)
        print('recips:', (self.rcpttos), file=DEBUGSTREAM)
        self.push('250 OK')

    def smtp_RSET(self, arg):
        if arg:
            self.push('501 Syntax: RSET')
            return
        self._set_rset_state()
        self.push('250 OK')

    def smtp_DATA(self, arg):
        if not self.seen_greeting:
            self.push('503 Error: send HELO first')
            return
        else:
            self.rcpttos or self.push('503 Error: need RCPT command')
            return
        if arg:
            self.push('501 Syntax: DATA')
            return
        self.smtp_state = self.DATA
        self.set_terminator(b'\r\n.\r\n')
        self.push('354 End data with <CR><LF>.<CR><LF>')

    def smtp_EXPN(self, arg):
        self.push('502 EXPN not implemented')


class SMTPServer(asyncore.dispatcher):
    channel_class = SMTPChannel

    def __init__(self, localaddr, remoteaddr, data_size_limit=DATA_SIZE_DEFAULT, map=None, enable_SMTPUTF8=False, decode_data=False):
        self._localaddr = localaddr
        self._remoteaddr = remoteaddr
        self.data_size_limit = data_size_limit
        self.enable_SMTPUTF8 = enable_SMTPUTF8
        self._decode_data = decode_data
        if enable_SMTPUTF8:
            if decode_data:
                raise ValueError('decode_data and enable_SMTPUTF8 cannot be set to True at the same time')
        asyncore.dispatcher.__init__(self, map=map)
        try:
            gai_results = (socket.getaddrinfo)(*localaddr, **{'type': socket.SOCK_STREAM})
            self.create_socket(gai_results[0][0], gai_results[0][1])
            self.set_reuse_addr()
            self.bind(localaddr)
            self.listen(5)
        except:
            self.close()
            raise
        else:
            print(('%s started at %s\n\tLocal addr: %s\n\tRemote addr:%s' % (
             self.__class__.__name__, time.ctime(time.time()),
             localaddr, remoteaddr)),
              file=DEBUGSTREAM)

    def handle_accepted(self, conn, addr):
        print(('Incoming connection from %s' % repr(addr)), file=DEBUGSTREAM)
        channel = self.channel_class(self, conn, addr, self.data_size_limit, self._map, self.enable_SMTPUTF8, self._decode_data)

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        raise NotImplementedError


class DebuggingServer(SMTPServer):

    def _print_message_content(self, peer, data):
        inheaders = 1
        lines = data.splitlines()
        for line in lines:
            if inheaders:
                if not line:
                    peerheader = 'X-Peer: ' + peer[0]
                    if not isinstance(data, str):
                        peerheader = repr(peerheader.encode('utf-8'))
                    print(peerheader)
                    inheaders = 0
            if not isinstance(data, str):
                line = repr(line)
            print(line)

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('---------- MESSAGE FOLLOWS ----------')
        if kwargs:
            if kwargs.get('mail_options'):
                print('mail options: %s' % kwargs['mail_options'])
            if kwargs.get('rcpt_options'):
                print('rcpt options: %s\n' % kwargs['rcpt_options'])
        self._print_message_content(peer, data)
        print('------------ END MESSAGE ------------')


class PureProxy(SMTPServer):

    def __init__(self, *args, **kwargs):
        if 'enable_SMTPUTF8' in kwargs:
            if kwargs['enable_SMTPUTF8']:
                raise ValueError('PureProxy does not support SMTPUTF8.')
        (super(PureProxy, self).__init__)(*args, **kwargs)

    def process_message(self, peer, mailfrom, rcpttos, data):
        lines = data.split('\n')
        i = 0
        for line in lines:
            if not line:
                break
            i += 1

        lines.insert(i, 'X-Peer: %s' % peer[0])
        data = NEWLINE.join(lines)
        refused = self._deliver(mailfrom, rcpttos, data)
        print('we got some refusals:', refused, file=DEBUGSTREAM)

    def _deliver(self, mailfrom, rcpttos, data):
        import smtplib
        refused = {}
        try:
            s = smtplib.SMTP()
            s.connect(self._remoteaddr[0], self._remoteaddr[1])
            try:
                refused = s.sendmail(mailfrom, rcpttos, data)
            finally:
                s.quit()

        except smtplib.SMTPRecipientsRefused as e:
            try:
                print('got SMTPRecipientsRefused', file=DEBUGSTREAM)
                refused = e.recipients
            finally:
                e = None
                del e

        except (OSError, smtplib.SMTPException) as e:
            try:
                print('got', (e.__class__), file=DEBUGSTREAM)
                errcode = getattr(e, 'smtp_code', -1)
                errmsg = getattr(e, 'smtp_error', 'ignore')
                for r in rcpttos:
                    refused[r] = (
                     errcode, errmsg)

            finally:
                e = None
                del e

        return refused


class MailmanProxy(PureProxy):

    def __init__(self, *args, **kwargs):
        if 'enable_SMTPUTF8' in kwargs:
            if kwargs['enable_SMTPUTF8']:
                raise ValueError('MailmanProxy does not support SMTPUTF8.')
        (super(PureProxy, self).__init__)(*args, **kwargs)

    def process_message(self, peer, mailfrom, rcpttos, data):
        from io import StringIO
        from Mailman import Utils
        from Mailman import Message
        from Mailman import MailList
        listnames = []
        for rcpt in rcpttos:
            local = rcpt.lower().split('@')[0]
            parts = local.split('-')
            if len(parts) > 2:
                continue
            else:
                listname = parts[0]
                if len(parts) == 2:
                    command = parts[1]
                else:
                    command = ''
            if Utils.list_exists(listname):
                if command not in ('', 'admin', 'owner', 'request', 'join', 'leave'):
                    continue
                listnames.append((rcpt, listname, command))

        for rcpt, listname, command in listnames:
            rcpttos.remove(rcpt)

        print('forwarding recips:', (' '.join(rcpttos)), file=DEBUGSTREAM)
        if rcpttos:
            refused = self._deliver(mailfrom, rcpttos, data)
            print('we got refusals:', refused, file=DEBUGSTREAM)
        mlists = {}
        s = StringIO(data)
        msg = Message.Message(s)
        if not msg.get('from'):
            msg['From'] = mailfrom
        if not msg.get('date'):
            msg['Date'] = time.ctime(time.time())
        for rcpt, listname, command in listnames:
            print('sending message to', rcpt, file=DEBUGSTREAM)
            mlist = mlists.get(listname)
            if not mlist:
                mlist = MailList.MailList(listname, lock=0)
                mlists[listname] = mlist
            if command == '':
                msg.Enqueue(mlist, tolist=1)
            elif command == 'admin':
                msg.Enqueue(mlist, toadmin=1)
            elif command == 'owner':
                msg.Enqueue(mlist, toowner=1)
            elif command == 'request':
                msg.Enqueue(mlist, torequest=1)
            elif command in ('join', 'leave'):
                if command == 'join':
                    msg['Subject'] = 'subscribe'
                else:
                    msg['Subject'] = 'unsubscribe'
                msg.Enqueue(mlist, torequest=1)


class Options:
    setuid = True
    classname = 'PureProxy'
    size_limit = None
    enable_SMTPUTF8 = False


def parseargs():
    global DEBUGSTREAM
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'nVhc:s:du', [
         "'class='", "'nosetuid'", "'version'", "'help'", "'size='", 
         "'debug'", 
         "'smtputf8'"])
    except getopt.error as e:
        try:
            usage(1, e)
        finally:
            e = None
            del e

    options = Options()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage(0)
        elif opt in ('-V', '--version'):
            print(__version__)
            sys.exit(0)
        elif opt in ('-n', '--nosetuid'):
            options.setuid = False
        elif opt in ('-c', '--class'):
            options.classname = arg
        elif opt in ('-d', '--debug'):
            DEBUGSTREAM = sys.stderr
        else:
            if opt in ('-u', '--smtputf8'):
                options.enable_SMTPUTF8 = True

    if len(args) < 1:
        localspec = 'localhost:8025'
        remotespec = 'localhost:25'
    else:
        if len(args) < 2:
            localspec = args[0]
            remotespec = 'localhost:25'
        else:
            if len(args) < 3:
                localspec = args[0]
                remotespec = args[1]
            else:
                usage(1, 'Invalid arguments: %s' % COMMASPACE.join(args))
    i = localspec.find(':')
    if i < 0:
        usage(1, 'Bad local spec: %s' % localspec)
    options.localhost = localspec[:i]
    try:
        options.localport = int(localspec[i + 1:])
    except ValueError:
        usage(1, 'Bad local port: %s' % localspec)

    i = remotespec.find(':')
    if i < 0:
        usage(1, 'Bad remote spec: %s' % remotespec)
    options.remotehost = remotespec[:i]
    try:
        options.remoteport = int(remotespec[i + 1:])
    except ValueError:
        usage(1, 'Bad remote port: %s' % remotespec)

    return options


if __name__ == '__main__':
    options = parseargs()
    classname = options.classname
    if '.' in classname:
        lastdot = classname.rfind('.')
        mod = __import__(classname[:lastdot], globals(), locals(), [''])
        classname = classname[lastdot + 1:]
    else:
        import __main__ as mod
    class_ = getattr(mod, classname)
    proxy = class_((options.localhost, options.localport), (
     options.remotehost, options.remoteport),
      (options.size_limit),
      enable_SMTPUTF8=(options.enable_SMTPUTF8))
    if options.setuid:
        try:
            import pwd
        except ImportError:
            print('Cannot import module "pwd"; try running with -n option.', file=(sys.stderr))
            sys.exit(1)

        nobody = pwd.getpwnam('nobody')[2]
        try:
            os.setuid(nobody)
        except PermissionError:
            print('Cannot setuid "nobody"; try running with -n option.', file=(sys.stderr))
            sys.exit(1)

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
