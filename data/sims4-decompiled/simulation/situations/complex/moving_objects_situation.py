# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\complex\moving_objects_situation.py
# Compiled at: 2018-04-19 20:36:23
# Size of source mod 2**32: 13438 bytes

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
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
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
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_9
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= _lambda_body . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= list . 
expr ::= listcomp . 
expr ::= or . 
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
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
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
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
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
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
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
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg . load_closure load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg . load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
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
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9 . 
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_10
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= pos_arg . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list_comp ::= BUILD_LIST_0 . list_iter
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
listcomp ::= load_closure LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
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
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr BUILD_TUPLE_1 . 
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
   
 L. 329       172  LOAD_FAST                'moves'
                 174  LOAD_METHOD              append
                 176  LOAD_FAST                'object_to_move'
                 178  BUILD_TUPLE_1         1 
                 180  LOAD_CLOSURE             'chosen_strategy'
                 182  LOAD_CLOSURE             'resolver'
                 184  BUILD_TUPLE_2         2 
                 186  LOAD_LAMBDA              '<code_object <lambda>>'
                 188  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<lambda>'
->               190  MAKE_FUNCTION_9          'default, closure'
                 192  CALL_METHOD_1         1  '1 positional argument'
                 194  POP_TOP          
from _sims4_collections import frozendict
from element_utils import build_element, CleanupType
from elements import SoftSleepElement
from event_testing.resolver import GlobalResolver, SingleSimResolver, SingleActorAndObjectResolver
from event_testing.tests import TunableTestSet
from interactions import ParticipantType
from interactions.interaction_finisher import FinishingType
from objects.object_creation import ObjectCreationOp
from objects.placement.placement_helper import _PlacementStrategyLocation
from sims4 import random
from sims4.resources import Types
from sims4.tuning.tunable import TunableList, TunableTuple, TunableSimMinute, TunableSet, OptionalTunable, TunableReference
from sims4.tuning.tunable_base import GroupNames
from situations.situation import Situation
from situations.situation_complex import SituationComplexCommon, CommonSituationState, SituationStateData
from tag import TunableTags
from tunable_multiplier import TunableMultiplier
from vfx import PlayEffect
import clock, services

class _PreparationState(CommonSituationState):
    FACTORY_TUNABLES = {'creation_ops':TunableList(tunable=ObjectCreationOp.TunableFactory(description='\n                The operation that will create the objects.\n                ',
       locked_args={'destroy_on_placement_failure': True})), 
     'locked_args':{'job_and_role_changes':frozendict(), 
      'allow_join_situation':False, 
      'time_out':None}}

    def __init__(self, *args, creation_ops=(), **kwargs):
        (super().__init__)(*args, **kwargs)
        self.creation_ops = creation_ops

    def on_activate(self, reader=None):
        super().on_activate(reader=reader)
        resolver = self.owner._get_placement_resolver()
        for operation in self.creation_ops:
            operation.apply_to_resolver(resolver)

        self.owner.on_objects_ready()


class _WaitingToMoveState(CommonSituationState):
    FACTORY_TUNABLES = {'locked_args': {'job_and_role_changes':frozendict(), 
                     'allow_join_situation':False}}

    def timer_expired(self):
        self.owner.on_ready_to_move()


OBJECT_TOKEN = 'object_id'

class MovingObjectsSituation(SituationComplexCommon):
    INSTANCE_TUNABLES = {'_preparation_state':_PreparationState.TunableFactory(tuning_group=GroupNames.STATE), 
     '_waiting_to_move_state':_WaitingToMoveState.TunableFactory(tuning_group=GroupNames.STATE), 
     '_tests_to_continue':TunableTestSet(description='\n            A list of tests that must pass in order to continue the situation\n            after the tuned duration for the waiting state has elapsed.\n            ',
       tuning_group=GroupNames.STATE), 
     'starting_requirements':TunableTestSet(description='\n            A list of tests that must pass in order for the situation\n            to start.\n            ',
       tuning_group=GroupNames.SITUATION), 
     'object_tags':TunableTags(description='\n            Tags used to find objects which will move about.\n            ',
       tuning_group=GroupNames.SITUATION), 
     'placement_strategy_locations':TunableList(description='\n            A list of weighted location strategies.\n            ',
       tunable=TunableTuple(weight=TunableMultiplier.TunableFactory(description='\n                    The weight of this strategy relative to other locations.\n                    '),
       placement_strategy=_PlacementStrategyLocation.TunableFactory(description='\n                    The placement strategy for the object.\n                    ')),
       minlength=1,
       tuning_group=GroupNames.SITUATION), 
     'fade':OptionalTunable(description='\n            If enabled, the objects will fade-in/fade-out as opposed to\n            immediately moving to their location.\n            ',
       tunable=TunableTuple(out_time=TunableSimMinute(description='\n                    Time over which the time will fade out.\n                    ',
       default=1),
       in_time=TunableSimMinute(description='\n                    Time over which the time will fade in.\n                    ',
       default=1)),
       enabled_by_default=True,
       tuning_group=GroupNames.SITUATION), 
     'vfx_on_move':OptionalTunable(description='\n            If tuned, apply this one-shot vfx on the moving object when it\n            is about to move.\n            ',
       tunable=PlayEffect.TunableFactory(),
       tuning_group=GroupNames.SITUATION), 
     'situation_end_loots_to_apply_on_objects':TunableSet(description='\n            The loots to apply on the tagged objects when the situation ends \n            or is destroyed.\n            \n            E.g. use this to reset objects to a specific state after \n            the situation is over.\n            \n            The loot will be processed with the active sim as the actor,\n            and the object as the target.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(Types.ACTION)),
       pack_safe=True),
       tuning_group=GroupNames.SITUATION)}
    REMOVE_INSTANCE_TUNABLES = Situation.NON_USER_FACING_REMOVE_INSTANCE_TUNABLES

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        reader = self._seed.custom_init_params_reader
        if reader is None:
            self._target_id = self._seed.extra_kwargs.get('default_target_id', None)
        else:
            self._target_id = reader.read_uint64(OBJECT_TOKEN, None)

    @classmethod
    def _states(cls):
        return (
         SituationStateData(0, _PreparationState, factory=(cls._preparation_state)),
         SituationStateData(1, _WaitingToMoveState, factory=(cls._waiting_to_move_state)))

    @classmethod
    def default_job(cls):
        pass

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return []

    @classmethod
    def situation_meets_starting_requirements(cls, **kwargs):
        if not cls.starting_requirements:
            return True
        else:
            resolver = SingleSimResolver(services.active_sim_info())
            return cls.starting_requirements.run_tests(resolver) or False
        return True

    def _save_custom_situation(self, writer):
        super()._save_custom_situation(writer)
        if self._target_id is not None:
            writer.write_uint64(OBJECT_TOKEN, self._target_id)

    def start_situation(self):
        super().start_situation()
        self._change_state(self._preparation_state())

    def load_situation(self):
        if not self.situation_meets_starting_requirements():
            return False
        return super().load_situation()

    def on_objects_ready(self):
        self._change_state(self._waiting_to_move_state())

    def on_ready_to_move(self):
        if self._tests_to_continue.run_tests(GlobalResolver()):
            self._move_objects()
            self._change_state(self._waiting_to_move_state())
        else:
            self._self_destruct()

    def _get_placement_resolver(self):
        additional_participants = {}
        if self._target_id is not None:
            target = services.object_manager().get(self._target_id)
            additional_participants[ParticipantType.Object] = (
             target,)
            if target is not None:
                if target.is_sim:
                    additional_participants[ParticipantType.TargetSim] = (
                     target.sim_info,)
        return SingleSimResolver((services.active_sim_info()), additional_participants=additional_participants)

    def _destroy(self):
        objects_of_interest = services.object_manager().get_objects_matching_tags((self.object_tags), match_any=True)
        if not objects_of_interest:
            return
        active_sim_info = services.active_sim_info()
        for obj in objects_of_interest:
            resolver = SingleActorAndObjectResolver(active_sim_info, obj, self)
            for loot in self.situation_end_loots_to_apply_on_objects:
                loot.apply_to_resolver(resolver)

        super()._destroy()

    def _move_objects--- This code section failed: ---

 L. 303         0  LOAD_GLOBAL              services
                2  LOAD_METHOD              object_manager
                4  CALL_METHOD_0         0  '0 positional arguments'
                6  LOAD_ATTR                get_objects_matching_tags
                8  LOAD_DEREF               'self'
               10  LOAD_ATTR                object_tags
               12  LOAD_CONST               True
               14  LOAD_CONST               ('match_any',)
               16  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               18  STORE_FAST               'objects_to_move'

 L. 304        20  LOAD_FAST                'objects_to_move'
               22  POP_JUMP_IF_TRUE     28  'to 28'

 L. 305        24  LOAD_CONST               None
               26  RETURN_VALUE     
             28_0  COME_FROM            22  '22'

 L. 307        28  LOAD_DEREF               'self'
               30  LOAD_METHOD              _get_placement_resolver
               32  CALL_METHOD_0         0  '0 positional arguments'
               34  STORE_DEREF              'resolver'

 L. 308        36  LOAD_CLOSURE             'resolver'
               38  BUILD_TUPLE_1         1 
               40  LOAD_LISTCOMP            '<code_object <listcomp>>'
               42  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<listcomp>'
               44  MAKE_FUNCTION_8          'closure'
               46  LOAD_DEREF               'self'
               48  LOAD_ATTR                placement_strategy_locations
               50  GET_ITER         
               52  CALL_FUNCTION_1       1  '1 positional argument'
               54  STORE_FAST               'choices'

 L. 309        56  LOAD_GLOBAL              random
               58  LOAD_METHOD              weighted_random_item
               60  LOAD_FAST                'choices'
               62  CALL_METHOD_1         1  '1 positional argument'
               64  STORE_DEREF              'chosen_strategy'

 L. 311        66  LOAD_DEREF               'self'
               68  LOAD_ATTR                fade
               70  LOAD_CONST               None
               72  COMPARE_OP               is-not
               74  STORE_FAST               'do_fade'

 L. 313        76  BUILD_LIST_0          0 
               78  STORE_FAST               'out_sequence'

 L. 314        80  BUILD_LIST_0          0 
               82  STORE_FAST               'moves'

 L. 315        84  BUILD_LIST_0          0 
               86  STORE_FAST               'in_sequence'

 L. 318        88  SETUP_LOOP          226  'to 226'
               90  LOAD_FAST                'objects_to_move'
               92  GET_ITER         
             94_0  COME_FROM           198  '198'
               94  FOR_ITER            224  'to 224'
               96  STORE_FAST               'object_to_move'

 L. 321        98  LOAD_FAST                'object_to_move'
              100  LOAD_ATTR                cancel_interactions_running_on_object
              102  LOAD_GLOBAL              FinishingType
              104  LOAD_ATTR                OBJECT_CHANGED
              106  LOAD_STR                 'Object changing location.'
              108  LOAD_CONST               ('cancel_reason_msg',)
              110  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              112  POP_TOP          

 L. 323       114  LOAD_DEREF               'self'
              116  LOAD_ATTR                vfx_on_move
              118  LOAD_CONST               None
              120  COMPARE_OP               is-not
              122  POP_JUMP_IF_FALSE   146  'to 146'

 L. 324       124  LOAD_FAST                'out_sequence'
              126  LOAD_METHOD              append
              128  LOAD_FAST                'object_to_move'
              130  BUILD_TUPLE_1         1 
              132  LOAD_CLOSURE             'self'
              134  BUILD_TUPLE_1         1 
              136  LOAD_LAMBDA              '<code_object <lambda>>'
              138  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<lambda>'
              140  MAKE_FUNCTION_9          'default, closure'
              142  CALL_METHOD_1         1  '1 positional argument'
              144  POP_TOP          
            146_0  COME_FROM           122  '122'

 L. 326       146  LOAD_FAST                'do_fade'
              148  POP_JUMP_IF_FALSE   172  'to 172'

 L. 327       150  LOAD_FAST                'out_sequence'
              152  LOAD_METHOD              append
              154  LOAD_FAST                'object_to_move'
              156  BUILD_TUPLE_1         1 
              158  LOAD_CLOSURE             'self'
              160  BUILD_TUPLE_1         1 
              162  LOAD_LAMBDA              '<code_object <lambda>>'
              164  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<lambda>'
              166  MAKE_FUNCTION_9          'default, closure'
              168  CALL_METHOD_1         1  '1 positional argument'
              170  POP_TOP          
            172_0  COME_FROM           148  '148'

 L. 329       172  LOAD_FAST                'moves'
              174  LOAD_METHOD              append
              176  LOAD_FAST                'object_to_move'
              178  BUILD_TUPLE_1         1 
              180  LOAD_CLOSURE             'chosen_strategy'
              182  LOAD_CLOSURE             'resolver'
              184  BUILD_TUPLE_2         2 
              186  LOAD_LAMBDA              '<code_object <lambda>>'
              188  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<lambda>'
              190  MAKE_FUNCTION_9          'default, closure'
              192  CALL_METHOD_1         1  '1 positional argument'
              194  POP_TOP          

 L. 331       196  LOAD_FAST                'do_fade'
              198  POP_JUMP_IF_FALSE    94  'to 94'

 L. 332       200  LOAD_FAST                'in_sequence'
              202  LOAD_METHOD              append
              204  LOAD_FAST                'object_to_move'
              206  BUILD_TUPLE_1         1 
              208  LOAD_CLOSURE             'self'
              210  BUILD_TUPLE_1         1 
              212  LOAD_LAMBDA              '<code_object <lambda>>'
              214  LOAD_STR                 'MovingObjectsSituation._move_objects.<locals>.<lambda>'
              216  MAKE_FUNCTION_9          'default, closure'
              218  CALL_METHOD_1         1  '1 positional argument'
              220  POP_TOP          
              222  JUMP_BACK            94  'to 94'
              224  POP_BLOCK        
            226_0  COME_FROM_LOOP       88  '88'

 L. 335       226  BUILD_LIST_0          0 
              228  STORE_FAST               'sequence'

 L. 337       230  LOAD_FAST                'out_sequence'
          232_234  POP_JUMP_IF_FALSE   270  'to 270'

 L. 338       236  LOAD_FAST                'sequence'
              238  LOAD_METHOD              append
              240  LOAD_FAST                'out_sequence'
              242  CALL_METHOD_1         1  '1 positional argument'
              244  POP_TOP          

 L. 340       246  LOAD_FAST                'sequence'
              248  LOAD_METHOD              append
              250  LOAD_GLOBAL              SoftSleepElement
              252  LOAD_GLOBAL              clock
              254  LOAD_METHOD              interval_in_sim_minutes
              256  LOAD_DEREF               'self'
              258  LOAD_ATTR                fade
              260  LOAD_ATTR                out_time
              262  CALL_METHOD_1         1  '1 positional argument'
              264  CALL_FUNCTION_1       1  '1 positional argument'
              266  CALL_METHOD_1         1  '1 positional argument'
              268  POP_TOP          
            270_0  COME_FROM           232  '232'

 L. 342       270  LOAD_FAST                'sequence'
              272  LOAD_METHOD              append
              274  LOAD_FAST                'moves'
              276  CALL_METHOD_1         1  '1 positional argument'
              278  POP_TOP          

 L. 344       280  LOAD_FAST                'in_sequence'
          282_284  POP_JUMP_IF_FALSE   296  'to 296'

 L. 345       286  LOAD_FAST                'sequence'
              288  LOAD_METHOD              append
              290  LOAD_FAST                'in_sequence'
              292  CALL_METHOD_1         1  '1 positional argument'
              294  POP_TOP          
            296_0  COME_FROM           282  '282'

 L. 347       296  LOAD_GLOBAL              build_element
              298  LOAD_FAST                'sequence'
              300  LOAD_GLOBAL              CleanupType
              302  LOAD_ATTR                RunAll
              304  LOAD_CONST               ('critical',)
              306  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              308  STORE_FAST               'element'

 L. 349       310  LOAD_GLOBAL              services
              312  LOAD_METHOD              time_service
              314  CALL_METHOD_0         0  '0 positional arguments'
              316  LOAD_ATTR                sim_timeline
              318  LOAD_METHOD              schedule
              320  LOAD_FAST                'element'
              322  CALL_METHOD_1         1  '1 positional argument'
              324  POP_TOP          

Parse error at or near `MAKE_FUNCTION_9' instruction at offset 190
