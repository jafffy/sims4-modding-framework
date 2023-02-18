# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\part.py
# Compiled at: 2022-04-05 15:48:07
# Size of source mod 2**32: 41524 bytes

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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
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
binary_operator ::= BINARY_SUBTRACT . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
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
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
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
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= kvlist_0 . 
dict_comp_body ::= expr . expr MAP_ADD
dict_comp_body ::= expr expr . MAP_ADD
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
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
expr ::= dict . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr ::= subscript . 
expr ::= yield . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
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
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kwarg ::= LOAD_STR . expr
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_2
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR . LOAD_STR
load_genexpr ::= BUILD_TUPLE_1 LOAD_GENEXPR LOAD_STR . 
load_genexpr ::= LOAD_GENEXPR . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_2
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= genexpr_func . 
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
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
testexpr ::= testfalse . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
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
   
 L. 398       102  LOAD_FAST                'parts'
                 104  LOAD_FAST                'index'
                 106  LOAD_CONST               1
                 108  BINARY_ADD       
                 110  BINARY_SUBSCR    
                 112  YIELD_VALUE      
                 114  POP_TOP          
               116_0  COME_FROM           100  '100'
->             116_1  COME_FROM            48  '48'
from _weakrefset import WeakSet
from animation.animation_utils import AnimationOverrides
from animation.arb_element import ArbElement
from caches import cached
from event_testing.resolver import DoubleObjectResolver
from interactions.utils.routing import RouteTargetType
from native.animation import get_joint_transform_from_rig
from objects.components.slot_component import SlotComponent
from objects.proxy import ProxyObject
from objects.slots import RuntimeSlot
from postures.posture import TunablePostureTypeListSnippet
from reservation.reservation_mixin import ReservationMixin
from routing.portals.portal_data import TunablePortalReference
from sims4.callback_utils import CallableList
from sims4.hash_util import hash32
from sims4.math import Transform
from sims4.tuning.instances import TunedInstanceMetaclass
from sims4.tuning.tunable import TunableList, TunableReference, Tunable, TunableTuple, TunableSet, HasTunableReference, TunableEnumEntry, TunableVariant, HasTunableSingletonFactory, AutoFactoryInit
from sims4.tuning.tunable_hash import TunableStringHash32
from sims4.utils import Result, constproperty
from singletons import DEFAULT
from snippets import TunableAffordanceFilterSnippet
from traits.traits import Trait
from tunable_utils.tunable_white_black_list import TunableWhiteBlackList
import routing, services, sims4.callback_utils, sims4.log
logger = sims4.log.Logger('Parts')

def purge_cache():
    ObjectPart._bone_name_hashes_for_part_suffices = None


sims4.callback_utils.add_callbacks(sims4.callback_utils.CallbackEvent.TUNING_CODE_RELOAD, purge_cache)

class _OverrideSurfaceType(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'override_surface_type': TunableEnumEntry(description="\n            The override for the surface type. If used, part owner's \n            surface type will be ignored.\n            ",
                                tunable_type=(routing.SurfaceType),
                                default=(routing.SurfaceType.SURFACETYPE_WORLD))}

    def get_surface_type(self, part, **kwargs):
        return self.override_surface_type


class _PartOwnerSurfaceType(HasTunableSingletonFactory, AutoFactoryInit):

    def get_surface_type(self, part, transform=None):
        owner = part.part_owner
        if owner.routing_surface is None:
            return
        return owner.routing_surface.type


class Part(ProxyObject, ReservationMixin):
    _unproxied_attributes = ProxyObject._unproxied_attributes | {
     "'_data'", "'_reservation_handlers'", "'_joint_transform'", "'_routing_context'", 
     "'_children_cache'", 
     "'_is_surface'", "'_parts'", "'_part_location'", 
     "'_containment_slot_info_cache'", "'_disabling_states'", 
     "'get_locations_for_posture'", 
     "'get_position_and_routing_surface_for_posture'", 
     "'_cached_locations_for_posture'", 
     "'_cached_position_and_routing_surface_for_posture'", 
     "'_on_children_changed_callbacks'"}

    def __init__(self, owner, data):
        super().__init__(owner)
        self._data = data
        self._reservation_handlers = ()
        self._joint_transform = None
        self._routing_context = None
        self._children_cache = None
        self._containment_slot_info_cache = None
        self._part_location = None
        self._is_surface = {}
        self._disabling_states = None
        self._cached_locations_for_posture = None
        self._cached_position_and_routing_surface_for_posture = None
        self.mark_get_locations_for_posture_needs_update()
        self._on_children_changed_callbacks = None

    def __repr__(self):
        return '<part {0} on {1}>'.format(self.part_group_index, self.part_owner)

    def __str__(self):
        return '{}[{}]'.format(self.part_owner, self.part_group_index)

    @constproperty
    def is_part():
        return True

    @property
    def parts(self):
        pass

    @property
    def _parts(self):
        raise AttributeError()

    @property
    def part_owner(self):
        return self._proxied_obj

    @property
    def part_group_index(self):
        return self.part_owner.parts.index(self)

    @property
    def part_definition(self):
        return self._data.part_definition

    @property
    def part_identifier(self):
        part_identifier = getattr(self._data, 'part_data_key', self.part_group_index)
        return part_identifier

    @property
    def disable_sim_aop_forwarding(self):
        return self._data.disable_sim_aop_forwarding

    @property
    def disable_child_aop_forwarding(self):
        return self._data.disable_child_aop_forwarding

    @property
    def restrict_autonomy_preference(self):
        return self._data.restrict_autonomy_preference

    @property
    def disabling_states(self):
        return self._data.disabling_states

    @property
    def part_name(self):
        return self._data.name

    @property
    def posture_transition_target_tag(self):
        if self._data.posture_transition_target_tag is None:
            return self.part_owner.posture_transition_target_tag
        return self._data.posture_transition_target_tag

    @property
    def forward_direction_for_picking(self):
        offset = self._data.forward_direction_for_picking
        return sims4.math.Vector3(offset.x, 0, offset.y)

    @property
    def transform(self):
        return self._part_location.world_transform

    @transform.setter
    def transform(self):
        raise AttributeError("A part's Transform should never be set by hand. Only the part owner's transform should be set.")

    def add_disabling_state(self, state):
        if not self._disabling_states:
            self._disabling_states = set()
        self._disabling_states.add(state)

    @property
    def additional_part_posture_cost(self):
        if self._data is None or self._data.is_old_part_data:
            return 0
        return self._data.additional_part_posture_cost

    @property
    def current_body_target_cost_bonus(self):
        if self._data is None or self._data.is_old_part_data:
            return 0
        return self._data.current_body_target_cost_bonus

    def remove_disabling_state(self, state):
        self._disabling_states.remove(state)

    def get_joint_transform(self):
        if self._joint_transform is None:
            target_root_joint = self.is_base_part or ArbElement._BASE_SUBROOT_STRING + str(self.subroot_index)
            try:
                self._joint_transform = get_joint_transform_from_rig(self.rig, target_root_joint)
            except KeyError:
                raise KeyError('Unable to find joint {} on {}'.format(target_root_joint, self))
            except ValueError:
                raise ValueError('Unable to find rig for joint {} on {}'.format(self.rig, self))

        else:
            self._joint_transform = Transform.IDENTITY()
        return self._joint_transform

    def get_joint_transform_for_joint(self, joint_name):
        if isinstance(joint_name, str):
            joint_name = joint_name + str(self.subroot_index)
        else:
            joint_name = hash32((str(self.subroot_index)), initial_hash=joint_name)
        transform = get_joint_transform_from_rig(self.rig, joint_name)
        transform = Transform.concatenate(transform, self.part_owner.transform)
        return transform

    @property
    def location(self):
        return self._part_location

    @property
    def routing_surface(self):
        return self._part_location.world_routing_surface

    def is_routing_surface_overlapped_at_position(self, position):
        return self.part_owner.is_routing_surface_overlapped_at_position(position)

    @property
    def provided_routing_surface(self):
        return self.part_owner.provided_routing_surface

    def on_children_changed(self):
        self._children_cache = None

    def _add_child(self, child, location):
        self.part_owner._add_child(child, location)
        self.on_children_changed()
        if self._on_children_changed_callbacks is None:
            return
        self._on_children_changed_callbacks(child, location=location)

    def _remove_child(self, child, new_parent=None):
        self.part_owner._remove_child(child, new_parent=new_parent)
        self.on_children_changed()
        if self._on_children_changed_callbacks is None:
            return
        self._on_children_changed_callbacks(child, new_parent=new_parent)

    @property
    def children(self):
        if self._children_cache is None:
            self._children_cache = WeakSet()
            for child in self.part_owner.children:
                if self.has_slot(child.location.slot_hash or child.location.joint_name_hash):
                    self._children_cache.add(child)

        return self._children_cache

    @property
    def routing_context(self):
        return self.part_owner.routing_context

    @property
    def supported_posture_types(self):
        return self.part_definition.supported_posture_types

    @property
    def _anim_overrides_internal(self):
        params = {}
        if any((p.in_use for p in self.part_owner.parts if p is not self if p.part_definition is self.part_definition)):
            params['otherSimPresent'] = True
        overrides = super()._anim_overrides_internal
        if self._data.anim_overrides:
            overrides = overrides(self._data.anim_overrides())
        return AnimationOverrides(overrides=overrides, params=params)

    @property
    def can_reset(self):
        return False

    def reset(self, reset_reason):
        super().reset(reset_reason)
        self.part_owner.reset(reset_reason)

    def adjacent_parts_gen--- This code section failed: ---

 L. 387         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _data
                4  LOAD_ATTR                adjacent_parts
                6  LOAD_CONST               None
                8  COMPARE_OP               is-not
               10  POP_JUMP_IF_FALSE    50  'to 50'

 L. 388        12  LOAD_FAST                'self'
               14  LOAD_ATTR                part_owner
               16  LOAD_ATTR                parts
               18  STORE_FAST               'parts'

 L. 389        20  SETUP_LOOP          116  'to 116'
               22  LOAD_FAST                'self'
               24  LOAD_ATTR                _data
               26  LOAD_ATTR                adjacent_parts
               28  GET_ITER         
               30  FOR_ITER             46  'to 46'
               32  STORE_FAST               'adjacent_part_index'

 L. 390        34  LOAD_FAST                'parts'
               36  LOAD_FAST                'adjacent_part_index'
               38  BINARY_SUBSCR    
               40  YIELD_VALUE      
               42  POP_TOP          
               44  JUMP_BACK            30  'to 30'
               46  POP_BLOCK        
               48  JUMP_FORWARD        116  'to 116'
             50_0  COME_FROM            10  '10'

 L. 392        50  LOAD_FAST                'self'
               52  LOAD_ATTR                part_group_index
               54  STORE_FAST               'index'

 L. 393        56  LOAD_FAST                'self'
               58  LOAD_ATTR                part_owner
               60  LOAD_ATTR                parts
               62  STORE_FAST               'parts'

 L. 395        64  LOAD_FAST                'index'
               66  LOAD_CONST               0
               68  COMPARE_OP               >
               70  POP_JUMP_IF_FALSE    86  'to 86'

 L. 396        72  LOAD_FAST                'parts'
               74  LOAD_FAST                'index'
               76  LOAD_CONST               1
               78  BINARY_SUBTRACT  
               80  BINARY_SUBSCR    
               82  YIELD_VALUE      
               84  POP_TOP          
             86_0  COME_FROM            70  '70'

 L. 397        86  LOAD_FAST                'index'
               88  LOAD_CONST               1
               90  BINARY_ADD       
               92  LOAD_GLOBAL              len
               94  LOAD_FAST                'parts'
               96  CALL_FUNCTION_1       1  '1 positional argument'
               98  COMPARE_OP               <
              100  POP_JUMP_IF_FALSE   116  'to 116'

 L. 398       102  LOAD_FAST                'parts'
              104  LOAD_FAST                'index'
              106  LOAD_CONST               1
              108  BINARY_ADD       
              110  BINARY_SUBSCR    
              112  YIELD_VALUE      
              114  POP_TOP          
            116_0  COME_FROM           100  '100'
            116_1  COME_FROM            48  '48'
            116_2  COME_FROM_LOOP       20  '20'

Parse error at or near `COME_FROM' instruction at offset 116_1

    def has_adjacent_part(self, sim):
        for part in self.adjacent_parts_gen():
            if part.may_reserve(sim):
                return True

        return False

    def may_reserve(self, sim, *args, check_overlapping_parts=True, **kwargs):
        if check_overlapping_parts:
            for overlapping_part in self.get_overlapping_parts():
                if overlapping_part is self:
                    continue
                reserve_result = overlapping_part.may_reserve(sim, check_overlapping_parts=False)
                if not reserve_result:
                    return reserve_result

        return (super().may_reserve)(sim, *args, **kwargs)

    def is_mirrored(self, part=None):
        if part is None:
            return self._data.is_mirrored
        offset = part.position - self.position
        return sims4.math.vector_cross_2d(self.forward, offset) < 0

    @property
    def route_target(self):
        return (RouteTargetType.PARTS, (self,))

    @property
    def is_base_part(self):
        return self.subroot_index is None

    @property
    def subroot_index(self):
        if self._data is None:
            return
        return self._data.subroot_index

    @property
    def part_suffix(self) -> str:
        subroot_index = self.subroot_index
        if subroot_index is not None:
            return str(subroot_index)

    @cached(key=(lambda p, a: (p.part_definition, a.affordance)))
    def supports_affordance(self, affordance_or_aop):
        affordance = affordance_or_aop.affordance
        supported_affordance_data = self.part_definition.supported_affordance_data
        if not affordance.is_super:
            if not supported_affordance_data.consider_mixers:
                return True
        return supported_affordance_data.compatibility(affordance, allow_ignore_exclude_all=True)

    def get_ignored_objects_for_line_of_sight(self):
        return self.part_owner.get_ignored_objects_for_line_of_sight()

    def _get_location_for_posture_internal(self):
        return self._part_location.world_transform.translation

    def _get_cached_locations_for_posture(self, node):
        return self._cached_locations_for_posture

    def _cache_and_return_locations_for_posture(self, node):
        self.get_locations_for_posture = self._get_cached_locations_for_posture
        self._cached_locations_for_posture = (
         routing.Location((self._get_location_for_posture_internal()),
           orientation=(self.orientation),
           routing_surface=(self.routing_surface)),)
        return self._cached_locations_for_posture

    def _get_position_and_routing_surface_for_posture_internal(self):
        position = self._get_location_for_posture_internal()
        routing_surface = self.routing_surface
        position_and_routing_surface_for_posture = [
         (
          position, routing_surface)]
        if routing_surface.type == routing.SurfaceType.SURFACETYPE_OBJECT:
            world_routing_surface = routing.SurfaceIdentifier(routing_surface.primary_id, routing_surface.secondary_id, routing.SurfaceType.SURFACETYPE_WORLD)
            position_and_routing_surface_for_posture.append((position, world_routing_surface))
        return position_and_routing_surface_for_posture

    def _get_cached_position_and_routing_surface_for_posture(self, node):
        return self._cached_position_and_routing_surface_for_posture

    def _cache_and_return_position_and_routing_surface_for_posture(self, node):
        self.get_position_and_routing_surface_for_posture = self._get_cached_position_and_routing_surface_for_posture
        self._cached_position_and_routing_surface_for_posture = self._get_position_and_routing_surface_for_posture_internal()
        return self._cached_position_and_routing_surface_for_posture

    def mark_get_locations_for_posture_needs_update(self):
        self.get_locations_for_posture = self._cache_and_return_locations_for_posture
        self.get_position_and_routing_surface_for_posture = self._cache_and_return_position_and_routing_surface_for_posture

    @cached(maxsize=512, key=(lambda p, posture_type, *_, is_specific=True, **__: (p.part_definition, posture_type, is_specific)))
    def supports_posture_type(self, posture_type, *_, is_specific=True, **__):
        if posture_type is None:
            return True
        else:
            part_supported_posture_types = {posture.posture_type for posture in self.part_definition.supported_posture_types}
            return part_supported_posture_types or True
        if is_specific:
            return posture_type in part_supported_posture_types
        return any((posture_type.family_name == supported_posture.family_name for supported_posture in part_supported_posture_types if supported_posture is not None))

    def _supports_sim_buffs(self, sim):
        return not any((sim.has_buff(blacklisted_buff) for blacklisted_buff in self.part_definition.blacklisted_buffs))

    def _meets_trait_requirements(self, sim):
        if self.part_definition.trait_requirements is None:
            return True
        traits = sim.sim_info.get_traits()
        return self.part_definition.trait_requirements.test_collection(traits)

    def is_disabled(self):
        if self._disabling_states:
            return True
        if self._state_index in self._data.disabling_model_suite_indices:
            return True
        return False

    def supports_posture_spec(self, posture_spec, interaction=None, sim=None):
        if self.is_disabled():
            return False
        elif interaction is not None:
            if interaction.is_super:
                affordance = interaction.affordance
                if affordance.requires_target_support:
                    if not self.supports_affordance(affordance):
                        return False
                else:
                    is_sim_putdown = interaction.is_putdown and interaction.carry_target is not None and interaction.carry_target.is_sim
                    test_sim = sim or interaction.sim
                    if not is_sim_putdown or interaction.carry_target is test_sim:
                        if not self._supports_sim_buffs(test_sim):
                            return False
                if not self._meets_trait_requirements(test_sim):
                    return False
        part_supported_posture_types = None
        if self.part_definition:
            part_supported_posture_types = self.part_definition.supported_posture_types
        body_posture = posture_spec.body
        if not part_supported_posture_types or body_posture is None:
            return True
        body_posture_type = body_posture.posture_type
        for supported_posture_info in part_supported_posture_types:
            if body_posture_type is supported_posture_info.posture_type:
                if self.affordancetuning_component is not None:
                    if sim is not None:
                        posture_providing_interactions = [affordance for affordance in self.super_affordances() if affordance.provided_posture_type is body_posture_type]
                        for interaction in posture_providing_interactions:
                            tests = self.affordancetuning_component.get_affordance_tests(interaction)
                            if tests is not None:
                                return tests.run_tests(DoubleObjectResolver(sim, self.part_owner)) or False

                return True

        return False

    @property
    def _bone_name_hashes(self):
        result = self.part_definition.get_bone_name_hashes_for_part_suffix(self.part_suffix)
        if self.part_owner.slot_component is not None:
            result |= self.get_deco_slot_hashes((self.part_owner.rig, (self.subroot_index, self.part_definition)))
        return result

    def get_provided_slot_types(self):
        return self.part_owner.get_provided_slot_types(part=self)

    def get_runtime_slots_gen(self, slot_types=None, bone_name_hash=None, owner_only=False):
        for slot_hash, slot_slot_types in self.get_containment_slot_infos():
            if slot_types is not None:
                if not slot_types.intersection(slot_slot_types):
                    continue
                elif bone_name_hash is not None and slot_hash != bone_name_hash:
                    continue
                if self.has_slot(slot_hash):
                    yield RuntimeSlot(self, slot_hash, slot_slot_types)

    def slot_object(self, parent_slot=None, slotting_object=None, objects_to_ignore=None):
        return self.part_owner.slot_object(parent_slot=parent_slot, slotting_object=slotting_object,
          target=self,
          objects_to_ignore=objects_to_ignore)

    def get_containment_slot_infos(self):
        if self._containment_slot_info_cache is None:
            owner = self.part_owner
            object_slots = owner.slots_resource
            if object_slots is None:
                self._containment_slot_info_cache = ()
            else:
                result = SlotComponent.get_containment_slot_infos_static(object_slots, owner.rig, owner)
                bone_name_hashes = self._bone_name_hashes
                self._containment_slot_info_cache = tuple(((slot_hash, slot_types) for slot_hash, slot_types in result if slot_hash in bone_name_hashes))
        return self._containment_slot_info_cache

    def is_valid_for_placement(self, *, obj=DEFAULT, definition=DEFAULT, objects_to_ignore=DEFAULT):
        result = Result.NO_RUNTIME_SLOTS
        for runtime_slot in self.get_runtime_slots_gen():
            result = runtime_slot.is_valid_for_placement(obj=obj, definition=definition, objects_to_ignore=objects_to_ignore)
            if result:
                break

        return result

    def has_slot(self, slot_hash):
        if slot_hash in self.part_definition.get_bone_name_hashes_for_part_suffix(self.part_suffix):
            return True
        if slot_hash in self.get_deco_slot_hashes((self.part_owner.rig, (self.subroot_index, self.part_definition))):
            return True
        return False

    def get_overlapping_parts(self):
        if self._data.overlapping_parts is None:
            return []
        parts = self.part_owner.parts
        return [parts[overlapping_part_index] for overlapping_part_index in self._data.overlapping_parts]

    @property
    def footprint(self):
        return self.part_owner.footprint

    @property
    def footprint_polygon(self):
        return self.part_owner.footprint_polygon

    def on_leaf_child_changed(self):
        self.part_owner.on_leaf_child_changed()

    def on_owner_location_changed(self):
        owner = self.part_owner
        if owner.parent is None:
            owner_transform = owner.transform
        else:
            owner_transform = owner.location.transform
        if self.subroot_index is None:
            transform = owner_transform
        else:
            transform = Transform.concatenate(self.get_joint_transform(), owner_transform)
        routing_surface = None
        surface_type = self.part_definition.part_surface.get_surface_type(self, transform=transform)
        if surface_type is not None:
            routing_surface = routing.SurfaceIdentifier(owner.zone_id, owner.level, surface_type)
        self._part_location = owner.location.clone(transform=transform, routing_surface=routing_surface)
        self.mark_get_locations_for_posture_needs_update()
        for child in self.children:
            if child.parts:
                for part in child.parts:
                    part.on_owner_location_changed()

    def _register_on_part_children_changed_callback(self, callback):
        if self._on_children_changed_callbacks is None:
            self._on_children_changed_callbacks = CallableList()
        if callback not in self._on_children_changed_callbacks:
            self._on_children_changed_callbacks.append(callback)

    def _unregister_on_part_children_changed_callback(self, callback):
        if self._on_children_changed_callbacks is not None:
            if callback in self._on_children_changed_callbacks:
                self._on_children_changed_callbacks.remove(callback)
            if not self._on_children_changed_callbacks:
                self._on_children_changed_callbacks = None


class ObjectPart(HasTunableReference, metaclass=TunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.OBJECT_PART)):
    INSTANCE_TUNABLES = {'supported_posture_types':TunablePostureTypeListSnippet(description='\n            The postures supported by this part. If empty, assumes all postures\n            are supported.\n            '), 
     'supported_affordance_data':TunableTuple(description='\n            Define affordance compatibility for this part.\n            ',
       compatibility=TunableAffordanceFilterSnippet(description='\n                Affordances supported by the part\n                '),
       consider_mixers=Tunable(description='\n                If checked, mixers are filtered through this compatibility\n                check. If unchecked, all mixers are assumed to be valid to run\n                on this part.\n                ',
       tunable_type=bool,
       default=False)), 
     'blacklisted_buffs':TunableList(description='\n            A list of buffs that will disable this part as a candidate to run an\n            interaction.\n            ',
       tunable=TunableReference(description='\n               Reference to a buff to disable the part.\n               ',
       manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
       pack_safe=True)), 
     'trait_requirements':TunableWhiteBlackList(description='\n            Trait blacklist and whitelist requirements to pick this part.\n            ',
       tunable=Trait.TunableReference(description='\n               Reference to the trait white/blacklists.\n               ',
       pack_safe=True)), 
     'subroot':TunableReference(description='\n            The reference of the subroot definition in the part.\n            ',
       manager=services.get_instance_manager(sims4.resources.Types.SUBROOT),
       allow_none=True), 
     'portal_data':TunableSet(description='\n            If the object owning this part has a portal component tuned, the\n            specified portals will be created for each part of this type. The\n            root position of the part is the subroot position.\n            ',
       tunable=TunablePortalReference(pack_safe=True)), 
     'can_pick':Tunable(description='\n            If checked, this part can be picked (selected as target when\n            clicking on object.)  If unchecked, cannot be picked.\n            ',
       tunable_type=bool,
       default=True), 
     'part_surface':TunableVariant(description='\n            The rules to determine the surface type for this object.\n            ',
       part_owner=_PartOwnerSurfaceType.TunableFactory(),
       override_surface=_OverrideSurfaceType.TunableFactory(),
       default='part_owner')}
    _bone_name_hashes_for_part_suffices = None

    @classmethod
    def register_tuned_animation(cls, *_, **__):
        pass

    @classmethod
    def add_auto_constraint(cls, participant_type, tuned_constraint, **kwargs):
        pass

    @classmethod
    def get_bone_name_hashes_for_part_suffix(cls, part_suffix):
        if cls._bone_name_hashes_for_part_suffices is None:
            cls._bone_name_hashes_for_part_suffices = {}
        if part_suffix in cls._bone_name_hashes_for_part_suffices:
            return cls._bone_name_hashes_for_part_suffices[part_suffix]
        bone_name_hashes = set()
        if cls.subroot is not None:
            for bone_name_hash in cls.subroot.bone_names:
                if part_suffix is not None:
                    bone_name_hash = hash32((str(part_suffix)), initial_hash=bone_name_hash)
                bone_name_hashes.add(bone_name_hash)

        cls._bone_name_hashes_for_part_suffices[part_suffix] = frozenset(bone_name_hashes)
        return cls._bone_name_hashes_for_part_suffices[part_suffix]


class Subroot(metaclass=TunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.SUBROOT)):
    INSTANCE_TUNABLES = {'bone_names': TunableSet(description='\n            The list of bone names that make up this subroot. Use this to\n            specify containment slots for the given part.\n            \n            If the part specifies a subroot, the bone name will be automatically\n            postfixed with the subroot index.\n            \n            For example, for part subroot 1:\n                _ctnm_eat_ -> _ctnm_eat_1\n            ',
                     tunable=TunableStringHash32(default='_ctnm_XXX_'),
                     minlength=1)}
