# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\career_commands.py
# Compiled at: 2022-03-15 22:18:12
# Size of source mod 2**32: 48650 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
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
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg CALL_FUNCTION_1 . 
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5 . 
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
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
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
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
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
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
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr expr expr expr expr expr expr BUILD_TUPLE_8
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . expr expr expr expr expr expr BUILD_TUPLE_8
tuple ::= expr expr expr . expr expr expr expr expr BUILD_TUPLE_8
tuple ::= expr expr expr expr . expr expr expr expr BUILD_TUPLE_8
tuple ::= expr expr expr expr expr . expr expr expr BUILD_TUPLE_8
tuple ::= expr expr expr expr expr expr . expr expr BUILD_TUPLE_8
tuple ::= expr expr expr expr expr expr expr . expr BUILD_TUPLE_8
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  94       360  LOAD_FAST                'career_tracker'
                 362  LOAD_METHOD              remove_career
                 364  LOAD_FAST                'career_instance_id'
                 366  CALL_METHOD_1         1  '1 positional argument'
->               368  POP_TOP          
from careers.career_base import set_career_event_override
from careers.career_event_manager import CareerEventManager
from careers.career_ops import CareerOps
from careers.career_tuning import Career
from careers.career_enums import CareerShiftType
from event_testing.resolver import SingleSimResolver
from interactions.context import QueueInsertStrategy
from objects.system import find_object
from rewards.reward_enums import RewardType
from server_commands.argument_helpers import OptionalTargetParam, get_optional_target, TunableInstanceParam, RequiredTargetParam, OptionalSimInfoParam
from sims.sim_info_lod import SimInfoLODLevel
from sims4.localization import LocalizationHelperTuning
import build_buy, distributor, interactions, random, services, sims4.commands, sims4.log
logger = sims4.log.Logger('CareerCommand', default_owner='rrodgers')

@sims4.commands.Command('careers.select', command_type=(sims4.commands.CommandType.Live))
def select_career--- This code section failed: ---

 L.  40         0  LOAD_FAST                'sim_id'
                2  LOAD_CONST               None
                4  COMPARE_OP               is
                6  POP_JUMP_IF_TRUE     32  'to 32'
                8  LOAD_FAST                'career_instance_id'
               10  LOAD_CONST               None
               12  COMPARE_OP               is
               14  POP_JUMP_IF_TRUE     32  'to 32'
               16  LOAD_FAST                'track_id'
               18  LOAD_CONST               None
               20  COMPARE_OP               is
               22  POP_JUMP_IF_TRUE     32  'to 32'
               24  LOAD_FAST                'level'
               26  LOAD_CONST               None
               28  COMPARE_OP               is
               30  POP_JUMP_IF_FALSE    46  'to 46'
             32_0  COME_FROM            22  '22'
             32_1  COME_FROM            14  '14'
             32_2  COME_FROM             6  '6'

 L.  41        32  LOAD_GLOBAL              logger
               34  LOAD_METHOD              error
               36  LOAD_STR                 'Not all of the data needed for the careers.select command was passed.'
               38  CALL_METHOD_1         1  '1 positional argument'
               40  POP_TOP          

 L.  42        42  LOAD_CONST               False
               44  RETURN_VALUE     
             46_0  COME_FROM            30  '30'

 L.  44        46  LOAD_GLOBAL              services
               48  LOAD_METHOD              get_instance_manager
               50  LOAD_GLOBAL              sims4
               52  LOAD_ATTR                resources
               54  LOAD_ATTR                Types
               56  LOAD_ATTR                CAREER
               58  CALL_METHOD_1         1  '1 positional argument'
               60  STORE_FAST               'career_manager'

 L.  45        62  LOAD_FAST                'career_manager'
               64  LOAD_METHOD              get
               66  LOAD_FAST                'career_instance_id'
               68  CALL_METHOD_1         1  '1 positional argument'
               70  STORE_FAST               'career_type'

 L.  46        72  LOAD_FAST                'career_type'
               74  LOAD_CONST               None
               76  COMPARE_OP               is
               78  POP_JUMP_IF_FALSE    94  'to 94'

 L.  47        80  LOAD_GLOBAL              logger
               82  LOAD_METHOD              error
               84  LOAD_STR                 'invalid career Id sent to careers.select'
               86  CALL_METHOD_1         1  '1 positional argument'
               88  POP_TOP          

 L.  48        90  LOAD_CONST               False
               92  RETURN_VALUE     
             94_0  COME_FROM            78  '78'

 L.  50        94  LOAD_FAST                'sim_id'
               96  LOAD_CONST               None
               98  COMPARE_OP               is
              100  POP_JUMP_IF_FALSE   116  'to 116'

 L.  51       102  LOAD_GLOBAL              logger
              104  LOAD_METHOD              error
              106  LOAD_STR                 'invalid sim Id passed to careers.select'
              108  CALL_METHOD_1         1  '1 positional argument'
              110  POP_TOP          

 L.  52       112  LOAD_CONST               False
              114  RETURN_VALUE     
            116_0  COME_FROM           100  '100'

 L.  54       116  LOAD_GLOBAL              services
              118  LOAD_METHOD              sim_info_manager
              120  CALL_METHOD_0         0  '0 positional arguments'
              122  LOAD_METHOD              get
              124  LOAD_FAST                'sim_id'
              126  CALL_METHOD_1         1  '1 positional argument'
              128  STORE_FAST               'sim_info'

 L.  56       130  LOAD_FAST                'sim_info'
              132  LOAD_CONST               None
              134  COMPARE_OP               is
              136  POP_JUMP_IF_FALSE   152  'to 152'

 L.  57       138  LOAD_GLOBAL              logger
              140  LOAD_METHOD              error
              142  LOAD_STR                 'invalid sim Id passed to careers.select. No sim info was found'
              144  CALL_METHOD_1         1  '1 positional argument'
              146  POP_TOP          

 L.  58       148  LOAD_CONST               False
              150  RETURN_VALUE     
            152_0  COME_FROM           136  '136'

 L.  60       152  LOAD_GLOBAL              services
              154  LOAD_METHOD              get_instance_manager
              156  LOAD_GLOBAL              sims4
              158  LOAD_ATTR                resources
              160  LOAD_ATTR                Types
              162  LOAD_ATTR                CAREER_TRACK
              164  CALL_METHOD_1         1  '1 positional argument'
              166  STORE_FAST               'career_track_manager'

 L.  61       168  LOAD_FAST                'career_track_manager'
              170  LOAD_METHOD              get
              172  LOAD_FAST                'track_id'
              174  CALL_METHOD_1         1  '1 positional argument'
              176  STORE_FAST               'career_track'

 L.  62       178  LOAD_FAST                'career_track'
              180  LOAD_CONST               None
              182  COMPARE_OP               is
              184  POP_JUMP_IF_FALSE   200  'to 200'

 L.  63       186  LOAD_GLOBAL              logger
              188  LOAD_METHOD              error
              190  LOAD_STR                 'invalid career track Id passed to careers.select'
              192  CALL_METHOD_1         1  '1 positional argument'
              194  POP_TOP          

 L.  64       196  LOAD_CONST               False
              198  RETURN_VALUE     
            200_0  COME_FROM           184  '184'

 L.  66       200  LOAD_FAST                'reason'
              202  LOAD_CONST               None
              204  COMPARE_OP               is
              206  POP_JUMP_IF_FALSE   222  'to 222'

 L.  67       208  LOAD_GLOBAL              logger
              210  LOAD_METHOD              error
              212  LOAD_STR                 'invalid career selection reason passed to careers.select'
              214  CALL_METHOD_1         1  '1 positional argument'
              216  POP_TOP          

 L.  68       218  LOAD_CONST               False
              220  RETURN_VALUE     
            222_0  COME_FROM           206  '206'

 L.  71       222  LOAD_FAST                'sim_info'
              224  LOAD_ATTR                career_tracker
              226  STORE_FAST               'career_tracker'

 L.  72       228  LOAD_FAST                'reason'
              230  LOAD_GLOBAL              CareerOps
              232  LOAD_ATTR                JOIN_CAREER
              234  COMPARE_OP               ==
          236_238  POP_JUMP_IF_FALSE   348  'to 348'

 L.  73       240  LOAD_FAST                'career_tracker'
              242  LOAD_METHOD              get_career_by_uid
              244  LOAD_FAST                'career_instance_id'
              246  CALL_METHOD_1         1  '1 positional argument'
              248  STORE_FAST               'current_career'

 L.  74       250  LOAD_FAST                'current_career'
              252  LOAD_CONST               None
              254  COMPARE_OP               is-not
          256_258  POP_JUMP_IF_FALSE   272  'to 272'

 L.  77       260  LOAD_FAST                'current_career'
              262  LOAD_METHOD              on_branch_selection
              264  LOAD_FAST                'career_track'
              266  CALL_METHOD_1         1  '1 positional argument'
              268  POP_TOP          
              270  JUMP_FORWARD        348  'to 348'
            272_0  COME_FROM           256  '256'

 L.  79       272  LOAD_FAST                'level'
              274  LOAD_GLOBAL              len
              276  LOAD_FAST                'career_track'
              278  LOAD_ATTR                career_levels
              280  CALL_FUNCTION_1       1  '1 positional argument'
              282  COMPARE_OP               >=
          284_286  POP_JUMP_IF_FALSE   310  'to 310'

 L.  80       288  LOAD_GLOBAL              logger
              290  LOAD_ATTR                error
              292  LOAD_STR                 'The career track {} does not have a level {}'

 L.  81       294  LOAD_FAST                'career_track'
              296  LOAD_FAST                'level'
              298  LOAD_STR                 'jmorrow'
              300  LOAD_CONST               ('owner',)
              302  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
              304  POP_TOP          

 L.  82       306  LOAD_CONST               False
              308  RETURN_VALUE     
            310_0  COME_FROM           284  '284'

 L.  86       310  LOAD_FAST                'career_type'
              312  LOAD_FAST                'sim_info'
              314  CALL_FUNCTION_1       1  '1 positional argument'
              316  STORE_FAST               'career'

 L.  87       318  LOAD_FAST                'career_tracker'
              320  LOAD_ATTR                add_career
              322  LOAD_FAST                'career'

 L.  88       324  LOAD_CONST               True

 L.  89       326  LOAD_FAST                'schedule_shift_type'

 L.  90       328  LOAD_FAST                'career_track'
              330  LOAD_ATTR                career_levels
              332  LOAD_FAST                'level'
              334  BINARY_SUBSCR    

 L.  91       336  LOAD_GLOBAL              RewardType
              338  LOAD_ATTR                MONEY
              340  BUILD_TUPLE_1         1 
              342  LOAD_CONST               ('show_confirmation_dialog', 'schedule_shift_override', 'career_level_override', 'disallowed_reward_types')
              344  CALL_FUNCTION_KW_5     5  '5 total positional and keyword args'
              346  POP_TOP          
            348_0  COME_FROM           270  '270'
            348_1  COME_FROM           236  '236'

 L.  93       348  LOAD_FAST                'reason'
              350  LOAD_GLOBAL              CareerOps
              352  LOAD_ATTR                QUIT_CAREER
              354  COMPARE_OP               ==
          356_358  POP_JUMP_IF_FALSE   370  'to 370'

 L.  94       360  LOAD_FAST                'career_tracker'
              362  LOAD_METHOD              remove_career
              364  LOAD_FAST                'career_instance_id'
              366  CALL_METHOD_1         1  '1 positional argument'
              368  POP_TOP          
            370_0  COME_FROM           356  '356'

Parse error at or near `POP_TOP' instruction at offset 368


@sims4.commands.Command('careers.send_to_work', command_type=(sims4.commands.CommandType.Live))
def send_to_work(sim_id: int=None, career_uid: int=None, _connection=None):
    if sim_id is None:
        logger.error('careers.send_to_work got no Sim to start the event for.')
        return False
    else:
        sim_info = services.sim_info_manager.get(sim_id)
        if sim_info is None:
            logger.error('invalid sim Id passed to careers.send_to_work')
            return False
        career = sim_info.career_tracker.get_career_by_uid(career_uid)
        if career.can_work_early:
            career.go_to_work_early
            return
        return sim_info.career_tracker.available_for_work(career) or None
    career.put_sim_in_career_rabbit_hole


@sims4.commands.Command('careers.set_follow_enabled', command_type=(sims4.commands.CommandType.Live))
def set_follow_enabled(sim_id: int=None, career_uid: int=None, enabled: bool=False, _connection=None):
    if sim_id is None:
        logger.error('Careers.set_follow_enabled got no Sim.')
        return False
    sim_info = services.sim_info_manager.get(sim_id)
    if sim_info is None:
        logger.error('Invalid sim Id passed to careers.set_follow_enabled')
        return False
    career_tracker = sim_info.career_tracker
    career = career_tracker.get_career_by_uid(career_uid)
    if career is None:
        logger.error('Invalid career Id passed to careers.set_follow_enabled')
        return False
    career.follow_enabled = enabled
    career_tracker.resend_career_data
    return True


@sims4.commands.Command('careers.leave_work', command_type=(sims4.commands.CommandType.Live))
def leave_work(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), sim_id: int=None, _connection=None):
    if sim_id is None:
        logger.error('careers.leave_work got no Sim to start the event for.')
        return False
    sim_info = services.sim_info_manager.get(sim_id)
    if sim_info is None:
        logger.error('invalid Sim Id passed to careers.leave_work')
        return False
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        logger.error('invalid Career Id passed to careers.leave_work')
        return False
    if career.is_work_time:
        career.leave_work_early
    return True


@sims4.commands.Command('careers.on_career_event_scoring_dialog_close', command_type=(sims4.commands.CommandType.Live))
def on_career_event_scoring_dialog_close(sim_id: int=None, _connection=None):
    if sim_id is None:
        logger.error('careers.leave_work got no Sim to start the event for.')
        return False
    sim = services.sim_info_manager.get(sim_id)
    if sim is None:
        logger.error('invalid Sim Id passed to careers.on_career_event_scoring_dialog_close')
        return False
    CareerEventManager.post_career_event_travel(sim)
    return True


@sims4.commands.Command('careers.stay_late', command_type=(sims4.commands.CommandType.Live))
def stay_late(_connection=None):
    career = services.get_career_service.get_career_in_career_event
    if career is not None:
        career.extend_career_session


@sims4.commands.Command('careers.list_careers')
def list_all_careers(_connection=None):
    career_manager = services.get_instance_manager(sims4.resources.Types.CAREER)
    current_time = services.time_service.sim_now
    sims4.commands.output('Current Time: {}'.format(current_time), _connection)
    for career_id in career_manager.types:
        career = career_manager.get(career_id)
        sims4.commands.output('{}: {}'.format(career, int(career.guid64)), _connection)
        cur_track = career.start_track
        sims4.commands.output('    {}: {}'.format(cur_track, int(cur_track.guid)), _connection)
        for career_level in cur_track.career_levels:
            sims4.commands.output('        {}'.format(career_level), _connection)


@sims4.commands.Command('qa.careers.info', command_type=(sims4.commands.CommandType.Automation))
def qa_print_sim_career_info(opt_sim: OptionalTargetParam=None, _connection=None):
    output = sims4.commands.AutomationOutput(_connection)
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Target sim could not be found', _connection)
        return
    careers = sim.sim_info.careers.values
    results = 'CareerInfo; NumCareers:%d' % len(careers)
    for idx, career in enumerate(careers):
        company_name = career.get_company_name
        results += ', Name%d:%s' % (idx, type(career).__name__) + ', Performance%d:%s' % (idx, career.work_performance) + ', Level%d:%s' % (idx, career.level) + ', Track%d:%s' % (idx, career.current_track_tuning.__name__) + ', Company%d:%s' % (idx, company_name.hash)

    output(results)
    sims4.commands.output(results, _connection)


@sims4.commands.Command('careers.add_career', command_type=(sims4.commands.CommandType.Cheat))
def add_career_to_sim(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if career_type is None:
        career_names = []
        career_manager = services.get_instance_manager(sims4.resources.Types.CAREER)
        for career_id in career_manager.types:
            career_type = career_manager.get(career_id)
            career_names.append(career_type.__name__)

        all_careers_str = ' '.join(career_names)
        sims4.commands.output('Usage: careers.add_career <career_name> <opt_sim>)'.format(all_careers_str), _connection)
        sims4.commands.output('Please choose a valid career: {}'.format(all_careers_str), _connection)
        return
    if sim is not None:
        sim.sim_info.career_tracker.add_career(career_type(sim.sim_info))
        return True


@sims4.commands.Command('careers.remove_career', command_type=(sims4.commands.CommandType.Cheat))
def remove_career_from_sim(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        sim.sim_info.career_tracker.remove_career(career_type.guid64)
        return True
    return False


@sims4.commands.Command('careers.promote', command_type=(sims4.commands.CommandType.Cheat))
def career_promote_sim(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        career = sim.sim_info.career_tracker.get_career_by_uid(career_type.guid64)
        if career is not None:
            career.promote
            return True
    return False


@sims4.commands.Command('careers.demote', command_type=(sims4.commands.CommandType.Cheat))
def career_demote_sim(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        career = sim.sim_info.career_tracker.get_career_by_uid(career_type.guid64)
        if career is not None:
            career.demote
            return True
    return False


@sims4.commands.Command('careers.retire', command_type=(sims4.commands.CommandType.Cheat))
def career_retire_sim(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        return False
    sim_info.career_tracker.retire_career(career_type.guid64)
    return True


@sims4.commands.Command('careers.pay_retirement')
def career_pay_retirement(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        return False
    retirement = sim_info.career_tracker.retirement
    if retirement is None:
        return False
    retirement.pay_retirement
    return True


@sims4.commands.Command('careers.add_performance', command_type=(sims4.commands.CommandType.Cheat))
def add_career_performance(opt_sim: OptionalTargetParam=None, amount: int=None, career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('careers.add_performance Invalid Sim passed', _connection)
        sims4.commands.output('Usage: careers.add_performance <opt_sim> <amount> <career type>', _connection)
        return
    if amount is None:
        sims4.commands.output('careers.add_performance Invalid amount passed', _connection)
        sims4.commands.output('Usage: careers.add_performance <opt_sim> <amount> <career type>', _connection)
        return
    if career_type is None:
        sims4.commands.output('careers.add_performance Invalid career passed', _connection)
        sims4.commands.output('Usage: careers.add_performance <opt_sim> <amount> <career type>', _connection)
        return
    if len(sim.sim_info.careers) > 0:
        career = sim.sim_info.career_tracker.get_career_by_uid(career_type.guid64)
        if career is not None:
            performance_stat = sim.statistic_tracker.get_statistic(career.current_level_tuning.performance_stat)
            performance_stat.add_value(amount)


@sims4.commands.Command('careers.set_performance', command_type=(sims4.commands.CommandType.Cheat))
def set_career_performance(career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, amount: int=None, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('careers.set_performance Invalid Sim passed', _connection)
        sims4.commands.output('Usage: careers.set_performance <career type> <amount> <opt_sim>', _connection)
        return
    if amount is None:
        sims4.commands.output('careers.set_performance Invalid amount passed', _connection)
        sims4.commands.output('Usage: careers.set_performance <career type> <amount> <opt_sim>', _connection)
        return
    if career_type is None:
        sims4.commands.output('careers.set_performance Invalid career passed', _connection)
        sims4.commands.output('Usage: careers.set_performance <career type> <amount> <opt_sim>', _connection)
        return
    if len(sim.sim_info.careers) > 0:
        career = sim.sim_info.career_tracker.get_career_by_uid(career_type.guid64)
        if career is not None:
            performance_stat = sim.statistic_tracker.get_statistic(career.current_level_tuning.performance_stat)
            performance_stat.set_value(amount)
            sim.sim_info.career_tracker.resend_career_data


@sims4.commands.Command('careers.set_performance_percentage', command_type=(sims4.commands.CommandType.Cheat))
def set_career_performance_percentage(career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, percent: float=None, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('careers.set_performance Invalid Sim passed', _connection)
        sims4.commands.output('Usage: careers.set_performance_percentage <career type> <percent> <opt_sim>', _connection)
        return
    if percent is None:
        sims4.commands.output('careers.set_performance Invalid amount passed', _connection)
        sims4.commands.output('Usage: careers.set_performance_percentage <career type> <percent> <opt_sim>', _connection)
        return
    if career_type is None:
        sims4.commands.output('careers.set_performance Invalid career passed', _connection)
        sims4.commands.output('Usage: careers.set_performance_percentage <career type> <percent> <opt_sim>', _connection)
        return
    if len(sim.sim_info.careers) > 0:
        career = sim.sim_info.career_tracker.get_career_by_uid(career_type.guid64)
        if career is not None:
            performance_stat = sim.statistic_tracker.get_statistic(career.current_level_tuning.performance_stat)
            stat_range = performance_stat.max_value - performance_stat.min_value
            amount = percent * stat_range + performance_stat.min_value
            performance_stat.set_value(amount)
            sim.sim_info.career_tracker.resend_career_data


@sims4.commands.Command('careers.update_find_career_interaction_availability', command_type=(sims4.commands.CommandType.Live))
def update_find_career_interaction_availability(sim: RequiredTargetParam=None, _connection=None):
    client = services.client_manager.get(_connection)
    sim = sim.get_target
    context = client.create_interaction_context(sim)
    aop = Career.FIND_JOB_PHONE_INTERACTION.generate_aop(sim, context)
    test_result = aop.test(context)
    tooltip = None if test_result.tooltip is None else test_result.tooltip(sim)
    op = distributor.ops.UpdateFindCareerInteractionAvailability(test_result.result, tooltip)
    distributor.system.Distributor.instance.add_op(sim.sim_info, op)


@sims4.commands.Command('careers.find_career', command_type=(sims4.commands.CommandType.Live))
def find_career(sim: RequiredTargetParam=None, _connection=None):
    sim = sim.get_target
    if sim.queue.has_duplicate_super_affordance(Career.FIND_JOB_PHONE_INTERACTION, sim, None):
        return False
    else:
        context = interactions.context.InteractionContext(sim, (interactions.context.InteractionContext.SOURCE_SCRIPT_WITH_USER_INTENT),
          (interactions.priority.Priority.High),
          insert_strategy=(QueueInsertStrategy.NEXT))
        enqueue_result = sim.push_super_affordance(Career.FIND_JOB_PHONE_INTERACTION, sim, context)
        return enqueue_result or False
    return True


@sims4.commands.Command('careers.show_parent_tracks', command_type=(sims4.commands.CommandType.DebugOnly))
def show_parent_tracks(sim: RequiredTargetParam=None, _connection=None):
    for track in services.get_instance_manager(sims4.resources.Types.CAREER_TRACK).get_ordered_types:
        sims4.commands.output('{} -> {}'.format(str(track), str(track.parent_track)), _connection)


@sims4.commands.Command('careers.show_career_level_info')
def show_career_level_info(sim: RequiredTargetParam=None, _connection=None):
    for level in services.get_instance_manager(sims4.resources.Types.CAREER_LEVEL).get_ordered_types:
        sims4.commands.output('{}: Career {}, Track {}, Level {}, User Level {}'.format(level.__name__, level.career.__name__ if level.career is not None else 'None', level.track.__name__ if level.track is not None else 'None', level.level, level.user_level), _connection)


@sims4.commands.Command('careers.override_career_event', command_type=(sims4.commands.CommandType.Automation))
def override_career_event(career_event: TunableInstanceParam(sims4.resources.Types.CAREER_EVENT), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('Failed to find Sim', _connection)
    else:
        set_career_event_override(sim_info, career_event)
        sims4.commands.output('{} will run {} on the next work day'.format(sim_info, career_event), _connection)


@sims4.commands.Command('careers.offer_specific_assignment', command_type=(sims4.commands.CommandType.DebugOnly))
def offer_specific_assignment(assignment: TunableInstanceParam(sims4.resources.Types.ASPIRATION)=None, opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    for career in sim_info.career_tracker.careers.values:
        if assignment in set((tuning.career_assignment for tuning in career.current_track_tuning.assignments)):
            career.clear_career_assignments
            career.offer_assignments(forced_assignment=assignment)
            return

    sims4.commands.output('Assignment invalid or could not be found for current career.', _connection)


@sims4.commands.Command('careers.offer_assignments', command_type=(sims4.commands.CommandType.DebugOnly))
def offer_assignments(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    for career in sim_info.career_tracker.careers.values:
        if not career.on_assignment:
            if not career.currently_at_work:
                sims4.commands.output('{} career is not inside work hours or Sim is already on assignment.'.format(career), _connection)
                continue
            career.offer_assignments


@sims4.commands.Command('careers.show_early_warning_dialog', command_type=(sims4.commands.CommandType.DebugOnly))
def show_early_warning_dialog(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    for career in sim_info.career_tracker.careers.values:
        if career.currently_at_work:
            sims4.commands.output('{} career Sim is already at work.'.format(career), _connection)
            continue
        career.early_warning_callback


@sims4.commands.Command('careers.test_career_events', command_type=(sims4.commands.CommandType.DebugOnly))
def test_career_events(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('Failed to find Sim', _connection)
        return
    resolver = SingleSimResolver(sim_info)
    for career in sim_info.careers.values:
        for event in career.career_events:
            if career.is_career_event_on_cooldown(event):
                sims4.commands.output('{} : on cooldown'.format(event.__name__), _connection)
            else:
                result = event.tests.run_tests(resolver)
                sims4.commands.output('{} : {}'.format(event.__name__, result), _connection)


@sims4.commands.Command('careers.enable_careers', command_type=(sims4.commands.CommandType.Automation))
def enable_careers(enable: bool=None, _connection=None):
    if enable is None:
        logger.error('Not all of the data needed for the careers.enable_careers was passed.')
        return
    services.get_career_service.enabled = enable


@sims4.commands.Command('careers.register_custom_career', command_type=(sims4.commands.CommandType.Live))
def register_custom_career(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)

    def on_response(dialog):
        if not dialog.accepted:
            return
        name = dialog.text_input_responses.get(Career.TEXT_INPUT_NEW_NAME)
        description = dialog.text_input_responses.get(Career.TEXT_INPUT_NEW_DESCRIPTION)
        sim_info.career_tracker.set_custom_career_data(custom_name=name, custom_description=description)

    register_dialog_data = Career.REGISTER_CAREER_DIALOG_DATA
    dialog = register_dialog_data.register_career_dialog(sim_info, SingleSimResolver(sim_info))
    text_input_overrides = None
    if sim_info.career_tracker.has_custom_career:
        text_input_overrides = {}
        custom_career_data = sim_info.career_tracker.custom_career_data
        text_input_overrides[Career.TEXT_INPUT_NEW_NAME] = lambda *_, **__: LocalizationHelperTuning.get_raw_text(custom_career_data.get_custom_career_name)
        text_input_overrides[Career.TEXT_INPUT_NEW_DESCRIPTION] = lambda *_, **__: LocalizationHelperTuning.get_raw_text(custom_career_data.get_custom_career_description)
    dialog.show_dialog(on_response=on_response, text_input_overrides=text_input_overrides)
    return True


@sims4.commands.Command('careers.unregister_custom_career', command_type=(sims4.commands.CommandType.Live))
def unregister_custom_career(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    sim_info.career_tracker.remove_custom_career_data
    return True


@sims4.commands.Command('careers.set_avg_careers', command_type=(sims4.commands.CommandType.Automation))
def set_avg_careers(average_careers: float, _connection=None):
    sim_info_manager = services.sim_info_manager
    sim_count = len(sim_info_manager)
    adult_career_sims_infos = []
    adult_jobless_sim_infos = []
    target_careers = sim_count * average_careers
    career_count = 0
    for sim_info_id in sim_info_manager:
        sim_info = sim_info_manager.get(sim_info_id)
        if sim_info is not None and sim_info.lod != SimInfoLODLevel.MINIMUM:
            if sim_info.career_tracker.has_career:
                career_count += 1
        if sim_info.is_young_adult_or_older:
            if sim_info.is_npc:
                adult_career_sims_infos.append(sim_info)
            elif sim_info.is_young_adult_or_older:
                if sim_info.is_npc:
                    adult_jobless_sim_infos.append(sim_info)

    needed_careers = target_careers - career_count
    career_delta = 0
    if needed_careers > 0:
        random.shuffle(adult_jobless_sim_infos)
        career_service = services.get_career_service
        careers = list((career for career in career_service.get_career_list if career.career_story_progression.joining is not None))
        for sim_info in adult_jobless_sim_infos:
            random.shuffle(careers)
            for career in careers:
                if career.is_valid_career(sim_info, from_join=True):
                    sim_info.career_tracker.add_career(career(sim_info))
                    career_delta += 1
                    needed_careers -= 1
                    break

            if needed_careers <= 0:
                break

    else:
        if needed_careers < 0:
            random.shuffle(adult_career_sims_infos)
            for sim_info in adult_career_sims_infos:
                for career_uid in sim_info.career_tracker.get_quittable_careers:
                    sim_info.career_tracker.remove_career(career_uid)
                    career_delta -= 1
                    needed_careers += 1
                    if needed_careers >= 0:
                        break

                if needed_careers >= 0:
                    break

    sims4.commands.output('Number of Target Careers: {}\nNumber of Initial Careers: {}\nCareer count delta:{} '.format(target_careers, career_count, career_delta), _connection)


@sims4.commands.Command('careers.add_pto', command_type=(sims4.commands.CommandType.DebugOnly))
def add_pto(amount: int=1, opt_sim: OptionalSimInfoParam=None, _connection=None):
    if amount is None:
        sims4.commands.output('Need to specify int # of pto days to add to Sim', _connection)
        return
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('did not get valid sim_info')
        sims4.commands.output('Failed to find Sim', _connection)
        return
    for career in sim_info.careers.values:
        career.add_pto(amount)
        career.resend_career_data
        sims4.commands.output('add_pto: {} now has {} pto days after adding {} days'.format(career, career.pto, amount), _connection)


@sims4.commands.Command('careers.add_gig', command_type=(sims4.commands.CommandType.Automation))
def add_gig(gig: TunableInstanceParam(sims4.resources.Types.CAREER_GIG), opt_sim: OptionalSimInfoParam=None, sim_filter: TunableInstanceParam(sims4.resources.Types.SIM_FILTER)=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_filter is not None:
        results = services.sim_filter_service.submit_filter(sim_filter, callback=None, allow_yielding=False)
        chosen_result = sims4.random.pop_weighted([(result.score, result) for result in results])
        customer_sim_info = chosen_result.sim_info
        gig_budget = 10000
    else:
        customer_sim_info = None
        gig_budget = None
    if sim_info is None:
        logger.error('Failed to get sim info for add_gig.')
        sims4.commands.automation_output('CareerAddGigInfo; Status:Failed, Message:Failed to get sim info for add_gig.', _connection)
        return
    if gig is None:
        logger.error('Failed. Please provide a gig')
        sims4.commands.automation_output('CareerAddGigInfo; Status:Failed, Message:Please provide a gig.', _connection)
    now = services.time_service.sim_now
    time_till_gig = gig.get_time_until_next_possible_gig(now)
    if time_till_gig is None:
        logger.error('No possible scheduled times for gig.')
        sims4.commands.automation_output('CareerAddGigInfo; Status:Failed, Message:No possible scheduled times for gig.', _connection)
        return
    gig_time = now + time_till_gig
    sim_info.career_tracker.set_gig(gig, gig_time, customer_sim_info, gig_budget)


@sims4.commands.Command('careers.list_gigs')
def list_gigs(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for list_gigs.')
        return
    career_tracker = sim_info.career_tracker
    if career_tracker is None:
        logger.error('Failed to find career tracker on sim {} for list_gigs.', sim_info)
        return
    for career in career_tracker:
        for gig in career.get_current_gigs:
            sims4.commands.output(f"{career}: {type(gig).__name__} (ID:{gig.guid64})", _connection)


@sims4.commands.Command('careers.cancel_all_gigs', command_type=(sims4.commands.CommandType.Live))
def cancel_all_gigs(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for cancel_all_gigs.')
        return
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        logger.error('Failed to find career {} on sim {} for cancel_all_gigs.', career_type, sim_info)
        return
    for gig in list(career.get_current_gigs):
        career.cancel_gig(gig_id=(gig.guid64))


@sims4.commands.Command('careers.cancel_current_gig', command_type=(sims4.commands.CommandType.Live))
def cancel_current_gig(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for cancel_current_gig.')
        return
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        logger.error('Failed to find career {} on sim {} for cancel_current_gig.', career_type, sim_info)
        return
    career.cancel_gig


@sims4.commands.Command('careers.cancel_gig', command_type=(sims4.commands.CommandType.Live))
def cancel_gig(gig: TunableInstanceParam(sims4.resources.Types.CAREER_GIG), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for cancel_gig.')
        return
    career = sim_info.career_tracker.get_career_by_uid(gig.career.guid64)
    if career is None:
        logger.error('Failed to find a career for gig {} on sim {} for cancel_gig.', gig, sim_info)
        return
    career.cancel_gig(gig_id=(gig.guid64))


@sims4.commands.Command('careers.score_current_home_assignment_gig', command_type=(sims4.commands.CommandType.DebugOnly))
def score_current_home_assignment_gig(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for score_current_home_assignment_gig.')
        return
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        logger.error('Failed to find career {} on sim {} for score_current_home_assignment_gig.', career_type, sim_info)
        return
    career.score_work_at_home_gig_early


def _get_gig_for_command(sim_info, career_type, _connection):
    sim_info = get_optional_target(sim_info, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for a career gig command.')
        return
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        logger.error('Failed to find career {} on sim {} for a career gig command.', career_type, sim_info)
        return
    gig = career.get_current_gig
    if gig is None:
        logger.error('Failed to find a gig on career {} on sim {} for a career gig command.', career_type, sim_info)
        return
    return gig


@sims4.commands.Command('careers.reveal_gig_client_preference', command_type=(sims4.commands.CommandType.Live))
def reveal_gig_client_preference(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), count: int=1, opt_sim: OptionalSimInfoParam=None, _connection=None):
    gig = _get_gig_for_command(opt_sim, career_type, _connection)
    if gig is None:
        return
    if not hasattr(gig, 'reveal_client_preference'):
        logger.error("Gig {} doesn't have client preferences to reveal on career {} on sim {} for reveal_gig_client_preference.", gig, career_type, sim_info)
        return
    gig.reveal_client_preference(count)


@sims4.commands.Command('careers.replace_gig_preference_category', command_type=(sims4.commands.CommandType.Live))
def replace_gig_preference_category(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), preference_category: TunableInstanceParam(sims4.resources.Types.CAS_PREFERENCE_CATEGORY), opt_sim: OptionalSimInfoParam=None, _connection=None):
    gig = _get_gig_for_command(opt_sim, career_type, _connection)
    if gig is None:
        return
    gig.replace_client_preference_by_category(preference_category)


@sims4.commands.Command('careers.replace_gig_preference')
def replace_gig_preference(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), old_preference: TunableInstanceParam(sims4.resources.Types.TRAIT), new_preference: TunableInstanceParam(sims4.resources.Types.TRAIT), opt_sim: OptionalSimInfoParam=None, _connection=None):
    gig = _get_gig_for_command(opt_sim, career_type, _connection)
    if gig is None:
        return
    gig.replace_client_preference(old_preference, new_preference)


@sims4.commands.Command('careers.show_gig_objects', command_type=(sims4.commands.CommandType.DebugOnly))
def show_gig_objects(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), opt_sim: OptionalSimInfoParam=None, _connection=None):
    gig = _get_gig_for_command(opt_sim, career_type, _connection)
    if gig is None:
        return
    customer_lot_id = gig.get_customer_lot_id
    if not customer_lot_id:
        logger.error('Failed to find a customer lot id on career {} on sim {} for show_gig_objects.', career_type, sim_info)
        return
    gig_objects = build_buy.get_gig_objects_added(customer_lot_id)
    manager = services.object_manager
    for gig_object_id in gig_objects:
        gig_object = manager.get(gig_object_id)
        sims4.commands.output("Gig Object: '{}' ".format(gig_object), _connection)


@sims4.commands.Command('careers.resend_data')
def resend_data(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        logger.error('Failed to get sim info for resend_data.')
        return
    career_tracker = sim_info.career_tracker
    if career_tracker is None:
        logger.error('Failed to find career tracker on sim {} for resend_data.', sim_info)
        return
    career_tracker.resend_career_data


@sims4.commands.Command('careers.show_reveal_sequence', command_type=(sims4.commands.CommandType.Live))
def show_reveal_sequence(opt_sim: OptionalSimInfoParam=None, active_gig: bool=True, _connection=None):
    sim_info = get_optional_target(opt_sim, _connection, target_type=OptionalSimInfoParam)
    if sim_info is None:
        sims4.commands.output('Failed to find SimInfo.', _connection)
        return False
    dialog = Career.REVEAL_SEQUENCE_DIALOG(sim_info, resolver=(SingleSimResolver(sim_info)), active_gig=active_gig)
    dialog.show_dialog(owner=sim_info)
    return True


@sims4.commands.Command('careers.delete_active_gig_photos', command_type=(sims4.commands.CommandType.Live))
def delete_active_gig_photos(opt_sim: OptionalSimInfoParam=None, active_gig: bool=True, career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, _connection=None):
    sim_info = get_optional_target(opt_sim, _connection, target_type=OptionalSimInfoParam)
    if sim_info is None:
        sims4.commands.output('Failed to find SimInfo.', _connection)
        return False
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        sims4.commands.output('Sim is not in the interior decorator career.', _connection)
        return False
    sim_info.career_tracker.update_photo_difference(career, active_gig)
    return True


@sims4.commands.Command('careers.clear_deletion_from_gig_history', command_type=(sims4.commands.CommandType.Live))
def clear_deletion_from_gig_history(opt_sim: OptionalSimInfoParam=None, active_gig: bool=True, career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, _connection=None):
    sim_info = get_optional_target(opt_sim, _connection, target_type=OptionalSimInfoParam)
    if sim_info is None:
        sims4.commands.output('Failed to find SimInfo.', _connection)
        return False
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        sims4.commands.output('Sim is not in the specified career.', _connection)
        return False
    sim_info.career_tracker.clear_deletion_cache_from_gig_history(career, active_gig)
    return True


@sims4.commands.Command('careers.clear_selected_photos_from_gig_history', command_type=(sims4.commands.CommandType.Live))
def clear_selected_photos_from_gig_history(opt_sim: OptionalSimInfoParam=None, active_gig: bool=True, career_type: TunableInstanceParam(sims4.resources.Types.CAREER)=None, _connection=None):
    sim_info = get_optional_target(opt_sim, _connection, target_type=OptionalSimInfoParam)
    if sim_info is None:
        sims4.commands.output('Failed to find SimInfo.', _connection)
        return False
    career = sim_info.career_tracker.get_career_by_uid(career_type.guid64)
    if career is None:
        sims4.commands.output('Sim is not in the specified career.', _connection)
        return False
    sim_info.career_tracker.clear_selected_photos_from_gig_history(career, active_gig)
    return True


@sims4.commands.Command('careers.calculate_individual_customer_gig_scoring', command_type=(sims4.commands.CommandType.Live))
def calculate_individual_customer_gig_scoring(career_type: TunableInstanceParam(sims4.resources.Types.CAREER), likes_value: int=1, dislikes_value: int=1, opt_sim: OptionalSimInfoParam=None, _connection=None):
    gig = _get_gig_for_command(opt_sim, career_type, _connection)
    if gig is None:
        return False
    gig.calculate_gig_score_for_client_household(likes_value, dislikes_value)
    return True
