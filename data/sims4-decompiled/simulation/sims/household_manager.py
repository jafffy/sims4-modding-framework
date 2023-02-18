# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\household_manager.py
# Compiled at: 2022-06-21 21:52:57
# Size of source mod 2**32: 27913 bytes

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
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_slice2 ::= expr expr BUILD_SLICE_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
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
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
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
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
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
delete ::= delete_subscript . 
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
delete_subscript ::= expr expr DELETE_SUBSCR . 
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= build_slice2 . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
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
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
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
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= delete . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
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
   
 L. 508       178  LOAD_FAST                'household_msg'
                 180  LOAD_ATTR                inventory
                 182  LOAD_ATTR                objects
                 184  LOAD_CONST               None
                 186  LOAD_CONST               None
                 188  BUILD_SLICE_2         2 
                 190  DELETE_SUBSCR    
               192_0  COME_FROM           122  '122'
->             192_1  COME_FROM            98  '98'
import collections, time, distributor
from protocolbuffers import FileSerialization_pb2, MoveInMoveOut_pb2, Consts_pb2
from build_buy import _buildbuy
from interactions.context import InteractionContext
from interactions.priority import Priority
from relationships import global_relationship_tuning
from sims.fixup.sim_info_fixup_action import SimInfoFixupActionTiming
from sims4.utils import classproperty
from singletons import DEFAULT
from world.travel_tuning import TravelTuning
import build_buy, id_generator, indexed_manager, objects.object_manager, persistence_error_types, server.account, services, sims.household, sims4.log
logger = sims4.log.Logger('HouseholdManager')

class HouseholdFixupHelper:

    def __init__(self):
        self._households_sharing_sims = set()

    def add_shared_sim_household(self, household):
        self._households_sharing_sims.add(household)

    def fix_shared_sim_households(self):
        for household in self._households_sharing_sims:
            if not household.destroy_household_if_empty():
                household.handle_adultless_household(skip_hidden=True, skip_premade=True)


class HouseholdManager(objects.object_manager.DistributableObjectManager):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._loaded = False
        self._save_slot_data = None
        self._pending_household_funds = collections.defaultdict(list)
        self._pending_transfers = {}

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_HOUSEHOLD_MANAGER

    def create_household(self, account, starting_funds=DEFAULT):
        new_household = sims.household.Household(account, starting_funds)
        self.add(new_household)
        return new_household

    def load_households(self):
        if self._loaded:
            return
        if indexed_manager.capture_load_times:
            time_stamp = time.time()
        fixup_helper = HouseholdFixupHelper()
        business_service = services.business_service()
        for household_proto in services.get_persistence_service().all_household_protos():
            household_id = household_proto.household_id
            household = self.get(household_id)
            if household is None:
                household = self._load_household_from_household_proto(household_proto, fixup_helper=fixup_helper)
                business_service.load_legacy_data(household, household_proto)

        fixup_helper.fix_shared_sim_households()
        for household_id in self._pending_household_funds.keys():
            logger.error('Household {} has pending funds leftover from BB after all households were loaded.', household_id, owner='camilogarcia')

        self._pending_household_funds = None
        relationship_service = services.relationship_service()
        if relationship_service is not None:
            relationship_service.purge_invalid_relationships()
        for sim_info in services.sim_info_manager().get_all():
            sim_info.on_all_sim_infos_loaded()
            sim_info.set_default_data()

        if indexed_manager.capture_load_times:
            elapsed_time = time.time() - time_stamp
            indexed_manager.object_load_times['household'] = elapsed_time
        self._loaded = True

    def load_household(self, household_id):
        return self._load_household(household_id)

    def _load_household(self, household_id):
        household = self.get(household_id)
        if household is not None:
            for sim_info in household.sim_info_gen():
                zone_id = services.current_zone_id()
                if sim_info.zone_id != zone_id:
                    householdProto = services.get_persistence_service().get_household_proto_buff(household_id)
                    if householdProto is None:
                        logger.error('unable to find household with household id {}'.household_id)
                        return
                    found_sim = False
                    if householdProto.sims.ids:
                        for sim_id in householdProto.sims.ids:
                            if sim_id == sim_info.sim_id:
                                found_sim = True
                                break

                    if found_sim:
                        sim_proto = services.get_persistence_service().get_sim_proto_buff(sim_id)
                        sim_info.load_sim_info(sim_proto)

            return household
        logger.info('Starting to load household id = {0}', household_id)
        household_proto = services.get_persistence_service().get_household_proto_buff(household_id)
        if household_proto is None:
            sims4.log.error('Persistence', 'Household proto could not be found id = {0}', household_id)
            return
        household = self._load_household_from_household_proto(household_proto)
        return household

    def _load_household_from_household_proto(self, household_proto, fixup_helper=None):
        account = services.account_service().get_account_by_id((household_proto.account_id), try_load_account=True)
        if account is None:
            sims4.log.error('Persistence', "Household account doesn't exist in account ids. Creating temp account", owner='yshan')
            account = server.account.Account(household_proto.account_id, 'TempPersonaName')
        household = sims.household.Household(account)
        resend_sim_infos = household.load_data(household_proto, fixup_helper)
        logger.info('Household loaded. name:{:20} id:{:10} #sim_infos:{:2}', household.name, household.id, len(household))
        self.add(household)
        if resend_sim_infos:
            household.resend_sim_infos()
        household.initialize_sim_infos()
        if household is services.client_manager().get_first_client().household:
            for sim_info in household.sim_info_gen():
                for other_info in household.sim_info_gen():
                    if sim_info is not other_info:
                        relationship_service = services.relationship_service()
                        if relationship_service.has_bit(sim_info.id, other_info.id, global_relationship_tuning.RelationshipGlobalTuning.NEIGHBOR_RELATIONSHIP_BIT):
                            relationship_service.remove_relationship_bit(sim_info.id, other_info.id, global_relationship_tuning.RelationshipGlobalTuning.NEIGHBOR_RELATIONSHIP_BIT)

            household.bills_manager.sanitize_household_inventory()
        if self._pending_household_funds is not None:
            pending_funds_reasons = self._pending_household_funds.get(household.id)
            if pending_funds_reasons is not None:
                del self._pending_household_funds[household.id]
                for fund, reason in pending_funds_reasons:
                    household.funds.add(fund, reason, None)

        return household

    def switch_sim_household(self, sim_info, target_sim_info=None):
        active_household = services.active_household()
        starting_household = sim_info.household
        destination_household = active_household if target_sim_info is None else target_sim_info.household
        self.switch_sim_from_household_to_target_household(sim_info, starting_household, destination_household)

    def switch_sim_from_household_to_target_household(self, sim_info, starting_household, destination_household, destroy_if_empty_household=True):
        active_household = services.active_household()
        if services.hidden_sim_service().is_hidden(sim_info.id):
            services.hidden_sim_service().unhide(sim_info.id)
        elif starting_household is destination_household:
            logger.error('Trying to run AddToHousehold basic extra on a sim who is already in the destination household.')
            return False
            if not destination_household.can_add_sim_info(sim_info):
                logger.error('Trying to run AddToHousehold basic extra when there is no room in the destination household.')
                return False
            starting_household.remove_sim_info(sim_info, destroy_if_empty_household=destroy_if_empty_household, assign_to_none=False)
            destination_household.add_sim_info_to_household(sim_info)
            client = services.client_manager().get_first_client()
            destination_travel_group = destination_household.get_travel_group()
            failed_to_add_to_travel_group = False
            if destination_travel_group is not None:
                if sim_info.is_in_travel_group():
                    if sim_info not in destination_travel_group:
                        old_travel_group = services.travel_group_manager().get_travel_group_by_sim_info(sim_info)
                        old_travel_group.remove_sim_info(sim_info)
                if any((sim.sim_info in destination_travel_group for sim in client.selectable_sims.get_instanced_sims())):
                    can_add_to_travel_group = destination_travel_group.can_add_to_travel_group(sim_info)
                    failed_to_add_to_travel_group = not destination_travel_group.add_sim_info(sim_info) if can_add_to_travel_group else True
                    if can_add_to_travel_group:
                        if failed_to_add_to_travel_group:
                            logger.error('Unable to add Sim {} to travel group.', sim_info, owner='jdimailig')
            if destination_household is active_household:
                client.add_selectable_sim_info(sim_info)
                sim_info.apply_fixup_actions(SimInfoFixupActionTiming.ON_ADDED_TO_ACTIVE_HOUSEHOLD)
        else:
            client.remove_selectable_sim_info(sim_info)
        if sim_info.career_tracker is not None:
            sim_info.career_tracker.remove_invalid_careers()
        if sim_info.aspiration_tracker is not None:
            sim_info.aspiration_tracker.clear_tracked_client_data()
            sim_info.aspiration_tracker.send_event_data_to_client()
        sim = sim_info.get_sim_instance()
        if sim is not None:
            sim.update_intended_position_on_active_lot(update_ui=True)
            situation_manager = services.get_zone_situation_manager()
            for situation in situation_manager.get_situations_sim_is_in(sim):
                if destination_household is active_household:
                    if situation.is_user_facing:
                        continue
                situation_manager.remove_sim_from_situation(sim, situation.id)

            services.daycare_service().on_sim_spawn(sim_info)
            if destination_travel_group is not None:
                if failed_to_add_to_travel_group:
                    interaction_context = InteractionContext(sim, InteractionContext.SOURCE_SCRIPT, Priority.Critical)
                    sim.push_super_affordance(TravelTuning.GO_HOME_INTERACTION, None, interaction_context)
        return True

    def is_household_stored_in_any_neighborhood_proto(self, household_id):
        for neighborhood_proto in services.get_persistence_service().get_neighborhoods_proto_buf_gen():
            if any((household_id == household_account_proto.household_id for household_account_proto in neighborhood_proto.npc_households)):
                return True

        return False

    def get_by_sim_id(self, sim_id):
        for house in self._objects.values():
            if house.sim_in_household(sim_id):
                return house

    def save(self, **kwargs):
        households = self.get_all()
        for household in households:
            household.save_data()

    def on_all_households_and_sim_infos_loaded(self, client):
        for household in self.get_all():
            household.on_all_households_and_sim_infos_loaded()

    def on_client_disconnect(self, client):
        for household in self.get_all():
            household.on_client_disconnect()

    def on_zone_load(self):
        for household in self.get_all():
            household.on_zone_load()

    def on_zone_unload(self):
        for household in self.get_all():
            household.on_zone_unload()

    @staticmethod
    def get_active_sim_home_zone_id():
        client = services.client_manager().get_first_client()
        if client is not None:
            active_sim = client.active_sim
            if active_sim is not None:
                household = active_sim.household
                if household is not None:
                    return household.home_zone_id

    def try_add_pending_household_funds(self, household_id, funds, reason):
        if self._pending_household_funds is None:
            return False
        self._pending_household_funds[household_id].append((funds, reason))
        return True

    def add_pending_transfer(self, household_id, is_transfer_solo, transfer_proto):
        self._pending_transfers[household_id] = (
         is_transfer_solo, transfer_proto)

    def get_pending_transfer(self, household_id):
        pending_transfer_data = self._pending_transfers.get(household_id, (None, None))
        return pending_transfer_data

    def remove_pending_transfer(self, household_id):
        if household_id in self._pending_transfers:
            del self._pending_transfers[household_id]

    def transfer_household_inventory(self, source_household, target_household):
        active_household = services.active_household()
        target_household.copy_rewards_inventory_from_household(source_household)
        if source_household is active_household:
            self.transfer_active_household_inventory(source_household, target_household)
        else:
            if target_household is active_household:
                self.transfer_inactive_household_inventory(source_household, target_household)
            else:
                logger.error("Trying to transfer household inventory from one inactive household to another, we currently don't support that. Feel free to add if we come up with a use case. S={}, T={}", source_household, target_household)

    def transfer_active_household_inventory(self, source_household, target_household):
        inventory_available = build_buy.is_household_inventory_available(target_household.id)
        source_household_msg = services.get_persistence_service().get_household_proto_buff(source_household.id)
        target_household_msg = services.get_persistence_service().get_household_proto_buff(target_household.id)
        object_manager = services.object_manager()
        object_ids = build_buy.get_object_ids_in_household_inventory(source_household.id)
        for object_id in object_ids:
            object_data_raw = _buildbuy.get_object_data_in_household_inventory(object_id, source_household.id)
            if object_data_raw is None:
                continue
            obj = self.create_object_from_raw_inv_data(object_id, object_data_raw)
            self._transfer_object(target_household, obj, inventory_available, target_household_msg)

        for object_data in source_household_msg.inventory.objects:
            if object_data.object_id in object_ids:
                continue
            obj = object_manager.get(object_data.object_id)
            if obj is None:
                obj = self._create_object_from_object_data(object_data.object_id, object_data)
            if obj is not None:
                self._transfer_object(target_household, obj, inventory_available, target_household_msg)

    def _transfer_object(self, target_household, obj, inventory_available, target_household_msg):
        obj.set_household_owner_id(target_household.id)
        if inventory_available:
            build_buy.move_object_to_household_inventory(obj)
        else:
            if target_household_msg is not None:
                object_data = obj.save_object(target_household_msg.inventory.objects)
                if object_data is not None:
                    object_data.object_id = id_generator.generate_object_id()
            obj.destroy(cause='Merge/Transfer to New Household Inventory')

    def transfer_inactive_household_inventory--- This code section failed: ---

 L. 487         0  LOAD_GLOBAL              build_buy
                2  LOAD_METHOD              is_household_inventory_available
                4  LOAD_FAST                'source_household'
                6  LOAD_ATTR                id
                8  CALL_METHOD_1         1  '1 positional argument'
               10  POP_JUMP_IF_FALSE   100  'to 100'

 L. 488        12  LOAD_GLOBAL              build_buy
               14  LOAD_METHOD              get_object_ids_in_household_inventory
               16  LOAD_FAST                'source_household'
               18  LOAD_ATTR                id
               20  CALL_METHOD_1         1  '1 positional argument'
               22  STORE_FAST               'object_ids'

 L. 489        24  SETUP_LOOP          192  'to 192'
               26  LOAD_FAST                'object_ids'
               28  GET_ITER         
               30  FOR_ITER             96  'to 96'
               32  STORE_FAST               'object_id'

 L. 490        34  LOAD_GLOBAL              _buildbuy
               36  LOAD_METHOD              get_object_data_in_household_inventory
               38  LOAD_FAST                'object_id'
               40  LOAD_FAST                'source_household'
               42  LOAD_ATTR                id
               44  CALL_METHOD_2         2  '2 positional arguments'
               46  STORE_FAST               'object_data_raw'

 L. 491        48  LOAD_FAST                'self'
               50  LOAD_METHOD              create_object_from_raw_inv_data
               52  LOAD_FAST                'object_id'
               54  LOAD_FAST                'object_data_raw'
               56  CALL_METHOD_2         2  '2 positional arguments'
               58  STORE_FAST               'obj'

 L. 492        60  LOAD_GLOBAL              build_buy
               62  LOAD_METHOD              remove_object_from_household_inventory
               64  LOAD_FAST                'object_id'
               66  LOAD_FAST                'source_household'
               68  CALL_METHOD_2         2  '2 positional arguments'
               70  POP_TOP          

 L. 495        72  LOAD_FAST                'obj'
               74  LOAD_METHOD              set_household_owner_id
               76  LOAD_FAST                'target_household'
               78  LOAD_ATTR                id
               80  CALL_METHOD_1         1  '1 positional argument'
               82  POP_TOP          

 L. 496        84  LOAD_GLOBAL              build_buy
               86  LOAD_METHOD              move_object_to_household_inventory
               88  LOAD_FAST                'obj'
               90  CALL_METHOD_1         1  '1 positional argument'
               92  POP_TOP          
               94  JUMP_BACK            30  'to 30'
               96  POP_BLOCK        
               98  JUMP_FORWARD        192  'to 192'
            100_0  COME_FROM            10  '10'

 L. 500       100  LOAD_GLOBAL              services
              102  LOAD_METHOD              get_persistence_service
              104  CALL_METHOD_0         0  '0 positional arguments'
              106  LOAD_METHOD              get_household_proto_buff
              108  LOAD_FAST                'source_household'
              110  LOAD_ATTR                id
              112  CALL_METHOD_1         1  '1 positional argument'
              114  STORE_FAST               'household_msg'

 L. 501       116  LOAD_FAST                'household_msg'
              118  LOAD_CONST               None
              120  COMPARE_OP               is-not
              122  POP_JUMP_IF_FALSE   192  'to 192'

 L. 502       124  SETUP_LOOP          178  'to 178'
              126  LOAD_FAST                'household_msg'
              128  LOAD_ATTR                inventory
              130  LOAD_ATTR                objects
              132  GET_ITER         
              134  FOR_ITER            176  'to 176'
              136  STORE_FAST               'object_msg'

 L. 503       138  LOAD_FAST                'self'
              140  LOAD_METHOD              _create_object_from_object_data
              142  LOAD_FAST                'object_msg'
              144  LOAD_ATTR                object_id
              146  LOAD_FAST                'object_msg'
              148  CALL_METHOD_2         2  '2 positional arguments'
              150  STORE_FAST               'obj'

 L. 504       152  LOAD_FAST                'obj'
              154  LOAD_METHOD              set_household_owner_id
              156  LOAD_FAST                'target_household'
              158  LOAD_ATTR                id
              160  CALL_METHOD_1         1  '1 positional argument'
              162  POP_TOP          

 L. 505       164  LOAD_GLOBAL              build_buy
              166  LOAD_METHOD              move_object_to_household_inventory
              168  LOAD_FAST                'obj'
              170  CALL_METHOD_1         1  '1 positional argument'
              172  POP_TOP          
              174  JUMP_BACK           134  'to 134'
              176  POP_BLOCK        
            178_0  COME_FROM_LOOP      124  '124'

 L. 508       178  LOAD_FAST                'household_msg'
              180  LOAD_ATTR                inventory
              182  LOAD_ATTR                objects
              184  LOAD_CONST               None
              186  LOAD_CONST               None
              188  BUILD_SLICE_2         2 
              190  DELETE_SUBSCR    
            192_0  COME_FROM           122  '122'
            192_1  COME_FROM            98  '98'
            192_2  COME_FROM_LOOP       24  '24'

Parse error at or near `COME_FROM' instruction at offset 192_1

    def create_object_from_raw_inv_data(self, object_id, raw_inv_data, load_object=False):
        object_data = FileSerialization_pb2.ObjectData()
        object_data.ParseFromString(raw_inv_data)
        return self._create_object_from_object_data(object_id, object_data, load_object=load_object)

    def _create_object_from_object_data(self, object_id, object_data, load_object=False):
        post_add_callback = lambda o:         if load_object:
o.load_object(object_data, inline_finalize=True) # Avoid dead code: None
        obj = objects.system.create_object((object_data.guid), obj_id=object_id,
          obj_state=(object_data.state_index),
          post_add=post_add_callback)
        return obj

    def move_household_out_of_lot(self, household, sell_furniture, delta_funds):
        zone_id = household.home_zone_id
        msg = MoveInMoveOut_pb2.MoveInMoveOutData()
        msg.zone_src = zone_id
        msg.zone_dst = 0
        msg.move_out_data_src.sell_furniture = sell_furniture
        msg.move_out_data_src.delta_funds = delta_funds
        msg.notify_gameplay = True
        distributor.system.Distributor.instance().add_event(Consts_pb2.MSG_MOVE_FAMILY_OUT, msg)
