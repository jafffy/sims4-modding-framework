# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\animation\arb_accumulator.py
# Compiled at: 2017-10-09 18:09:11
# Size of source mod 2**32: 24944 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
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
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_SUBTRACT . 
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
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
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
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= or . 
expr ::= subscript . 
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
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_closure load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1 . 
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
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
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
inplace_op ::= INPLACE_SUBTRACT . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
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
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR . LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR LOAD_STR . 
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
stmt ::= aug_assign1 . 
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
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr BUILD_TUPLE_1 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_3 . store store store
unpack ::= UNPACK_SEQUENCE_3 store . store store
unpack ::= UNPACK_SEQUENCE_3 store store . store
unpack ::= UNPACK_SEQUENCE_3 store store store . 
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
   
 L. 128       238  LOAD_FAST                'arb_accumulator'
                 240  LOAD_METHOD              set_time_debt
                 242  LOAD_FAST                'actors'
                 244  LOAD_CONST               0
                 246  CALL_METHOD_2         2  '2 positional arguments'
                 248  POP_TOP          
               250_0  COME_FROM           228  '228'
               250_1  COME_FROM           194  '194'
->             250_2  COME_FROM_LOOP      146  '146'
               250_3  COME_FROM            86  '86'
from weakref import WeakKeyDictionary
import time
from animation.animation_sleep_element import AnimationSleepElement
from animation.animation_utils import get_actors_for_arb_sequence
from animation.arb_element import ArbElement, distribute_arb_element
from sims4.tuning.tunable import TunableRealSecond, Tunable
import animation.arb, distributor.system, element_utils, elements, services, sims4.callback_utils, sims4.log, sims4.service_manager
logger = sims4.log.Logger('ArbAccumulator')
dump_logger = sims4.log.LoggerClass('ArbAccumulator')

def _get_actors_for_arb_element_sequence(arb_element_sequence, main_timeline_only=False):
    all_actors = set()
    for arb_element in arb_element_sequence:
        for actor in arb_element._actors(main_timeline_only):
            if actor.is_sim:
                all_actors.add(actor)

    return all_actors


def with_skippable_animation_time(actors, sequence=None):

    def _with_skippable_animation_time(timeline):
        then = time.monotonic()
        yield from element_utils.run_child(timeline, sequence)
        now = time.monotonic()
        duration = now - then
        arb_accumulator = services.current_zone().arb_accumulator_service
        for actor in actors:
            time_debt = arb_accumulator.get_time_debt((actor,))
            new_time_debt = max(0, time_debt - duration)
            arb_accumulator.set_time_debt((actor,), new_time_debt)

        if False:
            yield None

    return element_utils.build_element(_with_skippable_animation_time)


class ArbSequenceElement(elements.SubclassableGeneratorElement):

    def __init__(self, arb_element_sequence, *args, animate_instantly=False, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._arb_element_sequence = arb_element_sequence
        self._current_arb_element = None
        self._animate_instantly = animate_instantly

    def _run_gen--- This code section failed: ---

 L.  77         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _arb_element_sequence
                4  POP_JUMP_IF_TRUE     10  'to 10'

 L.  78         6  LOAD_CONST               True
                8  RETURN_VALUE     
             10_0  COME_FROM             4  '4'

 L.  80        10  LOAD_CONST               0
               12  STORE_FAST               'duration_must_run'

 L.  82        14  SETUP_LOOP           70  'to 70'
               16  LOAD_FAST                'self'
               18  LOAD_ATTR                _arb_element_sequence
               20  GET_ITER         
               22  FOR_ITER             68  'to 68'
               24  STORE_FAST               'arb_element'

 L.  83        26  LOAD_FAST                'arb_element'
               28  LOAD_ATTR                arb
               30  LOAD_METHOD              get_timing
               32  CALL_METHOD_0         0  '0 positional arguments'
               34  UNPACK_SEQUENCE_3     3 
               36  STORE_FAST               'arb_duration_total'
               38  STORE_FAST               'arb_duration_must_run'
               40  STORE_FAST               'arb_duration_repeat'

 L.  84        42  LOAD_FAST                'arb_duration_total'
               44  LOAD_FAST                'arb_duration_must_run'
               46  BINARY_SUBTRACT  
               48  STORE_FAST               'arb_duration_interrupt'

 L.  87        50  LOAD_FAST                'duration_must_run'
               52  LOAD_FAST                'arb_duration_must_run'
               54  INPLACE_ADD      
               56  STORE_FAST               'duration_must_run'

 L.  91        58  LOAD_FAST                'arb_element'
               60  LOAD_METHOD              distribute
               62  CALL_METHOD_0         0  '0 positional arguments'
               64  POP_TOP          
               66  JUMP_BACK            22  'to 22'
               68  POP_BLOCK        
             70_0  COME_FROM_LOOP       14  '14'

 L.  94        70  LOAD_FAST                'arb_duration_interrupt'
               72  STORE_FAST               'duration_interrupt'

 L.  96        74  LOAD_FAST                'arb_duration_repeat'
               76  STORE_FAST               'duration_repeat'

 L.  99        78  LOAD_GLOBAL              ArbAccumulatorService
               80  LOAD_ATTR                MAXIMUM_TIME_DEBT
               82  LOAD_CONST               0
               84  COMPARE_OP               >
               86  POP_JUMP_IF_FALSE   250  'to 250'

 L. 102        88  LOAD_GLOBAL              _get_actors_for_arb_element_sequence
               90  LOAD_FAST                'self'
               92  LOAD_ATTR                _arb_element_sequence
               94  LOAD_CONST               True
               96  LOAD_CONST               ('main_timeline_only',)
               98  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              100  STORE_FAST               'actors'

 L. 103       102  LOAD_GLOBAL              services
              104  LOAD_METHOD              current_zone
              106  CALL_METHOD_0         0  '0 positional arguments'
              108  LOAD_ATTR                arb_accumulator_service
              110  STORE_FAST               'arb_accumulator'

 L. 104       112  LOAD_FAST                'arb_accumulator'
              114  LOAD_METHOD              get_time_debt
              116  LOAD_FAST                'actors'
              118  CALL_METHOD_1         1  '1 positional argument'
              120  STORE_FAST               'time_debt_max'

 L. 107       122  LOAD_FAST                'arb_accumulator'
              124  LOAD_METHOD              get_shave_time_given_duration_and_debt
              126  LOAD_FAST                'duration_must_run'

 L. 108       128  LOAD_FAST                'time_debt_max'
              130  CALL_METHOD_2         2  '2 positional arguments'
              132  STORE_FAST               'shave_time_actual'

 L. 111       134  LOAD_FAST                'duration_must_run'
              136  LOAD_FAST                'shave_time_actual'
              138  INPLACE_SUBTRACT 
              140  STORE_FAST               'duration_must_run'

 L. 113       142  LOAD_FAST                'shave_time_actual'
              144  POP_JUMP_IF_FALSE   196  'to 196'

 L. 114       146  SETUP_LOOP          250  'to 250'
              148  LOAD_FAST                'actors'
              150  GET_ITER         
              152  FOR_ITER            192  'to 192'
              154  STORE_FAST               'actor'

 L. 117       156  LOAD_FAST                'arb_accumulator'
              158  LOAD_METHOD              get_time_debt
              160  LOAD_FAST                'actor'
              162  BUILD_TUPLE_1         1 
              164  CALL_METHOD_1         1  '1 positional argument'
              166  STORE_FAST               'time_debt'

 L. 118       168  LOAD_FAST                'time_debt'
              170  LOAD_FAST                'shave_time_actual'
              172  INPLACE_ADD      
              174  STORE_FAST               'time_debt'

 L. 119       176  LOAD_FAST                'arb_accumulator'
              178  LOAD_METHOD              set_time_debt
              180  LOAD_FAST                'actor'
              182  BUILD_TUPLE_1         1 
              184  LOAD_FAST                'time_debt'
              186  CALL_METHOD_2         2  '2 positional arguments'
              188  POP_TOP          
              190  JUMP_BACK           152  'to 152'
              192  POP_BLOCK        
              194  JUMP_FORWARD        250  'to 250'
            196_0  COME_FROM           144  '144'

 L. 125       196  LOAD_FAST                'self'
              198  LOAD_ATTR                _arb_element_sequence
              200  LOAD_CONST               -1
              202  BINARY_SUBSCR    
              204  LOAD_ATTR                arb
              206  STORE_DEREF              'last_arb'

 L. 126       208  LOAD_GLOBAL              all
              210  LOAD_CLOSURE             'last_arb'
              212  BUILD_TUPLE_1         1 
              214  LOAD_GENEXPR             '<code_object <genexpr>>'
              216  LOAD_STR                 'ArbSequenceElement._run_gen.<locals>.<genexpr>'
              218  MAKE_FUNCTION_8          'closure'
              220  LOAD_FAST                'actors'
              222  GET_ITER         
              224  CALL_FUNCTION_1       1  '1 positional argument'
              226  CALL_FUNCTION_1       1  '1 positional argument'
              228  POP_JUMP_IF_FALSE   250  'to 250'

 L. 127       230  LOAD_FAST                'duration_must_run'
              232  LOAD_FAST                'time_debt_max'
              234  INPLACE_ADD      
              236  STORE_FAST               'duration_must_run'

 L. 128       238  LOAD_FAST                'arb_accumulator'
              240  LOAD_METHOD              set_time_debt
              242  LOAD_FAST                'actors'
              244  LOAD_CONST               0
              246  CALL_METHOD_2         2  '2 positional arguments'
              248  POP_TOP          
            250_0  COME_FROM           228  '228'
            250_1  COME_FROM           194  '194'
            250_2  COME_FROM_LOOP      146  '146'
            250_3  COME_FROM            86  '86'

 L. 130       250  LOAD_GLOBAL              tuple
              252  LOAD_GENEXPR             '<code_object <genexpr>>'
              254  LOAD_STR                 'ArbSequenceElement._run_gen.<locals>.<genexpr>'
              256  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              258  LOAD_FAST                'self'
              260  LOAD_ATTR                _arb_element_sequence
              262  GET_ITER         
              264  CALL_FUNCTION_1       1  '1 positional argument'
              266  CALL_FUNCTION_1       1  '1 positional argument'
              268  STORE_FAST               'arbs'

 L. 131       270  LOAD_GLOBAL              AnimationSleepElement
              272  LOAD_FAST                'duration_must_run'
              274  LOAD_FAST                'duration_interrupt'
              276  LOAD_FAST                'duration_repeat'
              278  LOAD_FAST                'arbs'
              280  LOAD_CONST               ('arbs',)
              282  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              284  STORE_FAST               'animation_sleep_element'

 L. 133       286  LOAD_FAST                'self'
              288  LOAD_ATTR                _animate_instantly
          290_292  POP_JUMP_IF_TRUE    312  'to 312'

 L. 134       294  LOAD_GLOBAL              element_utils
              296  LOAD_METHOD              run_child
              298  LOAD_FAST                'timeline'
              300  LOAD_FAST                'animation_sleep_element'
              302  CALL_METHOD_2         2  '2 positional arguments'
              304  GET_YIELD_FROM_ITER
              306  LOAD_CONST               None
              308  YIELD_FROM       
              310  POP_TOP          
            312_0  COME_FROM           290  '290'

 L. 138       312  LOAD_FAST                'animation_sleep_element'
              314  LOAD_ATTR                optional_time_elapsed
              316  STORE_FAST               'optional_time_elapsed'

 L. 140       318  LOAD_GLOBAL              ArbAccumulatorService
              320  LOAD_ATTR                MAXIMUM_TIME_DEBT
              322  LOAD_CONST               0
              324  COMPARE_OP               >
          326_328  POP_JUMP_IF_FALSE   400  'to 400'

 L. 141       330  LOAD_FAST                'optional_time_elapsed'
              332  LOAD_CONST               0
              334  COMPARE_OP               >
          336_338  POP_JUMP_IF_FALSE   400  'to 400'

 L. 142       340  SETUP_LOOP          400  'to 400'
              342  LOAD_FAST                'actors'
              344  GET_ITER         
              346  FOR_ITER            398  'to 398'
              348  STORE_FAST               'actor'

 L. 143       350  LOAD_FAST                'arb_accumulator'
              352  LOAD_METHOD              get_time_debt
              354  LOAD_FAST                'actor'
              356  BUILD_TUPLE_1         1 
              358  CALL_METHOD_1         1  '1 positional argument'
              360  STORE_FAST               'time_debt'

 L. 144       362  LOAD_FAST                'time_debt'
              364  LOAD_FAST                'optional_time_elapsed'
              366  BINARY_SUBTRACT  
              368  STORE_FAST               'new_time_debt'

 L. 145       370  LOAD_GLOBAL              max
              372  LOAD_FAST                'new_time_debt'
              374  LOAD_CONST               0
              376  CALL_FUNCTION_2       2  '2 positional arguments'
              378  STORE_FAST               'new_time_debt'

 L. 146       380  LOAD_FAST                'arb_accumulator'
              382  LOAD_METHOD              set_time_debt
              384  LOAD_FAST                'actor'
              386  BUILD_TUPLE_1         1 
              388  LOAD_FAST                'new_time_debt'
              390  CALL_METHOD_2         2  '2 positional arguments'
              392  POP_TOP          
          394_396  JUMP_BACK           346  'to 346'
              398  POP_BLOCK        
            400_0  COME_FROM_LOOP      340  '340'
            400_1  COME_FROM           336  '336'
            400_2  COME_FROM           326  '326'

 L. 148       400  LOAD_CONST               True
              402  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM_LOOP' instruction at offset 250_2


class _arb_parallelizer:

    def __init__(self, arb_accumulator):
        self._arb_accumulator = arb_accumulator
        self._arb_sequence = None
        self._old_add_arb_fn = None

    def _add_arb(self, arb, on_done_fn=None):
        if arb.empty:
            return
        if self._arb_sequence is None:
            self._arb_sequence = []
        self._arb_sequence.append(arb)

    def __enter__(self):
        self._old_add_arb_fn = self._arb_accumulator.add_arb
        self._arb_accumulator.add_arb = self._add_arb

    def __exit__(self, exc_type, exc_value, traceback):
        self._arb_accumulator.add_arb = self._old_add_arb_fn
        if self._arb_sequence:
            self._arb_accumulator.add_arb(self._arb_sequence)


class ArbAccumulatorService(sims4.service_manager.Service):
    CUSTOM_EVENT = 901
    MAX_XEVT = 999
    MAXIMUM_TIME_DEBT = TunableRealSecond(1, description='\n    The maximum amount of time in seconds to allow the server to run ahead \n    of the client when running a contiguous block of animation/routing to \n    improve blending. Setting this to 0 will disable this feature but ruin blending.')
    MAXIMUM_SHAVE_FRAMES_PER_ANIMATION = Tunable(int, 5, description='\n    The maximum number of frames to shave off of the must-run duration of each \n    animation until we reach a total amount of time debt equal to MAXIMUM_TIME_DEBT.')
    MAXIMUM_SHAVE_ANIMATION_RATIO = Tunable(float, 2, description='\n    The maximum ratio of an animation to shave off. For example, if this\n    is tuned to 2, we will shave off at most 1/2 of the total must-run\n    duration of an animation.\n    ')

    @staticmethod
    def get_shave_time_given_duration_and_debt(duration, debt):
        shave_time_max = max(0, ArbAccumulatorService.MAXIMUM_TIME_DEBT - debt)
        shave_time_requested = min(duration / ArbAccumulatorService.MAXIMUM_SHAVE_ANIMATION_RATIO, 0.03333333333333333 * ArbAccumulatorService.MAXIMUM_SHAVE_FRAMES_PER_ANIMATION)
        shave_time_actual = min(shave_time_max, shave_time_requested)
        return shave_time_actual

    def __init__(self, from_idle_fn, to_idle_fn):
        self._from_idle_func = from_idle_fn
        self._to_idle_func = to_idle_fn
        self._arb_sequence = []
        self._on_done = sims4.callback_utils.CallableList()
        self._in_flush = False
        self._custom_xevt_id_generator = self.CUSTOM_EVENT
        self._sequence_parallel = None
        self._time_debt = WeakKeyDictionary()
        self._shave_time = WeakKeyDictionary()

    def get_time_debt(self, sims):
        max_debt = 0
        for sim in sims:
            if sim not in self._time_debt:
                continue
            sim_debt = self._time_debt[sim]
            if sim_debt > max_debt:
                max_debt = sim_debt

        return max_debt

    def set_time_debt(self, sims, debt):
        for sim in sims:
            self._time_debt[sim] = debt

    def _clear(self):
        self._arb_sequence = []
        self._on_done = sims4.callback_utils.CallableList()
        self._custom_xevt_id_generator = self.CUSTOM_EVENT

    def parallelize(self):
        return _arb_parallelizer(self)

    def add_arb(self, arb, on_done_fn=None):
        if isinstance(arb, list):
            arbs = arb
        else:
            arbs = (
             arb,)
        for sub_arb in arbs:
            if not sub_arb._actors():
                logger.error('Attempt to play animation that has no connected actors:')
                sub_arb.log_request_history(dump_logger.error)

        if self._in_flush:
            for sub_arb in arbs:
                logger.debug('\n\nEvent-triggered ARB:\n{}\n\n', sub_arb.get_contents_as_string())
                distribute_arb_element(sub_arb)
                if on_done_fn is not None:
                    on_done_fn()

            return
        self._arb_sequence.append(arb)
        if on_done_fn is not None:
            self._on_done.append(on_done_fn)

    def claim_xevt_id(self):
        event_id = self._custom_xevt_id_generator
        self._custom_xevt_id_generator += 1
        if self._custom_xevt_id_generator == self.MAX_XEVT:
            logger.warn('Excessive XEVT IDs claimed before a flush. This is likely caused by an error in animation requests. -RS')
        return event_id

    def _add_idles_to_arb_element(self, arb_element, on_done):
        all_actors = arb_element._actors()
        actors_with_idles = set()
        if self._to_idle_func is not None:
            for actor in all_actors:
                if actor.is_sim:
                    to_idle_arb, on_done_func = arb_element.arb._normal_timeline_ends_in_looping_content(actor.id) or self._to_idle_func(actor)
                    if on_done_func is not None:
                        on_done.append(on_done_func)
                    if to_idle_arb is not None:
                        arb_element.execute_and_merge_arb(to_idle_arb, False)
                        actors_with_idles.add(actor)

        return actors_with_idles

    def _begin_arb_element(self, all_actors, actors_with_idles, on_done):
        element = ArbElement((animation.arb.Arb()), event_records=[])
        if actors_with_idles:
            if self._from_idle_func is not None:
                for actor in actors_with_idles:
                    from_idle_arb, on_done_idle = self._from_idle_func(actor)
                    if on_done_idle is not None:
                        on_done.append(on_done_idle)
                    if from_idle_arb is not None:
                        self._append_arb_to_element(element, from_idle_arb, all_actors, False)

                actors_with_idles.clear()
        return element

    def _flush_arb_element(self, element_run_queue, arb_element, all_actors, on_done, closes_sequence):
        if not arb_element.arb.empty:
            actors_with_idles = self._add_idles_to_arb_element(arb_element, on_done)
            if not closes_sequence:
                arb_element.enable_optional_sleep_time = False
            if arb_element.arb.empty:
                raise RuntimeError('About to flush an empty Arb')
            element_run_queue.append(arb_element)
            if not closes_sequence:
                return self._begin_arb_element(all_actors, actors_with_idles, on_done)
            return
        return arb_element

    def _append_arb_to_element(self, buffer_arb_element, arb, actors, safe_mode, attach=True):
        if not arb.empty:
            if buffer_arb_element.arb._can_append(arb, safe_mode):
                buffer_arb_element.event_records = buffer_arb_element.event_records or []
                if attach:
                    (buffer_arb_element.attach)(*actors, **{'actor_instances': arb._actor_instances()})
                buffer_arb_element.execute_and_merge_arb(arb, safe_mode)
                return True
        return False

    def _append_arb_element_to_element(self, buffer_arb_element, arb_element, actors, safe_mode):
        if not arb_element.arb.empty:
            if buffer_arb_element.arb._can_append(arb_element.arb, safe_mode):
                buffer_arb_element.event_records = buffer_arb_element.event_records or []
                (buffer_arb_element.attach)(*actors)
                buffer_arb_element.event_records.extend(arb_element.event_records)
                buffer_arb_element.arb.append(arb_element.arb, safe_mode)
                return True
        return False

    def flush(self, timeline, animate_instantly=False):
        arb_sequence = self._arb_sequence
        on_done = self._on_done
        self._clear()
        actors = get_actors_for_arb_sequence(*arb_sequence)
        self._in_flush = True
        try:
            if len(actors) > 0:
                first_unprocessed_arb = 0
                sequence_len = len(arb_sequence)
                buffer_arb_element = None
                element_run_queue = []
                sim_actors = [actor for actor in actors if actor.is_sim]
                with distributor.system.Distributor.instance().dependent_block():
                    while first_unprocessed_arb < sequence_len:
                        if buffer_arb_element is None:
                            buffer_arb_element = self._begin_arb_element(actors, sim_actors, on_done)
                        for i in range(first_unprocessed_arb, sequence_len):
                            arb = arb_sequence[i]
                            if isinstance(arb, list):
                                combined_arb = animation.arb.Arb()
                                for sub_arb in arb:
                                    combined_arb.append(sub_arb, False, True)

                                if not buffer_arb_element.arb._can_append(combined_arb, True):
                                    break
                                (buffer_arb_element.attach)(*actors)
                                buffer_arb_element_parallel = self._begin_arb_element(actors, None, on_done)
                                result = self._append_arb_to_element(buffer_arb_element_parallel, combined_arb,
                                  actors,
                                  False, attach=False)
                                arb_sequence[i] = buffer_arb_element_parallel
                                arb = buffer_arb_element_parallel
                                buffer_arb_element_parallel.detach()
                            elif isinstance(arb, ArbElement):
                                append_fn = self._append_arb_element_to_element
                            else:
                                append_fn = self._append_arb_to_element
                            if not append_fn(buffer_arb_element, arb, actors, True):
                                first_unprocessed_arb = i
                                break
                            first_unprocessed_arb = i + 1

                        buffer_arb_element = self._flush_arb_element(element_run_queue, buffer_arb_element, actors, on_done, first_unprocessed_arb == sequence_len)

                self._in_flush = False
                arb_sequence_element = ArbSequenceElement(element_run_queue, animate_instantly=animate_instantly)
                yield from element_utils.run_child(timeline, arb_sequence_element)
        finally:
            self._in_flush = False
            on_done()

        if False:
            yield None
