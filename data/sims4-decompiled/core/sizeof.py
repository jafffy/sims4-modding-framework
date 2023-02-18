# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sizeof.py
# Compiled at: 2020-10-06 17:11:30
# Size of source mod 2**32: 17781 bytes

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
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr DUP_TOP . designList
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
aug_assign2 ::= expr DUP_TOP . LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR . expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr . inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op . ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO . STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR . 
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
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
compare ::= compare_single . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr DUP_TOP . ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1b_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained1c_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained2_false_37 ::= expr DUP_TOP . ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
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
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= list . 
expr ::= tuple . 
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
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_cfs else_suitel . 
ifelsestmtl ::= testexpr c_stmts_opt jb_else . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt jb_else else_suitel . 
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
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
inplace_op ::= INPLACE_ADD . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK come_froms . 
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jb_else ::= JUMP_BACK COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_absolute_else ::= jb_else . 
kvlist_8 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr BUILD_MAP_8
kvlist_8 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr BUILD_MAP_8
kvlist_8 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr BUILD_MAP_8
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lastl_stmt come_froms . l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr BUILD_LIST_1 . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
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
setup_loop ::= SETUP_LOOP _come_froms . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign2 . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifstmtl . 
stmt ::= whilestmt . 
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
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
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
while1stmt ::= setup_loop l_stmts COME_FROM_LOOP JUMP_BACK . POP_BLOCK COME_FROM_LOOP
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
whilestmt ::= setup_loop testexpr l_stmts_opt come_froms . JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 120       118  LOAD_FAST                'second'
                 120  LOAD_ATTR                parent
                 122  DUP_TOP          
                 124  LOAD_ATTR                sizerec
                 126  LOAD_FAST                'second'
                 128  LOAD_ATTR                sizerec
                 130  INPLACE_ADD      
                 132  ROT_TWO          
                 134  STORE_ATTR               sizerec
               136_0  COME_FROM_LOOP       64  '64'
                 136  JUMP_BACK            12  'to 12'
->             138_0  COME_FROM            14  '14'
                 138  POP_BLOCK        
import collections, gc, itertools, struct, sys
from types import FunctionType, ModuleType

def recursive_sizeof(roots, skip_atomic=False):
    handler_cache = {}
    pending = collections.deque(((root, root) for root in roots))
    visited = set()
    sizes = {id(root): 0 for root in roots}
    while pending:
        obj, root = pending.popleft()
        if id(obj) in visited:
            continue
        if not skip_atomic or gc.is_tracked(obj):
            sizes[id(root)] += sys.getsizeof(obj)
        visited.add(id(obj))
        for child in enumerate_children(obj, handler_cache, HANDLERS):
            if child is None:
                continue
            pending.append((child, root))

    results = []
    for root in roots:
        results.append((root, sizes[id(root)]))

    return results


def report(labeled_roots, skip_atomic=False):
    labels = []
    roots = []
    for label, root in labeled_roots:
        labels.append(label)
        roots.append(root)

    results = recursive_sizeof(roots, skip_atomic=skip_atomic)
    counter = collections.Counter()
    for label, (root, size) in zip(labels, results):
        counter[label] += size

    return counter


class Node:
    __slots__ = ('sep', 'name', 'obj', 'size', 'sizerec', 'parent', 'child', 'sibling')

    def __init__(self, sep, name, obj, size):
        self.sep = sep
        self.name = name
        self.obj = obj
        self.size = size
        self.sizerec = 0
        self.parent = None
        self.child = None
        self.sibling = None

    def add_child(self, node):
        node.parent = self
        node.sibling = self.child
        self.child = node

    def __str__(self):
        obj = self
        name = ''
        while obj is not None:
            name = '{}{}{}'.format(obj.sep, obj.name, name)
            obj = obj.parent

        return name


def calc_sizerec--- This code section failed: ---

 L. 105         0  LOAD_FAST                'node'
                2  LOAD_CONST               None
                4  BUILD_TUPLE_2         2 
                6  BUILD_LIST_1          1 
                8  STORE_FAST               'pending'

 L. 109        10  SETUP_LOOP          140  'to 140'
             12_0  COME_FROM           116  '116'
             12_1  COME_FROM           106  '106'
               12  LOAD_FAST                'pending'
               14  POP_JUMP_IF_FALSE   138  'to 138'

 L. 110        16  LOAD_FAST                'pending'
               18  LOAD_METHOD              pop
               20  CALL_METHOD_0         0  '0 positional arguments'
               22  UNPACK_SEQUENCE_2     2 
               24  STORE_FAST               'first'
               26  STORE_FAST               'second'

 L. 111        28  LOAD_FAST                'first'
               30  LOAD_CONST               None
               32  COMPARE_OP               is-not
               34  POP_JUMP_IF_FALSE   100  'to 100'

 L. 112        36  LOAD_FAST                'first'
               38  LOAD_ATTR                size
               40  LOAD_FAST                'first'
               42  STORE_ATTR               sizerec

 L. 113        44  LOAD_FAST                'pending'
               46  LOAD_METHOD              append
               48  LOAD_CONST               None
               50  LOAD_FAST                'first'
               52  BUILD_TUPLE_2         2 
               54  CALL_METHOD_1         1  '1 positional argument'
               56  POP_TOP          

 L. 114        58  LOAD_FAST                'first'
               60  LOAD_ATTR                child
               62  STORE_FAST               'child'

 L. 115        64  SETUP_LOOP          136  'to 136'
               66  LOAD_FAST                'child'
               68  LOAD_CONST               None
               70  COMPARE_OP               is-not
               72  POP_JUMP_IF_FALSE    96  'to 96'

 L. 116        74  LOAD_FAST                'pending'
               76  LOAD_METHOD              append
               78  LOAD_FAST                'child'
               80  LOAD_CONST               None
               82  BUILD_TUPLE_2         2 
               84  CALL_METHOD_1         1  '1 positional argument'
               86  POP_TOP          

 L. 117        88  LOAD_FAST                'child'
               90  LOAD_ATTR                sibling
               92  STORE_FAST               'child'
               94  JUMP_BACK            66  'to 66'
             96_0  COME_FROM            72  '72'
               96  POP_BLOCK        
               98  JUMP_BACK            12  'to 12'
            100_0  COME_FROM            34  '34'

 L. 118       100  LOAD_FAST                'second'
              102  LOAD_CONST               None
              104  COMPARE_OP               is-not
              106  POP_JUMP_IF_FALSE    12  'to 12'

 L. 119       108  LOAD_FAST                'second'
              110  LOAD_ATTR                parent
              112  LOAD_CONST               None
              114  COMPARE_OP               is-not
              116  POP_JUMP_IF_FALSE    12  'to 12'

 L. 120       118  LOAD_FAST                'second'
              120  LOAD_ATTR                parent
              122  DUP_TOP          
              124  LOAD_ATTR                sizerec
              126  LOAD_FAST                'second'
              128  LOAD_ATTR                sizerec
              130  INPLACE_ADD      
              132  ROT_TWO          
              134  STORE_ATTR               sizerec
            136_0  COME_FROM_LOOP       64  '64'
              136  JUMP_BACK            12  'to 12'
            138_0  COME_FROM            14  '14'
              138  POP_BLOCK        
            140_0  COME_FROM_LOOP       10  '10'

Parse error at or near `COME_FROM' instruction at offset 138_0


def get_object_tree(labeled_roots, skip_atomic=False, allowed_ids=None, bfs=True, include_cycles=False):
    handler_cache = {}
    root = Node('', 'Root', None, 0)
    visited = {
     id(root)}
    pending = collections.deque([(obj, '', name, root) for name, obj in labeled_roots])
    while pending:
        if bfs:
            obj, sep, name, parent = pending.popleft()
        else:
            obj, sep, name, parent = pending.pop()
        obj_id = id(obj)
        if obj_id in visited:
            continue
        visited.add(obj_id)
        if allowed_ids is not None:
            if obj_id not in allowed_ids:
                continue
        if skip_atomic:
            if not gc.is_tracked(obj):
                continue
        size = sys.getsizeof(obj)
        node = Node(sep, name, obj, size)
        parent.add_child(node)
        try:
            for sep, field, child in enumerate_children(obj, handler_cache, FIELD_HANDLERS):
                if child is None:
                    continue
                if allowed_ids is not None:
                    if id(child) not in allowed_ids:
                        continue
                if id(child) in visited:
                    if include_cycles:
                        child_node = Node(sep, field + '&', child, 0)
                        node.add_child(child_node)
                        continue
                    pending.append((child, sep, field, node))

        except:
            pass

    calc_sizerec(root)
    return root


def _store_string(string_table, s):
    if s in string_table:
        return string_table[s]
    index = len(string_table)
    string_table[s] = index
    return index


def write_object_tree(node, fd):
    pending = [
     node]
    ns = struct.Struct('<4QL1s3L')
    string_table = collections.OrderedDict()
    fd.write(struct.pack('=b', 1))
    node_count = 0
    node_count_offset = fd.tell()
    fd.write(struct.pack('<Q', 0))
    while pending:
        node_count += 1
        node = pending.pop()
        parent_id = id(node.parent.obj) if node.parent is not None else 0
        fd.write(ns.pack(id(node.obj), parent_id, id(type(node.obj)), node.sizerec, node.size, node.sep.encode('utf-8'), sys.getrefcount(node.obj), _store_string(string_table, node.name), _store_string(string_table, short_str((node.obj), strip_object_name=True))))
        child = node.child
        while child is not None:
            pending.append(child)
            child = child.sibling

    string_table_offset = fd.tell()
    fd.seek(node_count_offset)
    fd.write(struct.pack('<Q', node_count))
    fd.seek(string_table_offset)
    fd.write(struct.pack('<Q', len(string_table)))
    for s in string_table:
        try:
            utf8 = s.encode('utf-8', errors='xmlcharrefreplace')
        except:
            utf8 = ('UTF-8 error: ' + repr(s)).encode('utf-8', errors='replace')

        fd.write(struct.pack('<L', len(utf8)))
        fd.write(utf8)


def enumerate_children(obj, handler_cache, handlers):
    t = type(obj)
    if t not in handler_cache:
        for st in t.__mro__:
            handler = handlers.get(st)
            if handler is not None:
                handler_cache[t] = handler
                break
        else:
            handler_cache[t] = None

    handler = handler_cache[t]
    if handler is not None:
        return handler(obj)
    return ()


def object_iter(obj):
    children = []
    for attr in dir(obj):
        try:
            v = getattr(obj, attr, None)
        except:
            continue

        ref = sys.getrefcount(v)
        if not v is None:
            if ref <= 2:
                continue
            children.append(v)

    return children


def module_iter(module):
    name = module.__name__
    members = []
    module_dict = vars(module)
    for value in module_dict.values():
        if isinstance(value, (type, FunctionType)):
            if value.__module__ != name:
                continue
        members.append(value)

    members.append(vars(module))
    return members


child_iter = iter
dict_iter = lambda obj: itertools.chain.from_iterable(obj.items())
HANDLERS = {collections.deque: child_iter, 
 frozenset: child_iter, 
 list: child_iter, 
 set: child_iter, 
 tuple: child_iter, 
 dict: dict_iter, 
 object: object_iter, 
 ModuleType: module_iter}

def _format_function_strings(string_to_update, prefix):
    at_index = string_to_update.find(' at ')
    if at_index > 0:
        return string_to_update[:at_index].replace(prefix, '')
    return string_to_update


def safe_str(obj, strip_object_name=False):
    if strip_object_name:
        try:
            if isinstance(obj, list):
                return 'list'
            if isinstance(obj, dict):
                return 'dict'
            obj_class_name = obj.__class__.__name__
            if 'metaclass' in obj_class_name.lower():
                return obj.__name__
            obj_string = str(obj)
            if 'type' == obj_class_name:
                return obj_string
            prefixes_to_test = [
             '<function ', '<code ', '<bound method ']
            for prefix_to_test in prefixes_to_test:
                if obj_string.startswith(prefix_to_test):
                    obj_string = _format_function_strings(obj_string, prefix_to_test)
                    return obj_string

            if obj_string.startswith('<cell'):
                at_index = obj_string.find(': ')
                if at_index > 0:
                    obj_string = obj_string[at_index:]
                at_index = obj_string.find(' at ')
                if at_index >= 0:
                    obj_string = obj_string[:at_index]
                return obj_string
            return obj_string
        except:
            pass

    try:
        return str(obj)
    except:
        pass

    try:
        return object.__str__(obj)
    except:
        pass

    try:
        t = type(obj)
        return '<{}.{} object at {:#X}>'.format(t.__module__, t.__qualname__, id(obj))
    except:
        pass

    return '<??? object at {:#X}>'.format(id(obj))


def short_str(obj, strip_object_name=False, maxlen=64, tail=17):
    s = safe_str(obj, strip_object_name=strip_object_name)
    if len(s) > maxlen:
        s = '{}...{}'.format(s[0:maxlen - tail - 3], s[len(s) - tail:])
    return s


def list_fields(obj):
    for i, value in enumerate(obj):
        field = sys.intern('[{}]'.format(i))
        yield ('', field, value)


def dict_fields(obj):
    try:
        for key, value in obj.items():
            yield ('.', short_str(key), value)

    except:
        pass

    yield from list_fields(obj)


def module_fields(module):
    name = module.__name__
    members = []
    module_dict = vars(module)
    for name, value in module_dict.items():
        if isinstance(value, (type, FunctionType)):
            if value.__module__ != name:
                continue
        members.append(('.', name, value))

    return members


def object_fields(obj):
    children = []
    children.append(('.', '__type__', type(obj)))
    ids = set()
    ids.add(id(type(obj)))
    ref_ids = set((id(v) for v in gc.get_referents(obj)))
    for attr in dir(obj):
        if attr == '__qualname__':
            continue
        try:
            v = getattr(obj, attr, None)
        except:
            continue

        vid = id(v)
        if vid not in ref_ids:
            continue
        ids.add(vid)
        ref = sys.getrefcount(v)
        if not v is None:
            if ref <= 2:
                continue
            if attr == '__annotations__':
                if ref == 3:
                    if not v:
                        delattr(obj, attr)
                        continue
            children.append(('.', attr, v))

    refs = gc.get_referents(obj)
    for v in refs:
        if id(v) not in ids:
            children.append(('.', '<gcref>', v))

    return children


FIELD_HANDLERS = {collections.deque: list_fields, 
 frozenset: list_fields, 
 list: list_fields, 
 set: list_fields, 
 tuple: list_fields, 
 dict: dict_fields, 
 object: object_fields, 
 ModuleType: module_fields}
