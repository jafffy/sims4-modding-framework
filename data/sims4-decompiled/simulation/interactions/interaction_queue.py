# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\interaction_queue.py
# Compiled at: 2020-02-26 02:42:10
# Size of source mod 2**32: 81649 bytes

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
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 . RAISE_VARARGS_1
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
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
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
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
continues ::= _stmts . lastl_stmt continue
continues ::= lastl_stmt . continue
else_suite ::= suite_stmts . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
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
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
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
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= iflaststmtl . 
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
lstmt ::= stmt . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR MAKE_FUNCTION_1 . 
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
or ::= expr_pjit_come_from . expr
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
returns ::= _stmts return . 
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
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
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
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse ::= testfalse_not_or . 
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 313        28  LOAD_FAST                'self'
                  30  LOAD_ATTR                _interactions
                  32  LOAD_METHOD              append
                  34  LOAD_FAST                'interaction'
                  36  CALL_METHOD_1         1  '1 positional argument'
                  38  POP_TOP          
->                40  JUMP_FORWARD        134  'to 134'
                42_0  COME_FROM            26  '26'
from _weakrefset import WeakSet
from contextlib import contextmanager
import weakref
from carry.pick_up_sim_liability import PickUpSimLiability
from clock import ClockSpeedMode
from event_testing.resolver import InteractionResolver
from event_testing.results import TestResult
from interactions import ParticipantType, PipelineProgress
from interactions.base.interaction import InteractionFailureOptions
from interactions.base.interaction_constants import InteractionQueuePreparationStatus
from interactions.constraints import Nowhere
from interactions.context import InteractionBucketType, InteractionContext, InteractionSource, QueueInsertStrategy
from interactions.interaction_finisher import FinishingType
from interactions.priority import Priority, can_priority_displace, can_displace
from interactions.utils.interaction_liabilities import CANCEL_AOP_LIABILITY
from postures.transition_sequence import TransitionSequenceController, DerailReason
from sims.sim_log import log_interaction
from sims4.callback_utils import CallableList
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, TunableRange, Tunable
from singletons import UNSET
import clock, element_utils, elements, gsi_handlers.sim_timeline_handlers, performance.counters, scheduling, services, sims4.log
__all__ = [
 'InteractionQueue', 'QueueView']
logger = sims4.log.Logger('Interaction Queue')

class BucketBase:
    __slots__ = '_sim_ref'

    def __init__(self, sim):
        self._sim_ref = sim.ref()

    @property
    def _sim(self):
        if self._sim_ref is not None:
            return self._sim_ref()

    def __iter__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def get_next_unblocked_interaction(self, blocked_sims_callback=None):
        for interaction in self:
            interaction.notify_queue_head()
            if interaction.is_finishing:
                continue
            return interaction

    def get_next_unblocked_interaction_cancel_incompatible(self, blocked_sims_callback=None):
        result = None
        to_cancel = []
        for interaction in self:
            interaction.notify_queue_head()
            if interaction.is_finishing:
                continue
            if interaction.is_super:
                if interaction.is_affordance_locked:
                    continue
                sims_with_invalid_paths = interaction.get_sims_with_invalid_paths()
                if sims_with_invalid_paths:
                    if blocked_sims_callback is not None:
                        blocked_sims_callback(sims_with_invalid_paths)
                    to_cancel.append(interaction)
                    logger.debug('Canceling incompatible interaction {} in bucket {}', interaction, self, owner='PI')
                    continue
            result = interaction
            break

        for interaction in to_cancel:
            interaction.cancel(FinishingType.INTERACTION_INCOMPATIBILITY, 'Canceled an incompatible interaction in a base bucket')

        return result

    def _append(self, interaction):
        raise NotImplementedError()

    def append(self, interaction):
        log_interaction('Enqueue', interaction)
        result = self._append(interaction)
        return result

    def _insert_next(self, interaction, insert_after=None):
        raise NotImplementedError()

    def insert_next(self, interaction, **kwargs):
        log_interaction('Enqueue_Next', interaction)
        result = (self._insert_next)(interaction, **kwargs)
        return result

    def _clear_interaction(self, interaction):
        raise NotImplementedError()

    def clear_interaction(self, interaction):
        ret = self._clear_interaction(interaction)
        if ret:
            interaction.on_removed_from_queue()
        return ret

    def remove_for_perform(self, interaction):
        if self._clear_interaction(interaction):
            return interaction

    def on_reset(self):
        for interaction in list(self):
            try:
                log_interaction('Reset', interaction)
                self.clear_interaction(interaction)
                interaction.on_reset()
            except Exception:
                logger.exception('Exception caught while clearing interaction from bucket:')


class BucketSingle(BucketBase):
    __slots__ = ('_interaction', )

    def __init__(self, sim):
        super().__init__(sim)
        self._interaction = None

    def __iter__(self):
        if self._interaction is not None:
            yield self._interaction

    def __len__(self):
        if self._interaction is not None:
            return 1
        return 0

    def _enqueue(self, interaction):
        if self._interaction is not None:
            if not self._interaction.is_finishing:
                if not self._interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg=('Bucket Single Enqueue: {}'.format(interaction))):
                    return TestResult(False, 'Unable to cancel existing interaction ({}) in BucketSingle.'.format(self._interaction))
        self._interaction = interaction
        return TestResult.TRUE

    def _append(self, interaction):
        result = self._enqueue(interaction)
        return result

    def _insert_next(self, interaction, insert_after=None):
        return self._enqueue(interaction)

    def _clear_interaction(self, interaction):
        if self._interaction is interaction:
            self._interaction = None
            interaction.on_removed_from_queue()
            return True
        return False


class BucketList(BucketBase):
    __slots__ = ('_interactions', )

    def __init__(self, sim):
        self._sim_ref = sim.ref()
        self._interactions = []

    def __iter__(self):
        return iter(self._interactions)

    def __len__(self):
        return len(self._interactions)

    def _append(self, interaction):
        self._interactions.append(interaction)
        return TestResult.TRUE

    def _insert_next(self, interaction, insert_after=None):
        index = 0
        if insert_after is not None:
            for i, queued_interaction in enumerate(self._interactions):
                if interaction.group_id == queued_interaction.group_id or queued_interaction is insert_after:
                    index = i + 1

        self._interactions.insert(index, interaction)
        return TestResult.TRUE

    def _clear_interaction(self, interaction):
        if not self._interactions or interaction not in self._interactions:
            return False
        self._interactions.remove(interaction)
        interaction.on_removed_from_queue()
        return True


class InteractionBucket(BucketList):
    __slots__ = ()

    def _append--- This code section failed: ---

 L. 310         0  LOAD_FAST                'interaction'
                2  LOAD_ATTR                is_super
                4  POP_JUMP_IF_TRUE     28  'to 28'

 L. 311         6  LOAD_GLOBAL              len
                8  LOAD_FAST                'self'
               10  LOAD_ATTR                _interactions
               12  CALL_FUNCTION_1       1  '1 positional argument'
               14  LOAD_CONST               0
               16  COMPARE_OP               ==
               18  POP_JUMP_IF_TRUE     28  'to 28'

 L. 312        20  LOAD_FAST                'interaction'
               22  LOAD_METHOD              should_insert_in_queue_on_append
               24  CALL_METHOD_0         0  '0 positional arguments'
               26  POP_JUMP_IF_TRUE     42  'to 42'
             28_0  COME_FROM            18  '18'
             28_1  COME_FROM             4  '4'

 L. 313        28  LOAD_FAST                'self'
               30  LOAD_ATTR                _interactions
               32  LOAD_METHOD              append
               34  LOAD_FAST                'interaction'
               36  CALL_METHOD_1         1  '1 positional argument'
               38  POP_TOP          
               40  JUMP_FORWARD        134  'to 134'
             42_0  COME_FROM            26  '26'

 L. 318        42  SETUP_LOOP          134  'to 134'
               44  LOAD_GLOBAL              enumerate
               46  LOAD_FAST                'self'
               48  LOAD_ATTR                _interactions
               50  CALL_FUNCTION_1       1  '1 positional argument'
               52  GET_ITER         
             54_0  COME_FROM            80  '80'
             54_1  COME_FROM            66  '66'
               54  FOR_ITER            120  'to 120'
               56  UNPACK_SEQUENCE_2     2 
               58  STORE_FAST               'i'
               60  STORE_FAST               'queued_interaction'

 L. 319        62  LOAD_FAST                'queued_interaction'
               64  LOAD_ATTR                is_super
               66  POP_JUMP_IF_FALSE    54  'to 54'
               68  LOAD_FAST                'queued_interaction'
               70  LOAD_ATTR                context
               72  LOAD_ATTR                insert_strategy
               74  LOAD_GLOBAL              QueueInsertStrategy
               76  LOAD_ATTR                LAST
               78  COMPARE_OP               ==
               80  POP_JUMP_IF_FALSE    54  'to 54'

 L. 320        82  LOAD_FAST                'queued_interaction'
               84  LOAD_ATTR                transition
               86  LOAD_CONST               None
               88  COMPARE_OP               is-not
               90  POP_JUMP_IF_FALSE   102  'to 102'
               92  LOAD_FAST                'queued_interaction'
               94  LOAD_ATTR                transition
               96  LOAD_ATTR                running
               98  POP_JUMP_IF_FALSE   102  'to 102'

 L. 324       100  CONTINUE             54  'to 54'
            102_0  COME_FROM            98  '98'
            102_1  COME_FROM            90  '90'

 L. 325       102  LOAD_FAST                'self'
              104  LOAD_ATTR                _interactions
              106  LOAD_METHOD              insert
              108  LOAD_FAST                'i'
              110  LOAD_FAST                'interaction'
              112  CALL_METHOD_2         2  '2 positional arguments'
              114  POP_TOP          

 L. 326       116  BREAK_LOOP       
              118  JUMP_BACK            54  'to 54'
              120  POP_BLOCK        

 L. 328       122  LOAD_FAST                'self'
              124  LOAD_ATTR                _interactions
              126  LOAD_METHOD              append
              128  LOAD_FAST                'interaction'
              130  CALL_METHOD_1         1  '1 positional argument'
              132  POP_TOP          
            134_0  COME_FROM_LOOP       42  '42'
            134_1  COME_FROM            40  '40'

 L. 329       134  LOAD_GLOBAL              TestResult
              136  LOAD_ATTR                TRUE
              138  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_FORWARD' instruction at offset 40

    def get_next_unblocked_interaction(self, blocked_sims_callback=None):
        interactions_iter = iter(self)
        for interaction in interactions_iter:
            interaction.notify_queue_head()
            if interaction.is_finishing:
                continue
            if interaction.is_super:
                if interaction.is_affordance_locked:
                    continue
                sims_with_invalid_paths = interaction.get_sims_with_invalid_paths()
                if sims_with_invalid_paths:
                    if blocked_sims_callback is not None:
                        blocked_sims_callback(sims_with_invalid_paths)
                    interaction.on_incompatible_in_queue()
                    break
            return interaction

        for interaction in interactions_iter:
            interaction.is_super or interaction.notify_queue_head()
            if interaction.is_finishing or interaction.super_interaction is not None and interaction.super_interaction in self._sim.si_state:
                return interaction.super_interaction.is_finishing or interaction


class AutonomyBucket(BucketList):
    __slots__ = ()
    get_next_unblocked_interaction = BucketBase.get_next_unblocked_interaction_cancel_incompatible


class SocialAdjustmentBucket(BucketSingle):
    __slots__ = ()
    get_next_unblocked_interaction = BucketBase.get_next_unblocked_interaction_cancel_incompatible


class VehicleBodyCancelAOPBucket(BucketSingle):
    __slots__ = ()


class BodyCancelAOPBucket(BucketList):
    __slots__ = ()


class CarryCancelAOPBucket(BucketList):
    __slots__ = ()


class InteractionQueue(HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'max_interactions':TunableRange(description='\n            The maximum number of visible interactions in the queue, including\n            running interactions. If this value is greater than 10, the\n            interaction queue .swf must be updated.\n            ',
       tunable_type=int,
       default=8,
       minimum=0,
       maximum=10), 
     'always_start_inertial':Tunable(description="\n            If this is checked, interactions queued on this Sim always start\n            inertial, regardless of what the content's tuning might say.\n            \n            This makes Sims more responsive to commands but less sticky and less\n            likely to complete any given task.\n            ",
       tunable_type=bool,
       default=False)}

    def __init__(self, sim, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._sim_ref = sim.ref()
        self._running = None
        self._social_adjustment = SocialAdjustmentBucket(sim)
        self._carry_cancel_replacements = CarryCancelAOPBucket(sim)
        self._interactions = InteractionBucket(sim)
        self._body_cancel_replacements = BodyCancelAOPBucket(sim)
        self._vehicle_cancel_replacements = VehicleBodyCancelAOPBucket(sim)
        self._autonomy = AutonomyBucket(sim)
        self._buckets = (
         self._social_adjustment,
         self._carry_cancel_replacements,
         self._vehicle_cancel_replacements,
         self._interactions,
         self._body_cancel_replacements,
         self._autonomy)
        self.transition_controller = None
        self._locked = False
        self._being_destroyed = False
        self._must_run_next_interaction = None
        self.on_head_changed = CallableList()
        self._head_cache = UNSET
        self._si_state_changed_callback_sims = set()
        self._suppress_head_depth = None

    @property
    def sim(self):
        if self._sim_ref is not None:
            return self._sim_ref()

    def __repr__(self):
        return 'InteractionQueue for {}'.format(self.sim)

    def __iter__(self):
        if self.running is not None:
            yield self.running
        for bucket in self._buckets:
            for interaction in bucket:
                if interaction is self.running:
                    continue
                yield interaction

    def __len__(self):
        return len(set(self))

    def log_interaction_queue(self, logger_func):
        logger_func('Interaction queue info for {}', self.sim)
        for bucket in list(self._buckets):
            for interaction in bucket:
                logger_func('    {}'.format(interaction))

        if self.running is not None:
            logger_func('Running interaction {}', self.sim)
            logger_func('    {}'.format(self.running))

    def _process_one_interaction_gen(self, timeline, interaction):
        result = False
        entered_si = False
        required_sims = None
        performance.counters.add_counter('PerfNumInteractions', 1)
        try:
            interaction.pipeline_progress = PipelineProgress.RUNNING
            if interaction.is_super:
                entered_si = yield from interaction.enter_si_gen(timeline)
            else:
                entered_si = True
            if entered_si:
                required_sims = interaction.required_sims(for_threading=True)
                for sim in required_sims:
                    sim.queue.running = interaction

                result = yield from self.run_interaction_gen(timeline, interaction)
        finally:
            if not result:
                interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='process_one_interaction_gen: interaction failed to run.')
            if not entered_si:
                interaction.on_removed_from_queue()
            if required_sims:
                for sim in required_sims:
                    sim.queue.running = None

        return result
        if False:
            yield None

    def run_interaction_gen(self, timeline, interaction, source_interaction=None, apply_posture_state=True):
        if interaction.is_finishing:
            return False
        else:
            interaction_parameters = {}
            interaction_parameters['interaction_starting'] = True
            result = (interaction.test)(skip_safe_tests=True, **interaction_parameters)
            if not result:
                msg = 'Test failed at run_interaction: {}'.format(result)
                interaction.cancel((FinishingType.FAILED_TESTS), cancel_reason_msg=msg)
                log_interaction('Failed', interaction, msg=msg)
                return False
            log_interaction('Running', interaction)
            if interaction.target and interaction.target.objectage_component:
                interaction.target.update_last_used()
        if not interaction.disable_transitions:
            interaction.apply_posture_state(self.sim.posture_state)
        else:
            if interaction.is_super:
                if self._must_run_next_interaction is not None:
                    if interaction.transition is not None:
                        if interaction.transition.interaction is interaction:
                            if interaction is not self._must_run_next_interaction:
                                if source_interaction is None or self._must_run_next_interaction is not source_interaction:
                                    self._must_run_next_interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg=('InteractionQueue: run_interaction: must_run_next: {} canceled by {}'.format(self._must_run_next_interaction, interaction)))
                                    self._must_run_next_interaction = None
            try:
                result, failure_reason = yield from interaction.perform_gen(timeline)
            finally:
                interaction.on_removed_from_queue()

            if result:
                if interaction.is_super and interaction.suspended:
                    log_interaction('Staged', interaction)
                else:
                    log_interaction('Done', interaction)
            else:
                log_interaction('Failed', interaction, msg=failure_reason)
        return result
        if False:
            yield None

    def process_one_interaction_gen(self, timeline):
        head_first = self.get_head()
        while 1:
            head = self.get_head()
            if not head is None:
                if head.is_finishing or head is not head_first:
                    break
                result = head.test(skip_safe_tests=(head.skip_test_on_execute()))
                if not result:
                    old_name = head.get_name()
                    old_icon_info = head.get_icon_info()
                    reason = result.reason if result.reason is not None else 'Interaction Queue head interaction failed tests'
                    head.cancel((FinishingType.FAILED_TESTS), cancel_reason_msg=reason)
                    self.remove_for_perform(head)
                    if head.is_user_directed:
                        if head.visible:
                            if head.is_super:
                                if head.target_in_inventory_when_queued:
                                    if not (head.target is None or head.target.is_in_inventory()):
                                        continue
                                self.insert_route_failure_interaction(head, old_name, old_icon_info)
                                continue
                            yield from self.sim.si_state.process_gen(timeline)
                            if not head.is_super:
                                if head.pipeline_progress == PipelineProgress.QUEUED:
                                    log_interaction('Preparing', head)
                                    try:
                                        result = yield from head.prepare_gen(timeline)
                                    except:
                                        logger.exception('Error in prepare_gen for mixer interaction')
                                        result = False

                                    if result != InteractionQueuePreparationStatus.FAILURE:
                                        if result == InteractionQueuePreparationStatus.SUCCESS:
                                            head.pipeline_progress = PipelineProgress.PREPARED
                                        if result == InteractionQueuePreparationStatus.NEEDS_DERAIL:
                                            return
                        else:
                            head.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='Failed to Prepare Interaction.')
                else:
                    continue
                if head.prepared:
                    head.pre_process_interaction()
                    try:
                        yield from self._process_one_interaction_gen(timeline, head)
                    finally:
                        self.remove_for_perform(head)

                    head.post_process_interaction()
                else:
                    if head.pipeline_progress == PipelineProgress.QUEUED:
                        head.pipeline_progress = PipelineProgress.PRE_TRANSITIONING
                        if not head.run_pre_transition_behavior():
                            log_interaction('PreTransition', head, msg='Failed')
                            head.cancel((FinishingType.TRANSITION_FAILURE), cancel_reason_msg='Pre Transition Behavior Failed.')
                            continue
                        log_interaction('PreTransition', head, msg='Succeeded')
                    if head.pipeline_progress == PipelineProgress.PRE_TRANSITIONING:
                        log_interaction('Preparing', head)
                        try:
                            result = yield from head.prepare_gen(timeline, cancel_incompatible_carry_interactions=True)
                        except scheduling.HardStopError:
                            raise
                        except Exception:
                            logger.exception('Exception in prepare_gen for super interaction.')
                            result = InteractionQueuePreparationStatus.FAILURE

                        if result == InteractionQueuePreparationStatus.NEEDS_DERAIL:
                            idle_element, _ = head.sim.get_idle_element(duration=1)
                            yield from element_utils.run_child(timeline, idle_element)
                            return
                            if result == InteractionQueuePreparationStatus.FAILURE:
                                head.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='Failed to Prepare Interaction.')
                        else:
                            head.pipeline_progress = PipelineProgress.PREPARED
                            continue
                    if head.prepared:
                        required_sims = head.required_sims(for_threading=True)
                        if head.transition is None:
                            head.transition = TransitionSequenceController(head)
                        else:
                            for required_sim in required_sims:
                                required_sim.queue.transition_controller = head.transition

                            if services.game_clock_service().clock_speed == ClockSpeedMode.PAUSED:
                                if not services.current_zone().force_process_transitions:
                                    sleep_paused_element = element_utils.build_element((element_utils.sleep_until_next_tick_element(),
                                     elements.SoftSleepElement(clock.interval_in_sim_seconds(1.0))))
                                    yield from element_utils.run_child(timeline, sleep_paused_element)
                            elif head.transition is None:
                                logger.error('Interaction {} transition is None.', head, owner='jdimailig')
                                result = False
                            else:
                                with gsi_handlers.sim_timeline_handlers.archive_sim_timeline_context_manager(self.sim, 'InteractionQueue', 'Run Transition', head):
                                    head.sim.ui_manager.running_transition(head)
                                    result = yield from head.transition.run_transitions(timeline)
                            for required_sim in required_sims:
                                required_sim.queue.transition_controller = None

                            if head.transition is not None:
                                if head.transition.canceled:
                                    head.transition = None
                                else:
                                    if head.transition.any_derailed:
                                        return
                            if result or head.is_finishing:
                                head.transition = None
                                if head.is_finishing:
                                    self.on_interaction_canceled(head)
                                else:
                                    self.remove_for_perform(head)
                        yield from self.sim.si_state.process_gen(timeline)

        yield from self.sim.si_state.process_gen(timeline)
        if False:
            yield None

    def insert_route_failure_interaction(self, interaction, interaction_name, interaction_icon_info):
        resolver = InteractionResolver(interaction.aop.affordance, interaction)
        anim_overrides = None
        for test_and_override in InteractionFailureOptions.FAILURE_REASON_TESTS:
            result = test_and_override.test_set.run_tests(resolver)
            if result:
                anim_overrides = test_and_override.anim_override
                break

        context = InteractionContext((interaction.sim), (InteractionContext.SOURCE_SCRIPT),
          (Priority.High),
          insert_strategy=(QueueInsertStrategy.NEXT))
        result = self.sim.push_super_affordance((InteractionFailureOptions.ROUTE_FAILURE_AFFORDANCE), (interaction.target),
          context, anim_overrides=anim_overrides,
          interaction_name=interaction_name,
          interaction_icon_info=interaction_icon_info)

    def needs_cancel_aop(self, aop, context):
        bucket = self._get_bucket_for_context(context)
        for cancel_si in bucket:
            if context.group_id == cancel_si.group_id:
                return False

        if self.sim.si_state.is_running_affordance((aop.affordance), target=(aop.target)):
            return False
        return True

    @property
    def transition_in_progress(self):
        return self.transition_controller is not None and not self.transition_controller.canceled

    @property
    def running(self):
        if self.transition_controller is not None:
            return self.transition_controller.interaction
        return self._running

    @running.setter
    def running(self, value):
        self._running = value
        if value is not None:
            if value.is_super:
                if self._must_run_next_interaction is not None:
                    if value is not self._must_run_next_interaction:
                        self._must_run_next_interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='Interaction is not the must_run_next interaction')

    def visible_len(self):
        return sum((1 for interaction in self if interaction.visible_as_interaction if self.running != interaction))

    def can_queue_visible_interaction(self):
        return self.visible_len() < self.max_interactions

    @contextmanager
    def _head_change_watcher(self, defer_on_head_change_call=False):
        if self._suppress_head_depth is None:
            old_head = self.get_head()
            if defer_on_head_change_call:
                self._suppress_head_depth = 1
        else:
            self._suppress_head_depth += 1
        try:
            yield
        finally:
            if self._suppress_head_depth is not None:
                self._suppress_head_depth -= 1
                if self._suppress_head_depth == 0:
                    self._suppress_head_depth = None
            if self._suppress_head_depth is None:
                if self._get_head() != old_head:
                    self.on_head_changed()

    def remove_for_perform(self, interaction):
        with self._head_change_watcher():
            for bucket in self._buckets:
                if bucket.remove_for_perform(interaction):
                    if interaction is self._must_run_next_interaction:
                        self._must_run_next_interaction = None
                    return interaction

    def clear_must_run_next_interaction(self, interaction):
        if interaction is self._must_run_next_interaction:
            self._must_run_next_interaction = None

    def _set_si_state_on_changed_callbacks_for_head(self, sims):
        for sim in self._si_state_changed_callback_sims:
            if sim not in sims:
                sim.si_state.on_changed.remove(self.on_si_phase_change)

        self._si_state_changed_callback_sims &= sims
        for sim in sims:
            if sim in self._si_state_changed_callback_sims:
                continue
            sim.si_state.on_changed.append(self.on_si_phase_change)
            self._si_state_changed_callback_sims.add(sim)

    def clear_head_cache(self):
        self._head_cache = UNSET
        self._set_si_state_on_changed_callbacks_for_head(set())

    def peek_head(self):
        if self._head_cache is UNSET:
            return
        return self._head_cache

    def get_head(self):
        if self._head_cache is UNSET:
            return self._get_head()
        return self._head_cache

    def _get_head(self):
        self.clear_head_cache()
        self._head_cache = None
        next_unblocked_interaction = None
        for bucket in self._buckets:
            next_unblocked_interaction = bucket.get_next_unblocked_interaction(blocked_sims_callback=(self._set_si_state_on_changed_callbacks_for_head))
            if next_unblocked_interaction is not None:
                break

        if self._head_cache is not None:
            if self._head_cache is not UNSET:
                return self._head_cache
        if next_unblocked_interaction is not None:
            required_sims = WeakSet(next_unblocked_interaction.required_sims())

            def clear_and_remove(si, self_ref=weakref.ref(self)):
                for sim in required_sims:
                    if sim.si_state is not None:
                        sim.si_state.on_changed.remove(clear_and_remove)

                self = self_ref()
                if self is not None:
                    self.clear_head_cache()

            for sim in required_sims:
                if sim.si_state is not None:
                    sim.si_state.on_changed.append(clear_and_remove)

            for sim in required_sims:
                if sim.si_state is None:
                    raise RuntimeError('Deleted sim:{} found in required sims of interaction:{} {} {}'.format(sim, next_unblocked_interaction, next_unblocked_interaction._pipeline_progress, next_unblocked_interaction._required_sims))

        self._head_cache = next_unblocked_interaction
        return next_unblocked_interaction

    def _resolve_priority_pressure(self):
        highest_priority_interaction = None
        for interaction in reversed(list(self)):
            allow_clobbering = interaction.interruptible
            super_priority = interaction.super_interaction.priority if interaction.super_interaction is not None else Priority.Low
            interaction_priority = interaction.priority
            max_priority = max(super_priority, interaction_priority)
            if highest_priority_interaction is not None:
                if not interaction.is_related_to(highest_priority_interaction):
                    if can_priority_displace((highest_priority_interaction.priority), max_priority, allow_clobbering=allow_clobbering):
                        if interaction.source == InteractionSource.CARRY_CANCEL_AOP or interaction.source == InteractionSource.BODY_CANCEL_AOP or interaction.source == InteractionSource.VEHCILE_CANCEL_AOP:
                            continue
                        interaction.displace(highest_priority_interaction, cancel_reason_msg='Interaction Queue displaced from resolving priority pressure.')
                        continue
            if highest_priority_interaction is None or interaction.priority > highest_priority_interaction.priority:
                highest_priority_interaction = interaction

    def _resolve_collapsible_interaction(self):
        if len(self._interactions) <= 1:
            return
        for si_a, si_b in zip(self._interactions, list(self._interactions)[1:]):
            if si_a.visible:
                if not si_b.visible:
                    continue
                if si_a.is_finishing or si_b.is_finishing:
                    continue
                if si_a.is_super and si_a.collapsible and si_b.is_super and si_b.collapsible:
                    si_a.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='Interaction Queue canceled because interaction is collapsible.')
                    break

    def _can_sis_pass_combinable_compatability_tests(self, first_si, second_si):
        if first_si.collapsible:
            return False
        else:
            return self.sim.si_state.are_sis_compatible(first_si, second_si) or False
        return True

    def _attempt_combination(self, combined_sis, si_to_evaluate, combination_constraint):
        if si_to_evaluate.visible:
            return si_to_evaluate.allowed_to_combine or Nowhere('SI is not visible({}), or not allowed to combine({}), SI: {}', si_to_evaluate.visible, si_to_evaluate.allowed_to_combine, si_to_evaluate)
        else:
            for combined_si in combined_sis:
                if si_to_evaluate.continuation_id is not None:
                    if si_to_evaluate.continuation_id == combined_si.continuation_id:
                        return Nowhere('Cannot combine two interactions from the same continuation chain. SI_A: {}, SI_B: {}', si_to_evaluate, combined_si)
                if not self._can_sis_pass_combinable_compatability_tests(combined_si, si_to_evaluate):
                    return Nowhere('Two SIs we tried to combine cannot pass combinable compatibility tests. SI_A: {}, SI_B: {}', si_to_evaluate, combined_si)

            si_to_evaluate_constraint = si_to_evaluate.constraint_intersection(sim=(self.sim), posture_state=None)
            return si_to_evaluate_constraint.valid or si_to_evaluate_constraint
        test_constraint = si_to_evaluate_constraint.intersect(combination_constraint)
        return test_constraint

    def _combine_compatible_interactions(self):
        head_interaction = self.get_head()
        if not head_interaction is None:
            if not head_interaction.is_putdown:
                if head_interaction.visible:
                    if not (head_interaction.is_super and head_interaction.allowed_to_combine):
                        return
        else:
            original_head_combinables = WeakSet(head_interaction.combinable_interactions)
            head_interaction.combinable_interactions.clear()
            head_constraint = head_interaction.constraint_intersection(sim=(self.sim), posture_state=None)
            return head_constraint.valid or None
        combined_included_sis = WeakSet((head_interaction,))
        if head_interaction.transition is not None:
            final_included_sis = head_interaction.transition.get_final_included_sis_for_sim(self.sim)
            if final_included_sis is not None:
                for final_si in final_included_sis:
                    if final_si.is_finishing:
                        continue
                    final_si_constraint = final_si.constraint_intersection(sim=(self.sim), posture_state=None)
                    if not final_si_constraint.valid:
                        return
                        head_constraint = self._attempt_combination(combined_included_sis, final_si, head_constraint)
                        if not head_constraint.valid:
                            return
                        combined_included_sis.add(final_si)

        else:
            combined_carry_targets = set()
            head_carryable = head_interaction.targeted_carryable
            if head_carryable is not None:
                combined_carry_targets.add(head_carryable)
            combined_interactions = WeakSet((head_interaction,))
            combined_constraint = head_constraint
            for queued_interaction in self._interactions:
                if not (queued_interaction is head_interaction or queued_interaction.is_super):
                    continue
                if queued_interaction.is_putdown:
                    break
                queued_interaction.combinable_interactions.clear()
                test_intersection = self._attempt_combination(combined_interactions, queued_interaction, combined_constraint)
                if not test_intersection.valid:
                    break
                combined_constraint = test_intersection
                combined_interactions.add(queued_interaction)
                queued_carryable = queued_interaction.targeted_carryable
                if queued_carryable is not None:
                    combined_carry_targets.add(queued_carryable)
                    if len(combined_carry_targets) > 1:
                        break

            if len(combined_interactions) == 1:
                return
            for interaction in combined_interactions:
                interaction.combinable_interactions = combined_interactions

            if original_head_combinables:
                if original_head_combinables != combined_interactions and head_interaction.transition is not None:
                    if len(combined_carry_targets) > 1:
                        posture_graph_service = services.current_zone().posture_graph_service
                        posture_graph_service.clear_goal_costs()
                    head_interaction.transition.derail(DerailReason.PROCESS_QUEUE, self.sim)

    def _get_bucket_for_context(self, context):
        bucket_type = context.bucket_type
        if bucket_type == InteractionBucketType.BASED_ON_SOURCE:
            source = context.source
            if source == InteractionContext.SOURCE_AUTONOMY:
                bucket_type = InteractionBucketType.AUTONOMY
            else:
                if source == InteractionContext.SOURCE_SOCIAL_ADJUSTMENT:
                    bucket_type = InteractionBucketType.SOCIAL_ADJUSTMENT
                else:
                    if source == InteractionContext.SOURCE_BODY_CANCEL_AOP:
                        bucket_type = InteractionBucketType.BODY_CANCEL_REPLACEMENT
                    else:
                        if source == InteractionContext.SOURCE_CARRY_CANCEL_AOP:
                            bucket_type = InteractionBucketType.CARRY_CANCEL_REPLACEMENT
                        else:
                            if source == InteractionContext.SOURCE_VEHICLE_CANCEL_AOP:
                                bucket_type = InteractionBucketType.VEHICLE_CANCEL_REPLACEMENT
                            else:
                                bucket_type = InteractionBucketType.DEFAULT
        elif bucket_type == InteractionBucketType.AUTONOMY:
            bucket = self._autonomy
        else:
            if bucket_type == InteractionBucketType.SOCIAL_ADJUSTMENT:
                bucket = self._social_adjustment
            else:
                if bucket_type == InteractionBucketType.VEHICLE_CANCEL_REPLACEMENT:
                    bucket = self._vehicle_cancel_replacements
                else:
                    if bucket_type == InteractionBucketType.BODY_CANCEL_REPLACEMENT:
                        bucket = self._body_cancel_replacements
                    else:
                        if bucket_type == InteractionBucketType.CARRY_CANCEL_REPLACEMENT:
                            bucket = self._carry_cancel_replacements
                        else:
                            if bucket_type == InteractionBucketType.DEFAULT:
                                bucket = self._interactions
                            else:
                                raise ValueError('Unrecognized bucket_type: {}'.format(bucket_type))
        return bucket

    def _get_bucket_for_interaction(self, interaction):
        if interaction.context.bucket_type not in InteractionBucketType.values:
            logger.error('Invalid interaction bucket in context for {}', interaction, owner='rez')
        bucket = self._get_bucket_for_context(interaction.context)
        return bucket

    def append(self, interaction):
        if self.locked:
            return TestResult(False, 'Interaction queue is locked.')
        if interaction.is_finishing:
            return TestResult(False, 'Interaction is already finishing.')
        target_queue = self._get_bucket_for_interaction(interaction)
        with self._head_change_watcher():
            if interaction.context.insert_strategy == QueueInsertStrategy.NEXT or interaction.context.insert_strategy == QueueInsertStrategy.FIRST:
                self._refresh_bucket_constraints()
                if interaction.context.insert_strategy != QueueInsertStrategy.FIRST:
                    insert_after_interaction = self.running
                else:
                    insert_after_interaction = None
                success = target_queue.insert_next(interaction, insert_after=insert_after_interaction)
            else:
                insert_after_interaction = None
                success = target_queue.append(interaction)
            if not success:
                interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='InteractionQueue: failed to append interaction')
                return success
            interaction_id_to_insert_after = insert_after_interaction.id if insert_after_interaction is not None else None
            interaction.on_added_to_queue(interaction_id_to_insert_after=interaction_id_to_insert_after)
            if interaction.is_user_directed:
                self._on_user_driven_action()
            if interaction.context.must_run_next:
                if self._must_run_next_interaction is not None:
                    self._must_run_next_interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg=('must_run_next inserted again: {} canceled by {}'.format(self._must_run_next_interaction, interaction)))
                    self._must_run_next_interaction = None
                self._must_run_next_interaction = interaction
            self._resolve_priority_pressure()
            self._resolve_collapsible_interaction()
            self._combine_compatible_interactions()
        if interaction.is_finishing:
            return TestResult(False, 'Interaction finished during append.  Finishing Info: {}'.format(interaction._finisher))
        return TestResult.TRUE

    def _refresh_bucket_constraints(self):
        for interaction in list(self._autonomy):
            interaction.refresh_constraints()

        for interaction in list(self._interactions):
            interaction.refresh_constraints()

    def _on_user_driven_action(self):
        for interaction in list(self._autonomy):
            interaction.cancel((FinishingType.PRIORITY), cancel_reason_msg='User-directed action takes precedence over autonomous interactions.')

        for interaction in list(self._social_adjustment):
            interaction.cancel((FinishingType.PRIORITY), cancel_reason_msg='User-directed action takes precedence over social adjustment interactions.')

    def mixer_interactions_gen(self):
        for interaction in self:
            if not interaction.is_super:
                yield interaction

    def find_sub_interaction(self, super_id, aop_id):
        for interaction in self:
            if interaction.super_interaction.id == super_id and interaction.aop.aop_id == aop_id:
                return interaction

    def find_continuation_by_id(self, source_id):
        for interaction in self:
            if interaction.is_continuation_by_id(source_id):
                return interaction

    def find_pushed_interaction_by_id(self, group_id):
        for interaction in self:
            if interaction.group_id == group_id:
                return interaction

    def find_interaction_by_id(self, id_to_find):
        for interaction in self:
            if interaction.id == id_to_find:
                return interaction

        if self.transition_controller is not None:
            if self.transition_controller.interaction.id == id_to_find:
                return self.transition_controller.interaction

    def has_adjustment_interaction(self):
        return len(self._social_adjustment) > 0

    def cancel_all(self):
        self.clear_head_cache()
        interactions = list(self)
        for interaction in interactions:
            interaction.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='InteractionQueue: all interactions canceled')

    def on_reset(self, being_destroyed=False):
        self._being_destroyed = being_destroyed
        with self._head_change_watcher(defer_on_head_change_call=True):
            if self.transition_controller is not None:
                self.transition_controller.on_reset()
                self.transition_controller.interaction.on_reset()
                self.transition_controller = None
            if self._running is not None:
                self._running.on_reset()
                self._running = None
            self.clear_head_cache()
            for bucket in self._buckets:
                try:
                    bucket.on_reset()
                except Exception:
                    logger.error('Exception caught while reseting interaction bucket. ListBucket.reset is not allowed to throw an exception and must always clear the bucket:')
                    raise

    def on_interaction_canceled(self, interaction):
        self.clear_must_run_next_interaction(interaction)
        if self.running is interaction:
            return
        elif interaction.is_super:
            si_order_changed = True
        else:
            si_order_changed = False
        log_interaction('Dequeue_Clear', interaction)
        with self._head_change_watcher():
            for bucket in self._buckets:
                if interaction in bucket and bucket.clear_interaction(interaction):
                    break

        if self.running is not None:
            if self.running.should_cancel_on_si_cancel(interaction):
                self.running.cancel((FinishingType.INTERACTION_QUEUE), cancel_reason_msg='Interaction Queue cancel running interaction to expedite SI cancel.')
        if not self._being_destroyed:
            if si_order_changed:
                self._combine_compatible_interactions()
                self._resolve_collapsible_interaction()

    @property
    def locked(self):
        return self._locked

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    def on_si_phase_change(self, si):
        for interaction in self:
            if not interaction.is_super:
                continue
            interaction.on_other_si_phase_change(si)

        with self._head_change_watcher():
            self._apply_next_pressure()

    def on_element_priority_changed(self, interaction):
        with self._head_change_watcher():
            self._apply_next_pressure()

    def _on_head_changed(self):
        if services.current_zone().is_zone_shutting_down:
            return
        with self._head_change_watcher():
            self._apply_next_pressure()
        self.on_head_changed()
        self._combine_compatible_interactions()

    @staticmethod
    def _should_head_dispace_running(sim, next_interaction, running_interaction):
        if running_interaction.disable_displace(next_interaction):
            return False
            if not running_interaction.is_super:
                if not running_interaction.interruptible:
                    return False
            if next_interaction.super_interaction is running_interaction:
                return False
            pick_up_sim_liability = running_interaction.get_liability(PickUpSimLiability.LIABILITY_TOKEN)
            if pick_up_sim_liability is not None:
                if pick_up_sim_liability.original_interaction is next_interaction:
                    return False
            cancel_aop_liability = next_interaction.get_liability(CANCEL_AOP_LIABILITY)
            if cancel_aop_liability is not None:
                if cancel_aop_liability.interaction_to_cancel is running_interaction:
                    return True
            if next_interaction.is_cancel_aop:
                allow_clobbering = running_interaction.disable_transitions or True
            else:
                allow_clobbering = running_interaction.interruptible
            if running_interaction.is_super:
                if running_interaction.is_guaranteed():
                    if not can_displace(next_interaction, running_interaction, allow_clobbering=allow_clobbering):
                        return False
            if next_interaction.is_related_to(running_interaction):
                return False
        elif running_interaction.is_super:
            if next_interaction.is_super:
                participant_type_a = running_interaction.get_participant_type(sim)
                participant_type_b = next_interaction.get_participant_type(sim)
                compatible = sim.si_state.are_sis_compatible(running_interaction, next_interaction,
                  participant_type_a=participant_type_a,
                  participant_type_b=participant_type_b)
                if compatible:
                    return False
        return True

    def _apply_next_pressure(self):
        next_interaction = self.get_head()
        if next_interaction is None:
            return
        for sim in next_interaction.required_sims():
            running_interaction = sim.queue.running
            if next_interaction is running_interaction:
                continue
            if running_interaction is None or running_interaction.must_run:
                continue
            if not self._should_head_dispace_running(sim, next_interaction, running_interaction):
                if running_interaction.transition is not None:
                    if running_interaction.sim is self.sim:
                        running_interaction.is_adjustment_interaction() or next_interaction.is_related_to(running_interaction) or running_interaction.transition.derail(DerailReason.PREEMPTED, sim)
                        continue
                    running_interaction.displace(next_interaction, cancel_reason_msg=('InteractionQueue: pressure to cancel running interaction from {}'.format(next_interaction)))

    def on_required_sims_changed(self, interaction):
        self.clear_head_cache()
        if self.get_head() is interaction:
            self._on_head_changed()

    def cancel_aop_exists_for_si(self, si):
        for interaction in self:
            cancel_liability = interaction.get_liability(CANCEL_AOP_LIABILITY)
            if cancel_liability is not None and si is cancel_liability.interaction_to_cancel:
                return True

        return False

    def queued_super_interactions_gen(self):
        for si in self._interactions:
            if si.is_super:
                yield si

    def has_duplicate_super_affordance(self, super_affordance, actor, target):
        for si in self._interactions:
            if si.affordance is super_affordance and si.target is target and si.context.sim is actor:
                return True

        return False
