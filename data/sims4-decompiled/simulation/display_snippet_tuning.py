# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\display_snippet_tuning.py
# Compiled at: 2021-09-13 22:15:21
# Size of source mod 2**32: 20532 bytes

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
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex ::= expr starred CALL_FUNCTION_EX . 
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST BUILD_CONST_KEY_MAP_1 . 
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_7
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= _lambda_body . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_ex . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= or . 
expr ::= set . 
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
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_10
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10 . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
lstmt ::= stmt . 
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
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
set ::= expr . BUILD_SET_1
set ::= expr BUILD_SET_1 . 
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
stmt ::= assign . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
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
tuple ::= expr expr expr BUILD_TUPLE_3 . 
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 409       280  LOAD_FAST                'test_result'
                 282  LOAD_ATTR                tooltip
                 284  LOAD_CONST               None
                 286  COMPARE_OP               is
             288_290  POP_JUMP_IF_FALSE   296  'to 296'
                 292  LOAD_CONST               None
                 294  JUMP_FORWARD        314  'to 314'
               296_0  COME_FROM           288  '288'
                 296  LOAD_FAST                'test_result'
                 298  LOAD_ATTR                tooltip
                 300  LOAD_CONST               ('tooltip',)
                 302  BUILD_CONST_KEY_MAP_1     1 
                 304  LOAD_CLOSURE             'tokens'
                 306  BUILD_TUPLE_1         1 
                 308  LOAD_LAMBDA              '<code_object <lambda>>'
                 310  LOAD_STR                 'DisplaySnippetPickerSuperInteraction.picker_rows_gen.<locals>.<lambda>'
                 312  MAKE_FUNCTION_10         'keyword-only, closure'
->             314_0  COME_FROM           294  '294'
                 314  STORE_FAST               'tooltip'
from collections import namedtuple
from event_testing.resolver import InteractionResolver
from event_testing.tests import TunableTestSetWithTooltip
from interactions import ParticipantTypeSim
from interactions.base.picker_interaction import PickerSuperInteraction
from interactions.utils.display_mixin import get_display_mixin
from interactions.utils.localization_tokens import LocalizationTokens
from interactions.utils.loot import LootActions
from interactions.utils.tunable import TunableContinuation
from sims.university.university_scholarship_tuning import ScholarshipMaintenaceType, ScholarshipEvaluationType, MeritEvaluation
from sims4.localization import TunableLocalizedString, TunableLocalizedStringFactory
from sims4.tuning.tunable import TunableEnumFlags, TunableList, TunableTuple, TunableReference, Tunable, TunableRange, TunableVariant, OptionalTunable, AutoFactoryInit, HasTunableSingletonFactory
from sims4.tuning.tunable_base import GroupNames, ExportModes
from sims4.utils import flexmethod
from singletons import DEFAULT
from ui.ui_dialog_picker import TunablePickerDialogVariant, ObjectPickerTuningFlags, BasePickerRow
import enum, event_testing, services, sims4.tuning
logger = sims4.log.Logger('Display Snippet', default_owner='shipark')
SnippetDisplayMixin = get_display_mixin(use_string_tokens=True, has_description=True, has_icon=True, has_tooltip=True, enabled_by_default=True,
  has_secondary_icon=True,
  export_modes=(ExportModes.All))

class DisplaySnippet(SnippetDisplayMixin, metaclass=sims4.tuning.instances.HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.SNIPPET)):
    pass


class ScholarshipAmountEnum(enum.Int, export=False):
    FIXED_AMOUNT = 0
    EVALUATION_TYPE = 1


class Scholarship(DisplaySnippet):

    @classmethod
    def _verify_tuning_callback(cls):
        if not cls._display_data.instance_display_name:
            logger.error("Scholarships require a display name, but scholarship ({})'s display name has a None value.", str(cls))
        else:
            if not cls._display_data.instance_display_description:
                logger.error("Scholarships require a display description, but scholarship ({})'s display description has a None value.", str(cls))
            cls._display_data.instance_display_icon or logger.error("Scholarships require a display icon, but scholarship ({})'s display icon has a None value.", str(cls))

    INSTANCE_TUNABLES = {'evaluation_type':ScholarshipEvaluationType.TunableFactory(description='\n            The evaluation type used by this scholarship.\n            '), 
     'maintenance_type':ScholarshipMaintenaceType.TunableFactory(description='\n            The maintenance requirement of this scholarship.\n            '), 
     'amount':TunableVariant(description='\n            If fixed_amount, use the tuned value when receiving the scholarship.\n            If evaluation_type, use the evaluation type to determine what the value of \n            the scholarship should be. \n            ',
       fixed_amount=TunableTuple(amount=TunableRange(description='\n                    The amount of money to award a Sim if they receive this scholarship.\n                    ',
       tunable_type=int,
       default=50,
       minimum=1),
       locked_args={'amount_enum': ScholarshipAmountEnum.FIXED_AMOUNT}),
       evaluation_type=TunableTuple(locked_args={'amount_enum': ScholarshipAmountEnum.EVALUATION_TYPE}))}

    @classmethod
    def verify_tuning_callback(cls):
        if cls.amount.amount_enum == ScholarshipAmountEnum.EVALUATION_TYPE:
            if not isinstance(cls.evaluation_type, MeritEvaluation):
                logger.error('Scholarship ({}) specified its value to be determined                    by use-evaluation-type, but evaluation type ({}) does not support                    dynamic value generation.', cls, cls.evaluation_type)

    @classmethod
    def get_value(cls, sim_info):
        if cls.amount.amount_enum == ScholarshipAmountEnum.FIXED_AMOUNT:
            return cls.amount.amount
        return cls.evaluation_type.get_value(sim_info)


class Organization(DisplaySnippet):
    INSTANCE_TUNABLES = {'progress_statistic':TunableReference(description='\n            The Ranked Statistic represents Organization Progress.\n            ',
       manager=services.get_instance_manager(sims4.resources.Types.STATISTIC),
       class_restrictions='RankedStatistic',
       export_modes=ExportModes.All), 
     'hidden':Tunable(description='\n            If True, then the organization is hidden from the organization panel.\n            ',
       tunable_type=bool,
       default=False,
       export_modes=ExportModes.All), 
     'organization_task_data':TunableList(description='\n            List of possible tested organization tasks that can be offered to \n            active organization members.\n            ',
       tunable=TunableTuple(description='\n                Tuple of test and aspirations that is run on activating\n                organization tasks.\n                ',
       tests=event_testing.tests.TunableTestSet(description='\n                   Tests run when the task is activated. If tests do not pass,\n                   the tasks are not considered for assignment.\n                   '),
       organization_task=TunableReference(description='\n                    An aspiration to use for task completion.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.ASPIRATION)),
       class_restrictions='AspirationOrganizationTask'))), 
     'organization_filter':TunableReference(description="\n            Terms to add a member to the Organization's membership list.\n            ",
       manager=services.get_instance_manager(sims4.resources.Types.SIM_FILTER),
       class_restrictions=('TunableSimFilter', )), 
     'no_events_are_scheduled_string':OptionalTunable(description='\n            If enabled and the organization has no scheduled events, this text\n            will be displayed in the org panel background.\n            ',
       tunable=TunableLocalizedString(description='\n                The string to show in the organization panel if there are no scheduled\n                events.\n                '))}


snippet_override_data = namedtuple('SnippetDisplayData', ('display_name', 'display_description',
                                                          'display_tooltip', 'display_icon'))

class _DisplaySnippetTextOverrides(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'display_name_override':OptionalTunable(description='\n            If enabled, the localized name override for each display snippet in \n            the list. \n            ',
       tunable=TunableLocalizedStringFactory(description='\n                The localized name override for each display snippet in \n                the list. \n                ')), 
     'display_description_override':OptionalTunable(description='\n            If enabled, the localized description override for each display \n            snippet in the list. \n            ',
       tunable=TunableLocalizedStringFactory(description='\n                The localized description override for each display snippet in \n                the list. \n                ')), 
     'display_tooltip_override':OptionalTunable(description='\n            If enabled, the localized tooltip override for each display \n            snippet in the list. \n            ',
       tunable=TunableLocalizedStringFactory(description='\n               The localized tooltip override for each display snippet in the \n               list. \n               '))}

    def __call__(self, original_snippet):
        name = self.display_name_override if self.display_name_override is not None else original_snippet.display_name
        description = self.display_description_override if self.display_description_override is not None else original_snippet.display_description
        tooltip = self.display_tooltip_override if self.display_tooltip_override is not None else original_snippet.display_tooltip
        return snippet_override_data(display_name=name, display_description=description,
          display_tooltip=tooltip,
          display_icon=(original_snippet.display_icon))


class _PickerDisplaySnippet(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'display_snippet':TunableReference(description='\n            A display snippet that holds the display data that will\n            populate the row in the picker.\n            ',
       manager=services.get_instance_manager(sims4.resources.Types.SNIPPET),
       class_restrictions='DisplaySnippet',
       allow_none=False), 
     'loot_on_selected':TunableList(description='\n            A list of loot actions that will be applied to the subject Sim.\n            ',
       tunable=LootActions.TunableReference(description='\n                A loot action applied to the subject Sim.\n                ')), 
     'tests':TunableTestSetWithTooltip(description='\n            Test set that must pass for this snippet to be available.\n            NOTE: A tooltip test result will take priority over any\n            instance display tooltip tuned in the display snippet.\n            \n            ID of the snippet will be the PickedItemID participant\n            '), 
     'display_snippet_text_tokens':LocalizationTokens.TunableFactory(description='\n            Localization tokens passed into the display snippet text fields.\n            These will be appended to the list of tokens when evaluating \n            strings for this snippet. \n            ',
       tuning_group=GroupNames.PICKERTUNING)}

    def test(self, resolver):
        return self.tests.run_tests(resolver, search_for_tooltip=True)


class DisplaySnippetPickerSuperInteraction(PickerSuperInteraction):
    INSTANCE_TUNABLES = {'picker_dialog':TunablePickerDialogVariant(description='\n            The item picker dialog.\n            ',
       available_picker_flags=ObjectPickerTuningFlags.ITEM,
       tuning_group=GroupNames.PICKERTUNING), 
     'subject':TunableEnumFlags(description="\n            To whom 'loot on selected' should be applied.\n            ",
       enum_type=ParticipantTypeSim,
       default=ParticipantTypeSim.Actor,
       tuning_group=GroupNames.PICKERTUNING), 
     'display_snippets':TunableList(description='\n            The list of display snippets available to select and paired loot actions\n            that will run if selected.\n            ',
       tunable=_PickerDisplaySnippet.TunableFactory(description='\n                Display snippet available to select.\n                '),
       tuning_group=GroupNames.PICKERTUNING), 
     'display_snippet_text_tokens':LocalizationTokens.TunableFactory(description='\n            Localization tokens passed into the display snippet text fields.\n            \n            When acting on the individual items within the snippet list, the \n            following text tokens will be appended to this list of tokens (in \n            order):\n            0: snippet instance display name\n            1: snippet instance display description\n            2: snippet instance display tooltip\n            3: tokens tuned alongside individual snippets within the snippet list\n            ',
       tuning_group=GroupNames.PICKERTUNING), 
     'display_snippet_text_overrides':OptionalTunable(description='\n            If enabled, display snippet text overrides for all snippets \n            to be displayed in the picker. \n            \n            Can be used together with the display snippet text tokens to \n            act as text wrappers around the existing snippet display data.\n            ',
       tunable=_DisplaySnippetTextOverrides.TunableFactory(description='\n                Display snippet text overrides for all snippets to be displayed\n                in the picker. \n            \n                Can be used together with the display snippet text tokens to \n                act as text wrappers around the existing snippet display data.\n                '),
       tuning_group=GroupNames.PICKERTUNING), 
     'continuations':TunableList(description='\n            List of continuations to push when a snippet is selected.\n            \n            ID of the snippet will be the PickedItemID participant in the \n            continuation.\n            ',
       tunable=TunableContinuation(),
       tuning_group=GroupNames.PICKERTUNING), 
     'run_continuations_on_no_selection':Tunable(description='\n            Checked, runs continuations regardless if anything is selected.\n            Unchecked, continuations are only run if something is selected.\n            ',
       tunable_type=bool,
       default=True,
       tuning_group=GroupNames.PICKERTUNING)}

    @classmethod
    def has_valid_choice(cls, target, context, **kwargs):
        snippet_count = 0
        for _ in (cls.picker_rows_gen)(target, context, **kwargs):
            snippet_count += 1
            if snippet_count >= cls.picker_dialog.min_selectable:
                return True

        return False

    def _run_interaction_gen(self, timeline):
        self._show_picker_dialog((self.sim), target_sim=(self.sim))
        return True
        if False:
            yield None

    @flexmethod
    def picker_rows_gen--- This code section failed: ---

 L. 375         0  LOAD_FAST                'inst'
                2  LOAD_CONST               None
                4  COMPARE_OP               is-not
                6  POP_JUMP_IF_FALSE    12  'to 12'
                8  LOAD_FAST                'inst'
               10  JUMP_FORWARD         14  'to 14'
             12_0  COME_FROM             6  '6'
               12  LOAD_FAST                'cls'
             14_0  COME_FROM            10  '10'
               14  STORE_FAST               'inst_or_cls'

 L. 376        16  LOAD_FAST                'target'
               18  LOAD_GLOBAL              DEFAULT
               20  COMPARE_OP               is-not
               22  POP_JUMP_IF_FALSE    28  'to 28'
               24  LOAD_FAST                'target'
               26  JUMP_FORWARD         32  'to 32'
             28_0  COME_FROM            22  '22'
               28  LOAD_FAST                'inst'
               30  LOAD_ATTR                target
             32_0  COME_FROM            26  '26'
               32  STORE_FAST               'target'

 L. 377        34  LOAD_FAST                'context'
               36  LOAD_GLOBAL              DEFAULT
               38  COMPARE_OP               is-not
               40  POP_JUMP_IF_FALSE    46  'to 46'
               42  LOAD_FAST                'context'
               44  JUMP_FORWARD         50  'to 50'
             46_0  COME_FROM            40  '40'
               46  LOAD_FAST                'inst'
               48  LOAD_ATTR                context
             50_0  COME_FROM            44  '44'
               50  STORE_FAST               'context'

 L. 378        52  LOAD_GLOBAL              InteractionResolver
               54  LOAD_FAST                'cls'
               56  LOAD_FAST                'inst'
               58  LOAD_FAST                'target'
               60  LOAD_FAST                'context'
               62  LOAD_CONST               ('target', 'context')
               64  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
               66  STORE_FAST               'resolver'

 L. 380        68  LOAD_FAST                'inst_or_cls'
               70  LOAD_ATTR                display_snippet_text_tokens
               72  LOAD_METHOD              get_tokens
               74  LOAD_FAST                'resolver'
               76  CALL_METHOD_1         1  '1 positional argument'
               78  STORE_FAST               'general_tokens'

 L. 381        80  LOAD_FAST                'inst_or_cls'
               82  LOAD_ATTR                display_snippet_text_overrides
               84  STORE_FAST               'overrides'

 L. 383        86  LOAD_CONST               0
               88  STORE_FAST               'index'

 L. 384     90_92  SETUP_LOOP          410  'to 410'
               94  LOAD_FAST                'inst_or_cls'
               96  LOAD_ATTR                display_snippets
               98  GET_ITER         
          100_102  FOR_ITER            408  'to 408'
              104  STORE_FAST               'display_snippet_data'

 L. 385       106  LOAD_FAST                'display_snippet_data'
              108  LOAD_ATTR                display_snippet
              110  STORE_FAST               'display_snippet'

 L. 388       112  LOAD_GLOBAL              InteractionResolver
              114  LOAD_FAST                'cls'
              116  LOAD_FAST                'inst'
              118  LOAD_FAST                'target'
              120  LOAD_FAST                'context'
              122  LOAD_FAST                'display_snippet'
              124  LOAD_ATTR                guid64
              126  BUILD_SET_1           1 
              128  LOAD_CONST               ('target', 'context', 'picked_item_ids')
              130  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              132  STORE_FAST               'resolver'

 L. 389       134  LOAD_FAST                'display_snippet_data'
              136  LOAD_METHOD              test
              138  LOAD_FAST                'resolver'
              140  CALL_METHOD_1         1  '1 positional argument'
              142  STORE_FAST               'test_result'

 L. 390       144  LOAD_FAST                'test_result'
              146  LOAD_ATTR                result
              148  STORE_FAST               'is_enable'

 L. 391       150  LOAD_FAST                'is_enable'
              152  POP_JUMP_IF_TRUE    166  'to 166'
              154  LOAD_FAST                'test_result'
              156  LOAD_ATTR                tooltip
              158  LOAD_CONST               None
              160  COMPARE_OP               is-not
          162_164  POP_JUMP_IF_FALSE   398  'to 398'
            166_0  COME_FROM           152  '152'

 L. 395       166  LOAD_FAST                'display_snippet'
              168  LOAD_ATTR                display_name
              170  LOAD_CONST               None
              172  COMPARE_OP               is-not
              174  POP_JUMP_IF_FALSE   186  'to 186'
              176  LOAD_FAST                'display_snippet'
              178  LOAD_ATTR                display_name
              180  LOAD_FAST                'general_tokens'
              182  CALL_FUNCTION_EX      0  'positional arguments only'
              184  JUMP_FORWARD        188  'to 188'
            186_0  COME_FROM           174  '174'
              186  LOAD_CONST               None
            188_0  COME_FROM           184  '184'

 L. 397       188  LOAD_FAST                'display_snippet'
              190  LOAD_ATTR                display_description
              192  LOAD_CONST               None
              194  COMPARE_OP               is-not
              196  POP_JUMP_IF_FALSE   208  'to 208'
              198  LOAD_FAST                'display_snippet'
              200  LOAD_ATTR                display_description
              202  LOAD_FAST                'general_tokens'
              204  CALL_FUNCTION_EX      0  'positional arguments only'
              206  JUMP_FORWARD        210  'to 210'
            208_0  COME_FROM           196  '196'
              208  LOAD_CONST               None
            210_0  COME_FROM           206  '206'

 L. 399       210  LOAD_FAST                'display_snippet'
              212  LOAD_ATTR                display_tooltip
              214  LOAD_CONST               None
              216  COMPARE_OP               is-not
              218  POP_JUMP_IF_FALSE   230  'to 230'
              220  LOAD_FAST                'display_snippet'
              222  LOAD_ATTR                display_tooltip
              224  LOAD_FAST                'general_tokens'
              226  CALL_FUNCTION_EX      0  'positional arguments only'
              228  JUMP_FORWARD        232  'to 232'
            230_0  COME_FROM           218  '218'
              230  LOAD_CONST               None
            232_0  COME_FROM           228  '228'
              232  BUILD_TUPLE_3         3 
              234  STORE_FAST               'snippet_default_tokens'

 L. 401       236  LOAD_FAST                'display_snippet_data'
              238  LOAD_ATTR                display_snippet_text_tokens
              240  LOAD_METHOD              get_tokens
              242  LOAD_FAST                'resolver'
              244  CALL_METHOD_1         1  '1 positional argument'
              246  STORE_FAST               'snippet_additional_tokens'

 L. 402       248  LOAD_FAST                'general_tokens'
              250  LOAD_FAST                'snippet_default_tokens'
              252  BINARY_ADD       
              254  LOAD_FAST                'snippet_additional_tokens'
              256  BINARY_ADD       
              258  STORE_DEREF              'tokens'

 L. 405       260  LOAD_FAST                'overrides'
              262  LOAD_CONST               None
              264  COMPARE_OP               is-not
          266_268  POP_JUMP_IF_FALSE   280  'to 280'

 L. 406       270  LOAD_FAST                'overrides'
              272  LOAD_FAST                'display_snippet_data'
              274  LOAD_ATTR                display_snippet
              276  CALL_FUNCTION_1       1  '1 positional argument'
              278  STORE_FAST               'display_snippet'
            280_0  COME_FROM           266  '266'

 L. 409       280  LOAD_FAST                'test_result'
              282  LOAD_ATTR                tooltip
              284  LOAD_CONST               None
              286  COMPARE_OP               is
          288_290  POP_JUMP_IF_FALSE   296  'to 296'
              292  LOAD_CONST               None
              294  JUMP_FORWARD        314  'to 314'
            296_0  COME_FROM           288  '288'
              296  LOAD_FAST                'test_result'
              298  LOAD_ATTR                tooltip
              300  LOAD_CONST               ('tooltip',)
              302  BUILD_CONST_KEY_MAP_1     1 
              304  LOAD_CLOSURE             'tokens'
              306  BUILD_TUPLE_1         1 
              308  LOAD_LAMBDA              '<code_object <lambda>>'
              310  LOAD_STR                 'DisplaySnippetPickerSuperInteraction.picker_rows_gen.<locals>.<lambda>'
              312  MAKE_FUNCTION_10         'keyword-only, closure'
            314_0  COME_FROM           294  '294'
              314  STORE_FAST               'tooltip'

 L. 410       316  LOAD_FAST                'tooltip'
          318_320  POP_JUMP_IF_TRUE    358  'to 358'

 L. 411       322  LOAD_FAST                'display_snippet'
              324  LOAD_ATTR                display_tooltip
              326  LOAD_CONST               None
              328  COMPARE_OP               is
          330_332  POP_JUMP_IF_FALSE   338  'to 338'
              334  LOAD_CONST               None
              336  JUMP_FORWARD        356  'to 356'
            338_0  COME_FROM           330  '330'
              338  LOAD_FAST                'display_snippet'
              340  LOAD_ATTR                display_tooltip
              342  LOAD_CONST               ('tooltip',)
              344  BUILD_CONST_KEY_MAP_1     1 
              346  LOAD_CLOSURE             'tokens'
              348  BUILD_TUPLE_1         1 
              350  LOAD_LAMBDA              '<code_object <lambda>>'
              352  LOAD_STR                 'DisplaySnippetPickerSuperInteraction.picker_rows_gen.<locals>.<lambda>'
              354  MAKE_FUNCTION_10         'keyword-only, closure'
            356_0  COME_FROM           336  '336'
              356  STORE_FAST               'tooltip'
            358_0  COME_FROM           318  '318'

 L. 412       358  LOAD_GLOBAL              BasePickerRow
              360  LOAD_FAST                'is_enable'

 L. 413       362  LOAD_FAST                'display_snippet'
              364  LOAD_ATTR                display_name
              366  LOAD_DEREF               'tokens'
              368  CALL_FUNCTION_EX      0  'positional arguments only'

 L. 414       370  LOAD_FAST                'display_snippet'
              372  LOAD_ATTR                display_icon

 L. 415       374  LOAD_FAST                'index'

 L. 416       376  LOAD_FAST                'display_snippet'
              378  LOAD_ATTR                display_description
              380  LOAD_DEREF               'tokens'
              382  CALL_FUNCTION_EX      0  'positional arguments only'

 L. 417       384  LOAD_FAST                'tooltip'
              386  LOAD_CONST               ('is_enable', 'name', 'icon', 'tag', 'row_description', 'row_tooltip')
              388  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
              390  STORE_FAST               'row'

 L. 418       392  LOAD_FAST                'row'
              394  YIELD_VALUE      
              396  POP_TOP          
            398_0  COME_FROM           162  '162'

 L. 419       398  LOAD_FAST                'index'
              400  LOAD_CONST               1
              402  INPLACE_ADD      
              404  STORE_FAST               'index'
              406  JUMP_BACK           100  'to 100'
              408  POP_BLOCK        
            410_0  COME_FROM_LOOP       90  '90'

Parse error at or near `COME_FROM' instruction at offset 314_0

    def _on_display_snippet_selected(self, picked_choice, **kwargs):
        resolver = (self.get_resolver)(**kwargs)
        for loot_on_selected in self.display_snippets[picked_choice].loot_on_selected:
            loot_on_selected.apply_to_resolver(resolver)

    def on_choice_selected(self, picked_choice, **kwargs):
        if picked_choice is None:
            if self.run_continuations_on_no_selection:
                for continuation in self.continuations:
                    self.push_tunable_continuation(continuation)

            return
        display_snippet = self.display_snippets[picked_choice].display_snippet
        picked_item_set = {display_snippet.guid64}
        self._on_display_snippet_selected(picked_choice, picked_item_ids=picked_item_set)
        for continuation in self.continuations:
            self.push_tunable_continuation(continuation, picked_item_ids=picked_item_set)
