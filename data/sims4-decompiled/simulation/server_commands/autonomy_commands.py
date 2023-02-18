# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\autonomy_commands.py
# Compiled at: 2020-11-20 09:48:58
# Size of source mod 2**32: 35748 bytes

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
binary_operator ::= BINARY_ADD . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= or . 
expr ::= unary_not . 
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
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
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
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
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
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_not ::= expr UNARY_NOT . 
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
-> 
 L. 236       164  LOAD_CONST               None
from _math import Vector3
import time
from autonomy.autonomy_modes import AutonomyMode, FullAutonomy
from autonomy.autonomy_modifier import AutonomyModifier
from autonomy.settings import AutonomyState, AutonomySettingsGroup, AutonomyRandomization
from objects.object_enums import ResetReason
from server_commands.argument_helpers import OptionalTargetParam, get_optional_target, TunableInstanceParam
import alarms, autonomy.autonomy_util, date_and_time, objects.components.types, services, sims.sim, sims4.commands, sims4.log, sims4.resources, singletons
logger = sims4.log.Logger('Autonomy')
automation_logger = sims4.log.Logger('AutonomyAutomation')
with sims4.reload.protected(globals()):
    g_distance_estimate_alarm_handle = None

@sims4.commands.Command('autonomy.show')
def show_autonomy_settings(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output("Couldn't find Sim.", _connection)
        return
    autonomy_state = _convert_state_to_string(sim.get_autonomy_state_setting())
    autonomy_randomization = _convert_randomization_to_string(sim.get_autonomy_randomization_setting())
    selected_sim_autonomy_enabled = services.autonomy_service()._selected_sim_autonomy_enabled
    sims4.commands.output('Autonomy State: {}\nAutonomyRandomization: {}\nSelected Sim Autonomy: {}'.format(autonomy_state, autonomy_randomization, selected_sim_autonomy_enabled), _connection)


@sims4.commands.Command('autonomy.sim')
def sim_autonomy_state(state, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    true_state = _parse_state(state, _connection=_connection)
    if true_state is None:
        return
    sim.autonomy_settings.set_setting(true_state, sim.get_autonomy_settings_group())


@sims4.commands.Command('autonomy.sim_randomization', command_type=(sims4.commands.CommandType.Automation))
def sim_autonomy_randomization(randomization, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    true_randomization = _parse_randomization(randomization)
    sim.autonomy_settings.set_setting(true_randomization, sim.get_autonomy_settings_group())


@sims4.commands.Command('autonomy.household', command_type=(sims4.commands.CommandType.Live))
def household_autonomy_state(state, opt_sim: OptionalTargetParam=None, settings_group: AutonomySettingsGroup=AutonomySettingsGroup.DEFAULT, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    household = sim.household
    if household is None:
        sims4.commands.output('No household for sim {}'.format(sim), _connection)
        return
    true_state = _parse_state(state, _connection=_connection)
    if true_state is None:
        return
    household.autonomy_settings.set_setting(true_state, settings_group)


@sims4.commands.Command('autonomy.household_randomization', command_type=(sims4.commands.CommandType.Automation))
def household_autonomy_randomization(randonmization, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    household = sim.household
    if household is None:
        sims4.commands.output('No household for sim {}'.format(sim), _connection)
        return
    true_randomization = _parse_randomization(randonmization)
    household.autonomy_settings.set_setting(true_randomization, AutonomySettingsGroup.DEFAULT)


@sims4.commands.Command('autonomy.global', command_type=(sims4.commands.CommandType.Automation))
def global_autonomy_state(state, settings_group: AutonomySettingsGroup=AutonomySettingsGroup.DEFAULT, _connection=None):
    autonomy_service = services.autonomy_service()
    true_state = _parse_state(state, _connection=_connection)
    if true_state is None:
        return
    autonomy_service.global_autonomy_settings.set_setting(true_state, settings_group)
    sims4.commands.output('Setting Global autonomy state to {} '.format(true_state), _connection)


@sims4.commands.Command('autonomy.global_randomization', command_type=(sims4.commands.CommandType.Automation))
def global_autonomy_randomization(randomization, settings_group: AutonomySettingsGroup=AutonomySettingsGroup.DEFAULT, _connection=None):
    autonomy_service = services.autonomy_service()
    true_randomization = _parse_randomization(randomization)
    if true_randomization is not None:
        autonomy_service.global_autonomy_settings.set_setting(true_randomization, settings_group)


@sims4.commands.Command('autonomy.global_all', command_type=(sims4.commands.CommandType.Automation))
def all_autonomy_state(state, _connection=None):
    autonomy_service = services.autonomy_service()
    true_state = _parse_state(state, _connection=_connection)
    if true_state is None:
        return
    for settings_group in AutonomySettingsGroup:
        autonomy_service.global_autonomy_settings.set_setting(true_state, settings_group)


@sims4.commands.Command('autonomy.set_autonomy_for_active_sim_option', command_type=(sims4.commands.CommandType.Live))
def set_autonomy_for_active_sim_option(enabled: bool, _connection=None):
    services.autonomy_service().set_autonomy_for_active_sim(enabled)


@sims4.commands.Command('autonomy.ambient', 'walkby.toggle', command_type=(sims4.commands.CommandType.Automation))
def set_ambient_autonomy(enabled: bool=None, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    if enabled is None:
        enabled = not tgt_client.account.debug_ambient_npcs_enabled
    tgt_client.account.debug_ambient_npcs_enabled = enabled
    sims4.commands.output('Ambient NPCs ' + ('enabled' if enabled else 'disabled'), _connection)


def _parse_state--- This code section failed: ---

 L. 224         0  LOAD_FAST                'state'
                2  LOAD_METHOD              lower
                4  CALL_METHOD_0         0  '0 positional arguments'
                6  STORE_FAST               'state_lower'

 L. 225         8  LOAD_FAST                'state_lower'
               10  LOAD_STR                 'on'
               12  COMPARE_OP               ==
               14  POP_JUMP_IF_TRUE     40  'to 40'
               16  LOAD_FAST                'state_lower'
               18  LOAD_STR                 'true'
               20  COMPARE_OP               ==
               22  POP_JUMP_IF_TRUE     40  'to 40'
               24  LOAD_FAST                'state_lower'
               26  LOAD_STR                 'full'
               28  COMPARE_OP               ==
               30  POP_JUMP_IF_TRUE     40  'to 40'
               32  LOAD_FAST                'state_lower'
               34  LOAD_STR                 '3'
               36  COMPARE_OP               ==
               38  POP_JUMP_IF_FALSE    46  'to 46'
             40_0  COME_FROM            30  '30'
             40_1  COME_FROM            22  '22'
             40_2  COME_FROM            14  '14'

 L. 226        40  LOAD_GLOBAL              AutonomyState
               42  LOAD_ATTR                FULL
               44  RETURN_VALUE     
             46_0  COME_FROM            38  '38'

 L. 227        46  LOAD_FAST                'state_lower'
               48  LOAD_STR                 'medium'
               50  COMPARE_OP               ==
               52  POP_JUMP_IF_FALSE    60  'to 60'

 L. 228        54  LOAD_GLOBAL              AutonomyState
               56  LOAD_ATTR                MEDIUM
               58  RETURN_VALUE     
             60_0  COME_FROM            52  '52'

 L. 229        60  LOAD_FAST                'state_lower'
               62  LOAD_STR                 'limitedonly'
               64  COMPARE_OP               ==
               66  POP_JUMP_IF_TRUE    100  'to 100'
               68  LOAD_FAST                'state_lower'
               70  LOAD_STR                 'la'
               72  COMPARE_OP               ==
               74  POP_JUMP_IF_TRUE    100  'to 100'
               76  LOAD_FAST                'state_lower'
               78  LOAD_STR                 'off'
               80  COMPARE_OP               ==
               82  POP_JUMP_IF_TRUE    100  'to 100'
               84  LOAD_FAST                'state_lower'
               86  LOAD_STR                 'false'
               88  COMPARE_OP               ==
               90  POP_JUMP_IF_TRUE    100  'to 100'
               92  LOAD_FAST                'state_lower'
               94  LOAD_STR                 '1'
               96  COMPARE_OP               ==
               98  POP_JUMP_IF_FALSE   106  'to 106'
            100_0  COME_FROM            90  '90'
            100_1  COME_FROM            82  '82'
            100_2  COME_FROM            74  '74'
            100_3  COME_FROM            66  '66'

 L. 230       100  LOAD_GLOBAL              AutonomyState
              102  LOAD_ATTR                LIMITED_ONLY
              104  RETURN_VALUE     
            106_0  COME_FROM            98  '98'

 L. 231       106  LOAD_FAST                'state_lower'
              108  LOAD_STR                 'undefined'
              110  COMPARE_OP               ==
              112  POP_JUMP_IF_TRUE    122  'to 122'
              114  LOAD_FAST                'state_lower'
              116  LOAD_STR                 'default'
              118  COMPARE_OP               ==
              120  POP_JUMP_IF_FALSE   128  'to 128'
            122_0  COME_FROM           112  '112'

 L. 232       122  LOAD_GLOBAL              AutonomyState
              124  LOAD_ATTR                UNDEFINED
              126  RETURN_VALUE     
            128_0  COME_FROM           120  '120'

 L. 234       128  LOAD_GLOBAL              sims4
              130  LOAD_ATTR                commands
              132  LOAD_METHOD              output
              134  LOAD_STR                 'Invalid Autonomy State: {}. Valid values are on, full, true, medium, false, off, default, undefined, limitedonly'
              136  LOAD_METHOD              format
              138  LOAD_FAST                'state_lower'
              140  CALL_METHOD_1         1  '1 positional argument'
              142  LOAD_FAST                '_connection'
              144  CALL_METHOD_2         2  '2 positional arguments'
              146  POP_TOP          

 L. 235       148  LOAD_GLOBAL              logger
              150  LOAD_ATTR                error
              152  LOAD_STR                 'Unknown state: {}'
              154  LOAD_FAST                'state_lower'
              156  LOAD_STR                 'rmccord'
              158  LOAD_CONST               ('owner',)
              160  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              162  POP_TOP          

 L. 236       164  LOAD_CONST               None
              166  RETURN_VALUE     

Parse error at or near `LOAD_CONST' instruction at offset 164


def _convert_state_to_string(autonomy_state):
    if autonomy_state == AutonomyState.UNDEFINED:
        return 'Undefined'
    if autonomy_state == AutonomyState.DISABLED:
        return 'Disabled'
    if autonomy_state == AutonomyState.LIMITED_ONLY:
        return 'Limited Only'
    if autonomy_state == AutonomyState.MEDIUM:
        return 'Medium'
    if autonomy_state == AutonomyState.FULL:
        return 'Full'
    return '<Unknown State: {}>'.format(autonomy_state)


def _parse_randomization(randomization):
    randomization_lower = randomization.lower()
    if randomization_lower == 'on' or randomization_lower == 'true' or randomization_lower == 'enabled':
        return AutonomyRandomization.ENABLED
    if randomization_lower == 'off' or randomization_lower == 'false' or randomization_lower == 'disabled':
        return AutonomyRandomization.DISABLED
    if randomization_lower == 'undefined' or randomization_lower == 'default':
        return AutonomyRandomization.UNDEFINED
    logger.error('Unknown randomization: {}', randomization_lower, owner='rez')
    return


def _convert_randomization_to_string(autonomy_randomization):
    if autonomy_randomization == AutonomyRandomization.UNDEFINED:
        return 'Undefined'
    if autonomy_randomization == AutonomyRandomization.DISABLED:
        return 'Disabled'
    if autonomy_randomization == AutonomyRandomization.ENABLED:
        return 'Enabled'
    return '<Unknown Randomization: {}>'.format(autonomy_randomization)


@sims4.commands.Command('autonomy.show_timers')
def show_autonomy_timers(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        sim.debug_output_autonomy_timers(_connection)
    else:
        sims4.commands.output('No target for autonomy.show_timers.', _connection)


@sims4.commands.Command('autonomy.clear_skipped_autonomy')
def clear_skipped_autonomy(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        sim.clear_all_autonomy_skip_sis()
    else:
        sims4.commands.output('No target for autonomy.clear_skipped_autonomy.', _connection)


def _reset_autonomy_timers_for_all_objects():
    for obj in services.object_manager().valid_objects():
        if obj.has_component(objects.components.types.AUTONOMY_COMPONENT):
            obj.debug_update_autonomy_timer(FullAutonomy)


@sims4.commands.Command('autonomy.toggle_user_directed_interaction_full_autonomy_ping')
def override_disable_autonomous_multitasking_if_user_directed(enabled=None, _connection=None):
    if enabled is None:
        to_enabled = None
    else:
        enabled_lower = enabled.lower()
        if not enabled_lower == 'on':
            if enabled_lower == 'true' or enabled_lower == 'enabled':
                to_enabled = True
        elif not enabled_lower == 'off':
            if enabled_lower == 'false' or enabled_lower == 'disabled':
                to_enabled = False
        elif enabled_lower == 'undefined' or enabled_lower == 'default':
            to_enabled = singletons.DEFAULT
    status = AutonomyMode.toggle_disable_autonomous_multitasking_if_user_directed(to_enabled)
    sims4.commands.output('Current disable autonomous multitasking: {}'.format(status), _connection)


@sims4.commands.Command('autonomy.override_full_autonomy_delay', command_type=(sims4.commands.CommandType.Automation))
def override_full_autonomy_delay(lower_bound: float, upper_bound: float, _connection=None):
    AutonomyMode.override_full_autonomy_delay(lower_bound, upper_bound)
    _reset_autonomy_timers_for_all_objects()


@sims4.commands.Command('autonomy.clear_full_autonomy_override', command_type=(sims4.commands.CommandType.Automation))
def clear_full_autonomy_override(_connection=None):
    AutonomyMode.clear_full_autonomy_delay_override()
    _reset_autonomy_timers_for_all_objects()


@sims4.commands.Command('autonomy.override_full_autonomy_delay_after_user_action', command_type=(sims4.commands.CommandType.Automation))
def override_full_autonomy_delay_after_user_action(delay: float, _connection=None):
    AutonomyMode.override_full_autonomy_delay_after_user_action(delay)
    _reset_autonomy_timers_for_all_objects()


@sims4.commands.Command('autonomy.clear_full_autonomy_delay_after_user_action', command_type=(sims4.commands.CommandType.Automation))
def clear_full_autonomy_delay_after_user_action(_connection=None):
    AutonomyMode.clear_full_autonomy_delay_after_user_action()
    _reset_autonomy_timers_for_all_objects()


@sims4.commands.Command('autonomy.reset_autonomy_alarm')
def reset_autonomy_alarm(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        sim.debug_reset_autonomy_alarm()
    else:
        sims4.commands.output('No target for autonomy.reset_autonomy_alarm.', _connection)


@sims4.commands.Command('autonomy.run')
def run_autonomy(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for autonomy.run', _connection)
        return
    sim.run_full_autonomy_next_ping()


@sims4.commands.Command('autonomy.test_ping', command_type=(sims4.commands.CommandType.Automation))
def test_ping_autonomy(opt_sim: OptionalTargetParam=None, affordance: TunableInstanceParam(sims4.resources.Types.INTERACTION)=None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        output('No target for autonomy.run')
        return
    if affordance is not None:
        affordance_list = (
         affordance,)
        commodity_list = affordance.commodity_flags
    else:
        affordance_list = None
        commodity_list = None
    selected_interaction = sim.run_test_autonomy_ping(affordance_list=affordance_list, commodity_list=commodity_list)
    output('Autonomy Test Ping: {}'.format(selected_interaction))


@sims4.commands.Command('autonomy.add_modifier')
def add_modifier(stat_multiplier_list_string, locked_stat_list_string='', decay_multiplier_list_string='', opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for autonomy.add_modifier', _connection)
        return
    multipliers = _read_multiplier_dictionary_from_string(stat_multiplier_list_string, _connection)
    if multipliers == None:
        sims4.commands.output('Unable to parse stat multiplier list.', _connection)
        return
    decay_multipliers = _read_multiplier_dictionary_from_string(decay_multiplier_list_string, _connection)
    if multipliers == None:
        sims4.commands.output('Unable to parse decay multiplier list.', _connection)
        return
    locked_stat_list = locked_stat_list_string.split()
    locked_stats = []
    for stat_str in locked_stat_list:
        stat = _get_stat_from_string(stat_str, _connection)
        if stat is None:
            return
        locked_stats.append(stat)

    modifier = AutonomyModifier(multipliers, locked_stats, decay_multipliers)
    handle = sim.add_statistic_modifier(modifier)
    sims4.commands.output('Successfully added autonomy modifier: {}.'.format(handle), _connection)


@sims4.commands.Command('autonomy.remove_modifier')
def remove_modifier(handle: int, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for autonomy.add_modifier', _connection)
        return
    elif sim.remove_statistic_modifier(handle):
        sims4.commands.output('Successfully removed autonomy modifier', _connection)
    else:
        sims4.commands.output('Unable to find autonomy handle: {}'.format(handle), _connection)


@sims4.commands.Command('autonomy.update_sleep_schedule')
def force_update_sleep_schedule(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for autonomy.update_sleep_schedule', _connection)
        return
    sim.update_sleep_schedule()


@sims4.commands.Command('autonomy.reset_multitasking_roll')
def reset_multitasking_roll(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for autonomy.reset_multitasking_roll', _connection)
        return
    sim.reset_multitasking_roll()


@sims4.commands.Command('qa.automation.start_autonomy_load_test', command_type=(sims4.commands.CommandType.Automation))
def start_autonomy_load_test(motive_value: float=-40, _connection=None):
    sim_list = [sim for sim in services.sim_info_manager().instanced_sims_gen()]
    global_autonomy_randomization('disabled', _connection=_connection)
    for sim in sim_list:
        sim.run_full_autonomy_next_ping()

    _randomize_all_motives_deterministically(sim_list, motive_value)
    services.autonomy_service().start_automated_load_test(_connection, len(sim_list))


@sims4.commands.Command('qa.automation.start_single_sim_performance_test', command_type=(sims4.commands.CommandType.Automation))
def start_single_sim_performance_test(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No target for qa.automation.start_single_sim_performance_test', _connection)
        return
    sim.reset(ResetReason.RESET_EXPECTED, None, 'start_single_sim_performance_test')
    services.autonomy_service().start_single_sim_load_test(_connection, sim)
    sim.run_full_autonomy_next_ping()


@sims4.commands.Command('autonomy.show_queue', command_type=(sims4.commands.CommandType.Automation))
def show_queue(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Autonomy Queue:')
    if services.autonomy_service()._active_sim is not None:
        output('    0) {}'.format(services.autonomy_service()._active_sim))
    else:
        output('    0) None')
    for index, request in enumerate((services.autonomy_service().queue), start=1):
        output('    {}) {}'.format(index, request.sim))

    queue_size = len(services.autonomy_service().queue)
    output('Queue size: {}'.format(queue_size))


@sims4.commands.Command('qa.automation.show_queue', command_type=(sims4.commands.CommandType.Automation))
def show_queue_automation(_connection=None):
    sims4.commands.automation_output('Autonomy; Queue:Begin', _connection)
    automation_logger.debug('Autonomy; Queue:Begin')
    for request in services.autonomy_service().queue:
        sims4.commands.automation_output('Autonomy; Queue:Data, Id:{}'.format(request.sim.id), _connection)
        automation_logger.debug('Autonomy; Queue:Data, Id:{}'.format(request.sim.id))

    sims4.commands.automation_output('Autonomy; Queue:End', _connection)
    automation_logger.debug('Autonomy; Queue:End')


@sims4.commands.Command('autonomy.show_update_times', command_type=(sims4.commands.CommandType.Automation))
def show_update_times(_connection=None):
    sim_info_manager = services.sim_info_manager()
    sim_times = []
    for sim in sim_info_manager.instanced_sims_gen():
        autonomy_component = sim.autonomy_component
        if autonomy_component is not None:
            sim_times.append((sim.full_name, autonomy_component.get_time_until_ping()))

    sim_times.sort(key=(lambda x: x[1]))
    output = sims4.commands.CheatOutput(_connection)
    output('Update Times:')
    for name, time in sim_times:
        output('    {}: {}'.format(time, name))


def _read_multiplier_dictionary_from_string(stat_list_string, _connection=None):
    string_list = stat_list_string.split()
    if len(string_list) % 2 != 0:
        sims4.commands.output("multiplier_list_string didn't have an even number of elements", _connection)
        return
    multiplier_dict = {}
    index = 0
    while index < len(string_list):
        stat = _get_stat_from_string(string_list[index], _connection)
        if stat is None:
            return
        try:
            multiplier = float(string_list[index + 1])
        except ValueError:
            sims4.commands.output('Multiplier value is not a valid float: {}.'.format(string_list[index + 1]), _connection)
            return
        else:
            multiplier_dict[stat] = multiplier
            index += 2

    return multiplier_dict


def _get_stat_from_string(stat_str, _connection):
    stat_name = stat_str.lower()
    stat = services.get_instance_manager(sims4.resources.Types.STATISTIC).get(stat_name)
    if stat is None:
        sims4.commands.output("Unable to get stat '{}'.".format(stat_name), _connection)
        return
    return stat


def _randomize_all_motives_deterministically(sim_list, motive_value: float):
    sim_list_length = len(sim_list)
    sim_list_index = 0
    while sim_list_index < sim_list_length:
        for commodity_type, count in autonomy.autonomy_modes.AutonomyMode.AUTOMATED_RANDOMIZATION_LIST.items():
            for _ in range(count):
                sim_list[sim_list_index].set_stat_value(commodity_type, motive_value)
                sim_list_index += 1
                if sim_list_index >= sim_list_length:
                    return

    logger.error('Weird exit in randomize_all_motives_deterministically()', owner='rez')


@sims4.commands.Command('autonomy.trigger_walkby', command_type=(sims4.commands.CommandType.DebugOnly))
def trigger_walkby(_connection=None):
    situation_id = services.current_zone().ambient_service.debug_update()
    if situation_id is not None:
        situation = services.get_zone_situation_manager().get(situation_id)
        sims4.commands.output('Created ambient situation: {}.{}'.format(situation, situation_id), _connection)
    else:
        sims4.commands.output('Did not create ambient situation. There are no types of walkbys that are available at this time.', _connection)
    return True


@sims4.commands.Command('autonomy.set_anchor', command_type=(sims4.commands.CommandType.DebugOnly))
def set_anchor(x, y, z, level, opt_sim=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output("Couldn't find Sim.", _connection)
        return
    vec = Vector3(x, y, z)
    sim.set_anchor((vec, level))


@sims4.commands.Command('autonomy.clear_anchor', command_type=(sims4.commands.CommandType.DebugOnly))
def clear_anchor(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output("Couldn't find Sim.", _connection)
        return
    sim.clear_anchor()


@sims4.commands.Command('autonomy.log_sim')
def sim_autonomy_log_on(status: bool, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Invalid Sim ID specified.', _connection)
        return False
    _set_sim_autonomy_log(sim, state=status)


def _set_sim_autonomy_log(sim: sims.sim.Sim, state=None):
    if state:
        services.autonomy_service().logging_sims.add(sim)
    else:
        services.autonomy_service().logging_sims.discard(sim)
    logger.debug('Autonomy log toggled to {0} on {1}', state, sim)
    return True


@sims4.commands.Command('autonomy.distance_estimates.enable', command_type=(sims4.commands.CommandType.Automation))
def autonomy_distance_estimates_enable(_connection=None):
    autonomy.autonomy_util.AutonomyAffordanceTimes.start()


@sims4.commands.Command('autonomy.distance_estimates.disable', command_type=(sims4.commands.CommandType.Automation))
def autonomy_distance_estimates_disable(_connection=None):
    autonomy.autonomy_util.AutonomyAffordanceTimes.stop()


@sims4.commands.Command('autonomy.distance_estimates.reset', command_type=(sims4.commands.CommandType.Automation))
def autonomy_reset_aggregate_times(_connection=None):
    autonomy.autonomy_util.AutonomyAffordanceTimes.reset()


@sims4.commands.Command('autonomy.distance_estimates.dump', command_type=(sims4.commands.CommandType.Automation))
def autonomy_distance_estimates_dump(_connection=None):
    autonomy.autonomy_util.AutonomyAffordanceTimes.dump(connection=_connection)


@sims4.commands.Command('autonomy.distance_estimates.perform_timed_run', command_type=(sims4.commands.CommandType.Automation))
def autonomy_distance_estimates_perform_timed_run(time_to_run_in_seconds: int=180, _connection=None):
    global g_distance_estimate_alarm_handle
    if g_distance_estimate_alarm_handle is not None:
        autonomy_distance_estimates_disable(_connection=_connection)
        alarms.cancel_alarm(g_distance_estimate_alarm_handle)
        g_distance_estimate_alarm_handle = None
    autonomy_distance_estimates_enable(_connection=_connection)

    def _finish_test_and_write_file(_):
        global g_distance_estimate_alarm_handle
        autonomy_distance_estimates_dump(_connection=_connection)
        autonomy_distance_estimates_disable(_connection=_connection)
        g_distance_estimate_alarm_handle = None

    time_span = date_and_time.create_time_span(minutes=time_to_run_in_seconds)
    g_distance_estimate_alarm_handle = alarms.add_alarm_real_time(services.autonomy_service(), time_span, _finish_test_and_write_file)
