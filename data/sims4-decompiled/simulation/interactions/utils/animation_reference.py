# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\animation_reference.py
# Compiled at: 2021-07-20 01:21:12
# Size of source mod 2**32: 17299 bytes

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
_jump ::= JUMP_FORWARD . 
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
alias ::= IMPORT_NAME_ATTR . attributes store
alias ::= IMPORT_NAME_ATTR . store
alias37 ::= IMPORT_FROM . store
alias37 ::= IMPORT_FROM store . 
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_AND . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . expr expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr . expr expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr . expr expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr . expr expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr . expr expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr expr . expr CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr expr expr . CALL_METHOD_9
call ::= expr expr expr expr expr expr expr expr expr expr CALL_METHOD_9 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex ::= expr starred CALL_FUNCTION_EX . 
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10 . 
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
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
except ::= POP_TOP . POP_TOP POP_TOP \e_c_stmts_opt POP_EXCEPT _jump
except ::= POP_TOP . POP_TOP POP_TOP c_stmts_opt POP_EXCEPT _jump
except ::= POP_TOP . POP_TOP POP_TOP returns
except ::= POP_TOP POP_TOP . POP_TOP \e_c_stmts_opt POP_EXCEPT _jump
except ::= POP_TOP POP_TOP . POP_TOP c_stmts_opt POP_EXCEPT _jump
except ::= POP_TOP POP_TOP . POP_TOP returns
except ::= POP_TOP POP_TOP POP_TOP . c_stmts_opt POP_EXCEPT _jump
except ::= POP_TOP POP_TOP POP_TOP . returns
except ::= POP_TOP POP_TOP POP_TOP \e_c_stmts_opt . POP_EXCEPT _jump
except ::= POP_TOP POP_TOP POP_TOP c_stmts_opt . POP_EXCEPT _jump
except ::= POP_TOP POP_TOP POP_TOP c_stmts_opt POP_EXCEPT . _jump
except ::= POP_TOP POP_TOP POP_TOP c_stmts_opt POP_EXCEPT _jump . 
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY \e_come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM except_stmts come_froms END_FINALLY come_from_opt
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_return
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_return
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . come_froms END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts END_FINALLY . 
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_return ::= POP_TOP . POP_TOP POP_TOP returns
except_return ::= POP_TOP POP_TOP . POP_TOP returns
except_return ::= POP_TOP POP_TOP POP_TOP . returns
except_stmt ::= except . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
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
expr ::= call_ex . 
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
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
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
import ::= LOAD_CONST LOAD_CONST . alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST . importlist37 store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST importlist37 . store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST importlist37 store . POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST importlist37 store POP_TOP . 
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR . importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR importlist37 . POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP . 
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST . import_from_attr37 store POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST import_from_attr37 . store POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST import_from_attr37 store . POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST import_from_attr37 store POP_TOP . 
import_from_attr37 ::= IMPORT_NAME_ATTR . IMPORT_FROM
import_from_attr37 ::= IMPORT_NAME_ATTR IMPORT_FROM . 
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR . IMPORT_STAR
import_one ::= importlists . ROT_TWO IMPORT_FROM
import_one ::= importlists . ROT_TWO POP_TOP IMPORT_FROM
importattr37 ::= IMPORT_NAME_ATTR . IMPORT_FROM
importattr37 ::= IMPORT_NAME_ATTR IMPORT_FROM . 
importlist37 ::= alias37 . 
importlist37 ::= importattr37 . 
importlist37 ::= importlist37 . alias37
importlists ::= importlist37 . 
importlists ::= importlists . importlist37
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
importmultiple ::= LOAD_CONST LOAD_CONST . alias imports_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_0 ::= BUILD_MAP_0 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_10
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_5
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_5 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
lstmt ::= stmt . 
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
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
starred ::= expr . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= import_from37 . 
stmt ::= import_from_as37 . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
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
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler \e_opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . jump_excepts come_from_except_clauses
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . opt_come_from_except
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler \e_opt_come_from_except . 
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler opt_come_from_except . 
try_except36 ::= SETUP_EXCEPT . returns except_handler36 \e_opt_come_from_except
try_except36 ::= SETUP_EXCEPT . returns except_handler36 opt_come_from_except
try_except36 ::= SETUP_EXCEPT . suite_stmts
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts . 
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 \e_come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler36 come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 . come_from_opt
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 \e_come_from_opt . 
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suite jump_excepts come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_from_except_clauses
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite come_froms
tryelsestmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suite jump_excepts come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler else_suitel come_from_except_clauses
tryelsestmtl ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . else_suitel come_from_except_clauses
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT . suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT \e_suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt . POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK . except_handler COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler . COME_FROM else_suitel opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel \e_opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM . else_suitel opt_come_from_except
tuple ::= expr . expr expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr . expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr . expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr expr . expr expr BUILD_TUPLE_6
tuple ::= expr expr expr expr expr . expr BUILD_TUPLE_6
tuple ::= expr expr expr expr expr expr . BUILD_TUPLE_6
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
   
 L. 162       524  LOAD_FAST                'add_participant_constraint'
                 526  LOAD_FAST                'target_participant_type'
                 528  LOAD_FAST                'animation_constraint_target'
                 530  CALL_FUNCTION_2       2  '2 positional arguments'
                 532  POP_TOP          
                 534  JUMP_BACK            34  'to 34'
                 536  POP_BLOCK        
->             538_0  COME_FROM_LOOP       22  '22'
from collections import defaultdict
from animation import get_throwaway_animation_context
from animation.asm import create_asm
from interactions import ParticipantType
from interactions.constraints import RequiredSlotSingle, create_constraint_set, Nowhere
from native.animation import ASM_ACTORTYPE_SIM
from sims4 import reload
from sims4.tuning.tunable import TunableReferenceFactory, TunableSingletonFactory
from singletons import DEFAULT
import animation.asm, caches, interactions.interaction_instance_manager, services, sims4.log
logger = sims4.log.Logger('Animation')
with reload.protected(globals()):
    _animation_reference_usage = defaultdict((lambda: defaultdict((lambda: 0))))

def get_animation_reference_usage():
    return _animation_reference_usage


class TunableAnimationReference(TunableReferenceFactory):

    @staticmethod
    def get_default_callback(interaction_asm_type):

        def callback--- This code section failed: ---

 L.  52         0  LOAD_DEREF               'cls'
                2  LOAD_CONST               None
                4  COMPARE_OP               is
                6  POP_JUMP_IF_FALSE    12  'to 12'

 L.  53         8  LOAD_CONST               None
               10  RETURN_VALUE     
             12_0  COME_FROM             6  '6'

 L.  55        12  BUILD_MAP_0           0 
               14  STORE_DEREF              'participant_constraint_lists'

 L.  56        16  LOAD_FAST                'factory'
               18  LOAD_ATTR                run_in_sequence
               20  STORE_DEREF              'run_in_sequence'

 L.  58     22_24  SETUP_LOOP          538  'to 538'
               26  LOAD_FAST                'factory'
               28  LOAD_METHOD              animation_element_gen
               30  CALL_METHOD_0         0  '0 positional arguments'
               32  GET_ITER         
             34_0  COME_FROM           494  '494'
             34_1  COME_FROM           488  '488'
             34_2  COME_FROM           442  '442'
             34_3  COME_FROM           318  '318'
            34_36  FOR_ITER            536  'to 536'
               38  STORE_FAST               'animation_element_factory'

 L.  59        40  LOAD_FAST                'animation_element_factory'
               42  CALL_FUNCTION_0       0  '0 positional arguments'
               44  STORE_FAST               'animation_element'

 L.  60        46  LOAD_FAST                'animation_element'
               48  LOAD_ATTR                asm_key
               50  STORE_FAST               'asm_key'

 L.  61        52  LOAD_FAST                'animation_element'
               54  LOAD_ATTR                actor_name
               56  STORE_FAST               'actor_name'

 L.  62        58  LOAD_FAST                'animation_element'
               60  LOAD_ATTR                target_name
               62  STORE_FAST               'target_name'

 L.  63        64  LOAD_FAST                'animation_element'
               66  LOAD_ATTR                carry_target_name
               68  STORE_FAST               'carry_target_name'

 L.  64        70  LOAD_FAST                'animation_element'
               72  LOAD_ATTR                create_target_name
               74  STORE_FAST               'create_target_name'

 L.  65        76  LOAD_FAST                'animation_element'
               78  LOAD_ATTR                initial_state
               80  STORE_FAST               'initial_state'

 L.  66        82  LOAD_FAST                'animation_element'
               84  LOAD_ATTR                begin_states
               86  STORE_FAST               'begin_states'

 L.  67        88  LOAD_FAST                'animation_element'
               90  LOAD_ATTR                end_states
               92  STORE_FAST               'end_states'

 L.  68        94  LOAD_FAST                'animation_element'
               96  LOAD_ATTR                base_object_name
               98  STORE_FAST               'base_object_name'

 L.  69       100  LOAD_FAST                'overrides'
              102  CALL_FUNCTION_0       0  '0 positional arguments'
              104  STORE_FAST               'instance_overrides'

 L.  70       106  LOAD_FAST                'animation_element'
              108  LOAD_ATTR                overrides
              110  LOAD_FAST                'instance_overrides'
              112  LOAD_CONST               ('overrides',)
              114  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              116  STORE_FAST               'total_overrides'

 L.  78       118  LOAD_DEREF               'cls'
              120  LOAD_METHOD              register_tuned_animation
              122  LOAD_DEREF               'interaction_asm_type'
              124  LOAD_FAST                'asm_key'

 L.  79       126  LOAD_FAST                'actor_name'
              128  LOAD_FAST                'target_name'
              130  LOAD_FAST                'carry_target_name'

 L.  80       132  LOAD_FAST                'create_target_name'
              134  LOAD_FAST                'total_overrides'

 L.  81       136  LOAD_FAST                'actor_participant_type'

 L.  82       138  LOAD_FAST                'target_participant_type'
              140  CALL_METHOD_9         9  '9 positional arguments'
              142  POP_TOP          

 L.  84       144  LOAD_FAST                'animation_element_factory'
              146  LOAD_ATTR                _child_animations
              148  POP_JUMP_IF_FALSE   176  'to 176'

 L.  85       150  SETUP_LOOP          176  'to 176'
              152  LOAD_FAST                'animation_element_factory'
              154  LOAD_ATTR                _child_animations
              156  GET_ITER         
              158  FOR_ITER            174  'to 174'
              160  STORE_FAST               'child_args'

 L.  86       162  LOAD_DEREF               'cls'
              164  LOAD_ATTR                register_tuned_animation
              166  LOAD_FAST                'child_args'
              168  CALL_FUNCTION_EX      0  'positional arguments only'
              170  POP_TOP          
              172  JUMP_BACK           158  'to 158'
              174  POP_BLOCK        
            176_0  COME_FROM_LOOP      150  '150'
            176_1  COME_FROM           148  '148'

 L.  93       176  LOAD_GLOBAL              interactions
              178  LOAD_ATTR                interaction_instance_manager
              180  LOAD_ATTR                BUILD_AC_CACHE
              182  POP_JUMP_IF_TRUE    228  'to 228'

 L.  94       184  LOAD_DEREF               'cls'
              186  LOAD_ATTR                resource_key
              188  LOAD_GLOBAL              sims4
              190  LOAD_ATTR                resources
              192  LOAD_ATTR                localwork_no_groupid
              194  COMPARE_OP               not-in
              196  POP_JUMP_IF_FALSE   228  'to 228'

 L.  95       198  LOAD_FAST                'asm_key'
              200  LOAD_GLOBAL              sims4
              202  LOAD_ATTR                resources
              204  LOAD_ATTR                localwork_no_groupid
              206  COMPARE_OP               not-in
              208  POP_JUMP_IF_FALSE   228  'to 228'

 L.  96       210  LOAD_GLOBAL              caches
              212  LOAD_ATTR                USE_ACC_AND_BCC
              214  LOAD_GLOBAL              caches
              216  LOAD_ATTR                AccBccUsage
              218  LOAD_ATTR                ACC
              220  BINARY_AND       
              222  POP_JUMP_IF_FALSE   228  'to 228'

 L.  97       224  LOAD_CONST               None
              226  RETURN_VALUE     
            228_0  COME_FROM           222  '222'
            228_1  COME_FROM           208  '208'
            228_2  COME_FROM           196  '196'
            228_3  COME_FROM           182  '182'

 L.  99       228  LOAD_FAST                'animation_element_factory'
              230  LOAD_ATTR                _child_constraints
          232_234  POP_JUMP_IF_FALSE   262  'to 262'

 L. 100       236  SETUP_LOOP          262  'to 262'
              238  LOAD_FAST                'animation_element_factory'
              240  LOAD_ATTR                _child_constraints
              242  GET_ITER         
              244  FOR_ITER            260  'to 260'
              246  STORE_FAST               'child_args'

 L. 101       248  LOAD_DEREF               'cls'
              250  LOAD_ATTR                add_auto_constraint
              252  LOAD_FAST                'child_args'
              254  CALL_FUNCTION_EX      0  'positional arguments only'
              256  POP_TOP          
              258  JUMP_BACK           244  'to 244'
              260  POP_BLOCK        
            262_0  COME_FROM_LOOP      236  '236'
            262_1  COME_FROM           232  '232'

 L. 103       262  LOAD_CONST               0
              264  LOAD_CONST               ('InteractionAsmType',)
              266  IMPORT_NAME_ATTR         animation.animation_constants
              268  IMPORT_FROM              InteractionAsmType
              270  STORE_DEREF              'InteractionAsmType'
              272  POP_TOP          

 L. 104       274  LOAD_DEREF               'interaction_asm_type'
              276  LOAD_DEREF               'InteractionAsmType'
              278  LOAD_ATTR                Interaction
              280  COMPARE_OP               ==
          282_284  POP_JUMP_IF_TRUE    320  'to 320'

 L. 105       286  LOAD_DEREF               'interaction_asm_type'
              288  LOAD_DEREF               'InteractionAsmType'
              290  LOAD_ATTR                Canonical
              292  COMPARE_OP               ==
          294_296  POP_JUMP_IF_TRUE    320  'to 320'

 L. 106       298  LOAD_DEREF               'interaction_asm_type'
              300  LOAD_DEREF               'InteractionAsmType'
              302  LOAD_ATTR                Outcome
              304  COMPARE_OP               ==
          306_308  POP_JUMP_IF_TRUE    320  'to 320'

 L. 107       310  LOAD_DEREF               'interaction_asm_type'
              312  LOAD_DEREF               'InteractionAsmType'
              314  LOAD_ATTR                Response
              316  COMPARE_OP               ==
              318  POP_JUMP_IF_FALSE    34  'to 34'
            320_0  COME_FROM           306  '306'
            320_1  COME_FROM           294  '294'
            320_2  COME_FROM           282  '282'

 L. 108       320  LOAD_CONST               0
              322  LOAD_CONST               ('create_animation_constraint',)
              324  IMPORT_NAME_ATTR         interactions.constraints
              326  IMPORT_FROM              create_animation_constraint
              328  STORE_FAST               'create_animation_constraint'
              330  POP_TOP          

 L. 110       332  LOAD_CLOSURE             'InteractionAsmType'
              334  LOAD_CLOSURE             'cls'
              336  LOAD_CLOSURE             'interaction_asm_type'
              338  LOAD_CLOSURE             'participant_constraint_lists'
              340  LOAD_CLOSURE             'run_in_sequence'
              342  BUILD_TUPLE_5         5 
              344  LOAD_CODE                <code_object add_participant_constraint>
              346  LOAD_STR                 'TunableAnimationReference.get_default_callback.<locals>.callback.<locals>.add_participant_constraint'
              348  MAKE_FUNCTION_8          'closure'
              350  STORE_FAST               'add_participant_constraint'

 L. 128       352  LOAD_CONST               None
              354  STORE_FAST               'animation_constraint_actor'

 L. 130       356  SETUP_EXCEPT        390  'to 390'

 L. 131       358  LOAD_FAST                'create_animation_constraint'

 L. 132       360  LOAD_FAST                'asm_key'
              362  LOAD_FAST                'actor_name'
              364  LOAD_FAST                'target_name'
              366  LOAD_FAST                'carry_target_name'

 L. 133       368  LOAD_FAST                'create_target_name'
              370  LOAD_FAST                'initial_state'
              372  LOAD_FAST                'begin_states'
              374  LOAD_FAST                'end_states'

 L. 134       376  LOAD_FAST                'total_overrides'
              378  LOAD_FAST                'base_object_name'
              380  LOAD_CONST               ('base_object_name',)
              382  CALL_FUNCTION_KW_10    10  '10 total positional and keyword args'
              384  STORE_FAST               'animation_constraint_actor'
              386  POP_BLOCK        
              388  JUMP_FORWARD        426  'to 426'
            390_0  COME_FROM_EXCEPT    356  '356'

 L. 135       390  POP_TOP          
              392  POP_TOP          
              394  POP_TOP          

 L. 140       396  LOAD_DEREF               'interaction_asm_type'
              398  LOAD_DEREF               'InteractionAsmType'
              400  LOAD_ATTR                Outcome
              402  COMPARE_OP               !=
          404_406  POP_JUMP_IF_FALSE   420  'to 420'

 L. 141       408  LOAD_GLOBAL              logger
              410  LOAD_METHOD              exception
              412  LOAD_STR                 'Exception while processing tuning for {}'
              414  LOAD_DEREF               'cls'
              416  CALL_METHOD_2         2  '2 positional arguments'
              418  POP_TOP          
            420_0  COME_FROM           404  '404'
              420  POP_EXCEPT       
              422  JUMP_FORWARD        426  'to 426'
              424  END_FINALLY      
            426_0  COME_FROM           422  '422'
            426_1  COME_FROM           388  '388'

 L. 143       426  LOAD_FAST                'add_participant_constraint'
              428  LOAD_FAST                'actor_participant_type'
              430  LOAD_FAST                'animation_constraint_actor'
              432  CALL_FUNCTION_2       2  '2 positional arguments'
              434  POP_TOP          

 L. 145       436  LOAD_FAST                'target_name'
              438  LOAD_CONST               None
              440  COMPARE_OP               is-not
              442  POP_JUMP_IF_FALSE    34  'to 34'

 L. 147       444  LOAD_GLOBAL              get_throwaway_animation_context
              446  CALL_FUNCTION_0       0  '0 positional arguments'
              448  STORE_FAST               'animation_context'

 L. 148       450  LOAD_GLOBAL              animation
              452  LOAD_ATTR                asm
              454  LOAD_ATTR                create_asm
              456  LOAD_FAST                'asm_key'
              458  LOAD_FAST                'animation_context'
              460  LOAD_FAST                'total_overrides'
              462  LOAD_ATTR                manifests
              464  LOAD_CONST               ('posture_manifest_overrides',)
              466  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              468  STORE_FAST               'asm'

 L. 149       470  LOAD_FAST                'asm'
              472  LOAD_METHOD              get_actor_definition
              474  LOAD_FAST                'target_name'
              476  CALL_METHOD_1         1  '1 positional argument'
              478  STORE_FAST               'target_actor_definition'

 L. 154       480  LOAD_FAST                'target_actor_definition'
              482  LOAD_ATTR                actor_type
              484  LOAD_GLOBAL              ASM_ACTORTYPE_SIM
              486  COMPARE_OP               ==
              488  POP_JUMP_IF_FALSE    34  'to 34'

 L. 156       490  LOAD_FAST                'target_actor_definition'
              492  LOAD_ATTR                is_virtual
              494  POP_JUMP_IF_TRUE     34  'to 34'

 L. 157       496  LOAD_FAST                'create_animation_constraint'

 L. 158       498  LOAD_FAST                'asm_key'
              500  LOAD_FAST                'target_name'
              502  LOAD_FAST                'actor_name'
              504  LOAD_FAST                'carry_target_name'

 L. 159       506  LOAD_FAST                'create_target_name'
              508  LOAD_FAST                'initial_state'
              510  LOAD_FAST                'begin_states'
              512  LOAD_FAST                'end_states'

 L. 160       514  LOAD_FAST                'total_overrides'
              516  LOAD_FAST                'base_object_name'
              518  LOAD_CONST               ('base_object_name',)
              520  CALL_FUNCTION_KW_10    10  '10 total positional and keyword args'
              522  STORE_FAST               'animation_constraint_target'

 L. 162       524  LOAD_FAST                'add_participant_constraint'
              526  LOAD_FAST                'target_participant_type'
              528  LOAD_FAST                'animation_constraint_target'
              530  CALL_FUNCTION_2       2  '2 positional arguments'
              532  POP_TOP          
              534  JUMP_BACK            34  'to 34'
              536  POP_BLOCK        
            538_0  COME_FROM_LOOP       22  '22'

 L. 164       538  LOAD_DEREF               'run_in_sequence'
          540_542  POP_JUMP_IF_TRUE    594  'to 594'
              544  LOAD_DEREF               'participant_constraint_lists'
              546  LOAD_CONST               None
              548  COMPARE_OP               is-not
          550_552  POP_JUMP_IF_FALSE   594  'to 594'

 L. 165       554  SETUP_LOOP          594  'to 594'
              556  LOAD_DEREF               'participant_constraint_lists'
              558  LOAD_METHOD              items
              560  CALL_METHOD_0         0  '0 positional arguments'
              562  GET_ITER         
              564  FOR_ITER            592  'to 592'
              566  UNPACK_SEQUENCE_2     2 
              568  STORE_FAST               'participant_type'
              570  STORE_FAST               'constraints_list'

 L. 166       572  LOAD_DEREF               'cls'
              574  LOAD_METHOD              add_auto_constraint
              576  LOAD_FAST                'participant_type'
              578  LOAD_GLOBAL              create_constraint_set
              580  LOAD_FAST                'constraints_list'
              582  CALL_FUNCTION_1       1  '1 positional argument'
              584  CALL_METHOD_2         2  '2 positional arguments'
              586  POP_TOP          
          588_590  JUMP_BACK           564  'to 564'
              592  POP_BLOCK        
            594_0  COME_FROM_LOOP      554  '554'
            594_1  COME_FROM           550  '550'
            594_2  COME_FROM           540  '540'

Parse error at or near `COME_FROM_LOOP' instruction at offset 538_0

        return callback

    def __init__(self, class_restrictions=DEFAULT, callback=DEFAULT, interaction_asm_type=DEFAULT, allow_reactionlets=True, override_animation_context=False, participant_enum_override=DEFAULT, **kwargs):
        if interaction_asm_type is DEFAULT:
            from animation.animation_constants import InteractionAsmType
            interaction_asm_type = InteractionAsmType.Interaction
        if callback is DEFAULT:
            callback = self.get_default_callback(interaction_asm_type)
        if class_restrictions is DEFAULT:
            class_restrictions = ('AnimationElement', 'AnimationElementSet')
        from animation.tunable_animation_overrides import TunableAnimationOverrides
        (super().__init__)(callback=callback, manager=services.get_instance_manager(sims4.resources.Types.ANIMATION), 
         class_restrictions=class_restrictions, 
         overrides=TunableAnimationOverrides(allow_reactionlets=allow_reactionlets, override_animation_context=override_animation_context,
  participant_enum_override=participant_enum_override,
  description='The overrides for interaction to replace the tunings on the animation elements'), **kwargs)


class TunedAnimationConstraint:

    def __init__(self, animation_ref):
        self._animation_ref = animation_ref

    def create_constraint(self, *args, **kwargs):
        animation_constraints = []
        if self._animation_ref:
            for animation_element_factory in self._animation_ref.animation_element_gen:
                animation_element = animation_element_factory()
                asm_key = animation_element.asm_key
                actor_name = animation_element.actor_name
                target_name = animation_element.target_name
                carry_target_name = animation_element.carry_target_name
                create_target_name = animation_element.create_target_name
                initial_state = animation_element.initial_state
                begin_states = animation_element.begin_states
                end_states = animation_element.end_states
                from interactions.constraints import create_animation_constraint
                animation_constraint = create_animation_constraint(asm_key, actor_name, target_name, carry_target_name, create_target_name, initial_state, begin_states, end_states, animation_element.overrides)
                animation_constraints.append(animation_constraint)

        return create_constraint_set(animation_constraints)


class TunableAnimationConstraint(TunableSingletonFactory):
    FACTORY_TYPE = TunedAnimationConstraint

    def __init__(self, description='A tunable type for creating animation-based constraints.', **kwargs):
        (super().__init__)(animation_ref=TunableAnimationReference(callback=None, description='\n                        The animation to use when generating the RequiredSlot constraint.'), **kwargs)


class TunableRoutingSlotConstraint(TunableSingletonFactory):

    class _TunedRoutingSlotConstraint:

        def __init__(self, animation_element):
            self.animation_element = animation_element

        def create_constraint(self, actor, target, **kwargs):
            if target is None:
                return Nowhere('{} is creating a RoutingSlotConstraint for a None Target.', actor)
            else:
                slot_constraints = []
                asm_key = self.animation_element.asm_key
                actor_name = self.animation_element.actor_name
                target_name = self.animation_element.target_name
                state_name = self.animation_element.begin_states[0]
                asm = create_asm(asm_key, context=(get_throwaway_animation_context()))
                asm.set_actoractor_nameactor
                asm.add_potentially_virtual_actor(actor_name, actor, target_name, target)
                asm.dirty_boundary_conditions
                if actor.is_sim:
                    age = actor.age.age_for_animation_cache
                else:
                    age = None
            boundary_conditions = asm.get_boundary_conditions_listactorstate_name
            for _, slots_to_params_entry in boundary_conditions:
                if not slots_to_params_entry:
                    continue
                slots_to_params_entry_absolute = []
                for boundary_condition_entry, param_sequences_entry in slots_to_params_entry:
                    routing_transform_entry, containment_transform, _, reference_joint_exit = boundary_condition_entry.get_transformsasmtarget
                    slots_to_params_entry_absolute.append((routing_transform_entry, reference_joint_exit, param_sequences_entry))

                slot_constraint = RequiredSlotSingle(actor, target, asm, asm_key, None, actor_name, target_name, state_name, containment_transform,
                  None, (tuple(slots_to_params_entry_absolute)), None,
                  asm_name=(asm.name), age=age)
                slot_constraints.append(slot_constraint)

            return create_constraint_set(slot_constraints)

    FACTORY_TYPE = _TunedRoutingSlotConstraint

    def __init__(self, description='A tunable type for creating animation-based constraints.', class_restrictions=DEFAULT, **kwargs):
        (super().__init__)(animation_element=TunableAnimationReference(description='\n                The animation to use when generating the RoutingSlot constraint.\n                ',
                              callback=None,
                              class_restrictions=class_restrictions), **kwargs)
