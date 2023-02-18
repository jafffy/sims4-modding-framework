# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\venues\venue_tuning.py
# Compiled at: 2022-03-30 21:04:46
# Size of source mod 2**32: 66934 bytes

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
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
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
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
list ::= BUILD_LIST_0 . 
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
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
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
testfalse_not_and ::= and . jmp_true come_froms
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
   
 L.1046       226  LOAD_FAST                'venue_game_service'
                 228  LOAD_METHOD              set_provider
                 230  LOAD_GLOBAL              services
                 232  LOAD_METHOD              current_zone_id
                 234  CALL_METHOD_0         0  '0 positional arguments'
                 236  LOAD_FAST                'self'
                 238  LOAD_ATTR                _civic_policy_provider
                 240  CALL_METHOD_2         2  '2 positional arguments'
                 242  POP_TOP          
               244_0  COME_FROM           194  '194'
->             244_1  COME_FROM           160  '160'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
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
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
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
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_8
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
comp_body ::= gen_comp_body . 
comp_for ::= expr . get_for_iter store comp_iter CONTINUE
comp_for ::= expr . get_for_iter store comp_iter JUMP_BACK
comp_if ::= expr . jmp_false comp_iter
comp_if ::= expr jmp_false . comp_iter
comp_if ::= expr jmp_false comp_iter . 
comp_if_not ::= expr . jmp_true comp_iter
comp_iter ::= comp_body . 
comp_iter ::= comp_if . 
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
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict ::= expr expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_8
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_51
dict_comp_body ::= expr . expr MAP_ADD
dict_comp_body ::= expr expr . MAP_ADD
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= list . 
expr ::= or . 
expr ::= yield . 
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
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
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
gen_comp_body ::= expr . YIELD_VALUE POP_TOP
gen_comp_body ::= expr YIELD_VALUE . POP_TOP
gen_comp_body ::= expr YIELD_VALUE POP_TOP . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1 . 
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG . _come_froms FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK . _come_froms
genexpr_func ::= LOAD_ARG \e__come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms . 
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms . FOR_ITER store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER . store comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter \e__come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store . comp_iter _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter . _come_froms JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK \e__come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms . JUMP_BACK _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK . _come_froms
genexpr_func ::= LOAD_ARG _come_froms FOR_ITER store comp_iter \e__come_froms JUMP_BACK \e__come_froms . 
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
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
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
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
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list_comp ::= BUILD_LIST_0 . list_iter
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_4
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR . LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR LOAD_STR . 
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
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
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
set_comp_body ::= expr . SET_ADD
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
stmt ::= function_def . 
stmt ::= genexpr_func . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
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
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
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
yield ::= expr YIELD_VALUE . 
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1287        46  JUMP_BACK            12  'to 12'
->                48  POP_BLOCK        
                50_0  COME_FROM_LOOP        4  '4'
from _collections import defaultdict
import random
from interactions.utils.tunable_icon import TunableIcon
from sims4.localization import TunableLocalizedString, TunableLocalizedStringFactory, TunableLocalizedStringVariant
from sims4.tuning.geometric import TunableCurve
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import Tunable, TunableList, TunableTuple, TunableResourceKey, TunableReference, AutoFactoryInit, HasTunableSingletonFactory, TunableVariant, OptionalTunable, TunableEnumEntry, TunableEnumFlags, TunableRange, TunableMapping, TunableSet
from sims4.tuning.tunable_base import ExportModes, GroupNames
from sims4.utils import classproperty
import enum, sims4.log, sims4.resources, sims4.tuning
from buffs.tunable import TunableBuffReference
from clubs.club_enums import ClubHangoutSetting
from event_testing.resolver import SingleSimResolver
from objects.doors.door_enums import VenueFrontdoorRequirement
from scheduler import SituationWeeklySchedule, WeeklySchedule
from sims.sim_info_types import Species
from situations.situation import Situation
from situations.situation_guest_list import SituationGuestList, SituationInvitationPurpose, SituationGuestInfo
from situations.situation_types import GreetedStatus
from ui.ui_tuning import TunableUiMessage
from venues.civic_policies.venue_civic_policy_provider import VenueCivicPolicyProvider
from venues.npc_summoning import ResidentialLotArrivalBehavior, CreateAndAddToSituation, AddToBackgroundSituation, NotfifyZoneDirector
from venues.venue_enums import TierBannerAppearanceState, VenueTypes, VenueFlags
from venues.venue_object_test import TunableVenueObjectWithPair
import date_and_time, services, tag, venues, zone_director
logger = sims4.log.Logger('Venues')

class ResidentialZoneFixupForNPC(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'description':'\n            Specify what to do with a non resident NPC on a residential lot\n            when the zone has to be fixed up on load. \n            This fix up will occur if sim time or the\n            active household has changed since the zone was last saved.\n            ', 
     'player_lot_greeted':CreateAndAddToSituation.TunableFactory(), 
     'npc_lot_greeted':CreateAndAddToSituation.TunableFactory(), 
     'npc_lot_ungreeted':CreateAndAddToSituation.TunableFactory()}

    def __call__(self, npc_infos, purpose=None):
        situation_manager = services.get_zone_situation_manager()
        is_active_household_residence = False
        active_household = services.active_household()
        if active_household is not None:
            is_active_household_residence = active_household.considers_current_zone_its_residence()
        for sim_info in npc_infos:
            npc = sim_info.get_sim_instance()
            if npc is None:
                continue
            else:
                greeted_status = situation_manager.get_npc_greeted_status_during_zone_fixup(sim_info)
                if is_active_household_residence:
                    if greeted_status == GreetedStatus.GREETED:
                        logger.debug('Player lot greeted {} during zone fixup', sim_info, owner='sscholl')
                        self.player_lot_greeted((sim_info,))
                    else:
                        if greeted_status == GreetedStatus.WAITING_TO_BE_GREETED:
                            logger.debug('NPC lot waiting to be greeted {} during zone fixup', sim_info, owner='sscholl')
                            self.npc_lot_ungreeted((sim_info,))
                else:
                    if greeted_status == GreetedStatus.GREETED:
                        logger.debug('NPC lot greeted {} during zone fixup', sim_info, owner='sscholl')
                        self.npc_lot_greeted((sim_info,))
                logger.debug('No option for {} during zone fixup', sim_info, owner='sscholl')


class ResidentialTravelDisplayName(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'description':'\n        Specify the contextual string for when a user clicks to travel to an\n        adjacent lot in the street.\n        ', 
     'ring_doorbell_name':TunableLocalizedStringFactory(description='\n            The interaction name for when the actor doesn\'t know any Sims that live on the\n            destination lot.\n            \n            Tokens: 0:ActorSim\n            Example: "Ring Doorbell"\n            '), 
     'visit_sim_name':TunableLocalizedStringFactory(description='\n            The interaction name for when the actor knows exactly one Sim that lives on the\n            destination lot.\n            \n            Tokens: 0:ActorSim, 1:Sim known\n            Example: "Visit {1.SimName}"\n            '), 
     'visit_household_name':TunableLocalizedStringFactory(description='\n            The interaction name for when the actor knows more than one Sim\n            that lives on the destination lot, or the Sim they know is not at\n            home.\n            \n            Tokens: 0:ActorSim, 1:Household Name\n            Example: "Visit The {1.String} Household"\n            '), 
     'visit_the_household_plural_name':TunableLocalizedStringFactory(description='\n            The interaction name for when the actor knows more than one Sim\n            that lives on the destination lot, or the Sim they know is not at\n            home, and everyone who lives there has the same household name as\n            their last name.\n            \n            Tokens: 0:ActorSim, 1:Household Name\n            Example: "Visit The {1.String|enHouseholdNamePlural}"\n            '), 
     'no_one_home_encapsulation':TunableLocalizedStringFactory(description='\n            The string that gets appended on the end of our interaction string\n            if none of the household Sims at the destination lot are home.\n            \n            Tokens: 0:Interaction Name\n            Example: "{0.String} (No One At Home)"\n            '), 
     'go_here_name':TunableLocalizedStringFactory(description='\n            The interaction name for when no household lives on the destination\n            lot.\n            \n            Tokens: 0:ActorSim\n            Example: "Go Here"\n            '), 
     'go_home_name':TunableLocalizedStringFactory(description='\n            The interaction name for when the actor\'s home lot is the\n            destination lot.\n            \n            Tokens: 0:ActorSim\n            Example: "Go Home"\n            ')}

    def __call__(self, target, context):
        sim = context.sim
        lot_id = context.pick.lot_id
        if lot_id is None:
            return
            persistence_service = services.get_persistence_service()
            to_zone_id = persistence_service.resolve_lot_id_into_zone_id(lot_id)
            if to_zone_id is None:
                return
            if sim.sim_info.vacation_or_home_zone_id == to_zone_id:
                return self.go_home_name(sim)
            household_id = None
            lot_owner_info = persistence_service.get_lot_proto_buff(lot_id)
            if lot_owner_info is not None:
                for household in lot_owner_info.lot_owner:
                    household_id = household.household_id
                    break

            elif household_id:
                household = services.household_manager().get(household_id)
            else:
                household = None
            if household is None:
                return self.go_here_name(sim)
            sim_infos_known = False
            sim_infos_known_at_home = []
            sim_infos_at_home = False
            same_last_name = True
            for sim_info in household.sim_info_gen():
                if sim_info.relationship_tracker.get_all_bits(sim.id):
                    sim_infos_known = True
                    if sim_info.zone_id == to_zone_id:
                        sim_infos_known_at_home.append(sim_info)
                    else:
                        if sim_info.zone_id == to_zone_id:
                            sim_infos_at_home = True
                    same_last_name = sim_info.last_name == household.name or False

            travel_name = sim_infos_known or self.ring_doorbell_name(sim)
        else:
            if len(sim_infos_known_at_home) == 1:
                return self.visit_sim_name(sim, sim_infos_known_at_home[0])
                if same_last_name:
                    travel_name = self.visit_the_household_plural_name(sim, household.name)
                else:
                    travel_name = self.visit_household_name(sim, household.name)
            else:
                return sim_infos_at_home or self.no_one_home_encapsulation(travel_name)
            return travel_name


class CommercialTravelDisplayName(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'visit_venue_name': TunableLocalizedStringFactory(description='\n            The interaction name for when the actor visit this venue\n            \n            Tokens: 0:ActorSim\n            ')}

    def __call__(self, target, context):
        if context is None:
            return
        return self.visit_venue_name(context.sim)


class Venue(metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.VENUE)):
    NEW_VENUE_TUNING_GROUP = 'New Venue Dialog'
    NEW_VENUE_DIALOG_SPECIAL_CASES = TunableList(description="\n        A list of venues that will always be eligible for the new venue dialog, even if they aren't\n        compatible with the region, or displayed in the UI. Currently both of those things need to\n        be true in order to see the New Venue Dialog for a venue. Additions to this list will show\n        up without meeting those requirements.\n        \n        Example: High School isn't compatible with any regions and doesn't show up in the UI because\n        we don't want players creating their own high school lots. You need to edit the existing \n        high school lot instead. Adding the High School venue to this list will allow the New Venue\n        Dialog to be displayed from any region.\n        ",
      tunable=TunableReference(description='\n            A reference to the venue that you would like to be able to see the New Venue Dialog for\n            from any region, regardless of visibility in the UI or compatability with the current \n            region.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.VENUE)),
      pack_safe=True),
      export_modes=(ExportModes.ClientBinary))
    INSTANCE_TUNABLES = {'display_name':TunableLocalizedString(description='\n            Name that will be displayed for the venue\n            ',
       export_modes=ExportModes.All), 
     'display_name_with_tier':TunableLocalizedString(description='\n            Name that will be displayed in contexts where we also want to show\n            the current venue tier. If this venue has no venue tiers, this\n            name will be ignored and display_name will be used.\n            ',
       allow_none=True,
       export_modes=ExportModes.All), 
     'display_name_incomplete':TunableLocalizedString(description='\n            Name that will be displayed for the incomplete venue\n            ',
       allow_none=True,
       export_modes=ExportModes.All), 
     'venue_description':TunableLocalizedString(description='\n            Description of Venue that will be displayed\n            ',
       export_modes=ExportModes.All), 
     'venue_icon':TunableResourceKey(description='\n            Venue Icon for UI\n            ',
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       export_modes=ExportModes.All), 
     'venue_thumbnail':TunableResourceKey(description='\n            Image of Venue that will be displayed',
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       allow_none=True,
       export_modes=ExportModes.All), 
     'venue_buffs':TunableList(description='\n            A list of buffs that are added on Sims while they are instanced in\n            this venue.\n            ',
       tunable=TunableBuffReference(description='\n                A buff that exists on Sims while they are instanced in this\n                venue.\n                ',
       pack_safe=True)), 
     'venue_type':TunableEnumEntry(description="\n            The venue's functional type. Used to distinguish venues that function differently.\n            ",
       tunable_type=VenueTypes,
       default=VenueTypes.STANDARD,
       export_modes=ExportModes.All), 
     'venue_flags':TunableEnumFlags(description='\n            Venue flags used to mark a venue with specific properties.\n            ',
       enum_type=VenueFlags,
       allow_no_flags=True,
       default=VenueFlags.NONE,
       export_modes=ExportModes.All), 
     'allow_game_triggered_events':Tunable(description='\n            Whether this venue can have game triggered events. ex for careers\n            ',
       tunable_type=bool,
       default=False), 
     'background_event_schedule':SituationWeeklySchedule.TunableFactory(description='\n            The Background Events that run on this venue. They run underneath\n            any user facing Situations and there can only be one at a time. The\n            schedule times and durations are windows in which background events\n            can start.\n            '), 
     'special_event_schedule':SituationWeeklySchedule.TunableFactory(description='\n            The Special Events that run on this venue. These run on top of\n            Background Events. We run only one user facing event at a time, so\n            if the player started something then this may run in the\n            background, otherwise the player will be invited to join in on this\n            Venue Special Event.\n            '), 
     'required_objects':TunableList(description='\n            A list of objects that are required to be on a lot before\n            that lot can be labeled as this venue.\n            ',
       tunable=TunableVenueObjectWithPair(description="\n                Specify object tag(s) that must be on this venue. Allows you to\n                group objects, i.e. weight bench, treadmill, and basketball\n                goals are tagged as 'exercise objects.'\n                \n                This is not the same as automatic objects tuning. \n                Please read comments for both the fields.\n                "),
       export_modes=ExportModes.All), 
     'venue_tiers':TunableList(description='\n            A list of requirements where each requirement corresponds to a tier \n            that will be shown in the buildbuy tier UI. Tiers should be tuned\n            in order from worst (tier n) to best (tier 1), where worst is the\n            element of this list.\n            ',
       tunable=TunableTuple(required_object=TunableVenueObjectWithPair(description="\n                    Specify object tag(s) that must be on this venue. Allows you to\n                    group objects, i.e. weight bench, treadmill, and basketball\n                    goals are tagged as 'exercise objects.'\n                    \n                    This is not the same as automatic objects tuning. \n                    Please read comments for both the fields.\n                    "),
       icon=TunableIcon(description='\n                    If tuned, an icon to associate with this requirement in the UI.\n                    Currently only supported for venue tier requirements.\n                    ',
       export_modes=(ExportModes.All),
       allow_none=True),
       tier_banner_text=TunableLocalizedString(description='\n                    If tuned, text which will be displayed on the tier banner if\n                    this requirement is the current active tier requirement.\n                    ',
       export_modes=(ExportModes.All),
       allow_none=True),
       tier_banner_state=TunableEnumEntry(description='\n                    The state to set on the tier banner in the UI if this\n                    requirement is the current active tier requirement.\n                    ',
       tunable_type=TierBannerAppearanceState,
       default=(TierBannerAppearanceState.INVALID),
       export_modes=(ExportModes.All)),
       tier_name=TunableLocalizedString(description='\n                    If tuned, the name of this tier. This will be used in places \n                    where we want to display a tier, but will not be used in the\n                    requirements panel (that will still be object_display_name).\n                    ',
       export_modes=(ExportModes.All),
       allow_none=True),
       tier_name_two_lines=TunableLocalizedString(description='\n                    If tuned, the name of this tier. This will be used in places\n                    like the tier cell view where we need to format the tier\n                    name as Tier x\nTier Name.\n                    ',
       export_modes=(ExportModes.All),
       allow_none=True),
       zone_modifiers=TunableSet(description='\n                    A set of zone modifiers to apply if this requirement is met.\n                    These zone modifiers will be "hidden" from the UI and will not\n                    appear as lot traits in the lot trait molecule or manage worlds.\n                    ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ZONE_MODIFIER)),
       pack_safe=True),
       export_modes=(ExportModes.All)),
       export_class_name='TunableVenueTier'),
       export_modes=ExportModes.All), 
     'forbidden_objects':TunableList(description='\n            A list of objects that are not allowed on the lot.  If they are \n            placed, the lot cannot be labeled as this venue.\n            ',
       tunable=TunableVenueObjectWithPair(description="\n                Specify object tag(s) that can't be on this venue. Allows you to\n                group objects, i.e. weight bench, treadmill, and basketball\n                goals are tagged as 'exercise objects.'\n                \n                This is not the same as automatic objects tuning. \n                Please read comments for both the fields.\n                "),
       export_modes=ExportModes.All), 
     'tier_banner_max_fail_text':TunableLocalizedString(description='\n            If tuned, a message that will be displayed in the tier\n            banner if the venue fails to satisfy the lowest tier due to\n            being over the maximum for that tier requirement.\n            ',
       export_modes=ExportModes.All,
       allow_none=True), 
     'tier_banner_min_fail_text':TunableLocalizedString(description='\n            If tuned, a message that will be displayed in the tier\n            banner if the venue fails to satisfy the lowest tier due to\n            being under the minimum for that tier requirement.\n            ',
       export_modes=ExportModes.All,
       allow_none=True), 
     'npc_summoning_behavior':TunableMapping(description='\n            Whenever an NPC is summoned to a lot by the player, determine\n            which action to take based on the summoning purpose. The purpose\n            is a dynamic enum: venues.venue_constants.NPCSummoningPurpose.\n            \n            The action will generally involve either adding a sim to an existing\n            situation or creating a situation then adding them to it.\n            \n            \\depot\\Sims4Projects\\Docs\\Design\\Open Streets\\Open Street Invite Matrix.xlsx\n            \n            residential: This is behavior pushed on the NPC if this venue was a residential lot.\n            create_situation: Place the NPC in the specified situation/job pair.\n            add_to_background_situation: Add the NPC the currently running background \n            situation in the venue.\n            notify_zone_director: notifies the current zones zone director that\n            a sim needs to be spawned and lets the zone director handle it.\n            ',
       key_type=sims4.tuning.tunable.TunableEnumEntry(description='\n                The different reasons that we have for summoning an NPC. Every\n                time an NPC is summoned they are given one of these reasons\n                as a key to how we want to handle that Sim.\n                ',
       tunable_type=(venues.venue_constants.NPCSummoningPurpose),
       default=(venues.venue_constants.NPCSummoningPurpose.DEFAULT)),
       value_type=TunableMapping(description="\n                A mapping between species and the action we want to take.  If\n                a species doesn't have specific tuning then the Human species\n                tuning will be used instead.\n                ",
       key_type=TunableEnumEntry(description='\n                    The species that we want to use to perform this behavior.\n                    ',
       tunable_type=Species,
       default=(Species.HUMAN),
       invalid_enums=(
      Species.INVALID,)),
       value_type=TunableVariant(description='\n                    The behavior that we want to accomplish based on the summoning\n                    type.\n                    ',
       locked_args={'disabled': None},
       residential=(ResidentialLotArrivalBehavior.TunableFactory()),
       create_situation=(CreateAndAddToSituation.TunableFactory()),
       add_to_background_situation=(AddToBackgroundSituation.TunableFactory()),
       notify_zone_director=(NotfifyZoneDirector.TunableFactory()),
       default='disabled')),
       tuning_group=GroupNames.TRIGGERS), 
     'store_travel_group_placed_objects':Tunable(description='\n            If checked, any placed objects while in a travel group will be returned to household inventory once\n            travel group is disbanded.\n            ',
       tunable_type=bool,
       default=False), 
     'player_requires_visitation_rights':OptionalTunable(description='\n            If enabled, then lots of this venue type will require player Sims that\n            are not on their home lot to go through the process of being greeted\n            before they are given full rights to using the lot.\n            ',
       tunable=TunableTuple(ungreeted=Situation.TunableReference(description='\n                    The situation to create for ungreeted player sims on this lot.\n                    ',
       display_name='Player Ungreeted Situation'),
       greeted=Situation.TunableReference(description='\n                    The situation to create for greeted player sims on this lot.\n                    ',
       display_name='Player Greeted Situation'))), 
     'zone_fixup':TunableVariant(description='\n            Specify what to do with a non resident NPC\n            when the zone has to be fixed up on load. \n            This fix up will occur if sim time or the\n            active household has changed since the zone was last saved.\n            ',
       residential=ResidentialZoneFixupForNPC.TunableFactory(),
       create_situation=CreateAndAddToSituation.TunableFactory(),
       add_to_background_situation=AddToBackgroundSituation.TunableFactory(),
       default='residential',
       tuning_group=GroupNames.SPECIAL_CASES), 
     'travel_group_limit':OptionalTunable(description='\n            Maximum number of travel groups allowed in this venue.\n            ',
       disabled_name='no_limit',
       enabled_by_default=True,
       tunable=TunableRange(description='\n                The maximum number of travel groups allowed in this venue.\n                ',
       tunable_type=int,
       default=1,
       minimum=1),
       tuning_group=GroupNames.SPECIAL_CASES), 
     'travel_interaction_name':TunableVariant(description='\n            Specify what name a travel interaction gets when this Venue is an\n            adjacent lot.\n            ',
       visit_residential=ResidentialTravelDisplayName.TunableFactory(description='\n                The interaction name for when the destination lot is a\n                residence.\n                '),
       visit_venue=CommercialTravelDisplayName.TunableFactory(description='\n                The interaction name for when the destination lot is a\n                commercial venue.\n                Example: "Visit The Bar"\n                '),
       tuning_group=GroupNames.SPECIAL_CASES), 
     'travel_with_interaction_name':TunableVariant(description='\n            Specify what name a travel interaction gets when this Venue is an\n            adjacent lot.\n            ',
       visit_residential=ResidentialTravelDisplayName.TunableFactory(description='\n                The interaction name for when the destination lot is a\n                residence and the actor Sim is traveling with someone.\n                '),
       visit_venue=CommercialTravelDisplayName.TunableFactory(description='\n                The interaction name for when the destination lot is a\n                commercial venue and the actor is traveling with someone.\n                Example: "Visit The Bar With..."\n                '),
       tuning_group=GroupNames.SPECIAL_CASES), 
     'venue_requires_front_door':TunableEnumEntry(description='\n            Set to NEVER if this venue should never run the front door\n            generation code. Set to ALWAYS if this venue should always \n            run the front door generation code (like Residential lots).\n            Set to OWNED_OR_RENTED if it should only run if the lot is\n            owned by a household or rented by one. \n            If it runs, venue will have the ring doorbell interaction and \n            additional behavior like backup logic for broom teleports.\n            ',
       tunable_type=VenueFrontdoorRequirement,
       default=VenueFrontdoorRequirement.NEVER), 
     'automatic_objects':TunableList(description='\n            A list of objects that is required to exist on this venue (e.g. the\n            mailbox). If any of these objects are missing from this venue, they\n            will be auto-placed on zone load.',
       tunable=TunableTuple(description="\n                An item that is required to be present on this venue. The object's tag \n                will be used to determine if any similar objects are present. If no \n                similar objects are present, then the object's actual definition is used to \n                create an object of this type.\n                \n                This is not the same as required objects tuning. Please read comments \n                for both the fields.\n                \n                E.g. To require a mailbox to be present on a lot, tune a hypothetical basicMailbox \n                here. The code will not trigger as long as a basicMailbox, fancyMailbox, or \n                cheapMailbox are present on the lot. If none of them are, then a basicMailbox \n                will be automatically created.\n                ",
       default_value=TunableReference(description='\n                    The default object to use if no suitably tagged object is\n                    present on the lot.\n                    ',
       manager=(services.definition_manager())),
       tag=TunableEnumEntry(description='\n                    The tag to search for\n                    ',
       tunable_type=(tag.Tag),
       default=(tag.Tag.INVALID)))), 
     'hide_from_buildbuy_ui':Tunable(description='\n            If True, this venue type will not be available in the venue picker in\n            build/buy.\n            ',
       tunable_type=bool,
       default=False,
       export_modes=ExportModes.All), 
     'exclude_owned_objects_in_lot_value_calculation':Tunable(description='\n            Whether or not owned objects should be excluded when computing the lot\n            value for this venue type. \n            Example: Residential should include the value but Rentable should not.\n            ',
       tunable_type=bool,
       default=False,
       export_modes=ExportModes.All), 
     'gallery_upload_venue_type':TunableReference(description="\n            The venue type that this venue gets uploaded as to the gallery. In\n            each region's tuning, make sure the upload type is downloaded as\n            the appropriate venue type. \n            Example: Rentable venues should be uploaded as Residential.\n            ",
       manager=services.get_instance_manager(sims4.resources.Types.VENUE),
       allow_none=True,
       export_modes=ExportModes.All), 
     'allows_fire':Tunable(description='\n            If True a fire can happen on this venue, \n            otherwise fires will not spawn on this venue.\n            ',
       tunable_type=bool,
       default=False), 
     'allow_rolestate_routing_on_navmesh':Tunable(description='\n            Allow all RoleStates routing permission on lot navmeshes of this\n            venue type. This is particularly useful for outdoor venue types\n            (lots with no walls), where it is awkward to have to "invite a sim\n            in" before they may route on the lot, be called over, etc.\n            \n            This tunable overrides the "Allow Npc Routing On Active Lot"\n            tunable of individual RoleStates.\n            ',
       tunable_type=bool,
       default=False), 
     'category_tags':TunableList(description='\n            A list of tags to associate with this venue type.\n            ',
       tunable=TunableEnumEntry(description='\n                A category tag for this venue.\n                ',
       tunable_type=(tag.Tag),
       default=(tag.Tag.INVALID)),
       export_modes=ExportModes.All), 
     'zone_director':zone_director.ZoneDirectorBase.TunableReference(description='\n            The ZoneDirector type to request for this Venue Type. This will be the\n            default type for this Venue Type. It may be overridden by a system such\n            as Active Careers (e.g. your house is a crime scene now).\n            '), 
     'zone_modifiers':TunableSet(description='\n            A set of default zone modifiers to apply in this Venue Type. These zone \n            modifiers will be "hidden" from the UI and will not appear as lot traits \n            in the lot trait molecule or manage worlds.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ZONE_MODIFIER)),
       pack_safe=True)), 
     'new_venue_type_dialog_description':TunableLocalizedString(description="\n            When the venue type is 'new' to the player, the Venue Celebration\n            dialog is shown.  This is the localized string ID for the description\n            text.\n            ",
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'new_venue_type_dialog_image':TunableResourceKey(description="\n            When the venue type is 'new' to the player, the Venue Celebration\n            dialog is shown.  This is the main image ID shown in the dialog.\n            ",
       resource_types=sims4.resources.CompoundTypes.IMAGE,
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'new_venue_type_dialog_example_item':TunableResourceKey(description="\n            When the venue type is 'new' to the player, the Venue Celebration\n            dialog is shown.  This is the example lot ID to apply should the\n            user respond positively to the dialog.\n            ",
       resource_types=(
      sims4.resources.Types.TRAY_METADATA,),
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'new_venue_type_buttons':TunableList(description='\n            A list of button data to be used to create buttons on the New Venue Dialog. If nothing is tuned here then\n            we will default to the original format of the dialog which contains just the single button.\n            ',
       tunable=TunableTuple(description='\n                Tuning data for buttons to show when this dialog pops up. Consists of the text to show as the button\n                text as well as the UiMessage to send (along with parameters) when the button is clicked.\n                ',
       button_string=TunableLocalizedStringFactory(description='\n                    The string to be displayed as button text.\n                    ',
       export_modes=(ExportModes.All)),
       ui_message=TunableUiMessage(description='\n                    The UI message to send when the button is clicked along with any parameters needed.\n                    ',
       export_modes=(ExportModes.All)),
       export_modes=(ExportModes.All),
       export_class_name='NewVenueTypeButtons'),
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'new_venue_type_headline_text':TunableLocalizedString(description="\n            When the venue type is 'new' to the player, the Venue Celebration\n            dialog is shown.  This is the localized string ID for the headline text. \n            If nothing is tuned it will show the default string as specified in ui\n            code. \n            \n            {0.String} will get you the name of the venue for the string.\n            ",
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'new_venue_type_button_headline_text':TunableLocalizedString(description="\n            When the venue type is 'new' to the player, the Venue Celebration\n            dialog is shown.  This is the localized string ID for the text that appears\n            just above the messages, but below the image.\n             \n            If nothing is tuned it will show the default string as specified in ui\n            code. Unless there are buttons tuned, then it will be hidden.\n            ",
       allow_none=True,
       export_modes=ExportModes.All,
       tuning_group=NEW_VENUE_TUNING_GROUP), 
     'allow_super_speed_three':Tunable(description='\n            If set to True, game is allowed to get into super speed 3.\n            ',
       tunable_type=bool,
       default=True), 
     'allowed_for_clubs':Tunable(description='\n            If checked, this Venue can be associated with Clubs and will be\n            available for Club Gatherings.\n            ',
       tunable_type=bool,
       default=False,
       tuning_group=GroupNames.CLUBS,
       export_modes=ExportModes.All), 
     'club_gathering_text':OptionalTunable(description="\n            Specify text included in an NPC's invite to join a gathering at this\n            venue. This must be enabled if allowed_for_clubs is checked. If\n            allowed_for_clubs is unchecked, setting this field has no effect.\n            ",
       tunable=TunableLocalizedStringVariant(),
       tuning_group=GroupNames.CLUBS), 
     'club_gathering_auto_spawn_schedule':OptionalTunable(description='\n            If enabled, this schedule will specify the times when we will attempt to\n            spawn associated Club Gatherings on this venue.\n            ',
       tunable=WeeklySchedule.TunableFactory(description='\n                This schedule will specify the times when we will attempt to spawn\n                associated Club Gatherings on this venue.\n                ',
       schedule_entry_data={'tuning_name':'club_gathering_data', 
      'tuning_type':TunableTuple(description='\n                        Specify gathering behavior at these days and time.\n                        ',
        maximum_club_gatherings=TunableRange(description='\n                            Define the maximum number of gatherings that can be auto-\n                            started.\n                            ',
        tunable_type=int,
        minimum=0,
        default=3),
        ideal_club_gatherings=TunableCurve(description='\n                            Define the ideal number of gatherings that should be\n                            auto-started.\n                            ',
        x_axis_name='clubs_using_this_as_preferred_venue',
        y_axis_name='ideal_number_of_club_gatherings'))}),
       tuning_group=GroupNames.CLUBS), 
     'whim_set':OptionalTunable(description='\n            If enabled then this venue type will offer a whim set to the Sim\n            when it is the active lot.\n            ',
       tunable=TunableReference(description='\n                A whim set that is active when this venue is the active lot.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.ASPIRATION)),
       class_restrictions=('ObjectivelessWhimSet', ))), 
     'drama_node_events':TunableList(description='\n            A list of drama nodes that provide special events to the venues\n            that they are a part of.\n            ',
       tunable=TunableReference(description='\n                A drama node that will contain a special even on a venue.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.DRAMA_NODE)),
       class_restrictions=('VenueEventDramaNode', ),
       pack_safe=True)), 
     'drama_node_events_to_schedule':TunableRange(description='\n            The number of drama node events that will be scheduled if events\n            are specified.\n            ',
       tunable_type=int,
       default=1,
       minimum=1), 
     'supports_welcome_wagon':Tunable(description='\n            Whether or not welcome wagons will appear on this venue type.\n            ',
       tunable_type=bool,
       default=True), 
     'included_venues_for_club_gathering':TunableList(description='\n            Venue types that will also be considered valid for club gatherings\n            for a club with this venue type as its club hangout.\n            ',
       tunable=TunableReference(description='\n                Venue type to be included for club gatherings.\n                ',
       manager=(services.get_instance_manager(sims4.resources.Types.VENUE)),
       pack_safe=True),
       tuning_group=GroupNames.CLUBS), 
     'variable_venues':OptionalTunable(description='\n            Enable for variable venues, where the venue can change automatically.  \n            Either this venue or one of the provided sub-venues can be\n            the active venue type.  Most venues do not enable this feature.\n            ',
       tunable=TunableTuple(description='\n                Variable venue tuning.\n                ',
       civic_policy=VenueCivicPolicyProvider.TunableFactory(description='\n                    Tuning to control the civic policy voting and enactment process for\n                    a venue.\n                    ',
       export_modes=(ExportModes.All)),
       variable_venue_display_name=TunableLocalizedStringFactory(description='\n                    Alternative name used when the parent venue is the active venue.\n                    Replaces Display Name.\n                    ',
       export_modes=(ExportModes.All)),
       variable_venue_description=TunableLocalizedStringFactory(description='\n                    Alternative description used when the parent venue is the active venue.\n                    Replaces Venue Description.\n                    ',
       export_modes=(ExportModes.All)),
       enable_civic_policy_support=Tunable(description='\n                    Whether or not Civic policies will control which venue is active.\n                    ',
       tunable_type=bool,
       default=True),
       export_class_name='VariableVenueTuning'),
       export_modes=ExportModes.All), 
     'display_venue_features':TunableList(description="\n            Features to be displayed on this venue's build buy configuration panel.\n            Currently this has no gameplay effect, only for UI purpose.\n            ",
       tunable=TunableTuple(venue_feature_name=TunableLocalizedStringFactory(description='\n                    Name of the venue feature.\n                    ',
       export_modes=(ExportModes.All)),
       venue_feature_description=TunableLocalizedStringFactory(description='\n                    Description of the venue feature.\n                    ',
       export_modes=(ExportModes.All)),
       venue_feature_icon=TunableIcon(description='\n                    Icon of the venue feature.\n                    ',
       export_modes=(ExportModes.All)),
       export_class_name='TunableDisplayVenueFeature'),
       export_modes=ExportModes.All)}

    @classmethod
    def _verify_tuning_callback(cls):
        if cls.special_event_schedule is not None:
            for entry in cls.special_event_schedule.schedule_entries:
                if entry.situation.venue_situation_player_job is None:
                    logger.error('Venue Situation Player Job {} tuned in Situation: {}', entry.situation.venue_situation_player_job, entry.situation)

        if cls.allowed_for_clubs:
            if not cls.club_gathering_text:
                logger.error('Venue {} is marked as allowed_for_clubs but has no club_gathering_text specified.', cls, owner='epanero')

    @classmethod
    def _tuning_loaded_callback(cls):
        cls.sub_venue_types = []
        if cls.variable_venues is None:
            return
        for policy in cls.variable_venues.civic_policy.civic_policies:
            if hasattr(policy, 'sub_venue') and policy.sub_venue is not None:
                cls.sub_venue_types.append(policy.sub_venue)

        if cls not in cls.sub_venue_types:
            cls.sub_venue_types.append(cls)

    def __init__--- This code section failed: ---

 L.1011         0  LOAD_CONST               None
                2  LOAD_FAST                'self'
                4  STORE_ATTR               _active_background_event_id

 L.1012         6  LOAD_CONST               None
                8  LOAD_FAST                'self'
               10  STORE_ATTR               _active_special_event_id

 L.1013        12  LOAD_CONST               None
               14  LOAD_FAST                'self'
               16  STORE_ATTR               _background_event_schedule

 L.1014        18  LOAD_CONST               None
               20  LOAD_FAST                'self'
               22  STORE_ATTR               _special_event_schedule

 L.1015        24  LOAD_CONST               None
               26  LOAD_FAST                'self'
               28  STORE_ATTR               _club_gathering_schedule

 L.1017        30  LOAD_GLOBAL              services
               32  LOAD_METHOD              venue_game_service
               34  CALL_METHOD_0         0  '0 positional arguments'
               36  STORE_FAST               'venue_game_service'

 L.1018        38  LOAD_FAST                'venue_game_service'
               40  LOAD_CONST               None
               42  COMPARE_OP               is
               44  POP_JUMP_IF_FALSE    56  'to 56'

 L.1019        46  LOAD_CONST               None
               48  LOAD_FAST                'self'
               50  STORE_ATTR               _civic_policy_provider

 L.1020        52  LOAD_CONST               None
               54  RETURN_VALUE     
             56_0  COME_FROM            44  '44'

 L.1021        56  LOAD_GLOBAL              services
               58  LOAD_METHOD              venue_service
               60  CALL_METHOD_0         0  '0 positional arguments'
               62  STORE_FAST               'venue_service'

 L.1022        64  LOAD_FAST                'venue_game_service'
               66  LOAD_METHOD              get_provider
               68  LOAD_GLOBAL              services
               70  LOAD_METHOD              current_zone_id
               72  CALL_METHOD_0         0  '0 positional arguments'
               74  CALL_METHOD_1         1  '1 positional argument'
               76  STORE_FAST               'existing_provider'

 L.1023        78  LOAD_GLOBAL              type
               80  LOAD_FAST                'self'
               82  CALL_FUNCTION_1       1  '1 positional argument'
               84  STORE_FAST               'venue_tuning'

 L.1025        86  LOAD_FAST                'source_venue_type'
               88  LOAD_CONST               None
               90  COMPARE_OP               is
               92  POP_JUMP_IF_FALSE   104  'to 104'

 L.1026        94  LOAD_FAST                'venue_service'
               96  LOAD_METHOD              get_variable_venue_source_venue
               98  LOAD_FAST                'venue_tuning'
              100  CALL_METHOD_1         1  '1 positional argument'
              102  STORE_FAST               'source_venue_type'
            104_0  COME_FROM            92  '92'

 L.1027       104  LOAD_FAST                'source_venue_type'
              106  LOAD_CONST               None
              108  COMPARE_OP               is
              110  POP_JUMP_IF_TRUE    130  'to 130'

 L.1028       112  LOAD_FAST                'source_venue_type'
              114  LOAD_ATTR                variable_venues
              116  LOAD_CONST               None
              118  COMPARE_OP               is
              120  POP_JUMP_IF_TRUE    130  'to 130'

 L.1029       122  LOAD_FAST                'source_venue_type'
              124  LOAD_ATTR                variable_venues
              126  LOAD_ATTR                enable_civic_policy_support
              128  POP_JUMP_IF_TRUE    162  'to 162'
            130_0  COME_FROM           120  '120'
            130_1  COME_FROM           110  '110'

 L.1031       130  LOAD_CONST               None
              132  LOAD_FAST                'self'
              134  STORE_ATTR               _civic_policy_provider

 L.1032       136  LOAD_FAST                'existing_provider'
              138  LOAD_CONST               None
              140  COMPARE_OP               is-not
              142  POP_JUMP_IF_FALSE   244  'to 244'

 L.1033       144  LOAD_FAST                'venue_game_service'
              146  LOAD_METHOD              set_provider
              148  LOAD_GLOBAL              services
              150  LOAD_METHOD              current_zone_id
              152  CALL_METHOD_0         0  '0 positional arguments'
              154  LOAD_CONST               None
              156  CALL_METHOD_2         2  '2 positional arguments'
              158  POP_TOP          
              160  JUMP_FORWARD        244  'to 244'
            162_0  COME_FROM           128  '128'

 L.1035       162  LOAD_FAST                'existing_provider'
              164  LOAD_CONST               None
              166  COMPARE_OP               is-not
              168  POP_JUMP_IF_FALSE   196  'to 196'
              170  LOAD_FAST                'existing_provider'
              172  LOAD_ATTR                source_venue_type
              174  LOAD_FAST                'source_venue_type'
              176  COMPARE_OP               is
              178  POP_JUMP_IF_FALSE   196  'to 196'

 L.1037       180  LOAD_FAST                'existing_provider'
              182  LOAD_FAST                'self'
              184  STORE_ATTR               _civic_policy_provider

 L.1039       186  LOAD_FAST                'self'
              188  LOAD_FAST                'self'
              190  LOAD_ATTR                _civic_policy_provider
              192  STORE_ATTR               active_venue_type
              194  JUMP_FORWARD        244  'to 244'
            196_0  COME_FROM           178  '178'
            196_1  COME_FROM           168  '168'

 L.1042       196  LOAD_FAST                'source_venue_type'
              198  LOAD_ATTR                variable_venues
              200  LOAD_METHOD              civic_policy
              202  LOAD_FAST                'source_venue_type'
              204  LOAD_FAST                'self'
              206  CALL_METHOD_2         2  '2 positional arguments'
              208  LOAD_FAST                'self'
              210  STORE_ATTR               _civic_policy_provider

 L.1043       212  LOAD_FAST                'self'
              214  LOAD_ATTR                _civic_policy_provider
              216  LOAD_ATTR                civic_policies
              218  POP_JUMP_IF_TRUE    226  'to 226'

 L.1045       220  LOAD_CONST               None
              222  LOAD_FAST                'self'
              224  STORE_ATTR               _civic_policy_provider
            226_0  COME_FROM           218  '218'

 L.1046       226  LOAD_FAST                'venue_game_service'
              228  LOAD_METHOD              set_provider
              230  LOAD_GLOBAL              services
              232  LOAD_METHOD              current_zone_id
              234  CALL_METHOD_0         0  '0 positional arguments'
              236  LOAD_FAST                'self'
              238  LOAD_ATTR                _civic_policy_provider
              240  CALL_METHOD_2         2  '2 positional arguments'
              242  POP_TOP          
            244_0  COME_FROM           194  '194'
            244_1  COME_FROM           160  '160'
            244_2  COME_FROM           142  '142'

Parse error at or near `COME_FROM' instruction at offset 244_1

    def create_zone_director_instance(self):
        return self.zone_director()

    @classmethod
    def valid_active_venue_type(cls, venue_type):
        return venue_type is cls or venue_type in cls.sub_venue_types

    @property
    def civic_policy_provider(self):
        return self._civic_policy_provider

    def set_active_event_ids(self, background_event_id=None, special_event_id=None):
        self._active_background_event_id = background_event_id
        self._active_special_event_id = special_event_id

    @property
    def active_background_event_id(self):
        return self._active_background_event_id

    @property
    def active_special_event_id(self):
        return self._active_special_event_id

    def _start_schedule(self, schedule, schedule_callback, *, schedule_immediate):
        if schedule is None:
            return
        schedule_instance = schedule(start_callback=schedule_callback, schedule_immediate=False)
        if schedule_immediate:
            best_time_span, best_data_list = schedule_instance.time_until_next_scheduled_event((services.time_service().sim_now), schedule_immediate=True)
            if best_time_span is not None:
                if best_time_span == date_and_time.TimeSpan.ZERO:
                    for best_data in best_data_list:
                        schedule_callback(schedule_instance, best_data)

        return schedule_instance

    def schedule_background_events(self, schedule_immediate=True):
        self._background_event_schedule = self._start_schedule((self.background_event_schedule), (self._start_background_event),
          schedule_immediate=schedule_immediate)

    def schedule_special_events(self, schedule_immediate=True):
        self._special_event_schedule = self.special_event_schedule(start_callback=(self._try_start_special_event), schedule_immediate=schedule_immediate)

    def schedule_club_gatherings(self, schedule_immediate=False):
        self._club_gathering_schedule = self._start_schedule((self.club_gathering_auto_spawn_schedule), (self._try_balance_club_gatherings),
          schedule_immediate=schedule_immediate)

    def _start_background_event(self, scheduler, alarm_data, extra_data=None):
        entry = alarm_data.entry
        situation = entry.situation
        situation_manager = services.get_zone_situation_manager()
        if self._active_background_event_id is not None:
            if self._active_background_event_id in situation_manager:
                situation_manager.destroy_situation_by_id(self._active_background_event_id)
        situation_id = services.get_zone_situation_manager().create_situation(situation, user_facing=False, spawn_sims_during_zone_spin_up=True)
        self._active_background_event_id = situation_id

    def _try_start_special_event(self, scheduler, alarm_data, extra_data):
        entry = alarm_data.entry
        situation = entry.situation
        situation_manager = services.get_zone_situation_manager()
        if self._active_special_event_id is None:
            client_manager = services.client_manager()
            client = next(iter(client_manager.values()))
            invited_sim = client.active_sim
            active_sim_available = situation.is_situation_available(invited_sim)

            def _start_special_event(dialog):
                guest_list = None
                if dialog.accepted:
                    start_user_facing = True
                    guest_list = SituationGuestList()
                    guest_info = SituationGuestInfo.construct_from_purpose(invited_sim.id, situation.venue_situation_player_job, SituationInvitationPurpose.INVITED)
                    guest_list.add_guest_info(guest_info)
                else:
                    start_user_facing = False
                situation_id = situation_manager.create_situation(situation, guest_list=guest_list, user_facing=start_user_facing)
                self._active_special_event_id = situation_id

            if situation.venue_invitation_message is not None and not situation_manager.is_user_facing_situation_running():
                if active_sim_available:
                    dialog = situation.venue_invitation_message(invited_sim, SingleSimResolver(invited_sim))
                    dialog.show_dialog(on_response=_start_special_event, additional_tokens=(situation.display_name, situation.venue_situation_player_job.display_name))
            else:
                situation_id = situation_manager.create_situation(situation, user_facing=False)
                self._active_special_event_id = situation_id

    def _try_balance_club_gatherings(self, scheduler, alarm_data, extra_data=None):
        club_service = services.get_club_service()
        if club_service is None:
            return
        else:
            club_gathering_data = alarm_data.entry.club_gathering_data

            def is_club_valid_for_venue(club):
                if club.hangout_setting == ClubHangoutSetting.HANGOUT_VENUE:
                    return club.hangout_venue is type(self)
                if club.hangout_setting == ClubHangoutSetting.HANGOUT_LOT:
                    return club.hangout_zone_id == services.current_zone_id()
                return False

            clubs = tuple((club for club in club_service.clubs if is_club_valid_for_venue(club)))
            return clubs or None
        ideal_club_gatherings = club_gathering_data.ideal_club_gatherings.get(len(clubs))
        ideal_club_gatherings = int(random.triangular(0, club_gathering_data.maximum_club_gatherings, ideal_club_gatherings))
        lot_household = services.active_lot().get_household()
        for club in clubs:
            if len(club_service.clubs_to_gatherings_map) >= ideal_club_gatherings:
                break
            else:
                if club in club_service.clubs_to_gatherings_map:
                    continue
                if not club.is_gathering_auto_spawning_available():
                    continue
                if lot_household is not None and not any((member.household is lot_household for member in club.members)):
                    continue
            if not club.is_gathering_auto_start_available():
                continue
            club_service.start_gathering(club)

    def shut_down(self):
        if self._background_event_schedule is not None:
            self._background_event_schedule.destroy()
        if self._special_event_schedule is not None:
            self._special_event_schedule.destroy()
        situation_manager = services.get_zone_situation_manager()
        if self._active_background_event_id is not None:
            situation_manager.destroy_situation_by_id(self._active_background_event_id)
            self._active_background_event_id = None
        if self._active_special_event_id is not None:
            situation_manager.destroy_situation_by_id(self._active_special_event_id)
            self._active_special_event_id = None

    @classmethod
    def lot_has_required_venue_objects--- This code section failed: ---

 L.1279         0  BUILD_LIST_0          0 
                2  STORE_FAST               'failure_reasons'

 L.1280         4  SETUP_LOOP           50  'to 50'
                6  LOAD_FAST                'cls'
                8  LOAD_ATTR                required_objects
               10  GET_ITER         
             12_0  COME_FROM            44  '44'
               12  FOR_ITER             48  'to 48'
               14  STORE_FAST               'required_object_tuning'

 L.1281        16  LOAD_FAST                'required_object_tuning'
               18  LOAD_ATTR                object
               20  STORE_FAST               'object_test'

 L.1282        22  LOAD_FAST                'object_test'
               24  CALL_FUNCTION_0       0  '0 positional arguments'
               26  STORE_FAST               'object_list'

 L.1283        28  LOAD_GLOBAL              len
               30  LOAD_FAST                'object_list'
               32  CALL_FUNCTION_1       1  '1 positional argument'
               34  STORE_FAST               'num_objects'

 L.1284        36  LOAD_FAST                'num_objects'
               38  LOAD_FAST                'required_object_tuning'
               40  LOAD_ATTR                number
               42  COMPARE_OP               <
               44  POP_JUMP_IF_FALSE    12  'to 12'

 L.1287        46  JUMP_BACK            12  'to 12'
               48  POP_BLOCK        
             50_0  COME_FROM_LOOP        4  '4'

 L.1298        50  LOAD_CONST               None
               52  STORE_FAST               'failure_message'

 L.1299        54  LOAD_GLOBAL              len
               56  LOAD_FAST                'failure_reasons'
               58  CALL_FUNCTION_1       1  '1 positional argument'
               60  LOAD_CONST               0
               62  COMPARE_OP               >
               64  STORE_FAST               'failure'

 L.1300        66  LOAD_FAST                'failure'
               68  POP_JUMP_IF_FALSE   100  'to 100'

 L.1301        70  LOAD_STR                 ''
               72  STORE_FAST               'failure_message'

 L.1302        74  SETUP_LOOP          100  'to 100'
               76  LOAD_FAST                'failure_reasons'
               78  GET_ITER         
               80  FOR_ITER             98  'to 98'
               82  STORE_FAST               'message'

 L.1303        84  LOAD_FAST                'failure_message'
               86  LOAD_FAST                'message'
               88  LOAD_STR                 '\n'
               90  BINARY_ADD       
               92  INPLACE_ADD      
               94  STORE_FAST               'failure_message'
               96  JUMP_BACK            80  'to 80'
               98  POP_BLOCK        
            100_0  COME_FROM_LOOP       74  '74'
            100_1  COME_FROM            68  '68'

 L.1305       100  LOAD_FAST                'failure'
              102  UNARY_NOT        
              104  LOAD_FAST                'failure_message'
              106  BUILD_TUPLE_2         2 
              108  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `POP_BLOCK' instruction at offset 48

    def summon_npcs(self, npc_infos, purpose, host_sim_info=None):
        summoned = False
        open_street_director = services.venue_service().get_zone_director().open_street_director
        if open_street_director is not None:
            summoned = open_street_director.summon_npcs(npc_infos, purpose, host_sim_info=host_sim_info)
        if summoned or self.npc_summoning_behavior is None:
            return
        summon_behaviors = self.npc_summoning_behavior.get(purpose)
        if summon_behaviors is None:
            summon_behaviors = self.npc_summoning_behavior.get(venues.venue_constants.NPCSummoningPurpose.DEFAULT)
            if summon_behaviors is None:
                return
        species_sim_info_map = defaultdict(list)
        for sim_info in npc_infos:
            species_sim_info_map[sim_info.species].append(sim_info)

        for species, sim_infos in species_sim_info_map.items():
            summon_behavior = summon_behaviors.get(species)
            if summon_behavior is None:
                summon_behavior = summon_behaviors.get(Species.HUMAN)
                if summon_behavior is None:
                    continue
            summon_behavior(sim_infos, host_sim_info=host_sim_info)

    @classproperty
    def is_residential(cls):
        return cls.venue_type == VenueTypes.RESIDENTIAL

    @classproperty
    def is_rental(cls):
        return cls.venue_type == VenueTypes.RENTAL

    @classproperty
    def is_university_housing(cls):
        return cls.venue_type == VenueTypes.UNIVERSITY_HOUSING

    @classproperty
    def requires_front_door(cls):
        return cls.venue_requires_front_door != VenueFrontdoorRequirement.NEVER

    @classproperty
    def requires_visitation_rights(cls):
        return cls.player_requires_visitation_rights is not None

    @classproperty
    def player_ungreeted_situation_type(cls):
        if cls.player_requires_visitation_rights is None:
            return
        return cls.player_requires_visitation_rights.ungreeted

    @classproperty
    def player_greeted_situation_type(cls):
        if cls.player_requires_visitation_rights is None:
            return
        return cls.player_requires_visitation_rights.greeted

    @classproperty
    def is_vacation_venue(cls):
        return cls.venue_flags & VenueFlags.VACATION_TARGET
