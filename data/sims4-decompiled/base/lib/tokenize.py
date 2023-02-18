# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\tokenize.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 27219 bytes

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
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assert_invert ::= testtrue LOAD_GLOBAL . RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr DUP_TOP . designList
assign ::= expr DUP_TOP designList . 
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign2 ::= expr expr ROT_TWO . store store
assign2 ::= expr expr ROT_TWO store . store
assign2 ::= expr expr ROT_TWO store store . 
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
aug_assign2 ::= expr DUP_TOP . LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_FLOOR_DIVIDE . 
binary_operator ::= BINARY_MULTIPLY . 
break ::= BREAK_LOOP . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
build_slice2 ::= expr expr BUILD_SLICE_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr expr CALL_METHOD_4
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr expr CALL_METHOD_4
call ::= expr expr expr expr . expr CALL_METHOD_4
call ::= expr expr expr expr expr . CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5 . 
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_8
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_8
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
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
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= _stmts lastl_stmt continue . 
continues ::= lastl_stmt . continue
designList ::= store . DUP_TOP designList
designList ::= store . store
designList ::= store DUP_TOP . designList
designList ::= store DUP_TOP designList . 
designList ::= store store . 
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
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= build_slice2 . 
expr ::= call . 
expr ::= compare . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr ::= tuple . 
expr ::= yield . 
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
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
get_iter ::= expr . GET_ITER
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= CONTINUE . ELSE
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_except ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
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
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr BUILD_LIST_1 . 
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr expr . BUILD_LIST_4
lstmt ::= stmt . 
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
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
set ::= expr . BUILD_SET_1
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
stmt ::= assign . 
stmt ::= assign2 . 
stmt ::= aug_assign1 . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= try_except . 
stmt ::= try_except36 . 
stmt ::= whilestmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
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
suite_stmts ::= continues . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
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
while1stmt ::= setup_loop l_stmts COME_FROM_LOOP . 
while1stmt ::= setup_loop l_stmts COME_FROM_LOOP . JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop l_stmts POP_BLOCK . COME_FROM_LOOP
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
whilestmt ::= setup_loop testexpr l_stmts_opt COME_FROM . JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK . come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms . POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . 
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK . COME_FROM_LOOP
whilestmt ::= setup_loop testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP . 
whilestmt ::= setup_loop testexpr l_stmts_opt come_froms . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
yield ::= expr . YIELD_VALUE
yield ::= expr YIELD_VALUE . 
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 561       692  SETUP_LOOP          806  'to 806'
                 694  LOAD_FAST                'column'
                 696  LOAD_FAST                'indents'
                 698  LOAD_CONST               -1
->             700_0  COME_FROM           250  '250'
                 700  BINARY_SUBSCR    
                 702  COMPARE_OP               <
             704_706  POP_JUMP_IF_FALSE   778  'to 778'
__author__ = 'Ka-Ping Yee <ping@lfw.org>'
__credits__ = 'GvR, ESR, Tim Peters, Thomas Wouters, Fred Drake, Skip Montanaro, Raymond Hettinger, Trent Nelson, Michael Foord'
from builtins import open as _builtin_open
from codecs import lookup, BOM_UTF8
import collections
from io import TextIOWrapper
from itertools import chain
import itertools as _itertools, re, sys
from token import *
cookie_re = re.compile('^[ \\t\\f]*#.*?coding[:=][ \\t]*([-\\w.]+)', re.ASCII)
blank_re = re.compile(b'^[ \\t\\f]*(?:[#\\r\\n]|$)', re.ASCII)
import token
__all__ = token.__all__ + ['tokenize', 'detect_encoding',
 'untokenize', 'TokenInfo']
del token
EXACT_TOKEN_TYPES = {
 '(': 'LPAR', 
 ')': 'RPAR', 
 '[': 'LSQB', 
 ']': 'RSQB', 
 ':': 'COLON', 
 ',': 'COMMA', 
 ';': 'SEMI', 
 '+': 'PLUS', 
 '-': 'MINUS', 
 '*': 'STAR', 
 '/': 'SLASH', 
 '|': 'VBAR', 
 '&': 'AMPER', 
 '<': 'LESS', 
 '>': 'GREATER', 
 '=': 'EQUAL', 
 '.': 'DOT', 
 '%': 'PERCENT', 
 '{': 'LBRACE', 
 '}': 'RBRACE', 
 '==': 'EQEQUAL', 
 '!=': 'NOTEQUAL', 
 '<=': 'LESSEQUAL', 
 '>=': 'GREATEREQUAL', 
 '~': 'TILDE', 
 '^': 'CIRCUMFLEX', 
 '<<': 'LEFTSHIFT', 
 '>>': 'RIGHTSHIFT', 
 '**': 'DOUBLESTAR', 
 '+=': 'PLUSEQUAL', 
 '-=': 'MINEQUAL', 
 '*=': 'STAREQUAL', 
 '/=': 'SLASHEQUAL', 
 '%=': 'PERCENTEQUAL', 
 '&=': 'AMPEREQUAL', 
 '|=': 'VBAREQUAL', 
 '^=': 'CIRCUMFLEXEQUAL', 
 '<<=': 'LEFTSHIFTEQUAL', 
 '>>=': 'RIGHTSHIFTEQUAL', 
 '**=': 'DOUBLESTAREQUAL', 
 '//': 'DOUBLESLASH', 
 '//=': 'DOUBLESLASHEQUAL', 
 '...': 'ELLIPSIS', 
 '->': 'RARROW', 
 '@': 'AT', 
 '@=': 'ATEQUAL'}

class TokenInfo(collections.namedtuple('TokenInfo', 'type string start end line')):

    def __repr__(self):
        annotated_type = '%d (%s)' % (self.type, tok_name[self.type])
        return 'TokenInfo(type=%s, string=%r, start=%r, end=%r, line=%r)' % self._replace(type=annotated_type)

    @property
    def exact_type(self):
        if self.type == OP:
            if self.string in EXACT_TOKEN_TYPES:
                return EXACT_TOKEN_TYPES[self.string]
        return self.type


def group(*choices):
    return '(' + '|'.join(choices) + ')'


def any(*choices):
    return group(*choices) + '*'


def maybe(*choices):
    return group(*choices) + '?'


Whitespace = '[ \\f\\t]*'
Comment = '#[^\\r\\n]*'
Ignore = Whitespace + any('\\\\\\r?\\n' + Whitespace) + maybe(Comment)
Name = '\\w+'
Hexnumber = '0[xX](?:_?[0-9a-fA-F])+'
Binnumber = '0[bB](?:_?[01])+'
Octnumber = '0[oO](?:_?[0-7])+'
Decnumber = '(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
Exponent = '[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group('[0-9](?:_?[0-9])*\\.(?:[0-9](?:_?[0-9])*)?', '\\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = '[0-9](?:_?[0-9])*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group('[0-9](?:_?[0-9])*[jJ]', Floatnumber + '[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)

def _all_string_prefixes():
    _valid_string_prefixes = [
     "'b'", "'r'", "'u'", "'f'", "'br'", "'fr'"]
    result = {
     ''}
    for prefix in _valid_string_prefixes:
        for t in _itertools.permutations(prefix):
            for u in (_itertools.product)(*[(c, c.upper()) for c in t]):
                result.add(''.join(u))

    return result


def _compile(expr):
    return re.compile(expr, re.UNICODE)


StringPrefix = group(*_all_string_prefixes())
Single = "[^'\\\\]*(?:\\\\.[^'\\\\]*)*'"
Double = '[^"\\\\]*(?:\\\\.[^"\\\\]*)*"'
Single3 = "[^'\\\\]*(?:(?:\\\\.|'(?!''))[^'\\\\]*)*'''"
Double3 = '[^"\\\\]*(?:(?:\\\\.|"(?!""))[^"\\\\]*)*"""'
Triple = group(StringPrefix + "'''", StringPrefix + '"""')
String = group(StringPrefix + "'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*'", StringPrefix + '"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*"')
Operator = group('\\*\\*=?', '>>=?', '<<=?', '!=', '//=?', '->', '[+\\-*/%&@|^=<>]=?', '~')
Bracket = '[][(){}]'
Special = group('\\r?\\n', '\\.\\.\\.', '[:;.,@]')
Funny = group(Operator, Bracket, Special)
PlainToken = group(Number, Funny, String, Name)
Token = Ignore + PlainToken
ContStr = group(StringPrefix + "'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*" + group("'", '\\\\\\r?\\n'), StringPrefix + '"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*' + group('"', '\\\\\\r?\\n'))
PseudoExtras = group('\\\\\\r?\\n|\\Z', Comment, Triple)
PseudoToken = Whitespace + group(PseudoExtras, Number, Funny, ContStr, Name)
endpats = {}
for _prefix in _all_string_prefixes():
    endpats[_prefix + "'"] = Single
    endpats[_prefix + '"'] = Double
    endpats[_prefix + "'''"] = Single3
    endpats[_prefix + '"""'] = Double3

single_quoted = set()
triple_quoted = set()
for t in _all_string_prefixes():
    for u in (t + '"', t + "'"):
        single_quoted.add(u)

    for u in (t + '"""', t + "'''"):
        triple_quoted.add(u)

tabsize = 8

class TokenError(Exception):
    pass


class StopTokenizing(Exception):
    pass


class Untokenizer:

    def __init__(self):
        self.tokens = []
        self.prev_row = 1
        self.prev_col = 0
        self.encoding = None

    def add_whitespace(self, start):
        row, col = start
        if (row < self.prev_row or row) == self.prev_row:
            if col < self.prev_col:
                raise ValueError('start ({},{}) precedes previous end ({},{})'.format(row, col, self.prev_row, self.prev_col))
        row_offset = row - self.prev_row
        if row_offset:
            self.tokens.append('\\\n' * row_offset)
            self.prev_col = 0
        col_offset = col - self.prev_col
        if col_offset:
            self.tokens.append(' ' * col_offset)

    def untokenize(self, iterable):
        it = iter(iterable)
        indents = []
        startline = False
        for t in it:
            if len(t) == 2:
                self.compat(t, it)
                break
            else:
                tok_type, token, start, end, line = t
                if tok_type == ENCODING:
                    self.encoding = token
                    continue
                if tok_type == ENDMARKER:
                    break
                if tok_type == INDENT:
                    indents.append(token)
                    continue
                else:
                    if tok_type == DEDENT:
                        indents.pop()
                        self.prev_row, self.prev_col = end
                        continue
                    else:
                        if tok_type in (NEWLINE, NL):
                            startline = True
                        else:
                            if startline:
                                if indents:
                                    indent = indents[-1]
                                    if start[1] >= len(indent):
                                        self.tokens.append(indent)
                                        self.prev_col = len(indent)
                                    startline = False
            self.add_whitespace(start)
            self.tokens.append(token)
            self.prev_row, self.prev_col = end
            if tok_type in (NEWLINE, NL):
                self.prev_row += 1
                self.prev_col = 0

        return ''.join(self.tokens)

    def compat(self, token, iterable):
        indents = []
        toks_append = self.tokens.append
        startline = token[0] in (NEWLINE, NL)
        prevstring = False
        for tok in chain([token], iterable):
            toknum, tokval = tok[:2]
            if toknum == ENCODING:
                self.encoding = tokval
                continue
            else:
                if toknum in (NAME, NUMBER):
                    tokval += ' '
                if toknum == STRING:
                    if prevstring:
                        tokval = ' ' + tokval
                    prevstring = True
                else:
                    prevstring = False
            if toknum == INDENT:
                indents.append(tokval)
                continue
            else:
                if toknum == DEDENT:
                    indents.pop()
                    continue
                else:
                    if toknum in (NEWLINE, NL):
                        startline = True
                    else:
                        if startline:
                            if indents:
                                toks_append(indents[-1])
                                startline = False
            toks_append(tokval)


def untokenize(iterable):
    ut = Untokenizer()
    out = ut.untokenize(iterable)
    if ut.encoding is not None:
        out = out.encode(ut.encoding)
    return out


def _get_normal_name(orig_enc):
    enc = orig_enc[:12].lower().replace('_', '-')
    if enc == 'utf-8' or enc.startswith('utf-8-'):
        return 'utf-8'
    if enc in ('latin-1', 'iso-8859-1', 'iso-latin-1') or enc.startswith(('latin-1-',
                                                                          'iso-8859-1-',
                                                                          'iso-latin-1-')):
        return 'iso-8859-1'
    return orig_enc


def detect_encoding(readline):
    try:
        filename = readline.__self__.name
    except AttributeError:
        filename = None

    bom_found = False
    encoding = None
    default = 'utf-8'

    def read_or_stop():
        try:
            return readline()
        except StopIteration:
            return b''

    def find_cookie(line):
        try:
            line_string = line.decode('utf-8')
        except UnicodeDecodeError:
            msg = 'invalid or missing encoding declaration'
            if filename is not None:
                msg = '{} for {!r}'.format(msg, filename)
            raise SyntaxError(msg)

        match = cookie_re.match(line_string)
        if not match:
            return
        encoding = _get_normal_name(match.group(1))
        try:
            codec = lookup(encoding)
        except LookupError:
            if filename is None:
                msg = 'unknown encoding: ' + encoding
            else:
                msg = 'unknown encoding for {!r}: {}'.format(filename, encoding)
            raise SyntaxError(msg)

        if bom_found:
            if encoding != 'utf-8':
                if filename is None:
                    msg = 'encoding problem: utf-8'
                else:
                    msg = 'encoding problem for {!r}: utf-8'.format(filename)
                raise SyntaxError(msg)
            encoding += '-sig'
        return encoding

    first = read_or_stop()
    if first.startswith(BOM_UTF8):
        bom_found = True
        first = first[3:]
        default = 'utf-8-sig'
    else:
        if not first:
            return (
             default, [])
        else:
            encoding = find_cookie(first)
            if encoding:
                return (
                 encoding, [first])
            return blank_re.match(first) or (
             default, [first])
        second = read_or_stop()
        return second or (
         default, [first])
    encoding = find_cookie(second)
    if encoding:
        return (
         encoding, [first, second])
    return (default, [first, second])


def open(filename):
    buffer = _builtin_open(filename, 'rb')
    try:
        encoding, lines = detect_encoding(buffer.readline)
        buffer.seek(0)
        text = TextIOWrapper(buffer, encoding, line_buffering=True)
        text.mode = 'r'
        return text
    except:
        buffer.close()
        raise


def tokenize(readline):
    from itertools import chain, repeat
    encoding, consumed = detect_encoding(readline)
    rl_gen = iter(readline, b'')
    empty = repeat(b'')
    return _tokenize(chain(consumed, rl_gen, empty).__next__, encoding)


def _tokenize--- This code section failed: ---

 L. 488         0  LOAD_CONST               0
                2  DUP_TOP          
                4  STORE_FAST               'lnum'
                6  DUP_TOP          
                8  STORE_FAST               'parenlev'
               10  STORE_FAST               'continued'

 L. 489        12  LOAD_STR                 '0123456789'
               14  STORE_FAST               'numchars'

 L. 490        16  LOAD_CONST               ('', 0)
               18  UNPACK_SEQUENCE_2     2 
               20  STORE_FAST               'contstr'
               22  STORE_FAST               'needcont'

 L. 491        24  LOAD_CONST               None
               26  STORE_FAST               'contline'

 L. 492        28  LOAD_CONST               0
               30  BUILD_LIST_1          1 
               32  STORE_FAST               'indents'

 L. 494        34  LOAD_FAST                'encoding'
               36  LOAD_CONST               None
               38  COMPARE_OP               is-not
               40  POP_JUMP_IF_FALSE    72  'to 72'

 L. 495        42  LOAD_FAST                'encoding'
               44  LOAD_STR                 'utf-8-sig'
               46  COMPARE_OP               ==
               48  POP_JUMP_IF_FALSE    54  'to 54'

 L. 497        50  LOAD_STR                 'utf-8'
               52  STORE_FAST               'encoding'
             54_0  COME_FROM            48  '48'

 L. 498        54  LOAD_GLOBAL              TokenInfo
               56  LOAD_GLOBAL              ENCODING
               58  LOAD_FAST                'encoding'
               60  LOAD_CONST               (0, 0)
               62  LOAD_CONST               (0, 0)
               64  LOAD_STR                 ''
               66  CALL_FUNCTION_5       5  '5 positional arguments'
               68  YIELD_VALUE      
               70  POP_TOP          
             72_0  COME_FROM            40  '40'

 L. 499     72_74  SETUP_LOOP         1504  'to 1504'

 L. 500        76  SETUP_EXCEPT         88  'to 88'

 L. 501        78  LOAD_FAST                'readline'
               80  CALL_FUNCTION_0       0  '0 positional arguments'
               82  STORE_FAST               'line'
               84  POP_BLOCK        
               86  JUMP_FORWARD        112  'to 112'
             88_0  COME_FROM_EXCEPT     76  '76'

 L. 502        88  DUP_TOP          
               90  LOAD_GLOBAL              StopIteration
               92  COMPARE_OP               exception-match
               94  POP_JUMP_IF_FALSE   110  'to 110'
               96  POP_TOP          
               98  POP_TOP          
              100  POP_TOP          

 L. 503       102  LOAD_CONST               b''
              104  STORE_FAST               'line'
              106  POP_EXCEPT       
              108  JUMP_FORWARD        112  'to 112'
            110_0  COME_FROM            94  '94'
              110  END_FINALLY      
            112_0  COME_FROM           108  '108'
            112_1  COME_FROM            86  '86'

 L. 505       112  LOAD_FAST                'encoding'
              114  LOAD_CONST               None
              116  COMPARE_OP               is-not
              118  POP_JUMP_IF_FALSE   130  'to 130'

 L. 506       120  LOAD_FAST                'line'
              122  LOAD_METHOD              decode
              124  LOAD_FAST                'encoding'
              126  CALL_METHOD_1         1  '1 positional argument'
              128  STORE_FAST               'line'
            130_0  COME_FROM           118  '118'

 L. 507       130  LOAD_FAST                'lnum'
              132  LOAD_CONST               1
              134  INPLACE_ADD      
              136  STORE_FAST               'lnum'

 L. 508       138  LOAD_CONST               0
              140  LOAD_GLOBAL              len
              142  LOAD_FAST                'line'
              144  CALL_FUNCTION_1       1  '1 positional argument'
              146  ROT_TWO          
              148  STORE_FAST               'pos'
              150  STORE_FAST               'max'

 L. 510       152  LOAD_FAST                'contstr'
          154_156  POP_JUMP_IF_FALSE   358  'to 358'

 L. 511       158  LOAD_FAST                'line'
              160  POP_JUMP_IF_TRUE    172  'to 172'

 L. 512       162  LOAD_GLOBAL              TokenError
              164  LOAD_STR                 'EOF in multi-line string'
              166  LOAD_FAST                'strstart'
              168  CALL_FUNCTION_2       2  '2 positional arguments'
              170  RAISE_VARARGS_1       1  'exception instance'
            172_0  COME_FROM           160  '160'

 L. 513       172  LOAD_FAST                'endprog'
              174  LOAD_METHOD              match
              176  LOAD_FAST                'line'
              178  CALL_METHOD_1         1  '1 positional argument'
              180  STORE_FAST               'endmatch'

 L. 514       182  LOAD_FAST                'endmatch'
              184  POP_JUMP_IF_FALSE   252  'to 252'

 L. 515       186  LOAD_FAST                'endmatch'
              188  LOAD_METHOD              end
              190  LOAD_CONST               0
              192  CALL_METHOD_1         1  '1 positional argument'
              194  DUP_TOP          
              196  STORE_FAST               'pos'
              198  STORE_FAST               'end'

 L. 516       200  LOAD_GLOBAL              TokenInfo
              202  LOAD_GLOBAL              STRING
              204  LOAD_FAST                'contstr'
              206  LOAD_FAST                'line'
              208  LOAD_CONST               None
              210  LOAD_FAST                'end'
              212  BUILD_SLICE_2         2 
              214  BINARY_SUBSCR    
              216  BINARY_ADD       

 L. 517       218  LOAD_FAST                'strstart'
              220  LOAD_FAST                'lnum'
              222  LOAD_FAST                'end'
              224  BUILD_TUPLE_2         2 
              226  LOAD_FAST                'contline'
              228  LOAD_FAST                'line'
              230  BINARY_ADD       
              232  CALL_FUNCTION_5       5  '5 positional arguments'
              234  YIELD_VALUE      
              236  POP_TOP          

 L. 518       238  LOAD_CONST               ('', 0)
              240  UNPACK_SEQUENCE_2     2 
              242  STORE_FAST               'contstr'
              244  STORE_FAST               'needcont'

 L. 519       246  LOAD_CONST               None
              248  STORE_FAST               'contline'
              250  JUMP_FORWARD        806  'to 806'
            252_0  COME_FROM           184  '184'

 L. 520       252  LOAD_FAST                'needcont'
          254_256  POP_JUMP_IF_FALSE   336  'to 336'
              258  LOAD_FAST                'line'
              260  LOAD_CONST               -2
              262  LOAD_CONST               None
              264  BUILD_SLICE_2         2 
              266  BINARY_SUBSCR    
              268  LOAD_STR                 '\\\n'
              270  COMPARE_OP               !=
          272_274  POP_JUMP_IF_FALSE   336  'to 336'
              276  LOAD_FAST                'line'
              278  LOAD_CONST               -3
              280  LOAD_CONST               None
              282  BUILD_SLICE_2         2 
              284  BINARY_SUBSCR    
              286  LOAD_STR                 '\\\r\n'
              288  COMPARE_OP               !=
          290_292  POP_JUMP_IF_FALSE   336  'to 336'

 L. 521       294  LOAD_GLOBAL              TokenInfo
              296  LOAD_GLOBAL              ERRORTOKEN
              298  LOAD_FAST                'contstr'
              300  LOAD_FAST                'line'
              302  BINARY_ADD       

 L. 522       304  LOAD_FAST                'strstart'
              306  LOAD_FAST                'lnum'
              308  LOAD_GLOBAL              len
              310  LOAD_FAST                'line'
              312  CALL_FUNCTION_1       1  '1 positional argument'
              314  BUILD_TUPLE_2         2 
              316  LOAD_FAST                'contline'
              318  CALL_FUNCTION_5       5  '5 positional arguments'
              320  YIELD_VALUE      
              322  POP_TOP          

 L. 523       324  LOAD_STR                 ''
              326  STORE_FAST               'contstr'

 L. 524       328  LOAD_CONST               None
              330  STORE_FAST               'contline'

 L. 525       332  CONTINUE             76  'to 76'
              334  JUMP_FORWARD        806  'to 806'
            336_0  COME_FROM           290  '290'
            336_1  COME_FROM           272  '272'
            336_2  COME_FROM           254  '254'

 L. 527       336  LOAD_FAST                'contstr'
              338  LOAD_FAST                'line'
              340  BINARY_ADD       
              342  STORE_FAST               'contstr'

 L. 528       344  LOAD_FAST                'contline'
              346  LOAD_FAST                'line'
              348  BINARY_ADD       
              350  STORE_FAST               'contline'

 L. 529       352  CONTINUE             76  'to 76'
          354_356  JUMP_FORWARD        806  'to 806'
            358_0  COME_FROM           154  '154'

 L. 531       358  LOAD_FAST                'parenlev'
              360  LOAD_CONST               0
              362  COMPARE_OP               ==
          364_366  POP_JUMP_IF_FALSE   782  'to 782'
              368  LOAD_FAST                'continued'
          370_372  POP_JUMP_IF_TRUE    782  'to 782'

 L. 532       374  LOAD_FAST                'line'
          376_378  POP_JUMP_IF_TRUE    382  'to 382'

 L. 532       380  BREAK_LOOP       
            382_0  COME_FROM           376  '376'

 L. 533       382  LOAD_CONST               0
              384  STORE_FAST               'column'

 L. 534       386  SETUP_LOOP          490  'to 490'
              388  LOAD_FAST                'pos'
              390  LOAD_FAST                'max'
              392  COMPARE_OP               <
          394_396  POP_JUMP_IF_FALSE   488  'to 488'

 L. 535       398  LOAD_FAST                'line'
              400  LOAD_FAST                'pos'
              402  BINARY_SUBSCR    
              404  LOAD_STR                 ' '
              406  COMPARE_OP               ==
          408_410  POP_JUMP_IF_FALSE   422  'to 422'

 L. 536       412  LOAD_FAST                'column'
              414  LOAD_CONST               1
              416  INPLACE_ADD      
              418  STORE_FAST               'column'
              420  JUMP_FORWARD        476  'to 476'
            422_0  COME_FROM           408  '408'

 L. 537       422  LOAD_FAST                'line'
              424  LOAD_FAST                'pos'
              426  BINARY_SUBSCR    
              428  LOAD_STR                 '\t'
              430  COMPARE_OP               ==
          432_434  POP_JUMP_IF_FALSE   454  'to 454'

 L. 538       436  LOAD_FAST                'column'
              438  LOAD_GLOBAL              tabsize
              440  BINARY_FLOOR_DIVIDE
              442  LOAD_CONST               1
              444  BINARY_ADD       
              446  LOAD_GLOBAL              tabsize
              448  BINARY_MULTIPLY  
              450  STORE_FAST               'column'
              452  JUMP_FORWARD        476  'to 476'
            454_0  COME_FROM           432  '432'

 L. 539       454  LOAD_FAST                'line'
              456  LOAD_FAST                'pos'
              458  BINARY_SUBSCR    
              460  LOAD_STR                 '\x0c'
              462  COMPARE_OP               ==
          464_466  POP_JUMP_IF_FALSE   474  'to 474'

 L. 540       468  LOAD_CONST               0
              470  STORE_FAST               'column'
              472  JUMP_FORWARD        476  'to 476'
            474_0  COME_FROM           464  '464'

 L. 542       474  BREAK_LOOP       
            476_0  COME_FROM           472  '472'
            476_1  COME_FROM           452  '452'
            476_2  COME_FROM           420  '420'

 L. 543       476  LOAD_FAST                'pos'
              478  LOAD_CONST               1
              480  INPLACE_ADD      
              482  STORE_FAST               'pos'
          484_486  JUMP_BACK           388  'to 388'
            488_0  COME_FROM           394  '394'
              488  POP_BLOCK        
            490_0  COME_FROM_LOOP      386  '386'

 L. 544       490  LOAD_FAST                'pos'
              492  LOAD_FAST                'max'
              494  COMPARE_OP               ==
          496_498  POP_JUMP_IF_FALSE   502  'to 502'

 L. 545       500  BREAK_LOOP       
            502_0  COME_FROM           496  '496'

 L. 547       502  LOAD_FAST                'line'
              504  LOAD_FAST                'pos'
              506  BINARY_SUBSCR    
              508  LOAD_STR                 '#\r\n'
              510  COMPARE_OP               in
          512_514  POP_JUMP_IF_FALSE   634  'to 634'

 L. 548       516  LOAD_FAST                'line'
              518  LOAD_FAST                'pos'
              520  BINARY_SUBSCR    
              522  LOAD_STR                 '#'
              524  COMPARE_OP               ==
          526_528  POP_JUMP_IF_FALSE   594  'to 594'

 L. 549       530  LOAD_FAST                'line'
              532  LOAD_FAST                'pos'
              534  LOAD_CONST               None
              536  BUILD_SLICE_2         2 
              538  BINARY_SUBSCR    
              540  LOAD_METHOD              rstrip
              542  LOAD_STR                 '\r\n'
              544  CALL_METHOD_1         1  '1 positional argument'
              546  STORE_FAST               'comment_token'

 L. 550       548  LOAD_GLOBAL              TokenInfo
              550  LOAD_GLOBAL              COMMENT
              552  LOAD_FAST                'comment_token'

 L. 551       554  LOAD_FAST                'lnum'
              556  LOAD_FAST                'pos'
              558  BUILD_TUPLE_2         2 
              560  LOAD_FAST                'lnum'
              562  LOAD_FAST                'pos'
              564  LOAD_GLOBAL              len
              566  LOAD_FAST                'comment_token'
              568  CALL_FUNCTION_1       1  '1 positional argument'
              570  BINARY_ADD       
              572  BUILD_TUPLE_2         2 
              574  LOAD_FAST                'line'
              576  CALL_FUNCTION_5       5  '5 positional arguments'
              578  YIELD_VALUE      
              580  POP_TOP          

 L. 552       582  LOAD_FAST                'pos'
              584  LOAD_GLOBAL              len
              586  LOAD_FAST                'comment_token'
              588  CALL_FUNCTION_1       1  '1 positional argument'
              590  INPLACE_ADD      
              592  STORE_FAST               'pos'
            594_0  COME_FROM           526  '526'

 L. 554       594  LOAD_GLOBAL              TokenInfo
              596  LOAD_GLOBAL              NL
              598  LOAD_FAST                'line'
              600  LOAD_FAST                'pos'
              602  LOAD_CONST               None
              604  BUILD_SLICE_2         2 
              606  BINARY_SUBSCR    

 L. 555       608  LOAD_FAST                'lnum'
              610  LOAD_FAST                'pos'
              612  BUILD_TUPLE_2         2 
              614  LOAD_FAST                'lnum'
              616  LOAD_GLOBAL              len
              618  LOAD_FAST                'line'
              620  CALL_FUNCTION_1       1  '1 positional argument'
              622  BUILD_TUPLE_2         2 
              624  LOAD_FAST                'line'
              626  CALL_FUNCTION_5       5  '5 positional arguments'
              628  YIELD_VALUE      
              630  POP_TOP          

 L. 556       632  CONTINUE             76  'to 76'
            634_0  COME_FROM           512  '512'

 L. 558       634  LOAD_FAST                'column'
              636  LOAD_FAST                'indents'
              638  LOAD_CONST               -1
              640  BINARY_SUBSCR    
              642  COMPARE_OP               >
          644_646  POP_JUMP_IF_FALSE   692  'to 692'

 L. 559       648  LOAD_FAST                'indents'
              650  LOAD_METHOD              append
              652  LOAD_FAST                'column'
              654  CALL_METHOD_1         1  '1 positional argument'
              656  POP_TOP          

 L. 560       658  LOAD_GLOBAL              TokenInfo
              660  LOAD_GLOBAL              INDENT
              662  LOAD_FAST                'line'
              664  LOAD_CONST               None
              666  LOAD_FAST                'pos'
              668  BUILD_SLICE_2         2 
              670  BINARY_SUBSCR    
              672  LOAD_FAST                'lnum'
              674  LOAD_CONST               0
              676  BUILD_TUPLE_2         2 
              678  LOAD_FAST                'lnum'
              680  LOAD_FAST                'pos'
              682  BUILD_TUPLE_2         2 
              684  LOAD_FAST                'line'
              686  CALL_FUNCTION_5       5  '5 positional arguments'
              688  YIELD_VALUE      
              690  POP_TOP          
            692_0  COME_FROM           644  '644'

 L. 561       692  SETUP_LOOP          806  'to 806'
              694  LOAD_FAST                'column'
              696  LOAD_FAST                'indents'
              698  LOAD_CONST               -1
            700_0  COME_FROM           250  '250'
              700  BINARY_SUBSCR    
              702  COMPARE_OP               <
          704_706  POP_JUMP_IF_FALSE   778  'to 778'

 L. 562       708  LOAD_FAST                'column'
              710  LOAD_FAST                'indents'
              712  COMPARE_OP               not-in
          714_716  POP_JUMP_IF_FALSE   736  'to 736'

 L. 563       718  LOAD_GLOBAL              IndentationError

 L. 564       720  LOAD_STR                 'unindent does not match any outer indentation level'

 L. 565       722  LOAD_STR                 '<tokenize>'
              724  LOAD_FAST                'lnum'
              726  LOAD_FAST                'pos'
              728  LOAD_FAST                'line'
              730  BUILD_TUPLE_4         4 
              732  CALL_FUNCTION_2       2  '2 positional arguments'
              734  RAISE_VARARGS_1       1  'exception instance'
            736_0  COME_FROM           714  '714'

 L. 566       736  LOAD_FAST                'indents'
              738  LOAD_CONST               None
              740  LOAD_CONST               -1
              742  BUILD_SLICE_2         2 
              744  BINARY_SUBSCR    
              746  STORE_FAST               'indents'

 L. 568       748  LOAD_GLOBAL              TokenInfo
              750  LOAD_GLOBAL              DEDENT
              752  LOAD_STR                 ''
              754  LOAD_FAST                'lnum'
              756  LOAD_FAST                'pos'
              758  BUILD_TUPLE_2         2 
              760  LOAD_FAST                'lnum'
              762  LOAD_FAST                'pos'
              764  BUILD_TUPLE_2         2 
              766  LOAD_FAST                'line'
              768  CALL_FUNCTION_5       5  '5 positional arguments'
              770  YIELD_VALUE      
              772  POP_TOP          
          774_776  JUMP_BACK           694  'to 694'
            778_0  COME_FROM           704  '704'
              778  POP_BLOCK        
              780  JUMP_FORWARD        806  'to 806'
            782_0  COME_FROM           370  '370'
            782_1  COME_FROM           364  '364'

 L. 571       782  LOAD_FAST                'line'
            784_0  COME_FROM           334  '334'
          784_786  POP_JUMP_IF_TRUE    802  'to 802'

 L. 572       788  LOAD_GLOBAL              TokenError
              790  LOAD_STR                 'EOF in multi-line statement'
              792  LOAD_FAST                'lnum'
              794  LOAD_CONST               0
              796  BUILD_TUPLE_2         2 
              798  CALL_FUNCTION_2       2  '2 positional arguments'
              800  RAISE_VARARGS_1       1  'exception instance'
            802_0  COME_FROM           784  '784'

 L. 573       802  LOAD_CONST               0
              804  STORE_FAST               'continued'
            806_0  COME_FROM           780  '780'
            806_1  COME_FROM_LOOP      692  '692'
            806_2  COME_FROM           354  '354'

 L. 575   806_808  SETUP_LOOP         1500  'to 1500'
              810  LOAD_FAST                'pos'
              812  LOAD_FAST                'max'
              814  COMPARE_OP               <
          816_818  POP_JUMP_IF_FALSE  1498  'to 1498'

 L. 576       820  LOAD_GLOBAL              _compile
              822  LOAD_GLOBAL              PseudoToken
              824  CALL_FUNCTION_1       1  '1 positional argument'
              826  LOAD_METHOD              match
              828  LOAD_FAST                'line'
              830  LOAD_FAST                'pos'
              832  CALL_METHOD_2         2  '2 positional arguments'
              834  STORE_FAST               'pseudomatch'

 L. 577       836  LOAD_FAST                'pseudomatch'
          838_840  POP_JUMP_IF_FALSE  1452  'to 1452'

 L. 578       842  LOAD_FAST                'pseudomatch'
              844  LOAD_METHOD              span
              846  LOAD_CONST               1
              848  CALL_METHOD_1         1  '1 positional argument'
              850  UNPACK_SEQUENCE_2     2 
              852  STORE_FAST               'start'
              854  STORE_FAST               'end'

 L. 579       856  LOAD_FAST                'lnum'
              858  LOAD_FAST                'start'
              860  BUILD_TUPLE_2         2 
              862  LOAD_FAST                'lnum'
              864  LOAD_FAST                'end'
              866  BUILD_TUPLE_2         2 
              868  LOAD_FAST                'end'
              870  ROT_THREE        
              872  ROT_TWO          
              874  STORE_FAST               'spos'
              876  STORE_FAST               'epos'
              878  STORE_FAST               'pos'

 L. 580       880  LOAD_FAST                'start'
              882  LOAD_FAST                'end'
              884  COMPARE_OP               ==
          886_888  POP_JUMP_IF_FALSE   894  'to 894'

 L. 581   890_892  CONTINUE            810  'to 810'
            894_0  COME_FROM           886  '886'

 L. 582       894  LOAD_FAST                'line'
              896  LOAD_FAST                'start'
              898  LOAD_FAST                'end'
              900  BUILD_SLICE_2         2 
              902  BINARY_SUBSCR    
              904  LOAD_FAST                'line'
              906  LOAD_FAST                'start'
              908  BINARY_SUBSCR    
              910  ROT_TWO          
              912  STORE_FAST               'token'
              914  STORE_FAST               'initial'

 L. 584       916  LOAD_FAST                'initial'
              918  LOAD_FAST                'numchars'
              920  COMPARE_OP               in
          922_924  POP_JUMP_IF_TRUE    956  'to 956'

 L. 585       926  LOAD_FAST                'initial'
              928  LOAD_STR                 '.'
              930  COMPARE_OP               ==
          932_934  POP_JUMP_IF_FALSE   978  'to 978'
              936  LOAD_FAST                'token'
              938  LOAD_STR                 '.'
              940  COMPARE_OP               !=
          942_944  POP_JUMP_IF_FALSE   978  'to 978'
              946  LOAD_FAST                'token'
              948  LOAD_STR                 '...'
              950  COMPARE_OP               !=
          952_954  POP_JUMP_IF_FALSE   978  'to 978'
            956_0  COME_FROM           922  '922'

 L. 586       956  LOAD_GLOBAL              TokenInfo
              958  LOAD_GLOBAL              NUMBER
              960  LOAD_FAST                'token'
              962  LOAD_FAST                'spos'
              964  LOAD_FAST                'epos'
              966  LOAD_FAST                'line'
              968  CALL_FUNCTION_5       5  '5 positional arguments'
              970  YIELD_VALUE      
              972  POP_TOP          
          974_976  JUMP_ABSOLUTE      1494  'to 1494'
            978_0  COME_FROM           952  '952'
            978_1  COME_FROM           942  '942'
            978_2  COME_FROM           932  '932'

 L. 587       978  LOAD_FAST                'initial'
              980  LOAD_STR                 '\r\n'
              982  COMPARE_OP               in
          984_986  POP_JUMP_IF_FALSE  1040  'to 1040'

 L. 588       988  LOAD_FAST                'parenlev'
              990  LOAD_CONST               0
              992  COMPARE_OP               >
          994_996  POP_JUMP_IF_FALSE  1018  'to 1018'

 L. 589       998  LOAD_GLOBAL              TokenInfo
             1000  LOAD_GLOBAL              NL
             1002  LOAD_FAST                'token'
             1004  LOAD_FAST                'spos'
             1006  LOAD_FAST                'epos'
             1008  LOAD_FAST                'line'
             1010  CALL_FUNCTION_5       5  '5 positional arguments'
             1012  YIELD_VALUE      
             1014  POP_TOP          
             1016  JUMP_ABSOLUTE      1494  'to 1494'
           1018_0  COME_FROM           994  '994'

 L. 591      1018  LOAD_GLOBAL              TokenInfo
             1020  LOAD_GLOBAL              NEWLINE
             1022  LOAD_FAST                'token'
             1024  LOAD_FAST                'spos'
             1026  LOAD_FAST                'epos'
             1028  LOAD_FAST                'line'
             1030  CALL_FUNCTION_5       5  '5 positional arguments'
             1032  YIELD_VALUE      
             1034  POP_TOP          
         1036_1038  JUMP_ABSOLUTE      1494  'to 1494'
           1040_0  COME_FROM           984  '984'

 L. 593      1040  LOAD_FAST                'initial'
             1042  LOAD_STR                 '#'
             1044  COMPARE_OP               ==
         1046_1048  POP_JUMP_IF_FALSE  1072  'to 1072'

 L. 595      1050  LOAD_GLOBAL              TokenInfo
             1052  LOAD_GLOBAL              COMMENT
             1054  LOAD_FAST                'token'
             1056  LOAD_FAST                'spos'
             1058  LOAD_FAST                'epos'
             1060  LOAD_FAST                'line'
             1062  CALL_FUNCTION_5       5  '5 positional arguments'
             1064  YIELD_VALUE      
             1066  POP_TOP          
         1068_1070  JUMP_ABSOLUTE      1494  'to 1494'
           1072_0  COME_FROM          1046  '1046'

 L. 597      1072  LOAD_FAST                'token'
             1074  LOAD_GLOBAL              triple_quoted
             1076  COMPARE_OP               in
         1078_1080  POP_JUMP_IF_FALSE  1188  'to 1188'

 L. 598      1082  LOAD_GLOBAL              _compile
             1084  LOAD_GLOBAL              endpats
             1086  LOAD_FAST                'token'
             1088  BINARY_SUBSCR    
             1090  CALL_FUNCTION_1       1  '1 positional argument'
             1092  STORE_FAST               'endprog'

 L. 599      1094  LOAD_FAST                'endprog'
             1096  LOAD_METHOD              match
             1098  LOAD_FAST                'line'
             1100  LOAD_FAST                'pos'
             1102  CALL_METHOD_2         2  '2 positional arguments'
             1104  STORE_FAST               'endmatch'

 L. 600      1106  LOAD_FAST                'endmatch'
         1108_1110  POP_JUMP_IF_FALSE  1158  'to 1158'

 L. 601      1112  LOAD_FAST                'endmatch'
             1114  LOAD_METHOD              end
             1116  LOAD_CONST               0
             1118  CALL_METHOD_1         1  '1 positional argument'
             1120  STORE_FAST               'pos'

 L. 602      1122  LOAD_FAST                'line'
             1124  LOAD_FAST                'start'
             1126  LOAD_FAST                'pos'
             1128  BUILD_SLICE_2         2 
             1130  BINARY_SUBSCR    
             1132  STORE_FAST               'token'

 L. 603      1134  LOAD_GLOBAL              TokenInfo
             1136  LOAD_GLOBAL              STRING
             1138  LOAD_FAST                'token'
             1140  LOAD_FAST                'spos'
             1142  LOAD_FAST                'lnum'
             1144  LOAD_FAST                'pos'
             1146  BUILD_TUPLE_2         2 
             1148  LOAD_FAST                'line'
             1150  CALL_FUNCTION_5       5  '5 positional arguments'
             1152  YIELD_VALUE      
             1154  POP_TOP          
             1156  JUMP_ABSOLUTE      1494  'to 1494'
           1158_0  COME_FROM          1108  '1108'

 L. 605      1158  LOAD_FAST                'lnum'
             1160  LOAD_FAST                'start'
             1162  BUILD_TUPLE_2         2 
             1164  STORE_FAST               'strstart'

 L. 606      1166  LOAD_FAST                'line'
             1168  LOAD_FAST                'start'
             1170  LOAD_CONST               None
             1172  BUILD_SLICE_2         2 
             1174  BINARY_SUBSCR    
             1176  STORE_FAST               'contstr'

 L. 607      1178  LOAD_FAST                'line'
             1180  STORE_FAST               'contline'

 L. 608      1182  BREAK_LOOP       
         1184_1186  JUMP_ABSOLUTE      1494  'to 1494'
           1188_0  COME_FROM          1078  '1078'

 L. 620      1188  LOAD_FAST                'initial'
             1190  LOAD_GLOBAL              single_quoted
             1192  COMPARE_OP               in
         1194_1196  POP_JUMP_IF_TRUE   1234  'to 1234'

 L. 621      1198  LOAD_FAST                'token'
             1200  LOAD_CONST               None
             1202  LOAD_CONST               2
             1204  BUILD_SLICE_2         2 
             1206  BINARY_SUBSCR    
             1208  LOAD_GLOBAL              single_quoted
             1210  COMPARE_OP               in
         1212_1214  POP_JUMP_IF_TRUE   1234  'to 1234'

 L. 622      1216  LOAD_FAST                'token'
             1218  LOAD_CONST               None
             1220  LOAD_CONST               3
             1222  BUILD_SLICE_2         2 
             1224  BINARY_SUBSCR    
             1226  LOAD_GLOBAL              single_quoted
             1228  COMPARE_OP               in
         1230_1232  POP_JUMP_IF_FALSE  1348  'to 1348'
           1234_0  COME_FROM          1212  '1212'
           1234_1  COME_FROM          1194  '1194'

 L. 623      1234  LOAD_FAST                'token'
             1236  LOAD_CONST               -1
             1238  BINARY_SUBSCR    
             1240  LOAD_STR                 '\n'
             1242  COMPARE_OP               ==
         1244_1246  POP_JUMP_IF_FALSE  1328  'to 1328'

 L. 624      1248  LOAD_FAST                'lnum'
             1250  LOAD_FAST                'start'
             1252  BUILD_TUPLE_2         2 
             1254  STORE_FAST               'strstart'

 L. 631      1256  LOAD_GLOBAL              _compile
             1258  LOAD_GLOBAL              endpats
             1260  LOAD_METHOD              get
             1262  LOAD_FAST                'initial'
             1264  CALL_METHOD_1         1  '1 positional argument'
         1266_1268  JUMP_IF_TRUE_OR_POP  1298  'to 1298'

 L. 632      1270  LOAD_GLOBAL              endpats
             1272  LOAD_METHOD              get
             1274  LOAD_FAST                'token'
             1276  LOAD_CONST               1
             1278  BINARY_SUBSCR    
             1280  CALL_METHOD_1         1  '1 positional argument'
         1282_1284  JUMP_IF_TRUE_OR_POP  1298  'to 1298'

 L. 633      1286  LOAD_GLOBAL              endpats
             1288  LOAD_METHOD              get
             1290  LOAD_FAST                'token'
             1292  LOAD_CONST               2
             1294  BINARY_SUBSCR    
             1296  CALL_METHOD_1         1  '1 positional argument'
           1298_0  COME_FROM          1282  '1282'
           1298_1  COME_FROM          1266  '1266'
             1298  CALL_FUNCTION_1       1  '1 positional argument'
             1300  STORE_FAST               'endprog'

 L. 634      1302  LOAD_FAST                'line'
             1304  LOAD_FAST                'start'
             1306  LOAD_CONST               None
             1308  BUILD_SLICE_2         2 
             1310  BINARY_SUBSCR    
             1312  LOAD_CONST               1
             1314  ROT_TWO          
             1316  STORE_FAST               'contstr'
             1318  STORE_FAST               'needcont'

 L. 635      1320  LOAD_FAST                'line'
             1322  STORE_FAST               'contline'

 L. 636      1324  BREAK_LOOP       
             1326  JUMP_FORWARD       1346  'to 1346'
           1328_0  COME_FROM          1244  '1244'

 L. 638      1328  LOAD_GLOBAL              TokenInfo
             1330  LOAD_GLOBAL              STRING
             1332  LOAD_FAST                'token'
             1334  LOAD_FAST                'spos'
             1336  LOAD_FAST                'epos'
             1338  LOAD_FAST                'line'
             1340  CALL_FUNCTION_5       5  '5 positional arguments'
             1342  YIELD_VALUE      
             1344  POP_TOP          
           1346_0  COME_FROM          1326  '1326'
             1346  JUMP_FORWARD       1450  'to 1450'
           1348_0  COME_FROM          1230  '1230'

 L. 640      1348  LOAD_FAST                'initial'
             1350  LOAD_METHOD              isidentifier
             1352  CALL_METHOD_0         0  '0 positional arguments'
         1354_1356  POP_JUMP_IF_FALSE  1378  'to 1378'

 L. 641      1358  LOAD_GLOBAL              TokenInfo
             1360  LOAD_GLOBAL              NAME
             1362  LOAD_FAST                'token'
             1364  LOAD_FAST                'spos'
             1366  LOAD_FAST                'epos'
             1368  LOAD_FAST                'line'
             1370  CALL_FUNCTION_5       5  '5 positional arguments'
             1372  YIELD_VALUE      
             1374  POP_TOP          
             1376  JUMP_FORWARD       1450  'to 1450'
           1378_0  COME_FROM          1354  '1354'

 L. 642      1378  LOAD_FAST                'initial'
             1380  LOAD_STR                 '\\'
             1382  COMPARE_OP               ==
         1384_1386  POP_JUMP_IF_FALSE  1394  'to 1394'

 L. 643      1388  LOAD_CONST               1
             1390  STORE_FAST               'continued'
             1392  JUMP_FORWARD       1450  'to 1450'
           1394_0  COME_FROM          1384  '1384'

 L. 645      1394  LOAD_FAST                'initial'
             1396  LOAD_STR                 '([{'
             1398  COMPARE_OP               in
         1400_1402  POP_JUMP_IF_FALSE  1414  'to 1414'

 L. 646      1404  LOAD_FAST                'parenlev'
             1406  LOAD_CONST               1
             1408  INPLACE_ADD      
             1410  STORE_FAST               'parenlev'
             1412  JUMP_FORWARD       1432  'to 1432'
           1414_0  COME_FROM          1400  '1400'

 L. 647      1414  LOAD_FAST                'initial'
             1416  LOAD_STR                 ')]}'
             1418  COMPARE_OP               in
         1420_1422  POP_JUMP_IF_FALSE  1432  'to 1432'

 L. 648      1424  LOAD_FAST                'parenlev'
             1426  LOAD_CONST               1
             1428  INPLACE_SUBTRACT 
             1430  STORE_FAST               'parenlev'
           1432_0  COME_FROM          1420  '1420'
           1432_1  COME_FROM          1412  '1412'

 L. 649      1432  LOAD_GLOBAL              TokenInfo
             1434  LOAD_GLOBAL              OP
             1436  LOAD_FAST                'token'
             1438  LOAD_FAST                'spos'
             1440  LOAD_FAST                'epos'
             1442  LOAD_FAST                'line'
             1444  CALL_FUNCTION_5       5  '5 positional arguments'
             1446  YIELD_VALUE      
             1448  POP_TOP          
           1450_0  COME_FROM          1392  '1392'
           1450_1  COME_FROM          1376  '1376'
           1450_2  COME_FROM          1346  '1346'
             1450  JUMP_BACK           810  'to 810'
           1452_0  COME_FROM           838  '838'

 L. 651      1452  LOAD_GLOBAL              TokenInfo
             1454  LOAD_GLOBAL              ERRORTOKEN
             1456  LOAD_FAST                'line'
             1458  LOAD_FAST                'pos'
             1460  BINARY_SUBSCR    

 L. 652      1462  LOAD_FAST                'lnum'
             1464  LOAD_FAST                'pos'
             1466  BUILD_TUPLE_2         2 
             1468  LOAD_FAST                'lnum'
             1470  LOAD_FAST                'pos'
             1472  LOAD_CONST               1
             1474  BINARY_ADD       
             1476  BUILD_TUPLE_2         2 
             1478  LOAD_FAST                'line'
             1480  CALL_FUNCTION_5       5  '5 positional arguments'
             1482  YIELD_VALUE      
             1484  POP_TOP          

 L. 653      1486  LOAD_FAST                'pos'
             1488  LOAD_CONST               1
             1490  INPLACE_ADD      
             1492  STORE_FAST               'pos'
         1494_1496  JUMP_BACK           810  'to 810'
           1498_0  COME_FROM           816  '816'
             1498  POP_BLOCK        
           1500_0  COME_FROM_LOOP      806  '806'
             1500  JUMP_BACK            76  'to 76'
             1502  POP_BLOCK        
           1504_0  COME_FROM_LOOP       72  '72'

 L. 655      1504  SETUP_LOOP         1554  'to 1554'
             1506  LOAD_FAST                'indents'
             1508  LOAD_CONST               1
             1510  LOAD_CONST               None
             1512  BUILD_SLICE_2         2 
             1514  BINARY_SUBSCR    
             1516  GET_ITER         
             1518  FOR_ITER           1552  'to 1552'
             1520  STORE_FAST               'indent'

 L. 656      1522  LOAD_GLOBAL              TokenInfo
             1524  LOAD_GLOBAL              DEDENT
             1526  LOAD_STR                 ''
             1528  LOAD_FAST                'lnum'
             1530  LOAD_CONST               0
             1532  BUILD_TUPLE_2         2 
             1534  LOAD_FAST                'lnum'
             1536  LOAD_CONST               0
             1538  BUILD_TUPLE_2         2 
             1540  LOAD_STR                 ''
             1542  CALL_FUNCTION_5       5  '5 positional arguments'
             1544  YIELD_VALUE      
             1546  POP_TOP          
         1548_1550  JUMP_BACK          1518  'to 1518'
             1552  POP_BLOCK        
           1554_0  COME_FROM_LOOP     1504  '1504'

 L. 657      1554  LOAD_GLOBAL              TokenInfo
             1556  LOAD_GLOBAL              ENDMARKER
             1558  LOAD_STR                 ''
             1560  LOAD_FAST                'lnum'
             1562  LOAD_CONST               0
             1564  BUILD_TUPLE_2         2 
             1566  LOAD_FAST                'lnum'
             1568  LOAD_CONST               0
             1570  BUILD_TUPLE_2         2 
             1572  LOAD_STR                 ''
             1574  CALL_FUNCTION_5       5  '5 positional arguments'
             1576  YIELD_VALUE      
             1578  POP_TOP          

Parse error at or near `COME_FROM' instruction at offset 700_0


def generate_tokens(readline):
    return _tokenize(readline, None)


def main():
    import argparse

    def perror(message):
        print(message, file=(sys.stderr))

    def error(message, filename=None, location=None):
        if location:
            args = (
             filename,) + location + (message,)
            perror('%s:%d:%d: error: %s' % args)
        else:
            if filename:
                perror('%s: error: %s' % (filename, message))
            else:
                perror('error: %s' % message)
        sys.exit(1)

    parser = argparse.ArgumentParser(prog='python -m tokenize')
    parser.add_argument(dest='filename', nargs='?', metavar='filename.py',
      help='the file to tokenize; defaults to stdin')
    parser.add_argument('-e', '--exact', dest='exact', action='store_true', help='display token names using the exact type')
    args = parser.parse_args()
    try:
        if args.filename:
            filename = args.filename
            with _builtin_open(filename, 'rb') as (f):
                tokens = list(tokenize(f.readline))
        else:
            filename = '<stdin>'
            tokens = _tokenize(sys.stdin.readline, None)
        for token in tokens:
            token_type = token.type
            if args.exact:
                token_type = token.exact_type
            token_range = '%d,%d-%d,%d:' % (token.start + token.end)
            print('%-20s%-15s%-15r' % (
             token_range, tok_name[token_type], token.string))

    except IndentationError as err:
        try:
            line, column = err.args[1][1:3]
            error(err.args[0], filename, (line, column))
        finally:
            err = None
            del err

    except TokenError as err:
        try:
            line, column = err.args[1]
            error(err.args[0], filename, (line, column))
        finally:
            err = None
            del err

    except SyntaxError as err:
        try:
            error(err, filename)
        finally:
            err = None
            del err

    except OSError as err:
        try:
            error(err)
        finally:
            err = None
            del err

    except KeyboardInterrupt:
        print('interrupted\n')
    except Exception as err:
        try:
            perror('unexpected error: %s' % err)
            raise
        finally:
            err = None
            del err


if __name__ == '__main__':
    main()
