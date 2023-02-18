# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server\client.py
# Compiled at: 2021-10-14 17:49:40
# Size of source mod 2**32: 49159 bytes

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
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD _come_froms
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
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr . expr BUILD_TUPLE_UNPACK_WITH_CALL_2
build_tuple_unpack_with_call ::= expr expr . BUILD_TUPLE_UNPACK_WITH_CALL_2
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
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw2 ::= expr . build_tuple_unpack_with_call build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw3 ::= expr . build_tuple_unpack_with_call expr CALL_FUNCTION_EX_KW
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
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
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
delete ::= expr . DELETE_ATTR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
else_suite ::= suite_stmts . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= get_iter . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
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
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
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
stmt ::= for . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
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
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
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
   
 L. 529       116  LOAD_FAST                'previous_inventory'
                 118  LOAD_METHOD              get_stack_items
                 120  LOAD_FAST                'stack_id'
                 122  CALL_METHOD_1         1  '1 positional argument'
                 124  STORE_FAST               'stack_items'
->             126_0  COME_FROM_LOOP       64  '64'
                 126  JUMP_FORWARD        132  'to 132'
               128_0  COME_FROM            58  '58'
from _collections import defaultdict
from _weakrefset import WeakSet
import itertools, operator, weakref
from protocolbuffers import Sims_pb2, Consts_pb2
from protocolbuffers.DistributorOps_pb2 import Operation, SetWhimBucks
from distributor.ops import GenericProtocolBufferOp
from distributor.rollback import ProtocolBufferRollback
from distributor.shared_messages import create_icon_info_msg
from distributor.system import Distributor
from objects import ALL_HIDDEN_REASONS, HiddenReasonFlag
from objects.object_enums import ResetReason
from server.live_drag_tuning import LiveDragLocation, LiveDragState, LiveDragTuning
from sims4.callback_utils import CallableList
from sims4.utils import constproperty
from vfx import vfx_mask
import distributor.fields, distributor.ops, gsi_handlers, interactions.context, omega, services, sims4.log, telemetry_helper
logger = sims4.log.Logger('Client')
logger_live_drag = sims4.log.Logger('LiveDrag', default_owner='rmccord')
TELEMETRY_GROUP_ACTIVE_SIM = 'ASIM'
TELEMETRY_HOOK_ACTIVE_SIM_CHANGED = 'ASCH'
writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_ACTIVE_SIM)
MSG_ID_NAMES = {}
for name, val in vars(Consts_pb2).items():
    if name.startswith('MSG_'):
        MSG_ID_NAMES[val] = name

class Client:
    _interaction_source = interactions.context.InteractionContext.SOURCE_PIE_MENU
    _interaction_priority = interactions.priority.Priority.High

    def __init__(self, session_id, account, household_id):
        self.id = session_id
        self.manager = None
        self._account = account
        self._household_id = household_id
        self._choice_menu = None
        self._interaction_parameters = {}
        self.active = True
        self.zone_id = services.current_zone_id()
        self._selectable_sims = SelectableSims(self)
        self._active_sim_info = None
        self._active_sim_changed = CallableList()
        self.ui_objects = weakref.WeakSet()
        self.primitives = ()
        self._live_drag_objects = []
        self._live_drag_start_system = LiveDragLocation.INVALID
        self._live_drag_is_stack = False
        self._live_drag_sell_dialog_active = False
        self.objects_moved_via_live_drag = WeakSet()

    def __repr__(self):
        return '<Client {0:#x}>'.format(self.id)

    @property
    def account(self):
        return self._account

    @distributor.fields.Field(op=(distributor.ops.UpdateClientActiveSim))
    def active_sim_info(self):
        return self._active_sim_info

    resend_active_sim_info = active_sim_info.get_resend()

    @active_sim_info.setter
    def active_sim_info(self, sim_info):
        self._set_active_sim_without_field_distribution(sim_info)

    @property
    def active_sim(self):
        if self.active_sim_info is not None:
            return self.active_sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)

    @active_sim.setter
    def active_sim(self, sim):
        self.active_sim_info = sim.sim_info

    def _set_active_sim_without_field_distribution(self, sim_info):
        if self._active_sim_info is not None:
            if self._active_sim_info is sim_info:
                return
        else:
            current_sim = self._active_sim_info.get_sim_instance() if self._active_sim_info is not None else None
            if sim_info is not None:
                self._active_sim_info = sim_info
                if sim_info.household is not None:
                    sim_info.household.on_active_sim_changed(sim_info)
            else:
                self._active_sim_info = None
        self.notify_active_sim_changed(current_sim, new_sim_info=sim_info)

    @property
    def choice_menu(self):
        return self._choice_menu

    @property
    def interaction_source(self):
        return self._interaction_source

    @interaction_source.setter
    def interaction_source(self, value):
        if value is None:
            if self._interaction_source is not Client._interaction_source:
                del self._interaction_source
        else:
            self._interaction_source = value

    @property
    def interaction_priority(self):
        return self._interaction_priority

    @interaction_priority.setter
    def interaction_priority(self, value):
        if value is None:
            if self._interaction_priority is not Client._interaction_priority:
                del self._interaction_priority
        else:
            self._interaction_priority = value

    @property
    def household_id(self):
        return self._household_id

    @property
    def household(self):
        household_manager = services.household_manager()
        if household_manager is not None:
            return household_manager.get(self._household_id)

    @property
    def selectable_sims(self):
        return self._selectable_sims

    def create_interaction_context(self, sim, **kwargs):
        context = (interactions.context.InteractionContext)(sim,
 self.interaction_source,
 self.interaction_priority, client=self, **kwargs)
        return context

    @property
    def live_drag_objects(self):
        return self._live_drag_objects

    def get_interaction_parameters(self):
        return self._interaction_parameters

    def set_interaction_parameters(self, **kwargs):
        self._interaction_parameters = kwargs

    def set_choices(self, new_choices):
        self._choice_menu = new_choices

    def select_interaction(self, choice_id, revision):
        if self.choice_menu is not None:
            if revision == self.choice_menu.revision:
                choice_menu = self.choice_menu
                self._choice_menu = None
                self.set_interaction_parameters()
                try:
                    return choice_menu.select(choice_id)
                except:
                    if choice_menu.simref is not None:
                        sim = choice_menu.simref()
                        if sim is not None:
                            sim.reset((ResetReason.RESET_ON_ERROR), cause='Exception while selecting interaction from the pie menu.')
                    raise

    def get_create_op(self, *args, **kwargs):
        return (distributor.ops.ClientCreate)(self, *args, is_active=True, **kwargs)

    def get_delete_op(self):
        return distributor.ops.ClientDelete()

    def get_create_after_objs(self):
        active = self.active_sim
        if active is not None:
            yield active
        household = self.household
        if household is not None:
            yield household

    @property
    def valid_for_distribution(self):
        return True

    def refresh_achievement_data(self):
        active_sim_info = None
        if self.active_sim is not None:
            active_sim_info = self.active_sim.sim_info
        self.account.achievement_tracker.refresh_progress(active_sim_info)

    def send_message(self, msg_id, msg):
        if self.active:
            omega.send(self.id, msg_id, msg.SerializeToString())
        else:
            logger.warn('Message sent to client {} after it has already disconnected.', self)

    def validate_selectable_sim(self):
        if not (self._active_sim_info is None or self._active_sim_info.get_is_enabled_in_skewer()):
            self.set_next_sim()

    def set_next_sim(self):
        sim_info = self._selectable_sims.get_next_selectable(self._active_sim_info)
        if sim_info is self.active_sim_info:
            self.resend_active_sim_info()
            return False
        return self.set_active_sim_info(sim_info)

    def set_next_sim_or_none(self, only_if_this_active_sim_info=None):
        if only_if_this_active_sim_info is not None:
            if self._active_sim_info is not only_if_this_active_sim_info:
                return
        sim_info = self._selectable_sims.get_next_selectable(self._active_sim_info)
        if sim_info is None:
            return self.set_active_sim_info(None)
        if sim_info is self._active_sim_info:
            return self.set_active_sim_info(None)
        return self.set_active_sim_info(sim_info)

    def set_active_sim_by_id(self, sim_id, consider_active_sim=True):
        if self.active_sim_info is not None:
            if self.active_sim_info.id == sim_id:
                return False
        for sim_info in self._selectable_sims:
            if sim_info.sim_id == sim_id and not sim_info.get_is_enabled_in_skewer(consider_active_sim=consider_active_sim):
                return False
                returnval = self.set_active_sim_info(sim_info)
                if returnval:
                    if not consider_active_sim:
                        self.send_selectable_sims_update()
                return returnval

        return False

    def set_active_sim(self, sim):
        return self.set_active_sim_info(sim.sim_info)

    def set_active_sim_info(self, sim_info):
        with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_ACTIVE_SIM_CHANGED, sim_info=sim_info):
            pass
        self.active_sim_info = sim_info
        return self._active_sim_info is not None

    def add_selectable_sim_info(self, sim_info, send_relationship_update=True):
        self._selectable_sims.add_selectable_sim_info(sim_info, send_relationship_update=send_relationship_update)
        if self.active_sim_info is None:
            self.set_next_sim()
        self.household.refresh_aging_updates(sim_info)

    def add_selectable_sim_by_id(self, sim_id):
        sim_info = services.sim_info_manager().get(sim_id)
        if sim_info is not None:
            self.add_selectable_sim_info(sim_info)

    def remove_selectable_sim_info(self, sim_info):
        self._selectable_sims.remove_selectable_sim_info(sim_info)
        if self.active_sim_info is None:
            self.set_next_sim()
        self.household.refresh_aging_updates(sim_info)

    def remove_selectable_sim_by_id(self, sim_id):
        if len(self._selectable_sims) <= 1:
            return False
        sim_info = services.sim_info_manager().get(sim_id)
        if sim_info is not None:
            self.remove_selectable_sim_info(sim_info)
        return True

    def make_all_sims_selectable(self):
        self.clear_selectable_sims()
        for sim_info in services.sim_info_manager().objects:
            self._selectable_sims.add_selectable_sim_info(sim_info)

        self.set_next_sim()

    def clear_selectable_sims(self):
        self.active_sim_info = None
        self._selectable_sims.clear_selectable_sims()

    def register_active_sim_changed(self, callback):
        if callback not in self._active_sim_changed:
            self._active_sim_changed.append(callback)

    def unregister_active_sim_changed(self, callback):
        if callback in self._active_sim_changed:
            self._active_sim_changed.remove(callback)

    def on_sim_added_to_skewer(self, sim_info, send_relationship_update=True):
        if send_relationship_update:
            sim_info.relationship_tracker.send_relationship_info()
        else:
            is_zone_running = services.current_zone().is_zone_running
            sim_info.on_sim_added_to_skewer()
            if not is_zone_running:
                sim_info.commodity_tracker.start_low_level_simulation()
            else:
                services.active_household().distribute_household_data()
            sim_info.commodity_tracker.send_commodity_progress_update(from_add=True)
            sim_info.career_tracker.on_sim_added_to_skewer()
            if sim_info.degree_tracker is not None:
                sim_info.degree_tracker.on_sim_added_to_skewer()
            sim_info.send_satisfaction_points_update(SetWhimBucks.LOAD)
            sim_info.resend_trait_ids()
            sim = sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
            if sim is not None:
                if is_zone_running:
                    sim.inventory_component.visible_storage.allow_ui = True
                    sim.inventory_component.publish_inventory_items()
                sim.ui_manager.refresh_ui_data()
                services.autonomy_service().logging_sims.add(sim)
                sim_info.start_aspiration_tracker_on_instantiation(force_ui_update=True)
                if sim_info.whim_tracker is not None:
                    sim_info.whim_tracker.start_whims_tracker()
        zone_director = services.venue_service().get_zone_director()
        if zone_director is not None:
            zone_director.on_sim_added_to_skewer(sim_info)
        sim_info.trait_tracker.sort_and_send_commodity_list()

    def on_sim_removed_from_skewer(self, sim_info):
        sim = sim_info.get_sim_instance()
        if sim is not None:
            autonomy_service = services.autonomy_service()
            if autonomy_service is not None:
                autonomy_service.logging_sims.discard(sim)

    def clean_and_send_remaining_relationship_info(self):
        relationship_service = services.relationship_service()
        for sim_info in self.selectable_sims:
            sim_info.relationship_tracker.clean_and_send_remaining_relationship_info()
            relationship_service.clean_and_send_remaining_object_relationships(sim_info.id)

    def cancel_live_drag_on_objects(self):
        for obj in self._live_drag_objects:
            obj.live_drag_component.cancel_live_dragging()

        self._live_drag_objects = []

    def _get_stack_items_from_drag_object--- This code section failed: ---

 L. 514         0  LOAD_FAST                'drag_object'
                2  LOAD_ATTR                inventoryitem_component
                4  LOAD_CONST               None
                6  COMPARE_OP               is
                8  POP_JUMP_IF_FALSE    14  'to 14'

 L. 515        10  LOAD_CONST               (False, None)
               12  RETURN_VALUE     
             14_0  COME_FROM             8  '8'

 L. 517        14  LOAD_FAST                'drag_object'
               16  LOAD_ATTR                inventoryitem_component
               18  LOAD_METHOD              get_inventory
               20  CALL_METHOD_0         0  '0 positional arguments'
               22  STORE_FAST               'previous_inventory'

 L. 518        24  LOAD_FAST                'previous_inventory'
               26  LOAD_CONST               None
               28  COMPARE_OP               is
               30  POP_JUMP_IF_FALSE    36  'to 36'

 L. 519        32  LOAD_CONST               (False, None)
               34  RETURN_VALUE     
             36_0  COME_FROM            30  '30'

 L. 521        36  LOAD_FAST                'drag_object'
               38  LOAD_ATTR                inventoryitem_component
               40  LOAD_METHOD              get_stack_id
               42  CALL_METHOD_0         0  '0 positional arguments'
               44  STORE_FAST               'stack_id'

 L. 522        46  LOAD_FAST                'previous_inventory'
               48  LOAD_METHOD              get_stack_items
               50  LOAD_FAST                'stack_id'
               52  CALL_METHOD_1         1  '1 positional argument'
               54  STORE_FAST               'stack_items'

 L. 523        56  LOAD_FAST                'remove'
               58  POP_JUMP_IF_FALSE   128  'to 128'

 L. 524        60  LOAD_FAST                'is_stack'
               62  POP_JUMP_IF_FALSE   100  'to 100'

 L. 525        64  SETUP_LOOP          126  'to 126'
               66  LOAD_FAST                'stack_items'
               68  GET_ITER         
               70  FOR_ITER             96  'to 96'
               72  STORE_FAST               'item'

 L. 526        74  LOAD_FAST                'previous_inventory'
               76  LOAD_ATTR                try_remove_object_by_id
               78  LOAD_FAST                'item'
               80  LOAD_ATTR                id
               82  LOAD_FAST                'item'
               84  LOAD_METHOD              stack_count
               86  CALL_METHOD_0         0  '0 positional arguments'
               88  LOAD_CONST               ('count',)
               90  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               92  STORE_FAST               'success'
               94  JUMP_BACK            70  'to 70'
               96  POP_BLOCK        
               98  JUMP_ABSOLUTE       132  'to 132'
            100_0  COME_FROM            62  '62'

 L. 528       100  LOAD_FAST                'previous_inventory'
              102  LOAD_ATTR                try_remove_object_by_id
              104  LOAD_FAST                'drag_object'
              106  LOAD_ATTR                id
              108  LOAD_CONST               1
              110  LOAD_CONST               ('count',)
              112  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              114  STORE_FAST               'success'

 L. 529       116  LOAD_FAST                'previous_inventory'
              118  LOAD_METHOD              get_stack_items
              120  LOAD_FAST                'stack_id'
              122  CALL_METHOD_1         1  '1 positional argument'
              124  STORE_FAST               'stack_items'
            126_0  COME_FROM_LOOP       64  '64'
              126  JUMP_FORWARD        132  'to 132'
            128_0  COME_FROM            58  '58'

 L. 531       128  LOAD_CONST               True
              130  STORE_FAST               'success'
            132_0  COME_FROM           126  '126'

 L. 532       132  LOAD_FAST                'success'
              134  LOAD_FAST                'stack_items'
              136  BUILD_TUPLE_2         2 
              138  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM_LOOP' instruction at offset 126_0

    def remove_drag_object_and_get_next_item(self, drag_object):
        next_object_id = None
        success, stack_items = self._get_stack_items_from_drag_object(drag_object, remove=True)
        if success:
            if stack_items:
                next_object_id = stack_items[0].id
        return (
         success, next_object_id)

    def get_live_drag_object_value(self, drag_object, is_stack=False):
        _, stack_items = self._get_stack_items_from_drag_object(drag_object, remove=False, is_stack=is_stack)
        value = 0
        if is_stack and stack_items:
            for item in stack_items:
                value += item.current_value * item.stack_count()

        else:
            value = drag_object.current_value
        return value

    def start_live_drag(self, live_drag_object, start_system, is_stack, should_send_start_message: bool=True):
        self._live_drag_start_system = start_system
        success = True
        if is_stack:
            inventoryitem_component = live_drag_object.inventoryitem_component
            stack_id = inventoryitem_component.get_stack_id()
            current_inventory = inventoryitem_component.get_inventory()
            stack_items = current_inventory.get_stack_items(stack_id)
        else:
            stack_items = [
             live_drag_object]
        for item in stack_items:
            live_drag_component = live_drag_object.live_drag_component
            live_drag_component = item.live_drag_component
            if live_drag_component is None:
                logger_live_drag.error('Live Drag Start called on an object with no Live Drag Component. Object: {}'.format(item))
                self.send_live_drag_cancel(live_drag_object.id)
                return
            if not item.in_use or item.in_use_by(self):
                if not live_drag_component.can_live_drag:
                    logger_live_drag.warn('Live Drag Start called on an object that is in use. Object: {}'.format(item))
                    self.send_live_drag_cancel(item.id)
                    return
                success = live_drag_component.start_live_dragging(self, start_system)
                if not success:
                    break
                self._live_drag_objects.append(item)

        if not success:
            self.cancel_live_drag_on_objects()
            self.send_live_drag_cancel(live_drag_object.id, LiveDragLocation.INVALID)
        self._live_drag_is_stack = is_stack
        if gsi_handlers.live_drag_handlers.live_drag_archiver.enabled:
            gsi_handlers.live_drag_handlers.archive_live_drag('Start', 'Operation',
              (LiveDragLocation.GAMEPLAY_SCRIPT),
              start_system,
              live_drag_object_id=(live_drag_object.id))
        if live_drag_object.live_drag_component.active_household_has_sell_permission:
            sell_value = self.get_live_drag_object_value(live_drag_object, self._live_drag_is_stack) if live_drag_object.definition.get_is_deletable() else -1
            for child_object in live_drag_object.get_all_children_gen():
                sell_value += self.get_live_drag_object_value(child_object) if child_object.definition.get_is_deletable() else 0

        else:
            sell_value = -1
        valid_drop_object_ids, valid_stack_id = live_drag_component.get_valid_drop_object_ids()
        icon_info = create_icon_info_msg(live_drag_object.get_icon_info_data())
        if should_send_start_message:
            op = distributor.ops.LiveDragStart(live_drag_object.id, start_system, valid_drop_object_ids, valid_stack_id, sell_value, icon_info)
            distributor_system = Distributor.instance()
            distributor_system.add_op_with_no_owner(op)

    def end_live_drag(self, source_object, target_object=None, end_system=LiveDragLocation.INVALID, location=None):
        live_drag_component = source_object.live_drag_component
        if live_drag_component is None:
            logger_live_drag.error('Live Drag End called on an object with no Live Drag Component. Object: {}'.format(source_object))
            self.send_live_drag_cancel(source_object.id, end_system)
            return
        elif source_object not in self._live_drag_objects:
            logger_live_drag.warn('Live Drag End called on an object not being Live Dragged. Object: {}'.format(source_object))
            self.send_live_drag_cancel(source_object.id, end_system)
            return
            source_object_id = source_object.id
            if end_system == LiveDragLocation.BUILD_BUY:
                self.objects_moved_via_live_drag.add(source_object)
        else:
            self.objects_moved_via_live_drag.discard(source_object)
        self.cancel_live_drag_on_objects()
        next_object_id = None
        success = False
        inventory_item = source_object.inventoryitem_component
        if target_object is not None:
            live_drag_target_component = target_object.live_drag_target_component
            if live_drag_target_component is not None:
                success, next_object_id = live_drag_target_component.drop_live_drag_object(source_object, self._live_drag_is_stack)
            else:
                if source_object.parent_object() is target_object:
                    success = True
                else:
                    if source_object.parent_object() is None and location is not None:
                        inventory_item = source_object.inventoryitem_component
                        if inventory_item is not None:
                            if inventory_item.is_in_inventory():
                                success, next_object_id = self.remove_drag_object_and_get_next_item(source_object)
                        source_object.set_location(location)
                    else:
                        logger_live_drag.error('Live Drag Target Component missing on object: {} and {} cannot be slotted into it.'.format(target_object, source_object))
                        success = False
        else:
            if not (inventory_item is not None and inventory_item.is_in_inventory()):
                if location is not None:
                    source_object.set_location(location)
                success, next_object_id = self.remove_drag_object_and_get_next_item(source_object)
            else:
                success = True
        if location is not None:
            source_object.set_location(location)
        elif success:
            if gsi_handlers.live_drag_handlers.live_drag_archiver.enabled:
                gsi_handlers.live_drag_handlers.archive_live_drag('End', 'Operation',
                  (LiveDragLocation.GAMEPLAY_SCRIPT),
                  end_system,
                  live_drag_object_id=source_object_id,
                  live_drag_target=target_object)
            if not self._live_drag_is_stack:
                next_object_id = None
            op = distributor.ops.LiveDragEnd(source_object_id, self._live_drag_start_system, end_system, next_object_id)
            distributor_system = Distributor.instance()
            distributor_system.add_op_with_no_owner(op)
            self._live_drag_objects = []
            self._live_drag_start_system = LiveDragLocation.INVALID
            self._live_drag_is_stack = False
        else:
            self.send_live_drag_cancel(source_object_id, end_system)

    def cancel_live_drag(self, live_drag_object, end_system=LiveDragLocation.INVALID):
        live_drag_component = live_drag_object.live_drag_component
        if live_drag_component is None:
            logger_live_drag.warn('Live Drag Cancel called on an object with no Live Drag Component. Object: {}'.format(live_drag_object))
            self.send_live_drag_cancel(live_drag_object.id)
            return
        elif live_drag_component.live_drag_state == LiveDragState.NOT_LIVE_DRAGGING:
            logger_live_drag.warn('Live Drag Cancel called on an object not being Live Dragged. Object: {}'.format(live_drag_object))
        else:
            self.cancel_live_drag_on_objects()
        self.send_live_drag_cancel(live_drag_object.id, end_system)

    def sell_live_drag_object(self, live_drag_object, currency_type, end_system=LiveDragLocation.INVALID):
        live_drag_component = live_drag_object.live_drag_component
        if not (live_drag_component is None or live_drag_object.definition.get_is_deletable()):
            logger_live_drag.error("Live Drag Sell called on object with no Live Drag Component or can't be deleted. Object: {}".format(live_drag_object))
            self.send_live_drag_cancel(live_drag_object.id, end_system)
            return

        def sell_response(dialog):
            op = distributor.ops.LiveDragEnd((live_drag_object.id), (self._live_drag_start_system), end_system, next_stack_object_id=None)
            distributor_system = Distributor.instance()
            distributor_system.add_op_with_no_owner(op)
            if not dialog.accepted:
                self.cancel_live_drag_on_objects()
                return
                value = int(self.get_live_drag_object_value(live_drag_object, self._live_drag_is_stack))
                for child_object in live_drag_object.get_all_children_gen():
                    value += self.get_live_drag_object_value(child_object) if child_object.definition.get_is_deletable() else 0

                object_tags = set()
                if self._live_drag_is_stack:
                    _, stack_items = self._get_stack_items_from_drag_object(live_drag_object, remove=True, is_stack=True)
                    for item in stack_items:
                        live_drag_component = item.live_drag_component
                        live_drag_component.cancel_live_dragging(should_reset=False)
                        item.base_value = 0
                        item.set_stack_count(0)
                        object_tags.update(item.get_tags())
                        item.destroy(source=item, cause='Selling stack of live drag objects.')

            else:
                live_drag_object.live_drag_component.cancel_live_dragging(should_reset=False)
                object_tags.update(live_drag_object.get_tags())
                if live_drag_object.is_in_inventory():
                    self.remove_drag_object_and_get_next_item(live_drag_object)
                else:
                    live_drag_object.remove_from_client()
                object_tags = frozenset(object_tags)
                live_drag_object.base_value = 0
                live_drag_object.destroy(source=live_drag_object, cause='Selling live drag object.')
            services.active_household().add_currency_amount(currency_type, value, (Consts_pb2.TELEMETRY_OBJECT_SELL), (self.active_sim), tags=object_tags)
            self._live_drag_objects = []
            self._live_drag_start_system = LiveDragLocation.INVALID
            self._live_drag_is_stack = False
            self._live_drag_sell_dialog_active = False

        favorites_tracker = self.active_sim_info.favorites_tracker
        if favorites_tracker and favorites_tracker.is_favorite_stack(live_drag_object):
            dialog = LiveDragTuning.LIVE_DRAG_SELL_FAVORITE_DIALOG(owner=live_drag_object)
        else:
            if self._live_drag_is_stack:
                dialog = LiveDragTuning.LIVE_DRAG_SELL_STACK_DIALOG(owner=live_drag_object)
            else:
                dialog = LiveDragTuning.LIVE_DRAG_SELL_DIALOG(owner=live_drag_object)
        dialog.show_dialog(on_response=sell_response)
        self._live_drag_sell_dialog_active = True

    def send_live_drag_cancel(self, live_drag_object_id, live_drag_end_system=LiveDragLocation.INVALID):
        if gsi_handlers.live_drag_handlers.live_drag_archiver.enabled:
            gsi_handlers.live_drag_handlers.archive_live_drag('Cancel', 'Operation',
              (LiveDragLocation.GAMEPLAY_SCRIPT),
              live_drag_end_system,
              live_drag_object_id=live_drag_object_id)
        op = distributor.ops.LiveDragCancel(live_drag_object_id, self._live_drag_start_system, live_drag_end_system)
        distributor_system = Distributor.instance()
        distributor_system.add_op_with_no_owner(op)
        if not self._live_drag_sell_dialog_active:
            self._live_drag_objects = []
            self._live_drag_start_system = LiveDragLocation.INVALID
            self._live_drag_is_stack = False

    def on_add(self):
        if self._account is not None:
            self._account.register_client(self)
        for sim_info in self._selectable_sims:
            self.on_sim_added_to_skewer(sim_info)

        distributor = Distributor.instance()
        distributor.add_object(self)
        distributor.add_client(self)
        self.send_selectable_sims_update()
        self.selectable_sims.add_watcher(self, self.send_selectable_sims_update)

    def on_remove(self):
        if self.active_sim is not None:
            self._set_active_sim_without_field_distribution(None)
        if self._account is not None:
            self._account.unregister_client(self)
        for sim_info in self._selectable_sims:
            self.on_sim_removed_from_skewer(sim_info)

        self.selectable_sims.remove_watcher(self)
        distributor = Distributor.instance()
        distributor.remove_client(self)
        self._selectable_sims = None
        self.active = False

    def get_objects_in_view_gen(self):
        for manager in services.client_object_managers():
            for obj in manager.get_all_for_distribution():
                yield obj

    def notify_active_sim_changed(self, old_sim, new_sim_info=None):
        new_sim = new_sim_info.get_sim_instance() if new_sim_info is not None else None
        self._active_sim_changed(old_sim, new_sim)
        vfx_mask.notify_client_mask_update(new_sim_info)

    def _get_selector_visual_type(self, sim_info):
        if sim_info.is_baby:
            return (
             Sims_pb2.SimPB.BABY, None)
            if sim_info.is_toddler:
                if services.daycare_service().is_sim_info_at_daycare(sim_info):
                    return (
                     Sims_pb2.SimPB.AT_DAYCARE, None)
            if sim_info.household.missing_pet_tracker.is_pet_missing(sim_info):
                return (
                 Sims_pb2.SimPB.PET_MISSING, None)
            sim = sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
            for career in sim_info.careers.values():
                if career.currently_at_work:
                    if career.is_at_active_event:
                        if sim is None:
                            return (
                             Sims_pb2.SimPB.MISSING_ACTIVE_WORK, career.career_category)
                    return (
                     Sims_pb2.SimPB.AT_WORK, career.career_category)
                    if career.is_late:
                        return career.taking_day_off or (
                         Sims_pb2.SimPB.LATE_FOR_WORK, career.career_category)

            if services.get_rabbit_hole_service().should_override_selector_visual_type(sim_info.id):
                return (
                 Sims_pb2.SimPB.OTHER, None)
            if sim is not None:
                if sim.has_hidden_flags(HiddenReasonFlag.RABBIT_HOLE):
                    return (
                     Sims_pb2.SimPB.OTHER, None)
            if services.hidden_sim_service().is_hidden(sim_info.id):
                return (
                 Sims_pb2.SimPB.OTHER, None)
        else:
            active_sim_info = services.active_sim_info()
            if active_sim_info is not None:
                if sim_info.travel_group_id != active_sim_info.travel_group_id:
                    return (
                     Sims_pb2.SimPB.OTHER, None)
            tutorial_service = services.get_tutorial_service()
            if tutorial_service is not None and tutorial_service.is_sim_unselectable(sim_info):
                return (
                 Sims_pb2.SimPB.OTHER, None)
        return (
         Sims_pb2.SimPB.NORMAL, None)

    def send_selectable_sims_update(self):
        msg = Sims_pb2.UpdateSelectableSims()
        for sim_info in self._selectable_sims:
            with ProtocolBufferRollback(msg.sims) as (new_sim):
                new_sim.id = sim_info.sim_id
                if sim_info.career_tracker is None:
                    logger.error('CareerTracker is None for selectable Sim {}'.format(sim_info))
                else:
                    career = sim_info.career_tracker.get_currently_at_work_career()
                    new_sim.at_work = career is not None and not career.is_at_active_event
                new_sim.is_selectable = sim_info.get_is_enabled_in_skewer()
                selector_visual_type, career_category = self._get_selector_visual_type(sim_info)
                new_sim.selector_visual_type = selector_visual_type
                if career_category is not None:
                    new_sim.career_category = career_category
                new_sim.can_care_for_toddler_at_home = sim_info.can_care_for_toddler_at_home
                if not sim_info.is_instanced(allow_hidden_flags=ALL_HIDDEN_REASONS):
                    new_sim.instance_info.zone_id = sim_info.zone_id
                    new_sim.instance_info.world_id = sim_info.world_id
                    new_sim.firstname = sim_info.first_name
                    new_sim.lastname = sim_info.last_name
                    zone_data_proto = services.get_persistence_service().get_zone_proto_buff(sim_info.zone_id)
                    if zone_data_proto is not None:
                        new_sim.instance_info.zone_name = zone_data_proto.name

        distributor = Distributor.instance()
        distributor.add_op_with_no_owner(GenericProtocolBufferOp(Operation.SELECTABLE_SIMS_UPDATE, msg))

    @constproperty
    def is_sim():
        return False


class SelectableSims:

    def __init__(self, client):
        self._selectable_sim_infos = []
        self.client = client
        self._watchers = defaultdict(list)
        self._can_select_pets = False

    def __iter__(self):
        return iter(sorted((self._selectable_sim_infos), key=(lambda x: (-x.species, x.age, x.age_progress)), reverse=True))

    def __contains__(self, sim_info):
        return sim_info in self._selectable_sim_infos

    def __bool__(self):
        if self._selectable_sim_infos:
            return True
        return False

    def __len__(self):
        return len(self._selectable_sim_infos)

    @property
    def can_select_pets(self):
        return self._can_select_pets

    @can_select_pets.setter
    def can_select_pets(self, value):
        self._can_select_pets = value
        self.notify_dirty()
        if not value:
            self.client.validate_selectable_sim()

    def add_selectable_sim_info(self, sim_info, send_relationship_update=True):
        if sim_info not in self._selectable_sim_infos:
            self._selectable_sim_infos.append(sim_info)
            self.client.on_sim_added_to_skewer(sim_info, send_relationship_update=send_relationship_update)
            self.notify_dirty()

    def remove_selectable_sim_info(self, sim_info):
        exists = sim_info in self._selectable_sim_infos
        if exists:
            self._selectable_sim_infos.remove(sim_info)
            self.client.on_sim_removed_from_skewer(sim_info)
            self.notify_dirty()

    def get_next_selectable(self, current_selected_sim_info):
        if not any((s.get_is_enabled_in_skewer() for s in self)):
            return
        if current_selected_sim_info is not None:
            current_selected_sim_info = current_selected_sim_info not in self._selectable_sim_infos or current_selected_sim_info.get_is_enabled_in_skewer() or None
        iterator = filter(operator.methodcaller('get_is_enabled_in_skewer'), itertools.cycle(self))
        for sim_info in iterator:
            if current_selected_sim_info is None or sim_info is current_selected_sim_info:
                return next(iterator)

    def clear_selectable_sims(self):
        removed_list = list(self._selectable_sim_infos)
        self._selectable_sim_infos = []
        for sim_info in removed_list:
            self.client.on_sim_removed_from_skewer(sim_info)

        self.notify_dirty()

    def add_watcher(self, handle, f):
        self._watchers[handle].append(f)
        return handle

    def remove_watcher(self, handle):
        del self._watchers[handle]

    def notify_dirty(self):
        for watcher in itertools.chain.from_iterable(self._watchers.values()):
            watcher()

    def get_instanced_sims(self, allow_hidden_flags=0):
        sims = []
        for sim_info in self:
            sim = sim_info.get_sim_instance(allow_hidden_flags=allow_hidden_flags)
            if sim is not None:
                sims.append(sim)

        return sims
