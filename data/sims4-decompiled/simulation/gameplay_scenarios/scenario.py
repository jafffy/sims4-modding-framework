# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gameplay_scenarios\scenario.py
# Compiled at: 2022-10-30 22:12:14
# Size of source mod 2**32: 76210 bytes

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
break ::= BREAK_LOOP . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= continues . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
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
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
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
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_28
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_28
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_28
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_28
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_28
else_suite ::= suite_stmts . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= list . 
expr ::= list_comp . 
expr ::= listcomp . 
expr ::= or . 
expr ::= tuple . 
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else else_suitel . 
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jb_or_c ::= JUMP_BACK . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= continues . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lastl_stmt come_froms l_stmts . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= forelselaststmtl . 
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
listcomp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
listcomp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
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
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= forelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= store_subscript . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= continues . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= testfalse_not_or . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
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
tuple ::= expr expr expr BUILD_TUPLE_3 . 
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
   
 L.1457        92  LOAD_FAST                'sim_info'
                  94  LOAD_FAST                'self'
                  96  LOAD_ATTR                _sim_filter_id_to_sim_info_map
                  98  LOAD_FAST                'sim_filter_id'
                 100  STORE_SUBSCR     
->               102  JUMP_BACK            20  'to 20'
                 104  POP_BLOCK        
import itertools, assertions, event_testing, services, sims4, uid
from cas.cas_tuning import CASContextCriterionList
from collections import namedtuple
from date_and_time import TimeSpan
from distributor.rollback import ProtocolBufferRollback
from event_testing import test_events
from event_testing.resolver import SingleSimResolver, DoubleSimResolver, GlobalResolver
from filters.tunable import TunableSimFilter
from gameplay_scenarios.scenario_enums import ScenarioDifficultyCategory, ScenarioEntryMethod, ScenarioProperties, ScenarioCategory, ScenarioTheme
from gameplay_scenarios.scenario_outcomes import ScenarioOutcome, ScenarioPhaseLoot
from gameplay_scenarios.scenario_phase import ScenarioPhase, TerminatorHandler, run_scenario_test, PhaseEndingReason
from gameplay_scenarios.scenario_profiling import record_scenario_profile_metrics, should_record_scenario_profile_metrics, scenario_profile_on_phase_end
from gameplay_scenarios.scenario_tests_set import TunableScenarioBreakTest
from interactions.utils.death import DeathType
from interactions.utils.tunable_icon import TunableIcon
from playstyles.playstyle_enums import Playstyle
from relationships.relationship_enums import RelationshipType
from sims4 import math
from sims4.localization import TunableLocalizedString
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import HasTunableFactory, TunableList, TunableTuple, TunableReference, TunablePackSafeReference, TunableInterval, OptionalTunable, TunableResourceKey, Tunable, TunableMapping, TunableEnumFlags, TunableEnumEntry, HasTunableReference
from sims4.tuning.tunable_base import ExportModes, GroupNames
from situations.situation_serialization import GoalSeedling
from ui.screen_slam import TunableScreenSlamSnippet
from ui.ui_utils import hide_selected_notifications
from ui.ui_dialog_notification import TunableUiDialogNotificationSnippet
logger = sims4.log.Logger('Gameplay Scenarios', default_owner='jmorrow')
with sims4.reload.protected(globals()):
    scenario_profiles = None

class ScenarioTag(metaclass=sims4.tuning.instances.HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.SNIPPET)):
    INSTANCE_TUNABLES = {'name':TunableLocalizedString(description='\n            Name of the scenario type to display in the UI.\n            ',
       export_modes=ExportModes.ClientBinary), 
     'theme':TunableEnumEntry(description='\n            The theme identifier for this tag.\n            ',
       tunable_type=ScenarioTheme,
       default=ScenarioTheme.INVALID,
       invalid_enums=(
      ScenarioTheme.INVALID,),
       export_modes=ExportModes.ClientBinary)}


class ScenarioRole(HasTunableReference, metaclass=sims4.tuning.instances.HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.SNIPPET)):
    INSTANCE_TUNABLES = {'criteria': TunableList(description='\n            Data about CAS criteria that constrains sims with this Scenario Role.\n            \n            Each entry contains a list of criteria associated with a Loc String.\n            ',
                   tunable=TunableTuple(description='\n                A set of criteria associated with a Loc String, which will be\n                displayed in the CAS as a household requirement.\n                ',
                   criteria_list=CASContextCriterionList(description='\n                    A list of criteria that define restrictions on sims in scenarios\n                    with this role.\n                    '),
                   household_requirement_text=TunableLocalizedString(description='\n                    The text that will display as the player-facing\n                    household requirement associated with this Criteria List.\n                    '),
                   export_class_name='TunableScenarioRoleCriteria',
                   export_modes=(ExportModes.ClientBinary)))}


ActiveGoal = namedtuple('ActiveGoal', ['situation_goal', 'scenario_goal'])
LastVisibleGoal = namedtuple('LastVisibleGoal', ['goal', 'is_mandatory'])

class Scenario(metaclass=sims4.tuning.instances.HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.SNIPPET)):
    SCENARIO_CATEGORIES = TunableMapping(description='\n        A mapping from category to category data.\n        ',
      key_type=TunableEnumEntry(description='\n            The scenario category.\n            ',
      tunable_type=ScenarioCategory,
      default=(ScenarioCategory.INVALID),
      invalid_enums=(
     ScenarioCategory.INVALID,)),
      value_type=TunableTuple(description='\n            Data associated with the scenario category.\n            ',
      category_name=TunableLocalizedString(description='\n                The player facing name for this scenario category.\n                '),
      category_description=TunableLocalizedString(description='\n                The player facing description for this scenario category.\n                '),
      export_class_name='CategoryDataTuple'),
      export_modes=(
     ExportModes.ClientBinary,),
      tuple_name='CategoryData')
    SCENARIO_DIFFICULTY_CATEGORIES = TunableMapping(description='\n        A mapping from difficulty category to difficulty data.\n        ',
      key_type=TunableEnumEntry(description='\n            The difficulty category.\n            ',
      tunable_type=ScenarioDifficultyCategory,
      default=(ScenarioDifficultyCategory.INVALID),
      invalid_enums=(
     ScenarioDifficultyCategory.INVALID,)),
      value_type=TunableTuple(description='\n            Data associated with the difficulty category.\n            ',
      player_facing_name=TunableLocalizedString(description='\n                The player facing name for this difficulty category.\n                '),
      export_class_name='DifficultyCategoryDataTuple'),
      export_modes=(
     ExportModes.ClientBinary,),
      tuple_name='DifficultyCategoryData')
    RECOMMENDED_SCENARIOS = TunableTuple(description='\n        Data associated with scenarios recommended to players.\n        ',
      recommended_scenarios_no_playstyle=TunableList(description="\n            A list of scenarios recommended for new players for whom we don't have\n            playstyle data yet.\n            ",
      tunable=TunableReference(description='\n                A scenario.\n                ',
      manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
      class_restrictions=('Scenario', ))),
      recommended_scenarios_for_playstyles=TunableMapping(description='\n            A mapping from playstyle to list of scenarios recommended for that playstyle.\n            ',
      key_name='playstyle',
      key_type=TunableEnumEntry(description='\n                A playstyle.\n                ',
      tunable_type=Playstyle,
      default=(Playstyle.INVALID),
      invalid_enums=(
     Playstyle.INVALID,)),
      value_name='recommended_scenarios',
      value_type=TunableList(description='\n                A list of scenarios recommended for players that match this playstyle.\n                ',
      tunable=TunableReference(description='\n                    A scenario.\n                    ',
      manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
      class_restrictions=('Scenario', ))),
      tuple_name='PlaystyleRecommendedScenariosData',
      export_modes=(ExportModes.ClientBinary)),
      export_modes=(
     ExportModes.ClientBinary,),
      export_class_name='RecommendedScenariosData')

    @classmethod
    def _verify_tuning_callback(cls):

        def traverse_validate_base(phase, phases):
            phase_to_check = phase.phase_fallback_output.output.next_phase
            if phase_to_check is not None:
                if phase_to_check in phases:
                    if len(phase.phase_outputs) == 0:
                        logger.error('A loop detected in scenario phase graph. Next default phase:{} of phase:{} is already                             a previous phase. Consider changing it or adding an alternative next phase.'.format(phase_to_check, phase))
                        return False
            phase_outputs = phase.phase_outputs
            if len(phase_outputs) == 1:
                fallback_output = phase.phase_fallback_output.output
                first_output = phase_outputs[0].output.output
                if first_output.next_phase is not None:
                    if fallback_output.next_phase is None:
                        if fallback_output.scenario_outcome is None:
                            if first_output.next_phase in phases:
                                logger.error('A loop detected in scenario phase graph. Only next phase:{} of phase:{} is already                                 a previous phase. Consider changing it or adding an alternative next phase.'.format(first_output.next_phase, phase))
                                return False
            return True

        def traverse_validate(phase, phases):
            if not traverse_validate_base(phase, phases):
                return
            phases.add(phase)
            for phase_output in phase.phase_outputs:
                next_phase = phase_output.output.output.next_phase
                if next_phase is not None:
                    traverse_validate(next_phase, phases)

            next_phase = phase.phase_fallback_output.output.next_phase
            if next_phase is not None:
                traverse_validate(next_phase, phases)
            phases.remove(phase)

        phases = set()
        if cls.starting_phase is not None:
            traverse_validate(cls.starting_phase, phases)

    INSTANCE_TUNABLES = {'compatibility_with_scenario_entry_method':TunableEnumFlags(description='\n            A set of values that defines which entry methods are compatible with this scenario.\n            \n            For example, if only NEW_HOUSEHOLDS is tuned, then this scenario\n            is only compatible with new households and cannot be applied to\n            an existing household. \n            ',
       enum_type=ScenarioEntryMethod,
       export_modes=ExportModes.All), 
     'category':TunableEnumEntry(description='\n            A value that defines which category this scenario falls under.\n\n            This category maps to a user-facing name that can be defined in \n            the gameplay_scenarios.scenario module tuning.\n            ',
       tunable_type=ScenarioCategory,
       default=ScenarioCategory.INVALID,
       invalid_enums=(
      ScenarioCategory.INVALID,),
       export_modes=ExportModes.ClientBinary), 
     'difficulty':TunableEnumEntry(description='\n            A value that defines how difficult the scenario is estimated to be.\n            \n            This difficulty maps to a user-facing name that can be defined in \n            the gameplay_scenarios.scenario module tuning.\n            ',
       tunable_type=ScenarioDifficultyCategory,
       default=ScenarioDifficultyCategory.INVALID,
       invalid_enums=(
      ScenarioDifficultyCategory.INVALID,),
       export_modes=ExportModes.ClientBinary), 
     'scenario_name':TunableLocalizedString(description='\n            A string that will be used in UI to display the name of the scenario.\n            ',
       export_modes=ExportModes.All,
       tuning_group=GroupNames.UI), 
     'scenario_description':TunableLocalizedString(description='\n            A string that will be used in UI to display the description of the scenario.\n            ',
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'tagline_text':TunableLocalizedString(description='\n            A string to show a brief description of the scenario in the scenario list.\n            ',
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'scenario_tags':TunableList(description='\n            A list of tags associated with this scenario that will be used in the\n            UI to filter scenarios.\n            ',
       tunable=TunableReference(description='\n                A scenario tag.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
       class_restrictions=('ScenarioTag', )),
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'icon':TunableResourceKey(description=',\n            If enabled, an icon to be displayed in the scenario browsing UI.\n            ',
       allow_none=True,
       export_modes=ExportModes.ClientBinary,
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       tuning_group=GroupNames.UI), 
     'reward_icon':TunableResourceKey(description=',\n            If enabled, an icon of the default reward given to players to displayed\n            in the scenario browsing UI, details panel and outcome ui.\n            ',
       allow_none=True,
       export_modes=ExportModes.All,
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       tuning_group=GroupNames.UI), 
     'reward_text':TunableLocalizedString(description=',\n            If enabled, the name of the reward players will be given upon completing\n            the scenario which is shown in the browsing UI, details panel and outcome ui.\n            ',
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.UI), 
     'scenario_start_notification':TunableUiDialogNotificationSnippet(description='\n            Provides access to the TNS data to allow injection of the scenario name.\n            '), 
     'scenario_role_data':TunableList(description='\n            A list of data about scenario roles for this scenario.\n            ',
       tunable=TunableTuple(role=TunableReference(description='\n                    The scenario role.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
       class_restrictions=('ScenarioRole', )),
       sim_count=TunableInterval(description='\n                    The minimum (inclusive) and maximum (inclusive) number of\n                    sims in the household that may have this role.\n                    ',
       tunable_type=int,
       default_lower=1,
       default_upper=1,
       minimum=0,
       maximum=8,
       export_class_name='ScenarioRoleTunableInterval'),
       role_traits=TunableList(description='\n                    A list of all role traits for this specific scenario role. These traits will be re-added to a sim \n                    with this scenario role every time that sim is instanced and removed every time that sim \n                    is de-instanced.\n                    ',
       tunable=TunableReference(description='\n                        This should only be used for Traits that do not add commodities, as these traits will be \n                        re-added every time the sim is instanced.\n                        ',
       manager=(services.get_instance_manager(sims4.resources.Types.TRAIT))),
       export_modes=(ExportModes.ServerXML)),
       export_class_name='TunableScenarioRoleData',
       export_modes=(ExportModes.ClientBinary),
       tuning_group=(GroupNames.UI))), 
     'relationship_requirements':TunableList(description='\n            Constraints on how sims with different roles must be related.\n            ',
       tunable=TunableTuple(description='\n                Data about how two sims with specific roles must be related.\n                ',
       subject_role=TunableReference(description='\n                    One role in the relationship.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
       class_restrictions=('ScenarioRole', )),
       target_role=TunableReference(description='\n                    The other role in the relationship.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
       class_restrictions=('ScenarioRole', )),
       relationship_type=TunableEnumEntry(description='\n                    The type of relationship between a subject sim and\n                    a target sim.\n                    \n                    A value of NONE indicates no familial relationship.\n                    \n                    Relationships are directed from sims with the Subject Role to\n                    sims with the Target Role. For example, if this is tuned to\n                    PARENT, then any sims with the Target Role will be\n                    the parents of any sims with the Subject Role.\n                    ',
       tunable_type=RelationshipType,
       default=(RelationshipType.NONE)),
       household_requirement_text=TunableLocalizedString(description='\n                    The text that will display for this requirement.\n                    '),
       export_class_name='TunableRelationshipRequirement',
       export_modes=(ExportModes.ClientBinary),
       tuning_group=(GroupNames.UI))), 
     'screen_slam_scenario_completed':OptionalTunable(description='\n            If enabled, trigger this Screen Slam when the scenario is completed.\n            ',
       tunable=TunableScreenSlamSnippet(description='\n                A Screen Slam to show when the scenario is completed.\n                \n                Localization Tokens: Scenario Name - {0.String}.\n                '),
       tuning_group=GroupNames.UI), 
     'starting_phase':ScenarioPhase.TunablePackSafeReference(description='\n            A reference to the first phase of the scenario.\n            If empty, scenario will be executed with scenario goals instead of phase goals,\n            according to scenario versions v1 and v2.\n            ',
       allow_none=True,
       export_modes=ExportModes.ClientBinary), 
     'terminators':TunableList(description='\n            List of Terminators.\n            If any terminator test is triggered, the current scenario will be terminated.\n            ',
       tunable=TunableTuple(description='\n                Data containing termination condition and associated scenario outcome. \n                ',
       scenario_outcome=ScenarioOutcome.TunablePackSafeReference(description='\n                    The scenario outcome that will happen if termination conditions are met.\n                    '),
       termination_condition=TunableScenarioBreakTest.TunableFactory(description='\n                    Test to determine if the terminator is triggered.\n                    '),
       terminator_description_text=TunableLocalizedString(description='\n                    Description text for terminator (only for debug purposes).\n                    '))), 
     'outcome_on_cancel':ScenarioOutcome.TunableReference(description='\n            The scenario outcome that will be executed when player manually cancels the scenario.\n            ',
       pack_safe=True,
       allow_none=True), 
     'outcome_on_validation_failed':ScenarioOutcome.TunableReference(description='\n            The scenario outcome that will be executed if for any reason the \n            sources needed for scenario cannot be validated.\n            i.e when npc sim is not alive anymore.\n            ',
       pack_safe=True,
       allow_none=True), 
     'loot_on_end':ScenarioPhaseLoot.TunableFactory(description='\n            The loots that will be applied when scenario ends no matter of the outcome.\n            This is a good place to clean up the temp buff/traits/items that are added only for the scenario.\n            '), 
     'scenario_npc_sims':TunableList(description='\n            A list of sim filters. Sim_infos of satisfying the conditions will be stored in the scenario\n            and used for referencing non household sims in loots and tests inside the scenario.\n            If sim_info satisfying filters does not exist a new one will be created.\n            ',
       tunable=TunableTuple(description='\n                Data containing the sim_filter to reference non household sims.\n                ',
       sim_filter=TunableReference(description='\n                    A sim filter to reference non household sims.\n                    If sim_info satisfying filter does not exist a new one will be created.           \n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.SIM_FILTER)),
       class_restrictions=TunableSimFilter),
       invalidation_trait=TunableReference(description='\n                    Trait used to invalidate the NPC associated to the scenario when the scenario is finished/reset.\n                    ',
       allow_none=True,
       manager=(services.get_instance_manager(sims4.resources.Types.TRAIT))),
       export_class_name='TunableScenarioNpcSims',
       export_modes=(ExportModes.ClientBinary))), 
     'goals':TunableList(description='\n            A list of SituationGoals that track on any household with this\n            scenario. These act as the end conditions for the scenario. If any\n            goal is achieved, the scenario will end.\n            This is only relevant for scenario versions v1 and v2.\n            Should be empty for v3 and start_phase should be filled instead.\n            ',
       tunable=TunableTuple(description='\n                Data containing the SituationGoal and any additional data about that goal specific to the scenario.\n                ',
       situation_goal=TunablePackSafeReference(description='\n                    A SituationGoal.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.SITUATION_GOAL))),
       goal_description_text=TunableLocalizedString(description='\n                    The text that will display for this goal in the load dialog\n                    and scenario outcome screen.\n                    '),
       goal_title_text=TunableLocalizedString(description='\n                    The title for this goal. This is shown in the scenario outcome screen\n                    and also in the ScenarioLivePanel.\n                    '),
       outcome_header_icon=TunableIcon(description='\n                    The icon that sits next to the header text for each goal\n                    in the ScenarioLivePanel.\n                    ',
       export_modes=(ExportModes.ServerXML),
       allow_none=True),
       required_pack=TunableEnumEntry(description='\n                    The pack that the goal may require.\n                    ',
       tunable_type=(sims4.common.Pack),
       default=(sims4.common.Pack.BASE_GAME),
       export_modes=(ExportModes.All)),
       visible_in_load_dialog=Tunable(description='\n                    If checked, the goal text will be visible in the scenario\n                    load dialog. If unchecked, the goal text will not be\n                    visible in the scenario load dialog.\n                    \n                    This will not affect whether or not the description text\n                    is shown in the outcome screen.\n                    ',
       tunable_type=bool,
       default=True),
       export_class_name='TunableScenarioGoalData',
       export_modes=(ExportModes.ClientBinary))), 
     'household_money':sims4.tuning.tunable.Tunable(description='\n            The starting money of the pre-made household. Can be overridden using a Loot Action in Live Mode.\n            Needed to allow the player to be able to purchase a lot in the Neighborhood Edit mode.\n            ',
       tunable_type=int,
       default=20000,
       export_modes=ExportModes.ClientBinary), 
     'loot_on_scenario_start':TunableMapping(key_name='Enum Entry',
       key_type=TunableEnumEntry(description='\n                How the household enters the scenario\n                ',
       tunable_type=ScenarioEntryMethod,
       default=(ScenarioEntryMethod.NEW_HOUSEHOLD)),
       value_name='Loots',
       value_type=TunableTuple(description='\n                A list of loot actions to apply to the household with this scenario.\n                These are applied only when the scenario starts (the first time a\n                household is loaded with the scenario).\n                ',
       household_loot=TunableList(description='\n                    Loot that will apply once to an arbitrary sim in the household.\n                    \n                    Useful for applying loot to the household as a whole. For example,\n                    this can be used to set the household funds at the start of the\n                    scenario.\n                    ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
       class_restrictions=('LootActions', ))),
       rel_loot=TunableList(description='\n                    Loot that will apply to each pair of sims in the household.\n                    \n                    Useful for setting up relationships at the start of the\n                    scenario.\n                    \n                    Subject and targets should be Actor and TargetSim, respectively.\n                    ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
       class_restrictions=('LootActions', ))))), 
     'loot_on_scenario_end':TunableTuple(description='\n            Loot that applies when the scenario ends.\n            ',
       household_loot_on_successful_completion=TunableList(description='\n                Loot that applies to an arbitrary sim in the household if the scenario\n                ends successfully, meaning the scenario ended because a non-hidden\n                goal was achieved.\n                ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ACTION)),
       class_restrictions=('LootActions', )))), 
     'outcome_screen_background_image':OptionalTunable(description=',\n            The background image for the outcome screen when the scenario ends.\n            ',
       tunable=TunableResourceKey(resource_types=(sims4.resources.CompoundTypes.IMAGE)),
       tuning_group=GroupNames.UI), 
     'ui_sort_order':sims4.tuning.tunable.Tunable(description='\n            Order in which the scenario will appear in the scenario list dialog.\n            Scenarios sort from lowest to highest.\n            ',
       tunable_type=int,
       default=0,
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'compatible_premade_household_templates':TunableList(description='\n            The Premade Households that are compatible with this scenario. \n            NOTE: only the first one in the list will be selected for this scenario \n            (in the future the player will have a choice of which one to pick from).\n            ',
       tunable=TunableResourceKey(description='\n                The Household file to use.\n                ',
       default=None,
       resource_types=(
      sims4.resources.Types.HOUSEHOLD_BINARY,),
       export_modes=(ExportModes.ClientBinary))), 
     'properties':TunableEnumFlags(description='\n            A set of properties related to this scenario.\n            ',
       enum_type=ScenarioProperties,
       export_modes=ExportModes.All)}

    def __init__(self, scenario_tracker, **kwargs):
        (super().__init__)(**kwargs)
        self._has_started = False
        self._active_goals = []
        self._triggered_phases_guid64 = set()
        self._skipped_phases_guid64 = set()
        self._last_completed_visible_goal_for_sequence = {}
        self._active_phase = None
        self._terminator_handlers = []
        self._last_phase_outputs = {}
        self._scenario_tracker = scenario_tracker
        self._goal_id_gen = uid.UniqueIdGenerator(1)
        self._role_id_to_role_traits = {}
        self._sim_id_to_role_id_map = {}
        self._role_id_to_sim_info_map = {}
        self._sim_time_lapsed = None
        self._sim_time_marker = None
        self._instance_id = 0
        self._scenario_entry_method = None
        for role_data in self.scenario_role_data:
            self._role_id_to_role_traits[role_data.role.guid64] = role_data.role_traits

        self._sim_filter_id_to_sim_info_map = {}
        self._loaded_sim_filter_id_to_sim_info_id_map = {}
        self._completed_goal_infos = {}
        self._terminated_phase_infos = {}

    @property
    def household(self):
        return self._scenario_tracker.household

    def reset_scenario_data(self):
        self._has_started = False
        self._role_id_to_role_traits = {}
        self._role_id_to_sim_info_map = {}
        self._sim_id_to_role_id_map = {}
        self._sim_time_lapsed = None
        self._sim_time_marker = None
        self._active_goals = []
        self._triggered_phases_guid64 = set()
        self._terminator_handlers = []
        self._last_phase_outputs = {}
        self._last_completed_visible_goal_for_sequence = {}
        self._sim_filter_id_to_sim_info_map = {}
        self._loaded_sim_filter_id_to_sim_info_id_map = {}
        self._completed_goal_infos = {}
        self._terminated_phase_infos = {}

    def sims_of_interest_gen(self, roles=None):
        if not roles:
            yield from (sim_info.get_sim_instance() for sim_info in self._scenario_tracker.household if sim_info.is_instanced())
        else:
            for role in roles:
                if role.guid64 not in self._role_id_to_sim_info_map:
                    continue
                sim_infos = self._role_id_to_sim_info_map[role.guid64]
                for sim_info in sim_infos:
                    sim = sim_info.get_sim_instance()
                    if sim is not None:
                        yield sim

    def sim_infos_of_interest_gen(self, roles=None):
        if not roles:
            yield from self._scenario_tracker.household
        else:
            for role in roles:
                if role is None:
                    continue
                if role.guid64 not in self._role_id_to_sim_info_map:
                    continue
                yield from self._role_id_to_sim_info_map[role.guid64]

        if False:
            yield None

    def on_household_member_removed(self, sim_info):
        self._sim_id_to_role_id_map.pop(sim_info.id, None)
        for _, sim_infos in self._role_id_to_sim_info_map.items():
            if sim_info in sim_infos:
                sim_infos.remove(sim_info)

    def get_role_traits_for_role_id(self, role_id):
        return self._role_id_to_role_traits.get(role_id, None)

    def get_role_id_for_sim(self, sim_id):
        return self._sim_id_to_role_id_map.get(sim_id, None)

    def get_role_for_sim(self, sim_id):
        return services.snippet_manager().get(self._sim_id_to_role_id_map.get(sim_id, 0))

    def active_goals_gen(self):
        for active_goal, _ in self._active_goals:
            yield active_goal

    def active_goals_and_tuning_gen(self):
        yield from self._active_goals
        if False:
            yield None

    def is_goal_completed(self, goal_guid64):
        return goal_guid64 in self._completed_goal_infos

    def get_goal_completion_time(self, goal_guid64):
        return self._completed_goal_infos.get(goal_guid64)

    @property
    def triggered_phases_guids(self):
        return self._triggered_phases_guid64

    def get_sim_info_from_sim_filter(self, sim_filter):
        if sim_filter.guid64 in self._sim_filter_id_to_sim_info_map:
            return self._sim_filter_id_to_sim_info_map[sim_filter.guid64]
        for scenario_npc in self.scenario_npc_sims:
            if scenario_npc.sim_filter.guid64 == sim_filter.guid64:
                filter_results = services.sim_filter_service().submit_matching_filter(sim_filter=sim_filter,
                  allow_yielding=False,
                  conform_if_constraints_fail=False)
                if len(filter_results) > 0:
                    self._sim_filter_id_to_sim_info_map[sim_filter.guid64] = filter_results[0].sim_info
                    return self._sim_filter_id_to_sim_info_map[sim_filter.guid64]

    @property
    def has_started(self):
        return self._has_started

    def start_scenario(self):
        self._sim_time_lapsed = TimeSpan(0)
        self._sim_time_marker = services.time_service().sim_now
        if self.starting_phase is None:
            self.start_scenario_without_phase()
        else:
            self.run_sim_filters_for_scenario_npcs()
            self.register_scenario_terminators()
            self.start_phase(self.starting_phase(scenario=self))
        self._has_started = True
        dialog = self.scenario_start_notification(services.active_sim_info())
        dialog.show_dialog(additional_tokens=(self.scenario_name,))

    def start_scenario_without_phase(self):
        loot_tuple = self.loot_on_scenario_start.get(ScenarioEntryMethod(self._scenario_entry_method))
        if loot_tuple is not None:
            with hide_selected_notifications():
                if loot_tuple.household_loot:
                    sim = next(iter(self._scenario_tracker.household), None)
                    if sim is None:
                        logger.error('Household is empty while trying to start scenario!')
                    else:
                        resolver = SingleSimResolver(sim)
                        for action in loot_tuple.household_loot:
                            action.apply_to_resolver(resolver)

                if loot_tuple.rel_loot:
                    for sim_info_a, sim_info_b in itertools.combinations(self._scenario_tracker.household, 2):
                        resolver = DoubleSimResolver(sim_info_a, sim_info_b)
                        for action in loot_tuple.rel_loot:
                            action.apply_to_resolver(resolver)

        self._active_goals = [ActiveGoal(goal_tuple.situation_goal(goal_id=(self._goal_id_gen()), scenario=self), goal_tuple) for goal_tuple in self.goals if goal_tuple.situation_goal is not None]
        self.setup_goals()

    def start_phase(self, phase, run_pretests=True):
        if phase.guid64 in self._triggered_phases_guid64:
            for goal_sequence_tuple in phase.goals:
                for goal_tuple in goal_sequence_tuple.goal_sequence:
                    goal_id = goal_tuple.goal.situation_goal.guid64
                    if goal_id in self._completed_goal_infos:
                        del self._completed_goal_infos[goal_id]

        else:
            self._triggered_phases_guid64.add(phase.guid64)
            services.get_event_manager().process_event((test_events.TestEvent.ScenarioPhaseTriggered), None,
              phase=phase)
            self._last_completed_visible_goal_for_sequence = {}
            if not run_pretests or phase.run_pre_tests():
                self._active_phase = phase
                self.apply_loot(phase.intro_loot.loots)
                self.set_active_goals_on_phase_start(phase)
                self.setup_goals()
                phase.on_start()
                self._scenario_tracker.send_goal_update_op_to_client()
            else:
                phase.choose_output_and_progress(PhaseEndingReason.SKIPPED)
                self._skipped_phases_guid64.add(phase.guid64)

    def reset_active_phase(self):
        self.start_phase(self._active_phase, False)

    def reset_goal(self, situation_goal_guid64):
        for active_goal in self._active_goals:
            if active_goal.situation_goal.guid64 == situation_goal_guid64:
                active_goal.situation_goal.reset_count()
                break
        else:
            return False

        self._scenario_tracker.send_goal_update_op_to_client()
        return True

    def __str__(self):
        return self.__class__.__name__

    def on_phase_ended(self, reason, end_description):
        if reason == PhaseEndingReason.TERMINATED:
            termination_time = services.time_service().sim_now.absolute_ticks()
            self._terminated_phase_infos[self._active_phase.guid64] = termination_time
        self._scenario_tracker.on_phase_finished(self._active_phase, reason, end_description)
        if scenario_profiles is not None:
            self.update_scenario_profile_on_phase_end()
        self._active_phase = None

    def update(self):
        if scenario_profiles is not None:
            self.update_scenario_profile()

    def update_scenario_profile(self):
        scenario_record_name = str(self)
        record = scenario_profiles.get(scenario_record_name)
        if record is None:
            record = dict()
            scenario_profiles[scenario_record_name] = record
        if should_record_scenario_profile_metrics(record, self._active_phase):
            record_scenario_profile_metrics(record, self._active_phase, math.ceil(get_sim_debt_time()))

    def update_scenario_profile_on_phase_end(self):
        scenario_record_name = str(self)
        record = scenario_profiles.get(scenario_record_name)
        if record is not None:
            scenario_profile_on_phase_end(record, self._active_phase, get_sim_debt_time())

    def on_phase_output_triggered(self, output_key, next_phase):
        output_time = services.time_service().sim_now.absolute_ticks()
        next_phase_name = next_phase.__name__ if next_phase is not None else 'None'
        self._last_phase_outputs[self._active_phase.guid64] = (output_key, next_phase_name, output_time)

    def get_phase_last_output_info(self, phase_guid64):
        return self._last_phase_outputs.get(phase_guid64)

    def set_active_goals_on_phase_start(self, phase):
        self.clean_up_goals()
        self._active_goals.clear()
        for goal_tuple in phase.goals:
            self.activate_goal(self.generate_active_goal_tuple_from_sequence(goal_tuple.goal_sequence, 0))

    def generate_active_goal_tuple_from_sequence(self, goal_sequence, index):
        if index < len(goal_sequence):
            phase_goal = goal_sequence[index].goal
            return ActiveGoal(phase_goal.situation_goal(goal_id=(self._goal_id_gen()), scenario=self), phase_goal)
        return

    def setup_goals(self):
        for goal in self.active_goals_gen():
            self.setup_goal(goal, reevaluate=False)

        for goal in self.active_goals_gen():
            if not goal.should_reevaluate_on_load:
                continue
            goal.reevaluate_goal_completion()

    def setup_goal(self, goal, reevaluate=True):
        goal.setup()
        goal.register_for_on_goal_completed_callback(self._on_goal_completed)
        if reevaluate:
            if goal.should_reevaluate_on_load:
                goal.reevaluate_goal_completion()

    def clean_up_goals(self):
        for goal in self.active_goals_gen():
            goal.decommision()

    def on_goal_sequence_reset(self, goal_sequence, sequence_index):
        for goal_tuple in goal_sequence:
            active_goal = self.get_active_goal_from_scenario_goal(goal_tuple.goal)
            goal_id = goal_tuple.goal.situation_goal.guid64
            if active_goal is not None:
                self._active_goals.remove(active_goal)
            elif goal_id in self._completed_goal_infos:
                del self._completed_goal_infos[goal_id]

        self._last_completed_visible_goal_for_sequence.pop(sequence_index)
        self.activate_goal(self.generate_active_goal_tuple_from_sequence(goal_sequence, 0))
        self.setup_goal(self._active_goals[-1].situation_goal)

    def get_active_goal_from_scenario_goal(self, scenario_goal):
        for active_goal in self._active_goals:
            if active_goal.scenario_goal is scenario_goal:
                return active_goal

    def register_scenario_terminators(self):
        for terminator in self.terminators:
            self._terminator_handlers.append(TerminatorHandler(self, terminator, self.on_terminator_triggered))
            services.get_event_manager().register_tests(self._terminator_handlers[-1], (terminator.termination_condition.scenario_test.test,))

    def unregister_scenario_terminators(self):
        for terminator_handler in self._terminator_handlers:
            services.get_event_manager().unregister_tests(terminator_handler, (terminator_handler.terminator.termination_condition.scenario_test.test,))

        self._terminator_handlers.clear()

    def on_terminator_triggered(self, terminator):
        last_phase = self._active_phase
        self._active_phase.on_terminator_triggered(terminator)
        self.end_scenario(terminator.scenario_outcome, last_phase)

    def run_sim_filters_for_scenario_npcs(self):
        for sim_filter_tuple in self.scenario_npc_sims:
            filter_results = services.sim_filter_service().submit_matching_filter(sim_filter=(sim_filter_tuple.sim_filter), allow_yielding=False, conform_if_constraints_fail=True)
            for result in filter_results:
                self._sim_filter_id_to_sim_info_map[sim_filter_tuple.sim_filter.guid64] = result.sim_info

    def end_scenario(self, outcome, last_phase, cancelled=False):
        scenario_outcome = outcome if not cancelled else self.outcome_on_cancel
        if scenario_outcome is not None:
            self.apply_outcome(scenario_outcome)
        self.apply_loot(self.loot_on_end.loots)
        if not cancelled:
            self._scenario_tracker.end_scenario(last_phase=last_phase, outcome=scenario_outcome)
        self.unregister_scenario_terminators()
        self.clean_up_goals()
        for sim_info in self.household:
            self._scenario_tracker.remove_role_traits(sim_info)

    def apply_loot(self, loots):

        def apply_double_sim_loot(sim_info, sim_info_2):
            resolver = DoubleSimResolver(sim_info, sim_info_2)
            resolver.set_additional_metric_key_data(self._active_phase)
            loot_tuple.scenario_loot.loot_action.apply_to_resolver(resolver)

        def check_and_apply_single_or_double_sim_loot(sim_info, loot_tuple):
            secondary_actor_role = loot_tuple.scenario_loot.secondary_actor_role
            secondary_actor_sim_filter = loot_tuple.scenario_loot.secondary_actor_sim_filter
            if secondary_actor_role is not None:
                for sim_info_2 in self.sim_infos_of_interest_gen([secondary_actor_role]):
                    apply_double_sim_loot(sim_info, sim_info_2)

            else:
                if secondary_actor_sim_filter is not None:
                    sim_info_2 = self.get_sim_info_from_sim_filter(secondary_actor_sim_filter)
                    if sim_info_2 is not None:
                        apply_double_sim_loot(sim_info, sim_info_2)
                    else:
                        logger.error('No sim satisfying secondary_actor_sim_filter conditions is found.')
                else:
                    resolver = event_testing.resolver.DataResolver(sim_info=sim_info, additional_metric_key_data=(self._active_phase))
                    loot_tuple.scenario_loot.loot_action.apply_to_resolver(resolver)

        for loot_tuple in loots:
            actor_role = loot_tuple.scenario_loot.actor_role
            actor_sim_filter = loot_tuple.scenario_loot.actor_sim_filter
            if actor_role is not None:
                for sim_info in self.sim_infos_of_interest_gen([actor_role]):
                    check_and_apply_single_or_double_sim_loot(sim_info, loot_tuple)

            elif actor_sim_filter is not None:
                sim_info = self.get_sim_info_from_sim_filter(actor_sim_filter)
                if sim_info is not None:
                    check_and_apply_single_or_double_sim_loot(sim_info, loot_tuple)
                else:
                    logger.error('No sim satisfying actor_sim_filter conditions is found.')
            else:
                loot_tuple.scenario_loot.loot_action.apply_to_resolver(GlobalResolver(additional_metric_key_data=(self._active_phase)))

    def apply_outcome(self, outcome):
        tests_passed = True
        for test_tuple in outcome.tests.scenario_tests:
            if not run_scenario_test(test_tuple.scenario_test, self, self._active_phase):
                tests_passed = False
                break

        if tests_passed:
            self.apply_loot(outcome.scenario_outcome_loot.loots)

    def save(self, household_proto):
        household_scenario_data_msg = household_proto.scenario_data
        gameplay_scenario_data_msg = household_proto.gameplay_data.gameplay_scenario_tracker.active_scenario_data
        household_scenario_data_msg.scenario_id = self.guid64
        household_scenario_data_msg.instance_id = self.instance_id
        for sim_id, role_id in self._sim_id_to_role_id_map.items():
            with ProtocolBufferRollback(household_scenario_data_msg.sim_role_pairs) as (sim_role_pair):
                sim_role_pair.sim_id = sim_id
                sim_role_pair.role_id = role_id

        household_scenario_data_msg.scenario_entry_method = self._scenario_entry_method
        if self._has_started:
            gameplay_scenario_data_msg.scenario_guid = self.guid64
            gameplay_scenario_data_msg.sim_time_lapsed = self.sim_time_lapsed.in_ticks()
            for active_goal in self.active_goals_gen():
                with ProtocolBufferRollback(gameplay_scenario_data_msg.active_goals) as (goal_proto):
                    goal_seed = active_goal.create_seedling()
                    goal_seed.finalize_creation_for_save()
                    goal_seed.serialize_to_proto(goal_proto.goal_data)

            if self.starting_phase is not None:
                self.save_phase_related_data(gameplay_scenario_data_msg)

    def save_phase_related_data(self, gameplay_scenario_data_msg):
        gameplay_scenario_data_msg.active_phase_guid = self._active_phase.guid64
        gameplay_scenario_data_msg.triggered_phases.extend(self._triggered_phases_guid64)
        gameplay_scenario_data_msg.skipped_phases.extend(self._skipped_phases_guid64)
        for sequence_index, last_visible_goal in self._last_completed_visible_goal_for_sequence.items():
            with ProtocolBufferRollback(gameplay_scenario_data_msg.last_completed_goal_sequence_pair) as (completed_goal_sequence_pair_proto):
                goal_seed = last_visible_goal.goal.create_seedling()
                goal_seed.finalize_creation_for_save()
                goal_seed.serialize_to_proto(completed_goal_sequence_pair_proto.completed_goal.goal_data)
                completed_goal_sequence_pair_proto.sequence_index = sequence_index
                completed_goal_sequence_pair_proto.is_mandatory = last_visible_goal.is_mandatory

        for phase_guid64, output_info in self._last_phase_outputs.items():
            output_key, next_phase, output_time = output_info
            with ProtocolBufferRollback(gameplay_scenario_data_msg.last_phase_outputs) as (phase_output_info):
                phase_output_info.phase_guid64 = phase_guid64
                phase_output_info.output_key = output_key
                phase_output_info.next_phase = next_phase
                phase_output_info.output_time = output_time

        for sim_filter_id, sim_info in self._sim_filter_id_to_sim_info_map.items():
            with ProtocolBufferRollback(gameplay_scenario_data_msg.sim_filter_sim_info_pair) as (sim_filter_sim_info_pair):
                sim_filter_sim_info_pair.sim_filter_id = sim_filter_id
                sim_filter_sim_info_pair.sim_info_id = sim_info.id

        for goal_guid64, completion_time in self._completed_goal_infos.items():
            with ProtocolBufferRollback(gameplay_scenario_data_msg.completed_goal_infos) as (completed_goal_info):
                completed_goal_info.goal_guid64 = goal_guid64
                completed_goal_info.completion_time = completion_time

        for phase_guid64, termination_time in self._terminated_phase_infos.items():
            with ProtocolBufferRollback(gameplay_scenario_data_msg.terminated_phase_infos) as (terminated_phase_info):
                terminated_phase_info.phase_guid64 = phase_guid64
                terminated_phase_info.termination_time = termination_time

    def load_household_data(self, scenario_data_msg, gameplay_scenario_data_msg, scenario_started_before=False):
        self._has_started = scenario_started_before
        self._instance_id = scenario_data_msg.instance_id
        sim_info_manager = services.sim_info_manager()
        for pair_proto in scenario_data_msg.sim_role_pairs:
            sim_info = sim_info_manager.get(pair_proto.sim_id)
            if sim_info is None:
                continue
            self._sim_id_to_role_id_map[pair_proto.sim_id] = pair_proto.role_id
            if pair_proto.role_id in self._role_id_to_sim_info_map:
                self._role_id_to_sim_info_map[pair_proto.role_id].append(sim_info)
            else:
                self._role_id_to_sim_info_map[pair_proto.role_id] = [
                 sim_info]

        self._sim_time_lapsed = TimeSpan(gameplay_scenario_data_msg.sim_time_lapsed)
        self._sim_time_marker = services.time_service().sim_now if self.household.is_active_household else None
        self._scenario_entry_method = scenario_data_msg.scenario_entry_method

        def to_goal(goal_seed):
            return goal_seed.goal_type(goal_id=(self._goal_id_gen()), count=(goal_seed.count),
              reader=(goal_seed.reader),
              completed_time=(goal_seed.completed_time),
              scenario=self,
              sub_goals=[to_goal(sub_goal_seed) for sub_goal_seed in goal_seed.sub_goal_seeds])

        if self._has_started:
            phase_id = gameplay_scenario_data_msg.active_phase_guid
            phase = self.get_phase_with_id(phase_id)
            if phase is None:
                self.load_data_without_phase(gameplay_scenario_data_msg, to_goal)
            else:
                self.load_data_with_phase(phase, gameplay_scenario_data_msg, to_goal)

    def load_data_without_phase(self, gameplay_scenario_data_msg, to_goal):
        for goal_proto in gameplay_scenario_data_msg.active_goals:
            goal_seed = GoalSeedling.deserialize_from_proto(goal_proto.goal_data)
            if goal_seed is None:
                continue
            goal_guid64_to_load = goal_seed.goal_type.guid64
            for goal_tuning in self.goals:
                if goal_tuning.situation_goal.guid64 == goal_guid64_to_load:
                    goal = to_goal(goal_seed)
                    self._active_goals.append(ActiveGoal(goal, goal_tuning))
                    break

        goal_ids = [situation_goal.guid64 for situation_goal in self.active_goals_gen()]
        for goal_tuning in self.goals:
            if goal_tuning.situation_goal is not None and goal_tuning.situation_goal.guid64 not in goal_ids:
                goal = goal_tuning.situation_goal(goal_id=(self._goal_id_gen()), scenario=self)
                self._active_goals.append(ActiveGoal(goal, goal_tuning))

    def load_data_with_phase(self, phase, gameplay_scenario_data_msg, to_goal):
        self.register_scenario_terminators()
        self._active_phase = phase(scenario=self)
        self._active_phase.on_load()
        for completed_goal_info in gameplay_scenario_data_msg.completed_goal_infos:
            self._completed_goal_infos[completed_goal_info.goal_guid64] = completed_goal_info.completion_time

        for goal_proto in gameplay_scenario_data_msg.active_goals:
            goal_seed = GoalSeedling.deserialize_from_proto(goal_proto.goal_data)
            if goal_seed is None:
                continue
            goal_guid64_to_load = goal_seed.goal_type.guid64
            for goal_sequence_tuple in phase.goals:
                for goal_tuple in goal_sequence_tuple.goal_sequence:
                    if goal_tuple.goal.situation_goal.guid64 == goal_guid64_to_load:
                        goal = to_goal(goal_seed)
                        self.activate_goal(ActiveGoal(goal, goal_tuple.goal))
                        break
                else:
                    continue

                break

        self._triggered_phases_guid64 = set(gameplay_scenario_data_msg.triggered_phases)
        self._skipped_phases_guid64 = set(gameplay_scenario_data_msg.skipped_phases)
        active_goal_ids = [situation_goal.guid64 for situation_goal in self.active_goals_gen()]
        for goal_sequence_tuple in phase.goals:
            new_goal_candidate = None
            for goal_tuple in goal_sequence_tuple.goal_sequence:
                goal_id = goal_tuple.goal.situation_goal.guid64
                if goal_id in active_goal_ids:
                    new_goal_candidate = None
                    break
                elif self.is_goal_completed(goal_id):
                    new_goal_candidate = None
                elif new_goal_candidate is None and goal_id not in active_goal_ids:
                    new_goal_candidate = self.is_goal_completed(goal_id) or goal_tuple

            if new_goal_candidate is not None:
                goal = new_goal_candidate.goal.situation_goal(goal_id=(self._goal_id_gen()), scenario=self)
                self.activate_goal(ActiveGoal(goal, new_goal_candidate.goal))

        for completed_goal_sequence_pair_proto in gameplay_scenario_data_msg.last_completed_goal_sequence_pair:
            goal_seed = GoalSeedling.deserialize_from_proto(completed_goal_sequence_pair_proto.completed_goal.goal_data)
            if goal_seed is None:
                continue
            goal = to_goal(goal_seed)
            self._last_completed_visible_goal_for_sequence[completed_goal_sequence_pair_proto.sequence_index] = LastVisibleGoal(goal, completed_goal_sequence_pair_proto.is_mandatory)

        for pair_proto in gameplay_scenario_data_msg.sim_filter_sim_info_pair:
            self._loaded_sim_filter_id_to_sim_info_id_map[pair_proto.sim_filter_id] = pair_proto.sim_info_id

        for phase_output_info in gameplay_scenario_data_msg.last_phase_outputs:
            self._last_phase_outputs[phase_output_info.phase_guid64] = (phase_output_info.output_key,
             phase_output_info.next_phase,
             phase_output_info.output_time)

        for terminated_phase_info in gameplay_scenario_data_msg.terminated_phase_infos:
            self._terminated_phase_infos[terminated_phase_info.phase_guid64] = terminated_phase_info.termination_time

    def activate_goal(self, active_goal):
        self._active_goals.append(active_goal)
        self.apply_loot(active_goal.scenario_goal.loot_on_instantiate)

    def validate_sim_infos--- This code section failed: ---

 L.1450         0  LOAD_GLOBAL              services
                2  LOAD_METHOD              sim_info_manager
                4  CALL_METHOD_0         0  '0 positional arguments'
                6  STORE_FAST               'sim_info_manager'

 L.1451         8  SETUP_LOOP          106  'to 106'
               10  LOAD_FAST                'self'
               12  LOAD_ATTR                _loaded_sim_filter_id_to_sim_info_id_map
               14  LOAD_METHOD              items
               16  CALL_METHOD_0         0  '0 positional arguments'
               18  GET_ITER         
               20  FOR_ITER            104  'to 104'
               22  UNPACK_SEQUENCE_2     2 
               24  STORE_FAST               'sim_filter_id'
               26  STORE_FAST               'sim_info_id'

 L.1452        28  LOAD_FAST                'sim_info_manager'
               30  LOAD_METHOD              get
               32  LOAD_FAST                'sim_info_id'
               34  CALL_METHOD_1         1  '1 positional argument'
               36  STORE_FAST               'sim_info'

 L.1453        38  LOAD_FAST                'sim_info'
               40  LOAD_CONST               None
               42  COMPARE_OP               is
               44  POP_JUMP_IF_TRUE     74  'to 74'
               46  LOAD_FAST                'sim_info'
               48  LOAD_ATTR                can_instantiate_sim
               50  POP_JUMP_IF_FALSE    74  'to 74'

 L.1454        52  LOAD_FAST                'sim_info'
               54  LOAD_ATTR                death_type
               56  LOAD_CONST               None
               58  COMPARE_OP               is-not
               60  POP_JUMP_IF_FALSE    92  'to 92'
               62  LOAD_FAST                'sim_info'
               64  LOAD_ATTR                death_type
               66  LOAD_GLOBAL              DeathType
               68  LOAD_ATTR                NONE
               70  COMPARE_OP               !=
               72  POP_JUMP_IF_FALSE    92  'to 92'
             74_0  COME_FROM            50  '50'
             74_1  COME_FROM            44  '44'

 L.1455        74  LOAD_FAST                'self'
               76  LOAD_METHOD              end_scenario
               78  LOAD_FAST                'self'
               80  LOAD_ATTR                outcome_on_validation_failed
               82  LOAD_FAST                'self'
               84  LOAD_ATTR                _active_phase
               86  CALL_METHOD_2         2  '2 positional arguments'
               88  POP_TOP          

 L.1456        90  BREAK_LOOP       
             92_0  COME_FROM            72  '72'
             92_1  COME_FROM            60  '60'

 L.1457        92  LOAD_FAST                'sim_info'
               94  LOAD_FAST                'self'
               96  LOAD_ATTR                _sim_filter_id_to_sim_info_map
               98  LOAD_FAST                'sim_filter_id'
              100  STORE_SUBSCR     
              102  JUMP_BACK            20  'to 20'
              104  POP_BLOCK        
            106_0  COME_FROM_LOOP        8  '8'

Parse error at or near `JUMP_BACK' instruction at offset 102

    def get_phase_with_id(self, phase_id):
        if self.starting_phase is not None:
            return find_phase_with_id(self.starting_phase, phase_id)

    def get_all_phases(self):

        def traverse_next_phases(phase, phases):
            if phase in phases:
                return
            phases.add(phase)
            for phase_output in phase.phase_outputs:
                if phase_output.output.output.next_phase is not None:
                    traverse_next_phases(phase_output.output.output.next_phase, phases)

            if phase.phase_fallback_output.output.next_phase is not None:
                traverse_next_phases(phase.phase_fallback_output.output.next_phase, phases)

        all_phases = set()
        if self.starting_phase is not None:
            traverse_next_phases(self.starting_phase, all_phases)
        return all_phases

    @property
    def sim_time_lapsed(self):
        if self._sim_time_marker is None:
            return self._sim_time_lapsed
        delta_time_span = services.time_service().sim_now - self._sim_time_marker
        return self._sim_time_lapsed + delta_time_span

    def _on_goal_completed(self, goal, is_completed):
        completed_goal = goal if is_completed else None
        if self.starting_phase is None:
            self._scenario_tracker.send_goal_update_op_to_client(completed_goal=completed_goal)
            self._scenario_tracker.on_goal_completed(goal, is_completed)
        else:
            if is_completed and self._active_phase is not None:
                self.update_goal_sequences_on_complete(goal)
                self._scenario_tracker.send_goal_update_op_to_client(completed_goal=completed_goal)
                completed_goal.decommision()
                services.get_event_manager().process_event((test_events.TestEvent.ScenarioGoalCompleted), None, situation_goal=completed_goal)
                if not self.is_there_mandatory_active_goals():
                    if self._active_phase is not None:
                        self._active_phase.choose_output_and_progress(PhaseEndingReason.COMPLETE)
            else:
                self._scenario_tracker.send_goal_update_op_to_client(completed_goal=completed_goal)

    def update_goal_sequences_on_complete(self, completed_goal):
        completed_goal.unregister_for_on_goal_completed_callback(self._on_goal_completed)
        if self._active_phase is None:
            return
        next_goal_in_sequence_found = False
        for sequence_index, goal_tuple in enumerate(self._active_phase.goals):
            if next_goal_in_sequence_found:
                break
            for index, phase_goal in enumerate(goal_tuple.goal_sequence):
                if phase_goal.goal.situation_goal.guid64 == completed_goal.guid64:
                    if completed_goal.is_visible:
                        self._last_completed_visible_goal_for_sequence[sequence_index] = LastVisibleGoal(completed_goal, phase_goal.goal.mandatory)
                    if len(goal_tuple.goal_sequence) > index + 1:
                        goal_to_add = self.generate_active_goal_tuple_from_sequence(goal_tuple.goal_sequence, index + 1)
                        self.activate_goal(goal_to_add)
                        self.setup_goal(self._active_goals[-1].situation_goal)
                        next_goal_in_sequence_found = True
                    break

        found_in_active_goals = False
        for active_goal in self._active_goals:
            if active_goal.situation_goal.id == completed_goal.id:
                self.apply_loot(active_goal.scenario_goal.goal_loot)
                found_in_active_goals = True
                completion_time = services.time_service().sim_now.absolute_ticks()
                self._completed_goal_infos[active_goal.situation_goal.guid64] = completion_time
                break

        if found_in_active_goals:
            self._active_goals.remove(active_goal)

    def is_there_mandatory_active_goals(self):
        for active_goal in self._active_goals:
            if active_goal.scenario_goal.mandatory:
                return True

        return False

    def is_phase_active(self, phase_guid64):
        return self.current_phase_id == phase_guid64

    def is_phase_triggered(self, phase_guid64):
        return phase_guid64 in self._triggered_phases_guid64

    def is_phase_skipped(self, phase_guid64):
        return phase_guid64 in self._skipped_phases_guid64

    def is_phase_terminated(self, phase_guid64):
        return phase_guid64 in self._terminated_phase_infos

    def get_phase_termination_time(self, phase_guid64):
        return self._terminated_phase_infos.get(phase_guid64)

    @property
    def instance_id(self):
        return self._instance_id

    @property
    def current_phase(self):
        return self._active_phase

    @property
    def current_phase_id(self):
        if self._active_phase:
            return self._active_phase.guid64


@assertions.not_recursive
def find_phase_with_id(phase, phase_guid64):
    if phase.guid64 == phase_guid64:
        return phase
    for phase_output in phase.phase_outputs:
        if phase_output.output.output.next_phase is not None:
            found_phase = find_phase_with_id(phase_output.output.output.next_phase, phase_guid64)
            if found_phase is not None:
                return found_phase

    if phase.phase_fallback_output.output.next_phase is not None:
        found_phase = find_phase_with_id(phase.phase_fallback_output.output.next_phase, phase_guid64)
        if found_phase is not None:
            return found_phase


def get_sim_debt_time():
    time_service = services.time_service()
    if time_service:
        return time_service.get_simulator_debt()
    return 0
