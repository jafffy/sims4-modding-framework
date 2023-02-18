# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\statistics\base_statistic_tracker.py
# Compiled at: 2021-04-22 02:16:56
# Size of source mod 2**32: 35089 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
and ::= expr jmp_false expr COME_FROM . 
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
c_stmts ::= continues . 
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
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
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
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
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
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
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
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
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
testfalse ::= testfalse_not_and . 
testfalse ::= testfalse_not_or . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= and jmp_true . come_froms
testfalse_not_and ::= and jmp_true come_froms . 
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
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
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
   
 L. 586        74  LOAD_FAST                'self'
                  76  LOAD_METHOD              set_value
                  78  LOAD_FAST                'stat_type'
                  80  LOAD_FAST                'stat_type'
                  82  LOAD_ATTR                best_value
                  84  CALL_METHOD_2         2  '2 positional arguments'
                  86  POP_TOP          
                  88  JUMP_BACK            12  'to 12'
->                90  POP_BLOCK        
from sims.sim_info_lod import SimInfoLODLevel
from sims.sim_info_tracker import SimInfoTracker
from singletons import DEFAULT
from statistics.base_statistic import GalleryLoadBehavior
from statistics.base_statistic_listener import BaseStatisticCallbackListener
from traits.trait_type import TraitType
import gsi_handlers, services, sims, sims4.callback_utils, sims4.log, uid
logger = sims4.log.Logger('Statistic')
lod_logger = sims4.log.Logger('LoD', default_owner='miking')
with sims4.reload.protected(globals()):
    _handle_id_gen = uid.UniqueIdGenerator(1)

class BaseStatisticTracker(SimInfoTracker):
    __slots__ = ('_statistics', '_owner', '_watchers', '_delta_watchers', '_listener_seeds',
                 '_on_remove_callbacks', 'suppress_callback_setup_during_load', 'statistics_to_skip_load',
                 'suppress_callback_alarm_calculation', '_recovery_add_in_progress',
                 '_delayed_active_lod_statistics')

    def __init__(self, owner=None):
        self._statistics = None
        self._owner = owner
        self._watchers = None
        self._delta_watchers = None
        self._listener_seeds = None
        self._on_remove_callbacks = None
        self.suppress_callback_setup_during_load = False
        self.suppress_callback_alarm_calculation = False
        self.statistics_to_skip_load = None
        self._recovery_add_in_progress = None
        self._delayed_active_lod_statistics = None

    def __iter__(self):
        if self._statistics is None:
            return iter([])
        stat_iter = self._statistics.values().__iter__()
        return (stat for stat in stat_iter if stat is not None)

    def __len__(self):
        if self._statistics is not None:
            return len(self._statistics)
        return 0

    def all_statistics(self):
        if self._statistics is None:
            return []
        stat_iter = self._statistics.items().__iter__()
        return (stat_type if stat is None else stat for stat_type, stat in stat_iter)

    @property
    def owner(self):
        return self._owner

    def set_callback_alarm_calculation_supression(self, value):
        if self.suppress_callback_alarm_calculation != value:
            self.suppress_callback_alarm_calculation = value
            if not value:
                if self._statistics:
                    for stat in self._statistics.values():
                        if stat is not None:
                            stat._update_callback_listeners()

    def _statistics_values_gen(self):
        if self._statistics:
            for stat in self._statistics.values():
                if stat is not None:
                    yield stat

    def destroy(self):
        for stat in list(self):
            stat.on_remove(on_destroy=True)

        if self._watchers is not None:
            self._watchers.clear()
        self._on_remove_callbacks = None

    def on_initial_startup(self):
        pass

    def remove_statistics_on_travel(self):
        for statistic in tuple(self._statistics_values_gen()):
            stat_type = statistic.persisted or statistic.stat_type
            if not self.owner is None:
                self.owner.is_statistic_type_added_by_modifier(stat_type) or self.remove_statistic(stat_type)

    def _add_callback_listener_seed(self, stat_type, seed):
        if seed is not None:
            if self._listener_seeds is None:
                self._listener_seeds = {}
            if stat_type not in self._listener_seeds:
                self._listener_seeds[stat_type] = []
            if seed not in self._listener_seeds[stat_type]:
                self._listener_seeds[stat_type].append(seed)

    def _remove_callback_listener_seed(self, seed):
        if seed is None:
            return
            if self._listener_seeds is None:
                return
        else:
            stat_type = seed.statistic_type
            if stat_type in self._listener_seeds:
                seeds = self._listener_seeds[stat_type]
                if seed in seeds:
                    seeds.remove(seed)
                    seed.destroy()
                    if not seeds:
                        self._listener_seeds[stat_type]

    def create_and_add_listener(self, stat_type, threshold, callback, on_callback_alarm_reset=None) -> BaseStatisticCallbackListener:
        if stat_type.added_by_default():
            add = stat_type.add_if_not_in_tracker
        else:
            add = False
        stat = self.get_statistic(stat_type, add=add)
        if stat is None:
            seed = stat_type.create_callback_listener_seed(stat_type, threshold,
              callback, on_callback_alarm_reset=on_callback_alarm_reset)
            self._add_callback_listener_seed(stat_type, seed)
            return seed
        callback_listener = stat.create_and_add_callback_listener(threshold, callback, on_callback_alarm_reset=on_callback_alarm_reset)
        return callback_listener

    def remove_listener(self, listener: BaseStatisticCallbackListener):
        stat = self.get_statistic(listener.statistic_type)
        if stat is None:
            self._remove_callback_listener_seed(listener)
        else:
            stat.remove_callback_listener(listener)

    def add_watcher(self, callback):
        if self._watchers is None:
            self._watchers = {}
        handle_id = _handle_id_gen()
        self._watchers[handle_id] = callback
        return handle_id

    def has_watcher(self, handle):
        if self._watchers is None:
            return False
        return handle in self._watchers

    def remove_watcher(self, handle):
        if self._watchers is None:
            return
        del self._watchers[handle]

    def notify_watchers(self, stat_type, old_value, new_value):
        if self._watchers is None:
            return
        for watcher in list(self._watchers.values()):
            watcher(stat_type, old_value, new_value)

    def add_delta_watcher(self, callback):
        if self._delta_watchers is None:
            self._delta_watchers = {}
        handle_id = _handle_id_gen()
        self._delta_watchers[handle_id] = callback
        return handle_id

    def has_delta_watcher(self, handle):
        if self._delta_watchers is None:
            return
        return handle in self._delta_watchers

    def remove_delta_watcher(self, handle):
        if self._delta_watchers is None:
            return
        del self._delta_watchers[handle]

    def notify_delta(self, stat_type, delta):
        if self._delta_watchers is None:
            return
        for watcher in tuple(self._delta_watchers.values()):
            watcher(stat_type, delta)

    def add_on_remove_callback(self, callback):
        if self._on_remove_callbacks is None:
            self._on_remove_callbacks = sims4.callback_utils.RemovableCallableList()
        self._on_remove_callbacks.append(callback)

    def remove_on_remove_callback(self, callback):
        if self._on_remove_callbacks is not None:
            if callback in self._on_remove_callbacks:
                self._on_remove_callbacks.remove(callback)
            if not self._on_remove_callbacks:
                self._on_remove_callbacks = None

    def add_statistic(self, stat_type, owner=None, create_instance=True, **kwargs):
        if self._statistics:
            stat = self._statistics.get(stat_type)
        else:
            stat = None
        if owner is None:
            owner = self._owner
        is_sim = owner.is_sim if owner is not None else False
        if is_sim:
            if stat_type in owner.get_blacklisted_statistics():
                robot_traits = owner.trait_tracker.get_traits_of_type(TraitType.ROBOT)
                if not robot_traits:
                    logger.error('Attempting to add stat {} when it is blacklisted on sim {}.', stat_type, self.owner)
                return
        owner_lod = owner.lod if is_sim else None
        if owner_lod is not None:
            if stat_type.remove_at_owner_lod(lod=owner_lod, owner=owner):
                return
        if stat is None:
            if (stat_type.can_add)(owner, **kwargs):
                stat = stat_type(self)
                if self._statistics is None:
                    self._statistics = {}
                if not create_instance:
                    if not stat.instance_required:
                        self._statistics[stat_type] = None
                        return
                self._statistics[stat_type] = stat
                stat.on_add()
                value = stat.get_value()
                if self._watchers:
                    self.notify_watchers(stat_type, value, value)
                if self._listener_seeds is not None:
                    if stat_type in self._listener_seeds:
                        for seed in self._listener_seeds[stat_type]:
                            seed.stat = stat
                            stat.add_callback_listener(seed)

                        del self._listener_seeds[stat_type]
                        stat._update_callback_listeners(stat_type.default_value, value)
        return stat

    def remove_statistic(self, stat_type, on_destroy=False):
        if self.has_statistic(stat_type):
            stat = self._statistics[stat_type]
            del self._statistics[stat_type]
            if stat is not None:
                if self._on_remove_callbacks:
                    self._on_remove_callbacks(stat)
                stat.on_remove(on_destroy=on_destroy)

    def clear_statistic(self, stat_type):
        if self._statistics:
            if stat_type in self._statistics:
                stat = self._statistics[stat_type]
                if stat is not None:
                    self._statistics[stat_type] = None
                    if self._on_remove_callbacks:
                        self._on_remove_callbacks(stat)
                    stat.on_remove()

    def get_statistic(self, stat_type, add=False):
        try:
            must_end_recovery = False
            if self._statistics:
                stat = self._statistics.get(stat_type)
                if stat is None and self.has_statistic(stat_type):
                    if self._recovery_add_in_progress is None:
                        self._recovery_add_in_progress = set()
                    self._recovery_add_in_progress.add(stat_type)
                    must_end_recovery = True
                    add = True
            else:
                stat = None
            if stat is None:
                if add:
                    stat = self.add_statistic(stat_type)
                    if stat is not None:
                        if self._recovery_add_in_progress is not None:
                            if stat_type in self._recovery_add_in_progress:
                                stat.on_recovery()
            return stat
        finally:
            if must_end_recovery:
                if stat_type in self._recovery_add_in_progress:
                    self._recovery_add_in_progress.remove(stat_type)
                    if not self._recovery_add_in_progress:
                        self._recovery_add_in_progress = None

    def has_statistic(self, stat_type):
        if self._statistics is None:
            return False
        return stat_type in self._statistics

    @property
    def recovery_add_in_progress(self):
        return bool(self._recovery_add_in_progress)

    def get_communicable_statistic_set(self):
        if self._statistics is None:
            return set()
        return {stat_type for stat_type in self._statistics if stat_type.communicable_by_interaction_tag is not None}

    def get_value(self, stat_type, add=False):
        stat = self.get_statistic(stat_type, add=add)
        if stat is None:
            return stat_type.default_value
        return stat.get_value()

    def get_int_value(self, stat_type, scale: int=None):
        value = self.get_value(stat_type)
        if scale is not None:
            value = scale * value / stat_type.max_value
        return int(sims4.math.floor(value))

    def get_user_value(self, stat_type):
        stat_or_stat_type = self.get_statistic(stat_type) or stat_type
        return stat_or_stat_type.get_user_value()

    def set_value(self, stat_type, value, add=DEFAULT, from_load=False, from_init=False, **kwargs):
        if add is DEFAULT:
            add = from_load or stat_type.add_if_not_in_tracker
        if from_init:
            if add:
                if not stat_type.added_by_default():
                    add = False
        stat = self.get_statistic(stat_type, add=add)
        if stat is not None:
            stat.set_value(value, from_load=from_load)

    def set_user_value(self, stat_type, user_value):
        stat = self.get_statistic(stat_type, add=True)
        if stat is not None:
            stat.set_user_value(user_value)

    def add_value(self, stat_type, amount, **kwargs):
        if amount == 0:
            return
        stat = self.get_statistic(stat_type, add=(stat_type.add_if_not_in_tracker))
        if stat is not None:
            (stat.add_value)(amount, **kwargs)

    def set_max(self, stat_type):
        stat = self.get_statistic(stat_type, add=(stat_type.add_if_not_in_tracker))
        if stat is not None:
            self.set_value(stat_type, stat.max_value)

    def set_min(self, stat_type):
        stat = self.get_statistic(stat_type, add=(stat_type.add_if_not_in_tracker))
        if stat is not None:
            self.set_value(stat_type, stat.min_value)

    def get_decay_time(self, stat_type, threshold):
        pass

    def set_convergence(self, stat_type, convergence):
        raise TypeError("This stat type doesn't have a convergence value.")

    def reset_convergence(self, stat_type):
        raise TypeError("This stat type doesn't have a convergence value.")

    def set_all_commodities_to_best_value--- This code section failed: ---

 L. 575         0  SETUP_LOOP           92  'to 92'
                2  LOAD_GLOBAL              list
                4  LOAD_FAST                'self'
                6  LOAD_ATTR                _statistics
                8  CALL_FUNCTION_1       1  '1 positional argument'
               10  GET_ITER         
             12_0  COME_FROM            72  '72'
             12_1  COME_FROM            66  '66'
             12_2  COME_FROM            32  '32'
               12  FOR_ITER             90  'to 90'
               14  STORE_FAST               'stat_type'

 L. 576        16  LOAD_FAST                'self'
               18  LOAD_METHOD              get_statistic
               20  LOAD_FAST                'stat_type'
               22  CALL_METHOD_1         1  '1 positional argument'
               24  STORE_FAST               'stat'

 L. 580        26  LOAD_FAST                'stat'
               28  LOAD_CONST               None
               30  COMPARE_OP               is-not
               32  POP_JUMP_IF_FALSE    12  'to 12'

 L. 581        34  LOAD_FAST                'ignore_ranked'
               36  POP_JUMP_IF_FALSE    46  'to 46'
               38  LOAD_FAST                'stat'
               40  LOAD_ATTR                is_ranked
               42  POP_JUMP_IF_FALSE    46  'to 46'

 L. 582        44  CONTINUE             12  'to 12'
             46_0  COME_FROM            42  '42'
             46_1  COME_FROM            36  '36'

 L. 583        46  LOAD_FAST                'visible_only'
               48  POP_JUMP_IF_TRUE     54  'to 54'
               50  LOAD_FAST                'core_only'
               52  POP_JUMP_IF_FALSE    74  'to 74'
             54_0  COME_FROM            48  '48'

 L. 584        54  LOAD_FAST                'visible_only'
               56  POP_JUMP_IF_FALSE    64  'to 64'
               58  LOAD_FAST                'stat'
               60  LOAD_ATTR                is_visible
               62  POP_JUMP_IF_TRUE     74  'to 74'
             64_0  COME_FROM            56  '56'

 L. 585        64  LOAD_FAST                'core_only'
               66  POP_JUMP_IF_FALSE    12  'to 12'
               68  LOAD_FAST                'stat'
               70  LOAD_ATTR                core
               72  POP_JUMP_IF_FALSE    12  'to 12'
             74_0  COME_FROM            62  '62'
             74_1  COME_FROM            52  '52'

 L. 586        74  LOAD_FAST                'self'
               76  LOAD_METHOD              set_value
               78  LOAD_FAST                'stat_type'
               80  LOAD_FAST                'stat_type'
               82  LOAD_ATTR                best_value
               84  CALL_METHOD_2         2  '2 positional arguments'
               86  POP_TOP          
               88  JUMP_BACK            12  'to 12'
               90  POP_BLOCK        
             92_0  COME_FROM_LOOP        0  '0'

Parse error at or near `POP_BLOCK' instruction at offset 90

    def save(self):
        self.check_for_unneeded_initial_statistics()
        save_list = []
        if self._statistics:
            for stat_type, stat in self._statistics.items():
                if stat_type.persisted:
                    value = stat.get_saved_value() if stat else None
                    save_data = (stat_type.__name__, value)
                    save_list.append(save_data)

        if self._delayed_active_lod_statistics is not None:
            save_list.extend(self._delayed_active_lod_statistics)
        return save_list

    def _should_add_commodity_from_gallery(self, statistic_type, skip_load):
        if statistic_type.gallery_load_behavior == GalleryLoadBehavior.LOAD_FOR_ALL:
            return True
            if self.owner.is_sim:
                if skip_load and statistic_type.gallery_load_behavior != GalleryLoadBehavior.LOAD_ONLY_FOR_SIM:
                    return False
        elif self.owner.is_downloaded:
            if statistic_type.gallery_load_behavior != GalleryLoadBehavior.LOAD_ONLY_FOR_OBJECT:
                return False
        return True

    def load(self, load_list):
        try:
            statistic_manager = services.get_instance_manager(sims4.resources.Types.STATISTIC)
            for stat_type_name, value in load_list:
                stat_cls = statistic_manager.get(stat_type_name)
                if stat_cls is None:
                    continue
                else:
                    if self._sim_info.lod >= stat_cls.min_lod_value:
                        if stat_cls.persisted:
                            self.set_value(stat_cls, value)
                        else:
                            logger.info('Trying to load unavailable STATISTIC resource: {}', stat_type_name)
                if stat_cls.min_lod_value == SimInfoLODLevel.ACTIVE:
                    if self._delayed_active_lod_statistics is None:
                        self._delayed_active_lod_statistics = list()
                    self._delayed_active_lod_statistics.append((stat_type_name, value))

        except ValueError:
            logger.error('Attempting to load old data in BaseStatisticTracker.load()')

        self.check_for_unneeded_initial_statistics()

    def debug_output_all(self, _connection):
        if self._statistics:
            for stat_type, stat in self._statistics.items():
                sims4.commands.output('{:<24} Value: {:-6.2f}'.format(stat_type.__name__, stat.get_value() if stat else 'None'), _connection)

    def debug_set_all_to_best_except(self, stat_to_exclude, core=True):
        for stat_type in list(self._statistics):
            if not core or self.get_statistic(stat_type).core:
                if stat_type != stat_to_exclude:
                    self.set_value(stat_type, stat_type.best_value)

    def debug_set_all_to_min(self, core=True):
        for stat_type in list(self._statistics):
            if not core or self.get_statistic(stat_type).core:
                self.set_value(stat_type, stat_type.min_value)

    def debug_set_all_to_default(self, core=True):
        for stat_type in list(self._statistics):
            if not core or self.get_statistic(stat_type).core:
                self.set_value(stat_type, stat_type.initial_value)

    def _load_delayed_active_statistics(self):
        statistic_manager = services.get_instance_manager(sims4.resources.Types.STATISTIC)
        for stat_type_name, value in self._delayed_active_lod_statistics:
            stat_cls = statistic_manager.get(stat_type_name)
            if stat_cls is None:
                continue
            if stat_cls.persisted:
                self.set_value(stat_cls, value)
            else:
                logger.info('Trying to load unavailable STATISTIC resource: {}', stat_type_name)

        self._delayed_active_lod_statistics = None

    def _get_stat_data_for_active_lod(self, statistic):
        return (
         statistic.guid64, statistic.get_saved_value())

    def on_lod_update(self, old_lod, new_lod):
        if self.owner is None:
            return
        else:
            if not isinstance(self._owner, sims.sim_info.SimInfo):
                raise NotImplementedError('LOD is updating from {} to {} on an non-sim object. This is not supported.'.format(old_lod, new_lod))
            if self._statistics is not None:
                for stat_type in tuple(self._statistics):
                    stat_to_test = self.get_statistic(stat_type)
                    if stat_to_test is not None:
                        if stat_to_test.remove_at_owner_lod(lod=new_lod, owner=(self._owner)):
                            if stat_to_test.min_lod_value == SimInfoLODLevel.ACTIVE:
                                if self._delayed_active_lod_statistics is None:
                                    self._delayed_active_lod_statistics = list()
                                self._delayed_active_lod_statistics.append(self._get_stat_data_for_active_lod(stat_to_test))
                        self.remove_statistic(stat_type)

            if new_lod >= SimInfoLODLevel.ACTIVE and self._delayed_active_lod_statistics is not None:
                self._load_delayed_active_statistics()

    def check_for_unneeded_initial_statistics(self):
        if not self._statistics:
            return
        total_stats = len(self._statistics)
        removed_stats = 0
        for stat_type, stat_to_test in self._statistics.items():
            if not stat_to_test is None:
                if stat_to_test.instance_required:
                    continue
                callback_listeners = stat_to_test.release_control_on_all_callback_listeners()
                for listener in callback_listeners:
                    if listener.should_seed:
                        if hasattr(listener._callback, '__self__'):
                            if listener._callback.__self__ is listener.stat:
                                listener.destroy()
                                continue
                        listener.stat = None
                        stat_type = listener.statistic_type
                        if stat_type is not None:
                            self._add_callback_listener_seed(stat_type, listener)

                if gsi_handlers.statistics_removed_handlers.is_archive_enabled():
                    gsi_handlers.statistics_removed_handlers.archive_removed_statistic(stat_type.__name__, gsi_handlers.gsi_utils.format_object_name(self.owner))
                self.clear_statistic(stat_type)
                removed_stats = removed_stats + 1

        removed_pct = removed_stats / total_stats * 100 if total_stats > 0 else 0
        lod_logger.info('---> {}: Removed {} of {} statistics ({}%)', self.owner, removed_stats, total_stats, removed_pct)
