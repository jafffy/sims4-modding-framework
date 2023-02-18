# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\math.py
# Compiled at: 2022-02-02 16:36:15
# Size of source mod 2**32: 30107 bytes

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
binary_operator ::= BINARY_MULTIPLY . 
binary_operator ::= BINARY_SUBTRACT . 
binary_operator ::= BINARY_TRUE_DIVIDE . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr expr . CALL_METHOD_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= yield . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
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
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_2
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_2
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
pos_arg ::= expr . 
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
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
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
tuple ::= expr expr . BUILD_TUPLE_2
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
yield ::= expr YIELD_VALUE . 
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  81       112  LOAD_FAST                'stop'
                 114  YIELD_VALUE      
                 116  POP_TOP          
               118_0  COME_FROM           110  '110'
->             118_1  COME_FROM            96  '96'
from _animation import get_joint_transform_from_rig
from _math import Vector2, Vector3, Quaternion, Transform, Vector3Immutable, QuaternionImmutable, minimum_distance
from _math import mod_2pi
from collections import namedtuple
from math import pi as PI, sqrt, fmod, floor, atan2, acos, asin, ceil, pi, e
import operator
from sims4.repr_utils import standard_repr
from singletons import DEFAULT
import enum, native.animation, sims4.hash_util, sims4.log
TWO_PI = PI * 2
EPSILON = 1.192092896e-07
EPSILON_SQ = EPSILON * EPSILON
QUATERNION_EPSILON = 0.001
MAX_FLOAT = 3.402823466e+38
MAX_UINT64 = 18446744073709551615
MAX_INT64 = 922337203685477580
MAX_UINT32 = 4294967295
MAX_INT32 = 2147483647
MAX_UINT16 = 65535
MAX_INT16 = 32767
POS_INFINITY = float('inf')
NEG_INFINITY = float('-inf')
FORWARD_AXIS = Vector3.Z_AXIS()
UP_AXIS = Vector3.Y_AXIS()
VECTOR3_ZERO = Vector3.ZERO()
logger = sims4.log.Logger('Sims4Math')

def clamp(lower_bound, x, upper_bound):
    if x < lower_bound:
        return lower_bound
    if x > upper_bound:
        return upper_bound
    return x


def interpolate(starting_value, ending_value, fraction):
    return (1 - fraction) * starting_value + ending_value * fraction


def linear_seq_gen--- This code section failed: ---

 L.  69         0  LOAD_FAST                'stop'
                2  LOAD_FAST                'start'
                4  BINARY_SUBTRACT  
                6  STORE_FAST               'delta'

 L.  70         8  LOAD_GLOBAL              floor
               10  LOAD_GLOBAL              abs
               12  LOAD_FAST                'delta'
               14  LOAD_FAST                'step'
               16  BINARY_TRUE_DIVIDE
               18  CALL_FUNCTION_1       1  '1 positional argument'
               20  CALL_FUNCTION_1       1  '1 positional argument'
               22  STORE_FAST               'num'

 L.  72        24  LOAD_FAST                'max_count'
               26  LOAD_CONST               None
               28  COMPARE_OP               is-not
               30  POP_JUMP_IF_FALSE    46  'to 46'

 L.  73        32  LOAD_GLOBAL              min
               34  LOAD_FAST                'num'
               36  LOAD_FAST                'max_count'
               38  LOAD_CONST               1
               40  BINARY_SUBTRACT  
               42  CALL_FUNCTION_2       2  '2 positional arguments'
               44  STORE_FAST               'num'
             46_0  COME_FROM            30  '30'

 L.  75        46  LOAD_FAST                'num'
               48  LOAD_CONST               0
               50  COMPARE_OP               >
               52  POP_JUMP_IF_FALSE    98  'to 98'

 L.  76        54  SETUP_LOOP          118  'to 118'
               56  LOAD_GLOBAL              range
               58  LOAD_CONST               0
               60  LOAD_FAST                'num'
               62  LOAD_CONST               1
               64  BINARY_ADD       
               66  CALL_FUNCTION_2       2  '2 positional arguments'
               68  GET_ITER         
               70  FOR_ITER             94  'to 94'
               72  STORE_FAST               'i'

 L.  77        74  LOAD_FAST                'start'
               76  LOAD_FAST                'i'
               78  LOAD_FAST                'delta'
               80  BINARY_MULTIPLY  
               82  LOAD_FAST                'num'
               84  BINARY_TRUE_DIVIDE
               86  BINARY_ADD       
               88  YIELD_VALUE      
               90  POP_TOP          
               92  JUMP_BACK            70  'to 70'
               94  POP_BLOCK        
               96  JUMP_FORWARD        118  'to 118'
             98_0  COME_FROM            52  '52'

 L.  79        98  LOAD_FAST                'start'
              100  YIELD_VALUE      
              102  POP_TOP          

 L.  80       104  LOAD_FAST                'stop'
              106  LOAD_FAST                'start'
              108  COMPARE_OP               !=
              110  POP_JUMP_IF_FALSE   118  'to 118'

 L.  81       112  LOAD_FAST                'stop'
              114  YIELD_VALUE      
              116  POP_TOP          
            118_0  COME_FROM           110  '110'
            118_1  COME_FROM            96  '96'
            118_2  COME_FROM_LOOP       54  '54'

Parse error at or near `COME_FROM' instruction at offset 118_1


def deg_to_rad(deg):
    return deg * PI / 180


def rad_to_deg(rad):
    return rad * 180 / PI


def is_angle_in_between(a, start, end):
    _a = sims4.math.mod_2pi(a)
    _start = sims4.math.mod_2pi(start)
    _end = sims4.math.mod_2pi(end)
    if _start <= _end:
        return _start <= _a <= _end
    return _start <= _a or _a <= _end


def angle_abs_difference(a1, a2):
    delta = mod_2pi(a1 - a2)
    if delta > PI:
        delta = TWO_PI - delta
    return delta


def vector_from_seq(list_or_tuple):
    if not list_or_tuple:
        return
    length = len(list_or_tuple)
    if length >= 3:
        return Vector3(list_or_tuple[0], list_or_tuple[1], list_or_tuple[2])
    if length == 2:
        return Vector2(list_or_tuple[0], list_or_tuple[1])


def vector_dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def vector_dot_2d(a, b):
    return a.x * b.x + a.z * b.z


def vector_cross(a, b):
    return Vector3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)


def vector_cross_2d(a, b):
    return a.z * b.x - a.x * b.z


def vector_normalize(v):
    return v / v.magnitude()


def vector_normalize_2d(v):
    s = 1 / v.magnitude_2d()
    return Vector3(v.x * s, 0, v.z * s)


def vector_flatten(v):
    return Vector3(v.x, 0, v.z)


def vector_interpolate(a, b, fraction):
    return a + (b - a) * fraction


def almost_equal(a, b, epsilon=EPSILON):
    return abs(a - b) < epsilon


def almost_equal_sq(a, b, epsilon_sq=EPSILON_SQ):
    return abs(a - b) < epsilon_sq


def vector3_almost_equal(v1, v2, epsilon=EPSILON):
    return abs(v1.x - v2.x) < epsilon and abs(v1.y - v2.y) < epsilon and abs(v1.z - v2.z) < epsilon


def vector3_almost_equal_2d(v1, v2, epsilon=EPSILON):
    return abs(v1.x - v2.x) < epsilon and abs(v1.z - v2.z) < epsilon


def quaternion_almost_equal(q1, q2, epsilon=QUATERNION_EPSILON):
    if abs(q1.x - q2.x) < epsilon:
        if abs(q1.y - q2.y) < epsilon:
            if abs(q1.z - q2.z) < epsilon:
                if abs(q1.w - q2.w) < epsilon:
                    return True
    if abs(q1.x + q2.x) < epsilon:
        if abs(q1.y + q2.y) < epsilon:
            if abs(q1.z + q2.z) < epsilon:
                if abs(q1.w + q2.w) < epsilon:
                    return True
    return False


def transform_almost_equal(t1, t2, epsilon=EPSILON, epsilon_orientation=QUATERNION_EPSILON):
    if epsilon_orientation is DEFAULT:
        epsilon_orientation = epsilon
    return vector3_almost_equal((t1.translation), (t2.translation), epsilon=epsilon) and quaternion_almost_equal((t1.orientation), (t2.orientation), epsilon=epsilon_orientation)


def transform_almost_equal_2d(t1, t2, epsilon=EPSILON, epsilon_orientation=QUATERNION_EPSILON):
    if epsilon_orientation is DEFAULT:
        epsilon_orientation = epsilon
    return vector3_almost_equal_2d((t1.translation), (t2.translation), epsilon=epsilon) and quaternion_almost_equal((t1.orientation), (t2.orientation), epsilon=epsilon_orientation)


def vector3_rotate_axis_angle(v, angle, axis):
    q = Quaternion.from_axis_angle(angle, axis)
    return q.transform_vector(v)


def vector3_angle(v):
    return atan2(v.x, v.z)


def angle_to_yaw_quaternion(angle):
    return Quaternion.from_axis_angle(angle, UP_AXIS)


def yaw_quaternion_to_angle(q):
    logger.assert_log(almost_equal((q.x), 0.0, epsilon=QUATERNION_EPSILON) and almost_equal((q.z), 0.0, epsilon=QUATERNION_EPSILON), '{} is not a rotation around y.', q)
    if almost_equal(q.y, 0.0):
        return 0
    angle = acos(q.w) * 2.0
    if q.y > 0:
        return angle
    return -angle


def get_closest_point_2D(segment, p):
    a1 = segment[0]
    a2 = segment[1]
    x1, x2, x3 = a1.x, a2.x, p.x
    z1, z2, z3 = a1.z, a2.z, p.z
    dx = x2 - x1
    dz = z2 - z1
    t = ((x3 - x1) * dx + (z3 - z1) * dz) / (dx * dx + dz * dz)
    t = clamp(0, t, 1)
    x0 = x1 + t * dx
    z0 = z1 + t * dz
    return Vector3(x0, p.y, z0)


def invert_quaternion(q):
    d = 1.0 / (q.x * q.x + q.y * q.y + q.z * q.z + q.w * q.w)
    return Quaternion(-d * q.x, -d * q.y, -d * q.z, d * q.w)


def get_difference_transform(transform_a, transform_b):
    v = transform_b.translation - transform_a.translation
    a_q_i = invert_quaternion(transform_a.orientation)
    q = Quaternion.concatenate(transform_b.orientation, a_q_i)
    v_prime = Quaternion.transform_vector(a_q_i, v)
    return Transform(v_prime, q)


def get_bounds_2D(points):
    min_x = min((point.x for point in points))
    max_x = max((point.x for point in points))
    min_z = min((point.z for point in points))
    max_z = max((point.z for point in points))
    return (
     Vector2(min_x, min_z), Vector2(max_x, max_z))


def circle_contains_position_2d(circle, position, return_dist_sq=False):
    dist_sq = pow(circle.center.x - position.x, 2) + pow(circle.center.y - position.z, 2)
    return (dist_sq < pow(circle.radius, 2) if not return_dist_sq else dist_sq < pow(circle.radius, 2), dist_sq)


_Location = namedtuple('_Location', ('transform', 'routing_surface', 'parent_ref',
                                     'joint_name_or_hash', 'slot_hash', 'world_routing_surface',
                                     'world_transform'))

class Location(_Location):
    __slots__ = ()
    REQUIRED_PROVIDED_SURFACE_HEIGHT = 0.1

    def __new__(cls, transform, routing_surface, parent=None, joint_name_or_hash=None, slot_hash=0):
        if parent is not None:
            world_routing_surface = cls.get_world_routing_surface(parent, transform, joint_name_or_hash, slot_hash)
            world_transform = cls.get_world_transform(parent, transform, joint_name_or_hash)
            parent = parent.ref()
            routing_surface = None
        else:
            world_transform = transform
            world_routing_surface = routing_surface
        return super().__new__(cls, transform, routing_surface, parent, joint_name_or_hash, slot_hash, world_routing_surface, world_transform)

    @staticmethod
    def get_world_routing_surface(parent, transform, joint_name_or_hash, slot_hash):
        if parent.provided_routing_surface:
            if slot_hash:
                if transform.translation.y > Location.REQUIRED_PROVIDED_SURFACE_HEIGHT:
                    return parent.provided_routing_surface
            if joint_name_or_hash:
                joint_transform = get_joint_transform_from_rig(parent.rig, joint_name_or_hash)
                if joint_transform.translation.y > Location.REQUIRED_PROVIDED_SURFACE_HEIGHT:
                    return parent.provided_routing_surface
        return parent.routing_surface

    @staticmethod
    def get_world_transform(parent, transform, joint_name_or_hash):
        if parent.is_part:
            parent_transform = parent.part_owner.transform
        else:
            parent_transform = parent.transform
        if joint_name_or_hash is None:
            if transform is None:
                return parent_transform
            return Transform.concatenate(transform, parent_transform)
        try:
            joint_transform = native.animation.get_joint_transform_from_rig(parent.rig, joint_name_or_hash)
        except (KeyError, ValueError) as e:
            try:
                return parent_transform
            finally:
                e = None
                del e

        if transform is None:
            return Transform.concatenate(joint_transform, parent_transform)
        local_transform = Transform.concatenate(transform, joint_transform)
        return Transform.concatenate(local_transform, parent_transform)

    def __repr__(self):
        return standard_repr(self, (self.transform), (self.routing_surface), parent=(self.parent),
          joint_name_or_hash=(self.joint_name_or_hash),
          slot_hash=(self.slot_hash))

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        if self.transform != other.transform:
            return False
        if self.world_transform.translation != other.world_transform.translation:
            return False
        if self.parent != other.parent:
            return False
        if self.routing_surface != other.routing_surface:
            return False
        slot_hash0 = self.joint_name_or_hash or self.slot_hash
        slot_hash1 = other.joint_name_or_hash or other.slot_hash
        if slot_hash0 != slot_hash1:
            return False
        return True

    def almost_equal(self, other):
        if self.routing_surface != other.routing_surface:
            return False
        else:
            if not vector3_almost_equal_2d(self.transform.translation, other.transform.translation):
                return False
            return quaternion_almost_equal(self.transform.orientation, other.transform.orientation) or False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((type(self), self.transform, self.parent_ref, self.routing_surface,
         self.joint_name_or_hash, self.slot_hash))

    @property
    def parent(self):
        if self.parent_ref is not None:
            return self.parent_ref()

    @property
    def joint_name_hash(self):
        if self.joint_name_or_hash is None:
            return 0
        if isinstance(self.joint_name_or_hash, int):
            return self.joint_name_or_hash
        return sims4.hash_util.hash32(self.joint_name_or_hash)

    @property
    def zone_id(self):
        if self.world_routing_surface.type == 1:
            return self.world_routing_surface.primary_id
        return sims4.zone_utils.zone_id

    @property
    def level(self):
        return self.world_routing_surface.secondary_id

    def duplicate(self):
        return type(self)(self.transform, self.routing_surface, self.parent, self.joint_name_or_hash, self.slot_hash)

    def clone(self, *, transform=DEFAULT, translation=DEFAULT, orientation=DEFAULT, routing_surface=DEFAULT, parent=DEFAULT, joint_name_or_hash=DEFAULT, slot_hash=DEFAULT):
        if transform is DEFAULT:
            if translation is DEFAULT:
                translation = self.transform.translation
            if orientation is DEFAULT:
                orientation = self.transform.orientation
        else:
            if transform is None:
                raise ValueError('Attempt to pass a None transform into a location clone.')
            if translation is DEFAULT:
                translation = transform.translation
            if orientation is DEFAULT:
                orientation = transform.orientation
        transform = Transform(translation, orientation)
        if routing_surface is DEFAULT:
            routing_surface = self.routing_surface
        if parent is DEFAULT:
            parent = self.parent
        if joint_name_or_hash is DEFAULT:
            joint_name_or_hash = self.joint_name_or_hash
        if slot_hash is DEFAULT:
            slot_hash = self.slot_hash
        return type(self)(transform, routing_surface, parent, joint_name_or_hash, slot_hash)


class LinearCurve:
    __slots__ = ('points', )

    def __init__(self, points):
        self.points = points
        self.points.sort(key=(lambda i: i[0]))

    def get(self, val):
        p_max = len(self.points) - 1
        if val <= self.points[0][0]:
            return self.points[0][1]
        if val >= self.points[p_max][0]:
            return self.points[p_max][1]
        i = p_max - 1
        while i > 0 and val < self.points[i][0]:
            i -= 1

        p1 = self.points[i]
        p2 = self.points[i + 1]
        percent = (val - p1[0]) / (p2[0] - p1[0])
        return (p2[1] - p1[1]) * percent + p1[1]


class WeightedUtilityCurve(LinearCurve):

    def __init__(self, points, max_y=0, weight=1):
        if max_y == 0:
            max_y = self._find_largest_y(points)
        transformed_points = [(point[0], point[1] / max_y * weight) for point in points]
        super().__init__(transformed_points)

    def _find_largest_y(self, points):
        max_y = 0
        for point in points:
            if point[1] > max_y:
                max_y = point[1]

        return max_y


class CircularUtilityCurve(LinearCurve):

    def __init__(self, points, min_x, max_x):
        super().__init__(points)
        self._min_x = min_x
        self._max_x = max_x
        last_point = self.points[-1]
        distance_to_end = max_x - last_point[0]
        total_length = distance_to_end + self.points[0][1]
        distance_to_pivot_point = distance_to_end / total_length
        pivot_y_value = (self.points[0][1] - last_point[1]) * distance_to_pivot_point + self.points[0][1]
        self.points.insert(0, (0, pivot_y_value))
        self.points.insert(len(self.points), (self._max_x, pivot_y_value))

    def get(self, val):
        return super().get(val)


class Operator(enum.Int):
    GREATER = 1
    GREATER_OR_EQUAL = 2
    EQUAL = 3
    NOTEQUAL = 4
    LESS_OR_EQUAL = 5
    LESS = 6

    @staticmethod
    def from_function(fn):
        if fn == operator.gt:
            return Operator.GREATER
        if fn == operator.ge:
            return Operator.GREATER_OR_EQUAL
        if fn == operator.eq:
            return Operator.EQUAL
        if fn == operator.ne:
            return Operator.NOTEQUAL
        if fn == operator.le:
            return Operator.LESS_OR_EQUAL
        if fn == operator.lt:
            return Operator.LESS

    @property
    def function(self):
        if self.value == Operator.GREATER:
            return operator.gt
        if self.value == Operator.GREATER_OR_EQUAL:
            return operator.ge
        if self.value == Operator.EQUAL:
            return operator.eq
        if self.value == Operator.NOTEQUAL:
            return operator.ne
        if self.value == Operator.LESS_OR_EQUAL:
            return operator.le
        if self.value == Operator.LESS:
            return operator.lt

    @property
    def inverse(self):
        if self == Operator.GREATER:
            return Operator.LESS_OR_EQUAL
        if self == Operator.GREATER_OR_EQUAL:
            return Operator.LESS
        if self == Operator.EQUAL:
            return Operator.NOTEQUAL
        if self == Operator.NOTEQUAL:
            return Operator.EQUAL
        if self == Operator.LESS_OR_EQUAL:
            return Operator.GREATER
        if self == Operator.LESS:
            return Operator.GREATER_OR_EQUAL

    @property
    def symbol(self):
        if self == Operator.GREATER:
            return '>'
        if self == Operator.GREATER_OR_EQUAL:
            return '>='
        if self == Operator.EQUAL:
            return '=='
        if self == Operator.NOTEQUAL:
            return '!='
        if self == Operator.LESS_OR_EQUAL:
            return '<='
        if self == Operator.LESS:
            return '<'

    @property
    def category(self):
        if self == Operator.GREATER:
            return Operator.GREATER
        if self == Operator.GREATER_OR_EQUAL:
            return Operator.GREATER
        if self == Operator.EQUAL:
            return Operator.EQUAL
        if self == Operator.NOTEQUAL:
            return Operator.EQUAL
        if self == Operator.LESS_OR_EQUAL:
            return Operator.LESS
        if self == Operator.LESS:
            return Operator.LESS


class InequalityOperator(enum.Int):
    GREATER = Operator.GREATER
    GREATER_OR_EQUAL = Operator.GREATER_OR_EQUAL
    LESS_OR_EQUAL = Operator.LESS_OR_EQUAL
    LESS = Operator.LESS


with InequalityOperator.__reload_context__(InequalityOperator, InequalityOperator):
    InequalityOperator.from_function = Operator.from_function
    InequalityOperator.function = Operator.function
    InequalityOperator.inverse = Operator.inverse
    InequalityOperator.symbol = Operator.symbol
    InequalityOperator.category = Operator.category

class Threshold:
    __slots__ = ('value', 'comparison')

    def __init__(self, value=None, comparison=None):
        self.value = value
        self.comparison = comparison

    def compare(self, source_value):
        if self.value is not None:
            if self.comparison is not None:
                return self.comparison(source_value, self.value)
        return False

    def compare_value(self, source_value):
        if self.value is not None:
            if self.comparison is not None:
                return self.comparison(source_value.value, self.value.value)
        return False

    def inverse(self):
        return Threshold(self.value, Operator.from_function(self.comparison).inverse.function)

    def __str__(self):
        if self.comparison is None:
            return 'None'
        return '{} {}'.format(Operator.from_function(self.comparison).symbol, self.value)

    def __repr__(self):
        return '<Threshold {}>'.format(str(self))

    def __eq__(self, other):
        if not isinstance(other, Threshold):
            return False
        else:
            if not self.value == other.value:
                return False
            return self.comparison == other.comparison or False
        return True

    def __hash__(self):
        return hash((self.value, self.comparison))


def safe_max(*args, default=None, **kwargs):
    try:
        return max(*args, **kwargs)
    except ValueError:
        return default


def safe_min(*args, default=None, **kwargs):
    try:
        return max(*args, **kwargs)
    except ValueError:
        return default
