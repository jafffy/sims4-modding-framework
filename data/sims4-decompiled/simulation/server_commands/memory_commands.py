# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\memory_commands.py
# Compiled at: 2022-09-12 18:52:13
# Size of source mod 2**32: 33915 bytes

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
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
_jump ::= JUMP_FORWARD . 
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
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= BREAK_LOOP . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
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
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr . expr expr expr expr CALL_METHOD_5
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr . expr expr expr CALL_METHOD_5
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr . expr expr CALL_METHOD_5
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr expr expr expr expr . expr CALL_METHOD_5
call ::= expr expr expr expr expr expr . CALL_METHOD_5
call ::= expr expr expr expr expr expr CALL_METHOD_5 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
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
continues ::= lastl_stmt . continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
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
except_cond1 ::= DUP_TOP . expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr . COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP . jmp_false POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false . POP_TOP POP_TOP POP_TOP
except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP . POP_TOP POP_TOP
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
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store . POP_TOP \e_come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store . POP_TOP come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store POP_TOP . come_from_opt
except_cond2 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP store POP_TOP \e_come_from_opt . 
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
except_handler ::= jmp_abs . COME_FROM except_stmts \e__come_froms END_FINALLY
except_handler ::= jmp_abs . COME_FROM except_stmts _come_froms END_FINALLY
except_handler ::= jmp_abs . COME_FROM_EXCEPT except_stmts
except_handler ::= jmp_abs . COME_FROM_EXCEPT except_stmts \e__come_froms END_FINALLY
except_handler ::= jmp_abs . COME_FROM_EXCEPT except_stmts _come_froms END_FINALLY
except_handler ::= jmp_abs COME_FROM_EXCEPT . except_stmts
except_handler ::= jmp_abs COME_FROM_EXCEPT . except_stmts \e__come_froms END_FINALLY
except_handler ::= jmp_abs COME_FROM_EXCEPT . except_stmts _come_froms END_FINALLY
except_handler36 ::= JUMP_FORWARD . COME_FROM_EXCEPT except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT . except_stmts
except_handler36 ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts . 
except_return ::= POP_TOP . POP_TOP POP_TOP returns
except_return ::= POP_TOP POP_TOP . POP_TOP returns
except_return ::= POP_TOP POP_TOP POP_TOP . returns
except_stmt ::= except . 
except_stmt ::= except_cond2 . except_suite \e_come_from_opt
except_stmt ::= except_cond2 . except_suite come_from_opt
except_stmt ::= except_cond2 . except_suite_finalize
except_stmts ::= except_stmt . 
except_stmts ::= except_stmts . except_stmt
except_suite ::= \e_c_stmts_opt . COME_FROM POP_EXCEPT jump_except COME_FROM
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except
except_suite ::= \e_c_stmts_opt . POP_EXCEPT jump_except ELSE
except_suite_finalize ::= SETUP_FINALLY . c_stmts_opt except_var_finalize END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY \e_c_stmts_opt . except_var_finalize END_FINALLY _jump
except_suite_finalize ::= SETUP_FINALLY c_stmts_opt . except_var_finalize END_FINALLY _jump
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= subscript . 
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
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
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
ifstmt ::= testexpr . _ifstmts_jump
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_abs ::= JUMP_BACK . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_0 ::= BUILD_MAP_0 . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
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
stmt ::= aug_assign1 . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmtl . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= whilestmt . 
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
suite_stmts_opt ::= suite_stmts . 
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
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY suite_stmts_opt END_FINALLY
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts . JUMP_BACK else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK . else_suitel
while1elsestmt ::= setup_loop l_stmts JUMP_BACK \e__come_froms . POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK _come_froms . POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop l_stmts JUMP_BACK _come_froms POP_BLOCK . else_suitel COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts . POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts COME_FROM . JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts COME_FROM . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK . COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop l_stmts_opt JUMP_BACK . POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK else_suitel COME_FROM_LOOP
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
whilestmt ::= setup_loop testexpr . l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr . l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr . returns come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr \e_l_stmts_opt . come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt . come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . 
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP . 
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L. 274       436  POP_BLOCK        
                 438  LOAD_CONST               None
               440_0  COME_FROM_FINALLY   420  '420'
                 440  LOAD_CONST               None
                 442  STORE_FAST               'e'
                 444  DELETE_FAST              'e'
                 446  END_FINALLY      
                 448  POP_EXCEPT       
                 450  JUMP_BACK           144  'to 144'
               452_0  COME_FROM           410  '410'
                 452  END_FINALLY      
                 454  JUMP_BACK           144  'to 144'
                 456  POP_BLOCK        
               458_0  COME_FROM_LOOP      128  '128'
                 458  POP_BLOCK        
                 460  LOAD_CONST               None
               462_0  COME_FROM_WITH      108  '108'
                 462  WITH_CLEANUP_START
                 464  WITH_CLEANUP_FINISH
                 466  END_FINALLY      
import collections, gc, os, sys, time
from sims4.commands import CommandType
from sims4.utils import create_csv
from sims4.utils import create_text_file
import alarms, clock, game_services, services, sims4.commands, sims4.core_services, sims4.gsi.archive, sims4.reload, sizeof, tracemalloc
with sims4.reload.protected(globals()):
    g_log_python_memory_alarm = None

def _get_objects():
    gc.collect()
    if hasattr(sys, 'getobjects'):
        return sys.getobjects(sys.maxsize)
    return gc.get_objects()


def _find_object(obj_id):
    for obj in _get_objects():
        if obj_id == id(obj):
            return obj


def _truncate(s, max_len, cont='...'):
    if len(s) < max_len:
        return s
    return s[:max_len - len(cont)] + cont


def _print_object_info(obj, output, max_len=100, predicate=None):
    if predicate is not None:
        if not predicate(obj):
            return False
    info_str = '{0:#010x}:\t{1}\t{2}\t{3}'.format(id(obj), obj.__class__.__name__, _truncate(repr(obj), max_len), type(obj))
    if hasattr(obj, 'zone_id'):
        zone_id = getattr(obj, 'zone_id')
        info_str += '\t{:#018x}'.format(zone_id)
    output(info_str)
    return True


@sims4.commands.Command('mem.get_objects')
def get_objects(type_name=None, exact: bool=False, limit: int=1000, _connection=None):
    predicate = None
    if type_name == '*':
        type_name = None
    elif type_name is not None:
        if exact:

            def predicate(obj):
                return obj.__class__.__name__ == type_name

        else:

            def predicate(obj):
                return type_name in obj.__class__.__name__

    output = sims4.commands.Output(_connection)
    count = 0
    for obj in _get_objects():
        if _print_object_info(obj, output, predicate=predicate):
            count += 1
        if limit >= 0 and count >= limit:
            output("Terminating search after {} results (increase 'limit' to see more)".format(limit))
            break

    output('Found {} results'.format(count))
    return True


@sims4.commands.Command('mem.get_object_categories')
def get_object_categories(_connection=None):
    output = sims4.commands.Output(_connection)
    output('get_object_catagories is not supported in optimized python builds.')

    @sims4.commands.Command('mem.set_object_categories_checkpoint')
    def set_object_categories_checkpoints(_connection=None):
        global _previous_categories
        categories = collections.Counter((obj.__class__ for obj in gc.get_objects()))
        _previous_categories = dict(categories)
        return True


@sims4.commands.Command('mem.get_game_object')
def get_game_object(obj_id: int, _connection=None):
    output = sims4.commands.Output(_connection)
    manager = services.object_manager()
    if obj_id in manager:
        obj = manager.get(obj_id)
    else:
        output('Object with id {} cannot be found.'.format(obj_id))
    _print_object_info(obj, output)
    return True


@sims4.commands.Command('mem.get_referents')
def get_referents(python_id: int, _connection=None):
    output = sims4.commands.Output(_connection)
    obj = _find_object(python_id)
    if obj is None:
        output('Object with id {0:#08x} cannot be found'.format(python_id))
        return False
    _print_object_info(obj, output)
    obj_list = gc.get_referents(obj)
    for ref_obj in obj_list:
        _print_object_info(ref_obj, output)

    output('Found {} results'.format(len(obj_list)))
    return True


@sims4.commands.Command('mem.get_referrers')
def get_referrers(python_id: int, _connection=None):
    output = sims4.commands.Output(_connection)
    obj = _find_object(python_id)
    if obj is None:
        output('Object with id {0:#08x} cannot be found'.format(python_id))
        return False
    _print_object_info(obj, output)
    obj_list = gc.get_referrers(obj)
    for ref_obj in obj_list:
        _print_object_info(ref_obj, output)

    output('Found {} results'.format(len(obj_list)))
    return True


def populate_all_referants(cur_obj, referer_dict):
    referrants = gc.get_referents(cur_obj)
    for referrant in referrants:
        if id(referrant) not in referer_dict:
            referer_dict[id(referrant)] = referrant
            populate_all_referants(referrant, referer_dict)


@sims4.commands.Command('mem.gc_dump')
def garbage_collector_dump--- This code section failed: ---

 L. 225         0  LOAD_GLOBAL              gc
                2  LOAD_METHOD              collect
                4  CALL_METHOD_0         0  '0 positional arguments'
                6  POP_TOP          

 L. 226         8  LOAD_GLOBAL              gc
               10  LOAD_METHOD              get_objects
               12  CALL_METHOD_0         0  '0 positional arguments'
               14  STORE_FAST               'all_gc_objects'

 L. 227        16  BUILD_MAP_0           0 
               18  STORE_FAST               'all_objects'

 L. 228        20  SETUP_LOOP           56  'to 56'
               22  LOAD_FAST                'all_gc_objects'
               24  GET_ITER         
               26  FOR_ITER             54  'to 54'
               28  STORE_FAST               'obj'

 L. 229        30  LOAD_FAST                'obj'
               32  LOAD_FAST                'all_objects'
               34  LOAD_GLOBAL              id
               36  LOAD_FAST                'obj'
               38  CALL_FUNCTION_1       1  '1 positional argument'
               40  STORE_SUBSCR     

 L. 230        42  LOAD_GLOBAL              populate_all_referants
               44  LOAD_FAST                'obj'
               46  LOAD_FAST                'all_objects'
               48  CALL_FUNCTION_2       2  '2 positional arguments'
               50  POP_TOP          
               52  JUMP_BACK            26  'to 26'
               54  POP_BLOCK        
             56_0  COME_FROM_LOOP       20  '20'

 L. 232        56  LOAD_CONST               0
               58  STORE_FAST               'index'

 L. 233        60  LOAD_STR                 'python_mem_dump.txt'
               62  STORE_FAST               'file_name'

 L. 234        64  SETUP_LOOP          100  'to 100'
               66  LOAD_GLOBAL              os
               68  LOAD_ATTR                path
               70  LOAD_METHOD              exists
               72  LOAD_FAST                'file_name'
               74  CALL_METHOD_1         1  '1 positional argument'
               76  POP_JUMP_IF_FALSE    98  'to 98'

 L. 235        78  LOAD_FAST                'index'
               80  LOAD_CONST               1
               82  INPLACE_ADD      
               84  STORE_FAST               'index'

 L. 236        86  LOAD_STR                 'python_mem_dump{}.txt'
               88  LOAD_METHOD              format
               90  LOAD_FAST                'index'
               92  CALL_METHOD_1         1  '1 positional argument'
               94  STORE_FAST               'file_name'
               96  JUMP_BACK            66  'to 66'
             98_0  COME_FROM            76  '76'
               98  POP_BLOCK        
            100_0  COME_FROM_LOOP       64  '64'

 L. 238       100  LOAD_GLOBAL              open
              102  LOAD_FAST                'file_name'
              104  LOAD_STR                 'w'
              106  CALL_FUNCTION_2       2  '2 positional arguments'
          108_110  SETUP_WITH          462  'to 462'
              112  STORE_FAST               'output_file'

 L. 239       114  LOAD_FAST                'output_file'
              116  LOAD_METHOD              write
              118  LOAD_STR                 'Index,Address,Size,Name,Repr\n'
              120  CALL_METHOD_1         1  '1 positional argument'
              122  POP_TOP          

 L. 240       124  LOAD_CONST               0
              126  STORE_FAST               'cur_index'

 L. 241   128_130  SETUP_LOOP          458  'to 458'
              132  LOAD_GLOBAL              sorted
              134  LOAD_FAST                'all_objects'
              136  LOAD_METHOD              keys
              138  CALL_METHOD_0         0  '0 positional arguments'
              140  CALL_FUNCTION_1       1  '1 positional argument'
              142  GET_ITER         
          144_146  FOR_ITER            456  'to 456'
              148  STORE_FAST               'key'

 L. 242       150  LOAD_FAST                'cur_index'
              152  LOAD_CONST               1
              154  INPLACE_ADD      
              156  STORE_FAST               'cur_index'

 L. 243       158  SETUP_EXCEPT        172  'to 172'

 L. 244       160  LOAD_GLOBAL              str
              162  LOAD_FAST                'key'
              164  CALL_FUNCTION_1       1  '1 positional argument'
              166  STORE_FAST               'key_str'
              168  POP_BLOCK        
              170  JUMP_FORWARD        188  'to 188'
            172_0  COME_FROM_EXCEPT    158  '158'

 L. 245       172  POP_TOP          
              174  POP_TOP          
              176  POP_TOP          

 L. 246       178  LOAD_STR                 'FAILED'
              180  STORE_FAST               'key_str'
              182  POP_EXCEPT       
              184  JUMP_FORWARD        188  'to 188'
              186  END_FINALLY      
            188_0  COME_FROM           184  '184'
            188_1  COME_FROM           170  '170'

 L. 248       188  SETUP_EXCEPT        254  'to 254'

 L. 249       190  LOAD_GLOBAL              hasattr
              192  LOAD_FAST                'all_objects'
              194  LOAD_FAST                'key'
              196  BINARY_SUBSCR    
              198  LOAD_STR                 '__name__'
              200  CALL_FUNCTION_2       2  '2 positional arguments'
              202  POP_JUMP_IF_FALSE   232  'to 232'

 L. 250       204  LOAD_STR                 '{}::{}'
              206  LOAD_METHOD              format
              208  LOAD_GLOBAL              type
              210  LOAD_FAST                'all_objects'
              212  LOAD_FAST                'key'
              214  BINARY_SUBSCR    
              216  CALL_FUNCTION_1       1  '1 positional argument'
              218  LOAD_FAST                'all_objects'
              220  LOAD_FAST                'key'
              222  BINARY_SUBSCR    
              224  LOAD_ATTR                __name__
              226  CALL_METHOD_2         2  '2 positional arguments'
              228  STORE_FAST               'name_str'
              230  JUMP_FORWARD        250  'to 250'
            232_0  COME_FROM           202  '202'

 L. 252       232  LOAD_STR                 '{}'
              234  LOAD_METHOD              format
              236  LOAD_GLOBAL              type
              238  LOAD_FAST                'all_objects'
              240  LOAD_FAST                'key'
              242  BINARY_SUBSCR    
              244  CALL_FUNCTION_1       1  '1 positional argument'
              246  CALL_METHOD_1         1  '1 positional argument'
              248  STORE_FAST               'name_str'
            250_0  COME_FROM           230  '230'
              250  POP_BLOCK        
              252  JUMP_FORWARD        270  'to 270'
            254_0  COME_FROM_EXCEPT    188  '188'

 L. 253       254  POP_TOP          
              256  POP_TOP          
              258  POP_TOP          

 L. 254       260  LOAD_STR                 'FAILED'
              262  STORE_FAST               'name_str'
              264  POP_EXCEPT       
              266  JUMP_FORWARD        270  'to 270'
              268  END_FINALLY      
            270_0  COME_FROM           266  '266'
            270_1  COME_FROM           252  '252'

 L. 256       270  SETUP_EXCEPT        294  'to 294'

 L. 257       272  LOAD_GLOBAL              str
              274  LOAD_GLOBAL              sys
              276  LOAD_METHOD              getsizeof
              278  LOAD_FAST                'all_objects'
              280  LOAD_FAST                'key'
              282  BINARY_SUBSCR    
              284  CALL_METHOD_1         1  '1 positional argument'
              286  CALL_FUNCTION_1       1  '1 positional argument'
              288  STORE_FAST               'obj_size'
              290  POP_BLOCK        
              292  JUMP_FORWARD        310  'to 310'
            294_0  COME_FROM_EXCEPT    270  '270'

 L. 258       294  POP_TOP          
              296  POP_TOP          
              298  POP_TOP          

 L. 259       300  LOAD_STR                 'FAILED'
              302  STORE_FAST               'obj_size'
              304  POP_EXCEPT       
              306  JUMP_FORWARD        310  'to 310'
              308  END_FINALLY      
            310_0  COME_FROM           306  '306'
            310_1  COME_FROM           292  '292'

 L. 261       310  SETUP_EXCEPT        358  'to 358'

 L. 262       312  LOAD_GLOBAL              str
              314  LOAD_FAST                'all_objects'
              316  LOAD_FAST                'key'
              318  BINARY_SUBSCR    
              320  CALL_FUNCTION_1       1  '1 positional argument'
              322  STORE_FAST               'repr_str'

 L. 263       324  LOAD_STR                 ''
              326  LOAD_METHOD              join
              328  LOAD_FAST                'repr_str'
              330  LOAD_METHOD              split
              332  CALL_METHOD_0         0  '0 positional arguments'
              334  CALL_METHOD_1         1  '1 positional argument'
              336  STORE_FAST               'repr_str'

 L. 264       338  LOAD_STR                 ''
              340  LOAD_METHOD              join
              342  LOAD_FAST                'repr_str'
              344  LOAD_METHOD              split
              346  LOAD_STR                 ','
              348  CALL_METHOD_1         1  '1 positional argument'
              350  CALL_METHOD_1         1  '1 positional argument'
              352  STORE_FAST               'repr_str'
              354  POP_BLOCK        
              356  JUMP_FORWARD        374  'to 374'
            358_0  COME_FROM_EXCEPT    310  '310'

 L. 265       358  POP_TOP          
              360  POP_TOP          
              362  POP_TOP          

 L. 266       364  LOAD_STR                 'FAILED'
              366  STORE_FAST               'obj_size'
              368  POP_EXCEPT       
              370  JUMP_FORWARD        374  'to 374'
              372  END_FINALLY      
            374_0  COME_FROM           370  '370'
            374_1  COME_FROM           356  '356'

 L. 268       374  SETUP_EXCEPT        404  'to 404'

 L. 269       376  LOAD_FAST                'output_file'
              378  LOAD_METHOD              write
              380  LOAD_STR                 '{},{},{},{},{}\n'
              382  LOAD_METHOD              format
              384  LOAD_FAST                'cur_index'
              386  LOAD_FAST                'key_str'
              388  LOAD_FAST                'obj_size'
              390  LOAD_FAST                'name_str'
              392  LOAD_FAST                'repr_str'
              394  CALL_METHOD_5         5  '5 positional arguments'
              396  CALL_METHOD_1         1  '1 positional argument'
              398  POP_TOP          
              400  POP_BLOCK        
              402  JUMP_BACK           144  'to 144'
            404_0  COME_FROM_EXCEPT    374  '374'

 L. 270       404  DUP_TOP          
              406  LOAD_GLOBAL              Exception
              408  COMPARE_OP               exception-match
          410_412  POP_JUMP_IF_FALSE   452  'to 452'
              414  POP_TOP          
              416  STORE_FAST               'e'
              418  POP_TOP          
              420  SETUP_FINALLY       440  'to 440'

 L. 271       422  LOAD_FAST                'e'
              424  LOAD_GLOBAL              EnvironmentError
              426  COMPARE_OP               is
          428_430  POP_JUMP_IF_FALSE   436  'to 436'

 L. 272       432  BREAK_LOOP       
              434  JUMP_FORWARD        436  'to 436'
            436_0  COME_FROM           434  '434'
            436_1  COME_FROM           428  '428'

 L. 274       436  POP_BLOCK        
              438  LOAD_CONST               None
            440_0  COME_FROM_FINALLY   420  '420'
              440  LOAD_CONST               None
              442  STORE_FAST               'e'
              444  DELETE_FAST              'e'
              446  END_FINALLY      
              448  POP_EXCEPT       
              450  JUMP_BACK           144  'to 144'
            452_0  COME_FROM           410  '410'
              452  END_FINALLY      
              454  JUMP_BACK           144  'to 144'
              456  POP_BLOCK        
            458_0  COME_FROM_LOOP      128  '128'
              458  POP_BLOCK        
              460  LOAD_CONST               None
            462_0  COME_FROM_WITH      108  '108'
              462  WITH_CLEANUP_START
              464  WITH_CLEANUP_FINISH
              466  END_FINALLY      

 L. 276       468  LOAD_GLOBAL              sims4
              470  LOAD_ATTR                commands
              472  LOAD_METHOD              output
              474  LOAD_STR                 'Memory Output Complete'
              476  LOAD_FAST                '_connection'
              478  CALL_METHOD_2         2  '2 positional arguments'
              480  POP_TOP          

Parse error at or near `POP_BLOCK' instruction at offset 436


@sims4.commands.Command('mem.py_gc_dump', command_type=(sims4.commands.CommandType.Automation))
def py_gc_dump(file_name=None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    gc.collect()
    labeled_roots = [
     (
      'gc', gc.get_objects())]
    output('Starting GC Dump...')
    file_name = write_out_py_tree_dump(labeled_roots, file_name, 'python_gc_dump', None, cheat_output=output, bfs=True,
      include_cycles=False)
    output_str = "Wrote Python GC Dump: '{}'".format(file_name)
    output(output_str)


@sims4.commands.Command('mem.py_tree_dump', command_type=(sims4.commands.CommandType.Automation))
def py_tree_dump(file_name=None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Gathering labeled roots...')
    labeled_roots = get_labeled_roots()
    labeled_roots.insert0('Integers', list(range(-5, 257)))
    output('Starting Tree Dump...')
    file_name = write_out_py_tree_dump(labeled_roots, file_name, 'python_tree_dump', None, cheat_output=output, bfs=True, include_cycles=False)
    output_str = "Wrote Python heap tree: '{}'".format(file_name)
    output(output_str)


@sims4.commands.Command('mem.py_garbage_dump', command_type=(sims4.commands.CommandType.Automation))
def py_gc_collect_dump(file_name=None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    old_flags = gc.get_debug()
    try:
        gc.set_debug(gc.DEBUG_SAVEALL)
        gc.collect()
    finally:
        gc.set_debug(old_flags)

    labeled_roots = [('garbage', gc.garbage)]
    allowed_ids = set((id(obj) for obj in gc.garbage))
    allowed_ids.add(id(gc.garbage))
    for obj in gc.garbage:
        allowed_ids.add(id(type(obj)))

    file_name = write_out_py_tree_dump(labeled_roots, file_name, 'python_garbage_dump', allowed_ids, bfs=False, include_cycles=True)
    output_str = "Wrote Python gc dump: '{}'".format(file_name)
    output(output_str)
    gc.garbage.clear()


def write_out_py_tree_dump(labeled_roots, file_name, default_name_base, allowed_ids, cheat_output=None, bfs=True, include_cycles=False):
    if file_name is None:
        current_time = time.strftime'%Y-%m-%d-%H-%M-%S'time.gmtime()
        file_name = '{}-{}.mem'.formatdefault_name_basecurrent_time
    if cheat_output is not None:
        cheat_output('    Getting object tree.')
    try:
        try:
            sims4.log.Logger.suppress = True
            root = sizeof.get_object_tree(labeled_roots, allowed_ids=allowed_ids, bfs=bfs,
              include_cycles=include_cycles)
        except:
            if cheat_output is not None:
                cheat_output('    exception occured {}'.format(sys.exc_info()[0]))

    finally:
        sims4.log.Logger.suppress = False

    if cheat_output is not None:
        cheat_output('    Finished Getting Tree.  Writing to file.')
    with open(file_name, 'wb') as (fd):
        sizeof.write_object_treerootfd
    del root
    gc.collect()
    return file_name


def get_labeled_roots(reverse_entries=False):
    labeled_roots = []
    from objects.definition_manager import DefinitionManager
    from sims4.tuning.instance_manager import InstanceManager
    from indexed_manager import IndexedManager
    from postures.posture_graph import PostureGraphService
    SERVICE_GROUPS = [
     (
      DefinitionManager, 'DefinitionManager'),
     (
      InstanceManager, 'TuningManager'),
     (
      IndexedManager, 'IndexedManager'),
     (
      PostureGraphService, 'PostureGraph'),
     (
      object, 'Other')]
    direction_iter = reversed if reverse_entries else iter
    zone = services.current_zone()
    service_sources = []
    if zone:
        zone_services = [source for service in zone.service_manager.services for source in iter((service.get_buckets_for_memory_tracking()))]
        service_sources.append((zone_services, 'ZoneService/'))
        game_service_list = [source for service in game_services.service_manager.services for source in iter((service.get_buckets_for_memory_tracking()))]
        service_sources.append((game_service_list, 'GameService/'))
    core_services = [source for service in sims4.core_services.service_manager.services for source in iter((service.get_buckets_for_memory_tracking()))]
    service_sources.append((core_services, 'CoreService/'))
    for source, source_name in service_sources:
        for service in direction_iter(source):
            group = source_name + _first_applicable_match(service, SERVICE_GROUPS)
            labeled_roots.append(('{1}/{0}'.formatservicegroup, service))

    for name, module in direction_iter(sorted(sys.modules.items())):
        path_root = 'Other'
        if getattr(module, '__file__', None) is not None:
            matching_paths = [path for path in sys.path if module.__file__.startswith(path)]
            if matching_paths:
                path_root = os.path.split(next(iter(matching_paths)))[-1]
                path_root = path_root.capitalize()
        group = 'Module/{}'.format(path_root)
        labeled_roots.append(('{1}/{0}'.formatnamegroup, module))

    labeled_roots.append(('GSI/Archivers/', sims4.gsi.archive.archive_data))
    return labeled_roots


def generate_summary_report(skip_atomic, reverse_entries):
    labeled_roots = get_labeled_roots(reverse_entries=reverse_entries)
    report = sizeof.report(labeled_roots, skip_atomic=skip_atomic)
    return report


def _first_applicable_match(obj, groups):
    for t, group in groups:
        if isinstance(obj, t):
            return group

    raise TypeError('No group for obj {}'.format(obj))


@sims4.commands.Command('mem.py_summary', command_type=(sims4.commands.CommandType.Automation))
def print_summary(skip_atomic: bool=False, reverse_entries: bool=False, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    report = generate_summary_report(skip_atomic, reverse_entries)
    for name, size in sorted(report.items()):
        output('{},{}'.formatnamesize)


@sims4.commands.Command('mem.py_summary_file', command_type=(sims4.commands.CommandType.Automation))
def log_summary(skip_atomic: bool=False, reverse_entries: bool=False, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    automation_output = sims4.commands.AutomationOutput(_connection)
    current_time = time.strftime'%Y-%m-%d-%H-%M-%S'time.gmtime()
    file_name = 'python_mem_summary-{}.csv'.format(current_time)
    with open(file_name, 'w') as (fd):
        fd.write('Category,Group,System,Size\n')
        report = generate_summary_report(skip_atomic, reverse_entries)
        for name, size in sorted(report.items()):
            category, group, system = name.split('/')
            fd.write('{},{},{},{}\n'.format(category, group, system, size))

    output_str = "Wrote Python memory summary to: '{}'".format(file_name)
    output(output_str)
    automation_output('MemPySummaryFile; FileName:%s' % file_name)


@sims4.commands.Command('mem.clear_merged_tuning_manager')
def clear_merged_tuning_manager(_connection=None):
    output = sims4.commands.Output(_connection)
    from sims4.tuning.merged_tuning_manager import get_manager
    get_manager().clear()
    output('Merged tuning manager cleared.  WARNING: Tuning reload may break.')


@sims4.commands.Command('mem.print_leak_chain')
def print_leak_chain(obj_address: int, recursion_depth: int=10, _connection=None):
    obj = _find_object(obj_address)
    if obj is None:
        obj = services.object_manager().get(obj_address)
    if obj is not None:
        from sims4.leak_detector import find_object_refs
        termination_points = set(services._zone_manager)
        termination_points.update(services.client_object_managers())
        find_object_refs(obj, termination_points=termination_points, recursion_depth=recursion_depth)


def _size_of_slots(n):
    if n == 0:
        return 8
    return 24 + 4 * n


def _size_of_tuple(n):
    return 28 + 4 * n


@sims4.commands.Command('mem.analyze_slots', command_type=(sims4.commands.CommandType.Automation))
def analyze_slots(verbose: bool=False, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if verbose:
        output('Collecting GC')
    gc.collect()
    if verbose:
        output('Gathering objects')
    pending = collections.deque(gc.get_objects())
    all_objects = {id(obj): obj for obj in pending}
    while pending:
        obj = pending.pop()
        referents = gc.get_referents(obj)
        for child in referents:
            if id(child) not in all_objects:
                all_objects[id(child)] = child
                pending.append(child)
                if verbose:
                    len(all_objects) % 1000000 or output('...{} pending: {}'.formatlen(all_objects)len(pending))

    if verbose:
        output('Collating types')
    type_map = collections.defaultdict(list)
    for obj in all_objects.values():
        tp = type(obj)
        type_map[tp.__module__ + '.' + tp.__qualname__].append(obj)

    del all_objects

    def write_to_file(file):
        file.write('Type,Count,Size,Each,SlotSize,SlotEach,Attribs,SlotSavings,SlotSavings(MB),__slots__\n')
        for type_name in sorted(type_map.keys()):
            objects = type_map[type_name]
            if not hasattr(objects[0], '__dict__'):
                continue
            size = 0
            attribs = set()
            if isinstance(objects[0], tuple):
                for obj in objects:
                    attribs |= set((str(name) for name in vars(obj)))
                    size += sys.getsizeof(obj)

            else:
                for obj in objects:
                    attribs |= set((str(name) for name in vars(obj)))
                    size += sys.getsizeof(obj) + sys.getsizeof(obj.__dict__)

            inst_size = size / len(objects)
            slot_inst_size = _size_of_slots(len(attribs))
            slot_size = slot_inst_size * len(objects)
            slot_savings = size - slot_size
            slots_string = str(tuple(attribs)).replace',''' if len(attribs) < 50 else '(...)'
            file.write('{},{},{},{:0.2f},{},{},{},{},{:0.2f},{}\n'.format(type_name, len(objects), size, inst_size, slot_size, slot_inst_size, len(attribs), slot_savings, slot_savings / 1048576, slots_string))

    filename = 'PyOpt_AnalyzeSlots'
    create_csv(filename, callback=write_to_file, connection=_connection)


@sims4.commands.Command('mem.record_python_memory.start', command_type=(CommandType.Automation))
def record_python_memory_start(start_time: int=150, frequency: int=120, _connection=None):
    global g_log_python_memory_alarm
    record_python_memory_stop(_connection=_connection)
    output = sims4.commands.CheatOutput(_connection)
    repeating_time_span = clock.interval_in_sim_minutes(frequency)

    def record_callback(_):
        sims4.commands.client_cheat'|memory_dump'_connection
        sims4.commands.client_cheat'|py.heapcheckpoint'_connection
        output('Recording python memory. Next attempt in {}.'.format(repeating_time_span))

    time_span = clock.interval_in_sim_minutes(start_time)
    g_log_python_memory_alarm = alarms.add_alarm(record_python_memory_start, time_span, record_callback, repeating=True,
      repeating_time_span=repeating_time_span)
    output('Recording python memory. First record will occur in {}.'.format(time_span))


@sims4.commands.Command('mem.record_python_memory.stop', command_type=(CommandType.Automation))
def record_python_memory_stop(_connection=None):
    global g_log_python_memory_alarm
    if g_log_python_memory_alarm is not None:
        alarms.cancel_alarm(g_log_python_memory_alarm)
        g_log_python_memory_alarm = None


tracemalloc.Statistic.calc_count_and_size = lambda self: (self.count, self.size)
tracemalloc.StatisticDiff.calc_count_and_size = lambda self: (self.count_diff, self.size_diff)

class SnapshotDiffAdapter:

    def __init__(self, old_snapshot, new_snapshot):
        self.old_snapshot = old_snapshot
        self.new_snapshot = new_snapshot

    def statistics(self, key_type: str, cumulative: bool=False):
        return self.new_snapshot.compare_to(self.old_snapshot, key_type, cumulative)


def tracemalloc_dump_stats_imp(snapshot, dump_traceback_stats: bool, dump_per_line_stats: bool, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if dump_per_line_stats:

        def write_statistics_to_file(file, cumulative):
            output('Getting snapshot statistics per line of code (cumulative={})...'.format(cumulative))
            stats = snapshot.statistics'lineno'cumulative
            file.write('Traceback, Size, Count\n')
            for stat in stats:
                count, size = stat.calc_count_and_size()
                if count == 0:
                    if size == 0:
                        continue
                file.write('%s, %i, %i\n' % (stat.traceback, size, count))

        create_csv('tracemalloc_lineno_stats', callback=(lambda x: write_statistics_to_file(x, False)), connection=_connection)
        create_csv('tracemalloc_lineno_cumulative_stats', callback=(lambda x: write_statistics_to_file(x, True)), connection=_connection)
    if dump_traceback_stats:

        def write_traceback_to_file(file):
            output('Getting snapshot tracebacks...')
            traceback_stats = snapshot.statistics('traceback')
            output('Writing tracebacks to file...')
            file.write('Traceback\n')
            total_traceback_size = 0
            max_traceback_depth = 0
            for stat in traceback_stats:
                count, size = stat.calc_count_and_size()
                if count == 0:
                    if size == 0:
                        continue
                file.write('Size: {} Count: {}\n'.formatsizecount)
                total_traceback_size = total_traceback_size + size
                max_traceback_depth = max(max_traceback_depth, len(stat.traceback))
                for line in stat.traceback.format():
                    file.write('{}\n'.format(line))

                file.write('\n')

            file.write('Total Size: {}\n'.format(total_traceback_size))
            file.write('Max Traceback Depth: {}\n'.format(max_traceback_depth))

        create_text_file('tracemalloc_tracebacks', callback=write_traceback_to_file, connection=_connection)


@sims4.commands.Command('mem.tracemalloc_save_snapshot', command_type=(sims4.commands.CommandType.Automation))
def tracemalloc_save_snapshot(dump_per_line_stats: bool=False, dump_traceback_stats: bool=False, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if not tracemalloc.is_tracing():
        output('Tracemalloc must be tracing to generate a snapshot. Please run the client with --python_tracemalloc=1 or run the |mem.tracemalloc_start command.')
        return
    output('Taking snapshot...')
    new_snapshot = tracemalloc.take_snapshot()
    output("Dumping snapshot in internal tracemalloc's format...")

    def write_raw_snapshot_to_file(file):
        name = file.name
        file.close()
        new_snapshot.dump(name)

    create_text_file('tracemalloc_snapshot', file_extension='raw', callback=write_raw_snapshot_to_file, connection=_connection)
    tracemalloc_dump_stats_imp(new_snapshot, dump_traceback_stats, dump_per_line_stats, _connection)
    output('Saved snapshot')


@sims4.commands.Command('mem.tracemalloc_dump_stats', command_type=(sims4.commands.CommandType.Automation))
def tracemalloc_dump_stats(snapshot_file_name, snapshot_to_compare_file_name=None, dump_traceback_stats=True, dump_per_line_stats=True, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if not os.path.isfile(snapshot_file_name):
        output("File doesn't exist: " + snapshot_file_name)
        return
    output('Loading snapshot from: ' + snapshot_file_name)
    snapshot = tracemalloc.Snapshot.load(snapshot_file_name)
    if snapshot_to_compare_file_name:
        if not os.path.isfile(snapshot_to_compare_file_name):
            output("File doesn't exist: " + snapshot_to_compare_file_name)
            return
        output('Loading snapshot from: ' + snapshot_to_compare_file_name)
        snapshot_to_compare = tracemalloc.Snapshot.load(snapshot_to_compare_file_name)
        snapshot = SnapshotDiffAdapter(snapshot_to_compare, snapshot)
    tracemalloc_dump_stats_imp(snapshot, dump_traceback_stats, dump_per_line_stats, _connection)


@sims4.commands.Command('mem.tracemalloc_start', command_type=(sims4.commands.CommandType.Automation))
def tracemalloc_start(frames: int=25, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if not tracemalloc.is_tracing():
        tracemalloc.start(frames)
        output('Tracemalloc started with {} frames'.format(frames))
    else:
        output('Tracemalloc was already started, please use mem.tracemalloc_stop before starting again')


@sims4.commands.Command('mem.tracemalloc_stop', command_type=(sims4.commands.CommandType.Automation))
def tracemalloc_stop(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    if tracemalloc.is_tracing():
        tracemalloc.stop()
        output('Tracemalloc stopped')
    else:
        output('Tracemalloc was not running')


@sims4.commands.Command('mem.tracemalloc_print_memory', command_type=(sims4.commands.CommandType.Automation))
def tracemalloc_print_memory(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    traced_memory = tracemalloc.get_traced_memory()
    output('Trace Malloc Memory: {} Traced Memory Current: {} Peak: {}'.format(tracemalloc.get_tracemalloc_memory(), traced_memory[0], traced_memory[1]))


@sims4.commands.Command('mem.debugmallocstats', command_type=(sims4.commands.CommandType.Automation))
def print_debugmallocstats(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sys._debugmallocstats()
    output('gc.get_mem_info: {}'.format(gc.get_mem_info()))
