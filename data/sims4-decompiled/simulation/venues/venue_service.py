# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\venues\venue_service.py
# Compiled at: 2022-06-24 19:09:02
# Size of source mod 2**32: 52345 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
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
binary_operator ::= BINARY_SUBTRACT . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
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
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
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
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
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
returns ::= return . 
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
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= withasstmt . 
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
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
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
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with_suffix ::= WITH_CLEANUP_START . WITH_CLEANUP_FINISH END_FINALLY
with_suffix ::= WITH_CLEANUP_START WITH_CLEANUP_FINISH . END_FINALLY
with_suffix ::= WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY . 
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK . LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST . COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH . with_suffix
withasstmt ::= expr SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 281       124  LOAD_FAST                'self'
                 126  LOAD_METHOD              start_venue_situations
                 128  LOAD_FAST                'active_venue'
                 130  CALL_METHOD_1         1  '1 positional argument'
                 132  POP_TOP          
               134_0  COME_FROM           122  '122'
               134_1  COME_FROM           118  '118'
->             134_2  COME_FROM_LOOP       86  '86'
from protocolbuffers import GameplaySaveData_pb2 as gameplay_serialization, Consts_pb2, Venue_pb2
import alarms, build_buy, clock, persistence_error_types, random, services, sims4.log, sims4.resources, telemetry_helper
from build_buy import get_current_venue
from date_and_time import TimeSpan
from distributor.ops import OwnedUniversityHousingLoad
from distributor.system import Distributor
from objects.components.types import FOOTPRINT_COMPONENT
from open_street_director.open_street_director_request import OpenStreetDirectorRequestFactory
from protocolbuffers import GameplaySaveData_pb2
from sims4.common import Pack
from sims.university.university_housing_tuning import UniversityHousingTuning
from sims.university.university_utils import UniversityUtils
from sims4.callback_utils import CallableList
from sims4.service_manager import Service
from sims4.tuning.tunable import TunableSimMinute
from sims4.utils import classproperty
from situations.service_npcs.modify_lot_items_tuning import ModifyAllLotItems
from venues.venue_constants import ZoneDirectorRequestType
from venues.venue_enums import VenueTypes
from world.region import get_region_instance_from_zone_id, get_region_description_id_from_zone_id
TELEMETRY_GROUP_VENUE = 'VENU'
TELEMETRY_HOOK_TIMESPENT = 'TMSP'
TELEMETRY_FIELD_VENUE = 'venu'
TELEMETRY_FIELD_VENUE_TIMESPENT = 'vtsp'
venue_telemetry_writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_VENUE)
try:
    import _zone
except ImportError:

    class _zone:
        pass


logger = sims4.log.Logger('Venue', default_owner='manus')

class VenueService(Service):
    SPECIAL_EVENT_SCHEDULE_DELAY = TunableSimMinute(description='\n        Number of real time seconds to wait after the loading screen before scheduling\n        special events.\n        ',
      default=10.0)
    VENUE_CLEANUP_ACTIONS = ModifyAllLotItems.TunableFactory()
    ELAPSED_TIME_SINCE_LAST_VISIT_FOR_CLEANUP = TunableSimMinute(description='\n        If more than this amount of sim minutes has elapsed since the lot was\n        last visited, the auto cleanup will happen.\n        ',
      default=720,
      minimum=0)

    def __init__(self):
        self._persisted_background_event_id = None
        self._persisted_special_event_id = None
        self._special_event_start_alarm = None
        self._source_venue = None
        self._active_venue = None
        self._zone_director = None
        self._requested_zone_directors = []
        self._prior_zone_director_proto = None
        self._open_street_director_requests = []
        self._prior_open_street_director_proto = None
        self.build_buy_edit_mode = False
        self.on_venue_type_changed = CallableList()
        self._venue_start_time = None
        self._university_housing_household_validation_alarm = None
        self._university_housing_kick_out_completed = False

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_VENUE_SERVICE

    @property
    def active_venue(self):
        return self._active_venue

    @property
    def source_venue(self):
        return self._source_venue

    def venue_is_type(self, required_type):
        if type(self.active_venue) is required_type:
            return True
        return False

    @staticmethod
    def get_variable_venue_source_venue(test_venue_type):
        if test_venue_type is None:
            return
        sub_venue_types = test_venue_type.sub_venue_types
        if sub_venue_types:
            return test_venue_type
        venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
        for venue_tuning_type in venue_manager.types.values():
            if test_venue_type == venue_tuning_type:
                continue
            if venue_tuning_type.valid_active_venue_type(test_venue_type):
                return venue_tuning_type

    def _set_venue(self, active_venue_type, source_venue_type):
        if active_venue_type is None:
            logger.error('Zone {} has invalid active venue type.', services.current_zone().id)
            return False
            if source_venue_type is None:
                source_venue_type = active_venue_type
        else:
            current_source_venue = self.source_venue
            source_venue_changed = type(current_source_venue) is not source_venue_type
            current_active_venue = self.active_venue
            active_venue_changed = type(current_active_venue) is not active_venue_type
            if not source_venue_changed:
                if not active_venue_changed:
                    return False
            if active_venue_changed:
                if current_active_venue is not None:
                    current_active_venue.shut_down()
                    if self._special_event_start_alarm is not None:
                        alarms.cancel_alarm(self._special_event_start_alarm)
                        self._special_event_start_alarm = None
                else:
                    self._send_venue_time_spent_telemetry()
                    if not source_venue_changed:
                        if source_venue_type is active_venue_type:
                            self._active_venue = self._source_venue
                    self._active_venue = active_venue_type(source_venue_type=source_venue_type)
                self._venue_start_time = services.time_service().sim_now
            if source_venue_changed:
                if source_venue_type is active_venue_type:
                    self._source_venue = self._active_venue
                else:
                    self._source_venue = source_venue_type()
                provider = self._source_venue.civic_policy_provider
                if provider is not None:
                    provider.finalize_startup()
        return active_venue_changed

    def _send_venue_time_spent_telemetry(self):
        if self.active_venue is None or self._venue_start_time is None:
            return
        time_spent_mins = (services.time_service().sim_now - self._venue_start_time).in_minutes()
        if time_spent_mins:
            with telemetry_helper.begin_hook(venue_telemetry_writer, TELEMETRY_HOOK_TIMESPENT) as (hook):
                hook.write_guid(TELEMETRY_FIELD_VENUE, self.active_venue.guid64)
                hook.write_int(TELEMETRY_FIELD_VENUE_TIMESPENT, time_spent_mins)

    def get_venue_tuning(self, zone_id):
        venue_tuning = None
        venue_type = get_current_venue(zone_id)
        if venue_type is not None:
            venue_tuning = services.get_instance_manager(sims4.resources.Types.VENUE).get(venue_type)
        return venue_tuning

    def on_change_venue_type_at_runtime--- This code section failed: ---

 L. 261         0  LOAD_FAST                'self'
                2  LOAD_ATTR                build_buy_edit_mode
                4  POP_JUMP_IF_FALSE    10  'to 10'

 L. 264         6  LOAD_CONST               None
                8  RETURN_VALUE     
             10_0  COME_FROM             4  '4'

 L. 266        10  LOAD_FAST                'self'
               12  LOAD_METHOD              _set_venue
               14  LOAD_FAST                'active_venue_type'
               16  LOAD_FAST                'source_venue_type'
               18  CALL_METHOD_2         2  '2 positional arguments'
               20  STORE_FAST               'type_changed'

 L. 267        22  LOAD_FAST                'self'
               24  LOAD_ATTR                active_venue
               26  LOAD_CONST               None
               28  COMPARE_OP               is
               30  POP_JUMP_IF_FALSE    36  'to 36'

 L. 268        32  LOAD_FAST                'type_changed'
               34  RETURN_VALUE     
             36_0  COME_FROM            30  '30'

 L. 270        36  LOAD_FAST                'self'
               38  LOAD_ATTR                active_venue
               40  STORE_FAST               'active_venue'

 L. 271        42  LOAD_FAST                'type_changed'
               44  POP_JUMP_IF_FALSE   120  'to 120'

 L. 272        46  LOAD_FAST                'active_venue'
               48  LOAD_METHOD              create_zone_director_instance
               50  CALL_METHOD_0         0  '0 positional arguments'
               52  STORE_FAST               'zone_director'

 L. 273        54  LOAD_FAST                'self'
               56  LOAD_ATTR                change_zone_director
               58  LOAD_FAST                'zone_director'
               60  LOAD_CONST               True
               62  LOAD_CONST               ('run_cleanup',)
               64  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               66  POP_TOP          

 L. 274        68  LOAD_FAST                'self'
               70  LOAD_METHOD              start_venue_situations
               72  LOAD_FAST                'active_venue'
               74  CALL_METHOD_1         1  '1 positional argument'
               76  POP_TOP          

 L. 275        78  LOAD_FAST                'self'
               80  LOAD_METHOD              on_venue_type_changed
               82  CALL_METHOD_0         0  '0 positional arguments'
               84  POP_TOP          

 L. 277        86  SETUP_LOOP          134  'to 134'
               88  LOAD_GLOBAL              services
               90  LOAD_METHOD              sim_info_manager
               92  CALL_METHOD_0         0  '0 positional arguments'
               94  LOAD_METHOD              instanced_sims_on_active_lot_gen
               96  CALL_METHOD_0         0  '0 positional arguments'
               98  GET_ITER         
              100  FOR_ITER            116  'to 116'
              102  STORE_FAST               'sim'

 L. 278       104  LOAD_FAST                'sim'
              106  LOAD_ATTR                sim_info
              108  LOAD_METHOD              add_venue_buffs
              110  CALL_METHOD_0         0  '0 positional arguments'
              112  POP_TOP          
              114  JUMP_BACK           100  'to 100'
              116  POP_BLOCK        
              118  JUMP_FORWARD        134  'to 134'
            120_0  COME_FROM            44  '44'

 L. 280       120  LOAD_FAST                'force_start_situations'
              122  POP_JUMP_IF_FALSE   134  'to 134'

 L. 281       124  LOAD_FAST                'self'
              126  LOAD_METHOD              start_venue_situations
              128  LOAD_FAST                'active_venue'
              130  CALL_METHOD_1         1  '1 positional argument'
              132  POP_TOP          
            134_0  COME_FROM           122  '122'
            134_1  COME_FROM           118  '118'
            134_2  COME_FROM_LOOP       86  '86'

 L. 283       134  LOAD_FAST                'type_changed'
              136  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM_LOOP' instruction at offset 134_2

    def start_venue_situations(self, active_venue):
        self.create_situations_during_zone_spin_up()
        if self._zone_director.should_create_venue_background_situation:
            active_venue.schedule_background_events(schedule_immediate=True)
            active_venue.schedule_special_events(schedule_immediate=False)
            active_venue.schedule_club_gatherings(schedule_immediate=True)

    def make_venue_type_zone_director_request(self):
        active_venue = self.active_venue
        if active_venue is None:
            raise RuntimeError('Venue type must be determined before requesting a zone director.')
        else:
            zone_director = active_venue.create_zone_director_instance()
            if active_venue is self.source_venue:
                request_type = ZoneDirectorRequestType.AMBIENT_VENUE
            else:
                request_type = ZoneDirectorRequestType.AMBIENT_SUB_VENUE
        self.request_zone_director(zone_director, request_type)

    def setup_lot_premade_status(self):
        services.active_lot().flag_as_premade(True)

    def _select_zone_director(self):
        if self._requested_zone_directors is None:
            raise RuntimeError('Cannot select a zone director twice')
        if not self._requested_zone_directors:
            raise RuntimeError('At least one zone director must be requested')
        requested_zone_directors = self._requested_zone_directors
        self._requested_zone_directors = None
        requested_zone_directors.sort()
        _, zone_director, preserve_state = requested_zone_directors[0]
        self._set_zone_director(zone_director, True)
        if self._prior_zone_director_proto:
            self._zone_director.load((self._prior_zone_director_proto), preserve_state=preserve_state)
            self._prior_zone_director_proto = None
        self._setup_open_street_director()

    def _setup_open_street_director(self):
        street = services.current_street()
        if street is not None:
            if street.open_street_director is not None:
                self._open_street_director_requests.append(OpenStreetDirectorRequestFactory((street.open_street_director), priority=(street.open_street_director.priority)))
        self._zone_director.setup_open_street_director_manager(self._open_street_director_requests, self._prior_open_street_director_proto)
        self._open_street_director_requests = None
        self._prior_open_street_director_proto = None

    @property
    def has_zone_director(self):
        return self._zone_director is not None

    def get_zone_director(self):
        return self._zone_director

    def has_requested_zone_director(self, zone_director):
        if self._requested_zone_directors is None:
            return False
        for _, prior_zone_director, _ in self._requested_zone_directors:
            if prior_zone_director.guid64 == zone_director.guid64:
                return True

        return False

    def get_requested_zone_director(self, zone_director):
        if self._requested_zone_directors is None:
            return
        for _, prior_zone_director, _ in self._requested_zone_directors:
            if prior_zone_director.guid64 == zone_director.guid64:
                return prior_zone_director

    def request_zone_director(self, zone_director, request_type, preserve_state=True):
        if self._requested_zone_directors is None:
            raise RuntimeError('Cannot request a new zone director after one has been selected.')
        if zone_director is None:
            raise ValueError('Cannot request a None zone director.')
        for prior_request_type, prior_zone_director, _ in self._requested_zone_directors:
            if prior_request_type == request_type:
                raise ValueError('Multiple requests for zone directors with the same request type {}.  Original: {} New: {}'.format(request_type, prior_zone_director, zone_director))

        self._requested_zone_directors.append((request_type, zone_director, preserve_state))

    def change_zone_director(self, zone_director, run_cleanup):
        if self._zone_director is None:
            raise RuntimeError('Cannot request a new zone director before one has been selected.')
        if self._zone_director is zone_director:
            raise ValueError('Attempting to change zone director to the same instance')
        self._set_zone_director(zone_director, run_cleanup)

    def _set_zone_director(self, zone_director, run_cleanup):
        if self._zone_director is not None:
            if run_cleanup:
                self._zone_director.process_cleanup_actions()
            else:
                for cleanup_action in self._zone_director._cleanup_actions:
                    zone_director.add_cleanup_action(cleanup_action)

            if zone_director is not None:
                zone_director.transfer_open_street_director(self._zone_director)
                zone_director.transfer_from_zone_director(self._zone_director)
            self._zone_director.on_shutdown()
        self._zone_director = zone_director
        if self._zone_director is not None:
            self._zone_director.on_startup()
            if services.current_zone().is_zone_running:
                self._zone_director.create_situations()

    def request_open_street_director(self, open_street_director_request):
        if services.current_zone().is_zone_running:
            self._zone_director.request_new_open_street_director(open_street_director_request)
            return
        self._open_street_director_requests.append(open_street_director_request)

    def determine_which_situations_to_load(self):
        self._zone_director.determine_which_situations_to_load()

    def get_additional_zone_modifiers(self, zone_id):
        current_venue_tuning = self.get_venue_tuning(zone_id)
        if not current_venue_tuning:
            return ()
        else:
            zone_modifiers = set(current_venue_tuning.zone_modifiers)
            return current_venue_tuning.venue_tiers or zone_modifiers
        current_tier = build_buy.get_venue_tier(zone_id)
        if current_tier != -1:
            zone_modifiers.update(current_venue_tuning.venue_tiers[current_tier].zone_modifiers)
        return zone_modifiers

    def on_client_connect(self, client):
        zone = services.current_zone()
        active_venue_key = get_current_venue(zone.id)
        logger.assert_raise((active_venue_key is not None), ' Venue Type is None for zone id:{}', (zone.id), owner='shouse')
        raw_active_venue_key = get_current_venue((zone.id), allow_ineligible=True)
        logger.assert_raise((raw_active_venue_key is not None), ' Raw Venue Type is None for zone id:{}', (zone.id), owner='shouse')
        if not active_venue_key is None:
            if not raw_active_venue_key is None:
                venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
                active_venue_type = venue_manager.get(active_venue_key)
                raw_active_venue_type = venue_manager.get(raw_active_venue_key)
                source_venue_type = VenueService.get_variable_venue_source_venue(raw_active_venue_type)
                self._set_venue(active_venue_type, source_venue_type)

    def on_cleanup_zone_objects(self, client):
        zone = services.current_zone()
        if client.household_id != zone.lot.owner_household_id:
            time_elapsed = zone.time_elapsed_since_last_save()
            if time_elapsed.in_minutes() > self.ELAPSED_TIME_SINCE_LAST_VISIT_FOR_CLEANUP:
                cleanup = VenueService.VENUE_CLEANUP_ACTIONS()
                cleanup.modify_objects()

    def stop(self):
        self._send_venue_time_spent_telemetry()
        if self.build_buy_edit_mode:
            return
        self._set_zone_director(None, True)

    def create_situations_during_zone_spin_up(self):
        self._zone_director.create_situations_during_zone_spin_up()
        self.initialize_venue_schedules()

    def handle_active_lot_changing_edge_cases(self):
        self._zone_director.handle_active_lot_changing_edge_cases()

    def initialize_venue_schedules(self):
        if not self._zone_director.should_create_venue_background_situation:
            return
        active_venue = self.active_venue
        if active_venue is not None:
            active_venue.set_active_event_ids(self._persisted_background_event_id, self._persisted_special_event_id)
            situation_manager = services.current_zone().situation_manager
            schedule_immediate = self._persisted_background_event_id is None or self._persisted_background_event_id not in situation_manager
            active_venue.schedule_background_events(schedule_immediate=schedule_immediate)
            active_venue.schedule_club_gatherings(schedule_immediate=schedule_immediate)

    def process_traveled_and_persisted_and_resident_sims_during_zone_spin_up(self, traveled_sim_infos, zone_saved_sim_infos, plex_group_saved_sim_infos, open_street_saved_sim_infos, injected_into_zone_sim_infos):
        self._zone_director.process_traveled_and_persisted_and_resident_sims(traveled_sim_infos, zone_saved_sim_infos, plex_group_saved_sim_infos, open_street_saved_sim_infos, injected_into_zone_sim_infos)

    def setup_special_event_alarm(self):
        special_event_time_span = clock.interval_in_sim_minutes(self.SPECIAL_EVENT_SCHEDULE_DELAY)
        self._special_event_start_alarm = alarms.add_alarm(self,
          special_event_time_span,
          (self._schedule_venue_special_events),
          repeating=False)

    def _schedule_venue_special_events(self, alarm_handle):
        if self.active_venue is not None:
            self.active_venue.schedule_special_events(schedule_immediate=True)

    def get_zone_venue_type_valid_for_venue_types(self, zone_id, venue_types, compatible_region=None, ignore_region_compatability_tags=False, region_blacklist=[]):
        if not zone_id:
            return
            venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
            venue_type = venue_manager.get(build_buy.get_current_venue(zone_id))
            if venue_type not in venue_types:
                return
        else:
            if compatible_region is not None:
                venue_region = get_region_instance_from_zone_id(zone_id)
                return venue_region is None or compatible_region.is_region_compatible(venue_region, ignore_tags=ignore_region_compatability_tags) or None
            if region_blacklist:
                venue_region_description_id = get_region_description_id_from_zone_id(zone_id)
                if venue_region_description_id in region_blacklist:
                    return
        return venue_type

    def has_zone_for_venue_type(self, venue_types, compatible_region=None):
        for _ in (self.get_zones_for_venue_type_gen)(*venue_types, **{'compatible_region': compatible_region}):
            return True

        return False

    def get_zones_for_venue_type_gen(self, *venue_types, compatible_region=None, ignore_region_compatability_tags=False, region_blacklist=[]):
        for lot_owner_info in services.get_persistence_service().get_lots_proto_buff_gen():
            zone_id = lot_owner_info.zone_instance_id
            if self.get_zone_venue_type_valid_for_venue_types(zone_id, venue_types,
              compatible_region=compatible_region,
              ignore_region_compatability_tags=ignore_region_compatability_tags,
              region_blacklist=region_blacklist) is not None:
                yield zone_id

    def get_zone_and_venue_type_for_venue_types(self, venue_types, compatible_region=None):
        possible_zone_venue_types = []
        for lot_owner_info in services.get_persistence_service().get_lots_proto_buff_gen():
            zone_id = lot_owner_info.zone_instance_id
            venue_type = self.get_zone_venue_type_valid_for_venue_types(zone_id, venue_types,
              compatible_region=compatible_region)
            if venue_type is not None:
                possible_zone_venue_types.append((zone_id, venue_type))

        if possible_zone_venue_types:
            return random.choice(possible_zone_venue_types)
        return (None, None)

    def save(self, zone_data=None, open_street_data=None, **kwargs):
        active_venue = self.active_venue
        if zone_data is not None:
            if active_venue is not None:
                venue_data = zone_data.gameplay_zone_data.venue_data
                if active_venue.active_background_event_id is not None:
                    venue_data.background_situation_id = active_venue.active_background_event_id
                if active_venue.active_special_event_id is not None:
                    venue_data.special_event_id = active_venue.active_special_event_id
                if self._zone_director is not None:
                    zone_director_data = gameplay_serialization.ZoneDirectorData()
                    self._zone_director.save(zone_director_data, open_street_data)
                    venue_data.zone_director = zone_director_data
                else:
                    if self._prior_open_street_director_proto is not None:
                        open_street_data.open_street_director = self._prior_open_street_director_proto
                    if self._prior_zone_director_proto is not None:
                        venue_data.zone_director = self._prior_zone_director_proto

    def load(self, zone_data=None, **kwargs):
        if zone_data is not None:
            if zone_data.HasField('gameplay_zone_data'):
                if zone_data.gameplay_zone_data.HasField('venue_data'):
                    venue_data = zone_data.gameplay_zone_data.venue_data
                    if venue_data.HasField('background_situation_id'):
                        self._persisted_background_event_id = venue_data.background_situation_id
                    if venue_data.HasField('special_event_id'):
                        self._persisted_special_event_id = venue_data.special_event_id
                    if venue_data.HasField('zone_director'):
                        self._prior_zone_director_proto = gameplay_serialization.ZoneDirectorData()
                        self._prior_zone_director_proto.CopyFrom(venue_data.zone_director)
        open_street_id = services.current_zone().open_street_id
        open_street_data = services.get_persistence_service().get_open_street_proto_buff(open_street_id)
        if open_street_data is not None:
            if open_street_data.HasField('open_street_director'):
                self._prior_open_street_director_proto = gameplay_serialization.OpenStreetDirectorData()
                self._prior_open_street_director_proto.CopyFrom(open_street_data.open_street_director)

    def on_loading_screen_animation_finished(self):
        if self._zone_director is not None:
            self._zone_director.on_loading_screen_animation_finished()

    def set_university_housing_kick_out_completed(self):
        self._university_housing_kick_out_completed = True

    def get_university_housing_kick_out_completed(self):
        return self._university_housing_kick_out_completed

    def run_venue_preparation_operations(self):
        if self.active_venue is None:
            return
        zone = services.current_zone()
        venue_type = self.active_venue.venue_type
        owner_household = zone.lot.get_household()
        if venue_type == VenueTypes.UNIVERSITY_HOUSING:
            if owner_household is not None:
                op = OwnedUniversityHousingLoad(zone.id)
                Distributor.instance().add_op_with_no_owner(op)
                self._university_housing_household_validation_alarm = alarms.add_alarm(self, (UniversityHousingTuning.UNIVERSITY_HOUSING_VALIDATION_CADENCE()),
                  (lambda _: UniversityUtils.validate_household_sims()),
                  repeating=True)

    def validate_university_housing_household_sims(self):
        if self.active_venue.venue_type.venue_type == VenueTypes.UNIVERSITY_HOUSING:
            UniversityUtils.validate_household_sims()


class VenueGameService(Service):

    def __init__(self):
        super().__init__()
        self._zone_provider = dict()
        self.on_venue_type_changed = CallableList()
        self._venue_restore_alarm_handler = None
        self._venue_restore_zone_id = None
        self._venue_restore_type_id = None
        self._sub_venue_loading = False

    def stop(self):
        self._clear_venue_restore_alarm()
        super().stop()

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_VENUE_GAME_SERVICE

    @classproperty
    def required_packs(cls):
        return (Pack.EP09, Pack.EP12)

    def on_cleanup_zone_objects(self, client):
        self.load_providers()
        for provider in self._zone_provider.values():
            provider.finalize_startup()

        if self._venue_restore_zone_id is not None:
            if self._venue_restore_zone_id != services.current_zone_id():
                self.restore_venue_type(self._venue_restore_zone_id, None)

    def save(self, object_list=None, zone_data=None, open_street_data=None, save_slot_data=None):
        for zone_id, provider in self._zone_provider.items():
            if provider is None:
                continue
            zone_data = services.get_persistence_service().get_zone_proto_buff(zone_id)
            if zone_data is None:
                continue
            venue_data = zone_data.gameplay_zone_data.venue_data
            provider.save(venue_data.civic_provider_data)

        if self._venue_restore_zone_id is not None:
            venue_game_data = GameplaySaveData_pb2.PersistableVenueGameService()
            venue_game_data.venue_restore_zone_id = self._venue_restore_zone_id
            venue_game_data.venue_restore_type_id = self._venue_restore_type_id
            venue_game_data.venue_restore_alarm_time = self._venue_restore_alarm_handler.get_remaining_time().in_ticks()
            save_slot_data.gameplay_data.venue_game_service = venue_game_data

    def load_providers(self, zone_data=None):
        persistence_service = services.get_persistence_service()

        def _get_current_venue(zone_id):
            neighborhood_data = persistence_service.get_neighborhood_proto_buf_from_zone_id(zone_id)
            for lot_data in neighborhood_data.lots:
                if zone_id == lot_data.zone_instance_id:
                    return lot_data.venue_key

        current_zone_id = services.current_zone_id()
        zones = services.get_persistence_service().get_save_game_data_proto().zones
        for zone_data_msg in zones:
            if zone_data_msg is None:
                continue
            elif zone_data_msg.zone_id == current_zone_id:
                active_venue_tuning_id = get_current_venue(zone_data_msg.zone_id)
                raw_active_venue_tuning_id = get_current_venue((zone_data_msg.zone_id), allow_ineligible=True)
            else:
                active_venue_tuning_id = _get_current_venue(zone_data_msg.zone_id)
                raw_active_venue_tuning_id = active_venue_tuning_id
            if active_venue_tuning_id is None:
                self.set_provider(zone_data_msg.zone_id, None)
                continue
            venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
            active_venue_type = venue_manager.get(active_venue_tuning_id)
            raw_active_venue_type = venue_manager.get(raw_active_venue_tuning_id)
            source_venue_type = VenueService.get_variable_venue_source_venue(raw_active_venue_type)
            if source_venue_type is None:
                self.set_provider(zone_data_msg.zone_id, None)
                continue
            if not source_venue_type.variable_venues is None:
                if source_venue_type.variable_venues is not None:
                    if not source_venue_type.variable_venues.enable_civic_policy_support:
                        self.set_provider(zone_data_msg.zone_id, None)
                        continue
                else:
                    existing_provider = self.get_provider(zone_data_msg.zone_id)
                    if existing_provider is not None:
                        if existing_provider.source_venue_type is source_venue_type:
                            continue
                    provider = source_venue_type.variable_venues.civic_policy(source_venue_type, active_venue_type)
                    provider or self.set_provider(zone_data_msg.zone_id, None)
                    continue
                self.set_provider(zone_data_msg.zone_id, provider)
                if zone_data_msg.HasField('gameplay_zone_data') and zone_data_msg.gameplay_zone_data.HasField('venue_data') and zone_data_msg.gameplay_zone_data.venue_data.HasField('civic_provider_data'):
                    provider.load(zone_data_msg.gameplay_zone_data.venue_data.civic_provider_data)

    def load(self, zone_data=None):
        self.load_providers(zone_data=zone_data)
        save_slot_data_msg = services.get_persistence_service().get_save_slot_proto_buff()
        if save_slot_data_msg.gameplay_data.HasField('venue_game_service'):
            venue_game_data = save_slot_data_msg.gameplay_data.venue_game_service
            self._venue_restore_type_id = venue_game_data.venue_restore_type_id
            self._venue_restore_zone_id = venue_game_data.venue_restore_zone_id
            if self._venue_restore_type_id == services.venue_service().get_venue_tuning(self._venue_restore_zone_id).guid64:
                self._venue_restore_alarm_handler = alarms.add_alarm(self,
                  (TimeSpan(venue_game_data.venue_restore_alarm_time)),
                  (self._restore_venue_type_delay_handler),
                  repeating=False)
            else:
                self._venue_restore_zone_id = None
                self._venue_restore_type_id = None

    def get_zone_for_provider(self, provider):
        zone_manager = services.get_zone_manager()
        for zone, stored_provider in self._zone_provider.items():
            if stored_provider is provider:
                return zone_manager.get(zone, allow_uninstantiated_zones=True)

    def get_provider(self, zone_id):
        return self._zone_provider.get(zone_id)

    def set_provider(self, zone_id, provider):
        if zone_id in self._zone_provider:
            self._zone_provider[zone_id].stop_civic_policy_provider()
            del self._zone_provider[zone_id]
        if provider is not None:
            self._zone_provider[zone_id] = provider

    def change_provider_venue_type(self, provider, active_venue_type, source_venue_type=None):
        zone = self.get_zone_for_provider(provider)
        if zone is None:
            return False
        zone_id = zone.id
        return self.change_venue_type(zone_id, active_venue_type, source_venue_type=source_venue_type, zone=zone)

    def change_venue_type(self, zone_id, active_venue_type, source_venue_type=None, zone=None):
        if not zone:
            zone = services.get_zone_manager().get(zone_id, allow_uninstantiated_zones=True)
        else:
            persistence_service = services.get_persistence_service()
            neighborhood_data = persistence_service.get_neighborhood_proto_buf_from_zone_id(zone_id)
            for lot_data in neighborhood_data.lots:
                if zone_id == lot_data.zone_instance_id:
                    if lot_data.venue_key == active_venue_type.guid64:
                        return False
                    lot_data.venue_key = active_venue_type.guid64
                    if lot_data.sub_venue_infos:
                        for sub_venue_info in lot_data.sub_venue_infos:
                            if sub_venue_info.sub_venue_key == lot_data.venue_key:
                                lot_data.venue_eligible = sub_venue_info.sub_venue_eligible
                                break
                        else:
                            sub_venue_info = lot_data.sub_venue_infos.add()
                            sub_venue_info.sub_venue_key = lot_data.venue_key
                            sub_venue_info.sub_venue_eligible = False
                            lot_data.venue_eligible = False

                    break

            on_active_lot = zone_id == services.current_zone_id()
            if on_active_lot:
                if source_venue_type is None:
                    source_venue_type = VenueService.get_variable_venue_source_venue(active_venue_type)
                services.venue_service().on_change_venue_type_at_runtime(active_venue_type, source_venue_type)
            lot_id = None
            world_id = None
            if zone.is_instantiated:
                lot_id = zone.lot.lot_id
                world_id = zone.world_id
            else:
                save_game_data = persistence_service.get_save_game_data_proto()
                for zone_data in save_game_data.zones:
                    if zone_data.zone_id == zone_id:
                        lot_id = zone_data.lot_id
                        world_id = zone_data.world_id
                        break

        if lot_id is None or world_id is None:
            return False
        if zone.is_instantiated:
            self._sub_venue_loading = True
        distributor = Distributor.instance()
        venue_update_request_msg = Venue_pb2.VenueUpdateRequest()
        venue_update_request_msg.venue_key = active_venue_type.guid64
        venue_update_request_msg.lot_id = lot_id
        venue_update_request_msg.world_id = world_id
        distributor.add_event(Consts_pb2.MSG_SET_SUB_VENUE, venue_update_request_msg)
        distributor.add_event(Consts_pb2.MSG_NS_NEIGHBORHOOD_UPDATE, neighborhood_data)
        self.on_venue_type_changed(zone_id, active_venue_type)
        return True

    def on_sub_venue_finished_loading(self):
        if not self._sub_venue_loading:
            return
        self._sub_venue_loading = False
        for obj in services.object_manager().values():
            footprint_component = obj.get_component(FOOTPRINT_COMPONENT)
            if footprint_component is not None:
                footprint_component.on_finalize_load()

    @property
    def sub_venue_loading(self):
        return self._sub_venue_loading

    def _restore_venue_type_delay_handler(self, _):
        if self._venue_restore_type_id == services.venue_service().get_venue_tuning(self._venue_restore_zone_id).guid64:
            self.restore_venue_type(self._venue_restore_zone_id, None)

    def _clear_venue_restore_alarm(self):
        if self._venue_restore_alarm_handler is not None:
            self._venue_restore_zone_id = None
            alarms.cancel_alarm(self._venue_restore_alarm_handler)
            self._venue_restore_alarm_handler = None
            self._venue_restore_type_id = None

    def restore_venue_type(self, zone_id, delay):
        if delay:
            if zone_id == services.current_zone_id():
                self._venue_restore_alarm_handler = alarms.add_alarm(self,
                  delay,
                  (self._restore_venue_type_delay_handler),
                  repeating=False)
                self._venue_restore_zone_id = zone_id
                self._venue_restore_type_id = services.venue_service().get_venue_tuning(zone_id).guid64
                return
        if zone_id == self._venue_restore_zone_id:
            self._clear_venue_restore_alarm()
        active_venue_type = services.venue_service().get_venue_tuning(zone_id)
        source_venue_type = VenueService.get_variable_venue_source_venue(active_venue_type)
        self.change_venue_type(zone_id, source_venue_type, source_venue_type=source_venue_type)
