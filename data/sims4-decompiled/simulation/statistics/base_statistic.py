# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\statistics\base_statistic.py
# Compiled at: 2020-11-04 23:18:35
# Size of source mod 2**32: 31952 bytes

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
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD _come_froms
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr DUP_TOP . designList
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
aug_assign2 ::= expr DUP_TOP . LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR . expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr . inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op . ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO . STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR . 
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
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
compare ::= compare_single . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
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
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= list . 
expr ::= or . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
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
for_iter ::= \e__come_froms . FOR_ITER
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
ifelsestmtc ::= testexpr c_stmts_opt JUMP_ABSOLUTE . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jump_absolute_else else_suitec . 
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
iflaststmt ::= testexpr c_stmts JUMP_ABSOLUTE . 
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
inplace_op ::= INPLACE_TRUE_DIVIDE . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= JUMP_ABSOLUTE . ELSE
jump_absolute_else ::= JUMP_ABSOLUTE . _come_froms
jump_absolute_else ::= JUMP_ABSOLUTE \e__come_froms . 
jump_absolute_else ::= JUMP_ABSOLUTE _come_froms . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
list ::= BUILD_LIST_0 . 
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
list_comp ::= BUILD_LIST_0 . list_iter
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c _come_froms
list_if ::= expr . jmp_false list_iter
list_if ::= expr . jmp_false list_iter COME_FROM
list_if ::= expr . jmp_false37 list_iter
list_if_not ::= expr . jmp_true list_iter
list_if_not ::= expr . jmp_true list_iter COME_FROM
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
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign2 . 
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
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
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
   
 L. 472       170  LOAD_FAST                'self'
                 172  DUP_TOP          
                 174  LOAD_ATTR                _statistic_multiplier_decrease
                 176  LOAD_FAST                'value'
                 178  LOAD_ATTR                multiplier
                 180  INPLACE_TRUE_DIVIDE
                 182  ROT_TWO          
                 184  STORE_ATTR               _statistic_multiplier_decrease
->             186_0  COME_FROM_LOOP       78  '78'
                 186  JUMP_FORWARD        200  'to 200'
               188_0  COME_FROM            54  '54'
from collections import namedtuple
from interactions import ParticipantType
from objects import ALL_HIDDEN_REASONS
from sims.lod_mixin import HasTunableLodMixin
from sims.sim_info_lod import SimInfoLODLevel
from sims4.tuning.tunable import Tunable
from sims4.utils import classproperty, flexmethod, flexproperty, constproperty
from statistics.base_statistic_listener import BaseStatisticCallbackListener
import caches, enum, sims4.log, sims4.math
__unittest__ = 'test.statistics.base_statistic_tests'
logger = sims4.log.Logger('SimStatistics')

class StatisticChangeDirection(enum.Int):
    INCREASE = 0
    DECREASE = 1
    BOTH = 2


class GalleryLoadBehavior(enum.Int):
    DONT_LOAD = 0
    LOAD_ONLY_FOR_OBJECT = 1
    LOAD_ONLY_FOR_SIM = 2
    LOAD_FOR_ALL = 3


class BaseStatistic(HasTunableLodMixin):
    INSTANCE_TUNABLES = {'respect_lod_on_add': Tunable(description='\n            If enabled then we will not add the statistic if the LOD value of the Sim\n            is lower than the required LOD of the statistic.  Otherwise instanced\n            Sims will be allowed to get statistics of higher LOD values.\n            ',
                             tunable_type=bool,
                             default=False)}
    decay_rate = 0.0
    _utility_curve = None
    SkillBasedMultiplier = namedtuple('SkillBasedMultiplier', ['curve', 'use_effective_skill'])
    _skill_based_statistic_multipliers_increase = {}
    _skill_based_statistic_multipliers_decrease = {}

    def __init__(self, tracker, initial_value):
        self._tracker = tracker
        self._value = initial_value
        self._locked = 0
        self._statistic_modifier = 0
        self._statistic_modifiers = None
        self._statistic_multiplier_increase = 1.0
        self._statistic_multiplier_decrease = 1.0
        self._statistic_multipliers = None
        self._statistic_callback_listeners = []
        self.state_backed = False

    def __repr__(self):
        statistic_type_name = type(self).__mro__[1].__name__
        statistic_instance_name = type(self).__name__
        return '{}({}@{})'.format(statistic_type_name, statistic_instance_name, self.get_value())

    @classproperty
    def max_value(cls):
        raise NotImplementedError

    @classproperty
    def min_value(cls):
        raise NotImplementedError

    @classproperty
    def best_value(cls):
        raise NotImplementedError

    @classmethod
    def added_by_default(cls, min_range=None, max_range=None):
        return True

    @classproperty
    def persisted(cls):
        raise NotImplementedError

    @classproperty
    def stat_type(cls):
        return cls

    @classmethod
    def type_id(cls):
        return cls.guid64

    @classmethod
    def get_skill_based_statistic_multiplier(cls, targets, add_amount):
        multiplier = 1
        if add_amount < 0:
            if cls not in cls._skill_based_statistic_multipliers_decrease:
                return multiplier
            skill_map = cls._skill_based_statistic_multipliers_decrease.get(cls)
        else:
            if cls not in cls._skill_based_statistic_multipliers_increase:
                return multiplier
            skill_map = cls._skill_based_statistic_multipliers_increase.get(cls)
        for target in targets:
            for skill_type, modifier in skill_map.items():
                skill_or_skill_type = target.get_stat_instance(skill_type) or skill_type
                if modifier.use_effective_skill:
                    value = target.Buffs.get_effective_skill_level(skill_or_skill_type)
                else:
                    value = skill_or_skill_type.get_user_value()
                multiplier *= modifier.curve.get(value)

        return multiplier

    @classmethod
    def add_skill_based_statistic_multiplier(cls, skill_type, curve, direction, use_effective_skill):
        increase_dict = cls._skill_based_statistic_multipliers_increase
        decrease_dict = cls._skill_based_statistic_multipliers_decrease
        if direction != StatisticChangeDirection.DECREASE:
            if cls not in increase_dict:
                increase_dict[cls] = {}
            increase_dict[cls][skill_type] = cls.SkillBasedMultiplier(curve, use_effective_skill)
        if direction != StatisticChangeDirection.INCREASE:
            if cls not in decrease_dict:
                decrease_dict[cls] = {}
            decrease_dict[cls][skill_type] = cls.SkillBasedMultiplier(curve, use_effective_skill)

    @classproperty
    def continuous(self):
        return False

    @classproperty
    def stat_name(self):
        pass

    def get_statistic_multiplier_increase(self):
        return self._statistic_multiplier_increase

    def get_statistic_multiplier_decrease(self):
        return self._statistic_multiplier_decrease

    def on_add(self):
        pass

    def on_remove(self, on_destroy=False):
        owner = self._tracker.owner if self._tracker is not None else None
        if owner is not None:
            if not owner.is_sim:
                self._tracker = None
        for callback_listener in self._statistic_callback_listeners:
            callback_listener.destroy()

        self._statistic_callback_listeners.clear()

    def on_recovery(self):
        pass

    @property
    def tracker(self):
        return self._tracker

    def get_asm_param(self, *_):
        return (None, None)

    @flexmethod
    def get_value(cls, inst):
        if inst is not None:
            return inst._value
        return cls.default_value

    @flexmethod
    def get_saved_value(cls, inst):
        cls_or_inst = inst if inst is not None else cls
        value = cls_or_inst.get_value()
        return value

    def _update_callback_listeners(self, old_value=0, new_value=0, resort_list=True):
        for callback_listener in tuple(self._statistic_callback_listeners):
            if callback_listener.threshold.compare(new_value):
                callback_listener.trigger_callback()

    def set_value(self, value, **kwargs):
        old_value = self._value
        self._value = value
        self._clamp()
        self._notify_change(old_value)

    def _notify_change(self, old_value):
        value = self.get_value()
        if old_value != value:
            if self._tracker is not None:
                self._tracker.notify_watchers(self.stat_type, old_value, value)
        if not caches.skip_cache:
            caches.clear_all_caches()
        self._update_callback_listeners(old_value, value)

    def add_value(self, add_amount, interaction=None, from_load=False, **kwargs):
        tracker = self._tracker
        if tracker is not None:
            if tracker.owner is not None:
                if tracker.owner.is_locked(self):
                    return
        else:
            multiplier = 1
            if interaction is not None:
                sims = interaction.get_participants(ParticipantType.AllSims)
                multiplier = self.get_skill_based_statistic_multiplier(sims, add_amount)
            if add_amount < 0:
                multiplier *= self.get_statistic_multiplier_decrease()
            else:
                multiplier *= self.get_statistic_multiplier_increase()
        add_amount *= multiplier
        if tracker is not None:
            tracker.notify_delta(self.stat_type, add_amount)
        (self._add_value)(add_amount, from_load=from_load, **kwargs)

    def _add_value(self, amount, min_value=None, max_value=None, from_load=False, **kwargs):
        curr_value = self.get_value()
        new_value = curr_value + amount
        if max_value is not None:
            if curr_value < max_value:
                new_value = min(new_value, max_value)
            else:
                return
        if min_value is not None:
            if curr_value > min_value:
                new_value = max(new_value, min_value)
            else:
                return
        (self.set_value)(new_value, from_load=from_load, **kwargs)

    @flexmethod
    def get_user_value(cls, inst):
        inst_or_cls = inst if inst is not None else cls
        return inst_or_cls.convert_to_user_value(inst_or_cls.get_value())

    def set_user_value(self, value):
        self.set_value(self.convert_from_user_value(value))

    def add_statistic_modifier(self, value):
        if value == 0:
            logger.debug('Attempting to add statistic modifier with value zero to {}', self)
            return
        logger.debug('Adding statistic modifier of {} to {}', value, self)
        if self._statistic_modifiers is None:
            self._statistic_modifiers = []
        self._statistic_modifiers.append(value)
        self._statistic_modifier += value
        self._on_statistic_modifier_changed()

    def remove_statistic_modifier(self, value):
        if self._statistic_modifiers is None:
            return
        else:
            if value in self._statistic_modifiers:
                logger.debug('Removing statistic modifier of {} from {}', value, self)
                self._statistic_modifiers.remove(value)
                if self._statistic_modifiers:
                    self._statistic_modifier -= value
                else:
                    self._statistic_modifier = 0
                self._on_statistic_modifier_changed()
            self._statistic_modifiers = self._statistic_modifiers or None

    def _recalculate_statistic_multiplier(self, value):
        if value.apply_direction == StatisticChangeDirection.BOTH or value.apply_direction == StatisticChangeDirection.INCREASE:
            self._statistic_multiplier_increase *= value.multiplier
        if value.apply_direction == StatisticChangeDirection.BOTH or value.apply_direction == StatisticChangeDirection.DECREASE:
            self._statistic_multiplier_decrease *= value.multiplier

    def add_statistic_multiplier(self, value):
        logger.debug('Adding statistic multiplier of {} to {}', value, self)
        if self._statistic_multipliers is None:
            self._statistic_multipliers = []
        self._statistic_multipliers.append(value)
        self._recalculate_statistic_multiplier(value)
        self._on_statistic_modifier_changed(notify_watcher=(self._statistic_modifier != 0))

    def remove_statistic_multiplier--- This code section failed: ---

 L. 452         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _statistic_multipliers
                4  LOAD_CONST               None
                6  COMPARE_OP               is
                8  POP_JUMP_IF_FALSE    14  'to 14'

 L. 453        10  LOAD_CONST               None
               12  RETURN_VALUE     
             14_0  COME_FROM             8  '8'

 L. 455        14  LOAD_FAST                'value'
               16  LOAD_FAST                'self'
               18  LOAD_ATTR                _statistic_multipliers
               20  COMPARE_OP               in
               22  POP_JUMP_IF_FALSE   218  'to 218'

 L. 456        24  LOAD_GLOBAL              logger
               26  LOAD_METHOD              debug
               28  LOAD_STR                 'Removing statistic multiplier of {} from {}'
               30  LOAD_FAST                'value'
               32  LOAD_FAST                'self'
               34  CALL_METHOD_3         3  '3 positional arguments'
               36  POP_TOP          

 L. 457        38  LOAD_FAST                'self'
               40  LOAD_ATTR                _statistic_multipliers
               42  LOAD_METHOD              remove
               44  LOAD_FAST                'value'
               46  CALL_METHOD_1         1  '1 positional argument'
               48  POP_TOP          

 L. 458        50  LOAD_FAST                'self'
               52  LOAD_ATTR                _statistic_multipliers
               54  POP_JUMP_IF_FALSE   188  'to 188'

 L. 459        56  LOAD_FAST                'value'
               58  LOAD_ATTR                multiplier
               60  LOAD_CONST               0
               62  COMPARE_OP               ==
               64  POP_JUMP_IF_FALSE   106  'to 106'

 L. 462        66  LOAD_CONST               1.0
               68  LOAD_FAST                'self'
               70  STORE_ATTR               _statistic_multiplier_increase

 L. 463        72  LOAD_CONST               1.0
               74  LOAD_FAST                'self'
               76  STORE_ATTR               _statistic_multiplier_decrease

 L. 464        78  SETUP_LOOP          186  'to 186'
               80  LOAD_FAST                'self'
               82  LOAD_ATTR                _statistic_multipliers
               84  GET_ITER         
               86  FOR_ITER            102  'to 102'
               88  STORE_FAST               'statistic_multiplier'

 L. 465        90  LOAD_FAST                'self'
               92  LOAD_METHOD              _recalculate_statistic_multiplier
               94  LOAD_FAST                'statistic_multiplier'
               96  CALL_METHOD_1         1  '1 positional argument'
               98  POP_TOP          
              100  JUMP_BACK            86  'to 86'
              102  POP_BLOCK        
              104  JUMP_ABSOLUTE       200  'to 200'
            106_0  COME_FROM            64  '64'

 L. 467       106  LOAD_FAST                'value'
              108  LOAD_ATTR                apply_direction
              110  LOAD_GLOBAL              StatisticChangeDirection
              112  LOAD_ATTR                BOTH
              114  COMPARE_OP               ==
              116  POP_JUMP_IF_TRUE    130  'to 130'

 L. 468       118  LOAD_FAST                'value'
              120  LOAD_ATTR                apply_direction
              122  LOAD_GLOBAL              StatisticChangeDirection
              124  LOAD_ATTR                INCREASE
              126  COMPARE_OP               ==
              128  POP_JUMP_IF_FALSE   146  'to 146'
            130_0  COME_FROM           116  '116'

 L. 469       130  LOAD_FAST                'self'
              132  DUP_TOP          
              134  LOAD_ATTR                _statistic_multiplier_increase
              136  LOAD_FAST                'value'
              138  LOAD_ATTR                multiplier
              140  INPLACE_TRUE_DIVIDE
              142  ROT_TWO          
              144  STORE_ATTR               _statistic_multiplier_increase
            146_0  COME_FROM           128  '128'

 L. 470       146  LOAD_FAST                'value'
              148  LOAD_ATTR                apply_direction
              150  LOAD_GLOBAL              StatisticChangeDirection
              152  LOAD_ATTR                BOTH
              154  COMPARE_OP               ==
              156  POP_JUMP_IF_TRUE    170  'to 170'

 L. 471       158  LOAD_FAST                'value'
              160  LOAD_ATTR                apply_direction
              162  LOAD_GLOBAL              StatisticChangeDirection
              164  LOAD_ATTR                DECREASE
              166  COMPARE_OP               ==
              168  POP_JUMP_IF_FALSE   200  'to 200'
            170_0  COME_FROM           156  '156'

 L. 472       170  LOAD_FAST                'self'
              172  DUP_TOP          
              174  LOAD_ATTR                _statistic_multiplier_decrease
              176  LOAD_FAST                'value'
              178  LOAD_ATTR                multiplier
              180  INPLACE_TRUE_DIVIDE
              182  ROT_TWO          
              184  STORE_ATTR               _statistic_multiplier_decrease
            186_0  COME_FROM_LOOP       78  '78'
              186  JUMP_FORWARD        200  'to 200'
            188_0  COME_FROM            54  '54'

 L. 474       188  LOAD_CONST               1.0
              190  LOAD_FAST                'self'
              192  STORE_ATTR               _statistic_multiplier_increase

 L. 475       194  LOAD_CONST               1.0
              196  LOAD_FAST                'self'
              198  STORE_ATTR               _statistic_multiplier_decrease
            200_0  COME_FROM           186  '186'
            200_1  COME_FROM           168  '168'

 L. 476       200  LOAD_FAST                'self'
              202  LOAD_ATTR                _on_statistic_modifier_changed
              204  LOAD_FAST                'self'
              206  LOAD_ATTR                _statistic_modifier
              208  LOAD_CONST               0
              210  COMPARE_OP               !=
              212  LOAD_CONST               ('notify_watcher',)
              214  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              216  POP_TOP          
            218_0  COME_FROM            22  '22'

 L. 478       218  LOAD_FAST                'self'
              220  LOAD_ATTR                _statistic_multipliers
              222  POP_JUMP_IF_TRUE    230  'to 230'

 L. 479       224  LOAD_CONST               None
              226  LOAD_FAST                'self'
              228  STORE_ATTR               _statistic_multipliers
            230_0  COME_FROM           222  '222'

Parse error at or near `COME_FROM_LOOP' instruction at offset 186_0

    def _on_statistic_modifier_changed(self, notify_watcher=True):
        if notify_watcher:
            if self._tracker is not None:
                value = self.get_value()
                self._tracker.notify_watchers(self.stat_type, value, value)

    @classproperty
    def default_value(cls):
        return 0

    @classmethod
    def convert_to_user_value(cls, value):
        return value

    @classmethod
    def convert_from_user_value(cls, user_value):
        return user_value

    @property
    def core(self):
        return False

    @flexmethod
    def remove_at_owner_lod(cls, inst, lod=None, owner=None):
        owner = inst._tracker.owner if (inst is not None and inst._tracker is not None) else owner
        owner_is_sim = owner is not None and owner.is_sim
        if owner_is_sim:
            if lod is None:
                lod = owner.lod
        elif lod is None:
            return False
            inst_or_cls = inst if inst is not None else cls
            if owner_is_sim and not inst_or_cls.respect_lod_on_add:
                if owner.can_instantiate_sim and owner.is_instanced(allow_hidden_flags=ALL_HIDDEN_REASONS):
                    min_lod_value = min(SimInfoLODLevel.BACKGROUND, inst_or_cls.min_lod_value)
        else:
            min_lod_value = inst_or_cls.min_lod_value
        return lod < min_lod_value

    @property
    def is_visible(self):
        return False

    @classproperty
    def is_scored(cls):
        if cls._utility_curve:
            return True
        return False

    @flexproperty
    def autonomous_desire(cls, inst):
        this = inst if inst is not None else cls
        if this._utility_curve:
            return this._utility_curve.get(this.get_value())
        return 0

    @classproperty
    def autonomy_weight(cls):
        return 1

    @classproperty
    def use_stat_value_on_initialization(cls):
        return True

    def lock(self):
        self._locked += 1

    def unlock(self):
        if self._locked > 0:
            self._locked -= 1
        else:
            logger.warn('BaseStatistic._locked variable became out of sync.')

    @classmethod
    def clamp(cls, value):
        return sims4.math.clamp(cls.min_value, value, cls.max_value)

    def _clamp(self, value=None):
        if value is None:
            value = self._value
        self._value = sims4.math.clamp(self.min_value, value, self.max_value)

    @classmethod
    def _build_utility_curve_from_tuning_data(cls, data, weight=1):
        if data:
            point_list = [(point.x, point.y) for point in data]
            cls._utility_curve = sims4.math.WeightedUtilityCurve(point_list, max_y=1, weight=weight)

    @classmethod
    def can_add(cls, owner):
        return True

    @constproperty
    def is_skill():
        return False

    @constproperty
    def is_commodity():
        return False

    @constproperty
    def is_ranked():
        return False

    @classmethod
    def save_for_delayed_active_lod(cls, commodity_proto, commodities, skills, ranked_statistics):
        return NotImplementedError

    def get_save_message(self, tracker):
        return NotImplementedError

    def save_statistic(self, commodities, skills, ranked_stats, tracker):
        return NotImplementedError

    @classproperty
    def add_if_not_in_tracker(cls):
        return True

    @property
    def instance_required(self):
        return not (self.get_value() == self.default_value and self._statistic_modifier == 0)

    @property
    def _callback_queue_head(self):
        if self._statistic_callback_listeners:
            return self._statistic_callback_listeners[0]

    def create_callback_listener(self, threshold, callback, on_callback_alarm_reset=None, should_seed=True):
        return BaseStatisticCallbackListener(self, (self.stat_type), threshold, callback, on_callback_alarm_reset, should_seed=should_seed)

    def create_callback_listener_seed(stat_type, threshold, callback, on_callback_alarm_reset=None):
        return BaseStatisticCallbackListener(None, stat_type, threshold, callback, on_callback_alarm_reset)

    def create_and_add_callback_listener(self, threshold, callback, on_callback_alarm_reset=None, should_seed=True):
        callback_listener = self.create_callback_listener(threshold, callback, on_callback_alarm_reset=on_callback_alarm_reset, should_seed=should_seed)
        self.add_callback_listener(callback_listener)
        return callback_listener

    def add_callback_listener(self, callback_listener, update_active_callback=True) -> type(None):
        self._insert_callback_listener(callback_listener)

    def _validate_callback_listener(self, callback_listener):
        if callback_listener is None:
            logger.warn('Adding None callback listener to {}', self)
        else:
            if callback_listener.is_seed:
                logger.warn('Adding seed callback listener to {}', self)
            else:
                if callback_listener.statistic_type != self.stat_type:
                    logger.warn('Adding incompatible callback listener to {}', self)
                else:
                    if callback_listener in self._statistic_callback_listeners:
                        logger.error('Adding listener {} to {} that already exists', callback_listener, self)

    def _insert_callback_listener(self, callback_listener: BaseStatisticCallbackListener):
        self._statistic_callback_listeners.append(callback_listener)

    def remove_callback_listener(self, callback_listener: BaseStatisticCallbackListener):
        if callback_listener in self._statistic_callback_listeners:
            self._statistic_callback_listeners.remove(callback_listener)
            callback_listener.destroy()
            return True
        logger.debug('Failed to remove callback from queue because it was already removed: {}', callback_listener)
        return False

    def release_control_on_all_callback_listeners(self):
        ret = self._statistic_callback_listeners
        self._statistic_callback_listeners = []
        return ret

    @classmethod
    def get_categories(cls):
        return ()

    @classproperty
    def valid_for_stat_testing(cls):
        return False

    @flexmethod
    def get_normalized_value(cls, inst):
        inst_or_cls = inst if inst is not None else cls
        value = inst_or_cls.get_value()
        return cls.convert_to_normalized_value(value)

    @classmethod
    def convert_to_normalized_value(cls, value):
        min_value = cls.min_value
        max_value = cls.max_value
        normalized_value = (value - min_value) / (max_value - min_value)
        return normalized_value
