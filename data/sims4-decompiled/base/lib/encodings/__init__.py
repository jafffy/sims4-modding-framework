# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\encodings\__init__.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 5838 bytes

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
binary_operator ::= BINARY_MODULO . 
break ::= BREAK_LOOP . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_stmt ::= expr . POP_TOP
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
compare ::= compare_chained . 
compare ::= compare_single . 
compare_chained ::= compare_chained37 . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1 ::= expr DUP_TOP ROT_THREE . COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr DUP_TOP ROT_THREE . COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1 ::= expr DUP_TOP ROT_THREE COMPARE_OP . JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr DUP_TOP ROT_THREE COMPARE_OP . JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . 
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 . COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM . POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP . COME_FROM
compare_chained1a_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM . 
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 . POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP ROT_THREE . COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP . POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE . compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2a_37 ::= expr . COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE JUMP_BACK
compare_chained2a_37 ::= expr . COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE JUMP_FORWARD
compare_chained2a_37 ::= expr . COMPARE_OP come_from_opt POP_JUMP_IF_TRUE JUMP_BACK
compare_chained2a_37 ::= expr . COMPARE_OP come_from_opt POP_JUMP_IF_TRUE JUMP_FORWARD
compare_chained2a_37 ::= expr COMPARE_OP . come_from_opt POP_JUMP_IF_TRUE JUMP_BACK
compare_chained2a_37 ::= expr COMPARE_OP . come_from_opt POP_JUMP_IF_TRUE JUMP_FORWARD
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt . POP_JUMP_IF_TRUE JUMP_BACK
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt . POP_JUMP_IF_TRUE JUMP_FORWARD
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE . JUMP_BACK
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE . JUMP_FORWARD
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE JUMP_FORWARD . 
compare_chained2a_false_37 ::= expr . COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE jf_cfs
compare_chained2a_false_37 ::= expr . COMPARE_OP come_from_opt POP_JUMP_IF_FALSE jf_cfs
compare_chained2a_false_37 ::= expr COMPARE_OP . come_from_opt POP_JUMP_IF_FALSE jf_cfs
compare_chained2a_false_37 ::= expr COMPARE_OP \e_come_from_opt . POP_JUMP_IF_FALSE jf_cfs
compare_chained2b_false_37 ::= expr . COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD
compare_chained2b_false_37 ::= expr . COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD COME_FROM
compare_chained2b_false_37 ::= expr . COMPARE_OP come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD
compare_chained2b_false_37 ::= expr . COMPARE_OP come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD COME_FROM
compare_chained2b_false_37 ::= expr COMPARE_OP . come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD
compare_chained2b_false_37 ::= expr COMPARE_OP . come_from_opt POP_JUMP_IF_FALSE JUMP_FORWARD COME_FROM
compare_chained2b_false_37 ::= expr COMPARE_OP \e_come_from_opt . POP_JUMP_IF_FALSE JUMP_FORWARD
compare_chained2b_false_37 ::= expr COMPARE_OP \e_come_from_opt . POP_JUMP_IF_FALSE JUMP_FORWARD COME_FROM
compare_chained2c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE compare_chained2a_false_37
compare_chained2c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE compare_chained2a_false_37 ELSE
compare_chained2c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP come_from_opt POP_JUMP_IF_FALSE compare_chained2a_false_37
compare_chained2c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP come_from_opt POP_JUMP_IF_FALSE compare_chained2a_false_37 ELSE
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37 ::= expr compare_chained1a_37 . 
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
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . 
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY \e_come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_return
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_return
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts END_FINALLY . 
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms END_FINALLY . 
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_stmt ::= except_cond1 . except_suite \e_come_from_opt
except_stmt ::= except_cond1 . except_suite come_from_opt
except_stmt ::= except_cond1 except_suite . come_from_opt
except_stmt ::= except_cond1 except_suite \e_come_from_opt . 
except_stmt ::= except_cond1 except_suite come_from_opt . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= \e_c_stmts_opt POP_EXCEPT . jump_except
except_suite ::= \e_c_stmts_opt POP_EXCEPT . jump_except ELSE
except_suite ::= \e_c_stmts_opt POP_EXCEPT jump_except . 
except_suite ::= \e_c_stmts_opt POP_EXCEPT jump_except . ELSE
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . 
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . ELSE
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jitop ::= expr JUMP_IF_TRUE_OR_POP . 
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
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitec . _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms . 
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms . 
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suitec . COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP . 
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
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitel . _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms . 
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms . 
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suitel . COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP . 
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
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suite . _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms . 
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK else_suite _come_froms . 
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suite . COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP . 
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
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
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
ifelsestmt ::= testexpr \e_c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt jump_forward_else . else_suite _come_froms
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
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
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
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtl ::= testexpr \e_c_stmts_opt jump_forward_else . else_suitec
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
iflaststmt ::= testexpr \e_c_stmts_opt JUMP_FORWARD . 
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
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_except ::= JUMP_BACK . 
jump_except ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lastc_stmt ::= forelselaststmt . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= forelselaststmtl . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr BUILD_LIST_1 . 
list ::= expr expr . BUILD_LIST_2
list ::= expr expr BUILD_LIST_2 . 
lstmt ::= stmt . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= COME_FROM_EXCEPT . 
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jitop . expr COME_FROM
or ::= expr_jitop expr . COME_FROM
or ::= expr_jitop expr COME_FROM . 
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
ret_or ::= expr JUMP_IF_TRUE_OR_POP . return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond . COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM . 
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr ::= ret_or . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
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
starred ::= expr . 
stmt ::= assign . 
stmt ::= break . 
stmt ::= continue . 
stmt ::= for . 
stmt ::= forelsestmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= tryelsestmtl3 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= store_subscript . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
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
testtrue ::= compare_chained37 . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except . 
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler opt_come_from_except . 
try_except36 ::= SETUP_EXCEPT . returns except_handler36 \e_opt_come_from_except
try_except36 ::= SETUP_EXCEPT . returns except_handler36 opt_come_from_except
try_except36 ::= SETUP_EXCEPT . suite_stmts
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 . come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 come_from_opt . 
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite jump_excepts come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suitel come_from_except_clauses
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel . opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
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
   
 L. 133       460  LOAD_FAST                'mod'
                 462  LOAD_ATTR                __name__
                 464  LOAD_FAST                'mod'
                 466  LOAD_ATTR                __file__
                 468  BUILD_TUPLE_2         2 
                 470  BINARY_MODULO    
                 472  CALL_FUNCTION_1       1  '1 positional argument'
                 474  RAISE_VARARGS_1       1  'exception instance'
->             476_0  COME_FROM           452  '452'
               476_1  COME_FROM           438  '438'
               476_2  COME_FROM           424  '424'
import codecs, sys
from . import aliases
_cache = {}
_unknown = '--unknown--'
_import_tail = ['*']
_aliases = aliases.aliases

class CodecRegistryError(LookupError, SystemError):
    pass


def normalize_encoding(encoding):
    if isinstance(encoding, bytes):
        encoding = str(encoding, 'ascii')
    chars = []
    punct = False
    for c in encoding:
        if c.isalnum() or c == '.':
            if punct:
                if chars:
                    chars.append('_')
            chars.append(c)
            punct = False
        else:
            punct = True

    return ''.join(chars)


def search_function--- This code section failed: ---

 L.  74         0  LOAD_GLOBAL              _cache
                2  LOAD_METHOD              get
                4  LOAD_FAST                'encoding'
                6  LOAD_GLOBAL              _unknown
                8  CALL_METHOD_2         2  '2 positional arguments'
               10  STORE_FAST               'entry'

 L.  75        12  LOAD_FAST                'entry'
               14  LOAD_GLOBAL              _unknown
               16  COMPARE_OP               is-not
               18  POP_JUMP_IF_FALSE    24  'to 24'

 L.  76        20  LOAD_FAST                'entry'
               22  RETURN_VALUE     
             24_0  COME_FROM            18  '18'

 L.  85        24  LOAD_GLOBAL              normalize_encoding
               26  LOAD_FAST                'encoding'
               28  CALL_FUNCTION_1       1  '1 positional argument'
               30  STORE_FAST               'norm_encoding'

 L.  86        32  LOAD_GLOBAL              _aliases
               34  LOAD_METHOD              get
               36  LOAD_FAST                'norm_encoding'
               38  CALL_METHOD_1         1  '1 positional argument'
               40  JUMP_IF_TRUE_OR_POP    58  'to 58'

 L.  87        42  LOAD_GLOBAL              _aliases
               44  LOAD_METHOD              get
               46  LOAD_FAST                'norm_encoding'
               48  LOAD_METHOD              replace
               50  LOAD_STR                 '.'
               52  LOAD_STR                 '_'
               54  CALL_METHOD_2         2  '2 positional arguments'
               56  CALL_METHOD_1         1  '1 positional argument'
             58_0  COME_FROM            40  '40'
               58  STORE_FAST               'aliased_encoding'

 L.  88        60  LOAD_FAST                'aliased_encoding'
               62  LOAD_CONST               None
               64  COMPARE_OP               is-not
               66  POP_JUMP_IF_FALSE    78  'to 78'

 L.  89        68  LOAD_FAST                'aliased_encoding'

 L.  90        70  LOAD_FAST                'norm_encoding'
               72  BUILD_LIST_2          2 
               74  STORE_FAST               'modnames'
               76  JUMP_FORWARD         84  'to 84'
             78_0  COME_FROM            66  '66'

 L.  92        78  LOAD_FAST                'norm_encoding'
               80  BUILD_LIST_1          1 
               82  STORE_FAST               'modnames'
             84_0  COME_FROM            76  '76'

 L.  93        84  SETUP_LOOP          162  'to 162'
               86  LOAD_FAST                'modnames'
               88  GET_ITER         
             90_0  COME_FROM            96  '96'
               90  FOR_ITER            156  'to 156'
               92  STORE_FAST               'modname'

 L.  94        94  LOAD_FAST                'modname'
               96  POP_JUMP_IF_FALSE    90  'to 90'
               98  LOAD_STR                 '.'
              100  LOAD_FAST                'modname'
              102  COMPARE_OP               in
              104  POP_JUMP_IF_FALSE   108  'to 108'

 L.  95       106  CONTINUE             90  'to 90'
            108_0  COME_FROM           104  '104'

 L.  96       108  SETUP_EXCEPT        132  'to 132'

 L.  99       110  LOAD_GLOBAL              __import__
              112  LOAD_STR                 'encodings.'
              114  LOAD_FAST                'modname'
              116  BINARY_ADD       
              118  LOAD_GLOBAL              _import_tail

 L. 100       120  LOAD_CONST               0
              122  LOAD_CONST               ('fromlist', 'level')
              124  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              126  STORE_FAST               'mod'
              128  POP_BLOCK        
              130  JUMP_FORWARD        152  'to 152'
            132_0  COME_FROM_EXCEPT    108  '108'

 L. 101       132  DUP_TOP          
              134  LOAD_GLOBAL              ImportError
              136  COMPARE_OP               exception-match
              138  POP_JUMP_IF_FALSE   150  'to 150'
              140  POP_TOP          
              142  POP_TOP          
              144  POP_TOP          

 L. 104       146  POP_EXCEPT       
              148  JUMP_BACK            90  'to 90'
            150_0  COME_FROM           138  '138'
              150  END_FINALLY      
            152_0  COME_FROM           130  '130'

 L. 106       152  BREAK_LOOP       
              154  JUMP_BACK            90  'to 90'
              156  POP_BLOCK        

 L. 108       158  LOAD_CONST               None
              160  STORE_FAST               'mod'
            162_0  COME_FROM_LOOP       84  '84'

 L. 110       162  SETUP_EXCEPT        174  'to 174'

 L. 111       164  LOAD_FAST                'mod'
              166  LOAD_ATTR                getregentry
              168  STORE_FAST               'getregentry'
              170  POP_BLOCK        
              172  JUMP_FORWARD        198  'to 198'
            174_0  COME_FROM_EXCEPT    162  '162'

 L. 112       174  DUP_TOP          
              176  LOAD_GLOBAL              AttributeError
              178  COMPARE_OP               exception-match
              180  POP_JUMP_IF_FALSE   196  'to 196'
              182  POP_TOP          
              184  POP_TOP          
              186  POP_TOP          

 L. 114       188  LOAD_CONST               None
              190  STORE_FAST               'mod'
              192  POP_EXCEPT       
              194  JUMP_FORWARD        198  'to 198'
            196_0  COME_FROM           180  '180'
              196  END_FINALLY      
            198_0  COME_FROM           194  '194'
            198_1  COME_FROM           172  '172'

 L. 116       198  LOAD_FAST                'mod'
              200  LOAD_CONST               None
              202  COMPARE_OP               is
              204  POP_JUMP_IF_FALSE   218  'to 218'

 L. 118       206  LOAD_CONST               None
              208  LOAD_GLOBAL              _cache
              210  LOAD_FAST                'encoding'
              212  STORE_SUBSCR     

 L. 119       214  LOAD_CONST               None
              216  RETURN_VALUE     
            218_0  COME_FROM           204  '204'

 L. 122       218  LOAD_FAST                'getregentry'
              220  CALL_FUNCTION_0       0  '0 positional arguments'
              222  STORE_FAST               'entry'

 L. 123       224  LOAD_GLOBAL              isinstance
              226  LOAD_FAST                'entry'
              228  LOAD_GLOBAL              codecs
              230  LOAD_ATTR                CodecInfo
              232  CALL_FUNCTION_2       2  '2 positional arguments'
          234_236  POP_JUMP_IF_TRUE    554  'to 554'

 L. 124       238  LOAD_CONST               4
              240  LOAD_GLOBAL              len
              242  LOAD_FAST                'entry'
              244  CALL_FUNCTION_1       1  '1 positional argument'
              246  DUP_TOP          
              248  ROT_THREE        
              250  COMPARE_OP               <=
          252_254  POP_JUMP_IF_FALSE   266  'to 266'
              256  LOAD_CONST               7
              258  COMPARE_OP               <=
          260_262  POP_JUMP_IF_TRUE    288  'to 288'
              264  JUMP_FORWARD        268  'to 268'
            266_0  COME_FROM           252  '252'
              266  POP_TOP          
            268_0  COME_FROM           264  '264'

 L. 125       268  LOAD_GLOBAL              CodecRegistryError
              270  LOAD_STR                 'module "%s" (%s) failed to register'

 L. 126       272  LOAD_FAST                'mod'
              274  LOAD_ATTR                __name__
              276  LOAD_FAST                'mod'
              278  LOAD_ATTR                __file__
              280  BUILD_TUPLE_2         2 
              282  BINARY_MODULO    
              284  CALL_FUNCTION_1       1  '1 positional argument'
              286  RAISE_VARARGS_1       1  'exception instance'
            288_0  COME_FROM           260  '260'

 L. 127       288  LOAD_GLOBAL              callable
              290  LOAD_FAST                'entry'
              292  LOAD_CONST               0
              294  BINARY_SUBSCR    
              296  CALL_FUNCTION_1       1  '1 positional argument'
          298_300  POP_JUMP_IF_FALSE   456  'to 456'
              302  LOAD_GLOBAL              callable
              304  LOAD_FAST                'entry'
              306  LOAD_CONST               1
              308  BINARY_SUBSCR    
              310  CALL_FUNCTION_1       1  '1 positional argument'
          312_314  POP_JUMP_IF_FALSE   456  'to 456'

 L. 128       316  LOAD_FAST                'entry'
              318  LOAD_CONST               2
              320  BINARY_SUBSCR    
              322  LOAD_CONST               None
              324  COMPARE_OP               is-not
          326_328  POP_JUMP_IF_FALSE   344  'to 344'
              330  LOAD_GLOBAL              callable
              332  LOAD_FAST                'entry'
              334  LOAD_CONST               2
              336  BINARY_SUBSCR    
              338  CALL_FUNCTION_1       1  '1 positional argument'
          340_342  POP_JUMP_IF_FALSE   456  'to 456'
            344_0  COME_FROM           326  '326'

 L. 129       344  LOAD_FAST                'entry'
              346  LOAD_CONST               3
              348  BINARY_SUBSCR    
              350  LOAD_CONST               None
              352  COMPARE_OP               is-not
          354_356  POP_JUMP_IF_FALSE   372  'to 372'
              358  LOAD_GLOBAL              callable
              360  LOAD_FAST                'entry'
              362  LOAD_CONST               3
              364  BINARY_SUBSCR    
              366  CALL_FUNCTION_1       1  '1 positional argument'
          368_370  POP_JUMP_IF_FALSE   456  'to 456'
            372_0  COME_FROM           354  '354'

 L. 130       372  LOAD_GLOBAL              len
              374  LOAD_FAST                'entry'
              376  CALL_FUNCTION_1       1  '1 positional argument'
              378  LOAD_CONST               4
              380  COMPARE_OP               >
          382_384  POP_JUMP_IF_FALSE   414  'to 414'
              386  LOAD_FAST                'entry'
              388  LOAD_CONST               4
              390  BINARY_SUBSCR    
              392  LOAD_CONST               None
              394  COMPARE_OP               is-not
          396_398  POP_JUMP_IF_FALSE   414  'to 414'
              400  LOAD_GLOBAL              callable
              402  LOAD_FAST                'entry'
              404  LOAD_CONST               4
              406  BINARY_SUBSCR    
              408  CALL_FUNCTION_1       1  '1 positional argument'
          410_412  POP_JUMP_IF_FALSE   456  'to 456'
            414_0  COME_FROM           396  '396'
            414_1  COME_FROM           382  '382'

 L. 131       414  LOAD_GLOBAL              len
              416  LOAD_FAST                'entry'
              418  CALL_FUNCTION_1       1  '1 positional argument'
              420  LOAD_CONST               5
              422  COMPARE_OP               >
          424_426  POP_JUMP_IF_FALSE   476  'to 476'
              428  LOAD_FAST                'entry'
              430  LOAD_CONST               5
              432  BINARY_SUBSCR    
              434  LOAD_CONST               None
              436  COMPARE_OP               is-not
          438_440  POP_JUMP_IF_FALSE   476  'to 476'
              442  LOAD_GLOBAL              callable
              444  LOAD_FAST                'entry'
              446  LOAD_CONST               5
              448  BINARY_SUBSCR    
              450  CALL_FUNCTION_1       1  '1 positional argument'
          452_454  POP_JUMP_IF_TRUE    476  'to 476'
            456_0  COME_FROM           410  '410'
            456_1  COME_FROM           368  '368'
            456_2  COME_FROM           340  '340'
            456_3  COME_FROM           312  '312'
            456_4  COME_FROM           298  '298'

 L. 132       456  LOAD_GLOBAL              CodecRegistryError
              458  LOAD_STR                 'incompatible codecs in module "%s" (%s)'

 L. 133       460  LOAD_FAST                'mod'
              462  LOAD_ATTR                __name__
              464  LOAD_FAST                'mod'
              466  LOAD_ATTR                __file__
              468  BUILD_TUPLE_2         2 
              470  BINARY_MODULO    
              472  CALL_FUNCTION_1       1  '1 positional argument'
              474  RAISE_VARARGS_1       1  'exception instance'
            476_0  COME_FROM           452  '452'
            476_1  COME_FROM           438  '438'
            476_2  COME_FROM           424  '424'

 L. 134       476  LOAD_GLOBAL              len
              478  LOAD_FAST                'entry'
              480  CALL_FUNCTION_1       1  '1 positional argument'
              482  LOAD_CONST               7
              484  COMPARE_OP               <
          486_488  POP_JUMP_IF_TRUE    504  'to 504'
              490  LOAD_FAST                'entry'
              492  LOAD_CONST               6
              494  BINARY_SUBSCR    
              496  LOAD_CONST               None
              498  COMPARE_OP               is
          500_502  POP_JUMP_IF_FALSE   544  'to 544'
            504_0  COME_FROM           486  '486'

 L. 135       504  LOAD_FAST                'entry'
              506  LOAD_CONST               (None,)
              508  LOAD_CONST               6
              510  LOAD_GLOBAL              len
              512  LOAD_FAST                'entry'
              514  CALL_FUNCTION_1       1  '1 positional argument'
              516  BINARY_SUBTRACT  
              518  BINARY_MULTIPLY  
              520  LOAD_FAST                'mod'
              522  LOAD_ATTR                __name__
              524  LOAD_METHOD              split
              526  LOAD_STR                 '.'
              528  LOAD_CONST               1
              530  CALL_METHOD_2         2  '2 positional arguments'
              532  LOAD_CONST               1
              534  BINARY_SUBSCR    
              536  BUILD_TUPLE_1         1 
              538  BINARY_ADD       
              540  INPLACE_ADD      
              542  STORE_FAST               'entry'
            544_0  COME_FROM           500  '500'

 L. 136       544  LOAD_GLOBAL              codecs
              546  LOAD_ATTR                CodecInfo
              548  LOAD_FAST                'entry'
              550  CALL_FUNCTION_EX      0  'positional arguments only'
              552  STORE_FAST               'entry'
            554_0  COME_FROM           234  '234'

 L. 139       554  LOAD_FAST                'entry'
              556  LOAD_GLOBAL              _cache
              558  LOAD_FAST                'encoding'
              560  STORE_SUBSCR     

 L. 143       562  SETUP_EXCEPT        576  'to 576'

 L. 144       564  LOAD_FAST                'mod'
              566  LOAD_METHOD              getaliases
              568  CALL_METHOD_0         0  '0 positional arguments'
              570  STORE_FAST               'codecaliases'
              572  POP_BLOCK        
              574  JUMP_FORWARD        598  'to 598'
            576_0  COME_FROM_EXCEPT    562  '562'

 L. 145       576  DUP_TOP          
              578  LOAD_GLOBAL              AttributeError
              580  COMPARE_OP               exception-match
          582_584  POP_JUMP_IF_FALSE   596  'to 596'
              586  POP_TOP          
              588  POP_TOP          
              590  POP_TOP          

 L. 146       592  POP_EXCEPT       
              594  JUMP_FORWARD        632  'to 632'
            596_0  COME_FROM           582  '582'
              596  END_FINALLY      
            598_0  COME_FROM           574  '574'

 L. 148       598  SETUP_LOOP          632  'to 632'
              600  LOAD_FAST                'codecaliases'
              602  GET_ITER         
            604_0  COME_FROM           614  '614'
              604  FOR_ITER            630  'to 630'
              606  STORE_FAST               'alias'

 L. 149       608  LOAD_FAST                'alias'
              610  LOAD_GLOBAL              _aliases
              612  COMPARE_OP               not-in
          614_616  POP_JUMP_IF_FALSE   604  'to 604'

 L. 150       618  LOAD_FAST                'modname'
              620  LOAD_GLOBAL              _aliases
              622  LOAD_FAST                'alias'
              624  STORE_SUBSCR     
          626_628  JUMP_BACK           604  'to 604'
              630  POP_BLOCK        
            632_0  COME_FROM_LOOP      598  '598'
            632_1  COME_FROM           594  '594'

 L. 153       632  LOAD_FAST                'entry'
              634  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 476_0


codecs.register(search_function)
if sys.platform == 'win32':

    def _alias_mbcs(encoding):
        try:
            import _winapi
            ansi_code_page = 'cp%s' % _winapi.GetACP()
            if encoding == ansi_code_page:
                import encodings.mbcs
                return encodings.mbcs.getregentry()
        except ImportError:
            pass


    codecs.register(_alias_mbcs)
