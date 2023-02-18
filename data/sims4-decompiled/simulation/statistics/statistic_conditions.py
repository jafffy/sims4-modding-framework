# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\statistics\statistic_conditions.py
# Compiled at: 2021-07-13 22:45:47
# Size of source mod 2**32: 79989 bytes

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
_ifstmts_jumpl ::= COME_FROM c_stmts JUMP_FORWARD . 
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
break ::= BREAK_LOOP . 
build_class ::= LOAD_BUILD_CLASS . mkfunc expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS . mkfunc expr expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS . mkfunc expr expr expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS . mkfunc expr expr expr expr CALL_FUNCTION_5
build_class ::= LOAD_BUILD_CLASS mkfunc . expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc . expr expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc . expr expr expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc . expr expr expr expr CALL_FUNCTION_5
build_class ::= LOAD_BUILD_CLASS mkfunc expr . CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr . expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr . expr expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr . expr expr expr CALL_FUNCTION_5
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr . CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr . expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr . expr expr CALL_FUNCTION_5
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr CALL_FUNCTION_3 . 
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
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
call ::= expr CALL_FUNCTION_0 . 
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
call ::= expr expr expr expr CALL_METHOD_3 . 
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
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_5
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr CALL_FUNCTION_EX_KW . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdef ::= build_class . store
classdef ::= build_class store . 
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3 . 
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4 . 
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_18
dict ::= kvlist_1 . 
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_ex_kw4 . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= list . 
expr ::= list_comp . 
expr ::= listcomp . 
expr ::= or . 
expr ::= unary_not . 
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
for_iter ::= \e__come_froms . FOR_ITER
for_iter ::= \e__come_froms FOR_ITER . 
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_or_c ::= JUMP_BACK . 
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
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_1 ::= expr expr BUILD_MAP_1 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
lc_body ::= expr LIST_APPEND . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
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
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
lstmt ::= stmt . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR MAKE_FUNCTION_1 . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
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
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
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
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP . STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME . RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME RETURN_VALUE . RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST . 
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
set ::= expr . expr BUILD_SET_2
set ::= expr expr . BUILD_SET_2
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= classdef . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= function_def_deco . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= return_closure . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1741       132  LOAD_CONST               (None, None)
->               134  RETURN_VALUE     
from _collections import defaultdict
import math, operator
from date_and_time import MINUTES_PER_HOUR
from event_testing.test_events import TestEvent
from interactions import ParticipantType, ParticipantTypeActorTargetSim, ParticipantTypeSingle
from interactions.constraint_variants import TunableGeometricConstraintVariant
from interactions.constraints import Anywhere
from objects import HiddenReasonFlag
from objects.components.state import TunableStateValueReference, CommodityBasedObjectStateValue, ObjectStateMetaclass
from objects.slots import SlotType
from sims4.repr_utils import standard_repr
from sims4.tuning.tunable import Tunable, TunableEnumEntry, TunableVariant, TunableReference, TunableThreshold, TunableFactory, TunableTuple, TunableSimMinute, HasTunableFactory, AutoFactoryInit, TunableSet, OptionalTunable, TunableList, TunableMapping, TunableEnumFlags, TunablePackSafeReference
from statistics.mood import Mood
from world.daytime_state_change import DaytimeStateChange
import alarms, clock, date_and_time, enum, services, sims4.log, sims4.math, sims4.resources
logger = sims4.log.Logger('Condition')

class Condition:
    __slots__ = ('_satisfied', '_handle', '_owner', 'si_callback')

    def __init__(self, exit_action=None, interaction=None, situation=None):
        self._satisfied = False
        self._handle = None
        self._owner = None
        self.si_callback = None

    def _satisfy(self, *_):
        if not self._satisfied:
            self._satisfied = True
            if not self.si_callback:
                logger.callstack('Condition is missing si_callback: {}', self, level=(sims4.log.LEVEL_ERROR), owner='tingyul')
                return
            self.si_callback(self._handle)

    def _unsatisfy(self, *_):
        self._satisfied = False

    @property
    def satisfied(self):
        return self._satisfied

    def attach_to_owner(self, owner, callback):
        raise NotImplementedError

    def detach_from_owner(self, owner, exiting=False):
        raise NotImplementedError

    def get_time_until_satisfy(self, interaction):
        return (None, None, None)

    def _get_target_and_tracker(self, interaction, participant, stat):
        target = interaction.get_participant(participant)
        if target is None:
            return (None, None)
        return (
         target, target.get_tracker(stat))

    def get_time_for_stat_satisfaction(self, interaction, subject, linked_stat, state_range):
        target, tracker = self._get_target_and_tracker(interaction, subject, linked_stat)
        if target is None or tracker is None:
            return (None, None, None)
        override_min_max_stats = interaction.progress_bar_enabled.override_min_max_values
        blacklist_statistics = interaction.progress_bar_enabled.blacklist_statistics
        best_time = None
        best_percent = None
        best_rate_of_change = None
        if tracker is not None:
            current_value = tracker.get_user_value(linked_stat)
            stat_op_list = interaction.instance_statistic_operations_gen()
            for stat_op in stat_op_list:
                if stat_op.stat is linked_stat:
                    if not stat_op.test_resolver(interaction.get_resolver()):
                        continue
                    elif blacklist_statistics:
                        if linked_stat in blacklist_statistics:
                            return (None, None, None)
                        elif override_min_max_stats is not None:
                            if override_min_max_stats.statistic is stat_op.stat:
                                override_stat_values = True
                            else:
                                override_stat_values = False
                            stat_instance = tracker.get_statistic(stat_op.stat)
                            if stat_instance is None:
                                continue
                            if stat_instance.continuous:
                                rate_change = stat_instance.get_change_rate()
                        else:
                            interval = stat_op._get_interval(interaction)
                            if not interval:
                                continue
                            rate_change = stat_op.get_value() / interval
                        if rate_change > 0:
                            if state_range is not None:
                                upper_bound = state_range.lower_bound
                            else:
                                upper_bound = self.threshold.value
                            lower_bound = linked_stat.min_value
                        else:
                            if state_range is not None:
                                lower_bound = state_range.upper_bound
                            else:
                                lower_bound = self.threshold.value
                            upper_bound = linked_stat.max_value
                        if override_stat_values:
                            if override_min_max_stats.min_value is not None:
                                lower_bound = override_min_max_stats.min_value
                            if override_min_max_stats.max_value is not None:
                                upper_bound = override_min_max_stats.max_value
                        if rate_change > 0:
                            threshold = upper_bound
                            denominator = threshold - lower_bound
                            percent = abs((current_value - lower_bound) / denominator) if denominator else 0
                    else:
                        threshold = lower_bound
                        denominator = threshold - upper_bound
                        percent = abs((current_value + denominator) / denominator) if denominator else 0
                    if rate_change:
                        if not denominator:
                            continue
                        time = (threshold - current_value) / rate_change
                        rate_of_change = abs((1 - percent) / time if time != 0 else 0)
                        if best_time is None or time < best_time:
                            best_time = time
                            best_percent = percent
                            best_rate_of_change = rate_of_change

        return (
         best_time, best_percent, best_rate_of_change)


class StatisticCondition(Condition):
    __slots__ = ('who', 'stat', 'threshold', 'absolute', '_unsatisfy_handle')

    def __init__(self, who=None, stat=None, threshold=None, absolute=False, **kwargs):
        (super().__init__)(**kwargs)
        self.who = who
        self.stat = stat
        self.threshold = threshold
        self.absolute = absolute
        self._unsatisfy_handle = None

    def __str__(self):
        return standard_repr(self, '{}.{} {}'.format(self.who.name, self.stat.__name__, self.threshold))

    def create_threshold(self, tracker):
        threshold = sims4.math.Threshold()
        threshold.comparison = self.threshold.comparison
        if self.absolute:
            cur_val = 0
        else:
            cur_val = tracker.get_value((self.stat), add=True)
        if not self.absolute:
            if self.threshold.comparison is operator.ge:
                pass
            if self.threshold.comparison is operator.le:
                pass
        elif self.threshold.comparison is operator.ge:
            threshold.value = min([cur_val + self.threshold.value, self.stat.max_value])
        else:
            if self.threshold.comparison is operator.le:
                threshold.value = max([cur_val + self.threshold.value, self.stat.min_value])
            else:
                raise NotImplementedError
        return threshold

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        _, tracker = self._get_target_and_tracker(owner, self.who, self.stat)
        if tracker is None:
            self._satisfy()
            return (None, None)
        threshold = self.create_threshold(tracker)
        value = tracker.get_value(self.stat)
        if threshold.compare(value):
            self._satisfy()
        self._handle = tracker.create_and_add_listener(self.stat, threshold, self._satisfy)
        self._unsatisfy_handle = tracker.create_and_add_listener(self.stat, threshold.inverse(), self._unsatisfy)
        return (None, None)

    def detach_from_owner(self, owner, exiting=False):
        self._owner = None
        self.si_callback = None
        _, tracker = self._get_target_and_tracker(owner, self.who, self.stat)
        if tracker is None:
            return
        if self._handle is not None:
            tracker.remove_listener(self._handle)
            self._handle = None
        if self._unsatisfy_handle is not None:
            tracker.remove_listener(self._unsatisfy_handle)
            self._unsatisfy_handle = None

    def get_time_until_satisfy(self, interaction):
        return self.get_time_for_stat_satisfaction(interaction, self.who, self.stat, None)


class StateCondition(Condition):

    def __init__(self, subject, state, **kwargs):
        (super().__init__)(**kwargs)
        self._subject = subject
        self._state = state

    def __str__(self):
        return 'State {} on {}'.format(self._state, self._subject)

    def _on_owner_state_changed(self, owner, state, old_value, new_value):
        if state is self._state.state:
            if self._state is new_value:
                self._satisfy(None)

    def attach_to_owner(self, owner, callback):
        subject = owner.get_participant(self._subject)
        if subject is not None:
            if subject.state_component:
                self.si_callback = callback
                subject.add_state_changed_callback(self._on_owner_state_changed)
        return (None, None)

    def detach_from_owner(self, owner, **kwargs):
        subject = owner.get_participant(self._subject)
        if subject is not None:
            if subject.state_component:
                subject.remove_state_changed_callback(self._on_owner_state_changed)
        self.si_callback = None

    def get_time_until_satisfy(self, interaction):
        if self._state.state.linked_stat is None:
            return (None, None, None)
        return self.get_time_for_stat_satisfaction(interaction, self._subject, self._state.state.linked_stat, self._state.range)


class TimeBasedCondition(Condition):
    __slots__ = '_interval'

    def __init__(self, interval_in_sim_minutes=0, **kwargs):
        (super().__init__)(**kwargs)
        self._interval = interval_in_sim_minutes

    def __str__(self):
        return 'Time Interval: {}'.format(self._interval)

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        time_span = clock.interval_in_sim_minutes(self._interval)
        alarm_owner = owner.sim if hasattr(owner, 'sim') else owner
        self._handle = alarms.add_alarm(alarm_owner, time_span, self._satisfy)
        return (
         None, self._handle)

    def detach_from_owner(self, _, exiting=False):
        if self._handle is not None:
            alarms.cancel_alarm(self._handle)
            self._handle = None
        self._owner = None
        self.si_callback = None

    def get_time_until_satisfy(self, interaction):
        rounded_interval = math.floor(self._interval)
        if rounded_interval == 0:
            return (None, None, None)
        elif self._satisfied:
            remaining_time = 0
        else:
            remaining_time = math.floor(self._handle.get_remaining_time().in_minutes())
        percent_done = (rounded_interval - remaining_time) / rounded_interval
        change_rate = 0
        if self._interval != 0:
            change_rate = 1 / self._interval
        return (
         self._interval, percent_done, change_rate)


class EventBasedCondition(Condition):
    __slots__ = '_event_type'

    def __init__(self, event_type, **kwargs):
        (super().__init__)(**kwargs)
        self._event_type = event_type

    def __str__(self):
        return 'Event {}'.format(self._event_type)

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        self._handle = services.get_event_manager().register(self, (self._event_type,))
        return (
         None, self._handle)

    def handle_event(self, sim_info, event, resolver):
        self._satisfy(event)

    def detach_from_owner(self, _, exiting=False):
        services.get_event_manager().unregister(self, (self._event_type,))
        self._handle = None
        self._owner = None
        self.si_callback = None


class InUseCondition(HasTunableFactory, AutoFactoryInit, Condition):
    FACTORY_TUNABLES = {'description':'\n            A condition that is satisfied when an object is no longer in use,\n            optionally specifying an affordance that the user of the object must\n            be running.\n            ', 
     'participant':TunableEnumEntry(description='\n            The participant of the interaction used to fetch the users against\n            which the condition test is run.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Object), 
     'affordance':OptionalTunable(description='\n            If specified, then the condition is satisfied if no user of the\n            specified object is running this affordance. If unspecified, will\n            be satisfied if object is no longer in use by any Sim.\n            ',
       tunable=TunableReference(description='\n                Only looking to see if this interaction is running and stopping\n                when this interaction is no longer running\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
       class_restrictions='SuperInteraction'),
       disabled_name='Unspecified',
       enabled_name='Specific_Interaction')}

    def __str__(self):
        return 'In Use: {}'.format(self.affordance)

    def _get_use_list_obj(self):
        obj = self._owner.get_participant(self.participant)
        if obj.is_part:
            obj = obj.part_owner
        return obj

    def _on_use_list_changed(self, **kwargs):
        obj = self._get_use_list_obj()
        if obj is not None:
            if self.affordance is None:
                if obj.in_use:
                    return
            else:
                for user in obj.get_users(sims_only=True):
                    for si in user.si_state:
                        if si.get_interaction_type() is self.affordance:
                            return

        self._satisfy(None)

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        obj = self._get_use_list_obj()
        if obj is not None:
            obj.register_on_use_list_changed(self._on_use_list_changed)
        return (None, None)

    def detach_from_owner(self, *_, **__):
        obj = self._get_use_list_obj()
        if obj is not None:
            obj.unregister_on_use_list_changed(self._on_use_list_changed)
        self._owner = None
        self.si_callback = None


class GroupBasedCondition(Condition, HasTunableFactory):
    FACTORY_TUNABLES = {'threshold': TunableThreshold(description='Threshold tested against group size.')}

    def __init__(self, threshold, **kwargs):
        (super().__init__)(**kwargs)
        self._threshold = threshold
        self._social_group = None
        self._previously_satisfied = self._threshold.compare(0)

    def __str__(self):
        return 'Group Threshold: {}'.format(self._threshold)

    def _group_changed(self, group):
        if self._threshold.compare(group.get_active_sim_count()):
            self._previously_satisfied = self._previously_satisfied or True
            self._satisfy()
        else:
            self._previously_satisfied = False

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        social_group_owner = owner.super_interaction
        self._social_group = social_group_owner.social_group
        self._social_group.on_group_changed.append(self._group_changed)
        self._group_changed(self._social_group)
        return (None, None)

    def detach_from_owner(self, *_, **__):
        if self._social_group is not None:
            if self._group_changed in self._social_group.on_group_changed:
                self._social_group.on_group_changed.remove(self._group_changed)
            self._social_group = None
        self._owner = None
        self.si_callback = None


class ConstraintBasedCondition(HasTunableFactory, AutoFactoryInit, Condition):
    FACTORY_TUNABLES = {'constraints_to_use': OptionalTunable(description='\n            If enabled, this condition will use custom constraints. If disabled,\n            it will use the geometric constraints of the interaction on which\n            this is tuned.\n            ',
                             tunable=TunableTuple(relative_participant=TunableEnumEntry(description="\n                    The participant that constraints will be generated\n                    relative to. For performance reasons, it is best to choose\n                    a participant that won't be moving during this interaction \n                    (usually the actor) since constraints must be recalculated\n                    whenever this participant moves.\n                    ",
                             tunable_type=ParticipantTypeSingle,
                             default=(ParticipantTypeSingle.Object)),
                             _constraints=TunableMapping(description='\n                    Mapping between a participant and a set of constraints. The\n                    participant is what we check constraints against. This\n                    participant should rarely be the same as the relative\n                    participant since most constraints would have no meaning (an\n                    object is always within a radius of itself, etc).Constraints\n                    currently only supports geometry constraints.\n                    ',
                             key_name='constrained_participant',
                             value_name='constraints',
                             key_type=TunableEnumEntry(tunable_type=ParticipantTypeSingle,
                             default=(ParticipantTypeSingle.Actor)),
                             value_type=TunableList(tunable=TunableGeometricConstraintVariant(constraint_locked_args={'multi_surface': True}, circle_locked_args={'require_los': False},
                             disabled_constraints={
                            'spawn_points', 'current_position'}),
                             minlength=1),
                             minlength=1)),
                             disabled_name='reuse_interaction_constraints',
                             enabled_name='use_custom_constraints')}

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self._tuned_constraints = None
        self._constraints = dict()
        self._relative_object = None

    def __str__(self):
        return 'Constraint: {}, Relative Object: {}'.format(self._constraints, self._relative_object)

    def generate_constraints(self, participant=None):
        for participant, constraints in self._tuned_constraints.items():
            constraint = Anywhere()
            for tuned_constraint in constraints:
                constraint = constraint.intersect(tuned_constraint.create_constraint(None, target=(self._relative_object), target_position=(self._relative_object.position)))

            self._constraints[participant] = constraint

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        if self.constraints_to_use:
            self._tuned_constraints = defaultdict()
            for participant, constraint_list in self.constraints_to_use._constraints.items():
                constrained_object = owner.get_participant(participant)
                self._tuned_constraints[constrained_object] = constraint_list

            self._relative_object = owner.get_participant(self.constraints_to_use.relative_participant)
        else:
            self._tuned_constraints = dict()
            for participant, constraints in owner._constraints.items():
                constrained_object = owner.get_participant(participant)
                self._tuned_constraints[constrained_object] = [constraint.value for constraint in constraints[0]]

            self._relative_object = owner.get_participant(owner._constraints_actor)
        self.generate_constraints()
        for participant, _ in self._constraints.items():
            self._check_constraint(participant)
            participant.register_on_location_changed(self._check_constraint)

        self._relative_object.register_on_location_changed(self._check_constraint)
        return (None, None)

    def _check_constraint(self, moved_participant, *_, **__):
        if moved_participant is self._relative_object:
            self.generate_constraints()
            participants_to_check = self._constraints.keys()
        else:
            participants_to_check = [
             moved_participant]
        for participant in participants_to_check:
            constraint = self._constraints[participant]
            if constraint.geometry is not None:
                if not constraint.geometry.test_transform(participant.transform):
                    self._satisfy()
                    return
            self._unsatisfy()

    def detach_from_owner(self, *_, **__):
        self._relative_object.unregister_on_location_changed(self._check_constraint)
        for participant, _ in self._constraints.items():
            participant.unregister_on_location_changed(self._check_constraint)

        self._owner = None
        self.si_callback = None


class TunableCondition(TunableVariant):

    def __init__(self, *args, **kwargs):
        (super().__init__)(args, stat_based=TunableStatisticCondition(description='A condition based on the status of a statistic.'), 
         state_based=TunableStateCondition(description='A condition based on the state of an object.'), 
         time_based=TunableTimeRangeCondition(description='The minimum and maximum amount of time required to satisfy this condition.'), 
         event_based=TunableEventBasedCondition(description='A condition that is satisfied by some event'), 
         career_based=TunableCareerCondition(description='A condition that is satisfied by career data'), 
         wakeup_time_based=TunableWakeupCondition(description='A condition that is satisfied by being close to the schedule time for the sims career'), 
         sim_spawn_based=TunableSimSpawnCondition(description='A condition that is satisfied when a Sim spawns in the world.'), 
         group_based=GroupBasedCondition.TunableFactory(), 
         daytime_state_change_based=DaytimeStateChangeCondition.TunableFactory(), 
         in_use_based=InUseCondition.TunableFactory(), 
         mood_based=MoodBasedCondition.TunableFactory(), 
         object_relationship_based=ObjectRelationshipCondition.TunableFactory(), 
         buff_based=BuffCondition.TunableFactory(), 
         child_based=ObjectChildrenChangedCondition.TunableFactory(), 
         constraint_based=ConstraintBasedCondition.TunableFactory(), 
         rabbit_hole_based=TunableRabbitHoleExitCondition(), 
         hidden_or_shown=HiddenOrShownCondition.TunableFactory(), 
         default='stat_based', **kwargs)


class TunableTimeRangeCondition(TunableFactory):

    @staticmethod
    def factory(min_time, max_time, interaction=None, **kwargs):
        import random
        if min_time is None:
            time_in_sim_minutes = max_time
        else:
            if max_time is None:
                time_in_sim_minutes = min_time
            else:
                if min_time == max_time:
                    time_in_sim_minutes = min_time
                else:
                    time_in_sim_minutes = random.uniform(min_time, max_time)
        return TimeBasedCondition(time_in_sim_minutes, interaction=interaction, **kwargs)

    @staticmethod
    def _on_tunable_loaded_callback(cls, fields, source, *, min_time, max_time):
        pass

    FACTORY_TYPE = factory

    def __init__(self, description='A time range in Sim minutes for this condition to be satisfied.', **kwargs):
        (super().__init__)(description=description, verify_tunable_callback=self._on_tunable_loaded_callback, 
         min_time=TunableSimMinute(description='\n                             Minimum amount of time (in sim minutes) for this condition to be satisfied.\n                             ',
  default=1), 
         max_time=TunableSimMinute(description='\n                             Maximum amount of time (in sim minutes) for this condition to be satisfied.\n                             ',
  default=None), **kwargs)


class RabbitHoleTimeBasedCondition(Condition):

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self._duration = None

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        self._duration = services.get_rabbit_hole_service().get_time_for_head_rabbit_hole(owner.sim.id).in_minutes()

    def detach_from_owner(self, _, exiting=False):
        self._handle = None
        self._owner = None
        self.si_callback = None

    def get_time_until_satisfy(self, interaction):
        time_in_rabbit_hole = services.get_rabbit_hole_service().get_time_for_head_rabbit_hole(self._owner.sim.id)
        if time_in_rabbit_hole is None:
            logger.error('Rabbit hole time condition is tuned on affordance ({}) but rabbit hole service cannot generate a time for it', self._owner)
            return (None, None, None)
        remaining_time = time_in_rabbit_hole.in_minutes()
        if remaining_time is None or self._duration is None:
            logger.error('Rabbit hole time condition is tuned on affordance but rabbit hole service cannot generate a time for it')
            return (None, None, None)
        percent_done = 1 - remaining_time / self._duration
        return (self._duration, percent_done, 1 / self._duration)


class TunableRabbitHoleExitCondition(TunableTimeRangeCondition):

    @staticmethod
    def factory(min_time, max_time, interaction, **kwargs):
        return RabbitHoleTimeBasedCondition()

    FACTORY_TYPE = factory

    def __init__(self, description='An exit condition for rabbithole interactions', **kwargs):
        (super().__init__)(description=description, **kwargs)


class TunableStatisticCondition(TunableFactory):
    FACTORY_TYPE = StatisticCondition

    def __init__(self, description='Apply an operation to a statistic.', **kwargs):
        (super().__init__)(who=TunableEnumEntry(ParticipantType, (ParticipantType.Actor), description='Who or what to apply this test to'), stat=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)), description='The commodity we are gaining.'), 
         threshold=TunableThreshold(description='A commodity value and comparison that defines the exit condition hits (or hit commodity.maximum).'), 
         absolute=Tunable(bool, True, description="True = treat the threshold value as an absolute commodity value.  Otherwise, it is relative to the Sim's start value."), **kwargs)


class TunableStateCondition(TunableFactory):

    @staticmethod
    def factory(subject, state, **kwargs):
        if isinstance(state, ObjectStateMetaclass):
            return StateCondition(subject, state, **kwargs)
        else:
            linked_stat = state.state.state.linked_stat
            if state.boundary:
                threshold = sims4.math.Threshold(state.state.range.upper_bound, operator.ge)
            else:
                threshold = sims4.math.Threshold(state.state.range.lower_bound, operator.le)
        return StatisticCondition(subject, linked_stat, threshold, absolute=True)

    FACTORY_TYPE = factory

    def __init__(self, description='A condition to determine if an object is in a particular state.', **kwargs):
        (super().__init__)(subject=TunableEnumEntry(ParticipantType, (ParticipantType.Object), description='The subject to check the condition on.'), state=TunableVariant(description='The state to check for.', on_trigger=TunableStateValueReference(description='Satisfy the condition when this state is triggered.'),
  on_boundary=TunableTuple(description='Satisfy the condition when a boundary of this stat-based state is reached', state=TunableStateValueReference(class_restrictions=CommodityBasedObjectStateValue, description='The state required to satisfy the condition'),
  boundary=TunableVariant(description='The boundary required to be reached for the condition to be satisfied.', locked_args={'upper':True, 
 'lower':False},
  default='upper')),
  default='on_trigger'), **kwargs)


class TunableEventBasedCondition(TunableFactory):

    @staticmethod
    def factory(event_to_listen_for, **kwargs):
        return EventBasedCondition(event_to_listen_for, **kwargs)

    FACTORY_TYPE = factory

    def __init__(self, description='A condition that is satisfied by some event', **kwargs):
        (super().__init__)(description=description, event_to_listen_for=TunableEnumEntry(TestEvent, (TestEvent.Invalid), description='Event that this exit condition should listen for '), **kwargs)


class TunableCareerCondition(TunableFactory):

    @staticmethod
    def factory(*args, **kwargs):
        return CareerCondition(*args, **kwargs)

    FACTORY_TYPE = factory

    def __init__(self, description='A Career Condition to cause an interaction to exit.', **kwargs):
        (super().__init__)(description=description, who=TunableEnumEntry(ParticipantType, (ParticipantType.Actor), description='Who or what to apply this test to'), **kwargs)


class CareerCondition(Condition):
    __slots__ = ('who', '_career')

    def __init__(self, who=None, **kwargs):
        (super().__init__)(**kwargs)
        self.who = who
        self._career = None

    def __str__(self):
        return 'Career: {}'.format(self.who)

    def handle_event(self, sim_info, event, resolver):
        if event == TestEvent.CareerStayLate:
            if sim_info is self._owner.sim.sim_info:
                alarms.cancel_alarm(self._handle)
                self._schedule_alarm(self._career)

    def _schedule_alarm(self, career):
        time_to_work_end = career.time_until_end_of_work()
        self._handle = alarms.add_alarm(self._owner.sim.sim_info, time_to_work_end, self._satisfy)

    def attach_to_owner(self, owner, callback):
        self.si_callback = callback
        self._career = self._get_target_career(owner)
        self._owner = owner
        self._schedule_alarm(self._career)
        services.get_event_manager().register_single_event(self, TestEvent.CareerStayLate)
        return (
         None, self._handle)

    def detach_from_owner(self, owner, exiting=False):
        if self._handle is not None:
            alarms.cancel_alarm(self._handle)
            self._handle = None
        self.si_callback = None
        services.get_event_manager().unregister_single_event(self, TestEvent.CareerStayLate)

    def _get_target_career(self, interaction, exiting=False):
        target_sim = interaction.get_participant(self.who)
        if exiting:
            if target_sim is None:
                return
        target_career = interaction.get_career()
        return target_career

    def get_time_until_satisfy(self, interaction):
        career = self._get_target_career(interaction)
        if career is None:
            return (None, None, None)
        time_to_work_end = career.time_until_end_of_work().in_minutes()
        time_worked = career.get_hours_worked() * MINUTES_PER_HOUR
        total_time = time_worked + time_to_work_end
        if total_time == 0:
            return (None, None, None)
        percentage_done = time_worked / total_time
        rate = 1 / total_time
        return (time_to_work_end, percentage_done, rate)


class DaytimeStateChangeCondition(HasTunableFactory, AutoFactoryInit, TimeBasedCondition):
    FACTORY_TUNABLES = {'who':TunableEnumEntry(description="\n            The Sim who we're running this test on\n            ",
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     '_daytime':TunableEnumEntry(description='\n            The daytime state change (i.e. sunrise) that triggers the condition\n            ',
       tunable_type=DaytimeStateChange,
       default=DaytimeStateChange.Sunset)}

    def __str__(self):
        return 'DaytimeStateChange: {}, trigger on next {}'.format(self.who, self._daytime)

    def attach_to_owner(self, owner, callback):
        sim = owner.get_participant(self.who)
        if sim is None:
            return
        else:
            region_instance = services.current_region()
            if region_instance is None:
                logger.error('region instance is unexpectedly None')
                return
                state_change_time = None
                if self._daytime == DaytimeStateChange.Sunrise:
                    state_change_time = region_instance.get_sunrise_time()
            elif self._daytime == DaytimeStateChange.Sunset:
                state_change_time = region_instance.get_sunset_time()
            else:
                logger.error('Unhandled case for DaytimeStateChange value: {}', self._daytime)
                return
        time_span = services.game_clock_service().now().time_till_next_day_time(state_change_time)
        self._interval = time_span.in_minutes()
        super().attach_to_owner(owner, callback)


class TunableWakeupCondition(TunableFactory):

    @staticmethod
    def factory(*args, **kwargs):
        return WakeupCondition(*args, **kwargs)

    FACTORY_TYPE = factory

    def __init__(self, description='A Tunable Condition that takes into account when the Sim needs to be up for their work schedule.', **kwargs):
        (super().__init__)(description=description, who=TunableEnumEntry(ParticipantType, (ParticipantType.Actor), description='Who or what to apply this test to'), 
         hours_prior_to_schedule_start=Tunable(float, 0, description='The number of hours prior to the schedule start to satisfy this condition.'), **kwargs)


class WakeupCondition(TimeBasedCondition):

    def __init__(self, who=None, hours_prior_to_schedule_start=0, **kwargs):
        (super().__init__)(*(0, ), **kwargs)
        self.who = who
        self.hours_prior_to_schedule_start = hours_prior_to_schedule_start

    def __str__(self):
        return 'Wakeup: {}, {} hours before schedule'.format(self.who, self.hours_prior_to_schedule_start)

    def attach_to_owner(self, owner, callback):
        sim = owner.get_participant(self.who)
        if sim is None:
            return
        offset_time = date_and_time.create_time_span(hours=(self.hours_prior_to_schedule_start))
        time_span_until_work_start_time = sim.get_time_until_next_wakeup(offset_time=offset_time)
        if time_span_until_work_start_time.in_ticks() <= 0:
            logger.error('Wakeup time is in the past.', owner='rez')
            time_span_until_work_start_time += date_and_time.create_time_span(days=1)
        self._interval = time_span_until_work_start_time.in_minutes()
        return super().attach_to_owner(owner, callback)


class SimSpawnCondition(Condition):

    def __init__(self, participant_type=None, **kwargs):
        (super().__init__)(**kwargs)
        self._participant_type = participant_type
        self._sim_id = None

    def __str__(self):
        return 'Sim Spawn: {}'.format(self._sim_id)

    def attach_to_owner(self, owner, callback):
        self.si_callback = callback
        self._sim_id = owner.get_participant(self._participant_type)
        if self._sim_id is not None and isinstance(self._sim_id, int):
            object_manager = services.object_manager()
            object_manager.add_sim_spawn_condition(self._sim_id, self._satisfy)
        else:
            logger.error('SimSpawnCondition: invalid sim id found {} with participant type {}', self._sim_id, self._participant_type)
        return (None, None)

    def detach_from_owner(self, owner, exiting=False):
        if self._sim_id is not None and isinstance(self._sim_id, int):
            object_manager = services.object_manager()
            object_manager.remove_sim_spawn_condition(self._sim_id, self._satisfy)
        else:
            logger.error('SimSpawnCondition: invalid sim id found {} with participant type {}', self._sim_id, self._participant_type)
        self.si_callback = None


class TunableSimSpawnCondition(TunableFactory):

    @staticmethod
    def factory(*args, **kwargs):
        return SimSpawnCondition(*args, **kwargs)

    FACTORY_TYPE = factory

    def __init__(self, description='A Sim spawning Condition to cause an interaction to exit.', **kwargs):
        (super().__init__)(description=description, participant_type=TunableEnumEntry(ParticipantType, (ParticipantType.PickedItemId), description='Who or what to apply this test to'), **kwargs)


class MoodBasedCondition(HasTunableFactory, AutoFactoryInit, Condition):
    FACTORY_TUNABLES = {'description':'\n            A condition that is satisfied when a Sim enters a specific mood.\n            ', 
     'participant':TunableEnumEntry(description="\n            The Sim whose mood we're checking against.\n            ",
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'mood':Mood.TunableReference(description='\n            The mood that satisfies the condition.\n            ',
       needs_tuning=True), 
     'invert':Tunable(description='\n            If enabled, this condition will satisfy when the Sim is not in this\n            mood.\n            ',
       tunable_type=bool,
       default=False)}

    def __str__(self):
        if self.invert:
            return 'Not in Mood: {}'.format(self.mood)
        return 'Mood: {}'.format(self.mood)

    def _on_mood_changed(self, **kwargs):
        sim = self._owner.get_participant(self.participant)
        if sim is None:
            logger.error('MoodBasedCondition: Failed to find Sim for participant {} in {}', self.participant, self._owner)
            return
        else:
            in_mood = sim.get_mood() is self.mood
            if in_mood == self.invert:
                self._unsatisfy()
            else:
                self._satisfy()

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        sim = owner.get_participant(self.participant)
        sim.Buffs.on_mood_changed.append(self._on_mood_changed)
        self._on_mood_changed()
        return (None, None)

    def detach_from_owner(self, owner, exiting=False):
        sim = owner.get_participant(self.participant)
        if sim is not None:
            if self._on_mood_changed in sim.Buffs.on_mood_changed:
                sim.Buffs.on_mood_changed.remove(self._on_mood_changed)
        self._owner = None
        self.si_callback = None


class ObjectRelationshipCondition(HasTunableFactory, AutoFactoryInit, Condition):
    FACTORY_TUNABLES = {'description':'\n            A condition that is satisfied when a Sim reaches a specific object\n            relationship threshold.\n            ', 
     'sim':TunableEnumEntry(description="\n            The Sim whose object relationship we're checking.\n            ",
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'object':TunableEnumEntry(description="\n            The object whose object relationship we're checking.\n            ",
       tunable_type=ParticipantType,
       default=ParticipantType.Object), 
     'threshold':TunableThreshold(description='\n            The relationship threshold that will trigger this condition.\n            ')}

    def __init__(self, interaction=None, **kwargs):
        (super().__init__)(**kwargs)
        self._interaction = interaction

    def __str__(self):
        return 'Object Relationship: {} {}'.format(self.threshold.comparison, self.threshold.value)

    def _on_relationship_changed(self):
        sim = self._owner.get_participant(self.sim)
        obj = self._owner.get_participant(self.object)
        relationship_value = obj.objectrelationship_component.get_relationship_value(sim.id)
        if relationship_value is not None:
            if self.threshold.compare(relationship_value):
                self._satisfy()
                if self._interaction:
                    self._interaction._send_progress_bar_update_msg(1, 0, self._owner)
        if not self._satisfied:
            if self._interaction:
                initial_value = obj.objectrelationship_component.get_relationship_initial_value()
                denominator = self.threshold.value - initial_value
                if denominator != 0:
                    rate_change = relationship_value - initial_value / self.threshold.value - initial_value
                    self._owner._send_progress_bar_update_msg(rate_change / 100, 0, self._owner)

    def attach_to_owner(self, owner, callback):
        self._owner = owner
        self.si_callback = callback
        sim = owner.get_participant(self.sim)
        obj = self._owner.get_participant(self.object)
        if sim is None:
            logger.error('Trying to add a condition for {} to test object relationship, but the                           ParticipantType {} tuned for Sim is not valid.',
              (self._owner), sim, owner='tastle')
        else:
            if obj is None:
                logger.error('Trying to add a condition for {} to test object relationship, but the                           ParticipantType {} tuned for Object is not valid.',
                  (self._owner), obj, owner='tastle')
            else:
                if obj.objectrelationship_component is None:
                    logger.error('Trying to add a condition on interaction {} to test object relationship, but                           {} has no object relationship component.',
                      (self._owner), obj, owner='tastle')
                else:
                    obj.objectrelationship_component.add_relationship_changed_callback_for_sim_id(sim.sim_id, self._on_relationship_changed)
                    self._on_relationship_changed()
        return (None, None)

    def detach_from_owner(self, owner, exiting=False):
        sim = owner.get_participant(self.sim)
        obj = self._owner.get_participant(self.object)
        if sim is None or obj is None:
            return
        if obj.objectrelationship_component is not None:
            obj.objectrelationship_component.remove_relationship_changed_callback_for_sim_id(sim.sim_id, self._on_relationship_changed)
        self._owner = None
        self.si_callback = None


class BuffCondition(HasTunableFactory, AutoFactoryInit, Condition):

    class Timing(enum.Int):
        ON_ADD = 0
        ON_REMOVE = 1
        HAS_BUFF = 2
        NOT_HAS_BUFF = 3

    FACTORY_TUNABLES = {'description':'\n            A condition that is satisfied when a Sim gains or loses a buff.\n            ', 
     'participant':TunableEnumEntry(description="\n            The participant whose buffs we're checking.\n            ",
       tunable_type=ParticipantTypeActorTargetSim,
       default=ParticipantTypeActorTargetSim.Actor), 
     'buff':TunablePackSafeReference(description="\n            The buff we're checking.\n            ",
       manager=services.get_instance_manager(sims4.resources.Types.BUFF)), 
     'timing':TunableEnumEntry(description='\n            When the condition satisfies.\n            Choices:\n            ON_ADD: Only check the condition on the edge of the buff being\n            added.  This will not satisfy if you have the buff when the\n            interaction starts.\n            ON_REMOVE: Only check the condition on the edge of the buff being\n            removed.  This will not satisfy if you do not have the buff when\n            the interaction starts.\n            HAS_BUFF: Check for the buff existing at any time this condition\n            is active.  This will satisfy if you have the buff when the\n            interaction starts.\n            NOT_HAS_BUFF: Check for the buff not existing at any time this\n            condition is active.  This will satisfy if you do not have the buff\n            when the interaction starts.\n            ',
       tunable_type=Timing,
       default=Timing.ON_ADD)}

    def __str__(self):
        return 'BuffCondition: {} {} {}'.format(self.participant, self.buff, self.timing)

    def attach_to_owner(self, owner, callback):
        self.si_callback = callback
        self._owner = owner
        if self.buff is None:
            return (None, None)
            sim = self._owner.get_participant(self.participant)
            if self.timing == BuffCondition.Timing.HAS_BUFF:
                if sim.has_buff(self.buff):
                    self._satisfy()
        elif self.timing == BuffCondition.Timing.NOT_HAS_BUFF:
            if not sim.has_buff(self.buff):
                self._satisfy()
        self._enable_buff_watcher()
        return (None, None)

    def detach_from_owner(self, owner, exiting=False):
        if self.buff is not None:
            self._disable_buff_watcher()
        self._owner = None
        self.si_callback = None

    def _enable_buff_watcher(self):
        sim = self._owner.get_participant(self.participant)
        sim.Buffs.on_buff_added.append(self._on_buff_added)
        sim.Buffs.on_buff_removed.append(self._on_buff_removed)

    def _disable_buff_watcher(self):
        sim = self._owner.get_participant(self.participant)
        if self._on_buff_added in sim.Buffs.on_buff_added:
            sim.Buffs.on_buff_added.remove(self._on_buff_added)
        if self._on_buff_removed in sim.Buffs.on_buff_removed:
            sim.Buffs.on_buff_removed.remove(self._on_buff_removed)

    def _on_buff_added(self, buff_type, sim_id):
        if buff_type is self.buff:
            if self.timing == BuffCondition.Timing.ON_ADD or self.timing == BuffCondition.Timing.HAS_BUFF:
                self._satisfy()
            else:
                self._unsatisfy()

    def _on_buff_removed(self, buff_type, sim_id):
        if buff_type is self.buff:
            if self.timing == BuffCondition.Timing.ON_REMOVE or self.timing == BuffCondition.Timing.NOT_HAS_BUFF:
                self._satisfy()
            else:
                self._unsatisfy()


class ObjectChildrenChangedCondition(HasTunableFactory, AutoFactoryInit, Condition):
    CONDITION_SINGLE_CHILD = 'condition_single_child'
    CONDITION_CHILDREN_COUNT = 'condition_children_count'
    CONDITION_ALL_CHILDREN = 'condition_all_children'
    FACTORY_TUNABLES = {'participant':TunableEnumEntry(description='\n            The participant to be checked for a change in children.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Object), 
     'slot_types':OptionalTunable(description='\n            If enabled, we will restrict the contition tests against slots in\n            this list. Otherwise we will consider all slots.\n            ',
       tunable=TunableSet(description='\n                A list of slot types to restrict the test against.\n                ',
       tunable=SlotType.TunableReference(description=' \n                    The slot type to be tested against. This check will check to \n                    see if there is a child in the specified slot.\n                    '))), 
     'condition':TunableVariant(description='\n            The condition we want to test for.\n            ',
       single_child_changed=TunableTuple(description='\n                When a child is added to the specified slot types, we\n                will pass the test.\n                ',
       negate=Tunable(description='\n                    If enabled, we will check for a child removed instead of\n                    added to the slot types. Otherwise, we check for a child\n                    added to the specified slot types.\n                    ',
       tunable_type=bool,
       default=False),
       locked_args={'condition_type': CONDITION_SINGLE_CHILD}),
       children_count=TunableTuple(description='\n                When the number of children in the specified slot types passes\n                the threshold, we will satisfy the condition.\n                ',
       threshold=TunableThreshold(description='\n                    The threshold against the number of children in the\n                    specified slot types.\n                    ',
       value=Tunable(description='\n                        The number of objects we expect to be in the specified\n                        slot types.\n                        ',
       tunable_type=int,
       default=0)),
       locked_args={'condition_type': CONDITION_CHILDREN_COUNT}),
       all_or_none=TunableTuple(description='\n                Satisfied when we run out of slots of the specified types.\n                ',
       negate=Tunable(description='\n                    If checked, we will satisfy when all the slots are empty.\n                    Otherwise we satisfy when all slots are filled.\n                    ',
       tunable_type=bool,
       default=False),
       locked_args={'condition_type': CONDITION_ALL_CHILDREN}),
       default='single_child_changed')}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._parent_object_ref = None

    def attach_to_owner(self, owner, callback):
        self.si_callback = callback
        self._owner = owner
        parent = self._owner.get_participant(self.participant)
        if parent is None:
            return
        else:
            self._parent_object_ref = parent.ref()
            if self.condition.condition_type == ObjectChildrenChangedCondition.CONDITION_CHILDREN_COUNT:
                self._threshold_test(parent)
            else:
                if self.condition.condition_type == ObjectChildrenChangedCondition.CONDITION_ALL_CHILDREN:
                    self._all_slots_test(parent)
        parent.register_for_on_children_changed_callback(self._on_child_changed_callback)

    @property
    def parent_object(self):
        if self._parent_object_ref is not None:
            return self._parent_object_ref()

    def detach_from_owner(self, owner, exiting=False):
        self._owner = None
        self.si_callback = None
        parent = self.parent_object
        if parent is None:
            return
        parent.unregister_for_on_children_changed_callback(self._on_child_changed_callback)

    def _threshold_test(self, parent, *_, **__):
        runtime_slots = list(parent.get_runtime_slots_gen(slot_types=(self.slot_types), bone_name_hash=None))
        if self.condition.threshold.compare(sum([int(not runtime_slot.empty) for runtime_slot in runtime_slots])):
            self._satisfy()
        else:
            self._unsatisfy()

    def _all_slots_test(self, parent, *_, **__):
        runtime_slots = list(parent.get_runtime_slots_gen(slot_types=(self.slot_types), bone_name_hash=None))
        if not (self.condition.negate and all([runtime_slot.empty for runtime_slot in runtime_slots])):
            if not self.condition.negate:
                if all([not runtime_slot.empty for runtime_slot in runtime_slots]):
                    self._satisfy()
            self._unsatisfy()

    def _child_changed_test(self, parent, child, location=None):
        if location is None:
            if child.parent is parent and self.condition.negate:
                self._staisfy()
        elif location.parent is parent:
            for runtime_slot in parent.get_runtime_slots_gen(slot_types=(self.slot_types), bone_name_hash=None):
                if location.slot_hash == runtime_slot.slot_name_hash:
                    self.condition.negate or self._satisfy()
                    break

    def _on_child_changed_callback(self, child, location=None, new_parent=None):
        parent = self.parent_object
        if parent is None:
            return
        elif self.condition.condition_type == ObjectChildrenChangedCondition.CONDITION_CHILDREN_COUNT:
            self._threshold_test(parent)
        else:
            if self.condition.condition_type == ObjectChildrenChangedCondition.CONDITION_ALL_CHILDREN:
                self._all_slots_test(parent)
            else:
                if self.condition.condition_type == ObjectChildrenChangedCondition.CONDITION_SINGLE_CHILD:
                    self._child_changed_test(parent, child, location=location)


class HiddenOrShownCondition(HasTunableFactory, AutoFactoryInit, Condition):

    class Timing(enum.Int):
        ON_HIDDEN = 0
        ON_SHOWN = ...
        IS_HIDDEN = ...
        NOT_HIDDEN = ...

    FACTORY_TUNABLES = {'description':'\n            A condition that is satisfied when an object is hidden or shown.\n            ', 
     'participant':TunableEnumEntry(description='\n            The participant whose hidden flags we are checking.\n            ',
       tunable_type=ParticipantTypeSingle,
       default=ParticipantTypeSingle.Actor), 
     'hidden_flags':TunableEnumFlags(description='\n            The hidden reason we care about. If any of the flags exist as\n            hidden reasons, we satisfy this condition. If this is empty, then\n            we will care about any reason that would cause the object to be\n            hidden, and expect zero flags remaining when the object is shown.\n            ',
       enum_type=HiddenReasonFlag,
       default=HiddenReasonFlag.RABBIT_HOLE,
       allow_no_flags=True), 
     'timing':TunableEnumEntry(description='\n            When the condition satisfies.\n            Choices:\n            ON_HIDDEN: Only check the condition on the edge of the object being\n            hidden. This will not satisfy if you are hidden when the\n            interaction starts.\n            ON_SHOWN: Only check the condition on the edge of the object being\n            shown. This will not satisfy if you are not hidden when the \n            interaction starts.\n            IS_HIDDEN: Check that the object is hidden at any time this \n            condition is active. This will satisfy if you are hidden when the\n            interaction starts.\n            NOT_HIDDEN: Check that the object is not hidden at any time this\n            condition is active. This will satisfy if you are not hidden\n            when the interaction starts.\n            ',
       tunable_type=Timing,
       default=Timing.ON_HIDDEN)}

    def __str__(self):
        return 'HiddenOrShownCondition: {} {} {}'.format(self.participant, self.hidden_flags, self.timing)

    def attach_to_owner--- This code section failed: ---

 L.1727         0  LOAD_FAST                'callback'
                2  LOAD_FAST                'self'
                4  STORE_ATTR               si_callback

 L.1728         6  LOAD_FAST                'owner'
                8  LOAD_FAST                'self'
               10  STORE_ATTR               _owner

 L.1730        12  LOAD_FAST                'self'
               14  LOAD_ATTR                _owner
               16  LOAD_METHOD              get_participant
               18  LOAD_FAST                'self'
               20  LOAD_ATTR                participant
               22  CALL_METHOD_1         1  '1 positional argument'
               24  STORE_FAST               'obj'

 L.1731        26  LOAD_FAST                'obj'
               28  LOAD_METHOD              is_hidden
               30  CALL_METHOD_0         0  '0 positional arguments'
               32  STORE_FAST               'is_hidden'

 L.1733        34  LOAD_FAST                'self'
               36  LOAD_ATTR                timing
               38  LOAD_GLOBAL              HiddenOrShownCondition
               40  LOAD_ATTR                Timing
               42  LOAD_ATTR                IS_HIDDEN
               44  COMPARE_OP               ==
               46  POP_JUMP_IF_FALSE    80  'to 80'

 L.1734        48  LOAD_FAST                'is_hidden'
               50  POP_JUMP_IF_FALSE   124  'to 124'
               52  LOAD_FAST                'self'
               54  LOAD_ATTR                hidden_flags
               56  POP_JUMP_IF_FALSE    70  'to 70'
               58  LOAD_FAST                'obj'
               60  LOAD_METHOD              has_hidden_flags
               62  LOAD_FAST                'self'
               64  LOAD_ATTR                hidden_flags
               66  CALL_METHOD_1         1  '1 positional argument'
               68  POP_JUMP_IF_FALSE   124  'to 124'
             70_0  COME_FROM            56  '56'

 L.1735        70  LOAD_FAST                'self'
               72  LOAD_METHOD              _satisfy
               74  CALL_METHOD_0         0  '0 positional arguments'
               76  POP_TOP          
               78  JUMP_FORWARD        124  'to 124'
             80_0  COME_FROM            46  '46'

 L.1736        80  LOAD_FAST                'self'
               82  LOAD_ATTR                timing
               84  LOAD_GLOBAL              HiddenOrShownCondition
               86  LOAD_ATTR                Timing
               88  LOAD_ATTR                NOT_HIDDEN
               90  COMPARE_OP               ==
               92  POP_JUMP_IF_FALSE   124  'to 124'

 L.1737        94  LOAD_FAST                'is_hidden'
               96  POP_JUMP_IF_FALSE   116  'to 116'
               98  LOAD_FAST                'self'
              100  LOAD_ATTR                hidden_flags
              102  POP_JUMP_IF_FALSE   124  'to 124'
              104  LOAD_FAST                'obj'
              106  LOAD_METHOD              has_hidden_flags
              108  LOAD_FAST                'self'
              110  LOAD_ATTR                hidden_flags
              112  CALL_METHOD_1         1  '1 positional argument'
              114  POP_JUMP_IF_TRUE    124  'to 124'
            116_0  COME_FROM            96  '96'

 L.1738       116  LOAD_FAST                'self'
              118  LOAD_METHOD              _satisfy
              120  CALL_METHOD_0         0  '0 positional arguments'
              122  POP_TOP          
            124_0  COME_FROM           114  '114'
            124_1  COME_FROM           102  '102'
            124_2  COME_FROM            92  '92'
            124_3  COME_FROM            78  '78'
            124_4  COME_FROM            68  '68'
            124_5  COME_FROM            50  '50'

 L.1740       124  LOAD_FAST                'self'
              126  LOAD_METHOD              _enable_hidden_flags_watcher
              128  CALL_METHOD_0         0  '0 positional arguments'
              130  POP_TOP          

 L.1741       132  LOAD_CONST               (None, None)
              134  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 134

    def detach_from_owner(self, owner, exiting=False):
        self._disable_hidden_flags_watcher()
        self._owner = None
        self.si_callback = None

    def _enable_hidden_flags_watcher(self):
        obj = self._owner.get_participant(self.participant)
        obj.register_on_hidden_or_shown(self._on_hidden_or_shown)

    def _disable_hidden_flags_watcher(self):
        obj = self._owner.get_participant(self.participant)
        if obj.is_on_hidden_or_shown_callback_registered(self._on_hidden_or_shown):
            obj.unregister_on_hidden_or_shown(self._on_hidden_or_shown)

    def _on_hidden_or_shown(self, obj, hidden_flags_delta, added=False):
        if added:
            if not self.hidden_flags or obj.has_hidden_flags(self.hidden_flags):
                if self.timing == HiddenOrShownCondition.Timing.ON_HIDDEN or self.timing == HiddenOrShownCondition.Timing.IS_HIDDEN:
                    self._satisfy()
                else:
                    self._unsatisfy()
        elif not added:
            if not self.hidden_flags or obj.has_hidden_flags(self.hidden_flags) or self.timing == HiddenOrShownCondition.Timing.ON_SHOWN or self.timing == HiddenOrShownCondition.Timing.NOT_HIDDEN:
                self._satisfy()
            else:
                self._unsatisfy()
