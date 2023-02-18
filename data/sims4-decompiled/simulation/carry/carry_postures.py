# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\carry\carry_postures.py
# Compiled at: 2022-03-14 18:49:50
# Size of source mod 2**32: 37742 bytes

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
_stmts ::= _stmts . stmt
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
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
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
continues ::= _stmts . lastl_stmt continue
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
expr ::= LOAD_FAST . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
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
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
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
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . expr BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 242         6  LOAD_FAST                'self'
                   8  LOAD_ATTR                _runtime_slot
                  10  LOAD_METHOD              add_child
                  12  LOAD_FAST                'self'
                  14  LOAD_ATTR                _obj
                  16  CALL_METHOD_1         1  '1 positional argument'
                  18  POP_TOP          
                  20  JUMP_FORWARD         22  'to 22'
->              22_0  COME_FROM            20  '20'

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
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr expr expr CALL_METHOD_6
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr expr expr CALL_METHOD_6
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr . expr expr expr expr CALL_METHOD_6
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr . expr expr expr CALL_METHOD_6
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr CALL_FUNCTION_EX_KW . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
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
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST BUILD_CONST_KEY_MAP_1 . 
else_suite ::= suite_stmts . 
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_ex_kw4 . 
expr ::= compare . 
expr ::= dict . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
function_def_deco ::= mkfuncdeco . store
function_def_deco ::= mkfuncdeco store . 
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
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
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
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_4
mkfunc ::= expr LOAD_CODE LOAD_STR MAKE_FUNCTION_4 . 
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9 . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 . CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 CALL_FUNCTION_1 . 
mkfuncdeco0 ::= mkfunc . 
opt_come_from_except ::= _come_froms . 
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
return_closure ::= LOAD_CLOSURE DUP_TOP . STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME . RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME RETURN_VALUE . RETURN_LAST
return_closure ::= LOAD_CLOSURE DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST . 
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
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= function_def . 
stmt ::= function_def_deco . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmt ::= return_closure . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
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
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 283         6  LOAD_FAST                'self'
                   8  LOAD_ATTR                _inventory_owner
                  10  LOAD_ATTR                inventory_component
                  12  LOAD_METHOD              system_add_object
                  14  LOAD_FAST                'self'
                  16  LOAD_ATTR                _obj
                  18  CALL_METHOD_1         1  '1 positional argument'
                  20  POP_TOP          
                  22  JUMP_FORWARD         24  'to 24'
->              24_0  COME_FROM            22  '22'
import functools
from animation.arb_element import distribute_arb_element
from build_buy import HouseholdInventoryFlags
from carry.carry_utils import hide_held_props, SCRIPT_EVENT_ID_STOP_CARRY, PARAM_CARRY_TRACK, SCRIPT_EVENT_ID_START_CARRY, set_carry_track_param
from interactions.utils.sim_focus import with_sim_focus, SimFocus
from objects import VisibilityState
from objects.slots import get_surface_height_parameter_for_object, get_surface_height_parameter_for_height
from placement import FGLSearchFlagsDefaultForSim, FGLSearchFlagsDefault
from postures.posture_animation_data import AnimationDataUniversal, AnimationDataByActorSpecies
from postures.posture_specs import PostureSpecVariable
from routing import SurfaceType
from sims.sim_info_types import Species
from sims4.collections import frozendict
from sims4.log import StackVar
from sims4.math import vector3_angle
from sims4.tuning.tunable_base import GroupNames
from sims4.utils import flexmethod, classproperty, constproperty
import animation, animation.arb, build_buy, placement, postures.posture, routing, services, sims4.log, sims4.math
logger = sims4.log.Logger('Carry')

class CarrySystemTarget:

    def __init__(self, obj, put):
        self._obj = obj
        self._put = put

    @property
    def _route_target(self):
        return self._obj

    def get_constraint(self, sim, **kwargs):
        return (self._obj.get_carry_transition_constraint)(sim, (self._route_target.position), 
         (self._route_target.routing_surface), **kwargs)

    @property
    def surface_height(self) -> str:
        return get_surface_height_parameter_for_object(self._obj)

    @property
    def has_custom_animation(self) -> bool:
        raise NotImplementedError()

    def append_custom_animation_to_arb(self, arb, carry_posture, normal_carry_callback):
        raise NotImplementedError()

    def carry_event_callback(self, *_, **__):
        raise NotImplementedError()


class CarrySystemTransientTarget(CarrySystemTarget):

    def __init__(self, obj, put):
        super().__init__(obj, put)

    @property
    def surface_height(self) -> str:
        return 'discard'

    @property
    def has_custom_animation(self) -> bool:
        return False

    def carry_event_callback(self, *_, **__):
        self._obj.remove_from_client()


class CarrySystemTerrainTarget(CarrySystemTarget):

    def __init__(self, sim, obj, put, transform, routing_surface=None, custom_event_callback=None):
        super().__init__(obj, put)
        self._sim = sim
        self._transform = sims4.math.Transform(translation=(transform.translation), orientation=(transform.orientation))
        if put:
            put_down_strategy = obj.get_put_down_strategy(parent=sim)
            if put_down_strategy.put_down_on_terrain_facing_sim:
                angle = sims4.math.yaw_quaternion_to_angle(transform.orientation) + sims4.math.PI
                self._transform.orientation = sims4.math.angle_to_yaw_quaternion(angle)
            else:
                angle = vector3_angle(transform.orientation.transform_vector(sims4.math.Vector3.X_AXIS()))
                self._transform.orientation = sims4.math.angle_to_yaw_quaternion(angle)
        self._routing_surface = routing_surface
        self._custom_event_callback = custom_event_callback

    @property
    def transform(self):
        return self._transform

    @property
    def surface_height(self) -> str:
        routing_surface = self._routing_surface or self._obj.routing_surface
        surface_height = services.terrain_service.terrain_object().get_routing_surface_height_at(self.transform.translation.x, self.transform.translation.z, routing_surface)
        terrain_height = services.terrain_service.terrain_object().get_routing_surface_height_at(self._sim.position.x, self._sim.position.z, self._sim.routing_surface)
        return get_surface_height_parameter_for_height(surface_height - terrain_height)

    @property
    def has_custom_animation(self) -> bool:
        return False

    def carry_event_callback(self, *args, **kwargs):
        if self._put:
            CarryingObject.snap_to_good_location_on_floor((self._obj), starting_transform=(self._transform), starting_routing_surface=(self._routing_surface))
        if self._custom_event_callback is not None:
            (self._custom_event_callback)(*args, **kwargs)

    def get_constraint(self, sim, **kwargs):
        constraint = self._obj.get_pick_up_constraint(sim)
        if constraint is not None:
            return constraint
        return (super().get_constraint)(sim, **kwargs)


class CarrySystemCustomAnimationTarget(CarrySystemTarget):
    _custom_constraint = None
    _custom_animation = None

    def get_constraint(self, sim, **kwargs):
        if self._custom_constraint is not None:
            return self._custom_constraint
        return (super().get_constraint)(sim, **kwargs)

    @property
    def has_custom_animation(self) -> bool:
        return self._custom_animation is not None

    def append_custom_animation_to_arb(self, arb, carry_posture, normal_carry_callback):
        custom_carry_event_callback = self.carry_event_callback

        def _carry_event_callback(*_, **__):
            custom_carry_event_callback()
            normal_carry_callback()

        self.carry_event_callback = _carry_event_callback
        self._custom_animation(arb, carry_posture.sim, carry_posture.target, carry_posture.track, carry_posture.animation_context, self.surface_height)


class CarrySystemRuntimeSlotTarget(CarrySystemCustomAnimationTarget):

    def __init__(self, sim, obj, put, runtime_slot):
        super().__init__(obj, put)
        if runtime_slot is None:
            raise RuntimeError('Attempt to create a CarrySystemRuntimeSlotTarget with no runtime slot!')
        self._runtime_slot = runtime_slot
        if not runtime_slot.owner.is_sim:
            self._custom_constraint = runtime_slot.owner.get_surface_access_constraint(sim, put, obj)
            self._custom_animation = runtime_slot.owner.get_surface_access_animation(put)
        self._sim = sim

    @property
    def _route_target(self):
        return self._runtime_slot

    @property
    def surface_height(self) -> str:
        _, surface_height = self._runtime_slot.get_slot_height_and_parameter(self._sim)
        return surface_height

    def carry_event_callback--- This code section failed: ---

 L. 241         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _put
                4  POP_JUMP_IF_FALSE    22  'to 22'

 L. 242         6  LOAD_FAST                'self'
                8  LOAD_ATTR                _runtime_slot
               10  LOAD_METHOD              add_child
               12  LOAD_FAST                'self'
               14  LOAD_ATTR                _obj
               16  CALL_METHOD_1         1  '1 positional argument'
               18  POP_TOP          
               20  JUMP_FORWARD         22  'to 22'
             22_0  COME_FROM            20  '20'
             22_1  COME_FROM             4  '4'

Parse error at or near `COME_FROM' instruction at offset 22_0

    def get_constraint(self, sim, **kwargs):
        constraint = self._obj.get_pick_up_constraint(sim)
        if constraint is not None:
            return constraint
        return (super().get_constraint)(sim, **kwargs)


class CarrySystemInventoryTarget(CarrySystemCustomAnimationTarget):

    def __init__(self, sim, obj, is_put, inventory_owner, surface_height_override=None):
        super().__init__(obj, is_put)
        self._sim = sim
        self._inventory_owner = inventory_owner
        self._custom_constraint = inventory_owner.get_inventory_access_constraint(sim, is_put, obj)
        self._custom_animation = inventory_owner.get_inventory_access_animation(is_put)
        self._surface_height_override = surface_height_override

    @property
    def surface_height(self) -> str:
        if self._surface_height_override is not None:
            return self._surface_height_override
        if self._inventory_owner.is_sim:
            return 'inventory'
        return 'high'

    def carry_event_callback--- This code section failed: ---

 L. 282         0  LOAD_FAST                'self'
                2  LOAD_ATTR                _put
                4  POP_JUMP_IF_FALSE    24  'to 24'

 L. 283         6  LOAD_FAST                'self'
                8  LOAD_ATTR                _inventory_owner
               10  LOAD_ATTR                inventory_component
               12  LOAD_METHOD              system_add_object
               14  LOAD_FAST                'self'
               16  LOAD_ATTR                _obj
               18  CALL_METHOD_1         1  '1 positional argument'
               20  POP_TOP          
               22  JUMP_FORWARD         24  'to 24'
             24_0  COME_FROM            22  '22'
             24_1  COME_FROM             4  '4'

Parse error at or near `COME_FROM' instruction at offset 24_0


class CarrySystemDestroyTarget(CarrySystemCustomAnimationTarget):

    @property
    def surface_height(self) -> str:
        return 'high'

    def carry_event_callback(self, *_, **__):
        self._obj.remove_from_client()


class CarryPosture(postures.posture.Posture):
    INSTANCE_SUBCLASSES_ONLY = True
    _XEVT_ID = None
    IS_BODY_POSTURE = False

    @constproperty
    def mobile():
        return True

    @classmethod
    def post_load(cls, manager):
        species_to_provided_postures = {}
        for species, provided_postures, _ in cls._animation_data.get_supported_postures_gen():
            species_to_provided_postures[species] = provided_postures

        cls._provided_postures = frozendict(species_to_provided_postures)
        if cls.prebuild_boundary_conditions:
            cls.build_boundary_conditions()

    @classmethod
    def _tuning_loaded_callback(cls):
        services.get_instance_manager(sims4.resources.Types.POSTURE).add_on_load_complete(cls.post_load)

    @flexmethod
    def get_provided_postures(cls, inst, *args, species=Species.HUMAN, **kwargs):
        inst_or_cls = inst if inst is not None else cls
        return inst_or_cls._provided_postures[species]

    def _event_handler_start_pose(self, *args, **kwargs):
        arb = animation.arb.Arb()
        self.asm.request(self._state_name, arb)
        distribute_arb_element(arb)

    def append_transition_to_arb(self, arb, source_posture, in_xevt_handler=False, **kwargs):
        self.asm.context.register_custom_event_handler((functools.partial(hide_held_props, self.sim)), None,
          0, allow_stub_creation=True)
        (super().append_transition_to_arb)(arb, source_posture, **kwargs)
        if in_xevt_handler:
            self.asm.request(self._state_name, arb)
        else:
            arb.register_event_handler(self._event_handler_start_pose, animation.ClipEventType.Script, self._XEVT_ID)

    @property
    def slot_constraint(self):
        pass


class CarryingNothing(CarryPosture):
    _XEVT_ID = SCRIPT_EVENT_ID_STOP_CARRY
    INSTANCE_TUNABLES = {'_animation_data': AnimationDataUniversal.TunableFactory(animation_data_options={'locked_args': {'_idle_animation': None}},
                          tuning_group=(GroupNames.ANIMATION))}

    def _setup_asm_carry_parameter(self, asm, target):
        if not asm.set_parameter(PARAM_CARRY_TRACK, self.track.name.lower()):
            logger.warn('Failed to set {} on {}.', PARAM_CARRY_TRACK, asm.name)

    @property
    def source_interaction(self):
        pass

    @source_interaction.setter
    def source_interaction(self, value):
        pass

    def append_transition_to_arb(self, arb, source_posture, in_xevt_handler=False, locked_params=frozendict(), **kwargs):
        if source_posture is not None:
            target = source_posture.target
            if target is not None:
                target_anim_overrides = target.get_anim_overrides(source_posture.get_target_name())
                locked_params += target_anim_overrides.params
                self.asm.set_actor(source_posture.get_target_name(), source_posture.target)
        objects_to_find = []
        for object_id in arb.actor_ids:
            object_found = services.object_manager().get(object_id)
            if object_found is not None and object_found.carryable_component is not None:
                objects_to_find.append(object_found)

        for object_found in objects_to_find:
            if in_xevt_handler:
                object_found.carryable_component.on_object_uncarry(self.sim)
            else:
                arb.register_event_handler(lambda *args, **kwargs: (object_found.carryable_component.on_object_uncarry)(self.sim, *args, **kwargs), animation.ClipEventType.Script, SCRIPT_EVENT_ID_STOP_CARRY)

        (super().append_transition_to_arb)(arb, source_posture, locked_params=locked_params, in_xevt_handler=in_xevt_handler, **kwargs)

    def _update_non_body_posture_asm(self):
        pass


class CarryingObject(CarryPosture):
    _XEVT_ID = SCRIPT_EVENT_ID_START_CARRY
    INSTANCE_TUNABLES = {'_animation_data': AnimationDataByActorSpecies.TunableFactory(animation_data_options={'locked_args': {'_idle_animation': None}},
                          tuning_group=(GroupNames.ANIMATION))}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.holster_count = 0
        self.carry_system_target = None

    @property
    def is_two_handed_carry(self):
        return False

    @property
    def holstered(self):
        if self.holster_count:
            return True
        return False

    def _setup_asm_carry_parameter(self, asm, target):
        set_carry_track_param(asm, self.get_target_name(target=target), target, self.track)
        f1 = self.sim.forward
        f2 = -target.forward
        angle = sims4.math.vector3_angle(f1) - sims4.math.vector3_angle(f2)
        if angle > sims4.math.PI:
            angle = angle - sims4.math.TWO_PI
        else:
            if angle < -sims4.math.PI:
                angle = sims4.math.TWO_PI + angle
        angle = sims4.math.rad_to_deg(angle)
        asm.set_parameter('RelativePickUpAngle', angle)

    def add_transition_extras(self, sequence, **kwargs):
        return with_sim_focus(self.sim, self.sim, self.target, SimFocus.LAYER_INTERACTION, sequence)

    @property
    def target_is_transient(self) -> bool:
        if self.target is not None:
            return self.target.transient
        return False

    SNAP_TO_GOOD_LOCATION_SEARCH_FLAGS = placement.FGLSearchFlagsDefault | placement.FGLSearchFlag.SHOULD_TEST_BUILDBUY

    @staticmethod
    def get_good_location_on_floor(target, *, starting_transform, starting_routing_surface, additional_search_flags=0):
        starting_location = placement.create_starting_location(transform=starting_transform, routing_surface=starting_routing_surface)
        if target.is_sim:
            search_flags = FGLSearchFlagsDefaultForSim
            fgl_context_fn = placement.create_fgl_context_for_sim
        else:
            search_flags = FGLSearchFlagsDefault
            fgl_context_fn = placement.create_fgl_context_for_object
        search_flags |= additional_search_flags
        fgl_context = fgl_context_fn(starting_location, target, search_flags=search_flags)
        translation, orientation = placement.find_good_location(fgl_context)
        return (translation, orientation)

    @staticmethod
    def snap_to_good_location_on_floor(target, *args, starting_transform=None, starting_routing_surface=None, **kwargs):
        target.visibility = VisibilityState(True, True, True)
        parent = target.get_parenting_root()
        if starting_transform is None:
            starting_transform = parent.transform
            starting_transform = sims4.math.Transform(parent.position + parent.forward * parent.object_radius, starting_transform.orientation)
        if starting_routing_surface is None:
            starting_routing_surface = parent.routing_surface
        translation = None
        orientation = None
        is_lot_clearing = services.current_zone().is_active_lot_clearing
        if not is_lot_clearing:
            translation, orientation = (CarryingObject.get_good_location_on_floor)(target, *args, starting_transform=starting_transform, starting_routing_surface=starting_routing_surface, **kwargs)
        if translation is not None:
            target.clear_parent(sims4.math.Transform(translation, orientation), starting_routing_surface)
            return True
        logger.debug('snap_to_good_location_on_floor could not find good location for {}.', target)
        clear_transform = starting_transform
        clear_routing_surface = starting_routing_surface
        if not (is_lot_clearing or build_buy.has_floor_at_location(starting_transform.translation, starting_routing_surface.secondary_id)):
            clear_routing_surface = routing.SurfaceIdentifier(services.current_zone_id(), 0, routing.SurfaceType.SURFACETYPE_WORLD)
            ground_position = sims4.math.Vector3(starting_transform.translation.x, starting_transform.translation.y, starting_transform.translation.z)
            ground_position.y = services.terrain_service.terrain_object().get_routing_surface_height_at(starting_transform.translation.x, starting_transform.translation.z, clear_routing_surface)
            clear_transform = sims4.math.Transform(ground_position, starting_transform.orientation)
        target.clear_parent(clear_transform, clear_routing_surface)
        return False

    def setup_asm_posture(self, asm, sim, target, **kwargs):
        result = (super().setup_asm_posture)(asm, sim, target, **kwargs)
        if result:
            if 'locked_params' not in kwargs or 'surfaceHeight' not in kwargs['locked_params']:
                surface_height = get_surface_height_parameter_for_object(target, sim=sim)
                self.asm.set_parameter('surfaceHeight', surface_height)
        return result

    def append_transition_to_arb(self, arb, source_posture, in_xevt_handler=False, locked_params=frozendict(), posture_spec=None, **kwargs):
        if in_xevt_handler:
            locked_params += {'surfaceHeight': 'from_xevt'}
            (super().append_transition_to_arb)(arb, source_posture, locked_params=locked_params, in_xevt_handler=in_xevt_handler, **kwargs)
            if self.target.carryable_component is not None:
                self.target.carryable_component.on_object_carry(self.sim)
            return
            carry_system_target = CarrySystemTerrainTarget(self.sim, self.target, False, self.target.transform)
            if self.target.is_in_inventory():
                if self.target.is_in_sim_inventory():
                    obj_with_inventory = self.target.get_inventory().owner
                else:
                    if posture_spec is not None:
                        surface = posture_spec.surface
                        obj_with_inventory = surface.target
                    else:
                        obj_with_inventory = None
                if obj_with_inventory is None:
                    obj_with_inventory = self.target.get_inventory().owner
                carry_system_target = CarrySystemInventoryTarget(self.sim, self.target, False, obj_with_inventory)
        else:
            runtime_slot = self.target.parent_slot
        if runtime_slot is not None:
            carry_system_target = CarrySystemRuntimeSlotTarget(self.sim, self.target, False, runtime_slot)
        else:
            target_routing_surface = self.target.routing_surface
            if target_routing_surface is not None:
                if target_routing_surface.type == SurfaceType.SURFACETYPE_OBJECT:
                    locked_params += {'surfaceHeight': carry_system_target.surface_height}
            if self.target.parent is not None:
                self.asm.set_actor('surface', self.target.parent)
            call_super = True
            if carry_system_target.has_custom_animation:

                def normal_carry_callback():
                    arb = animation.arb.Arb()
                    self.append_transition_to_arb(arb, source_posture, locked_params=locked_params, in_xevt_handler=True)
                    distribute_arb_element(arb)

                carry_system_target.append_custom_animation_to_arb(arb, self, normal_carry_callback)
                call_super = False
            if self.target.carryable_component is not None:
                arb.register_event_handler(lambda *args, **kwargs: (self.target.carryable_component.on_object_carry)(self.sim, *args, **kwargs), animation.ClipEventType.Script, SCRIPT_EVENT_ID_START_CARRY)
            arb.register_event_handler(carry_system_target.carry_event_callback, animation.ClipEventType.Script, SCRIPT_EVENT_ID_START_CARRY)
            if call_super:
                (super().append_transition_to_arb)(arb, source_posture, locked_params=locked_params, in_xevt_handler=in_xevt_handler, **kwargs)

    def append_exit_to_arb(self, arb, dest_state, dest_posture, var_map, exit_while_holding=False, **kwargs):
        if exit_while_holding:
            self.asm.set_parameter('surfaceHeight', 'from_xevt')
            if self.target_is_transient:
                self.target.remove_from_client()
            if not self.holstered:
                (super().append_exit_to_arb)(arb, dest_state, dest_posture, var_map, **kwargs)
            return
            if self.carry_system_target is None:
                surface, slot_var = dest_state.get_slot_info()
                has_slot_surface = surface is not None and slot_var is not None
                if self.target_is_transient:
                    self.carry_system_target = has_slot_surface or CarrySystemTransientTarget(self.target, True)
        else:
            if slot_var is None:
                self.sim.schedule_reset_asap(cause='slot_var is None in append_exit_to_arb where we expect to be putting an object down in a slot')
                logger.error('slot_var is None in append_exit_to_arb: arb: {} dest_state: {} dest_posture: {} var_map: {} for sim: {} and target: {}', arb,
                  dest_state, dest_posture, var_map, (self.sim), (self.target), owner='bosee')
                return
            self.asm.set_actor('surface', surface)
            if slot_var not in var_map:
                stack_var = StackVar(('slot_var', 'var_map', '_interaction', 'dest_state'))
                raise RuntimeError('Unable to retrieve slot variable: {}'.format(stack_var))
            slot_manifest = var_map[slot_var]
            var_map += {PostureSpecVariable.SURFACE_TARGET: surface}
            slot_manifest = slot_manifest.apply_actor_map(var_map.get)
            runtime_slot = slot_manifest.runtime_slot
            if runtime_slot is None:
                for slot in slot_manifest.target.get_runtime_slots_gen(slot_types=(slot_manifest.slot_types)):
                    if slot.is_valid_for_placement(obj=(self.target)):
                        runtime_slot = slot
                        break
                else:
                    raise RuntimeError('Attempt to create a CarrySystemRuntimeSlotTarget with no valid runtime slot: {}'.format(slot_manifest))

            self.carry_system_target = CarrySystemRuntimeSlotTarget(self.sim, self.target, True, runtime_slot)
        arb.register_event_handler(self.carry_system_target.carry_event_callback, animation.ClipEventType.Script, SCRIPT_EVENT_ID_STOP_CARRY)
        if self.carry_system_target.has_custom_animation:

            def normal_carry_callback():
                arb = animation.arb.Arb()
                self.append_exit_to_arb(arb, dest_state, dest_posture, var_map, exit_while_holding=True)
                distribute_arb_element(arb)

            self.carry_system_target.append_custom_animation_to_arb(arb, self, normal_carry_callback)
            return
        self.asm.set_parameter('surfaceHeight', self.carry_system_target.surface_height)
        (super().append_exit_to_arb)(arb, dest_state, dest_posture, var_map, **kwargs)

    def _drop_carried_object(self):
        if self.target is None:
            return
            if self.target.is_sim:
                return
            if self.target_is_transient or self.target.parent is not self.sim:
                return
            if self.snap_to_good_location_on_floor(self.target):
                return
            if self.sim.household.id is self.target.get_household_owner_id():
                if self.sim.inventory_component.player_try_add_object(self.target):
                    return
            placement_flags = build_buy.get_object_placement_flags(self.target.definition.id)
            if placement_flags & build_buy.PlacementFlags.NON_DELETEABLE:
                if placement_flags & build_buy.PlacementFlags.NON_INVENTORYABLE:
                    logger.error("Failed to find a location to place {}, which cannot be deleted or moved to the household inventory.                           Object will be placed at the Sim's feet, but this is unsafe and will probably result in the object being                           destroyed on load.",
                      (self.target), owner='tastle')
                    return
            if placement_flags & build_buy.PlacementFlags.NON_INVENTORYABLE:
                self.target.destroy(source=(self.sim), cause='Failed to find location to drop non inventoryable object.')
        elif not build_buy.move_object_to_household_inventory((self.target), failure_flags=(HouseholdInventoryFlags.DESTROY_OBJECT)):
            logger.warn('Failed to drop carried object {}, which cannot be placed in the household inventory. This object will be destroyed.', (self.target), owner='rmccord')

    def _on_reset(self):
        super()._on_reset()
        self._drop_carried_object()
