# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\sim_info_tests.py
# Compiled at: 2022-05-18 13:20:03
# Size of source mod 2**32: 85238 bytes

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
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
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
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
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
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_5
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6 . 
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8 . 
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_9
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
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST BUILD_CONST_KEY_MAP_2 . 
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3 . 
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_7
dict ::= expr expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_9
dict ::= kvlist_1 . 
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= _lambda_body . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= list . 
expr ::= list_comp . 
expr ::= listcomp . 
expr ::= or . 
expr ::= set . 
expr ::= subscript . 
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
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
for_iter ::= \e__come_froms . FOR_ITER
for_iter ::= \e__come_froms FOR_ITER . 
for_iter ::= _come_froms . FOR_ITER
for_iter ::= _come_froms FOR_ITER . 
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
function_def_deco ::= mkfuncdeco . store
function_def_deco ::= mkfuncdeco store . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
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
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
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
iflaststmtl ::= testexprl c_stmts JUMP_BACK . 
iflaststmtl ::= testexprl c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexprl c_stmts JUMP_BACK POP_BLOCK . 
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
inplace_op ::= INPLACE_ADD . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_or_c ::= JUMP_BACK . 
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_false37 ::= POP_JUMP_IF_FALSE . COME_FROM
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_1 ::= expr expr BUILD_MAP_1 . 
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
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8 . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
lc_body ::= expr LIST_APPEND . 
list ::= BUILD_LIST_0 . 
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr expr . BUILD_LIST_4
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
list_if ::= expr jmp_false . list_iter
list_if ::= expr jmp_false . list_iter COME_FROM
list_if ::= expr jmp_false list_iter . 
list_if ::= expr jmp_false list_iter . COME_FROM
list_if_not ::= expr . jmp_true list_iter
list_if_not ::= expr . jmp_true list_iter COME_FROM
list_iter ::= lc_body . 
list_iter ::= list_for . 
list_iter ::= list_if . 
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 . expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr . GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER . CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1 . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
lstmt ::= stmt . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR MAKE_FUNCTION_1 . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 . CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 CALL_FUNCTION_1 . 
mkfuncdeco0 ::= mkfunc . 
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . 
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA . LAMBDA_MARKER
return_expr_lambda ::= return_expr RETURN_VALUE_LAMBDA LAMBDA_MARKER . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
set ::= expr . BUILD_SET_1
set ::= expr BUILD_SET_1 . 
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign1 . 
stmt ::= continue . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= function_def_deco . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= return_expr_lambda . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
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
testfalse ::= testfalse_not_and . 
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
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1745        80  LOAD_GLOBAL              TestResult
                  82  LOAD_CONST               False
                  84  LOAD_STR                 "{}'s option {} is set to {}"
                  86  LOAD_FAST                'subject'
                  88  LOAD_FAST                'self'
                  90  LOAD_ATTR                gameplay_option
                  92  LOAD_FAST                'option_result'
                  94  LOAD_FAST                'self'
                  96  LOAD_ATTR                tooltip
                  98  LOAD_CONST               ('tooltip',)
                 100  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
->               102  RETURN_VALUE     
from sims.global_gender_preference_tuning import GlobalGenderPreferenceTuning, GenderPreferenceType
import clock, enum, event_testing, services, sims4.log
from event_testing.results import TestResult, TestResultNumeric
from event_testing.test_base import BaseTest
from event_testing.test_events import TestEvent
from caches import cached_test
from interactions import ParticipantType, ParticipantTypeSim, ParticipantTypeSingle, ParticipantTypeSingleSim, ParticipantTypeActorTargetSim
from interactions.utils.death import DeathType
from objects import ALL_HIDDEN_REASONS
from objects.components import types
from objects.components.stored_object_info_tuning import StoredObjectType
from sims.sim_info_gameplay_options import SimInfoGameplayOptions, is_required_pack_installed
from sims.sim_info_types import Species, SpeciesExtended, Gender, Age
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableFactory, TunableEnumEntry, OptionalTunable, TunableEnumSet, TunableVariant, Tunable, TunableList, TunablePackSafeReference, TunableReference, TunableSet, TunableThreshold, TunableEnumFlags, TunableSimMinute, TunableRange, TunableSkinTone, TunableTuple
from sims4.utils import classproperty
from tag import TunableTags
from traits.trait_type import TraitType
logger = sims4.log.Logger('SimInfoTests')

class MatchType(enum.Int):
    MATCH_ALL = 0
    MATCH_ANY = 1


class _SpeciesTestSpecies(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'species': TunableEnumSet(description='\n            The Sim must be one of the specified species. Species are\n            consolidated, e.g. large/small dog are both DOG.\n            ',
                  enum_type=Species,
                  enum_default=(Species.HUMAN),
                  invalid_enums=(
                 Species.INVALID,))}

    def __call__(self, sim_info):
        return sim_info.species in self.species


class _SpeciesTestExtendedSpecies(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'species': TunableEnumSet(description='\n            The Sim must be one of the specified species. Species are *not*\n            consolidated, e.g. large/small dog are different species.\n            ',
                  enum_type=SpeciesExtended,
                  enum_default=(Species.HUMAN),
                  invalid_enums=(
                 SpeciesExtended.INVALID,))}

    def __call__(self, sim_info):
        return sim_info.extended_species in self.species


class _TraitConflictTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'trait_types': TunableList(description='\n            This test checks for conflicts among the traits of these types\n            from Sim A and Sim B. If no type is specified, it only checks\n            for PERSONALITY traits.\n            ',
                      tunable=TraitType,
                      set_default_as_first_entry=True,
                      unique_entries=True)}

    def __call__(self, trait_tracker_a, trait_tracker_b, invert_result, tooltip):
        conflicts = False
        traits_a = set()
        traits_b = set()
        for trait_type in self.trait_types:
            traits_a.update(trait_tracker_a.get_traits_of_type(trait_type))
            traits_b.update(trait_tracker_b.get_traits_of_type(trait_type))

        for trait_a in traits_a:
            for trait_b in traits_b:
                if trait_a.is_conflicting(trait_b):
                    conflicts = True
                    break
            else:
                continue

            break

        test_pass = conflicts if not invert_result else not conflicts
        if test_pass:
            return TestResult.TRUE
        return TestResult(False, '{} and {} trait conflict test failed. Conflicts: {}, Invert test: {}', (trait_tracker_a._sim_info),
          (trait_tracker_b._sim_info), conflicts, invert_result, tooltip=tooltip)


class _TraitMatchTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'trait_type':TunableEnumEntry(description='\n    \t\tThe trait type to check.\n    \t\t',
       tunable_type=TraitType,
       default=TraitType.PERSONALITY), 
     'minimum_number_of_matches':TunableRange(description='\n    \t\tSim A and B should have at least this number of traits of the specified type in common to pass.\n    \t\t',
       tunable_type=int,
       default=1,
       minimum=1)}

    def __call__(self, trait_tracker_a, trait_tracker_b, invert_result, tooltip):
        min_matches = self.minimum_number_of_matches
        matches = sum((1 for t in trait_tracker_b.get_traits_of_type(self.trait_type) if trait_tracker_a.has_trait(t)))
        test_pass = matches >= min_matches
        if invert_result:
            test_pass = not test_pass
        if test_pass:
            return TestResult.TRUE
        return TestResult(False, '{} and {} trait match test failed. Trait type: {}, Matches: {}, Min matches: {}, Invert result: {}', (trait_tracker_a._sim_info),
          (trait_tracker_b._sim_info), (self.trait_type),
          matches, min_matches, invert_result, tooltip=tooltip)


class AgeUpTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'who': TunableEnumEntry(description='\n                Who or what to apply this test to.\n                ',
                  tunable_type=participant_type_enum,
                  default=participant_type_default)}

    FACTORY_TUNABLES = {'who': TunableEnumEntry(description='\n            Who or what to apply this test to.\n            ',
              tunable_type=ParticipantTypeSingle,
              default=(ParticipantTypeSingle.Actor))}

    def __init__(self, **kwargs):
        (super().__init__)(safe_to_skip=True, **kwargs)

    def get_expected_args(self):
        return {'test_targets': self.who}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            if target is None:
                logger.error('Trying to call AgeUpTest with a None value in the sims iterable.')
                continue
            if target.is_npc:
                return TestResult.TRUE
                if target.can_age_up():
                    return TestResult.TRUE

        return TestResult(False, '{} failed AgeUp check. Current age: {}', target, (target._age_progress.get_value()), tooltip=(self.tooltip))


class SimInfoTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'who': TunableEnumEntry(description='"\n                Who or what to apply this test to\n                ',
                  tunable_type=participant_type_enum,
                  default=participant_type_default)}

    FACTORY_TUNABLES = {'who':TunableEnumEntry(description='\n            Who or what to apply this test to\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'gender':OptionalTunable(tunable=TunableEnumEntry(description='\n                The Sim must be of the specified gender.\n                ',
       tunable_type=Gender,
       default=None),
       enabled_name='specified',
       disabled_name='unspecified'), 
     'ages':OptionalTunable(tunable=TunableEnumSet(description='\n                The Sim must be one of the specified ages.\n                ',
       enum_type=Age,
       enum_default=(Age.ADULT),
       default_enum_list=[
      Age.TEEN,
      Age.YOUNGADULT,
      Age.ADULT,
      Age.ELDER]),
       disabled_name='unspecified',
       enabled_name='specified'), 
     'species':TunableVariant(specified=_SpeciesTestSpecies.TunableFactory(),
       specified_extended=_SpeciesTestExtendedSpecies.TunableFactory(),
       locked_args={'unspecified': None},
       default='unspecified'), 
     'can_age_up':OptionalTunable(tunable=Tunable(description='\n                Whether the Sim is eligible to advance to the next age.\n                ',
       tunable_type=bool,
       default=None),
       enabled_name='specified',
       disabled_name='unspecified'), 
     'npc':OptionalTunable(tunable=Tunable(description="\n                Whether the Sim must be an NPC or Playable Sim.\n                If enabled and true, the sim must be an NPC for this test to pass.\n                If enabled and false, the sim must be playable, non-NPC sim for this test to pass.\n                If disabled, this portion of the Sim Info test will be ignored.\n                \n                Note: NPC in this case means a Sim that is not currently\n                controllable (selectable), or Not Player Controllable. If you\n                need to know if the Sim has ever been played, use 'Has Been\n                Played'\n                ",
       tunable_type=bool,
       default=False)), 
     'has_been_played':OptionalTunable(tunable=Tunable(description='\n                Whether the Sim has ever been played as a Playable Sim.\n                If enabled and true, the Sim must have been played by the player.\n                If enabled and false, the Sim must never have been played.\n                If disabled, this portion of the Sim Info test will be ignored.\n                ',
       tunable_type=bool,
       default=False)), 
     'is_active_sim':OptionalTunable(tunable=Tunable(description='\n                Whether the Sim must be the active selected Sim.\n                If enabled and true, the sim must active for this test to pass.\n                If enabled and false, the sim must not be active for this test to pass.\n                If disabled, this portion of the Sim Info test will be ignored.\n                ',
       tunable_type=bool,
       default=True)), 
     'match_type':TunableEnumEntry(description='\n            When testing multiple participants if MATCH_ALL is set, then all the\n            participants need to pass the test.\n             \n            If MATCH_ANY is set, test will pass as soon as one of them meet the\n            criteria\n            ',
       tunable_type=MatchType,
       default=MatchType.MATCH_ALL)}
    __slots__ = ('gender', 'who', 'ages', 'species', 'can_age_up', 'is_active_sim',
                 'npc', 'has_been_played', 'match_type')

    def get_expected_args(self):
        return {'test_targets': self.who}

    @cached_test
    def __call__(self, test_targets=()):
        if self.match_type == MatchType.MATCH_ANY:
            for target in test_targets:
                result = self._test_sim_info(target)
                if result:
                    return result

            return result
        for target in test_targets:
            result = self._test_sim_info(target)
            if not result:
                return result

        return TestResult.TRUE

    def _test_sim_info(self, sim_info):
        if sim_info is None:
            return TestResult(False, 'Sim Info is None!')
            if self.gender is not None:
                if sim_info.gender != self.gender:
                    return TestResult(False, "{}'s gender is {}, must be {}", (self.who.name), (sim_info.gender), (self.gender), tooltip=(self.tooltip))
            if self.ages is not None:
                if sim_info.age not in self.ages:
                    return TestResult(False, "{}'s age is {}, must be one of the following: {}", (self.who.name),
                      (sim_info.age), (', '.join((str(age) for age in self.ages))), tooltip=(self.tooltip))
            if self.species is not None:
                result = self.species(sim_info)
                if not result:
                    return TestResult(False, '{} is not of a valid species', sim_info, tooltip=(self.tooltip))
            if self.can_age_up is not None:
                if self.can_age_up != sim_info.can_age_up():
                    return TestResult(False, '{} {} be able to advance to the next age.', (self.who.name),
                      ('must' if self.can_age_up else 'must not'), tooltip=(self.tooltip))
            if self.npc is not None:
                if sim_info.is_npc != self.npc:
                    return TestResult(False, '{} does not meet the npc requirement.', (sim_info.full_name), tooltip=(self.tooltip))
            if self.has_been_played is not None:
                if sim_info.is_player_sim != self.has_been_played:
                    return TestResult(False, '{} does not meet the has_been_played requirement.', (sim_info.full_name), tooltip=(self.tooltip))
            if self.is_active_sim is not None:
                active_sim = services.get_active_sim()
                if active_sim is None:
                    return TestResult(False, 'SimInfoTest: Client returned active Sim as None.', tooltip=(self.tooltip))
                if self.is_active_sim:
                    if active_sim.sim_info is not sim_info:
                        return TestResult(False, '{} does not meet the active sim requirement.', (sim_info.full_name), tooltip=(self.tooltip))
        elif active_sim.sim_info is sim_info:
            return TestResult(False, '{} does not meet the active sim requirement.', (sim_info.full_name), tooltip=(self.tooltip))
        return TestResult.TRUE


class TraitTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.TraitAddEvent, TestEvent.SimTravel, TestEvent.HouseholdChanged)

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'subject': TunableEnumEntry(participant_type_enum, participant_type_default, description='Who or what to apply this test to')}

    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The participant that is to be the subject of the test.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'whitelist_traits':TunableList(description='\n            The Sim is required to have the specified number of traits from this\n            list in order to pass the test.\n            ',
       tunable=TunablePackSafeReference(description="\n                A whitelist trait. Please note: for pack-safe entries that are\n                not loaded, the game will behave as if the entry doesn't exist.\n                This allows you to specify a pack trait and required count of 1\n                and always fail the test should the appropriate pack not be\n                installed.\n                ",
       manager=(services.get_instance_manager(sims4.resources.Types.TRAIT))),
       allow_none=True), 
     'blacklist_traits':TunableList(description='\n            The is required to not have traits from this list in order to pass\n            this test. Should num_blacklist_allowed be specified, then the Sim\n            is allowed to have up to that amount of blacklisted traits before\n            failing this test.\n            ',
       tunable=TunableReference(description='\n                A blacklist trait.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.TRAIT)),
       pack_safe=True)), 
     'whitelist_trait_types':TunableEnumSet(description='\n            The Sim is required to have the specified number of traits with \n            these types in order to pass the test.\n            ',
       enum_type=TraitType), 
     'blacklist_trait_types':TunableEnumSet(description='\n            The Sim is required to not have traits of these types to pass this \n            test. Should Num Blacklist Allowed be specified, then the Sim is \n            allowed to have up to that amount of blacklisted traits before \n            failing this test.\n            ',
       enum_type=TraitType), 
     'num_whitelist_required':Tunable(description='\n            The number of whitelist traits that the specified Sim is required to\n            have in order to pass this test.\n            ',
       tunable_type=int,
       default=1), 
     'num_blacklist_allowed':Tunable(description='\n            The threshold of blacklist traits owned by the specified Sim that\n            will trigger a test failure.\n            ',
       tunable_type=int,
       default=0), 
     'apply_thresholds_on_individual_basis':Tunable(description="\n            If checked then Num Whitelist Required and Num Blacklist Allowed\n            will be applied to each individual participant from the subject.\n            If unchecked then it will apply the values to the total whitelist\n            and blacklist matches on the group.\n            \n            IMPORTANT!!!\n            In the case of objectives this should probably be set to false\n            since we know that this is coming from only one sim and that we\n            want to use the value that comes out of the test result numeric.\n            This isn't just locked to being this value since there are valid\n            cases within that system when you are looking at a group of sims\n            and could want to test that one of your sims passes.  Ex. Having\n            a ghost sim in the household.\n            ",
       tunable_type=bool,
       default=True)}

    def get_test_events_to_register(self):
        if self.subject == ParticipantType.ActiveHousehold:
            return (
             TestEvent.TraitAddEvent, TestEvent.SimTravel, TestEvent.HouseholdChanged)
        return (
         TestEvent.TraitAddEvent, TestEvent.SimTravel)

    __slots__ = ('subject', 'whitelist_traits', 'blacklist_traits', 'whitelist_trait_types',
                 'blacklist_trait_types', 'num_whitelist_required', 'num_blacklist_allowed',
                 'apply_thresholds_on_individual_basis')

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        trait_pie_menu_icon = None
        white_count = 0
        black_count = 0
        for target in test_targets:
            if not hasattr(target, 'trait_tracker'):
                return TestResult(False, '{} does not have a TraitTracker and has no traits.', target, tooltip=(self.tooltip))
                trait_tracker = target.trait_tracker
                if self.whitelist_traits or self.whitelist_trait_types:
                    if self.apply_thresholds_on_individual_basis:
                        white_count = 0
                    pass_white = False
                    for trait in self.whitelist_traits:
                        if trait is None:
                            continue
                        if trait_tracker.has_trait(trait):
                            white_count += 1
                            if white_count >= self.num_whitelist_required:
                                if self.subject == ParticipantType.Actor:
                                    trait_pie_menu_icon = trait.pie_menu_icon
                                pass_white = True
                                break

                    if not pass_white:
                        for trait_type in self.whitelist_trait_types:
                            traits = trait_tracker.get_traits_of_type(trait_type)
                            white_count += len(traits)
                            if white_count >= self.num_whitelist_required:
                                if self.subject == ParticipantType.Actor:
                                    trait_pie_menu_icon = traits[0].pie_menu_icon
                                pass_white = True
                                break

                    if not pass_white:
                        if self.apply_thresholds_on_individual_basis:
                            return TestResult(False, "{} doesn't have any or enough traits in white list", (self.subject.name), tooltip=(self.tooltip))
                if self.blacklist_traits or self.blacklist_trait_types:
                    if self.apply_thresholds_on_individual_basis:
                        black_count = 0
                for trait in self.blacklist_traits:
                    if trait_tracker.has_trait(trait):
                        black_count += 1
                        if black_count > self.num_blacklist_allowed:
                            return TestResult(False, '{} has trait {} in black list', (self.subject.name), trait, tooltip=(self.tooltip))

                for trait_type in self.blacklist_trait_types:
                    black_count += len(trait_tracker.get_traits_of_type(trait_type))
                    if black_count > self.num_blacklist_allowed:
                        return TestResult(False, '{} has {} traits that are blacklisted by type.', (self.subject.name), black_count, tooltip=(self.tooltip))

        if not self.apply_thresholds_on_individual_basis:
            if white_count < self.num_whitelist_required:
                return TestResultNumeric(False, 'Not enough enough whitelist traits through all participants.',
                  current_value=white_count,
                  goal_value=(self.num_whitelist_required),
                  is_money=False)
        return TestResult(True, icon=trait_pie_menu_icon)

    def goal_value(self):
        return self.num_whitelist_required


class TraitComparisonTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    TRAIT_CONFLICT = 0
    TRAIT_MATCH = 1
    FACTORY_TUNABLES = {'sim_a':TunableEnumEntry(description='\n            One of the sims to check traits against another sim.\n            ',
       tunable_type=ParticipantTypeSim,
       default=ParticipantTypeSim.Actor), 
     'sim_b':TunableEnumEntry(description='\n            The other sim to check traits against.\n            ',
       tunable_type=ParticipantTypeSim,
       default=ParticipantTypeSim.TargetSim), 
     'trait_comparison':TunableVariant(conflict=_TraitConflictTest.TunableFactory(description='\n                The test passes if Sim A and Sim B have any conflicting traits.\n                '),
       match=_TraitMatchTest.TunableFactory(description='\n                Check if sims have matching traits of a certain type.\n                '),
       default='conflict'), 
     'invert_result':Tunable(description='\n            If checked, invert the test result.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'sim_a':self.sim_a, 
         'sim_b':self.sim_b}

    @cached_test
    def __call__(self, sim_a=None, sim_b=None):
        sim_a = next(iter(sim_a), None)
        sim_b = next(iter(sim_b), None)
        if sim_a is None:
            return TestResult(False, 'Participant {} is None', (self.sim_a), tooltip=(self.tooltip))
        if sim_b is None:
            return TestResult(False, 'Participant {} is None', (self.sim_b), tooltip=(self.tooltip))
        trait_tracker_a = sim_a.trait_tracker
        trait_tracker_b = sim_b.trait_tracker
        return self.trait_comparison(trait_tracker_a, trait_tracker_b, self.invert_result, self.tooltip)


class BuffTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.BuffBeganEvent,)

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'subject': TunableEnumEntry(description='\n                    To whom or what this test should be applied.\n                    ',
                      tunable_type=participant_type_enum,
                      default=participant_type_default)}

    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            Who or what to apply this test to.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'whitelist':OptionalTunable(description="\n            If enabled, participant will test for buff's on the whitelist.\n            ",
       tunable=TunableSet(description='\n                The participant must have at least one buff in this list to pass the\n                test.\n                ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
       pack_safe=True))), 
     'whitelist_tags':OptionalTunable(description='\n            If enabled, participant will test for buffs which match tags in the defined set.\n            ',
       tunable=TunableTags(description='\n                The participant must have at least one buff which matches a tag in this list to pass the test.\n                ',
       filter_prefixes=('buff', ))), 
     'blacklist':TunableSet(description='\n            The Sim must not have any buff in this list to pass the test.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
       pack_safe=True)), 
     'blacklist_tags':TunableTags(description='\n            The Sim must not have any buff that matches any of these tags to pass the test.\n            ',
       filter_prefixes=('buff', )), 
     'apply_whitelist_on_individual_basis':Tunable(description='\n            If checked, will require that each target has at least one\n            whitelisted buff. If unchecked, will require only a single target to\n            have at least one whitelisted trait.\n            ',
       tunable_type=bool,
       default=True)}
    __slots__ = ('subject', 'whitelist', 'whitelist_tags', 'blacklist', 'blacklist_tags',
                 'apply_whitelist_on_individual_basis')

    def __init__(self, **kwargs):
        (super().__init__)(safe_to_skip=True, **kwargs)

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        has_satisfied_whitelist_once = self.whitelist is None and self.whitelist_tags is None
        for target in test_targets:
            if self.blacklist:
                if any((target.has_buff(buff_type) for buff_type in self.blacklist)):
                    return TestResult(False, '{} has buff in blacklist {}', target, (self.blacklist), tooltip=(self.tooltip))
                elif self.blacklist_tags and any((target.has_buff_with_tag(blacklist_tag) for blacklist_tag in self.blacklist_tags)):
                    return TestResult(False, '{} has buff matching a blacklist tag {}', target, (self.blacklist_tags),
                      tooltip=(self.tooltip))
                if self.whitelist is not None:
                    if self.apply_whitelist_on_individual_basis:
                        if not any((target.has_buff(buff_type) for buff_type in self.whitelist)):
                            return TestResult(False, "{} doesn't have any buff in whitelist", target, tooltip=(self.tooltip))
            elif not has_satisfied_whitelist_once:
                if any((target.has_buff(buff_type) for buff_type in self.whitelist)):
                    has_satisfied_whitelist_once = True
            if self.whitelist_tags is not None:
                if self.apply_whitelist_on_individual_basis:
                    if not any((target.has_buff_with_tag(whitelist_tag) for whitelist_tag in self.whitelist_tags)):
                        return TestResult(False, "{} doesn't have any buff matching whitelist tags", target, tooltip=(self.tooltip))
                elif has_satisfied_whitelist_once or any((target.has_buff_with_tag(whitelist_tag) for whitelist_tag in self.whitelist_tags)):
                    has_satisfied_whitelist_once = True

        if self.apply_whitelist_on_individual_basis:
            return TestResult.TRUE
        if has_satisfied_whitelist_once:
            return TestResult.TRUE
        return TestResult(False, 'No target has a buff in whitelist', tooltip=(self.tooltip))


class BuffAddedTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.BuffBeganEvent,)
    USES_EVENT_DATA = True
    FACTORY_TUNABLES = {'acceptable_buffs':TunableSet(description='\n            Buffs that will pass the test.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
       pack_safe=True)), 
     'check_visibility':Tunable(description='\n            If checked then we will check to make sure that the buff is\n            visible.\n            ',
       tunable_type=bool,
       default=False)}

    def __init__(self, **kwargs):
        (super().__init__)(safe_to_skip=True, **kwargs)

    def get_expected_args(self):
        return {'buff': event_testing.test_constants.FROM_EVENT_DATA}

    def get_test_events_to_register(self):
        return ()

    def get_custom_event_registration_keys(self):
        keys = [(TestEvent.BuffBeganEvent, buff) for buff in self.acceptable_buffs]
        return keys

    @cached_test
    def __call__(self, buff=None):
        if buff is None:
            return TestResult(False, 'Buff provided is None, valid during zone load.')
        else:
            if self.acceptable_buffs:
                if buff not in self.acceptable_buffs:
                    return TestResult(False, "{} isn't in acceptable buff list.", buff, tooltip=(self.tooltip))
            if self.check_visibility:
                return buff.visible or TestResult(False, '{} is not visible when we are checking for visibility.', buff, tooltip=(self.tooltip))
        return TestResult.TRUE

    def validate_tuning_for_objective(self, objective):
        if not self.check_visibility:
            if not self.acceptable_buffs:
                logger.error('Invalid tuning in objective {}.  One of the following must be true: Check Visibility must be true or Acceptable Buffs must have entries.', objective)


class MoodTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.MoodChange, TestEvent.SimTravel)

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'who': TunableEnumEntry(description='\n                    To whom or what this test should be applied.\n                    ',
                  tunable_type=participant_type_enum,
                  default=participant_type_default)}

    FACTORY_TUNABLES = {'who':TunableEnumEntry(description='\n            To whom or what this test should be applied.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'mood':TunablePackSafeReference(description="\n            The mood that must be active (or must be inactive, if 'Disallow' is\n            checked).\n            ",
       manager=services.get_instance_manager(sims4.resources.Types.MOOD)), 
     'disallow':Tunable(description="\n            If True, this test will pass if the Sim's mood does NOT match the tuned mood reference.\n            ",
       tunable_type=bool,
       default=False)}
    __slots__ = ('who', 'mood', 'disallow')

    def __init__(self, **kwargs):
        (super().__init__)(safe_to_skip=True, **kwargs)

    def get_expected_args(self):
        return {'test_targets': self.who}

    @cached_test
    def __call__(self, test_targets=()):
        if self.mood is None:
            if self.disallow:
                return TestResult(True)
            return TestResult(False, "Can't match mood as it is None, probably due pack safeness.")
        influence_by_active_mood = False
        for target in test_targets:
            if not target is None:
                if not target.is_sim:
                    logger.error("Trying to call MoodTest with an invalid Participant Type, {}, in the 'Who' field of tuning. Skipping this participant and attempting to continue.", self)
                    continue
                sim_mood = target.get_mood()
                if self.disallow:
                    if self.mood is sim_mood:
                        return TestResult(False, '{} failed mood check for disallowed {}. Current mood: {}', target, (self.mood.__name__), (sim_mood.__name__ if sim_mood is not None else None), tooltip=(self.tooltip))
                else:
                    if self.mood is not sim_mood:
                        return TestResult(False, '{} failed mood check for {}. Current mood: {}', target, (self.mood.__name__), (sim_mood.__name__ if sim_mood is not None else None), tooltip=(self.tooltip))
                    if self.who == ParticipantTypeSim.Actor:
                        influence_by_active_mood = True

        return TestResult(True, influence_by_active_mood=influence_by_active_mood)


class GenealogyRelationType(enum.IntFlags):
    INVALID = 0
    PARENTS = 1
    GRANDPARENTS = 2
    PARENTS_AND_GRANDPARENTS = PARENTS | GRANDPARENTS


class GenealogyTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The subject who requires to have the genealogy relationship with\n            the target participant. e.g, if PARENTS is selected, then the\n            subject_sim must be a parent of the target_sim.\n            ',
       tunable_type=ParticipantTypeSim,
       default=ParticipantTypeSim.Actor), 
     'target_sim':TunableEnumEntry(description='\n            The target sim to test the relationship against.\n            ',
       tunable_type=ParticipantTypeSim,
       default=ParticipantTypeSim.TargetSim), 
     'required_relationship':TunableEnumEntry(description='\n            The genealogy relationship required from test_participant to\n            target_participant.\n            ',
       tunable_type=GenealogyRelationType,
       default=GenealogyRelationType.INVALID,
       invalid_enums=(
      GenealogyRelationType.INVALID,))}

    def get_expected_args(self):
        return {'source_participants':self.subject, 
         'target_participants':self.target_sim}

    def _get_required_ids(self, sim_info):
        genealogy = sim_info.genealogy
        match_ids = set()
        if self.required_relationship & GenealogyRelationType.PARENTS:
            match_ids.update(list(genealogy.get_parent_sim_ids_gen()))
        if self.required_relationship & GenealogyRelationType.GRANDPARENTS:
            match_ids.update(list(genealogy.get_grandparent_sim_ids_gen()))
        return match_ids

    @cached_test
    def __call__(self, source_participants=(), target_participants=()):
        for source_participant in source_participants:
            if not source_participant.is_sim:
                return TestResult(False, 'Source Participant {} is not a sim.', source_participant, tooltip=(self.tooltip))
                for target_participant in target_participants:
                    target_participant_info = None
                    if not target_participant.is_sim:
                        target_participant_info = getattr(target_participant, 'sim_info', None)
                        if target_participant_info is None:
                            return TestResult(False, 'Target Participant {} is not a sim.', target_participant, tooltip=(self.tooltip))
                    error_message = "Genealogy test fail, {} is not {}'s {}".format(source_participant, target_participant, self.required_relationship)
                    match_ids = self._get_required_ids(target_participant_info or target_participant)
                    if source_participant.sim_id not in match_ids:
                        return TestResult(False, error_message, tooltip=(self.tooltip))

        return TestResult.TRUE


class GenderPreferenceTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'negate':Tunable(description='\n            If checked, the test result will return True if\n            the actor and subject are not compatible and\n            false otherwise.\n            ',
       tunable_type=bool,
       default=False), 
     'subject':TunableEnumFlags(description='\n            The subject(s) checking this the gender preference.\n            ',
       enum_type=ParticipantTypeSim,
       default=ParticipantTypeSim.Actor), 
     'target_sim':TunableEnumFlags(description='\n            Target(s) of the relationship(s).\n            ',
       enum_type=ParticipantTypeSim,
       default=ParticipantTypeSim.TargetSim), 
     'gender_preference_type':TunableEnumEntry(description='\n            Preference type to check compatibility with.\n            ',
       tunable_type=GenderPreferenceType,
       default=GenderPreferenceType.ROMANTIC), 
     'consider_exploration':Tunable(description='\n            If checked, then we will allow sims who do not have matching attractions but are exploring.\n            If not, then we will strictly consider only their current preference.\n            Only applicable with Romantic Preference.\n            ',
       tunable_type=bool,
       default=True), 
     'override_target_gender_test':OptionalTunable(TunableEnumEntry(description='\n                Required gender to test against as the target gender.\n                ',
       tunable_type=Gender,
       default=(Gender.FEMALE)),
       disabled_name='test_target_sim_gender',
       enabled_name='test_specific_gender'), 
     'ignore_reciprocal':Tunable(description="\n            If checked, we will only check the actor's compatibility with\n            the target, and not the other way around.\n            ",
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'subject_participants':self.subject, 
         'target_participants':self.target_sim}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)

    def _check_gender_preference(self, sim_a, sim_b, override_target_gender=None):
        if override_target_gender is not None:
            sim_b_gender = override_target_gender
        else:
            sim_b_gender = sim_b.gender
        preference_map = None
        if self.gender_preference_type == GenderPreferenceType.ROMANTIC:
            preference_map = GlobalGenderPreferenceTuning.ROMANTIC_PREFERENCE_TRAITS_MAPPING
        else:
            if self.gender_preference_type == GenderPreferenceType.WOOHOO:
                preference_map = GlobalGenderPreferenceTuning.WOOHOO_PREFERENCE_TRAITS_MAPPING
        if preference_map is None:
            logger.error('GenderPreferenceTest not tuned with a valid preference type.', owner='amwu')
            return False
        attracted_trait = preference_map[sim_b_gender].is_attracted_trait
        is_sim_a_attracted = sim_a.has_trait(attracted_trait) or self.gender_preference_type == GenderPreferenceType.ROMANTIC and self.consider_exploration and sim_a.is_exploring_sexuality
        return is_sim_a_attracted

    @cached_test
    def __call__(self, subject_participants=None, target_participants=None):
        for subject_participant in subject_participants:
            if not subject_participant.is_sim:
                return TestResult(False, 'GenderPreferenceTest: subject {} is not a sim.', subject_participant, tooltip=(self.tooltip))
                if self.override_target_gender_test is not None:
                    result = self._check_gender_preference(subject_participant, None, self.override_target_gender_test)
                    if self.negate:
                        result = not result
                    if not result:
                        return TestResult(False, 'GenderPreferenceTest: Sim {} does not have desired compatibility with gender {}.',
                          subject_participant,
                          (self.override_target_gender_test),
                          tooltip=(self.tooltip))
                    return TestResult.TRUE
                for target_participant in target_participants:
                    if not target_participant.is_sim:
                        return TestResult(False, 'GenderPreferenceTest: target {} is not a sim.', target_participant, tooltip=(self.tooltip))
                        sim_a_result = self._check_gender_preference(subject_participant, target_participant)
                        if self.ignore_reciprocal:
                            if self.negate:
                                sim_a_result = not sim_a_result
                            return sim_a_result or TestResult(False, 'GenderPreferenceTest: Sim {} does not have desired compatibility with Sim {}.',
                              subject_participant,
                              target_participant,
                              tooltip=(self.tooltip))
                            continue
                        sim_b_result = self._check_gender_preference(target_participant, subject_participant)
                        total_result = sim_a_result and sim_b_result
                        if self.negate:
                            total_result = not total_result
                        return total_result or TestResult(False, 'GenderPreferenceTest: Sim {} does not have desired compatibility with Sim {}.',
                          subject_participant,
                          target_participant,
                          tooltip=(self.tooltip))

        return TestResult.TRUE


class KnowledgeTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The subject of the test. This is the Sim that needs to know\n            information about the target.\n            ',
       tunable_type=ParticipantTypeSingleSim,
       default=ParticipantTypeSingleSim.Actor), 
     'target':TunableEnumEntry(description='\n            The target of the test. This is the Sim whose information needs to\n            be known by the subject.\n            ',
       tunable_type=ParticipantTypeSingleSim,
       default=ParticipantTypeSingleSim.TargetSim), 
     'required_traits':TunableList(description='\n            If there are any traits specified in this list, the test will fail\n            if none of the traits are known.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.TRAIT)))), 
     'prohibited_traits':TunableSet(description='\n            The test will fail if any of the traits specified in this list are\n            known.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.TRAIT)))), 
     'career_knowledge_requirement':TunableVariant(description="\n            If enabled, the test will check the subject's knowledge of the\n            target's careers and fail if the knowledge requirement is not met.\n            ",
       locked_args={'disabled':None, 
      'knows_about_career':True, 
      'does_not_know_about_career':False},
       default='disabled'), 
     'major_knowledge_requirement':TunableVariant(description="\n            If enabled, the test will check the subject's knowledge of the\n            target's major and fail if the knowledge requirement is not met.\n            ",
       locked_args={'disabled':None, 
      'knows_about_major':True, 
      'does_not_know_about_major':False},
       default='disabled'), 
     'romantic_preference_knowledge_requirement':TunableVariant(description="\n            If enabled, the test will check the subject's knowledge of the\n            target's romantic preference and fail if the knowledge requirement is not met.\n            ",
       locked_args={'disabled':None, 
      'knows_about_romantic_preference':True, 
      'does_not_know_about_romantic_preference':False},
       default='disabled'), 
     'woohoo_preference_knowledge_requirement':TunableVariant(description="\n            If enabled, the test will check the subject's knowledge of the\n            target's woohoo preference and fail if the knowledge requirement is not met.\n            ",
       locked_args={'disabled':None, 
      'knows_about_woohoo_preference':True, 
      'does_not_know_about_woohoo_preference':False},
       default='disabled'), 
     'knows_all_traits_of_type':OptionalTunable(tunable=TunableTuple(description='\n                The subject Sim does/does not know all the traits of a certain type of target Sim.\n                ',
       knows_all=Tunable(description='\n                    If checked, the subject Sim must know all the traits of the specified type to pass.\n                    If unchecked, the subject Sim must not know all the traits of the specified type to pass.\n                    ',
       tunable_type=bool,
       default=True),
       trait_type=TunableEnumEntry(description='\n                    The trait type to check.\n                    ',
       tunable_type=TraitType,
       default=(TraitType.PERSONALITY))))}

    def get_expected_args(self):
        return {'subject':self.subject, 
         'target':self.target}

    @cached_test
    def __call__(self, subject=None, target=None):
        subject = next(iter(subject))
        target = next(iter(target))
        if subject is None:
            return TestResult(False, 'Participant {} is None', (self.subject), tooltip=(self.tooltip))
        if target is None:
            return TestResult(False, 'Participant {} is None', (self.target), tooltip=(self.tooltip))
        knowledge = subject.relationship_tracker.get_knowledge(target.id)
        known_traits = knowledge.known_traits if knowledge is not None else set()
        if self.required_traits:
            if not any((required_trait in known_traits for required_trait in self.required_traits)):
                return TestResult(False, '{} does not know {} has any of these traits: {}', subject, target, (self.required_traits), tooltip=(self.tooltip))
        if any((prohibited_trait in known_traits for prohibited_trait in self.prohibited_traits)):
            return TestResult(False, '{} knows {} has one or more of these traits: {}', subject, target, (self.prohibited_traits), tooltip=(self.tooltip))
        if self.career_knowledge_requirement is not None:
            knows_career = False if knowledge is None else knowledge.knows_career
            if knows_career != self.career_knowledge_requirement:
                return TestResult(False, '{} knowledge about {} career does not match requirement. Required: {}, Actual: {}', subject,
                  target, (self.career_knowledge_requirement), knows_career, tooltip=(self.tooltip))
        if self.major_knowledge_requirement is not None:
            knows_major = False if knowledge is None else knowledge.knows_major
            if knows_major != self.major_knowledge_requirement:
                return TestResult(False, '{} knowledge about {} major does not match requirement. Required: {}, Actual: {}', subject,
                  target, (self.major_knowledge_requirement), knows_major, tooltip=(self.tooltip))
        if self.romantic_preference_knowledge_requirement is not None:
            knows_romantic_preference = False if knowledge is None else knowledge.knows_romantic_preference
            if knows_romantic_preference != self.romantic_preference_knowledge_requirement:
                return TestResult(False, '{} knowledge about {} romantic orientation does not match requirement. Required {}, Actual: {}', subject,
                  target, (self.romantic_preference_knowledge_requirement), knows_romantic_preference, tooltip=(self.tooltip))
        if self.woohoo_preference_knowledge_requirement is not None:
            knows_woohoo_preference = False if knowledge is None else knowledge.knows_woohoo_preference
            if knows_woohoo_preference != self.woohoo_preference_knowledge_requirement:
                return TestResult(False, '{} knowledge about {} woohoo orientation does not match requirement. Required {}, Actual: {}', subject,
                  target, (self.woohoo_preference_knowledge_requirement), knows_woohoo_preference, tooltip=(self.tooltip))
        if self.knows_all_traits_of_type is not None:
            must_know_all = self.knows_all_traits_of_type.knows_all
            num_traits_of_type = len(target.trait_tracker.get_traits_of_type(self.knows_all_traits_of_type.trait_type))
            num_known_traits_of_type = sum((1 for trait in known_traits if trait.trait_type == self.knows_all_traits_of_type.trait_type))
            if must_know_all:
                if not (num_traits_of_type != num_known_traits_of_type or must_know_all):
                    if num_traits_of_type == num_known_traits_of_type:
                        return TestResult(False, '{} knowledge about {} all traits of type {} does not match requirement. Must know all: {}, Total number of traits: {}, Known: {}',
                          subject,
                          target, (self.knows_all_traits_of_type.trait_type), must_know_all,
                          num_traits_of_type, num_known_traits_of_type, tooltip=(self.tooltip))
        return TestResult.TRUE


class SatisfactionPointTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.WhimBucksChanged,)
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            Who or what to apply this test to\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'threshold':TunableThreshold(description="\n            The threshold to control availability based on the statistic's value\n            ")}

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            if not target.is_sim:
                return TestResult(False, 'Cannot test satisfaction points on object other than sim {} as subject {}.',
                  target,
                  (self.subject),
                  tooltip=(self.tooltip))
                current_satisfaction_points = target.get_satisfaction_points()
                return self.threshold.compare(current_satisfaction_points) or TestResult(False, 'No subjects have enough satisfaction points',
                  tooltip=(self.tooltip))

        return TestResult.TRUE


class StoredObjectInfoTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The participant that is to be the subject of the test.\n            ',
       tunable_type=ParticipantTypeSingle,
       default=ParticipantTypeSingle.Actor), 
     'target':TunableEnumEntry(description='\n            The target of the test. This is the Object whose information need \n            to be checked with StoredObjectInfo component from the subject.\n            ',
       tunable_type=ParticipantTypeSingle,
       default=ParticipantTypeSingle.Object), 
     'invert':Tunable(description='\n            Whether or not to invert the results of this test.\n            ',
       tunable_type=bool,
       default=False), 
     'stored_object_type':TunableEnumEntry(description='\n            The type of object being stored. This will be used to retrieve the\n            stored object from the Stored Object Info Component of the target.\n            ',
       tunable_type=StoredObjectType,
       default=StoredObjectType.INVALID,
       invalid_enums=(
      StoredObjectType.INVALID,))}

    def get_expected_args(self):
        return {'subject_participant':self.subject, 
         'target_participant':self.target}

    @cached_test
    def __call__(self, subject_participant=None, target_participant=None):
        if subject_participant is None or target_participant is None:
            return TestResult(False, 'Subject or Target participant is None.', tooltip=(self.tooltip))
        subject = next(iter(subject_participant))
        target = next(iter(target_participant))
        if not subject.has_component(types.STORED_OBJECT_INFO_COMPONENT):
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} has no StoredObjectInfo component.', subject, tooltip=(self.tooltip))
        stored_object_id = subject.get_stored_object_info_id(self.stored_object_type)
        if stored_object_id is None:
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} has no stored object id info.', subject, tooltip=(self.tooltip))
        if stored_object_id != target.id:
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} stored object id is not the same with {} id.', subject, target, tooltip=(self.tooltip))
        if self.invert:
            return TestResult(False, '{} stored object id is the same with {} id, but invert is checked.', subject, target, tooltip=(self.tooltip))
        return TestResult.TRUE


class StoredObjectInfoExistenceTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The participant that is to be the subject of the test.\n            ',
       tunable_type=ParticipantTypeSingle,
       default=ParticipantTypeSingle.Actor), 
     'invert':Tunable(description='\n            Whether or not to invert the results of this test.\n            ',
       tunable_type=bool,
       default=False), 
     'stored_object_type':TunableEnumEntry(description='\n            The type of object being stored. This will be used to retrieve the\n            stored object from the Stored Object Info Component of the target.\n            ',
       tunable_type=StoredObjectType,
       default=StoredObjectType.INVALID,
       invalid_enums=(
      StoredObjectType.INVALID,))}

    def get_expected_args(self):
        return {'subject_participant': self.subject}

    @cached_test
    def __call__(self, subject_participant=None):
        if subject_participant is None:
            return TestResult(False, 'Subject participant is None.', tooltip=(self.tooltip))
        subject = next(iter(subject_participant))
        if not subject.has_component(types.STORED_OBJECT_INFO_COMPONENT):
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} has no StoredObjectInfo component.', subject, tooltip=(self.tooltip))
        stored_object_id = subject.get_stored_object_info_id(self.stored_object_type)
        if stored_object_id is None:
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} has no stored object id info.', subject, tooltip=(self.tooltip))
        stored_object = services.object_manager().get(stored_object_id)
        if stored_object is None:
            if self.invert:
                return TestResult.TRUE
            return TestResult(False, '{} stored object is not found on current lot.', subject, tooltip=(self.tooltip))
        if self.invert:
            return TestResult(False, '{} stored object {} is found on current lot, but invert is checked', subject, stored_object, tooltip=(self.tooltip))
        return TestResult.TRUE


class PregnancyTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'participant':TunableEnumEntry(description='\n            The participant against which to run this pregnancy test.\n            ',
       tunable_type=ParticipantTypeSingleSim,
       default=ParticipantTypeSingleSim.Actor), 
     'offspring_gender':OptionalTunable(description="\n            If enabled, test for the offspring's gender.\n            ",
       tunable=TunableEnumEntry(description='\n                The gender to test for. If the offsrping is not of this gender,\n                the test fails.\n                ',
       tunable_type=Gender,
       default=(Gender.FEMALE)),
       disabled_name='Dont_Care',
       enabled_name='Require')}

    def get_expected_args(self):
        return {'test_targets': self.participant}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            pregnancy_tracker = target.pregnancy_tracker
            if not pregnancy_tracker.is_pregnant:
                return TestResult(False, '{} is not pregnant.', target, tooltip=(self.tooltip))
                pregnancy_tracker.create_offspring_data()
                first_offspring = next(pregnancy_tracker.get_offspring_data_gen(), None)
                if first_offspring is None:
                    return TestResult(False, '{} has no offspring.', target, tooltip=(self.tooltip))
                if self.offspring_gender is not None and first_offspring.gender != self.offspring_gender:
                    return TestResult(False, "{}'s first offspring should be {} but is {}.", target, (self.offspring_gender), (first_offspring.gender), tooltip=(self.tooltip))

        return TestResult.TRUE


class FilterTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'filter_target':OptionalTunable(tunable=TunableEnumEntry(description='\n                The sim that will have the filter checked against.\n                ',
       tunable_type=ParticipantType,
       default=(ParticipantType.TargetSim)),
       enabled_by_default=True), 
     'relative_sim':TunableEnumEntry(description='\n            The sim that will be the relative sim that the filter will\n            check against for relative checks such as relationships or\n            household ids.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'sim_filter':TunablePackSafeReference(manager=services.get_instance_manager(sims4.resources.Types.SIM_FILTER)), 
     'duration_available':TunableSimMinute(description='\n            The duration from now that will be used for the start\n            and end time of the filter request.\n            ',
       default=120,
       minimum=0), 
     'threshold_matched':OptionalTunable(description='\n            If enabled, we will require the number of Sims that match the\n            filter pass the threshold requirement. Otherwise we require all\n            Sims that the filter runs on to match.\n            \n            This is useful if you only need one or a number of Sims to match\n            the filter.\n            ',
       tunable=TunableThreshold(description='\n                A threshold of how many sims should match the filter.\n                ',
       value=TunableRange(description='\n                    The number that describes the threshold for how many Sims\n                    should match the filter.\n                    ',
       tunable_type=int,
       default=1,
       minimum=0))), 
     'in_current_zone':Tunable(description='\n            If enabled, check if any matching Sims are in the current zone.\n            ',
       tunable_type=bool,
       default=False)}

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self._duration_available = clock.interval_in_sim_minutes(self.duration_available)

    def get_expected_args(self):
        expected_args = {}
        if self.filter_target is not None:
            expected_args['filter_targets'] = self.filter_target
        expected_args['relative_sims'] = self.relative_sim
        return expected_args

    def _get_sim_filter_gsi_name(self, sim_match_filter_request_type, sim_info=None):
        if sim_match_filter_request_type == True:
            return 'Request to check if {} matches filter from {}'.format(sim_info, self)
        return 'Tuning: {}'.format(self)

    @cached_test
    def __call__(self, filter_targets=None, relative_sims=None):
        if not relative_sims:
            clients = [client for client in services.client_manager().values()]
            if not clients:
                return TestResult(False, 'FilterTest: No clients found when trying to get the active sim.', tooltip=(self.tooltip))
        else:
            client = clients[0]
            relative_sim = client.active_sim
            if not relative_sim:
                return TestResult(False, 'FilterTest: No active sim found.', tooltip=(self.tooltip))
                relative_sims = {relative_sim.sim_info}
            else:
                matches = 0
                zone_id = services.current_zone_id()
                if filter_targets is not None:
                    for filter_target in filter_targets:
                        if self.in_current_zone:
                            if filter_target.sim_info.zone_id != zone_id:
                                continue
                        for relative_sim_info in relative_sims:
                            matched = services.sim_filter_service().does_sim_match_filter((filter_target.id), sim_filter=(self.sim_filter),
                              requesting_sim_info=relative_sim_info,
                              household_id=(relative_sim_info.household_id),
                              gsi_source_fn=(lambda: self._get_sim_filter_gsi_name(True, sim_info=relative_sim_info)))
                            if not matched:
                                return TestResult(False, 'FilterTest: Sim {} (id {}) does not match filter {}.', (filter_target.full_name),
                                  (filter_target.id), (self.sim_filter.__name__), tooltip=(self.tooltip))
                                if self.threshold_matched is not None:
                                    matches = matches + 1 if matched else matches

                else:
                    for relative_sim_info in relative_sims:
                        results = services.sim_filter_service().submit_filter((self.sim_filter), None,
                          requesting_sim_info=relative_sim_info,
                          allow_yielding=False,
                          start_time=(services.time_service().sim_now),
                          end_time=(services.time_service().sim_now + self._duration_available),
                          household_id=(relative_sim_info.household_id),
                          gsi_source_fn=(lambda: self._get_sim_filter_gsi_name(False)))
                        if not results:
                            return TestResult(False, 'FilterTest: Sim {} (id {}) does not match filter {}.', (relative_sim_info.full_name),
                              (relative_sim_info.id), (self.sim_filter.__name__), tooltip=(self.tooltip))
                            if self.in_current_zone:
                                results = [result for result in results if result.sim_info.zone_id == zone_id]
                            if self.threshold_matched is not None:
                                matches += len(results)

            if self.threshold_matched is not None:
                return self.threshold_matched.compare(matches) or TestResult(False, 'FilterTest: {} Sims matched the filter {} but did not meet the threshold {}', matches, (self.sim_filter.__name__), (self.threshold_matched), tooltip=(self.tooltip))
        return TestResult.TRUE


class _AppropriatenessTestBase(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'participant': TunableEnumEntry(description='\n            The subject of this situation data test.\n            ',
                      tunable_type=ParticipantType,
                      default=(ParticipantType.Actor))}
    __slots__ = ('participant', 'is_appropriate')

    def get_expected_args(self):
        return {'test_targets':self.participant, 
         'affordance':ParticipantType.Affordance}

    @cached_test
    def __call__(self, test_targets=None, affordance=None):
        if not test_targets:
            return TestResult(False, 'AppropriatenessTest: There are no participants.', tooltip=(self.tooltip))
        else:
            return affordance or TestResult(False, 'AppropriatenessTest: There is no affordance.', tooltip=(self.tooltip))
        for target in test_targets:
            if target.is_sim:
                if target.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS) is None:
                    return TestResult(False, 'AppropriatenessTest: {} is not an instantiated sim.', target, tooltip=(self.tooltip))
                target = target.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
            if target.Buffs.is_appropriate(affordance.appropriateness_tags) != self.is_appropriate:
                return TestResult(False, 'AppropriatenessTest: This interaction is not appropriate for Sim of id {}. appropriateness tags {}.', (target.id), (affordance.appropriateness_tags), tooltip=(self.tooltip))

        return TestResult.TRUE


class AppropriatenessTest(_AppropriatenessTestBase):
    __slots__ = ()

    @classproperty
    def is_appropriate(self):
        return True


class InappropriatenessTest(_AppropriatenessTestBase):
    __slots__ = ()

    @classproperty
    def is_appropriate(self):
        return False


class SimInfoGameplayOptionsTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'participant':TunableEnumEntry(description='\n            The subject of the test.\n            ',
       tunable_type=ParticipantTypeSingleSim,
       default=ParticipantTypeSingleSim.Actor), 
     'gameplay_option':TunableEnumEntry(description='\n            The gameplay option to test. This test will pass if this option is\n            set.\n            ',
       tunable_type=SimInfoGameplayOptions,
       default=SimInfoGameplayOptions.ALLOW_FAME), 
     'invert':Tunable(description='\n            If enabled, requires the option to be unset for the test to pass.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'test_targets': self.participant}

    @cached_test
    def __call__--- This code section failed: ---

 L.1737         0  LOAD_GLOBAL              next
                2  LOAD_GLOBAL              iter
                4  LOAD_FAST                'test_targets'
                6  CALL_FUNCTION_1       1  '1 positional argument'
                8  CALL_FUNCTION_1       1  '1 positional argument'
               10  STORE_FAST               'subject'

 L.1738        12  LOAD_GLOBAL              is_required_pack_installed
               14  LOAD_FAST                'self'
               16  LOAD_ATTR                gameplay_option
               18  CALL_FUNCTION_1       1  '1 positional argument'
               20  POP_JUMP_IF_TRUE     40  'to 40'

 L.1739        22  LOAD_GLOBAL              TestResult
               24  LOAD_CONST               False
               26  LOAD_STR                 '{} option missing required pack'
               28  LOAD_FAST                'self'
               30  LOAD_ATTR                gameplay_option
               32  LOAD_FAST                'self'
               34  LOAD_ATTR                tooltip
               36  CALL_FUNCTION_4       4  '4 positional arguments'
               38  RETURN_VALUE     
             40_0  COME_FROM            20  '20'

 L.1741        40  LOAD_FAST                'subject'
               42  LOAD_ATTR                sim_info
               44  LOAD_METHOD              get_gameplay_option
               46  LOAD_FAST                'self'
               48  LOAD_ATTR                gameplay_option
               50  CALL_METHOD_1         1  '1 positional argument'
               52  STORE_FAST               'option_result'

 L.1742        54  LOAD_FAST                'self'
               56  LOAD_ATTR                invert
               58  POP_JUMP_IF_TRUE     64  'to 64'
               60  LOAD_FAST                'option_result'
               62  POP_JUMP_IF_TRUE     74  'to 74'
             64_0  COME_FROM            58  '58'
               64  LOAD_FAST                'self'
               66  LOAD_ATTR                invert
               68  POP_JUMP_IF_FALSE    80  'to 80'
               70  LOAD_FAST                'option_result'
               72  POP_JUMP_IF_TRUE     80  'to 80'
             74_0  COME_FROM            62  '62'

 L.1743        74  LOAD_GLOBAL              TestResult
               76  LOAD_ATTR                TRUE
               78  RETURN_VALUE     
             80_0  COME_FROM            72  '72'
             80_1  COME_FROM            68  '68'

 L.1745        80  LOAD_GLOBAL              TestResult
               82  LOAD_CONST               False
               84  LOAD_STR                 "{}'s option {} is set to {}"
               86  LOAD_FAST                'subject'
               88  LOAD_FAST                'self'
               90  LOAD_ATTR                gameplay_option
               92  LOAD_FAST                'option_result'
               94  LOAD_FAST                'self'
               96  LOAD_ATTR                tooltip
               98  LOAD_CONST               ('tooltip',)
              100  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
              102  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 102


class SkinToneTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The subject of the test.\n            ',
       tunable_type=ParticipantTypeActorTargetSim,
       default=ParticipantTypeActorTargetSim.Actor), 
     'skin_tones':TunableList(description="\n            The Sim's skin tone must be one of the specified skin tones.\n            ",
       tunable=TunableSkinTone(description='\n                A skin tone to test.\n                ',
       pack_safe=True),
       minlength=1), 
     'invert':Tunable(description='\n            If true, invert the result of this test.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'subject': self.subject}

    @cached_test
    def __call__(self, subject=None):
        subject = next(iter(subject))
        if subject.skin_tone in self.skin_tones:
            if self.invert:
                return TestResult(False, "{}'s skin tone is {} which is one of the following: {}, but invert is checked", subject,
                  (subject.skin_tone), (', '.join((str(skin_tone) for skin_tone in self.skin_tones))), tooltip=(self.tooltip))
            return TestResult.TRUE
        if self.invert:
            return TestResult.TRUE
        return TestResult(False, "{}'s skin tone is {} which is not one of the following: {}", subject,
          (subject.skin_tone), (', '.join((str(skin_tone) for skin_tone in self.skin_tones))), tooltip=(self.tooltip))


class BirthdayTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'participant':TunableEnumEntry(description='\n            The participant against which to run this birthday test.\n            ',
       tunable_type=ParticipantTypeSingleSim,
       default=ParticipantTypeSingleSim.Actor), 
     'days_until_birthday':TunableRange(description="\n            Check if days-until-sim's-birthday is inside this range. Set this\n            to 0 if we want to check if today is sim's birthday. \n            ",
       tunable_type=int,
       minimum=0,
       default=0), 
     'invert':Tunable(description='\n            If true, invert the result of this test.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'test_targets': self.participant}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            if target.days_until_ready_to_age() > self.days_until_birthday:
                if self.invert:
                    return TestResult.TRUE
                return TestResult(False, "It is not {}'s birthday.", target, tooltip=(self.tooltip))

        if self.invert:
            return TestResult(False, "Test inverted, it is {}'s birthday.", target, tooltip=(self.tooltip))
        return TestResult.TRUE


class DeadTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    test_events = (
     TestEvent.SimDeathTypeSet,)
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            Who or what to apply this test to.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'invert':Tunable(description='\n            If true, invert the result of this test.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            sim_info = services.sim_info_manager().get(target.sim_id)
            if not sim_info is None:
                if not sim_info.can_instantiate_sim or sim_info.death_type is not None and sim_info.death_type != DeathType.NONE:
                    if self.invert:
                        return TestResult(False, 'Sim {} is alive.', target, tooltip=(self.tooltip))
                return TestResult.TRUE

        return TestResult(False, 'No test target to test against.', tooltip=(self.tooltip))
