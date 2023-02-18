# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\crafting_component.py
# Compiled at: 2021-02-18 23:03:01
# Size of source mod 2**32: 30522 bytes

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
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
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
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
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
continues ::= lastl_stmt . continue
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
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
expr ::= dict . 
expr ::= get_iter . 
expr ::= or . 
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
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
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
kvlist_0 ::= BUILD_MAP_0 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
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
store ::= store_subscript . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
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
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
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
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 455       122  LOAD_FAST                'consume_affordance'
                 124  RETURN_VALUE     
               126_0  COME_FROM           120  '120'
               126_1  COME_FROM            96  '96'
->             126_2  COME_FROM_LOOP       48  '48'
               126_3  COME_FROM            38  '38'
from crafting.crafting_process import CraftingProcess, logger
from crafting.crafting_tunable import CraftingTuning
from event_testing import test_events
from notebook.notebook_entry import SubEntryData
from objects.components import Component, componentmethod, types, componentmethod_with_fallback
from objects.components.spoilable_object_mixin import SpoilableObjectMixin
from objects.game_object_properties import GameObjectProperty
from objects.hovertip import TooltipFieldsComplete
from protocolbuffers import SimObjectAttributes_pb2 as protocols, UI_pb2 as ui_protocols
from sims4.callback_utils import CallableList
from sims4.localization import LocalizationHelperTuning
from singletons import DEFAULT
import random, services, zone_types

class CraftingComponent(SpoilableObjectMixin, Component, component_name=types.CRAFTING_COMPONENT, persistence_key=protocols.PersistenceMaster.PersistableData.CraftingComponent, allow_dynamic=True):

    def __init__(self, owner, **kwargs):
        (super().__init__)(owner, **kwargs)
        self._crafting_process = None
        self._use_base_recipe = False
        self.object_mutated_listeners = CallableList()
        self._servings_statistic_tracker_handle = None
        self._quality_change_callback_added = False
        self._is_final_product = False

    @property
    def is_final_product(self):
        return self._is_final_product

    def set_final_product(self, is_final_product):
        self._is_final_product = is_final_product

    @componentmethod_with_fallback((lambda: (DEFAULT, DEFAULT)))
    def get_template_content_overrides(self):
        is_final_product = self._crafting_process.phase is None or self._crafting_process.phase.object_info_is_final_product
        if is_final_product or self.owner.name_component is None:
            return (
             DEFAULT, DEFAULT)
        name_component = self._crafting_process.recipe.final_product_definition.cls.tuned_components.name
        if name_component is not None:
            if name_component.templates:
                selected_template = random.choice(name_component.templates)
                return (selected_template.template_name, selected_template.template_description)
        return (
         DEFAULT, DEFAULT)

    def on_add(self, *_, **__):
        tracker = self.owner.get_tracker(CraftingTuning.SERVINGS_STATISTIC)
        self._servings_statistic_tracker_handle = tracker.add_watcher(self._on_servings_change)
        if tracker.has_statistic(CraftingTuning.SERVINGS_STATISTIC):
            current_value = tracker.get_value(CraftingTuning.SERVINGS_STATISTIC)
            if current_value is not None:
                self.owner.update_tooltip_field((TooltipFieldsComplete.servings), (max(int(current_value), 0)), should_update=True)
        if self.owner.state_component is not None:
            self.owner.add_state_changed_callback(self._on_object_state_change)
            self._quality_change_callback_added = True
            consumable_state_value = self.owner.get_state_value_from_stat_type(CraftingTuning.CONSUME_STATISTIC)
            if consumable_state_value is not None:
                self._on_object_state_change(self.owner, consumable_state_value.state, consumable_state_value, consumable_state_value)
            quality_state_value = self.owner.get_state_value_from_stat_type(CraftingTuning.QUALITY_STATISTIC)
            if quality_state_value is not None:
                self._on_object_state_change(self.owner, quality_state_value.state, quality_state_value, quality_state_value)
        self.spoilable_on_add()

    def on_remove(self, *_, **__):
        if self._servings_statistic_tracker_handle is not None:
            tracker = self.owner.get_tracker(CraftingTuning.SERVINGS_STATISTIC)
            if tracker.has_watcher(self._servings_statistic_tracker_handle):
                tracker.remove_watcher(self._servings_statistic_tracker_handle)
            self._servings_statistic_tracker_handle = None
        if self._quality_change_callback_added:
            self.owner.remove_state_changed_callback(self._on_object_state_change)
            self._quality_change_callback_added = False
        self.spoilable_on_remove()
        self._remove_hovertip()

    def on_mutated(self):
        self.object_mutated_listeners()
        self.object_mutated_listeners.clear()
        self.owner.remove_component(types.CRAFTING_COMPONENT)
        self.on_remove()

    @property
    def crafter_sim_id(self):
        if self._crafting_process.crafter_sim_id:
            return self._crafting_process.crafter_sim_id
        return 0

    def _on_servings_change(self, stat_type, old_value, new_value):
        if stat_type is CraftingTuning.SERVINGS_STATISTIC:
            owner = self.owner
            self.owner.update_tooltip_field((TooltipFieldsComplete.servings), (max(int(new_value), 0)), should_update=True)
            current_inventory = owner.get_inventory()
            if current_inventory is not None:
                current_inventory.push_inventory_item_update_msg(owner)
            if new_value <= 0:
                if old_value != new_value:
                    self.on_mutated()

    def _on_object_state_change(self, owner, state, old_value, new_value):
        self.spoilable_on_object_state_change(owner, state, old_value, new_value, CraftingTuning.QUALITY_STATE)
        if self.object_is_spoiled(owner):
            if self._crafting_process is not None:
                recipe = self._get_recipe()
                if recipe.show_spoiled_quality_description:
                    self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, CraftingTuning.SPOILED_STRING)
                self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0)
        elif owner.has_state(CraftingTuning.MASTERWORK_STATE):
            if owner.get_state(CraftingTuning.MASTERWORK_STATE) is CraftingTuning.MASTERWORK_STATE_VALUE:
                if self._crafting_process is not None:
                    recipe = self._get_recipe()
                    if recipe is not None:
                        if recipe.masterwork_name is not None:
                            self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, recipe.masterwork_name)
        if state is CraftingTuning.CONSUMABLE_STATE:
            value_consumable = CraftingTuning.CONSUMABLE_STATE_VALUE_MAP.get(new_value)
            if value_consumable is not None:
                self.owner.update_tooltip_field(TooltipFieldsComplete.percentage_left, value_consumable)
        if new_value is CraftingTuning.CONSUMABLE_EMPTY_STATE_VALUE:
            if old_value is not CraftingTuning.CONSUMABLE_EMPTY_STATE_VALUE:
                self._remove_hovertip()
        if new_value is CraftingTuning.LOCK_FRESHNESS_STATE_VALUE:
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0)
            if self._spoil_listener_handle is not None:
                spoil_tracker = self.owner.get_tracker(self._spoil_timer_state_value.state.linked_stat)
                spoil_tracker.remove_listener(self._spoil_listener_handle)
                self._spoil_listener_handle = None
        self.owner.update_object_tooltip()

    def _add_hovertip(self):
        if self._is_final_product:
            if self._is_finished():
                self._add_consumable_hovertip()

    def _is_finished(self):
        crafting_process = self._crafting_process
        tracker = None
        stat = CraftingTuning.PROGRESS_STATISTIC
        if crafting_process.current_ico is not None:
            tracker = crafting_process.current_ico.get_tracker(stat)
        if tracker is None:
            tracker = self.owner.get_tracker(stat)
        if not (tracker is None or tracker.has_statistic(stat)):
            tracker = crafting_process.get_tracker(stat)
        if tracker.has_statistic(stat):
            if tracker.get_value(stat) != stat.max_value:
                return crafting_process.is_complete
        return True

    def _get_recipe(self):
        recipe = self._crafting_process.recipe
        if self._use_base_recipe:
            recipe = recipe.get_base_recipe()
        return recipe

    def _add_consumable_hovertip(self):
        owner = self.owner
        owner.hover_tip = ui_protocols.UiObjectMetadata.HOVER_TIP_CONSUMABLE_CRAFTABLE
        crafting_process = self._crafting_process
        recipe = self._get_recipe()
        if recipe is None:
            return
            self.owner.update_tooltip_field(TooltipFieldsComplete.recipe_name, recipe.get_recipe_name(crafting_process.crafter))
            crafted_by_text = crafting_process.get_crafted_by_text(is_from_gallery=(self.owner.is_from_gallery))
            crafted_with_text = crafting_process.get_crafted_with_text()
            if crafted_by_text is not None:
                if crafted_with_text is not None:
                    crafted_by_text = LocalizationHelperTuning.NEW_LINE_LIST_STRUCTURE(crafted_by_text, crafted_with_text)
                crafter_sim_id = crafting_process.crafter_sim_id
                if crafter_sim_id is not None:
                    self.owner.update_tooltip_field(TooltipFieldsComplete.crafter_sim_id, crafter_sim_id)
        elif crafted_with_text is not None:
            crafted_by_text = crafted_with_text
        self.owner.update_tooltip_field(TooltipFieldsComplete.crafted_by_text, crafted_by_text)
        if owner.has_state(CraftingTuning.QUALITY_STATE):
            value_quality = CraftingTuning.QUALITY_STATE_VALUE_MAP.get(owner.get_state(CraftingTuning.QUALITY_STATE))
            if value_quality is not None:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality, value_quality.state_star_number)
        if owner.has_state(CraftingTuning.MASTERWORK_STATE):
            if owner.get_state(CraftingTuning.MASTERWORK_STATE) is CraftingTuning.MASTERWORK_STATE_VALUE:
                if recipe.masterwork_name is not None:
                    self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, recipe.masterwork_name)
        inscription = crafting_process.inscription
        if inscription is not None:
            self.owner.update_tooltip_field(TooltipFieldsComplete.inscription, inscription)
        self.spoilable_on_add_hovertip(recipe.spoil_time_commodity_override, recipe.time_until_spoiled_string_override)
        subtext = self.owner.get_state_strings()
        if subtext is not None:
            self.owner.update_tooltip_field(TooltipFieldsComplete.subtext, subtext)
        recipe.update_hovertip((self.owner), crafter=(crafting_process.crafter))
        current_inventory = owner.get_inventory()
        if current_inventory is not None:
            current_inventory.push_inventory_item_update_msg(owner)
        self.owner.update_object_tooltip()

    def update_simoleon_tooltip(self):
        self._crafting_process.apply_simoleon_value(self.owner)
        recipe = self._get_recipe()
        recipe.update_hovertip((self.owner), crafter=(self._crafting_process.crafter))
        self.owner.update_object_tooltip()

    def update_quality_tooltip(self):
        owner = self.owner
        recipe = self._get_recipe()
        if owner.has_state(CraftingTuning.QUALITY_STATE):
            value_quality = CraftingTuning.QUALITY_STATE_VALUE_MAP.get(owner.get_state(CraftingTuning.QUALITY_STATE))
            if value_quality is not None:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality, value_quality.state_star_number)
        if owner.has_state(CraftingTuning.MASTERWORK_STATE):
            quality_description = recipe.masterwork_name if owner.get_state(CraftingTuning.MASTERWORK_STATE) is CraftingTuning.MASTERWORK_STATE_VALUE else None
            if quality_description is not None:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, quality_description)

    def _remove_hovertip(self):
        owner = self.owner
        owner.hover_tip = ui_protocols.UiObjectMetadata.HOVER_TIP_DISABLED
        self.owner.update_tooltip_field(TooltipFieldsComplete.recipe_name, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.recipe_description, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.crafter_sim_id, 0)
        self.owner.update_tooltip_field(TooltipFieldsComplete.crafted_by_text, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.quality, 0)
        self.owner.update_tooltip_field(TooltipFieldsComplete.servings, 0)
        self.owner.update_tooltip_field(TooltipFieldsComplete.percentage_left, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.style_name, None)
        if self.owner.get_tooltip_field(TooltipFieldsComplete.simoleon_value) is not None:
            self.owner.update_tooltip_field(TooltipFieldsComplete.simoleon_value, owner.current_value)
        self.owner.update_tooltip_field(TooltipFieldsComplete.main_icon, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.sub_icons, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, None)
        self.owner.update_tooltip_field(TooltipFieldsComplete.subtext, None)
        self.spoilable_on_remove_hovertip()
        self.owner.update_object_tooltip()

    def _on_crafting_process_updated(self):
        if self._crafting_process.recipe is not None:
            self._add_hovertip()
            self.owner.update_component_commodity_flags()

    @componentmethod
    def set_crafting_process(self, crafting_process, use_base_recipe=False, is_final_product=False, from_load=False):
        if is_final_product and (from_load or self._crafting_process) is not None and crafting_process.multiple_order_process:
            new_process = crafting_process.copy_for_serve_interaction(crafting_process.get_order_or_recipe())
            self._crafting_process.linked_process = new_process
            self._crafting_process = new_process
        else:
            self._crafting_process = crafting_process
        self._use_base_recipe = use_base_recipe
        self._is_final_product = is_final_product
        self._on_crafting_process_updated()

    @componentmethod
    def get_crafting_process(self):
        return self._crafting_process

    @componentmethod
    def on_crafting_process_finished(self):
        self._add_hovertip()
        self.owner.update_component_commodity_flags()
        crafting_process = self._crafting_process
        if crafting_process is None:
            return
        crafting_process.clear_refundables()
        crafting_process.end_linked_situation()
        if crafting_process.current_ico is None:
            crafting_process.current_ico = self.owner
        recipe = crafting_process.recipe
        if self._use_base_recipe:
            recipe = recipe.get_base_recipe()
        skill_test = recipe.skill_test
        if crafting_process.crafter_sim_id is None:
            return
        sim_info = services.sim_info_manager().get(crafting_process.crafter_sim_id)
        if sim_info is not None:
            created_object_quality = self.owner.get_state(CraftingTuning.QUALITY_STATE) if self.owner.has_state(CraftingTuning.QUALITY_STATE) else None
            created_object_masterwork = self.owner.get_state(CraftingTuning.MASTERWORK_STATE) if self.owner.has_state(CraftingTuning.MASTERWORK_STATE) else None
            services.get_event_manager().process_event((test_events.TestEvent.ItemCrafted), sim_info=sim_info,
              crafted_object=(self.owner),
              skill=(skill_test.skill if skill_test is not None else None),
              quality=created_object_quality,
              masterwork=created_object_masterwork)

    @componentmethod
    def get_recipe(self):
        if self._crafting_process.recipe is None:
            return
        if self.owner.definition is not self._crafting_process.recipe.final_product.definition:
            for linked_recipe in self._crafting_process.recipe.linked_recipes_map.values():
                if self.owner.definition is linked_recipe.final_product.definition:
                    return linked_recipe

        return self._crafting_process.recipe

    @componentmethod
    def get_photo_definition(self):
        recipe = self.get_recipe()
        if recipe is None:
            return
        return recipe.photo_definition

    @componentmethod_with_fallback((lambda *_, **__: None))
    def get_craftable_property(self, property_type):
        recipe = self._get_recipe()
        crafting_process = self._crafting_process
        if crafting_process is None:
            return
        if property_type == GameObjectProperty.RECIPE_NAME:
            return recipe.get_recipe_name(crafting_process.crafter)
        if property_type == GameObjectProperty.RECIPE_DESCRIPTION:
            return recipe.recipe_description(crafting_process.crafter)
        logger.error(('Requested crafting property_type {} not found on game_object'.format(property_type)), owner='camilogarcia')

    @componentmethod
    def get_consume_affordance--- This code section failed: ---

 L. 435         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _is_final_product
                4  POP_JUMP_IF_TRUE     20  'to 20'

 L. 436         6  LOAD_GLOBAL              logger
                8  LOAD_METHOD              warn
               10  LOAD_STR                 "Attempting to get consume affordances for something that isn't final product."
               12  CALL_METHOD_1         1  '1 positional argument'
               14  POP_TOP          

 L. 437        16  LOAD_CONST               None
               18  RETURN_VALUE     
             20_0  COME_FROM             4  '4'

 L. 439        20  BUILD_MAP_0           0 
               22  STORE_FAST               'error_dict'

 L. 441        24  LOAD_FAST                'self'
               26  LOAD_ATTR                owner
               28  LOAD_ATTR                consumable_component
               30  STORE_FAST               'consumable_component'

 L. 442        32  LOAD_FAST                'consumable_component'
               34  LOAD_CONST               None
               36  COMPARE_OP               is-not
               38  POP_JUMP_IF_FALSE   126  'to 126'

 L. 445        40  LOAD_FAST                'context'
               42  LOAD_CONST               None
               44  COMPARE_OP               is-not
               46  POP_JUMP_IF_FALSE    98  'to 98'

 L. 446        48  SETUP_LOOP          126  'to 126'
               50  LOAD_FAST                'consumable_component'
               52  LOAD_ATTR                consume_affordances
               54  GET_ITER         
               56  FOR_ITER             94  'to 94'
               58  STORE_FAST               'consume_affordance'

 L. 447        60  LOAD_FAST                'consume_affordance'
               62  LOAD_ATTR                test
               64  LOAD_FAST                'self'
               66  LOAD_ATTR                owner
               68  LOAD_FAST                'context'
               70  LOAD_CONST               ('target', 'context')
               72  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               74  STORE_FAST               'result'

 L. 448        76  LOAD_FAST                'result'
               78  POP_JUMP_IF_FALSE    84  'to 84'

 L. 449        80  LOAD_FAST                'consume_affordance'
               82  RETURN_VALUE     
             84_0  COME_FROM            78  '78'

 L. 450        84  LOAD_FAST                'result'
               86  LOAD_FAST                'error_dict'
               88  LOAD_FAST                'consume_affordance'
               90  STORE_SUBSCR     
               92  JUMP_BACK            56  'to 56'
               94  POP_BLOCK        
               96  JUMP_FORWARD        126  'to 126'
             98_0  COME_FROM            46  '46'

 L. 453        98  LOAD_GLOBAL              next
              100  LOAD_GLOBAL              iter
              102  LOAD_FAST                'consumable_component'
              104  LOAD_ATTR                consume_affordances
              106  CALL_FUNCTION_1       1  '1 positional argument'
              108  LOAD_CONST               None
              110  CALL_FUNCTION_2       2  '2 positional arguments'
              112  STORE_FAST               'consume_affordance'

 L. 454       114  LOAD_FAST                'consume_affordance'
              116  LOAD_CONST               None
              118  COMPARE_OP               is-not
              120  POP_JUMP_IF_FALSE   126  'to 126'

 L. 455       122  LOAD_FAST                'consume_affordance'
              124  RETURN_VALUE     
            126_0  COME_FROM           120  '120'
            126_1  COME_FROM            96  '96'
            126_2  COME_FROM_LOOP       48  '48'
            126_3  COME_FROM            38  '38'

 L. 461       126  SETUP_LOOP          178  'to 178'
              128  LOAD_FAST                'self'
              130  LOAD_ATTR                owner
              132  LOAD_METHOD              super_affordances
              134  CALL_METHOD_0         0  '0 positional arguments'
              136  GET_ITER         
            138_0  COME_FROM           168  '168'
            138_1  COME_FROM           162  '162'
              138  FOR_ITER            176  'to 176'
              140  STORE_FAST               'affordance'

 L. 462       142  LOAD_CONST               0
              144  LOAD_CONST               ('GrabServingSuperInteraction',)
              146  IMPORT_NAME_ATTR         crafting.crafting_interactions
              148  IMPORT_FROM              GrabServingSuperInteraction
              150  STORE_FAST               'GrabServingSuperInteraction'
              152  POP_TOP          

 L. 463       154  LOAD_GLOBAL              issubclass
              156  LOAD_FAST                'affordance'
              158  LOAD_FAST                'GrabServingSuperInteraction'
              160  CALL_FUNCTION_2       2  '2 positional arguments'
              162  POP_JUMP_IF_FALSE   138  'to 138'

 L. 464       164  LOAD_FAST                'affordance'
              166  LOAD_ATTR                consume_affordances_override
              168  POP_JUMP_IF_TRUE    138  'to 138'

 L. 465       170  LOAD_FAST                'affordance'
              172  RETURN_VALUE     
              174  JUMP_BACK           138  'to 138'
              176  POP_BLOCK        
            178_0  COME_FROM_LOOP      126  '126'

 L. 466       178  LOAD_FAST                'error_dict'
              180  POP_JUMP_IF_FALSE   194  'to 194'

 L. 467       182  LOAD_GLOBAL              logger
              184  LOAD_METHOD              error
              186  LOAD_STR                 'Failed to find valid consume affordance. Consumable component affordances tested as follows:\n\n{}'
              188  LOAD_FAST                'error_dict'
              190  CALL_METHOD_2         2  '2 positional arguments'
              192  POP_TOP          
            194_0  COME_FROM           180  '180'

Parse error at or near `COME_FROM_LOOP' instruction at offset 126_2

    @componentmethod_with_fallback((lambda: None))
    def get_notebook_information(self, notebook_entry, notebook_sub_entries):
        recipe = self.get_recipe()
        if not recipe.use_ingredients:
            return
        sub_entries = (
         SubEntryData(recipe.guid64, False),)
        return (notebook_entry(None, sub_entries=sub_entries),)

    def _icon_override_gen(self):
        recipe = self.get_recipe()
        if recipe.icon_override is not None:
            yield recipe.icon_override

    @componentmethod
    def set_ready_to_serve(self):
        self._crafting_process.ready_to_serve = True

    def component_super_affordances_gen(self, **kwargs):
        recipe = self.get_recipe()
        if self._use_base_recipe:
            recipe = recipe.get_base_recipe()
        elif recipe is None:
            return
            if self._crafting_process.is_complete or self._crafting_process.ready_to_serve:
                for sa in recipe.final_product.super_affordances:
                    yield sa

                for linked_recipe in recipe.linked_recipes_map.values():
                    for sa in linked_recipe.final_product.super_affordances:
                        yield sa

            if recipe.resume_affordance:
                yield recipe.resume_affordance
        else:
            yield CraftingTuning.DEFAULT_RESUME_AFFORDANCE

    def component_interactable_gen(self):
        yield self

    def on_client_connect(self, client):
        if self._crafting_process.recipe is not None:
            self._add_hovertip()

    @componentmethod_with_fallback((lambda: False))
    def has_servings_statistic(self):
        tracker = self.owner.get_tracker(CraftingTuning.SERVINGS_STATISTIC)
        return tracker is None or tracker.has_statistic(CraftingTuning.SERVINGS_STATISTIC) or False
        return True

    def _on_households_loaded_update(self):
        self._add_hovertip()

    def get_recipe_effect_overrides(self, effect_name):
        if self._crafting_process.recipe is not None:
            if self._crafting_process.recipe:
                effect_override = self._crafting_process.recipe.vfx_overrides.get(effect_name)
                if effect_override is not None:
                    return effect_override
        return effect_name

    def component_anim_overrides_gen(self):
        if self._crafting_process.recipe is not None:
            if self._crafting_process.recipe.anim_overrides is not None:
                yield self._crafting_process.recipe.anim_overrides

    def save(self, persistence_master_message):
        logger.info('[PERSISTENCE]: ----Start saving crafting component of {0}.', self.owner)
        self.spoilable_pre_save()
        persistable_data = protocols.PersistenceMaster.PersistableData()
        persistable_data.type = protocols.PersistenceMaster.PersistableData.CraftingComponent
        crafting_save = persistable_data.Extensions[protocols.PersistableCraftingComponent.persistable_data]
        self._crafting_process.save(crafting_save.process)
        crafting_save.use_base_recipe = self._use_base_recipe
        crafting_save.is_final_product = self._is_final_product
        persistence_master_message.data.extend([persistable_data])

    def load(self, crafting_save_message):
        logger.info('[PERSISTENCE]: ----Start loading crafting component of {0}.', self.owner)
        crafting_component_data = crafting_save_message.Extensions[protocols.PersistableCraftingComponent.persistable_data]
        crafting_process = CraftingProcess()
        crafting_process.load(crafting_component_data.process)
        self.set_crafting_process(crafting_process, (crafting_component_data.use_base_recipe), (crafting_component_data.is_final_product), from_load=True)
        recipe = self.get_recipe()
        if recipe is not None:
            if crafting_process.crafted_value is not None:
                self.owner.base_value = crafting_process.crafted_value
            services.current_zone().register_callback(zone_types.ZoneState.HOUSEHOLDS_AND_SIM_INFOS_LOADED, self._on_households_loaded_update)
            self.owner.append_tags(recipe.apply_tags)
