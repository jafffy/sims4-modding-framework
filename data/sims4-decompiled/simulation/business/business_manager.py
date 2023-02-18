# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\business\business_manager.py
# Compiled at: 2018-12-04 01:43:42
# Size of source mod 2**32: 75883 bytes

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
_ifstmts_jumpl ::= COME_FROM c_stmts JUMP_BACK . 
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
and ::= expr JUMP_IF_FALSE_OR_POP . expr \e_come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP . expr come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr . come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr \e_come_from_opt . 
and ::= expr JUMP_IF_FALSE_OR_POP expr come_from_opt . 
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
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op ROT_THREE . STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op ROT_THREE STORE_SUBSCR . 
aug_assign1 ::= expr expr inplace_op store . 
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_SUBTRACT . 
binary_operator ::= BINARY_TRUE_DIVIDE . 
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
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr CALL_METHOD_3 . 
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
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
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
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= or . 
expr ::= subscript . 
expr ::= subscript2 . 
expr ::= tuple . 
expr ::= unary_not . 
expr ::= unary_op . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
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
inplace_op ::= INPLACE_ADD . 
inplace_op ::= INPLACE_MULTIPLY . 
inplace_op ::= INPLACE_TRUE_DIVIDE . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jifop_come_from ::= JUMP_IF_FALSE_OR_POP . come_froms
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
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
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
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP . return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond . COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM . 
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr ::= ret_and . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
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
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign1 . 
stmt ::= aug_assign2 . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= withasstmt . 
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
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr DUP_TOP_TWO . BINARY_SUBSCR
subscript2 ::= expr expr DUP_TOP_TWO BINARY_SUBSCR . 
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
unary_not ::= expr . UNARY_NOT
unary_not ::= expr UNARY_NOT . 
unary_op ::= expr . unary_operator
unary_op ::= expr unary_operator . 
unary_operator ::= UNARY_NEGATIVE . 
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
   
 L.1216        24  LOAD_GLOBAL              services
                  26  LOAD_METHOD              game_clock_service
                  28  CALL_METHOD_0         0  '0 positional arguments'
                  30  LOAD_METHOD              now
                  32  CALL_METHOD_0         0  '0 positional arguments'
                  34  LOAD_FAST                'self'
                  36  LOAD_ATTR                _open_time
                  38  BINARY_SUBTRACT  
->                40  RETURN_VALUE     
from _collections import defaultdict
from collections import Counter
import operator
from protocolbuffers import UI_pb2, Consts_pb2, Business_pb2, ResourceKey_pb2, DistributorOps_pb2
from audio.primitive import PlaySound
from business.business_customer_manager import BusinessCustomerManager
from business.business_employee_manager import BusinessEmployeeManager
from business.business_enums import BusinessQualityType
from business.business_funds import BusinessFunds
from date_and_time import DateAndTime
from distributor.ops import GenericProtocolBufferOp
from distributor.rollback import ProtocolBufferRollback
from distributor.system import Distributor
from event_testing.resolver import SingleSimResolver
from event_testing.test_events import TestEvent
from gsi_handlers import business_handlers
from objects import ALL_HIDDEN_REASONS
from retail.retail_balance_transfer_dialog import FundsTransferDialog
from sims4.callback_utils import CallableList
from singletons import DEFAULT
from world.premade_lot_status import PremadeLotStatus
from zone_types import ZoneState
import distributor, services, sims4.log, telemetry_helper
TELEMETRY_GROUP_BUSINESS = 'BUSI'
TELEMETRY_HOOK_BUSINESS_PURCHASED = 'BUSP'
TELEMETRY_HOOK_NEW_GAME_BUSINESS_PURCHASED = 'BUNG'
TELEMETRY_HOOK_BUSINESS_SOLD = 'BUSS'
TELEMETRY_HOOK_NPC_BUSINESS_VISITED = 'BUNS'
TELEMETRY_HOOK_BUSINESS_CLOSED = 'BUSC'
TELEMETRY_HOOK_LENGTH_BUSINESS_OPENED = 'lsto'
TELEMETRY_HOOK_NUM_WORKERS = 'numw'
TELEMETRY_HOOK_AMOUNT_PROFIT = 'prof'
TELEMETRY_HOOK_STAR_RATING = 'star'
TELEMETRY_HOOK_BUSINESS_TYPE = 'btyp'
business_telemetry_writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_BUSINESS)
logger = sims4.log.Logger('Business', default_owner='trevor')

class BusinessManager:
    EVENTS = (
     TestEvent.SimDeathTypeSet,)

    def __init__(self, business_type):
        self._business_type = business_type
        self._business_type_data = services.business_service().get_business_tuning_data_for_business_type(business_type)
        self._owner_household_id = None
        self._zone_id = None
        self._employee_manager = BusinessEmployeeManager(self)
        self._customer_manager = BusinessCustomerManager(self)
        self._is_open = False
        self._open_time = None
        self._last_off_lot_update = None
        self.on_store_closed = CallableList()
        self._funds_category_tracker = Counter()
        self._funds = None
        self._markup_multiplier = self.tuning_data.default_markup_multiplier
        self._daily_revenue = 0
        self._daily_items_sold = 0
        self._grand_opening = False
        self._star_rating_value = self._business_type_data.default_business_star_rating_value
        self._buff_bucket_totals = defaultdict(float)
        self._buff_bucket_size = 0
        self._summary_dialog_class = None
        self._quality_unlocked = False
        self._off_lot_negative_profit_notification_shown = False

    @property
    def business_type(self):
        return self._business_type

    @property
    def owner_household_id(self):
        return self._owner_household_id

    @property
    def is_owned_by_npc(self):
        return self._owner_household_id is None

    @property
    def business_zone_id(self):
        return self._zone_id

    @property
    def tuning_data(self):
        return self._business_type_data

    @property
    def is_open(self):
        return self._is_open

    @property
    def minutes_open(self):
        timespan = self.get_timespan_since_open()
        if timespan is None:
            return 0
        return timespan.in_minutes()

    @property
    def daily_revenue(self):
        return self._daily_revenue

    @property
    def funds(self):
        return self._funds

    @property
    def funds_transfer_gain_reason(self):
        return Consts_pb2.FUNDS_RETAIL_TRANSFER_GAIN

    @property
    def funds_transfer_loss_reason(self):
        return Consts_pb2.FUNDS_RETAIL_TRANSFER_LOSS

    @property
    def daily_items_sold(self):
        return self._daily_items_sold

    @daily_items_sold.setter
    def daily_items_sold(self, value):
        self._daily_items_sold = value
        self._send_daily_items_sold_update()

    @property
    def is_owner_household_active(self):
        if self._owner_household_id is None:
            return False
        return self._owner_household_id == services.active_household_id()

    @property
    def markup_multiplier(self):
        return self._markup_multiplier

    @property
    def employee_count(self):
        return self._employee_manager.employee_count

    @property
    def quality_setting(self):
        return BusinessQualityType.INVALID

    def set_owner_household_id(self, owner_household_id):
        self._owner_household_id = owner_household_id
        starting_funds = self.tuning_data.npc_starting_funds if self._owner_household_id is None else 0
        self._funds = BusinessFunds(self._owner_household_id, starting_funds, self)
        self._grand_opening = self._owner_household_id is not None

    def set_zone_id(self, business_zone_id):
        self._zone_id = business_zone_id

    def get_star_rating(self):
        star_rating = self._get_star_rating_from_curve()
        star_rating = round(star_rating * 2) / 2
        return sims4.math.clamp(self.tuning_data.min_and_max_star_rating.lower_bound, star_rating, self.tuning_data.min_and_max_star_rating.upper_bound)

    def is_household_owner(self, household_id):
        if self._owner_household_id is None:
            return False
        return self._owner_household_id == household_id

    def should_automatically_close(self):
        return False

    def _update_off_lot_time_and_get_delta(self):
        now = services.time_service().sim_now
        hours_since_last_sim = (now - self._last_off_lot_update).in_hours()
        self._last_off_lot_update = now
        return hours_since_last_sim

    def run_off_lot_simulation(self):
        if self.should_show_no_way_to_make_money_notification():
            return
            if self._last_off_lot_update is None:
                return
            if not self.tuning_data.off_lot_star_rating_increase_per_hour_curve:
                return
            hours_since_last_sim = self._update_off_lot_time_and_get_delta()
            star_rating = self.get_star_rating()
            value_change = 0
            if sims4.random.random_chance(self.tuning_data.off_lot_chance_of_star_rating_increase):
                value_change = self.tuning_data.off_lot_star_rating_increase_per_hour_curve.get(star_rating)
                if business_handlers.business_archiver.enabled:
                    business_handlers.archive_business_event('OffLot', None, 'business with star rating: {} using increase mapping with value change of: {}'.format(star_rating, value_change))
        else:
            value_change = self.tuning_data.off_lot_star_rating_decay_per_hour_curve.get(star_rating)
            perk_tuning = self.tuning_data.off_lot_star_rating_decay_multiplier_perk
            perk_unlocked = False
            if perk_tuning is not None:
                bucks_tracker = services.active_household().bucks_tracker
                if bucks_tracker.is_perk_unlocked(perk_tuning.perk):
                    value_change *= perk_tuning.decay_multiplier
                    perk_unlocked = True
            if business_handlers.business_archiver.enabled:
                if perk_unlocked:
                    event_description = 'business with star rating: {} using decay mapping with value change of: {} after multiplier applied :{}'.format(star_rating, value_change, perk_tuning.decay_multiplier)
                else:
                    event_description = 'business with star rating: {} using decay mapping with value change of: {}'.format(star_rating, value_change)
                business_handlers.archive_business_event('OffLot', None, event_description)
        value_change *= hours_since_last_sim
        self._adjust_star_rating_value(value_change, send_update_message=False)
        self._adjust_profit(hours_since_last_sim)
        self._send_review_update_message()
        self.send_daily_profit_and_cost_update()

    def prepare_for_off_lot_simulation(self):
        self._off_lot_negative_profit_notification_shown = False

    def _adjust_profit(self, hours_since_last_sim):
        final_customer_count = self._get_off_lot_customer_count(hours_since_last_sim)
        self._customer_manager._session_customers_served += final_customer_count
        self._customer_manager._lifetime_customers_served += final_customer_count
        self._customer_manager._send_daily_customers_served_update()
        profit_per_service = self._get_average_profit_per_service()
        profit_per_service *= self.tuning_data.off_lot_profit_per_item_multiplier
        total_profit = profit_per_service * final_customer_count
        self.modify_funds(total_profit, from_item_sold=True)
        if self.tuning_data.off_lot_net_loss_notification is None:
            return
        employee_wages = self._employee_manager.get_total_employee_wages_per_hour() * hours_since_last_sim
        advertising_cost = self._advertising_manager.get_advertising_cost_per_hour() * hours_since_last_sim
        net_profit = total_profit - employee_wages - advertising_cost
        if net_profit < 0:
            if not self._off_lot_negative_profit_notification_shown:
                zone_data = services.get_persistence_service().get_zone_proto_buff(self._zone_id)
                active_sim_info = services.active_sim_info()
                if zone_data is not None:
                    if active_sim_info is not None:
                        notification = self.tuning_data.off_lot_net_loss_notification(active_sim_info, resolver=(SingleSimResolver(active_sim_info)))
                        notification.show_dialog(additional_tokens=(zone_data.name,))
                        self._off_lot_negative_profit_notification_shown = True

    def set_open(self, is_open):
        if self._is_open == is_open:
            return
        elif is_open:
            self._open_business()
        else:
            self._close_business()

    def start_already_opened_business(self):
        self._employee_manager.open_business()
        self.tuning_data.lighting_helper_open.execute_lighting_helper(self)

    def should_close_after_load(self):
        current_zone = services.current_zone()
        if current_zone.active_household_changed_between_save_and_load():
            if services.active_household_id() == self._owner_household_id:
                return True
        if current_zone.id == self._zone_id:
            return self.should_automatically_close() and current_zone.time_has_passed_in_world_since_zone_save()
        return self.should_automatically_close()

    def is_employee(self, sim_info):
        return self._employee_manager.is_employee(sim_info)

    def is_valid_employee_type(self, employee_type):
        return employee_type in self.tuning_data.employee_data_map

    def is_valid_employee_skill(self, employee_skill, employee_type):
        employee_type_data = self.tuning_data.employee_data_map.get(employee_type, None)
        if employee_type_data is None:
            return False
        return employee_skill in employee_type_data.employee_skills

    def get_employee_count(self, employee_type):
        return self._employee_manager.get_number_of_employees_by_type(employee_type)

    def get_employees_by_type(self, employee_type):
        return self._employee_manager.get_employees_by_type(employee_type)

    def get_employee_data(self, sim_info):
        return self._employee_manager.get_employee_data(sim_info)

    def remove_employee(self, sim_info):
        self._employee_manager.remove_employee(sim_info)
        self.send_min_employee_req_met_update_message()
        if self.should_show_no_way_to_make_money_notification():
            active_sim_info = services.active_sim_info()
            notification = self.tuning_data.no_way_to_make_money_notification(active_sim_info, resolver=(SingleSimResolver(active_sim_info)))
            notification.show_dialog()

    def get_total_employee_wages_per_hour(self):
        return self._employee_manager.get_total_employee_wages_per_hour()

    def get_desired_career_level(self, sim_info, employee_type):
        return self._employee_manager.get_desired_career_level(sim_info, employee_type)

    def get_customer_star_rating(self, sim_id):
        return self._customer_manager.get_customer_star_rating(sim_id)

    def _should_make_customer(self, sim_info):
        return self.is_owner_household_active and not self.is_household_owner(sim_info.household_id)

    def add_customer(self, sim_info):
        if self._should_make_customer(sim_info):
            self._customer_manager.add_customer(sim_info.sim_id)

    def remove_customer(self, sim_info, review_business=True):
        if not self._should_make_customer(sim_info):
            return
        self._customer_manager.remove_customer(sim_info, review_business)

    def set_daily_revenue(self, value):
        self._daily_revenue = value
        if self._owner_household_id is not None:
            self.send_daily_profit_and_cost_update()

    def set_markup_multiplier(self, multiplier):
        valid_multipliers = [entry.markup_multiplier for entry in self._business_type_data.markup_multiplier_data]
        if multiplier in valid_multipliers:
            self._markup_multiplier = multiplier
            self.send_markup_multiplier_message()
        else:
            logger.error('Tried setting the markup multiplier to an invalid multiplier. Invalid multiplier is: {}. Valid multipliers are: {}.', multiplier, valid_multipliers)
        self._distribute_markup_multiplier_update()

    def _distribute_markup_multiplier_update(self):
        markup_msg = Business_pb2.BusinessMarkupUpdate()
        markup_msg.zone_id = self.business_zone_id
        markup_msg.markup_chosen = self.markup_multiplier
        op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_MARKUP_DATA_UPDATE, markup_msg)
        Distributor.instance().add_op_with_no_owner(op)

    def get_value_with_markup(self, value) -> int:
        markup_multiplier = self.markup_multiplier
        if self.owner_household_id is not None:
            tracker = services.business_service().get_business_tracker_for_household(self.owner_household_id, self.business_type)
            markup_multiplier += tracker.additional_markup_multiplier
        else:
            active_household = services.active_household()
            if active_household is not None:
                markup_multiplier *= active_household.holiday_tracker.get_active_holiday_business_price_multiplier(self.business_type)
        return int(value * markup_multiplier)

    def add_to_funds_category(self, funds_category, amount):
        if not self.is_open:
            return
        self._funds_category_tracker[funds_category] += amount
        self.send_daily_profit_and_cost_update()

    def get_funds_category_entries_gen(self):
        for funds_category, amount in self._funds_category_tracker.items():
            funds_category_data = self.tuning_data.funds_category_data.get(funds_category)
            if funds_category_data is not None and funds_category_data.summary_dialog_entry is not None:
                yield (
                 funds_category_data.summary_dialog_entry, amount)

    def potential_manage_outfit_interactions_gen(self, context, **kwargs):
        for affordance in self.tuning_data.manage_outfit_affordances:
            for aop in (affordance.potential_interactions)((context.sim), context, **kwargs):
                yield aop

    def modify_funds(self, amount, from_item_sold=True, from_comped_item=False, funds_category=None):
        if amount == 0:
            return
        if amount < 0:
            if from_item_sold:
                logger.warn("Trying to deduct funds from a business but claiming it's from an item sold. Makes no sense so we're bailing.")
                return
            self._funds.try_remove((-amount), (Consts_pb2.FUNDS_RETAIL_PROFITS), funds_category=funds_category)
        else:
            if from_comped_item:
                logger.warn("Trying to add funds to a business but claiming it's from a comped meal. Comped meals should deduct money, not add.")
            self._funds.add(amount, Consts_pb2.FUNDS_RETAIL_PROFITS)
        if from_item_sold or from_comped_item:
            self.set_daily_revenue(self.daily_revenue + amount)
        if from_item_sold:
            self.daily_items_sold += 1

    def transfer_balance_to_household(self):
        owner_household = services.household_manager().get(self._owner_household_id)
        if owner_household is None:
            return
        sim = next(owner_household.instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS))
        funds = self._funds.money
        if funds > 0:
            owner_household._funds.add(funds, Consts_pb2.FUNDS_RETAIL_PROFITS, sim)
        self._funds.try_remove(funds, Consts_pb2.FUNDS_RETAIL_PROFITS, sim)

    def get_daily_outgoing_costs(self, include_employee_wages=True):
        employee_wages = self._employee_manager._daily_employee_wages if include_employee_wages else 0
        return int(employee_wages + sum(self._funds_category_tracker.values()))

    def get_cost_from_tracker(self, funds_category):
        return self._funds_category_tracker.get(funds_category, 0)

    def get_daily_net_profit(self, **kwargs):
        return int(self.daily_revenue - (self.get_daily_outgoing_costs)(**kwargs))

    def get_skills_for_employee_type(self, employee_type):
        employee_type_tuning_data = self._get_tuning_data_for_employee_type(employee_type)
        if employee_type_tuning_data is None:
            return
        return employee_type_tuning_data.skills

    def get_uniform_pose_for_employee_type(self, employee_type):
        employee_type_tuning_data = self._get_tuning_data_for_employee_type(employee_type)
        if employee_type_tuning_data is None:
            return
        return employee_type_tuning_data.uniform_pose

    def is_employee_clocked_in(self, sim_info):
        return self._employee_manager.is_employee_clocked_in(sim_info)

    def on_employee_clock_in(self, employee_sim_info):
        self._employee_manager.on_employee_clock_in(employee_sim_info)

    def on_employee_clock_out(self, employee_sim_info, career_level=DEFAULT):
        self._employee_manager.on_employee_clock_out(employee_sim_info, career_level=career_level)

    def update_employees(self):
        self._employee_manager.update_employees()

    def get_employee_uniform_data(self, employee_type, gender, sim_id=0):
        return self._employee_manager.get_employee_uniform_data(employee_type, gender, sim_id)

    def set_quality_setting(self, quality):
        raise NotImplementedError('set_quality is not implemented this means this business is using the base business manager, no functionality is implemented')

    def set_advertising_type(self, advertising_type):
        raise NotImplementedError('set_advertising_type is not implemented this means this business is using the base business manager, no functionality is implemented')

    def get_current_advertising_cost(self):
        raise NotImplementedError('get_current_advertising_cost is not implemented this means this business is using the base business manager, no functionality is implemented')

    def get_advertising_type_for_gsi(self):
        return ''

    def get_total_employee_wages(self):
        if not self.is_open:
            return self._employee_manager.final_daily_wages()
        return self._employee_manager.get_total_employee_wages()

    def get_employee_career_level(self, employee_sim_info):
        return self._employee_manager.get_employee_career_level(employee_sim_info)

    def get_employee_career(self, employee_sim_info):
        return self._employee_manager.get_employee_career(employee_sim_info)

    def add_employee(self, sim_info, employee_type, is_npc_employee=False):
        self._employee_manager.add_employee(sim_info, employee_type, is_npc_employee=is_npc_employee)
        self.send_min_employee_req_met_update_message()

    def get_employees_on_payroll(self):
        return self._employee_manager.get_employees_on_payroll()

    def get_employee_wages(self, employee_sim_info):
        return self._employee_manager.get_employee_wages(employee_sim_info)

    def get_employee_wages_breakdown_gen(self, employee_sim_info):
        return self._employee_manager.get_employee_wages_breakdown_gen(employee_sim_info)

    def run_hire_interaction(self, target_sim, employee_type):
        employee_tuning_data = self._employee_manager.get_employee_tuning_data_for_employee_type(employee_type)
        return self._employee_manager.run_employee_interaction(employee_tuning_data.interaction_hire, target_sim)

    def run_fire_employee_interaction(self, target_sim):
        employee_data = self._employee_manager.get_employee_data(target_sim.sim_info)
        employee_tuning_data = self._employee_manager.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
        return self._employee_manager.run_employee_interaction(employee_tuning_data.interaction_fire, target_sim)

    def run_promote_employee_interaction(self, target_sim):
        employee_data = self._employee_manager.get_employee_data(target_sim.sim_info)
        employee_tuning_data = self._employee_manager.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
        return self._employee_manager.run_employee_interaction(employee_tuning_data.interaction_promote, target_sim)

    def run_demote_employee_interaction(self, target_sim):
        employee_data = self._employee_manager.get_employee_data(target_sim.sim_info)
        employee_tuning_data = self._employee_manager.get_employee_tuning_data_for_employee_type(employee_data.employee_type)
        return self._employee_manager.run_employee_interaction(employee_tuning_data.interaction_demote, target_sim)

    def try_open_npc_store(self):
        if self.owner_household_id is None:
            self._open_pure_npc_store(services.active_lot().get_premade_status() == PremadeLotStatus.IS_PREMADE)
        else:
            if not self.is_owner_household_active:
                self._open_household_owned_npc_store()
        with telemetry_helper.begin_hook(business_telemetry_writer, TELEMETRY_HOOK_NPC_BUSINESS_VISITED, household=(services.household_manager().get(self.owner_household_id))) as (hook):
            hook.write_enum(TELEMETRY_HOOK_BUSINESS_TYPE, self.business_type)

    def send_data_to_client(self):
        zone = services.get_zone((self._zone_id), allow_uninstantiated_zones=True)
        if zone is None:
            logger.error('Trying to send the business data to client but the business manager {} has an invalid zone id.', self)
            return
        business_data_msg = Business_pb2.SetBusinessData()
        self.construct_business_message(business_data_msg)
        business_data_op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.SET_BUSINESS_DATA, business_data_msg)
        Distributor.instance().add_op_with_no_owner(business_data_op)

    def construct_business_message(self, msg):
        msg.zone_id = self.business_zone_id
        persistence = services.get_persistence_service()
        zone_data = persistence.get_zone_proto_buff(self.business_zone_id)
        if zone_data is not None:
            msg.name = zone_data.name
        msg.is_open = self.is_open
        if self._open_time is not None:
            msg.time_opened = self._open_time.absolute_ticks()
        msg.daily_items_sold = self._daily_items_sold
        msg.daily_outgoing_costs = self.get_daily_outgoing_costs(include_employee_wages=False)
        msg.funds = self.funds.money
        msg.daily_customers_served = self._customer_manager.session_customers_served
        msg.net_profit = self.get_daily_net_profit(include_employee_wages=False)
        msg.markup_chosen = self.markup_multiplier
        msg.daily_revenue = int(self._daily_revenue)
        icon_tuning = self.tuning_data.business_icon
        msg.icon = ResourceKey_pb2.ResourceKey()
        msg.icon.instance = icon_tuning.instance
        msg.icon.group = icon_tuning.group
        msg.icon.type = icon_tuning.type
        msg.review_data = Business_pb2.ReviewDataUpdate()
        self._populate_review_update_message(msg.review_data)
        msg.minimum_employee_requirements_met = self.meets_minimum_employee_requirment()

    def get_interpolated_buff_bucket_value(self, buff_bucket_type, value):
        bucket_data = self.tuning_data.customer_star_rating_buff_bucket_data.get(buff_bucket_type)
        bucket_total = sims4.math.clamp(-1, value, 1)
        if bucket_total >= 0:
            return sims4.math.interpolate(bucket_data.bucket_value_median, bucket_data.bucket_value_maximum, bucket_total)
        return sims4.math.interpolate(bucket_data.bucket_value_median, bucket_data.bucket_value_minimum, abs(bucket_total))

    def process_customer_rating(self, customer_sim_info, customer_star_rating, customer_buff_bucket_totals):
        star_rating_delta = customer_star_rating - self.get_star_rating()
        star_rating_value_change = self.tuning_data.customer_rating_delta_to_business_star_rating_value_change_curve.get(star_rating_delta)
        critic_tuning = self.tuning_data.critic
        if critic_tuning is not None:
            if customer_sim_info.has_trait(critic_tuning.critic_trait):
                star_rating_value_change *= critic_tuning.critic_star_rating_application_count
        for bucket, value in customer_buff_bucket_totals.items():
            self._buff_bucket_totals[bucket] += self.get_interpolated_buff_bucket_value(bucket, value)

        self._buff_bucket_size += 1
        self._adjust_star_rating_value(star_rating_value_change)

    def show_summary_dialog(self, is_from_close=False):
        if self._summary_dialog_class is None:
            raise NotImplementedError('No Summary Dialog specified for business {}'.format(self.business_type()))
        if services.active_household() is None:
            return
        self._summary_dialog_class(self).show_business_summary_dialog()

    def send_min_employee_req_met_update_message(self):
        update_message = Business_pb2.MinEmployeeReqMetUpdate()
        update_message.zone_id = self.business_zone_id
        update_message.minimum_employee_requirements_met = self.meets_minimum_employee_requirment()
        op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_EMPLOYEE_MIN_REQUIREMENT_UPDATE, update_message)
        Distributor.instance().add_op_with_no_owner(op)

    def _open_household_owned_npc_store(self):
        self.set_open(True)

    def _get_star_rating_from_curve(self):
        curve_data = self.tuning_data.star_rating_value_to_user_facing_rating_curve
        if curve_data is None:
            return 0
        return curve_data.get(self._star_rating_value)

    def _get_sorted_delta_buff_buckets_tuple(self):
        if self._buff_bucket_size == 0:
            return
        difference = defaultdict(float)
        for bucket, value in self._buff_bucket_totals.items():
            buff_bucket_data = self.tuning_data.customer_star_rating_buff_bucket_data[bucket]
            difference[bucket] = buff_bucket_data.bucket_value_maximum - value / self._buff_bucket_size

        return sorted((difference.items()), key=(operator.itemgetter(1)), reverse=True)

    def _get_top_performing_bucket_tuple(self):
        if self._buff_bucket_size == 0:
            return
        top_value = None
        top_bucket = None
        for bucket, value in self._buff_bucket_totals.items():
            value /= self._buff_bucket_size
            if top_value is None or value > top_value:
                bucket_data = self.tuning_data.customer_star_rating_buff_bucket_data[bucket]
                if value > bucket_data.bucket_excellence_threshold:
                    top_value = value
                    top_bucket = bucket

        return (
         top_bucket, top_value)

    def set_star_rating_value(self, value):
        self._star_rating_value = 0
        self._adjust_star_rating_value(value)

    def _adjust_star_rating_value(self, delta, send_update_message=True):
        previous_whole_star_rating = int(self.get_star_rating())
        self._star_rating_value = sims4.math.clamp(self.tuning_data.min_and_max_star_rating_value.lower_bound, self._star_rating_value + delta, self.tuning_data.min_and_max_star_rating_value.upper_bound)
        current_whole_star_rating = int(self.get_star_rating())
        if current_whole_star_rating > previous_whole_star_rating:
            if current_whole_star_rating in self.tuning_data.star_rating_to_screen_slam_map:
                screen_slam = self.tuning_data.star_rating_to_screen_slam_map.get(current_whole_star_rating)
                screen_slam.send_screen_slam_message(services.active_sim_info())
        if send_update_message:
            self._send_review_update_message()

    def start_off_lot_simulation_time(self):
        self._last_off_lot_update = services.time_service().sim_now

    def should_show_no_way_to_make_money_notification(self):
        return False

    def meets_minimum_employee_requirment(self):
        return True

    def meets_zone_requirement(self):
        zone_director = services.venue_service().get_zone_director()
        return zone_director is not None and zone_director.supports_business_type(self._business_type)

    def meets_requirements_to_be_open(self):
        return self.meets_zone_requirement() and self.meets_minimum_employee_requirment() and not self.should_show_no_way_to_make_money_notification()

    def _show_appropriate_open_business_notification(self):
        if not self.is_owned_by_npc:
            return self.is_owner_household_active or None
        else:
            active_sim_info = services.active_sim_info()
            if self.should_show_no_way_to_make_money_notification():
                notification = self.tuning_data.no_way_to_make_money_notification(active_sim_info, resolver=(SingleSimResolver(active_sim_info)))
            else:
                notification = self.tuning_data.open_business_notification(active_sim_info, resolver=(SingleSimResolver(active_sim_info)))
        notification.show_dialog()

    def _open_business(self):
        self._show_appropriate_open_business_notification()
        self._clear_state()
        self._is_open = True
        self._open_time = services.time_service().sim_now
        self._employee_manager.open_business()
        if self._owner_household_id is not None:
            owner_household = services.household_manager().get(self.owner_household_id)
            owner_household.bucks_tracker.activate_stored_temporary_perk_timers_of_type(self.tuning_data.bucks)
        else:
            self._distribute_business_open_status(is_open=True, open_time=(self._open_time.absolute_ticks()))
            if self.business_zone_id == services.current_zone_id():
                self.tuning_data.lighting_helper_open.execute_lighting_helper(self)
                zone_director = services.venue_service().get_zone_director()
                zone_director.set_customers_allowed(True)
                zone_director.refresh_open_street_director_status()
            else:
                self.start_off_lot_simulation_time()
        sound = PlaySound(services.get_active_sim(), self.tuning_data.audio_sting_open.instance)
        sound.start()
        self.send_daily_profit_and_cost_update()
        self._send_daily_items_sold_update()
        self._send_review_update_message()

    def _close_business(self, play_sound=True):
        if not self._is_open:
            return
            if play_sound:
                sound = PlaySound(services.get_active_sim(), self.tuning_data.audio_sting_close.instance)
                sound.start()
            self._employee_manager.close_business()
            self.send_daily_profit_and_cost_update()
            self._send_business_closed_telemetry()
            if self._owner_household_id is not None:
                owner_household = services.household_manager().get(self._owner_household_id)
                owner_household.bucks_tracker.deactivate_all_temporary_perk_timers_of_type(self.tuning_data.bucks)
                self.modify_funds((-self._employee_manager.final_daily_wages()), from_item_sold=False)
            self.on_store_closed()
            services.get_event_manager().process_event(TestEvent.BusinessClosed)
            self._distribute_business_open_status(False)
            if self.business_zone_id == services.current_zone_id():
                self.tuning_data.lighting_helper_close.execute_lighting_helper(self)
                zone_director = services.venue_service().get_zone_director()
                if zone_director is not None:
                    zone_director.refresh_open_street_director_status()
        else:
            self.run_off_lot_simulation()
            self._last_off_lot_update = None
        self._is_open = False
        self.show_summary_dialog(is_from_close=True)
        self._open_time = None

    def _clear_state(self):
        self._open_time = None
        self._daily_revenue = 0
        self._daily_items_sold = 0
        self._funds_category_tracker.clear()
        self._buff_bucket_totals.clear()
        self._buff_bucket_size = 0
        self._employee_manager._clear_state()
        self._customer_manager._clear_state()
        self._off_lot_negative_profit_notification_shown = False

    def get_timespan_since_open--- This code section failed: ---

 L.1211         0  LOAD_FAST                'self'
                2  LOAD_ATTR                is_open
                4  POP_JUMP_IF_TRUE     10  'to 10'
                6  LOAD_FAST                'is_from_close'
                8  POP_JUMP_IF_FALSE    20  'to 20'
             10_0  COME_FROM             4  '4'
               10  LOAD_FAST                'self'
               12  LOAD_ATTR                _open_time
               14  LOAD_CONST               None
               16  COMPARE_OP               is
               18  POP_JUMP_IF_FALSE    24  'to 24'
             20_0  COME_FROM             8  '8'

 L.1212        20  LOAD_CONST               None
               22  RETURN_VALUE     
             24_0  COME_FROM            18  '18'

 L.1216        24  LOAD_GLOBAL              services
               26  LOAD_METHOD              game_clock_service
               28  CALL_METHOD_0         0  '0 positional arguments'
               30  LOAD_METHOD              now
               32  CALL_METHOD_0         0  '0 positional arguments'
               34  LOAD_FAST                'self'
               36  LOAD_ATTR                _open_time
               38  BINARY_SUBTRACT  
               40  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 40

    def _send_daily_items_sold_update(self):
        if self.is_active_household_and_zone():
            items_sold_msg = Business_pb2.BusinessDailyItemsSoldUpdate()
            items_sold_msg.zone_id = self.business_zone_id
            items_sold_msg.daily_items_sold = self.daily_items_sold
            op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_DAILY_ITEMS_SOLD_UPDATE, items_sold_msg)
            Distributor.instance().add_op_with_no_owner(op)

    def is_active_household_and_zone(self):
        return self.is_owner_household_active and self._zone_id is not None and self._zone_id == services.current_zone_id()

    def _get_tuning_data_for_employee_type(self, employee_type):
        return self.tuning_data.employee_data_map.get(employee_type, None)

    def _send_business_closed_telemetry(self):
        with telemetry_helper.begin_hook(business_telemetry_writer, TELEMETRY_HOOK_BUSINESS_CLOSED, household=(services.household_manager().get(self.owner_household_id))) as (hook):
            hook.write_int(TELEMETRY_HOOK_LENGTH_BUSINESS_OPENED, self.minutes_open)
            hook.write_int(TELEMETRY_HOOK_NUM_WORKERS, self.employee_count)
            hook.write_int(TELEMETRY_HOOK_AMOUNT_PROFIT, self.get_daily_net_profit())
            hook.write_float(TELEMETRY_HOOK_STAR_RATING, self.get_star_rating())
            hook.write_enum(TELEMETRY_HOOK_BUSINESS_TYPE, self.business_type)

    def send_business_funds_update(self):
        if self.is_owner_household_active:
            funds_msg = Business_pb2.BusinessFundsUpdate()
            funds_msg.available_funds = self.funds.money
            funds_msg.zone_id = self.business_zone_id
            op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_FUNDS_UPDATE, funds_msg)
            Distributor.instance().add_op_with_no_owner(op)

    def send_daily_profit_and_cost_update(self):
        if self.is_owner_household_active:
            profit_msg = Business_pb2.BusinessProfitUpdate()
            profit_msg.zone_id = self.business_zone_id
            profit_msg.net_profit = self.get_daily_net_profit(include_employee_wages=False)
            op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_PROFIT_UPDATE, profit_msg)
            Distributor.instance().add_op_with_no_owner(op)
            cost_msg = Business_pb2.BusinessDailyCostsUpdate()
            cost_msg.zone_id = self.business_zone_id
            cost_msg.daily_outgoing_costs = int(self.get_daily_outgoing_costs())
            op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_DAILY_OUTGOING_COSTS_UPDATE, cost_msg)
            Distributor.instance().add_op_with_no_owner(op)

    def send_markup_multiplier_message(self):
        if not self.is_active_household_and_zone():
            return
        markup_msg = UI_pb2.RetailMarkupMultiplierMessage()
        for markup_multiplier in self.tuning_data.markup_multiplier_data:
            with ProtocolBufferRollback(markup_msg.markup_multipliers) as (multiplier_entry):
                multiplier_entry.name = markup_multiplier.name
                multiplier_entry.multiplier = markup_multiplier.markup_multiplier
                multiplier_entry.is_selected = markup_multiplier.markup_multiplier == self._markup_multiplier

        op = distributor.shared_messages.create_message_op(markup_msg, Consts_pb2.MSG_RETAIL_MARKUP_MULTIPLIER)
        Distributor.instance().add_op_with_no_owner(op)

    def _distribute_business_open_status(self, is_open=True, open_time=0):
        open_msg = Business_pb2.BusinessIsOpenUpdate()
        open_msg.is_open = is_open
        open_msg.time_opened = open_time
        open_msg.zone_id = self.business_zone_id
        op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.BUSINESS_OPEN_UPDATE, open_msg)
        Distributor.instance().add_op_with_no_owner(op)

    def _send_review_update_message(self):
        review_msg = Business_pb2.ReviewDataUpdate()
        self._populate_review_update_message(review_msg)
        op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.REVIEW_DATA_UPDATE, review_msg)
        Distributor.instance().add_op_with_no_owner(op)

    def _populate_review_update_message(self, review_msg):
        review_msg.zone_id = self.business_zone_id
        review_msg.score = self.get_star_rating()
        review_msg.review_count = self._customer_manager.lifetime_customers_served
        sorted_buckets = self._get_sorted_delta_buff_buckets_tuple()
        if sorted_buckets is None or len(sorted_buckets) == 0:
            return
        bottom_growth_msg = review_msg.icons.add()
        top_growth_msg = review_msg.icons.add()
        excellence_msg = review_msg.icons.add()
        top_performer_bucket, top_performer_value = self._get_top_performing_bucket_tuple()
        if top_performer_bucket is not None:
            top_bucket_data = self.tuning_data.customer_star_rating_buff_bucket_data[top_performer_bucket]
            self._fill_review_data(True, top_bucket_data, excellence_msg, top_bucket_data.bucket_value_maximum - top_performer_value)
        top_growth_filled = False
        for buff_bucket, delta in sorted_buckets:
            buff_bucket_data = self.tuning_data.customer_star_rating_buff_bucket_data[buff_bucket]
            if delta < buff_bucket_data.bucket_growth_opportunity_threshold:
                continue
            if not top_growth_filled:
                self._fill_review_data(False, buff_bucket_data, top_growth_msg, delta)
                top_growth_filled = True
            else:
                self._fill_review_data(False, buff_bucket_data, bottom_growth_msg, delta)
                break

    def _fill_review_data(self, is_positive, buff_bucket_data, icon_msg, delta):
        icon_msg.desc = buff_bucket_data.bucket_excellence_text() if is_positive else buff_bucket_data.bucket_growth_opportunity_text()
        icon_msg.icon = ResourceKey_pb2.ResourceKey()
        icon_msg.icon.instance = buff_bucket_data.bucket_icon.instance
        icon_msg.icon.group = buff_bucket_data.bucket_icon.group
        icon_msg.icon.type = buff_bucket_data.bucket_icon.type
        icon_msg.title = buff_bucket_data.bucket_title

    def populate_employee_msg(self, sim_info, employee_msg, business_employee_type, business_employee_data):
        employee_msg.sim_id = sim_info.sim_id
        employee_data = self._employee_manager.get_employee_data(sim_info)
        employee_is_training = sim_info.has_buff_with_tag(self.tuning_data.employee_training_buff_tag)
        for skill_type, skill_type_data in business_employee_data.employee_skills.items():
            with ProtocolBufferRollback(employee_msg.skill_data) as (employee_skill_msg):
                employee_skill_msg.skill_id = skill_type.guid64
                employee_skill_msg.curr_points = int(sim_info.get_stat_value(skill_type))
                employee_skill_msg.is_training = employee_is_training
                employee_skill_msg.has_skilled_up = employee_data.has_leveled_up_skill(skill_type) if employee_data is not None else False
                employee_skill_msg.skill_tooltip = skill_type_data.business_summary_description

        if self.is_employee(sim_info):
            satisfaction_stat = sim_info.get_statistic(business_employee_data.satisfaction_commodity)
            statisfaction_state_index = satisfaction_stat.get_state_index()
            if statisfaction_state_index is not None:
                employee_msg.satisfaction_string = satisfaction_stat.states[statisfaction_state_index].buff.buff_type.buff_name(sim_info)
            career_level = self.get_employee_career_level(sim_info)
            employee_msg.pay = career_level.simoleons_per_hour
            career = self.get_employee_career(sim_info)
            employee_msg.current_career_level = career.level
            employee_msg.max_career_level = len(career.current_track_tuning.career_levels) - 1
        else:
            desired_level = self.get_desired_career_level(sim_info, business_employee_type)
            career_level = business_employee_data.career.start_track.career_levels[desired_level]
            employee_msg.pay = career_level.simoleons_per_hour
            employee_msg.current_career_level = desired_level
            employee_msg.max_career_level = len(business_employee_data.career.start_track.career_levels) - 1

    def on_protocols_loaded(self):
        pass

    def on_build_buy_enter(self):
        self.send_business_funds_update()

    def on_build_buy_exit(self):
        if self._owner_household_id is not None:
            owner_household = services.household_manager().get(self._owner_household_id)
            owner_household.funds.send_money_update(vfx_amount=0)
        if not self.meets_requirements_to_be_open():
            self.set_open(False)

    def on_zone_load(self):
        services.get_event_manager().register(self, self.EVENTS)
        self._employee_manager.on_zone_load()
        self._customer_manager.on_zone_load()
        if self.should_close_after_load():
            self._close_business(play_sound=False)
        self._funds._send_money_update_internal(self._owner_household_id, 0)
        self.send_daily_profit_and_cost_update()
        self._send_daily_items_sold_update()

    def on_client_disconnect(self):
        self._employee_manager.on_client_disconnect()
        event_manager = services.get_event_manager()
        if event_manager is not None:
            event_manager.unregister(self, self.EVENTS)

    def on_registered_perk_callback(self):
        if self.tuning_data.quality_unlock_perk is None:
            return
        if self.is_owner_household_active:
            active_household = services.active_household()
            bucks_tracker = active_household.bucks_tracker
            quality_unlocked = bucks_tracker.is_perk_unlocked(self.tuning_data.quality_unlock_perk)
            if self._quality_unlocked != quality_unlocked:
                self._quality_unlocked = quality_unlocked
                self.send_data_to_client()
            if not self._quality_unlocked:
                active_household.bucks_tracker.add_perk_unlocked_callback(self.tuning_data.bucks, self._business_perk_unlocked_callback)
                current_zone = services.current_zone()
                if current_zone is not None:
                    current_zone.register_callback(ZoneState.SHUTDOWN_STARTED, self._unregister_perk_unlock_callback)

    def _unregister_perk_unlock_callback(self):
        if not self._quality_unlocked:
            owning_household = services.household_manager().get(self.owner_household_id)
            if owning_household is None:
                return
            owning_household.bucks_tracker.remove_perk_unlocked_callback(self.tuning_data.bucks, self._business_perk_unlocked_callback)

    def _business_perk_unlocked_callback(self, perk):
        if perk == self.tuning_data.quality_unlock_perk:
            self._unregister_perk_unlock_callback()
            self._quality_unlocked = True
            self._distribute_business_manager_data_message()
            current_zone = services.current_zone()
            if current_zone is not None:
                current_zone.unregister_callback(ZoneState.SHUTDOWN_STARTED, self._unregister_perk_unlock_callback)

    def _distribute_business_manager_data_message(self):
        pass

    def handle_event(self, sim_info, event, resolver):
        if event == TestEvent.SimDeathTypeSet:
            if self.is_employee(sim_info):
                self.remove_employee(sim_info)

    def save_data(self, business_save_data):
        business_save_data.is_open = self._is_open
        business_save_data.funds = self._funds.money
        business_save_data.markup = self._markup_multiplier
        business_save_data.grand_opening = self._grand_opening
        business_save_data.daily_revenue = int(self._daily_revenue)
        business_save_data.daily_items_sold = self._daily_items_sold
        business_save_data.star_rating_value = self._star_rating_value
        self.start_off_lot_simulation_time()
        business_save_data.last_off_lot_update = self._last_off_lot_update
        if self._open_time is not None:
            business_save_data.open_time = self._open_time.absolute_ticks()
        for funds_category, amount in self._funds_category_tracker.items():
            with ProtocolBufferRollback(business_save_data.funds_category_tracker_data) as (funds_category_msg):
                funds_category_msg.funds_category = funds_category
                funds_category_msg.amount = int(amount)

        for buff_bucket, buff_bucket_total in self._buff_bucket_totals.items():
            with ProtocolBufferRollback(business_save_data.buff_bucket_totals) as (buff_bucket_total_msg):
                buff_bucket_total_msg.buff_bucket = buff_bucket
                buff_bucket_total_msg.buff_bucket_total = buff_bucket_total

        business_save_data.buff_bucket_size = self._buff_bucket_size
        self._employee_manager.save_data(business_save_data.employee_payroll)
        self._customer_manager.save_data(business_save_data)

    def load_data(self, business_save_data, is_legacy=False):
        self._is_open = business_save_data.is_open
        self._markup_multiplier = business_save_data.markup
        self._grand_opening = business_save_data.grand_opening
        self._daily_revenue = business_save_data.daily_revenue
        self._daily_items_sold = business_save_data.daily_items_sold
        if self._is_open:
            self._open_time = DateAndTime(business_save_data.open_time)
            self._distribute_business_open_status(is_open=(self._is_open), open_time=(self._open_time.absolute_ticks()))
        else:
            self._distribute_business_open_status(self._is_open)
        for funds_category_msg in business_save_data.funds_category_tracker_data:
            self._funds_category_tracker[funds_category_msg.funds_category] = funds_category_msg.amount

        self._funds = BusinessFunds(self._owner_household_id, business_save_data.funds, self)
        if is_legacy:
            self._employee_manager.load_legacy_data(business_save_data)
        else:
            self._buff_bucket_totals.clear()
            for buff_bucket_total_msg in business_save_data.buff_bucket_totals:
                self._buff_bucket_totals[buff_bucket_total_msg.buff_bucket] = buff_bucket_total_msg.buff_bucket_total

            self._last_off_lot_update = DateAndTime(business_save_data.last_off_lot_update)
            self._star_rating_value = business_save_data.star_rating_value
            self._buff_bucket_size = business_save_data.buff_bucket_size
            self._customer_manager.load_data(business_save_data)
            self._employee_manager.load_data(business_save_data.employee_payroll)

    def on_loading_screen_animation_finished(self):
        self._customer_manager.on_loading_screen_animation_finished()
        if self._grand_opening:
            self._grand_opening = False
            FundsTransferDialog.show_dialog(first_time_buyer=True)
            if self.tuning_data.grand_opening_notification is not None:
                active_sim_info = services.active_sim_info()
                notification = self.tuning_data.grand_opening_notification(active_sim_info, resolver=(SingleSimResolver(active_sim_info)))
                notification.show_dialog()
        elif self.should_close_after_load():
            self._close_business(play_sound=False)
