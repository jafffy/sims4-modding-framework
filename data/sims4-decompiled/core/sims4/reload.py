# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\reload.py
# Compiled at: 2018-07-31 22:42:48
# Size of source mod 2**32: 23330 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
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
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr . CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 . RAISE_VARARGS_1
assert2 ::= expr jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1 . 
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assert_invert ::= testtrue LOAD_GLOBAL . RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
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
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
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
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= call . 
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
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jmp_true ::= POP_JUMP_IF_TRUE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
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
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assert2 . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr expr expr . BUILD_TUPLE_4
tuple ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr expr expr BUILD_TUPLE_4 . 
tuple ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr BUILD_TUPLE_13
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
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
   
 L. 121        36  LOAD_CLOSURE             'module_dict'
                  38  BUILD_TUPLE_1         1 
->                40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  42  LOAD_STR                 '_make_hooks_dict.<locals>.<dictcomp>'
                  44  MAKE_FUNCTION_8          'closure'
                  46  LOAD_FAST                'hooks'
                  48  GET_ITER         
                  50  CALL_FUNCTION_1       1  '1 positional argument'
                  52  STORE_FAST               'hooks'
                54_0  COME_FROM            34  '34'

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
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
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr . expr expr expr CALL_METHOD_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
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
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= call . 
expr ::= compare . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jmp_false ::= POP_JUMP_IF_FALSE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
list ::= expr . BUILD_LIST_1
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
set ::= expr . BUILD_SET_1
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
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
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr BUILD_TUPLE_13
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
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
   
 L. 538        50  LOAD_CLOSURE             'oldclass'
                  52  BUILD_TUPLE_1         1 
->                54  LOAD_SETCOMP             '<code_object <setcomp>>'
                  56  LOAD_STR                 '_update_class.<locals>.<setcomp>'
                  58  MAKE_FUNCTION_8          'closure'
                  60  LOAD_FAST                'oldslots'
                  62  GET_ITER         
                  64  CALL_FUNCTION_1       1  '1 positional argument'
                  66  STORE_FAST               'slots'
from _pyio import StringIO
from contextlib import contextmanager
import _pythonutils, imp, linecache, marshal, operator, os.path, sys, types
from sims4.utils import flexproperty, flexmethod, classproperty
import enum, sims4.log
set_function_closure = _pythonutils.set_function_closure
logger = sims4.log.Logger('Reload', default_owner='bhill')
SUPPORTED_BUILTIN_MODULES = ('builtins', 'collections', 'operator')
SUPPORTED_BUILTIN_TYPES = (int, float, complex, str, list, tuple, bytearray,
 set, frozenset, dict, operator.itemgetter,
 operator.attrgetter, operator.methodcaller)
SUPPORTED_CUSTOM_METACLASSES = (enum.Metaclass,)
SUPPORTED_CUSTOM_TYPES = (sims4.log.Logger,)
IMMUTABLE_CLASS_ATTRIBUTES = ('__dict__', '__doc__', '__slots__', '__weakref__', '__mro__',
                              '__reload_as__')

def _make_hooks_dict--- This code section failed: ---

 L. 118         0  LOAD_GLOBAL              isinstance
                2  LOAD_FAST                'hooks'
                4  LOAD_GLOBAL              dict
                6  LOAD_GLOBAL              tuple
                8  LOAD_GLOBAL              set
               10  LOAD_GLOBAL              list
               12  BUILD_TUPLE_4         4 
               14  CALL_FUNCTION_2       2  '2 positional arguments'
               16  POP_JUMP_IF_TRUE     26  'to 26'

 L. 119        18  LOAD_GLOBAL              TypeError
               20  LOAD_STR                 '__reload_hooks__ must be a list of global variable names or a dict of names to reload hooks'
               22  CALL_FUNCTION_1       1  '1 positional argument'
               24  RAISE_VARARGS_1       1  'exception instance'
             26_0  COME_FROM            16  '16'

 L. 120        26  LOAD_GLOBAL              isinstance
               28  LOAD_FAST                'hooks'
               30  LOAD_GLOBAL              dict
               32  CALL_FUNCTION_2       2  '2 positional arguments'
               34  POP_JUMP_IF_TRUE     54  'to 54'

 L. 121        36  LOAD_CLOSURE             'module_dict'
               38  BUILD_TUPLE_1         1 
               40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               42  LOAD_STR                 '_make_hooks_dict.<locals>.<dictcomp>'
               44  MAKE_FUNCTION_8          'closure'
               46  LOAD_FAST                'hooks'
               48  GET_ITER         
               50  CALL_FUNCTION_1       1  '1 positional argument'
               52  STORE_FAST               'hooks'
             54_0  COME_FROM            34  '34'

 L. 122        54  LOAD_FAST                'hooks'
               56  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_DICTCOMP' instruction at offset 40


@contextmanager
def protected(globals):
    old_names = set(globals.keys())
    try:
        yield
    finally:
        new_names = set(globals.keys()) - old_names
        if new_names:
            hooks = globals.get('__reload_hooks__', {})
            hooks = _make_hooks_dicthooksglobals
            for name in new_names:
                hooks[name] = None

            globals['__reload_hooks__'] = hooks


with protected(globals()):
    _reload_serial_number = 0
    currently_reloading = 0
_reload_object_stack = []

def reload_module(module):
    modname = module.__name__
    i = modname.rfind('.')
    if i >= 0:
        pkgname, modname = modname[:i], modname[i + 1:]
    else:
        pkgname = None
    if pkgname:
        pkg = sys.modules[pkgname]
        path = pkg.__path__
    else:
        pkg = None
        path = None
    stream, filename, (_, _, kind) = imp.find_module(modname, path)
    return _reload(module, filename, stream, kind)


def reload_module_from_file(module, filename):
    kind = imp.PY_SOURCE if filename.endswith('.py') else imp.PY_COMPILED
    stream = open(filename)
    module = _reload(module, filename, stream, kind)
    if module is not None:
        module = filename
    return module


def reload_module_from_string(module, source):
    stream = StringIO(source)
    filename = module.__dict__['__file__']
    kind = imp.PY_SOURCE
    return _reload(module, filename, stream, kind)


def get_module_for_filename(filename):
    module = None
    for _module in sys.modules.values():
        _filename = _module.__dict__.get('__file__')
        if _filename is not None and os.path.normcase(_filename) == os.path.normcase(filename):
            module = _module
            break

    return module


def reload_file(filename):
    import sims4.tuning.serialization
    module = get_module_for_filename(filename)
    if module is None:
        logger.error('{0} is not currently loaded as a module.', filename)
        return
    kind = imp.PY_SOURCE if filename.endswith('.py') else imp.PY_COMPILED
    stream = open(filename)
    reloaded_module = _reload(module, filename, stream, kind)
    try:
        sims4.tuning.serialization.process_tuning(module)
    except:
        logger.exception('Exception while reloading module tuning for {0}', filename)

    linecache.checkcache(filename)
    return reloaded_module


def _reload(module, filename, stream, kind):
    global _reload_serial_number
    global currently_reloading
    currently_reloading += 1
    _reload_serial_number += 1
    try:
        modns = module.__dict__
        try:
            if kind not in (imp.PY_COMPILED, imp.PY_SOURCE):
                raise NotImplementedError('Reloading non-source or byte code files is currently unimplemented.')
            elif kind == imp.PY_SOURCE:
                source = stream.read()
                code = compile(source, filename, 'exec')
            else:
                code = marshal.load(stream)
        finally:
            if stream:
                stream.close()

        tmpns = modns.copy()
        modns.clear()
        modns['__name__'] = tmpns['__name__']
        modns['__file__'] = tmpns['__file__']
        execcodemodns
        update_module_dicttmpnsmodns
        return module
    finally:
        currently_reloading -= 1


def update_module_dict(tmpns, modns):
    oldnames = set(tmpns)
    newnames = set(modns)
    update_names = oldnames & newnames
    delete_names = oldnames - newnames
    hooked_names = ()
    hooks = modns.get('__reload_hooks__')
    if hooks is not None:
        hooks = _make_hooks_dicthooksmodns
        hooked_names = hooks.keys() & update_names
        update_names = update_names - hooked_names
    for name in update_names:
        modns[name] = _updatetmpns[name]modns[name]

    for name in delete_names:
        oldobj = tmpns[name]
        if isinstanceoldobjtypes.ModuleType:
            logger.warn('Preserving old sub-module: {} ({})', name, oldobj)
            modns[name] = oldobj

    for name in hooked_names:
        hook = hooks[name]
        if hook is not None:
            modns[name] = hook(tmpns[name], modns[name], _update)
        else:
            modns[name] = tmpns[name]


def _getattr_exact(obj, name, default=None):
    try:
        vars_obj = vars(obj)
    except TypeError:
        return default
    else:
        return vars_obj.get(name, default)


def _log_reload_position(obj):
    lines = str(obj).splitlines()
    for line in lines:
        line = line.strip()
        if line:
            break

    if len(lines) > 1:
        line += '...'
    logger.warn('{}{}', '  ' * len(_reload_object_stack), line)


def _update_reload_mark(oldobj, newobj):
    if _reload_serial_number == 0:
        return
    old_mark = _getattr_exact(oldobj, '__reload_mark__', 0)
    new_mark = _getattr_exact(newobj, '__reload_mark__', 0)
    if old_mark == _reload_serial_number:
        logger.warn('Updating an object of type {0} multiple times. (Value: {1})', type(oldobj), oldobj)
    else:
        if new_mark == _reload_serial_number:
            logger.error('Visiting an object of type {0} multiple times before it has finished updating. (Value: {1})', type(newobj), newobj)
        else:
            try:
                setattr(newobj, '__reload_mark__', _reload_serial_number)
            except (AttributeError, TypeError):
                pass


def _update(oldobj, newobj):
    try:
        _reload_object_stack.append(newobj)
        if oldobj is newobj:
            return newobj
            reload_as = _getattr_exactnewobj'__reload_as__'
            if reload_as is not None:
                return reload_as
            _update_reload_markoldobjnewobj
            if isinstancenewobjtype:
                if hasattrnewobj'__reload_update_class__':
                    return newobj.__reload_update_class__(oldobj, newobj, _update)
                if hasattroldobj'__reload_update_class__':
                    return oldobj.__reload_update_class__(oldobj, newobj, _update)
        else:
            if hasattrnewobj'__reload_update__':
                return newobj.__reload_update__(oldobj, newobj, _update)
            if hasattroldobj'__reload_update__':
                return oldobj.__reload_update__(oldobj, newobj, _update)
        reload_context = _getattr_exactnewobj'__reload_context__'
        if reload_context is None:
            reload_context = _getattr_exactoldobj'__reload_context__'
        if reload_context is not None:
            with reload_contextoldobjnewobj:
                return __updateoldobjnewobj
        return __updateoldobjnewobj
    finally:
        _reload_object_stack.pop()


def _is_supported_as_literal_value(newobj):
    if type(newobj).__module__ in SUPPORTED_BUILTIN_MODULES:
        if isinstancenewobjSUPPORTED_BUILTIN_TYPES:
            return True
    if isinstancenewobjSUPPORTED_CUSTOM_TYPES:
        return True
    if isinstancetype(newobj)SUPPORTED_CUSTOM_METACLASSES:
        return True
    return False


def _check_unupdated_newobj(newobj, what):
    if _is_supported_as_literal_value(newobj):
        logger.debug('Reloading {2} of type {0}. (New value: {1})', type(newobj), newobj, what)
    else:
        logger.warn('Leaking new {0} into old module while reloading {2}.  As long as this type is equivalent to a literal value, this is probably ok. (Value: {1})', type(newobj), newobj, what)


def __update(oldobj, newobj):
    if type(oldobj) is not type(newobj):
        return newobj
    if isinstancenewobjtype:
        return _update_classoldobjnewobj
    if isinstancenewobjtypes.FunctionType:
        return _update_functionoldobjnewobj
    if isinstancenewobjtypes.MethodType:
        return _update_methodoldobjnewobj
    if isinstancenewobjclassmethod:
        return _update_classmethodoldobjnewobj
    if isinstancenewobjstaticmethod:
        return _update_staticmethodoldobjnewobj
    if isinstancenewobjproperty:
        return _update_propertyoldobjnewobj
    if isinstancenewobjflexmethod:
        return _update_flexmethodoldobjnewobj
    if isinstancenewobjflexproperty:
        return _update_flexpropertyoldobjnewobj
    if isinstancenewobjclassproperty:
        return _update_classpropertyoldobjnewobj
    _check_unupdated_newobjnewobj'global/static member'
    return newobj


def _update_property(oldprop, newprop):
    _updateoldprop.fgetnewprop.fget
    _updateoldprop.fsetnewprop.fset
    _updateoldprop.fdelnewprop.fdel
    return oldprop


def _update_flexproperty(oldprop, newprop):
    _updateoldprop.fgetnewprop.fget
    return oldprop


def _update_classproperty(oldprop, newprop):
    _updateoldprop.fgetnewprop.fget
    return oldprop


def _update_function(oldfunc, newfunc):
    newfunc.__reload_as__ = oldfunc
    olddict = oldfunc.__dict__
    newdict = newfunc.__dict__
    for name in newdict.keys() - olddict.keys() - {'__reload_as__'}:
        setattr(oldfunc, name, newdict[name])

    for name in olddict.keys() - newdict.keys() - {'__reload_as__'}:
        delattroldfuncname

    for name in (olddict.keys() & newdict.keys()) - {'__reload_as__'}:
        setattr(oldfunc, name, _updateolddict[name]newdict[name])

    set_function_closureoldfuncnewfunc
    oldfunc.__code__ = newfunc.__code__
    oldfunc.__defaults__ = newfunc.__defaults__
    return oldfunc


def _update_method(oldmeth, newmeth):
    if hasattroldmeth'im_func':
        _updateoldmeth.im_funcnewmeth.im_func
    else:
        if hasattroldmeth'__func__':
            _updateoldmeth.__func__newmeth.__func__
        else:
            logger.error('Method {} has no im_func or __func__.', oldmeth)
    return oldmeth


def _get_slots_list_or_none(cls):
    if not hasattrcls'__slots__':
        return
    slots = cls.__slots__
    if isinstanceslotsstr:
        return [
         slots]
    return slots


def _mangle_attribute_name(cls, attr):
    if attr.startswith('__'):
        if not attr.endswith('__'):
            classname = cls.__name__.lstrip('_')
            if classname:
                return '_{0}{1}'.format(classname, attr)
    return attr


def _update_class--- This code section failed: ---

 L. 525         0  LOAD_DEREF               'oldclass'
                2  LOAD_FAST                'newclass'
                4  STORE_ATTR               __reload_as__

 L. 527         6  LOAD_DEREF               'oldclass'
                8  LOAD_ATTR                __dict__
               10  STORE_FAST               'olddict'

 L. 528        12  LOAD_FAST                'newclass'
               14  LOAD_ATTR                __dict__
               16  STORE_FAST               'newdict'

 L. 529        18  LOAD_GLOBAL              set
               20  LOAD_GLOBAL              IMMUTABLE_CLASS_ATTRIBUTES
               22  CALL_FUNCTION_1       1  '1 positional argument'
               24  STORE_FAST               'immutables'

 L. 531        26  LOAD_GLOBAL              _get_slots_list_or_none
               28  LOAD_DEREF               'oldclass'
               30  CALL_FUNCTION_1       1  '1 positional argument'
               32  STORE_FAST               'oldslots'

 L. 532        34  LOAD_GLOBAL              _get_slots_list_or_none
               36  LOAD_FAST                'newclass'
               38  CALL_FUNCTION_1       1  '1 positional argument'
               40  STORE_FAST               'newslots'

 L. 535        42  LOAD_FAST                'oldslots'
               44  LOAD_CONST               None
               46  COMPARE_OP               is-not
               48  POP_JUMP_IF_FALSE    76  'to 76'

 L. 538        50  LOAD_CLOSURE             'oldclass'
               52  BUILD_TUPLE_1         1 
               54  LOAD_SETCOMP             '<code_object <setcomp>>'
               56  LOAD_STR                 '_update_class.<locals>.<setcomp>'
               58  MAKE_FUNCTION_8          'closure'
               60  LOAD_FAST                'oldslots'
               62  GET_ITER         
               64  CALL_FUNCTION_1       1  '1 positional argument'
               66  STORE_FAST               'slots'

 L. 539        68  LOAD_FAST                'immutables'
               70  LOAD_FAST                'slots'
               72  INPLACE_OR       
               74  STORE_FAST               'immutables'
             76_0  COME_FROM            48  '48'

 L. 541        76  LOAD_GLOBAL              set
               78  LOAD_FAST                'olddict'
               80  CALL_FUNCTION_1       1  '1 positional argument'
               82  LOAD_FAST                'immutables'
               84  BINARY_SUBTRACT  
               86  STORE_FAST               'oldnames'

 L. 542        88  LOAD_GLOBAL              set
               90  LOAD_FAST                'newdict'
               92  CALL_FUNCTION_1       1  '1 positional argument'
               94  LOAD_FAST                'immutables'
               96  BINARY_SUBTRACT  
               98  STORE_FAST               'newnames'

 L. 543       100  SETUP_LOOP          134  'to 134'
              102  LOAD_FAST                'newnames'
              104  LOAD_FAST                'oldnames'
              106  BINARY_SUBTRACT  
              108  GET_ITER         
              110  FOR_ITER            132  'to 132'
              112  STORE_FAST               'name'

 L. 544       114  LOAD_GLOBAL              setattr
              116  LOAD_DEREF               'oldclass'
              118  LOAD_FAST                'name'
              120  LOAD_FAST                'newdict'
              122  LOAD_FAST                'name'
              124  BINARY_SUBSCR    
              126  CALL_FUNCTION_3       3  '3 positional arguments'
              128  POP_TOP          
              130  JUMP_BACK           110  'to 110'
              132  POP_BLOCK        
            134_0  COME_FROM_LOOP      100  '100'

 L. 545       134  SETUP_LOOP          162  'to 162'
              136  LOAD_FAST                'oldnames'
              138  LOAD_FAST                'newnames'
              140  BINARY_SUBTRACT  
              142  GET_ITER         
              144  FOR_ITER            160  'to 160'
              146  STORE_FAST               'name'

 L. 546       148  LOAD_GLOBAL              delattr
              150  LOAD_DEREF               'oldclass'
              152  LOAD_FAST                'name'
              154  CALL_FUNCTION_2       2  '2 positional arguments'
              156  POP_TOP          
              158  JUMP_BACK           144  'to 144'
              160  POP_BLOCK        
            162_0  COME_FROM_LOOP      134  '134'

 L. 547       162  SETUP_LOOP          206  'to 206'
              164  LOAD_FAST                'oldnames'
              166  LOAD_FAST                'newnames'
              168  BINARY_AND       
              170  GET_ITER         
              172  FOR_ITER            204  'to 204'
              174  STORE_FAST               'name'

 L. 548       176  LOAD_GLOBAL              setattr
              178  LOAD_DEREF               'oldclass'
              180  LOAD_FAST                'name'
              182  LOAD_GLOBAL              _update
              184  LOAD_FAST                'olddict'
              186  LOAD_FAST                'name'
              188  BINARY_SUBSCR    
              190  LOAD_FAST                'newdict'
              192  LOAD_FAST                'name'
              194  BINARY_SUBSCR    
              196  CALL_FUNCTION_2       2  '2 positional arguments'
              198  CALL_FUNCTION_3       3  '3 positional arguments'
              200  POP_TOP          
              202  JUMP_BACK           172  'to 172'
              204  POP_BLOCK        
            206_0  COME_FROM_LOOP      162  '162'

 L. 549       206  LOAD_DEREF               'oldclass'
              208  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_SETCOMP' instruction at offset 54


def _update_classmethod(oldcm, newcm):
    _updateoldcm.__get__(0)newcm.__get__(0)
    return oldcm


def _update_staticmethod(oldsm, newsm):
    _updateoldsm.__get__(0)newsm.__get__(0)
    return oldsm


def _update_flexmethod(oldfm, newfm):
    oldfm.__wrapped_method__ = _updateoldfm.__wrapped_method__newfm.__wrapped_method__
    return oldfm
