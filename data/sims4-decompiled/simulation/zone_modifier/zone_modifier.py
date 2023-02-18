# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\zone_modifier\zone_modifier.py
# Compiled at: 2021-03-02 22:34:56
# Size of source mod 2**32: 22872 bytes

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
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
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
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg CALL_FUNCTION_1 . 
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
call_stmt ::= expr . POP_TOP
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
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_19
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_19
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
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
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
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
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= ifelsestmt . 
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
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
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
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 411        62  LOAD_CLOSURE             'cls'
                  64  LOAD_CLOSURE             'curr_obj_tag_id_to_count'
                  66  BUILD_TUPLE_2         2 
->                68  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  70  LOAD_STR                 'ZoneModifier.apply_object_actions.<locals>.<dictcomp>'
                  72  MAKE_FUNCTION_8          'closure'
from event_testing.tests_with_data import InteractionTestEvents
from interactions.utils.loot import LootActions
from objects import ALL_HIDDEN_REASONS
from sims.household_utilities.utility_types import Utilities
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import HasTunableReference, TunableSet, TunableList, Tunable, OptionalTunable, TunableReference, TunableVariant, TunableMapping, TunableEnumEntry
from sims4.tuning.tunable_base import ExportModes, GroupNames
from sims4.utils import classproperty
from situations.situation_curve import SituationCurve
from tag import TunableTag, Tag
from tunable_utils.taggables_tests import SituationIdentityTest
from zone_modifier.zone_modifier_actions import ZoneInteractionTriggers, ZoneModifierWeeklySchedule, ZoneModifierUpdateAction
from zone_modifier.zone_modifier_from_objects_actions import ZoneModifierFromObjectsActionVariants, ZoneModifierFromObjectsActionType
from zone_modifier.zone_modifier_household_actions import ZoneModifierHouseholdActionVariants
import collections, services, sims4.resources
logger = sims4.log.Logger('ZoneModifier', default_owner='bnguyen')

class ZoneModifier(HasTunableReference, metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.ZONE_MODIFIER)):
    INSTANCE_TUNABLES = {'zone_modifier_locked':Tunable(description='\n            Whether this is a locked trait that cannot be assigned/removed\n            through build/buy.\n            ',
       tunable_type=bool,
       default=False,
       export_modes=ExportModes.All,
       tuning_group=GroupNames.UI), 
     'enter_lot_loot':TunableSet(description='\n            Loot applied to Sims when they enter or spawn in on the lot while\n            this zone modifier is active.\n            \n            NOTE: The corresponding exit loot is not guaranteed to be given.\n            For example, if the Sim walks onto the lot, player switches to a\n            different zone, then summons that Sim, that Sim will bypass\n            getting the exit loot.\n            A common use case for exit lot loot is to remove buffs granted\n            by this zone_mod.  This case is already covered as buffs are \n            automatically removed if they are non-persistable (have no associated commodity)\n            ',
       tunable=LootActions.TunableReference(pack_safe=True),
       tuning_group=GroupNames.LOOT), 
     'exit_lot_loot':TunableSet(description='\n            Loot applied to Sims when they exit or spawn off of the lot while\n            this zone modifier is active.\n            \n            NOTE: This loot is not guaranteed to be given after the enter loot.\n            For example, if the Sim walks onto the lot, player switches to a\n            different zone, then summons that Sim, that Sim will bypass\n            getting the exit loot.\n            A common use case for exit lot loot is to remove buffs granted\n            by this zone_mod.  This case is already covered as buffs are \n            automatically removed if they are non-persistable (have no associated commodity)\n            ',
       tunable=LootActions.TunableReference(pack_safe=True),
       tuning_group=GroupNames.LOOT), 
     'interaction_triggers':TunableList(description='\n            A mapping of interactions to possible loots that can be applied\n            when an on-lot Sim executes them if this zone modifier is set.\n            ',
       tunable=ZoneInteractionTriggers.TunableFactory()), 
     'schedule':ZoneModifierWeeklySchedule.TunableFactory(description='\n            Schedule to be activated for this particular zone modifier.\n            '), 
     'household_actions':TunableList(description='\n            Actions to apply to the household that owns this lot when this zone\n            modifier is set.\n            ',
       tunable=ZoneModifierHouseholdActionVariants(description='\n                The action to apply to the household.\n                ')), 
     'object_tag_to_actions':TunableMapping(description='\n            Mapping of object tag to zone modifier from object actions. Objects \n            in this tuning can be buy objects, build objects (column, window, pool),\n            and materials (floor tiles, roof tiles, wallpaper).\n            \n            This is primarily intended for architectural elements such as wallpaper, \n            roof materials, windows will give effect to utilities and eco footprint.\n            \n            All actions will always be applied to the current lot.\n            \n            NOTE: The actions will only be applied if user enables the \n            "Architecture Affects Eco Living" option under Game Options.\n            ',
       key_type=TunableTag(description='\n                The object tag that will be used to do actions.\n                '),
       value_type=TunableList(description='\n                The list of action to apply.\n                ',
       tunable=(ZoneModifierFromObjectsActionVariants()))), 
     'prohibited_situations':OptionalTunable(description='\n            Optionally define if this zone should prevent certain situations\n            from running or getting scheduled.\n            ',
       tunable=SituationIdentityTest.TunableFactory(description='\n                Prevent a situation from running if it is one of the specified \n                situations or if it contains one of the specified tags.\n                ')), 
     'venue_requirements':TunableVariant(description='\n            Whether or not we use a blacklist or white list for the venue\n            requirements on this zone modifier.\n            ',
       allowed_venue_types=TunableSet(description='\n                A list of venue types that this Zone Modifier can be placed on.\n                All other venue types are not allowed.\n                ',
       tunable=TunableReference(description='\n                    A venue type that this Zone Modifier can be placed on.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.VENUE)),
       pack_safe=True)),
       prohibited_venue_types=TunableSet(description='\n                A list of venue types that this Zone Modifier cannot be placed on.\n                ',
       tunable=TunableReference(description='\n                    A venue type that this Zone Modifier cannot be placed on.\n                    ',
       manager=(services.get_instance_manager(sims4.resources.Types.VENUE)),
       pack_safe=True)),
       export_modes=ExportModes.All), 
     'conflicting_zone_modifiers':TunableSet(description='\n            Conflicting zone modifiers for this zone modifier. If the lot has any of the\n            specified zone modifiers, then it is not allowed to be equipped with this\n            one.\n            ',
       tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.ZONE_MODIFIER)),
       pack_safe=True),
       export_modes=ExportModes.All), 
     'additional_situations':SituationCurve.TunableFactory(description="\n            An additional schedule of situations that can be added in addition\n            a situation scheduler's source tuning.\n            ",
       get_create_params={'user_facing': False}), 
     'zone_wide_loot':ZoneModifierUpdateAction.TunableFactory(description='\n            Loots applied when spawning into a zone with \n            this zone modifier. This loot is also applied to all sims, \n            objects, etc. in the zone when this zone modifier is added to a lot.\n            ',
       tuning_group=GroupNames.LOOT), 
     'cleanup_loot':ZoneModifierUpdateAction.TunableFactory(description='\n            Loots applied when this zone modifier is removed.\n            ',
       tuning_group=GroupNames.LOOT), 
     'on_add_loot':ZoneModifierUpdateAction.TunableFactory(description='\n            Loots applied when this zone modifier is added.\n            ',
       tuning_group=GroupNames.LOOT), 
     'spin_up_lot_loot':ZoneModifierUpdateAction.TunableFactory(description='\n            Loots applied when the zone spins up.\n            ',
       tuning_group=GroupNames.LOOT), 
     'utility_supply_surplus_loot':TunableMapping(description='\n            Loots applied when utility supply statistic change\n            from deficit to surplus.\n            ',
       key_type=TunableEnumEntry(description='\n                The utility that we want to listen for supply change.\n                ',
       tunable_type=Utilities,
       default=(Utilities.POWER)),
       value_type=ZoneModifierUpdateAction.TunableFactory(description='\n                Loots to apply.\n                '),
       tuning_group=GroupNames.LOOT), 
     'utility_supply_deficit_loot':TunableMapping(description='\n            Loots applied when utility supply statistic change\n            from surplus to deficit.\n            ',
       key_type=TunableEnumEntry(description='\n                The utility that we want to listen for supply change.\n                ',
       tunable_type=Utilities,
       default=(Utilities.POWER)),
       value_type=ZoneModifierUpdateAction.TunableFactory(description='\n                Loots to apply.\n                '),
       tuning_group=GroupNames.LOOT), 
     'ignore_route_events_during_zone_spin_up':Tunable(description="\n            Don't handle sim route events during zone spin up.  Useful for preventing\n            unwanted loot from being applied when enter_lot_loot runs situation blacklist tests.\n            If we require sims to retrieve loot on zone spin up, we can tune spin_up_lot_loot. \n            ",
       tunable_type=bool,
       default=False), 
     'hide_screen_slam':Tunable(description='\n            If checked, this zone modifier will not show the usual screen slam\n            when first applied.\n            ',
       tunable_type=bool,
       default=False,
       tuning_group=GroupNames.UI)}
    _obj_tag_id_to_count = None

    @classproperty
    def obj_tag_id_to_count(cls):
        return cls._obj_tag_id_to_count

    @classmethod
    def on_start_actions(cls):
        cls.register_interaction_triggers()

    @classmethod
    def on_spin_up_actions(cls, is_build_eco_effects_enabled):
        sim_spawner_service = services.sim_spawner_service()
        if not sim_spawner_service.is_registered_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim):
            sim_spawner_service.register_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim)
        cls.spin_up_lot_loot.apply_all_actions()
        cls.zone_wide_loot.apply_all_actions()
        cls.apply_object_actions(is_build_eco_effects_enabled)

    @classmethod
    def on_add_actions(cls, is_build_eco_effects_enabled):
        sim_spawner_service = services.sim_spawner_service()
        if not sim_spawner_service.is_registered_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim):
            sim_spawner_service.register_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim)
        cls.register_interaction_triggers()
        cls.start_household_actions()
        cls.on_add_loot.apply_all_actions()
        cls.zone_wide_loot.apply_all_actions()
        cls.apply_object_actions(is_build_eco_effects_enabled)

    @classmethod
    def on_stop_actions(cls):
        services.sim_spawner_service().unregister_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim)
        cls.unregister_interaction_triggers()
        cls.stop_household_actions()
        cls.revert_object_actions()

    @classmethod
    def on_remove_actions(cls):
        services.sim_spawner_service().unregister_sim_spawned_callback(cls.zone_wide_loot.apply_to_sim)
        cls.unregister_interaction_triggers()
        cls.stop_household_actions()
        cls.cleanup_loot.apply_all_actions()
        cls.revert_object_actions()

    @classmethod
    def on_utility_supply_surplus(cls, utility):
        if utility in cls.utility_supply_surplus_loot:
            cls.utility_supply_surplus_loot[utility].apply_all_actions()

    @classmethod
    def on_utility_supply_deficit(cls, utility):
        if utility in cls.utility_supply_deficit_loot:
            cls.utility_supply_deficit_loot[utility].apply_all_actions()

    @classmethod
    def handle_event(cls, sim_info, event, resolver):
        if event not in InteractionTestEvents:
            return
        else:
            sim = sim_info.get_sim_instance()
            return sim is None or sim.is_on_active_lot() or None
        for trigger in cls.interaction_triggers:
            trigger.handle_interaction_event(sim_info, event, resolver)

    @classmethod
    def start_household_actions(cls):
        if not cls.household_actions:
            return
        household_id = services.owning_household_id_of_active_lot()
        if household_id is not None:
            for household_action in cls.household_actions:
                household_action.start_action(household_id)

    @classmethod
    def stop_household_actions(cls):
        if not cls.household_actions:
            return
        household_id = services.owning_household_id_of_active_lot()
        if household_id is not None:
            for household_action in cls.household_actions:
                household_action.stop_action(household_id)

    @classmethod
    def _on_build_objects_environment_score_update(cls):
        household = services.active_household()
        if household is None:
            return
        for sim in household.instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS):
            sim.on_build_objects_environment_score_update()

    @classmethod
    def apply_object_actions--- This code section failed: ---

 L. 396         0  LOAD_FAST                'is_build_eco_effects_enabled'
                2  POP_JUMP_IF_TRUE      8  'to 8'

 L. 397         4  LOAD_CONST               None
                6  RETURN_VALUE     
              8_0  COME_FROM             2  '2'

 L. 400         8  LOAD_DEREF               'cls'
               10  LOAD_ATTR                object_tag_to_actions
               12  POP_JUMP_IF_TRUE     18  'to 18'

 L. 401        14  LOAD_CONST               None
               16  RETURN_VALUE     
             18_0  COME_FROM            12  '12'

 L. 404        18  LOAD_GLOBAL              list
               20  LOAD_DEREF               'cls'
               22  LOAD_ATTR                object_tag_to_actions
               24  LOAD_METHOD              keys
               26  CALL_METHOD_0         0  '0 positional arguments'
               28  CALL_FUNCTION_1       1  '1 positional argument'
               30  STORE_FAST               'object_tags'

 L. 405        32  LOAD_GLOBAL              services
               34  LOAD_METHOD              active_lot
               36  CALL_METHOD_0         0  '0 positional arguments'
               38  LOAD_METHOD              get_object_count_by_tags
               40  LOAD_FAST                'object_tags'
               42  CALL_METHOD_1         1  '1 positional argument'
               44  STORE_DEREF              'curr_obj_tag_id_to_count'

 L. 408        46  LOAD_DEREF               'cls'
               48  LOAD_ATTR                _obj_tag_id_to_count
               50  LOAD_CONST               None
               52  COMPARE_OP               is
               54  POP_JUMP_IF_FALSE    62  'to 62'

 L. 409        56  LOAD_DEREF               'curr_obj_tag_id_to_count'
               58  STORE_FAST               'delta_obj_tag_id_to_count'
               60  JUMP_FORWARD         82  'to 82'
             62_0  COME_FROM            54  '54'

 L. 411        62  LOAD_CLOSURE             'cls'
               64  LOAD_CLOSURE             'curr_obj_tag_id_to_count'
               66  BUILD_TUPLE_2         2 
               68  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               70  LOAD_STR                 'ZoneModifier.apply_object_actions.<locals>.<dictcomp>'
               72  MAKE_FUNCTION_8          'closure'

 L. 412        74  LOAD_DEREF               'curr_obj_tag_id_to_count'
               76  GET_ITER         
               78  CALL_FUNCTION_1       1  '1 positional argument'
               80  STORE_FAST               'delta_obj_tag_id_to_count'
             82_0  COME_FROM            60  '60'

 L. 414        82  LOAD_GLOBAL              services
               84  LOAD_METHOD              current_zone
               86  CALL_METHOD_0         0  '0 positional arguments'
               88  STORE_FAST               'zone'

 L. 415        90  LOAD_GLOBAL              collections
               92  LOAD_METHOD              defaultdict
               94  LOAD_GLOBAL              int
               96  CALL_METHOD_1         1  '1 positional argument'
               98  STORE_FAST               'total_architectural_stat_effects'

 L. 417       100  SETUP_LOOP          222  'to 222'
              102  LOAD_FAST                'delta_obj_tag_id_to_count'
              104  LOAD_METHOD              items
              106  CALL_METHOD_0         0  '0 positional arguments'
              108  GET_ITER         
              110  FOR_ITER            220  'to 220'
              112  UNPACK_SEQUENCE_2     2 
              114  STORE_FAST               'obj_tag_id'
              116  STORE_FAST               'delta_obj_count'

 L. 418       118  SETUP_LOOP          218  'to 218'
              120  LOAD_DEREF               'cls'
              122  LOAD_ATTR                object_tag_to_actions
              124  LOAD_GLOBAL              Tag
              126  LOAD_FAST                'obj_tag_id'
              128  CALL_FUNCTION_1       1  '1 positional argument'
              130  BINARY_SUBSCR    
              132  GET_ITER         
            134_0  COME_FROM           202  '202'
              134  FOR_ITER            216  'to 216'
              136  STORE_FAST               'action'

 L. 420       138  LOAD_FAST                'action'
              140  LOAD_ATTR                action_type
              142  LOAD_GLOBAL              ZoneModifierFromObjectsActionType
              144  LOAD_ATTR                STATISTIC_CHANGE
              146  COMPARE_OP               ==
              148  POP_JUMP_IF_FALSE   196  'to 196'

 L. 421       150  LOAD_FAST                'action'
              152  LOAD_ATTR                stat
              154  LOAD_CONST               None
              156  COMPARE_OP               is-not
              158  POP_JUMP_IF_FALSE   214  'to 214'

 L. 423       160  LOAD_DEREF               'curr_obj_tag_id_to_count'
              162  LOAD_FAST                'obj_tag_id'
              164  BINARY_SUBSCR    
              166  STORE_FAST               'obj_count'

 L. 424       168  LOAD_FAST                'total_architectural_stat_effects'
              170  LOAD_FAST                'action'
              172  LOAD_ATTR                stat
              174  LOAD_ATTR                guid64
              176  DUP_TOP_TWO      
              178  BINARY_SUBSCR    
              180  LOAD_FAST                'action'
              182  LOAD_METHOD              get_value
              184  LOAD_FAST                'obj_count'
              186  CALL_METHOD_1         1  '1 positional argument'
              188  INPLACE_ADD      
              190  ROT_THREE        
              192  STORE_SUBSCR     
              194  JUMP_BACK           134  'to 134'
            196_0  COME_FROM           148  '148'

 L. 426       196  LOAD_FAST                'delta_obj_count'
              198  LOAD_CONST               0
              200  COMPARE_OP               !=
              202  POP_JUMP_IF_FALSE   134  'to 134'

 L. 427       204  LOAD_FAST                'action'
              206  LOAD_METHOD              apply
              208  LOAD_FAST                'delta_obj_count'
              210  CALL_METHOD_1         1  '1 positional argument'
              212  POP_TOP          
            214_0  COME_FROM           158  '158'
              214  JUMP_BACK           134  'to 134'
              216  POP_BLOCK        
            218_0  COME_FROM_LOOP      118  '118'
              218  JUMP_BACK           110  'to 110'
              220  POP_BLOCK        
            222_0  COME_FROM_LOOP      100  '100'

 L. 430       222  LOAD_FAST                'zone'
              224  LOAD_METHOD              revert_zone_architectural_stat_effects
              226  CALL_METHOD_0         0  '0 positional arguments'
              228  POP_TOP          

 L. 433       230  LOAD_GLOBAL              services
              232  LOAD_METHOD              get_instance_manager
              234  LOAD_GLOBAL              sims4
              236  LOAD_ATTR                resources
              238  LOAD_ATTR                Types
              240  LOAD_ATTR                STATISTIC
              242  CALL_METHOD_1         1  '1 positional argument'
              244  STORE_FAST               'statistic_manager'

 L. 434       246  SETUP_LOOP          440  'to 440'
              248  LOAD_FAST                'total_architectural_stat_effects'
              250  LOAD_METHOD              items
              252  CALL_METHOD_0         0  '0 positional arguments'
              254  GET_ITER         
              256  FOR_ITER            438  'to 438'
              258  UNPACK_SEQUENCE_2     2 
              260  STORE_FAST               'stat_id'
              262  STORE_FAST               'value'

 L. 436       264  LOAD_FAST                'statistic_manager'
              266  LOAD_METHOD              get
              268  LOAD_FAST                'stat_id'
              270  CALL_METHOD_1         1  '1 positional argument'
              272  STORE_FAST               'stat'

 L. 437       274  LOAD_FAST                'stat'
              276  LOAD_CONST               None
              278  COMPARE_OP               is
          280_282  POP_JUMP_IF_FALSE   304  'to 304'

 L. 438       284  LOAD_GLOBAL              logger
              286  LOAD_ATTR                error
              288  LOAD_STR                 'B/B Gameplay Effect stat with ID {} expected, but not found.'
              290  LOAD_FAST                'stat_id'
              292  LOAD_STR                 'amwu'
              294  LOAD_CONST               ('owner',)
              296  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              298  POP_TOP          

 L. 439   300_302  CONTINUE            256  'to 256'
            304_0  COME_FROM           280  '280'

 L. 442       304  LOAD_FAST                'zone'
              306  LOAD_ATTR                lot
              308  LOAD_CONST               None
              310  COMPARE_OP               is
          312_314  POP_JUMP_IF_FALSE   338  'to 338'

 L. 443       316  LOAD_GLOBAL              logger
              318  LOAD_ATTR                error
              320  LOAD_STR                 'Trying to add architectural stat effects onto zone {} without lot'
              322  LOAD_FAST                'zone'
              324  LOAD_ATTR                id
              326  LOAD_STR                 'amwu'
              328  LOAD_CONST               ('owner',)
              330  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              332  POP_TOP          

 L. 444   334_336  CONTINUE            256  'to 256'
            338_0  COME_FROM           312  '312'

 L. 446       338  LOAD_FAST                'zone'
              340  LOAD_ATTR                lot
              342  LOAD_METHOD              get_tracker
              344  LOAD_FAST                'stat'
              346  CALL_METHOD_1         1  '1 positional argument'
              348  STORE_FAST               'tracker'

 L. 447       350  LOAD_FAST                'tracker'
              352  LOAD_CONST               None
              354  COMPARE_OP               is
          356_358  POP_JUMP_IF_FALSE   380  'to 380'

 L. 448       360  LOAD_GLOBAL              logger
              362  LOAD_ATTR                error
              364  LOAD_STR                 'Tracker for B/B Gameplay Effect stat {} expected, but not found.'
              366  LOAD_FAST                'stat_id'
              368  LOAD_STR                 'amwu'
              370  LOAD_CONST               ('owner',)
              372  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              374  POP_TOP          

 L. 449   376_378  CONTINUE            256  'to 256'
            380_0  COME_FROM           356  '356'

 L. 452       380  LOAD_FAST                'tracker'
              382  LOAD_METHOD              get_value
              384  LOAD_FAST                'stat'
              386  CALL_METHOD_1         1  '1 positional argument'
              388  STORE_FAST               'original_value'

 L. 453       390  LOAD_FAST                'tracker'
              392  LOAD_METHOD              add_value
              394  LOAD_FAST                'stat'
              396  LOAD_FAST                'value'
              398  CALL_METHOD_2         2  '2 positional arguments'
              400  POP_TOP          

 L. 454       402  LOAD_FAST                'tracker'
              404  LOAD_METHOD              get_value
              406  LOAD_FAST                'stat'
              408  CALL_METHOD_1         1  '1 positional argument'
              410  STORE_FAST               'new_value'

 L. 455       412  LOAD_FAST                'zone'
              414  LOAD_ATTR                zone_architectural_stat_effects
              416  LOAD_FAST                'stat_id'
              418  DUP_TOP_TWO      
              420  BINARY_SUBSCR    
              422  LOAD_FAST                'new_value'
              424  LOAD_FAST                'original_value'
              426  BINARY_SUBTRACT  
              428  INPLACE_ADD      
              430  ROT_THREE        
              432  STORE_SUBSCR     
          434_436  JUMP_BACK           256  'to 256'
              438  POP_BLOCK        
            440_0  COME_FROM_LOOP      246  '246'

 L. 458       440  LOAD_DEREF               'cls'
              442  LOAD_METHOD              _on_build_objects_environment_score_update
              444  CALL_METHOD_0         0  '0 positional arguments'
              446  POP_TOP          

 L. 461       448  LOAD_DEREF               'curr_obj_tag_id_to_count'
              450  LOAD_DEREF               'cls'
              452  STORE_ATTR               _obj_tag_id_to_count

Parse error at or near `LOAD_DICTCOMP' instruction at offset 68

    @classmethod
    def revert_object_actions(cls):
        if not cls._obj_tag_id_to_count:
            return
        zone = services.current_zone()
        for obj_tag_id, obj_count in cls._obj_tag_id_to_count.items():
            if obj_count != 0:
                for action in cls.object_tag_to_actions[Tag(obj_tag_id)]:
                    if action.action_type != ZoneModifierFromObjectsActionType.STATISTIC_CHANGE:
                        action.revert(obj_count)

        zone.revert_zone_architectural_stat_effects()
        cls._on_build_objects_environment_score_update()
        cls._obj_tag_id_to_count = None

    @classmethod
    def register_interaction_triggers(cls):
        services.get_event_manager().register_testsclscls._get_trigger_tests()

    @classmethod
    def unregister_interaction_triggers(cls):
        services.get_event_manager().unregister_testsclscls._get_trigger_tests()

    @classmethod
    def _get_trigger_tests(cls):
        tests = list()
        for trigger in cls.interaction_triggers:
            tests.extend(trigger.get_trigger_tests())

        return tests

    @classmethod
    def is_situation_prohibited(cls, situation_type):
        if cls.prohibited_situations is None:
            return False
        return cls.prohibited_situations(situation=situation_type)
