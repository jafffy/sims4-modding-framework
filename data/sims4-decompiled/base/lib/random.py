# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\random.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 28259 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
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
assign2 ::= expr expr ROT_TWO . store store
assign2 ::= expr expr ROT_TWO store . store
assign2 ::= expr expr ROT_TWO store store . 
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
binary_operator ::= BINARY_MULTIPLY . 
binary_operator ::= BINARY_SUBTRACT . 
binary_operator ::= BINARY_TRUE_DIVIDE . 
break ::= BREAK_LOOP . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
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
compare_chained2a_37 ::= expr COMPARE_OP \e_come_from_opt POP_JUMP_IF_TRUE JUMP_BACK . 
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
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
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
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt COME_FROM . POP_EXCEPT jump_except COME_FROM
except_suite ::= returns . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= if_exp . 
expr ::= list . 
expr ::= list_comp . 
expr ::= or . 
expr ::= subscript . 
expr ::= unary_op . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_or_arg ::= LOAD_ARG . 
expr_or_arg ::= expr . 
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
for_iter ::= \e__come_froms . FOR_ITER
for_iter ::= \e__come_froms FOR_ITER . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
get_iter ::= expr . GET_ITER
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
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt jb_else . else_suitel
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
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jb_or_c ::= JUMP_BACK . 
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
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
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts ::= returns . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
lc_body ::= expr LIST_APPEND . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list_comp ::= BUILD_LIST_0 . list_iter
list_comp ::= BUILD_LIST_0 list_iter . 
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c _come_froms
list_for ::= expr_or_arg for_iter . store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg for_iter . store list_iter jb_or_c _come_froms
list_for ::= expr_or_arg for_iter store . list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg for_iter store . list_iter jb_or_c _come_froms
list_for ::= expr_or_arg for_iter store list_iter . jb_or_c \e__come_froms
list_for ::= expr_or_arg for_iter store list_iter . jb_or_c _come_froms
list_for ::= expr_or_arg for_iter store list_iter jb_or_c . _come_froms
list_for ::= expr_or_arg for_iter store list_iter jb_or_c \e__come_froms . 
list_if ::= expr . jmp_false list_iter
list_if ::= expr . jmp_false list_iter COME_FROM
list_if ::= expr . jmp_false37 list_iter
list_if_not ::= expr . jmp_true list_iter
list_if_not ::= expr . jmp_true list_iter COME_FROM
list_iter ::= lc_body . 
list_iter ::= list_for . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_3
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_3
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
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
setup_loop ::= SETUP_LOOP _come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= assign2 . 
stmt ::= break . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= tryelsestmtl3 . 
stmt ::= while1stmt . 
stmt ::= whileTruestmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
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
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except . 
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr expr BUILD_TUPLE_5
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr expr BUILD_TUPLE_5
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr expr BUILD_TUPLE_5
tuple ::= expr expr expr expr . expr BUILD_TUPLE_5
tuple ::= expr expr expr expr expr . BUILD_TUPLE_5
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unary_op ::= expr unary_operator . 
unary_operator ::= UNARY_NEGATIVE . 
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK POP_BLOCK . else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK \e__come_froms . POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK \e__come_froms POP_BLOCK . else_suitel COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts COME_FROM_LOOP . 
while1stmt ::= setup_loop l_stmts COME_FROM_LOOP . JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts POP_BLOCK . COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts POP_BLOCK COME_FROM_LOOP . 
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK POP_BLOCK . _come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms . 
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK POP_BLOCK _come_froms . 
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
-> 
 L. 536       100  CONTINUE             72  'to 72'
               102_0  COME_FROM            94  '94'
from warnings import warn as _warn
from types import MethodType as _MethodType, BuiltinMethodType as _BuiltinMethodType
from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil
from math import sqrt as _sqrt, acos as _acos, cos as _cos, sin as _sin
from os import urandom as _urandom
from _collections_abc import Set as _Set, Sequence as _Sequence
from hashlib import sha512 as _sha512
import itertools as _itertools, bisect as _bisect, os as _os
__all__ = [
 "'Random'", "'seed'", "'random'", "'uniform'", "'randint'", "'choice'", "'sample'", 
 "'randrange'", 
 "'shuffle'", "'normalvariate'", "'lognormvariate'", 
 "'expovariate'", "'vonmisesvariate'", 
 "'gammavariate'", "'triangular'", 
 "'gauss'", "'betavariate'", "'paretovariate'", 
 "'weibullvariate'", 
 "'getstate'", "'setstate'", "'getrandbits'", "'choices'", 
 "'SystemRandom'"]
NV_MAGICCONST = 4 * _exp(-0.5) / _sqrt(2.0)
TWOPI = 2.0 * _pi
LOG4 = _log(4.0)
SG_MAGICCONST = 1.0 + _log(4.5)
BPF = 53
RECIP_BPF = 2 ** (-BPF)
import _random

class Random(_random.Random):
    VERSION = 3

    def __init__(self, x=None):
        self.seed(x)
        self.gauss_next = None

    def seed(self, a=None, version=2):
        if version == 1:
            if isinstance(a, (str, bytes)):
                a = a.decode('latin-1') if isinstance(a, bytes) else a
                x = ord(a[0]) << 7 if a else 0
                for c in map(ord, a):
                    x = (1000003 * x ^ c) & 18446744073709551615

                x ^= len(a)
                a = -2 if x == -1 else x
        elif version == 2 and isinstance(a, (str, bytes, bytearray)):
            if isinstance(a, str):
                a = a.encode()
            a += _sha512(a).digest()
            a = int.from_bytes(a, 'big')
        super().seed(a)
        self.gauss_next = None

    def getstate(self):
        return (
         self.VERSION, super().getstate(), self.gauss_next)

    def setstate(self, state):
        version = state[0]
        if version == 3:
            version, internalstate, self.gauss_next = state
            super().setstate(internalstate)
        else:
            if version == 2:
                version, internalstate, self.gauss_next = state
                try:
                    internalstate = tuple((x % 4294967296 for x in internalstate))
                except ValueError as e:
                    try:
                        raise TypeError from e
                    finally:
                        e = None
                        del e

                super().setstate(internalstate)
            else:
                raise ValueError('state with version %s passed to Random.setstate() of version %s' % (
                 version, self.VERSION))

    def __getstate__(self):
        return self.getstate()

    def __setstate__(self, state):
        self.setstate(state)

    def __reduce__(self):
        return (
         self.__class__, (), self.getstate())

    def randrange(self, start, stop=None, step=1, _int=int):
        istart = _int(start)
        if istart != start:
            raise ValueError('non-integer arg 1 for randrange()')
        if stop is None:
            if istart > 0:
                return self._randbelow(istart)
            raise ValueError('empty range for randrange()')
        istop = _int(stop)
        if istop != stop:
            raise ValueError('non-integer stop for randrange()')
        else:
            width = istop - istart
            if step == 1:
                if width > 0:
                    return istart + self._randbelow(width)
            else:
                if step == 1:
                    raise ValueError('empty range for randrange() (%d,%d, %d)' % (istart, istop, width))
                istep = _int(step)
                if istep != step:
                    raise ValueError('non-integer step for randrange()')
                if istep > 0:
                    n = (width + istep - 1) // istep
                else:
                    if istep < 0:
                        n = (width + istep + 1) // istep
                    else:
                        raise ValueError('zero step for randrange()')
        if n <= 0:
            raise ValueError('empty range for randrange()')
        return istart + istep * self._randbelow(n)

    def randint(self, a, b):
        return self.randrange(a, b + 1)

    def _randbelow(self, n, int=int, maxsize=1 << BPF, type=type, Method=_MethodType, BuiltinMethod=_BuiltinMethodType):
        random = self.random
        getrandbits = self.getrandbits
        if type(random) is BuiltinMethod or type(getrandbits) is Method:
            k = n.bit_length()
            r = getrandbits(k)
            while r >= n:
                r = getrandbits(k)

            return r
        if n >= maxsize:
            _warn('Underlying random() generator does not supply \nenough bits to choose from a population range this large.\nTo remove the range limitation, add a getrandbits() method.')
            return int(random() * n)
        if n == 0:
            raise ValueError('Boundary cannot be zero')
        rem = maxsize % n
        limit = (maxsize - rem) / maxsize
        r = random()
        while r >= limit:
            r = random()

        return int(r * maxsize) % n

    def choice(self, seq):
        try:
            i = self._randbelow(len(seq))
        except ValueError:
            raise IndexError('Cannot choose from an empty sequence') from None

        return seq[i]

    def shuffle(self, x, random=None):
        if random is None:
            randbelow = self._randbelow
            for i in reversed(range(1, len(x))):
                j = randbelow(i + 1)
                x[i], x[j] = x[j], x[i]

        else:
            _int = int
            for i in reversed(range(1, len(x))):
                j = _int(random() * (i + 1))
                x[i], x[j] = x[j], x[i]

    def sample(self, population, k):
        if isinstance(population, _Set):
            population = tuple(population)
        if not isinstance(population, _Sequence):
            raise TypeError('Population must be a sequence or set.  For dicts, use list(d).')
        randbelow = self._randbelow
        n = len(population)
        if not 0 <= k <= n:
            raise ValueError('Sample larger than population or is negative')
        result = [
         None] * k
        setsize = 21
        if k > 5:
            setsize += 4 ** _ceil(_log(k * 3, 4))
        if n <= setsize:
            pool = list(population)
            for i in range(k):
                j = randbelow(n - i)
                result[i] = pool[j]
                pool[j] = pool[n - i - 1]

        else:
            selected = set()
            selected_add = selected.add
            for i in range(k):
                j = randbelow(n)
                while j in selected:
                    j = randbelow(n)

                selected_add(j)
                result[i] = population[j]

        return result

    def choices(self, population, weights=None, *, cum_weights=None, k=1):
        random = self.random
        if cum_weights is None:
            if weights is None:
                _int = int
                total = len(population)
                return [population[_int(random() * total)] for i in range(k)]
            cum_weights = list(_itertools.accumulate(weights))
        else:
            if weights is not None:
                raise TypeError('Cannot specify both weights and cumulative weights')
        if len(cum_weights) != len(population):
            raise ValueError('The number of weights does not match the population')
        bisect = _bisect.bisect
        total = cum_weights[-1]
        return [population[bisect(cum_weights, random() * total)] for i in range(k)]

    def uniform(self, a, b):
        return a + (b - a) * self.random()

    def triangular(self, low=0.0, high=1.0, mode=None):
        u = self.random()
        try:
            c = 0.5 if mode is None else (mode - low) / (high - low)
        except ZeroDivisionError:
            return low
        else:
            if u > c:
                u = 1.0 - u
                c = 1.0 - c
                low, high = high, low
            return low + (high - low) * _sqrt(u * c)

    def normalvariate(self, mu, sigma):
        random = self.random
        while 1:
            u1 = random()
            u2 = 1.0 - random()
            z = NV_MAGICCONST * (u1 - 0.5) / u2
            zz = z * z / 4.0
            if zz <= -_log(u2):
                break

        return mu + z * sigma

    def lognormvariate(self, mu, sigma):
        return _exp(self.normalvariate(mu, sigma))

    def expovariate(self, lambd):
        return -_log(1.0 - self.random()) / lambd

    def vonmisesvariate(self, mu, kappa):
        random = self.random
        if kappa <= 1e-06:
            return TWOPI * random()
        else:
            s = 0.5 / kappa
            r = s + _sqrt(1.0 + s * s)
            while 1:
                u1 = random()
                z = _cos(_pi * u1)
                d = z / (r + z)
                u2 = random()
                if u2 < 1.0 - d * d or u2 <= (1.0 - d) * _exp(d):
                    break

            q = 1.0 / r
            f = (q + z) / (1.0 + q * z)
            u3 = random()
            if u3 > 0.5:
                theta = (mu + _acos(f)) % TWOPI
            else:
                theta = (mu - _acos(f)) % TWOPI
        return theta

    def gammavariate--- This code section failed: ---

 L. 519         0  LOAD_FAST                'alpha'
                2  LOAD_CONST               0.0
                4  COMPARE_OP               <=
                6  POP_JUMP_IF_TRUE     16  'to 16'
                8  LOAD_FAST                'beta'
               10  LOAD_CONST               0.0
               12  COMPARE_OP               <=
               14  POP_JUMP_IF_FALSE    24  'to 24'
             16_0  COME_FROM             6  '6'

 L. 520        16  LOAD_GLOBAL              ValueError
               18  LOAD_STR                 'gammavariate: alpha and beta must be > 0.0'
               20  CALL_FUNCTION_1       1  '1 positional argument'
               22  RAISE_VARARGS_1       1  'exception instance'
             24_0  COME_FROM            14  '14'

 L. 522        24  LOAD_FAST                'self'
               26  LOAD_ATTR                random
               28  STORE_FAST               'random'

 L. 523        30  LOAD_FAST                'alpha'
               32  LOAD_CONST               1.0
               34  COMPARE_OP               >
               36  POP_JUMP_IF_FALSE   218  'to 218'

 L. 529        38  LOAD_GLOBAL              _sqrt
               40  LOAD_CONST               2.0
               42  LOAD_FAST                'alpha'
               44  BINARY_MULTIPLY  
               46  LOAD_CONST               1.0
               48  BINARY_SUBTRACT  
               50  CALL_FUNCTION_1       1  '1 positional argument'
               52  STORE_FAST               'ainv'

 L. 530        54  LOAD_FAST                'alpha'
               56  LOAD_GLOBAL              LOG4
               58  BINARY_SUBTRACT  
               60  STORE_FAST               'bbb'

 L. 531        62  LOAD_FAST                'alpha'
               64  LOAD_FAST                'ainv'
               66  BINARY_ADD       
               68  STORE_FAST               'ccc'

 L. 533        70  SETUP_LOOP          216  'to 216'
             72_0  COME_FROM           202  '202'

 L. 534        72  LOAD_FAST                'random'
               74  CALL_FUNCTION_0       0  '0 positional arguments'
               76  STORE_FAST               'u1'

 L. 535        78  LOAD_CONST               1e-07
               80  LOAD_FAST                'u1'
               82  DUP_TOP          
               84  ROT_THREE        
               86  COMPARE_OP               <
               88  POP_JUMP_IF_FALSE    98  'to 98'
               90  LOAD_CONST               0.9999999
               92  COMPARE_OP               <
               94  POP_JUMP_IF_TRUE    102  'to 102'
               96  JUMP_BACK            72  'to 72'
             98_0  COME_FROM            88  '88'
               98  POP_TOP          

 L. 536       100  CONTINUE             72  'to 72'
            102_0  COME_FROM            94  '94'

 L. 537       102  LOAD_CONST               1.0
              104  LOAD_FAST                'random'
              106  CALL_FUNCTION_0       0  '0 positional arguments'
              108  BINARY_SUBTRACT  
              110  STORE_FAST               'u2'

 L. 538       112  LOAD_GLOBAL              _log
              114  LOAD_FAST                'u1'
              116  LOAD_CONST               1.0
              118  LOAD_FAST                'u1'
              120  BINARY_SUBTRACT  
              122  BINARY_TRUE_DIVIDE
              124  CALL_FUNCTION_1       1  '1 positional argument'
              126  LOAD_FAST                'ainv'
              128  BINARY_TRUE_DIVIDE
              130  STORE_FAST               'v'

 L. 539       132  LOAD_FAST                'alpha'
              134  LOAD_GLOBAL              _exp
              136  LOAD_FAST                'v'
              138  CALL_FUNCTION_1       1  '1 positional argument'
              140  BINARY_MULTIPLY  
              142  STORE_FAST               'x'

 L. 540       144  LOAD_FAST                'u1'
              146  LOAD_FAST                'u1'
              148  BINARY_MULTIPLY  
              150  LOAD_FAST                'u2'
              152  BINARY_MULTIPLY  
              154  STORE_FAST               'z'

 L. 541       156  LOAD_FAST                'bbb'
              158  LOAD_FAST                'ccc'
              160  LOAD_FAST                'v'
              162  BINARY_MULTIPLY  
              164  BINARY_ADD       
              166  LOAD_FAST                'x'
              168  BINARY_SUBTRACT  
              170  STORE_FAST               'r'

 L. 542       172  LOAD_FAST                'r'
              174  LOAD_GLOBAL              SG_MAGICCONST
              176  BINARY_ADD       
              178  LOAD_CONST               4.5
              180  LOAD_FAST                'z'
              182  BINARY_MULTIPLY  
              184  BINARY_SUBTRACT  
              186  LOAD_CONST               0.0
              188  COMPARE_OP               >=
              190  POP_JUMP_IF_TRUE    204  'to 204'
              192  LOAD_FAST                'r'
              194  LOAD_GLOBAL              _log
              196  LOAD_FAST                'z'
              198  CALL_FUNCTION_1       1  '1 positional argument'
              200  COMPARE_OP               >=
              202  POP_JUMP_IF_FALSE    72  'to 72'
            204_0  COME_FROM           190  '190'

 L. 543       204  LOAD_FAST                'x'
              206  LOAD_FAST                'beta'
              208  BINARY_MULTIPLY  
              210  RETURN_VALUE     
              212  JUMP_BACK            72  'to 72'
              214  POP_BLOCK        
            216_0  COME_FROM_LOOP       70  '70'
              216  JUMP_FORWARD        408  'to 408'
            218_0  COME_FROM            36  '36'

 L. 545       218  LOAD_FAST                'alpha'
              220  LOAD_CONST               1.0
              222  COMPARE_OP               ==
          224_226  POP_JUMP_IF_FALSE   268  'to 268'

 L. 547       228  LOAD_FAST                'random'
              230  CALL_FUNCTION_0       0  '0 positional arguments'
              232  STORE_FAST               'u'

 L. 548       234  SETUP_LOOP          254  'to 254'
              236  LOAD_FAST                'u'
              238  LOAD_CONST               1e-07
              240  COMPARE_OP               <=
              242  POP_JUMP_IF_FALSE   252  'to 252'

 L. 549       244  LOAD_FAST                'random'
              246  CALL_FUNCTION_0       0  '0 positional arguments'
              248  STORE_FAST               'u'
              250  JUMP_BACK           236  'to 236'
            252_0  COME_FROM           242  '242'
              252  POP_BLOCK        
            254_0  COME_FROM_LOOP      234  '234'

 L. 550       254  LOAD_GLOBAL              _log
              256  LOAD_FAST                'u'
              258  CALL_FUNCTION_1       1  '1 positional argument'
              260  UNARY_NEGATIVE   
              262  LOAD_FAST                'beta'
              264  BINARY_MULTIPLY  
              266  RETURN_VALUE     
            268_0  COME_FROM           224  '224'

 L. 556       268  SETUP_LOOP          400  'to 400'
            270_0  COME_FROM           388  '388'

 L. 557       270  LOAD_FAST                'random'
              272  CALL_FUNCTION_0       0  '0 positional arguments'
              274  STORE_FAST               'u'

 L. 558       276  LOAD_GLOBAL              _e
              278  LOAD_FAST                'alpha'
              280  BINARY_ADD       
              282  LOAD_GLOBAL              _e
              284  BINARY_TRUE_DIVIDE
              286  STORE_FAST               'b'

 L. 559       288  LOAD_FAST                'b'
              290  LOAD_FAST                'u'
              292  BINARY_MULTIPLY  
              294  STORE_FAST               'p'

 L. 560       296  LOAD_FAST                'p'
              298  LOAD_CONST               1.0
              300  COMPARE_OP               <=
          302_304  POP_JUMP_IF_FALSE   320  'to 320'

 L. 561       306  LOAD_FAST                'p'
              308  LOAD_CONST               1.0
              310  LOAD_FAST                'alpha'
              312  BINARY_TRUE_DIVIDE
              314  BINARY_POWER     
              316  STORE_FAST               'x'
              318  JUMP_FORWARD        338  'to 338'
            320_0  COME_FROM           302  '302'

 L. 563       320  LOAD_GLOBAL              _log
              322  LOAD_FAST                'b'
              324  LOAD_FAST                'p'
              326  BINARY_SUBTRACT  
              328  LOAD_FAST                'alpha'
              330  BINARY_TRUE_DIVIDE
              332  CALL_FUNCTION_1       1  '1 positional argument'
              334  UNARY_NEGATIVE   
              336  STORE_FAST               'x'
            338_0  COME_FROM           318  '318'

 L. 564       338  LOAD_FAST                'random'
              340  CALL_FUNCTION_0       0  '0 positional arguments'
              342  STORE_FAST               'u1'

 L. 565       344  LOAD_FAST                'p'
              346  LOAD_CONST               1.0
              348  COMPARE_OP               >
          350_352  POP_JUMP_IF_FALSE   376  'to 376'

 L. 566       354  LOAD_FAST                'u1'
              356  LOAD_FAST                'x'
              358  LOAD_FAST                'alpha'
              360  LOAD_CONST               1.0
              362  BINARY_SUBTRACT  
              364  BINARY_POWER     
              366  COMPARE_OP               <=
          368_370  POP_JUMP_IF_FALSE   394  'to 394'

 L. 567       372  BREAK_LOOP       
              374  JUMP_BACK           270  'to 270'
            376_0  COME_FROM           350  '350'

 L. 568       376  LOAD_FAST                'u1'
              378  LOAD_GLOBAL              _exp
              380  LOAD_FAST                'x'
              382  UNARY_NEGATIVE   
              384  CALL_FUNCTION_1       1  '1 positional argument'
              386  COMPARE_OP               <=
          388_390  POP_JUMP_IF_FALSE   270  'to 270'

 L. 569       392  BREAK_LOOP       
            394_0  COME_FROM           368  '368'
          394_396  JUMP_BACK           270  'to 270'
              398  POP_BLOCK        
            400_0  COME_FROM_LOOP      268  '268'

 L. 570       400  LOAD_FAST                'x'
              402  LOAD_FAST                'beta'
              404  BINARY_MULTIPLY  
              406  RETURN_VALUE     
            408_0  COME_FROM           216  '216'

Parse error at or near `CONTINUE' instruction at offset 100

    def gauss(self, mu, sigma):
        random = self.random
        z = self.gauss_next
        self.gauss_next = None
        if z is None:
            x2pi = random() * TWOPI
            g2rad = _sqrt(-2.0 * _log(1.0 - random()))
            z = _cos(x2pi) * g2rad
            self.gauss_next = _sin(x2pi) * g2rad
        return mu + z * sigma

    def betavariate(self, alpha, beta):
        y = self.gammavariate(alpha, 1.0)
        if y == 0:
            return 0.0
        return y / (y + self.gammavariate(beta, 1.0))

    def paretovariate(self, alpha):
        u = 1.0 - self.random()
        return 1.0 / u ** (1.0 / alpha)

    def weibullvariate(self, alpha, beta):
        u = 1.0 - self.random()
        return alpha * (-_log(u)) ** (1.0 / beta)


class SystemRandom(Random):

    def random(self):
        return (int.from_bytes(_urandom(7), 'big') >> 3) * RECIP_BPF

    def getrandbits(self, k):
        if k <= 0:
            raise ValueError('number of bits must be greater than zero')
        if k != int(k):
            raise TypeError('number of bits should be an integer')
        numbytes = (k + 7) // 8
        x = int.from_bytes(_urandom(numbytes), 'big')
        return x >> numbytes * 8 - k

    def seed(self, *args, **kwds):
        pass

    def _notimplemented(self, *args, **kwds):
        raise NotImplementedError('System entropy source does not have state.')

    getstate = setstate = _notimplemented


def _test_generator(n, func, args):
    import time
    print(n, 'times', func.__name__)
    total = 0.0
    sqsum = 0.0
    smallest = 10000000000.0
    largest = -10000000000.0
    t0 = time.time()
    for i in range(n):
        x = func(*args)
        total += x
        sqsum = sqsum + x * x
        smallest = min(x, smallest)
        largest = max(x, largest)

    t1 = time.time()
    print((round(t1 - t0, 3)), 'sec,', end=' ')
    avg = total / n
    stddev = _sqrt(sqsum / n - avg * avg)
    print('avg %g, stddev %g, min %g, max %g\n' % (
     avg, stddev, smallest, largest))


def _test(N=2000):
    _test_generator(N, random, ())
    _test_generator(N, normalvariate, (0.0, 1.0))
    _test_generator(N, lognormvariate, (0.0, 1.0))
    _test_generator(N, vonmisesvariate, (0.0, 1.0))
    _test_generator(N, gammavariate, (0.01, 1.0))
    _test_generator(N, gammavariate, (0.1, 1.0))
    _test_generator(N, gammavariate, (0.1, 2.0))
    _test_generator(N, gammavariate, (0.5, 1.0))
    _test_generator(N, gammavariate, (0.9, 1.0))
    _test_generator(N, gammavariate, (1.0, 1.0))
    _test_generator(N, gammavariate, (2.0, 1.0))
    _test_generator(N, gammavariate, (20.0, 1.0))
    _test_generator(N, gammavariate, (200.0, 1.0))
    _test_generator(N, gauss, (0.0, 1.0))
    _test_generator(N, betavariate, (3.0, 3.0))
    _test_generator(N, triangular, (0.0, 1.0, 0.3333333333333333))


_inst = Random()
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
choices = _inst.choices
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
getrandbits = _inst.getrandbits
if hasattr(_os, 'fork'):
    _os.register_at_fork(after_in_child=(_inst.seed))
if __name__ == '__main__':
    _test()
