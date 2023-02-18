# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\xml\etree\ElementTree.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 58928 bytes

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
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_ABSOLUTE . JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_BACK
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_FORWARD
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 . RAISE_VARARGS_1
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_MODULO . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_slice2 ::= expr expr BUILD_SLICE_2 . 
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
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr LOAD_CONST CALL_FUNCTION_KW_2 . 
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= kvlist_0 . 
dict ::= kvlist_1 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . 
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP come_from_opt
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
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms END_FINALLY . 
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_stmt ::= except_cond1 . except_suite \e_come_from_opt
except_stmt ::= except_cond1 . except_suite come_from_opt
except_stmt ::= except_cond1 except_suite . come_from_opt
except_stmt ::= except_cond1 except_suite \e_come_from_opt . 
except_stmt ::= except_cond1 except_suite come_from_opt . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . 
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . ELSE
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= _lambda_body . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= build_slice2 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
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
ifelsestmtc ::= testexpr c_stmts_opt JUMP_ABSOLUTE . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
iflaststmt ::= testexpr c_stmts JUMP_ABSOLUTE . 
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
import ::= LOAD_CONST LOAD_CONST . alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST . importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST . import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
importmultiple ::= LOAD_CONST LOAD_CONST . alias imports_cont
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
jump_absolute_else ::= JUMP_ABSOLUTE . ELSE
jump_absolute_else ::= JUMP_ABSOLUTE . _come_froms
jump_absolute_else ::= JUMP_ABSOLUTE \e__come_froms . 
jump_absolute_else ::= JUMP_ABSOLUTE _come_froms . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_except ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
kvlist_1 ::= expr expr BUILD_MAP_1 . 
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
lambda_body ::= LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_0
lambda_body ::= LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_0
lambda_body ::= LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_0 . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lambda_body ::= expr LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_1
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lambda_body ::= expr expr LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_3
lambda_body ::= expr expr LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_3
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_3
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_3
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
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
or ::= expr_pjit_come_from . expr
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
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
stmt ::= function_def . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
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
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 come_from_opt . 
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
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
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
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 943       406  LOAD_FAST                'write'
                 408  LOAD_STR                 '</'
                 410  LOAD_FAST                'tag'
                 412  BINARY_ADD       
                 414  LOAD_STR                 '>'
                 416  BINARY_ADD       
                 418  CALL_FUNCTION_1       1  '1 positional argument'
                 420  POP_TOP          
->               422  JUMP_FORWARD        432  'to 432'
               424_0  COME_FROM           342  '342'

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
binary_operator ::= BINARY_MODULO . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_slice2 ::= expr expr BUILD_SLICE_2 . 
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
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
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
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitel ::= l_stmts . 
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP . POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP . 
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP store POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . store POP_TOP come_from_opt
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
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms . END_FINALLY
except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts come_froms END_FINALLY . 
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_stmt ::= except_cond1 . except_suite \e_come_from_opt
except_stmt ::= except_cond1 . except_suite come_from_opt
except_stmt ::= except_cond1 except_suite . come_from_opt
except_stmt ::= except_cond1 except_suite \e_come_from_opt . 
except_stmt ::= except_cond1 except_suite come_from_opt . 
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite ::= c_stmts_opt COME_FROM . POP_EXCEPT jump_except COME_FROM
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except
except_suite ::= c_stmts_opt POP_EXCEPT . jump_except ELSE
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . 
except_suite ::= c_stmts_opt POP_EXCEPT jump_except . ELSE
except_suite ::= returns . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= build_slice2 . 
expr ::= call . 
expr ::= compare . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr ::= tuple . 
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
for_iter ::= \e__come_froms . FOR_ITER
get_iter ::= expr . GET_ITER
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
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_except ::= JUMP_FORWARD . 
jump_excepts ::= jump_except . 
jump_excepts ::= jump_excepts . jump_except
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_3
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
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
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_3
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_3
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
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
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
returns ::= _stmts return . 
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= import_from37 . 
stmt ::= import_from_as37 . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= tryelsestmtl3 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
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
try_except ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler jump_excepts . come_from_except_clauses
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
try_except36 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler36 come_from_opt . 
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
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel . opt_come_from_except
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel \e_opt_come_from_except . 
tryelsestmtl3 ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK except_handler COME_FROM else_suitel opt_come_from_except . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr BUILD_TUPLE_3 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_3 . store store store
unpack ::= UNPACK_SEQUENCE_3 store . store store
unpack ::= UNPACK_SEQUENCE_3 store store . store
unpack ::= UNPACK_SEQUENCE_3 store store store . 
unpack ::= UNPACK_SEQUENCE_4 . store store store store
unpack ::= UNPACK_SEQUENCE_4 store . store store store
unpack ::= UNPACK_SEQUENCE_4 store store . store store
unpack ::= UNPACK_SEQUENCE_4 store store store . store
unpack ::= UNPACK_SEQUENCE_4 store store store store . 
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
   
 L.1603       396  LOAD_GLOBAL              hasattr
                 398  LOAD_FAST                'self'
                 400  LOAD_ATTR                target
                 402  LOAD_STR                 'doctype'
                 404  CALL_FUNCTION_2       2  '2 positional arguments'
->             406_0  COME_FROM            80  '80'
             406_408  POP_JUMP_IF_FALSE   436  'to 436'
__all__ = [
 "'Comment'", 
 "'dump'", 
 "'Element'", "'ElementTree'", 
 "'fromstring'", 
 "'fromstringlist'", 
 "'iselement'", "'iterparse'", 
 "'parse'", "'ParseError'", 
 "'PI'", 
 "'ProcessingInstruction'", 
 "'QName'", 
 "'SubElement'", 
 "'tostring'", 
 "'tostringlist'", 
 "'TreeBuilder'", 
 "'VERSION'", 
 "'XML'", "'XMLID'", 
 "'XMLParser'", 
 "'XMLPullParser'", 
 "'register_namespace'"]
VERSION = '1.3.0'
import sys, re, warnings, io, collections, collections.abc, contextlib
from . import ElementPath

class ParseError(SyntaxError):
    pass


def iselement(element):
    return hasattr(element, 'tag')


class Element:
    tag = None
    attrib = None
    text = None
    tail = None

    def __init__(self, tag, attrib={}, **extra):
        if not isinstance(attrib, dict):
            raise TypeError('attrib must be dict, not %s' % (
             attrib.__class__.__name__,))
        attrib = attrib.copy()
        attrib.update(extra)
        self.tag = tag
        self.attrib = attrib
        self._children = []

    def __repr__(self):
        return '<%s %r at %#x>' % (self.__class__.__name__, self.tag, id(self))

    def makeelement(self, tag, attrib):
        return self.__class__(tag, attrib)

    def copy(self):
        elem = self.makeelement(self.tag, self.attrib)
        elem.text = self.text
        elem.tail = self.tail
        elem[:] = self
        return elem

    def __len__(self):
        return len(self._children)

    def __bool__(self):
        warnings.warn("The behavior of this method will change in future versions.  Use specific 'len(elem)' or 'elem is not None' test instead.",
          FutureWarning,
          stacklevel=2)
        return len(self._children) != 0

    def __getitem__(self, index):
        return self._children[index]

    def __setitem__(self, index, element):
        self._children[index] = element

    def __delitem__(self, index):
        del self._children[index]

    def append(self, subelement):
        self._assert_is_element(subelement)
        self._children.append(subelement)

    def extend(self, elements):
        for element in elements:
            self._assert_is_element(element)

        self._children.extend(elements)

    def insert(self, index, subelement):
        self._assert_is_element(subelement)
        self._children.insert(index, subelement)

    def _assert_is_element(self, e):
        if not isinstance(e, _Element_Py):
            raise TypeError('expected an Element, not %s' % type(e).__name__)

    def remove(self, subelement):
        self._children.remove(subelement)

    def getchildren(self):
        warnings.warn("This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.",
          DeprecationWarning,
          stacklevel=2)
        return self._children

    def find(self, path, namespaces=None):
        return ElementPath.find(self, path, namespaces)

    def findtext(self, path, default=None, namespaces=None):
        return ElementPath.findtext(self, path, default, namespaces)

    def findall(self, path, namespaces=None):
        return ElementPath.findall(self, path, namespaces)

    def iterfind(self, path, namespaces=None):
        return ElementPath.iterfind(self, path, namespaces)

    def clear(self):
        self.attrib.clear()
        self._children = []
        self.text = self.tail = None

    def get(self, key, default=None):
        return self.attrib.get(key, default)

    def set(self, key, value):
        self.attrib[key] = value

    def keys(self):
        return self.attrib.keys()

    def items(self):
        return self.attrib.items()

    def iter(self, tag=None):
        if tag == '*':
            tag = None
        if tag is None or self.tag == tag:
            yield self
        for e in self._children:
            yield from e.iter(tag)

    def getiterator(self, tag=None):
        warnings.warn("This method will be removed in future versions.  Use 'elem.iter()' or 'list(elem.iter())' instead.",
          PendingDeprecationWarning,
          stacklevel=2)
        return list(self.iter(tag))

    def itertext(self):
        tag = self.tag
        if not isinstance(tag, str):
            if tag is not None:
                return
        t = self.text
        if t:
            yield t
        for e in self:
            yield from e.itertext()
            t = e.tail
            if t:
                yield t


def SubElement(parent, tag, attrib={}, **extra):
    attrib = attrib.copy()
    attrib.update(extra)
    element = parent.makeelement(tag, attrib)
    parent.append(element)
    return element


def Comment(text=None):
    element = Element(Comment)
    element.text = text
    return element


def ProcessingInstruction(target, text=None):
    element = Element(ProcessingInstruction)
    element.text = target
    if text:
        element.text = element.text + ' ' + text
    return element


PI = ProcessingInstruction

class QName:

    def __init__(self, text_or_uri, tag=None):
        if tag:
            text_or_uri = '{%s}%s' % (text_or_uri, tag)
        self.text = text_or_uri

    def __str__(self):
        return self.text

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.text)

    def __hash__(self):
        return hash(self.text)

    def __le__(self, other):
        if isinstance(other, QName):
            return self.text <= other.text
        return self.text <= other

    def __lt__(self, other):
        if isinstance(other, QName):
            return self.text < other.text
        return self.text < other

    def __ge__(self, other):
        if isinstance(other, QName):
            return self.text >= other.text
        return self.text >= other

    def __gt__(self, other):
        if isinstance(other, QName):
            return self.text > other.text
        return self.text > other

    def __eq__(self, other):
        if isinstance(other, QName):
            return self.text == other.text
        return self.text == other


class ElementTree:

    def __init__(self, element=None, file=None):
        self._root = element
        if file:
            self.parse(file)

    def getroot(self):
        return self._root

    def _setroot(self, element):
        self._root = element

    def parse(self, source, parser=None):
        close_source = False
        if not hasattr(source, 'read'):
            source = open(source, 'rb')
            close_source = True
        try:
            if parser is None:
                parser = XMLParser()
                if hasattr(parser, '_parse_whole'):
                    self._root = parser._parse_whole(source)
                    return self._root
            while True:
                data = source.read(65536)
                if not data:
                    break
                parser.feed(data)

            self._root = parser.close()
            return self._root
        finally:
            if close_source:
                source.close()

    def iter(self, tag=None):
        return self._root.iter(tag)

    def getiterator(self, tag=None):
        warnings.warn("This method will be removed in future versions.  Use 'tree.iter()' or 'list(tree.iter())' instead.",
          PendingDeprecationWarning,
          stacklevel=2)
        return list(self.iter(tag))

    def find(self, path, namespaces=None):
        if path[:1] == '/':
            path = '.' + path
            warnings.warn(('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path),
              FutureWarning,
              stacklevel=2)
        return self._root.find(path, namespaces)

    def findtext(self, path, default=None, namespaces=None):
        if path[:1] == '/':
            path = '.' + path
            warnings.warn(('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path),
              FutureWarning,
              stacklevel=2)
        return self._root.findtext(path, default, namespaces)

    def findall(self, path, namespaces=None):
        if path[:1] == '/':
            path = '.' + path
            warnings.warn(('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path),
              FutureWarning,
              stacklevel=2)
        return self._root.findall(path, namespaces)

    def iterfind(self, path, namespaces=None):
        if path[:1] == '/':
            path = '.' + path
            warnings.warn(('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path),
              FutureWarning,
              stacklevel=2)
        return self._root.iterfind(path, namespaces)

    def write(self, file_or_filename, encoding=None, xml_declaration=None, default_namespace=None, method=None, *, short_empty_elements=True):
        if not method:
            method = 'xml'
        else:
            if method not in _serialize:
                raise ValueError('unknown method %r' % method)
            elif (encoding or method) == 'c14n':
                encoding = 'utf-8'
            else:
                encoding = 'us-ascii'
            enc_lower = encoding.lower()
            with _get_writer(file_or_filename, enc_lower) as (write):
                if method == 'xml' and not xml_declaration:
                    if xml_declaration is None:
                        if enc_lower not in ('utf-8', 'us-ascii', 'unicode'):
                            declared_encoding = encoding
                            if enc_lower == 'unicode':
                                import locale
                                declared_encoding = locale.getpreferredencoding()
                            write("<?xml version='1.0' encoding='%s'?>\n" % (
                             declared_encoding,))
                elif method == 'text':
                    _serialize_text(write, self._root)
                else:
                    qnames, namespaces = _namespaces(self._root, default_namespace)
                    serialize = _serialize[method]
                    serialize(write, (self._root), qnames, namespaces, short_empty_elements=short_empty_elements)

    def write_c14n(self, file):
        return self.write(file, method='c14n')


@contextlib.contextmanager
def _get_writer(file_or_filename, encoding):
    try:
        write = file_or_filename.write
    except AttributeError:
        if encoding == 'unicode':
            file = open(file_or_filename, 'w')
        else:
            file = open(file_or_filename, 'w', encoding=encoding, errors='xmlcharrefreplace')
        with file:
            yield file.write
    else:
        if encoding == 'unicode':
            yield write
        else:
            with contextlib.ExitStack() as (stack):
                if isinstance(file_or_filename, io.BufferedIOBase):
                    file = file_or_filename
                else:
                    if isinstance(file_or_filename, io.RawIOBase):
                        file = io.BufferedWriter(file_or_filename)
                        stack.callback(file.detach)
                    else:
                        file = io.BufferedIOBase()
                        file.writable = lambda: True
                        file.write = write
                        try:
                            file.seekable = file_or_filename.seekable
                            file.tell = file_or_filename.tell
                        except AttributeError:
                            pass

                        file = io.TextIOWrapper(file, encoding=encoding,
                          errors='xmlcharrefreplace',
                          newline='\n')
                        stack.callback(file.detach)
                        yield file.write


def _namespaces(elem, default_namespace=None):
    qnames = {None: None}
    namespaces = {}
    if default_namespace:
        namespaces[default_namespace] = ''

    def add_qname(qname):
        try:
            if qname[:1] == '{':
                uri, tag = qname[1:].rsplit('}', 1)
                prefix = namespaces.get(uri)
                if prefix is None:
                    prefix = _namespace_map.get(uri)
                    if prefix is None:
                        prefix = 'ns%d' % len(namespaces)
                    if prefix != 'xml':
                        namespaces[uri] = prefix
                if prefix:
                    qnames[qname] = '%s:%s' % (prefix, tag)
                else:
                    qnames[qname] = tag
            else:
                if default_namespace:
                    raise ValueError('cannot use non-qualified names with default_namespace option')
                qnames[qname] = qname
        except TypeError:
            _raise_serialization_error(qname)

    for elem in elem.iter():
        tag = elem.tag
        if isinstance(tag, QName):
            if tag.text not in qnames:
                add_qname(tag.text)
            else:
                if isinstance(tag, str):
                    if tag not in qnames:
                        add_qname(tag)
                elif tag is not None:
                    if tag is not Comment:
                        if tag is not PI:
                            _raise_serialization_error(tag)
            for key, value in elem.items():
                if isinstance(key, QName):
                    key = key.text
                if key not in qnames:
                    add_qname(key)
                if isinstance(value, QName) and value.text not in qnames:
                    add_qname(value.text)

            text = elem.text
            if isinstance(text, QName) and text.text not in qnames:
                add_qname(text.text)

    return (
     qnames, namespaces)


def _serialize_xml--- This code section failed: ---

 L. 901         0  LOAD_FAST                'elem'
                2  LOAD_ATTR                tag
                4  STORE_FAST               'tag'

 L. 902         6  LOAD_FAST                'elem'
                8  LOAD_ATTR                text
               10  STORE_FAST               'text'

 L. 903        12  LOAD_FAST                'tag'
               14  LOAD_GLOBAL              Comment
               16  COMPARE_OP               is
               18  POP_JUMP_IF_FALSE    36  'to 36'

 L. 904        20  LOAD_FAST                'write'
               22  LOAD_STR                 '<!--%s-->'
               24  LOAD_FAST                'text'
               26  BINARY_MODULO    
               28  CALL_FUNCTION_1       1  '1 positional argument'
               30  POP_TOP          
            32_34  JUMP_FORWARD        432  'to 432'
             36_0  COME_FROM            18  '18'

 L. 905        36  LOAD_FAST                'tag'
               38  LOAD_GLOBAL              ProcessingInstruction
               40  COMPARE_OP               is
               42  POP_JUMP_IF_FALSE    60  'to 60'

 L. 906        44  LOAD_FAST                'write'
               46  LOAD_STR                 '<?%s?>'
               48  LOAD_FAST                'text'
               50  BINARY_MODULO    
               52  CALL_FUNCTION_1       1  '1 positional argument'
               54  POP_TOP          
            56_58  JUMP_FORWARD        432  'to 432'
             60_0  COME_FROM            42  '42'

 L. 908        60  LOAD_FAST                'qnames'
               62  LOAD_FAST                'tag'
               64  BINARY_SUBSCR    
               66  STORE_FAST               'tag'

 L. 909        68  LOAD_FAST                'tag'
               70  LOAD_CONST               None
               72  COMPARE_OP               is
               74  POP_JUMP_IF_FALSE   128  'to 128'

 L. 910        76  LOAD_FAST                'text'
               78  POP_JUMP_IF_FALSE    92  'to 92'

 L. 911        80  LOAD_FAST                'write'
               82  LOAD_GLOBAL              _escape_cdata
               84  LOAD_FAST                'text'
               86  CALL_FUNCTION_1       1  '1 positional argument'
               88  CALL_FUNCTION_1       1  '1 positional argument'
               90  POP_TOP          
             92_0  COME_FROM            78  '78'

 L. 912        92  SETUP_LOOP          124  'to 124'
               94  LOAD_FAST                'elem'
               96  GET_ITER         
               98  FOR_ITER            122  'to 122'
              100  STORE_FAST               'e'

 L. 913       102  LOAD_GLOBAL              _serialize_xml
              104  LOAD_FAST                'write'
              106  LOAD_FAST                'e'
              108  LOAD_FAST                'qnames'
              110  LOAD_CONST               None

 L. 914       112  LOAD_FAST                'short_empty_elements'
              114  LOAD_CONST               ('short_empty_elements',)
              116  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              118  POP_TOP          
              120  JUMP_BACK            98  'to 98'
              122  POP_BLOCK        
            124_0  COME_FROM_LOOP       92  '92'
          124_126  JUMP_FORWARD        432  'to 432'
            128_0  COME_FROM            74  '74'

 L. 916       128  LOAD_FAST                'write'
              130  LOAD_STR                 '<'
              132  LOAD_FAST                'tag'
              134  BINARY_ADD       
              136  CALL_FUNCTION_1       1  '1 positional argument'
              138  POP_TOP          

 L. 917       140  LOAD_GLOBAL              list
              142  LOAD_FAST                'elem'
              144  LOAD_METHOD              items
              146  CALL_METHOD_0         0  '0 positional arguments'
              148  CALL_FUNCTION_1       1  '1 positional argument'
              150  STORE_FAST               'items'

 L. 918       152  LOAD_FAST                'items'
              154  POP_JUMP_IF_TRUE    162  'to 162'
              156  LOAD_FAST                'namespaces'
          158_160  POP_JUMP_IF_FALSE   324  'to 324'
            162_0  COME_FROM           154  '154'

 L. 919       162  LOAD_FAST                'namespaces'
              164  POP_JUMP_IF_FALSE   232  'to 232'

 L. 920       166  SETUP_LOOP          232  'to 232'
              168  LOAD_GLOBAL              sorted
              170  LOAD_FAST                'namespaces'
              172  LOAD_METHOD              items
              174  CALL_METHOD_0         0  '0 positional arguments'

 L. 921       176  LOAD_LAMBDA              '<code_object <lambda>>'
              178  LOAD_STR                 '_serialize_xml.<locals>.<lambda>'
              180  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              182  LOAD_CONST               ('key',)
              184  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              186  GET_ITER         
              188  FOR_ITER            230  'to 230'
              190  UNPACK_SEQUENCE_2     2 
              192  STORE_FAST               'v'
              194  STORE_FAST               'k'

 L. 922       196  LOAD_FAST                'k'
              198  POP_JUMP_IF_FALSE   208  'to 208'

 L. 923       200  LOAD_STR                 ':'
              202  LOAD_FAST                'k'
              204  BINARY_ADD       
              206  STORE_FAST               'k'
            208_0  COME_FROM           198  '198'

 L. 924       208  LOAD_FAST                'write'
              210  LOAD_STR                 ' xmlns%s="%s"'

 L. 925       212  LOAD_FAST                'k'

 L. 926       214  LOAD_GLOBAL              _escape_attrib
              216  LOAD_FAST                'v'
              218  CALL_FUNCTION_1       1  '1 positional argument'
              220  BUILD_TUPLE_2         2 
              222  BINARY_MODULO    
              224  CALL_FUNCTION_1       1  '1 positional argument'
              226  POP_TOP          
              228  JUMP_BACK           188  'to 188'
              230  POP_BLOCK        
            232_0  COME_FROM_LOOP      166  '166'
            232_1  COME_FROM           164  '164'

 L. 928       232  SETUP_LOOP          324  'to 324'
              234  LOAD_GLOBAL              sorted
              236  LOAD_FAST                'items'
              238  CALL_FUNCTION_1       1  '1 positional argument'
              240  GET_ITER         
              242  FOR_ITER            322  'to 322'
              244  UNPACK_SEQUENCE_2     2 
              246  STORE_FAST               'k'
              248  STORE_FAST               'v'

 L. 929       250  LOAD_GLOBAL              isinstance
              252  LOAD_FAST                'k'
              254  LOAD_GLOBAL              QName
              256  CALL_FUNCTION_2       2  '2 positional arguments'
          258_260  POP_JUMP_IF_FALSE   268  'to 268'

 L. 930       262  LOAD_FAST                'k'
              264  LOAD_ATTR                text
              266  STORE_FAST               'k'
            268_0  COME_FROM           258  '258'

 L. 931       268  LOAD_GLOBAL              isinstance
              270  LOAD_FAST                'v'
              272  LOAD_GLOBAL              QName
              274  CALL_FUNCTION_2       2  '2 positional arguments'
          276_278  POP_JUMP_IF_FALSE   292  'to 292'

 L. 932       280  LOAD_FAST                'qnames'
              282  LOAD_FAST                'v'
              284  LOAD_ATTR                text
              286  BINARY_SUBSCR    
              288  STORE_FAST               'v'
              290  JUMP_FORWARD        300  'to 300'
            292_0  COME_FROM           276  '276'

 L. 934       292  LOAD_GLOBAL              _escape_attrib
              294  LOAD_FAST                'v'
              296  CALL_FUNCTION_1       1  '1 positional argument'
              298  STORE_FAST               'v'
            300_0  COME_FROM           290  '290'

 L. 935       300  LOAD_FAST                'write'
              302  LOAD_STR                 ' %s="%s"'
              304  LOAD_FAST                'qnames'
              306  LOAD_FAST                'k'
              308  BINARY_SUBSCR    
              310  LOAD_FAST                'v'
              312  BUILD_TUPLE_2         2 
              314  BINARY_MODULO    
              316  CALL_FUNCTION_1       1  '1 positional argument'
              318  POP_TOP          
              320  JUMP_BACK           242  'to 242'
              322  POP_BLOCK        
            324_0  COME_FROM_LOOP      232  '232'
            324_1  COME_FROM           158  '158'

 L. 936       324  LOAD_FAST                'text'
          326_328  POP_JUMP_IF_TRUE    346  'to 346'
              330  LOAD_GLOBAL              len
              332  LOAD_FAST                'elem'
              334  CALL_FUNCTION_1       1  '1 positional argument'
          336_338  POP_JUMP_IF_TRUE    346  'to 346'
              340  LOAD_FAST                'short_empty_elements'
          342_344  POP_JUMP_IF_TRUE    424  'to 424'
            346_0  COME_FROM           336  '336'
            346_1  COME_FROM           326  '326'

 L. 937       346  LOAD_FAST                'write'
              348  LOAD_STR                 '>'
              350  CALL_FUNCTION_1       1  '1 positional argument'
              352  POP_TOP          

 L. 938       354  LOAD_FAST                'text'
          356_358  POP_JUMP_IF_FALSE   372  'to 372'

 L. 939       360  LOAD_FAST                'write'
              362  LOAD_GLOBAL              _escape_cdata
              364  LOAD_FAST                'text'
              366  CALL_FUNCTION_1       1  '1 positional argument'
              368  CALL_FUNCTION_1       1  '1 positional argument'
              370  POP_TOP          
            372_0  COME_FROM           356  '356'

 L. 940       372  SETUP_LOOP          406  'to 406'
              374  LOAD_FAST                'elem'
              376  GET_ITER         
              378  FOR_ITER            404  'to 404'
              380  STORE_FAST               'e'

 L. 941       382  LOAD_GLOBAL              _serialize_xml
              384  LOAD_FAST                'write'
              386  LOAD_FAST                'e'
              388  LOAD_FAST                'qnames'
              390  LOAD_CONST               None

 L. 942       392  LOAD_FAST                'short_empty_elements'
              394  LOAD_CONST               ('short_empty_elements',)
              396  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              398  POP_TOP          
          400_402  JUMP_BACK           378  'to 378'
              404  POP_BLOCK        
            406_0  COME_FROM_LOOP      372  '372'

 L. 943       406  LOAD_FAST                'write'
              408  LOAD_STR                 '</'
              410  LOAD_FAST                'tag'
              412  BINARY_ADD       
              414  LOAD_STR                 '>'
              416  BINARY_ADD       
              418  CALL_FUNCTION_1       1  '1 positional argument'
              420  POP_TOP          
              422  JUMP_FORWARD        432  'to 432'
            424_0  COME_FROM           342  '342'

 L. 945       424  LOAD_FAST                'write'
              426  LOAD_STR                 ' />'
              428  CALL_FUNCTION_1       1  '1 positional argument'
              430  POP_TOP          
            432_0  COME_FROM           422  '422'
            432_1  COME_FROM           124  '124'
            432_2  COME_FROM            56  '56'
            432_3  COME_FROM            32  '32'

 L. 946       432  LOAD_FAST                'elem'
              434  LOAD_ATTR                tail
          436_438  POP_JUMP_IF_FALSE   454  'to 454'

 L. 947       440  LOAD_FAST                'write'
              442  LOAD_GLOBAL              _escape_cdata
              444  LOAD_FAST                'elem'
              446  LOAD_ATTR                tail
              448  CALL_FUNCTION_1       1  '1 positional argument'
              450  CALL_FUNCTION_1       1  '1 positional argument'
              452  POP_TOP          
            454_0  COME_FROM           436  '436'

Parse error at or near `JUMP_FORWARD' instruction at offset 422


HTML_EMPTY = ('area', 'base', 'basefont', 'br', 'col', 'frame', 'hr', 'img', 'input',
              'isindex', 'link', 'meta', 'param')
try:
    HTML_EMPTY = set(HTML_EMPTY)
except NameError:
    pass

def _serialize_html(write, elem, qnames, namespaces, **kwargs):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write('<!--%s-->' % _escape_cdata(text))
    else:
        if tag is ProcessingInstruction:
            write('<?%s?>' % _escape_cdata(text))
        else:
            tag = qnames[tag]
            if tag is None:
                if text:
                    write(_escape_cdata(text))
                for e in elem:
                    _serialize_html(write, e, qnames, None)

            else:
                write('<' + tag)
                items = list(elem.items())
                if items or namespaces:
                    if namespaces:
                        for v, k in sorted((namespaces.items()), key=(lambda x: x[1])):
                            if k:
                                k = ':' + k
                            write(' xmlns%s="%s"' % (
                             k,
                             _escape_attrib(v)))

                    for k, v in sorted(items):
                        if isinstance(k, QName):
                            k = k.text
                        elif isinstance(v, QName):
                            v = qnames[v.text]
                        else:
                            v = _escape_attrib_html(v)
                        write(' %s="%s"' % (qnames[k], v))

                write('>')
                ltag = tag.lower()
                if text:
                    if ltag == 'script' or ltag == 'style':
                        write(text)
                    else:
                        write(_escape_cdata(text))
                for e in elem:
                    _serialize_html(write, e, qnames, None)

                if ltag not in HTML_EMPTY:
                    write('</' + tag + '>')
                if elem.tail:
                    write(_escape_cdata(elem.tail))


def _serialize_text(write, elem):
    for part in elem.itertext():
        write(part)

    if elem.tail:
        write(elem.tail)


_serialize = {'xml':_serialize_xml, 
 'html':_serialize_html, 
 'text':_serialize_text}

def register_namespace(prefix, uri):
    if re.match('ns\\d+$', prefix):
        raise ValueError('Prefix format reserved for internal use')
    for k, v in list(_namespace_map.items()):
        if k == uri or v == prefix:
            del _namespace_map[k]

    _namespace_map[uri] = prefix


_namespace_map = {
 'http://www.w3.org/XML/1998/namespace': "'xml'", 
 'http://www.w3.org/1999/xhtml': "'html'", 
 'http://www.w3.org/1999/02/22-rdf-syntax-ns#': "'rdf'", 
 'http://schemas.xmlsoap.org/wsdl/': "'wsdl'", 
 'http://www.w3.org/2001/XMLSchema': "'xs'", 
 'http://www.w3.org/2001/XMLSchema-instance': "'xsi'", 
 'http://purl.org/dc/elements/1.1/': "'dc'"}
register_namespace._namespace_map = _namespace_map

def _raise_serialization_error(text):
    raise TypeError('cannot serialize %r (type %s)' % (text, type(text).__name__))


def _escape_cdata(text):
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)


def _escape_attrib(text):
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        if '"' in text:
            text = text.replace('"', '&quot;')
        if '\r\n' in text:
            text = text.replace('\r\n', '\n')
        if '\r' in text:
            text = text.replace('\r', '\n')
        if '\n' in text:
            text = text.replace('\n', '&#10;')
        if '\t' in text:
            text = text.replace('\t', '&#09;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)


def _escape_attrib_html(text):
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        if '"' in text:
            text = text.replace('"', '&quot;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)


def tostring(element, encoding=None, method=None, *, short_empty_elements=True):
    stream = io.StringIO() if encoding == 'unicode' else io.BytesIO()
    ElementTree(element).write(stream, encoding, method=method, short_empty_elements=short_empty_elements)
    return stream.getvalue()


class _ListDataStream(io.BufferedIOBase):

    def __init__(self, lst):
        self.lst = lst

    def writable(self):
        return True

    def seekable(self):
        return True

    def write(self, b):
        self.lst.append(b)

    def tell(self):
        return len(self.lst)


def tostringlist(element, encoding=None, method=None, *, short_empty_elements=True):
    lst = []
    stream = _ListDataStream(lst)
    ElementTree(element).write(stream, encoding, method=method, short_empty_elements=short_empty_elements)
    return lst


def dump(elem):
    if not isinstance(elem, ElementTree):
        elem = ElementTree(elem)
    elem.write((sys.stdout), encoding='unicode')
    tail = elem.getroot().tail
    if not tail or tail[-1] != '\n':
        sys.stdout.write('\n')


def parse(source, parser=None):
    tree = ElementTree()
    tree.parse(source, parser)
    return tree


def iterparse(source, events=None, parser=None):
    pullparser = XMLPullParser(events=events, _parser=parser)

    def iterator():
        try:
            while True:
                yield from pullparser.read_events()
                data = source.read(16384)
                if not data:
                    break
                pullparser.feed(data)

            root = pullparser._close_and_return_root()
            yield from pullparser.read_events()
            it.root = root
        finally:
            if close_source:
                source.close()

        if False:
            yield None

    class IterParseIterator(collections.abc.Iterator):
        __next__ = iterator().__next__

    it = IterParseIterator()
    it.root = None
    del iterator
    del IterParseIterator
    close_source = False
    if not hasattr(source, 'read'):
        source = open(source, 'rb')
        close_source = True
    return it


class XMLPullParser:

    def __init__(self, events=None, *, _parser=None):
        self._events_queue = collections.deque()
        self._parser = _parser or XMLParser(target=(TreeBuilder()))
        if events is None:
            events = ('end', )
        self._parser._setevents(self._events_queue, events)

    def feed(self, data):
        if self._parser is None:
            raise ValueError('feed() called after end of stream')
        if data:
            try:
                self._parser.feed(data)
            except SyntaxError as exc:
                try:
                    self._events_queue.append(exc)
                finally:
                    exc = None
                    del exc

    def _close_and_return_root(self):
        root = self._parser.close()
        self._parser = None
        return root

    def close(self):
        self._close_and_return_root()

    def read_events(self):
        events = self._events_queue
        while events:
            event = events.popleft()
            if isinstance(event, Exception):
                raise event
            else:
                yield event


def XML(text, parser=None):
    if not parser:
        parser = XMLParser(target=(TreeBuilder()))
    parser.feed(text)
    return parser.close()


def XMLID(text, parser=None):
    if not parser:
        parser = XMLParser(target=(TreeBuilder()))
    parser.feed(text)
    tree = parser.close()
    ids = {}
    for elem in tree.iter():
        id = elem.get('id')
        if id:
            ids[id] = elem

    return (
     tree, ids)


fromstring = XML

def fromstringlist(sequence, parser=None):
    if not parser:
        parser = XMLParser(target=(TreeBuilder()))
    for text in sequence:
        parser.feed(text)

    return parser.close()


class TreeBuilder:

    def __init__(self, element_factory=None):
        self._data = []
        self._elem = []
        self._last = None
        self._tail = None
        if element_factory is None:
            element_factory = Element
        self._factory = element_factory

    def close(self):
        return self._last

    def _flush(self):
        if self._data:
            if self._last is not None:
                text = ''.join(self._data)
                if self._tail:
                    self._last.tail = text
                else:
                    self._last.text = text
            self._data = []

    def data(self, data):
        self._data.append(data)

    def start(self, tag, attrs):
        self._flush()
        self._last = elem = self._factory(tag, attrs)
        if self._elem:
            self._elem[-1].append(elem)
        self._elem.append(elem)
        self._tail = 0
        return elem

    def end(self, tag):
        self._flush()
        self._last = self._elem.pop()
        self._tail = 1
        return self._last


_sentinel = [
 'sentinel']

class XMLParser:

    def __init__(self, html=_sentinel, target=None, encoding=None):
        if html is not _sentinel:
            warnings.warn('The html argument of XMLParser() is deprecated',
              DeprecationWarning,
              stacklevel=2)
        else:
            try:
                from xml.parsers import expat
            except ImportError:
                try:
                    import pyexpat as expat
                except ImportError:
                    raise ImportError('No module named expat; use SimpleXMLTreeBuilder instead')

            parser = expat.ParserCreate(encoding, '}')
            if target is None:
                target = TreeBuilder()
            self.parser = self._parser = parser
            self.target = self._target = target
            self._error = expat.error
            self._names = {}
            parser.DefaultHandlerExpand = self._default
            if hasattr(target, 'start'):
                parser.StartElementHandler = self._start
            if hasattr(target, 'end'):
                parser.EndElementHandler = self._end
            if hasattr(target, 'data'):
                parser.CharacterDataHandler = target.data
            if hasattr(target, 'comment'):
                parser.CommentHandler = target.comment
            if hasattr(target, 'pi'):
                parser.ProcessingInstructionHandler = target.pi
            parser.buffer_text = 1
            parser.ordered_attributes = 1
            parser.specified_attributes = 1
            self._doctype = None
            self.entity = {}
            try:
                self.version = 'Expat %d.%d.%d' % expat.version_info
            except AttributeError:
                pass

    def _setevents(self, events_queue, events_to_report):
        parser = self._parser
        append = events_queue.append
        for event_name in events_to_report:
            if event_name == 'start':
                parser.ordered_attributes = 1
                parser.specified_attributes = 1

                def handler(tag, attrib_in, event=event_name, append=append, start=self._start):
                    append((event, start(tag, attrib_in)))

                parser.StartElementHandler = handler
            elif event_name == 'end':

                def handler(tag, event=event_name, append=append, end=self._end):
                    append((event, end(tag)))

                parser.EndElementHandler = handler
            elif event_name == 'start-ns':

                def handler(prefix, uri, event=event_name, append=append):
                    append((event, (prefix or '', uri or '')))

                parser.StartNamespaceDeclHandler = handler
            elif event_name == 'end-ns':

                def handler(prefix, event=event_name, append=append):
                    append((event, None))

                parser.EndNamespaceDeclHandler = handler
            else:
                raise ValueError('unknown event %r' % event_name)

    def _raiseerror(self, value):
        err = ParseError(value)
        err.code = value.code
        err.position = (value.lineno, value.offset)
        raise err

    def _fixname(self, key):
        try:
            name = self._names[key]
        except KeyError:
            name = key
            if '}' in name:
                name = '{' + name
            self._names[key] = name

        return name

    def _start(self, tag, attr_list):
        fixname = self._fixname
        tag = fixname(tag)
        attrib = {}
        if attr_list:
            for i in range(0, len(attr_list), 2):
                attrib[fixname(attr_list[i])] = attr_list[i + 1]

        return self.target.start(tag, attrib)

    def _end(self, tag):
        return self.target.end(self._fixname(tag))

    def _default--- This code section failed: ---

 L.1560         0  LOAD_FAST                'text'
                2  LOAD_CONST               None
                4  LOAD_CONST               1
                6  BUILD_SLICE_2         2 
                8  BINARY_SUBSCR    
               10  STORE_FAST               'prefix'

 L.1561        12  LOAD_FAST                'prefix'
               14  LOAD_STR                 '&'
               16  COMPARE_OP               ==
               18  POP_JUMP_IF_FALSE   176  'to 176'

 L.1563        20  SETUP_EXCEPT         34  'to 34'

 L.1564        22  LOAD_FAST                'self'
               24  LOAD_ATTR                target
               26  LOAD_ATTR                data
               28  STORE_FAST               'data_handler'
               30  POP_BLOCK        
               32  JUMP_FORWARD         54  'to 54'
             34_0  COME_FROM_EXCEPT     20  '20'

 L.1565        34  DUP_TOP          
               36  LOAD_GLOBAL              AttributeError
               38  COMPARE_OP               exception-match
               40  POP_JUMP_IF_FALSE    52  'to 52'
               42  POP_TOP          
               44  POP_TOP          
               46  POP_TOP          

 L.1566        48  LOAD_CONST               None
               50  RETURN_VALUE     
             52_0  COME_FROM            40  '40'
               52  END_FINALLY      
             54_0  COME_FROM            32  '32'

 L.1567        54  SETUP_EXCEPT         82  'to 82'

 L.1568        56  LOAD_FAST                'data_handler'
               58  LOAD_FAST                'self'
               60  LOAD_ATTR                entity
               62  LOAD_FAST                'text'
               64  LOAD_CONST               1
               66  LOAD_CONST               -1
               68  BUILD_SLICE_2         2 
               70  BINARY_SUBSCR    
               72  BINARY_SUBSCR    
               74  CALL_FUNCTION_1       1  '1 positional argument'
               76  POP_TOP          
               78  POP_BLOCK        
               80  JUMP_FORWARD        500  'to 500'
             82_0  COME_FROM_EXCEPT     54  '54'

 L.1569        82  DUP_TOP          
               84  LOAD_GLOBAL              KeyError
               86  COMPARE_OP               exception-match
               88  POP_JUMP_IF_FALSE   170  'to 170'
               90  POP_TOP          
               92  POP_TOP          
               94  POP_TOP          

 L.1570        96  LOAD_CONST               0
               98  LOAD_CONST               ('expat',)
              100  IMPORT_NAME_ATTR         xml.parsers
              102  IMPORT_FROM              expat
              104  STORE_FAST               'expat'
              106  POP_TOP          

 L.1571       108  LOAD_FAST                'expat'
              110  LOAD_METHOD              error

 L.1572       112  LOAD_STR                 'undefined entity %s: line %d, column %d'

 L.1573       114  LOAD_FAST                'text'
              116  LOAD_FAST                'self'
              118  LOAD_ATTR                parser
              120  LOAD_ATTR                ErrorLineNumber

 L.1574       122  LOAD_FAST                'self'
              124  LOAD_ATTR                parser
              126  LOAD_ATTR                ErrorColumnNumber
              128  BUILD_TUPLE_3         3 
              130  BINARY_MODULO    
              132  CALL_METHOD_1         1  '1 positional argument'
              134  STORE_FAST               'err'

 L.1576       136  LOAD_CONST               11
              138  LOAD_FAST                'err'
              140  STORE_ATTR               code

 L.1577       142  LOAD_FAST                'self'
              144  LOAD_ATTR                parser
              146  LOAD_ATTR                ErrorLineNumber
              148  LOAD_FAST                'err'
              150  STORE_ATTR               lineno

 L.1578       152  LOAD_FAST                'self'
              154  LOAD_ATTR                parser
              156  LOAD_ATTR                ErrorColumnNumber
              158  LOAD_FAST                'err'
              160  STORE_ATTR               offset

 L.1579       162  LOAD_FAST                'err'
              164  RAISE_VARARGS_1       1  'exception instance'
              166  POP_EXCEPT       
              168  JUMP_FORWARD        500  'to 500'
            170_0  COME_FROM            88  '88'
              170  END_FINALLY      
          172_174  JUMP_FORWARD        500  'to 500'
            176_0  COME_FROM            18  '18'

 L.1580       176  LOAD_FAST                'prefix'
              178  LOAD_STR                 '<'
              180  COMPARE_OP               ==
              182  POP_JUMP_IF_FALSE   210  'to 210'
              184  LOAD_FAST                'text'
              186  LOAD_CONST               None
              188  LOAD_CONST               9
              190  BUILD_SLICE_2         2 
              192  BINARY_SUBSCR    
              194  LOAD_STR                 '<!DOCTYPE'
              196  COMPARE_OP               ==
              198  POP_JUMP_IF_FALSE   210  'to 210'

 L.1581       200  BUILD_LIST_0          0 
              202  LOAD_FAST                'self'
              204  STORE_ATTR               _doctype
          206_208  JUMP_FORWARD        500  'to 500'
            210_0  COME_FROM           198  '198'
            210_1  COME_FROM           182  '182'

 L.1582       210  LOAD_FAST                'self'
              212  LOAD_ATTR                _doctype
              214  LOAD_CONST               None
              216  COMPARE_OP               is-not
          218_220  POP_JUMP_IF_FALSE   500  'to 500'

 L.1584       222  LOAD_FAST                'prefix'
              224  LOAD_STR                 '>'
              226  COMPARE_OP               ==
              228  POP_JUMP_IF_FALSE   240  'to 240'

 L.1585       230  LOAD_CONST               None
              232  LOAD_FAST                'self'
              234  STORE_ATTR               _doctype

 L.1586       236  LOAD_CONST               None
              238  RETURN_VALUE     
            240_0  COME_FROM           228  '228'

 L.1587       240  LOAD_FAST                'text'
              242  LOAD_METHOD              strip
              244  CALL_METHOD_0         0  '0 positional arguments'
              246  STORE_FAST               'text'

 L.1588       248  LOAD_FAST                'text'
          250_252  POP_JUMP_IF_TRUE    258  'to 258'

 L.1589       254  LOAD_CONST               None
              256  RETURN_VALUE     
            258_0  COME_FROM           250  '250'

 L.1590       258  LOAD_FAST                'self'
              260  LOAD_ATTR                _doctype
              262  LOAD_METHOD              append
              264  LOAD_FAST                'text'
              266  CALL_METHOD_1         1  '1 positional argument'
              268  POP_TOP          

 L.1591       270  LOAD_GLOBAL              len
              272  LOAD_FAST                'self'
              274  LOAD_ATTR                _doctype
              276  CALL_FUNCTION_1       1  '1 positional argument'
              278  STORE_FAST               'n'

 L.1592       280  LOAD_FAST                'n'
              282  LOAD_CONST               2
              284  COMPARE_OP               >
          286_288  POP_JUMP_IF_FALSE   500  'to 500'

 L.1593       290  LOAD_FAST                'self'
              292  LOAD_ATTR                _doctype
              294  LOAD_CONST               1
              296  BINARY_SUBSCR    
              298  STORE_FAST               'type'

 L.1594       300  LOAD_FAST                'type'
              302  LOAD_STR                 'PUBLIC'
              304  COMPARE_OP               ==
          306_308  POP_JUMP_IF_FALSE   354  'to 354'
              310  LOAD_FAST                'n'
              312  LOAD_CONST               4
              314  COMPARE_OP               ==
          316_318  POP_JUMP_IF_FALSE   354  'to 354'

 L.1595       320  LOAD_FAST                'self'
              322  LOAD_ATTR                _doctype
              324  UNPACK_SEQUENCE_4     4 
              326  STORE_FAST               'name'
              328  STORE_FAST               'type'
              330  STORE_FAST               'pubid'
              332  STORE_FAST               'system'

 L.1596       334  LOAD_FAST                'pubid'
          336_338  POP_JUMP_IF_FALSE   396  'to 396'

 L.1597       340  LOAD_FAST                'pubid'
              342  LOAD_CONST               1
              344  LOAD_CONST               -1
              346  BUILD_SLICE_2         2 
              348  BINARY_SUBSCR    
              350  STORE_FAST               'pubid'
              352  JUMP_FORWARD        396  'to 396'
            354_0  COME_FROM           316  '316'
            354_1  COME_FROM           306  '306'

 L.1598       354  LOAD_FAST                'type'
              356  LOAD_STR                 'SYSTEM'
              358  COMPARE_OP               ==
          360_362  POP_JUMP_IF_FALSE   392  'to 392'
              364  LOAD_FAST                'n'
              366  LOAD_CONST               3
              368  COMPARE_OP               ==
          370_372  POP_JUMP_IF_FALSE   392  'to 392'

 L.1599       374  LOAD_FAST                'self'
              376  LOAD_ATTR                _doctype
              378  UNPACK_SEQUENCE_3     3 
              380  STORE_FAST               'name'
              382  STORE_FAST               'type'
              384  STORE_FAST               'system'

 L.1600       386  LOAD_CONST               None
              388  STORE_FAST               'pubid'
              390  JUMP_FORWARD        396  'to 396'
            392_0  COME_FROM           370  '370'
            392_1  COME_FROM           360  '360'

 L.1602       392  LOAD_CONST               None
              394  RETURN_VALUE     
            396_0  COME_FROM           390  '390'
            396_1  COME_FROM           352  '352'
            396_2  COME_FROM           336  '336'

 L.1603       396  LOAD_GLOBAL              hasattr
              398  LOAD_FAST                'self'
              400  LOAD_ATTR                target
              402  LOAD_STR                 'doctype'
              404  CALL_FUNCTION_2       2  '2 positional arguments'
            406_0  COME_FROM            80  '80'
          406_408  POP_JUMP_IF_FALSE   436  'to 436'

 L.1604       410  LOAD_FAST                'self'
              412  LOAD_ATTR                target
              414  LOAD_METHOD              doctype
              416  LOAD_FAST                'name'
              418  LOAD_FAST                'pubid'
              420  LOAD_FAST                'system'
              422  LOAD_CONST               1
              424  LOAD_CONST               -1
              426  BUILD_SLICE_2         2 
              428  BINARY_SUBSCR    
              430  CALL_METHOD_3         3  '3 positional arguments'
              432  POP_TOP          
              434  JUMP_FORWARD        494  'to 494'
            436_0  COME_FROM           406  '406'

 L.1605       436  LOAD_FAST                'self'
              438  LOAD_ATTR                doctype
              440  LOAD_FAST                'self'
              442  LOAD_ATTR                _XMLParser__doctype
              444  COMPARE_OP               !=
          446_448  POP_JUMP_IF_FALSE   494  'to 494'

 L.1607       450  LOAD_FAST                'self'
              452  LOAD_METHOD              _XMLParser__doctype
              454  LOAD_FAST                'name'
              456  LOAD_FAST                'pubid'
              458  LOAD_FAST                'system'
              460  LOAD_CONST               1
              462  LOAD_CONST               -1
              464  BUILD_SLICE_2         2 
              466  BINARY_SUBSCR    
              468  CALL_METHOD_3         3  '3 positional arguments'
              470  POP_TOP          

 L.1608       472  LOAD_FAST                'self'
              474  LOAD_METHOD              doctype
              476  LOAD_FAST                'name'
              478  LOAD_FAST                'pubid'
              480  LOAD_FAST                'system'
              482  LOAD_CONST               1
              484  LOAD_CONST               -1
              486  BUILD_SLICE_2         2 
              488  BINARY_SUBSCR    
              490  CALL_METHOD_3         3  '3 positional arguments'
              492  POP_TOP          
            494_0  COME_FROM           446  '446'
            494_1  COME_FROM           434  '434'
            494_2  COME_FROM           168  '168'

 L.1609       494  LOAD_CONST               None
              496  LOAD_FAST                'self'
              498  STORE_ATTR               _doctype
            500_0  COME_FROM           286  '286'
            500_1  COME_FROM           218  '218'
            500_2  COME_FROM           206  '206'
            500_3  COME_FROM           172  '172'

Parse error at or near `COME_FROM' instruction at offset 406_0

    def doctype(self, name, pubid, system):
        warnings.warn('This method of XMLParser is deprecated.  Define doctype() method on the TreeBuilder target.', DeprecationWarning)

    _XMLParser__doctype = doctype

    def feed(self, data):
        try:
            self.parser.Parse(data, 0)
        except self._error as v:
            try:
                self._raiseerror(v)
            finally:
                v = None
                del v

    def close(self):
        try:
            self.parser.Parse('', 1)
        except self._error as v:
            try:
                self._raiseerror(v)
            finally:
                v = None
                del v

        try:
            try:
                close_handler = self.target.close
            except AttributeError:
                pass
            else:
                return close_handler()
        finally:
            del self.parser
            del self._parser
            del self.target
            del self._target


try:
    _Element_Py = Element
    from _elementtree import *
except ImportError:
    pass
