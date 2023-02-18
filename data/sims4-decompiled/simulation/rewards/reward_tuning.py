# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\rewards\reward_tuning.py
# Compiled at: 2021-10-14 17:49:40
# Size of source mod 2**32: 21497 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
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
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
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
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST BUILD_CONST_KEY_MAP_2 . 
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
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= dict . 
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
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE COME_FROM . 
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
function_def_deco ::= mkfuncdeco . store
function_def_deco ::= mkfuncdeco store . 
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
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_10
mkfunc ::= expr LOAD_CODE . LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr LOAD_CODE LOAD_STR . MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 . CALL_FUNCTION_1
mkfuncdeco ::= expr mkfuncdeco0 CALL_FUNCTION_1 . 
mkfuncdeco0 ::= mkfunc . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
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
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 436       102  LOAD_FAST                'tracker'
                 104  LOAD_METHOD              try_modify_bucks
                 106  LOAD_FAST                'self'
                 108  LOAD_ATTR                bucks_type
                 110  LOAD_FAST                'self'
                 112  LOAD_ATTR                amount
->               114  CALL_METHOD_2         2  '2 positional arguments'
from bucks.bucks_enums import BucksType
from bucks.bucks_utils import BucksUtils
from buffs.tunable import TunableBuffReference
from business.business_reward_tuning import TunableRewardAdditionalEmployeeSlot, TunableRewardAdditionalCustomerCount, TunableRewardAdditionalMarkup
from clubs.club_enums import ClubGatheringVibe
from objects import ALL_HIDDEN_REASONS
from objects.object_enums import ItemLocation
from objects.system import create_object
from protocolbuffers import Consts_pb2
from protocolbuffers.DistributorOps_pb2 import SetWhimBucks
from rewards.reward_enums import RewardDestination, RewardType
from rewards.tunable_reward_base import TunableRewardBase
from sims4.common import is_available_pack
from sims4.localization import LocalizationHelperTuning
from sims4.resources import Types
from sims4.tuning.dynamic_enum import _get_pack_from_enum_value
from sims4.tuning.tunable import TunableVariant, TunableReference, Tunable, TunableTuple, TunableCasPart, TunableMagazineCollection, TunableLiteralOrRandomValue, TunableEnumEntry, TunableRange, AutoFactoryInit, TunableFactory
from sims4.utils import constproperty
import build_buy, services, sims4.resources
logger = sims4.log.Logger('Rewards', default_owner='trevor')

class TunableRewardObject(TunableRewardBase):
    FACTORY_TUNABLES = {'definition': TunableReference(description='\n            Give an object as a reward.\n            ',
                     manager=(services.definition_manager()))}

    def __init__(self, *args, definition, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._definition = definition

    @constproperty
    def reward_type():
        return RewardType.OBJECT_DEFINITION

    def _try_create_in_mailbox(self, sim_info):
        if sim_info.household is None:
            logger.error('Trying to add an item [{}] to a mailbox but the provided sim [{}] has no household', (self._definition),
              sim_info, owner='trevor')
            return False
        zone = services.get_zone(sim_info.household.home_zone_id)
        if zone is None:
            logger.error('Trying to add an item [{}] to a mailbox but the provided sim [{}] has no home zone.', (self._definition),
              sim_info, owner='trevor')
            return False
        lot_hidden_inventory = zone.lot.get_hidden_inventory()
        if lot_hidden_inventory is None:
            logger.error("Trying to add an item [{}] to the lot's hidden inventory but the provided sim [{}] has no hidden inventory for their lot.", (self._definition),
              sim_info, owner='trevor')
            return False
        obj = create_object(self._definition)
        if obj is None:
            logger.error('Trying to give an object reward to a Sim, {}, and the object created was None. Definition: {}', sim_info, self._definition)
            return False
        try:
            lot_hidden_inventory.system_add_object(obj)
        except:
            logger.error('Could not add object [{}] to the mailbox inventory on the home lot of the Sim [{}].', obj,
              sim_info, owner='trevor')
            obj.destroy(source=self, cause='Could not add object to the mailbox inventory')
            return False
            return True

    def _try_create_in_sim_inventory(self, sim_info, obj=None, force_rewards_to_sim_info_inventory=False):
        sim = sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
        if sim is None:
            if force_rewards_to_sim_info_inventory:
                obj = create_object(self._definition) if obj is None else obj
                return sim_info.try_add_object_to_inventory_without_component(obj)
        else:
            return (False, None)
            obj = create_object(self._definition) if obj is None else obj
            if obj is None:
                logger.error('Trying to give an object reward to a Sim, {}, and the object created was None. Definition: {}', sim_info, self._definition)
                return (False, None)
            result = sim.inventory_component.player_try_add_object(obj)
            return result or (
             False, obj)
        obj.update_ownership(sim_info)
        return (True, obj)

    def _try_create_in_household_inventory(self, sim_info, obj=None):
        obj = create_object((self._definition), loc_type=(ItemLocation.HOUSEHOLD_INVENTORY)) if obj is None else obj
        if obj is None:
            logger.error('Trying to give an object reward to a Sim, {}, and the object created was None. Definition: {}', sim_info, self._definition)
            return (False, None)
        obj.update_ownership(sim_info, make_sim_owner=False)
        obj.set_post_bb_fixup_needed()
        if not build_buy.move_object_to_household_inventory(obj):
            logger.error('Failed to add reward definition object {} to household inventory.', (self._definition),
              owner='rmccord')

    def open_reward(self, sim_info, reward_destination=RewardDestination.HOUSEHOLD, force_rewards_to_sim_info_inventory=False, **kwargs):
        if reward_destination == RewardDestination.MAILBOX:
            self._try_create_in_mailbox(sim_info)
            return
        reward_object = None
        if reward_destination == RewardDestination.SIM:
            result, reward_object = self._try_create_in_sim_inventory(sim_info, force_rewards_to_sim_info_inventory=force_rewards_to_sim_info_inventory)
            if result:
                return
        self._try_create_in_household_inventory(sim_info, obj=reward_object)

    def _get_display_text(self, resolver=None):
        return LocalizationHelperTuning.get_object_name(self._definition)


class TunableRewardCASPart(TunableRewardBase):
    FACTORY_TUNABLES = {'cas_part': TunableCasPart(description='\n            The cas part for this reward.\n            ')}

    def __init__(self, *args, cas_part, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._cas_part = cas_part

    @constproperty
    def reward_type():
        return RewardType.CAS_PART

    def open_reward(self, sim_info, reward_source=None, **kwargs):
        household = sim_info.household
        household.add_cas_part_to_reward_inventory(self._cas_part)
        if reward_source is not None:
            if self._cas_part is not None:
                self.send_unlock_telemetry(sim_info, self._cas_part, reward_source.guid64)

    def valid_reward(self, sim_info):
        return not sim_info.household.part_in_reward_inventory(self._cas_part)


class TunableRewardMoney(TunableRewardBase):
    FACTORY_TUNABLES = {'money': TunableLiteralOrRandomValue(description='\n            Give money to a sim/household.\n            ',
                tunable_type=int,
                default=10)}

    def __init__(self, *args, money, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._awarded_money = money.random_int()

    @constproperty
    def reward_type():
        return RewardType.MONEY

    def open_reward(self, sim_info, **kwargs):
        household = services.household_manager().get(sim_info.household_id)
        if household is not None:
            household.funds.add(self._awarded_money, Consts_pb2.TELEMETRY_MONEY_ASPIRATION_REWARD, sim_info.get_sim_instance())

    def _get_display_text(self, resolver=None):
        return LocalizationHelperTuning.get_money(self._awarded_money)


class TunableRewardTrait(TunableRewardBase):
    FACTORY_TUNABLES = {'trait': TunableReference(description='\n            Give a trait as a reward\n            ',
                manager=(services.get_instance_manager(sims4.resources.Types.TRAIT)))}

    def __init__(self, *args, trait, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._trait = trait

    @constproperty
    def reward_type():
        return RewardType.TRAIT

    def open_reward(self, sim_info, reward_destination=RewardDestination.HOUSEHOLD, **kwargs):
        if reward_destination == RewardDestination.HOUSEHOLD:
            household = sim_info.household
            for sim in household.sim_info_gen():
                sim.add_trait(self._trait)

        else:
            if reward_destination == RewardDestination.SIM:
                sim_info.add_trait(self._trait)
            else:
                logger.warn('Attempting to open a RewardTrait with an invalid destination: {}. Reward traits can only be given to households or sims.', reward_destination, owner='trevor')

    def valid_reward(self, sim_info):
        return sim_info.trait_tracker.can_add_trait(self._trait)


class TunableRewardBuildBuyUnlockBase(TunableRewardBase):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.instance = None
        self.type = Types.INVALID

    def get_resource_key(self):
        return NotImplementedError

    def get_id_for_telemetry(self):
        return self.instance.id

    def open_reward(self, sim_info, reward_destination=RewardDestination.HOUSEHOLD, reward_source=None, **kwargs):
        key = self.get_resource_key()
        if key is not None:
            if reward_destination == RewardDestination.SIM:
                sim_info.add_build_buy_unlock(key)
            else:
                if reward_destination == RewardDestination.HOUSEHOLD:
                    for household_sim_info in sim_info.household.sim_info_gen():
                        household_sim_info.add_build_buy_unlock(key)

                else:
                    logger.warn('Invalid reward destination () on build buy unlock. The household will still get the buildbuy unlock added.', reward_destination, owner='trevor')
            sim_info.household.add_build_buy_unlock(key)
        else:
            logger.warn('Invalid Build Buy unlock tuned. No reward given.')
        if self.instance is not None:
            if reward_source is not None:
                self.send_unlock_telemetry(sim_info, self.get_id_for_telemetry(), reward_source.guid64)


class TunableBuildBuyObjectDefinitionUnlock(TunableRewardBuildBuyUnlockBase):

    @TunableFactory.factory_option
    def get_definition(pack_safe):
        return {'object_definition': TunableReference(description='\n                The definition of the object to be created.\n                ',
                                manager=(services.definition_manager()),
                                pack_safe=pack_safe)}

    def __init__(self, *args, object_definition, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.instance = object_definition
        self.type = Types.OBJCATALOG

    @constproperty
    def reward_type():
        return RewardType.BUILD_BUY_OBJECT

    def get_resource_key(self):
        return sims4.resources.Key(self.type, self.instance.id)


class TunableBuildBuyMagazineCollectionUnlock(TunableRewardBuildBuyUnlockBase):
    FACTORY_TUNABLES = {'magazine_collection': TunableMagazineCollection(description='\n            Unlock a magazine room to purchase in build/buy.\n            ')}

    def __init__(self, *args, magazine_collection, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.instance = magazine_collection
        self.type = Types.MAGAZINECOLLECTION

    @constproperty
    def reward_type():
        return RewardType.BUILD_BUY_MAGAZINE_COLLECTION

    def get_resource_key(self):
        if self.instance is not None:
            return sims4.resources.Key(self.type, self.instance)
        return

    def get_id_for_telemetry(self):
        return self.instance


class TunableSetClubGatheringVibe(TunableRewardBase):
    FACTORY_TUNABLES = {'vibe_to_set': TunableEnumEntry(description='\n            The vibe that the club gathering will be set to.\n            ',
                      tunable_type=ClubGatheringVibe,
                      default=(ClubGatheringVibe.NO_VIBE))}

    def __init__(self, *args, vibe_to_set=None, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._vibe_to_set = vibe_to_set

    @constproperty
    def reward_type():
        return RewardType.SET_CLUB_GATHERING_VIBE

    def get_resource_key(self):
        return NotImplementedError

    def open_reward(self, sim_info, **kwargs):
        club_service = services.get_club_service()
        if club_service is None:
            return
        sim = sim_info.get_sim_instance()
        if sim is None:
            return
        gathering = club_service.sims_to_gatherings_map.get(sim, None)
        if gathering is None:
            return
        gathering.set_club_vibe(self._vibe_to_set)


class TunableRewardDisplayText(TunableRewardBase):

    @constproperty
    def reward_type():
        return RewardType.DISPLAY_TEXT

    def open_reward(self, _, **kwargs):
        return True


class TunableRewardBucks(AutoFactoryInit, TunableRewardBase):
    FACTORY_TUNABLES = {'bucks_type':TunableEnumEntry(description='\n            The type of Bucks to grant.\n            ',
       tunable_type=BucksType,
       default=BucksType.INVALID,
       invalid_enums=(
      BucksType.INVALID,),
       pack_safe=True), 
     'amount':TunableRange(description='\n            The amount of Bucks to award. Must be a positive value.\n            ',
       tunable_type=int,
       default=10,
       minimum=1)}

    @constproperty
    def reward_type():
        return RewardType.BUCKS

    def open_reward--- This code section failed: ---

 L. 423         0  LOAD_FAST                'self'
                2  LOAD_ATTR                bucks_type
                4  LOAD_CONST               None
                6  COMPARE_OP               is
                8  POP_JUMP_IF_TRUE     40  'to 40'
               10  LOAD_FAST                'self'
               12  LOAD_ATTR                bucks_type
               14  LOAD_GLOBAL              BucksType
               16  LOAD_ATTR                INVALID
               18  COMPARE_OP               ==
               20  POP_JUMP_IF_TRUE     40  'to 40'

 L. 424        22  LOAD_GLOBAL              is_available_pack
               24  LOAD_GLOBAL              _get_pack_from_enum_value
               26  LOAD_GLOBAL              int
               28  LOAD_FAST                'self'
               30  LOAD_ATTR                bucks_type
               32  CALL_FUNCTION_1       1  '1 positional argument'
               34  CALL_FUNCTION_1       1  '1 positional argument'
               36  CALL_FUNCTION_1       1  '1 positional argument'
               38  POP_JUMP_IF_TRUE     44  'to 44'
             40_0  COME_FROM            20  '20'
             40_1  COME_FROM             8  '8'

 L. 426        40  LOAD_CONST               None
               42  RETURN_VALUE     
             44_0  COME_FROM            38  '38'

 L. 428        44  LOAD_FAST                'sim_info'
               46  LOAD_ATTR                is_npc
               48  POP_JUMP_IF_FALSE    54  'to 54'

 L. 429        50  LOAD_CONST               None
               52  RETURN_VALUE     
             54_0  COME_FROM            48  '48'

 L. 431        54  LOAD_GLOBAL              BucksUtils
               56  LOAD_ATTR                get_tracker_for_bucks_type
               58  LOAD_FAST                'self'
               60  LOAD_ATTR                bucks_type
               62  LOAD_FAST                'sim_info'
               64  LOAD_ATTR                id
               66  LOAD_CONST               True
               68  LOAD_CONST               ('add_if_none',)
               70  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               72  STORE_FAST               'tracker'

 L. 432        74  LOAD_FAST                'tracker'
               76  LOAD_CONST               None
               78  COMPARE_OP               is
               80  POP_JUMP_IF_FALSE   102  'to 102'

 L. 433        82  LOAD_GLOBAL              logger
               84  LOAD_METHOD              error
               86  LOAD_STR                 'Failed to open a TunableRewardBucks of buck type {} for Sim {}.'
               88  LOAD_FAST                'self'
               90  LOAD_ATTR                bucks_type
               92  LOAD_FAST                'sim_info'
               94  CALL_METHOD_3         3  '3 positional arguments'
               96  POP_TOP          

 L. 434        98  LOAD_CONST               None
              100  RETURN_VALUE     
            102_0  COME_FROM            80  '80'

 L. 436       102  LOAD_FAST                'tracker'
              104  LOAD_METHOD              try_modify_bucks
              106  LOAD_FAST                'self'
              108  LOAD_ATTR                bucks_type
              110  LOAD_FAST                'self'
              112  LOAD_ATTR                amount
              114  CALL_METHOD_2         2  '2 positional arguments'
              116  POP_TOP          

Parse error at or near `CALL_METHOD_2' instruction at offset 114


class TunableRewardBuff(AutoFactoryInit, TunableRewardBase):
    FACTORY_TUNABLES = {'buff': TunableBuffReference(description='\n            Buff to be given as a reward.\n            ')}

    @constproperty
    def reward_type():
        return RewardType.BUFF

    def open_reward(self, sim_info, reward_destination=RewardDestination.HOUSEHOLD, **kwargs):
        if reward_destination == RewardDestination.HOUSEHOLD:
            household = sim_info.household
            for sim_info in household.sim_info_gen():
                sim_info.add_buff_from_op(buff_type=(self.buff.buff_type), buff_reason=(self.buff.buff_reason))

        else:
            if reward_destination == RewardDestination.SIM:
                sim_info.add_buff_from_op(buff_type=(self.buff.buff_type), buff_reason=(self.buff.buff_reason))
            else:
                logger.error('Attempting to open a RewardBuff with an invalid destination: {}. Reward buffs can only be given to households or Sims.', reward_destination)


class TunableRewardWhimBucks(AutoFactoryInit, TunableRewardBase):
    FACTORY_TUNABLES = {'whim_bucks': TunableRange(description='\n            The number of whim bucks to give.\n            ',
                     tunable_type=int,
                     default=1,
                     minimum=1)}

    @constproperty
    def reward_type():
        return RewardType.WHIM_BUCKS

    def open_reward(self, sim_info, reward_destination=RewardDestination.HOUSEHOLD, **kwargs):
        if reward_destination == RewardDestination.HOUSEHOLD:
            household = sim_info.household
            for sim_info in household.sim_info_gen():
                sim_info.apply_satisfaction_points_delta(self.whim_bucks, SetWhimBucks.COMMAND)

        else:
            if reward_destination == RewardDestination.SIM:
                sim_info.apply_satisfaction_points_delta(self.whim_bucks, SetWhimBucks.COMMAND)
            else:
                logger.error('Attempting to open a RewardWhimBucks with an invalid destination: {}. Reward whim bucks can only be given to households or Sims.', reward_destination)


class TunableSpecificReward(TunableVariant):

    def __init__(self, description='A single specific reward.', pack_safe=False, **kwargs):
        (super().__init__)(money=TunableRewardMoney.TunableFactory(), 
         object_definition=TunableRewardObject.TunableFactory(), 
         trait=TunableRewardTrait.TunableFactory(), 
         cas_part=TunableRewardCASPart.TunableFactory(), 
         build_buy_object=TunableBuildBuyObjectDefinitionUnlock.TunableFactory(get_definition=(pack_safe,)), 
         build_buy_magazine_collection=TunableBuildBuyMagazineCollectionUnlock.TunableFactory(), 
         display_text=TunableRewardDisplayText.TunableFactory(), 
         additional_employee_slot=TunableRewardAdditionalEmployeeSlot.TunableFactory(), 
         additional_business_customer_count=TunableRewardAdditionalCustomerCount.TunableFactory(), 
         additional_business_markup=TunableRewardAdditionalMarkup.TunableFactory(), 
         set_club_gathering_vibe=TunableSetClubGatheringVibe.TunableFactory(), 
         bucks=TunableRewardBucks.TunableFactory(), 
         buff=TunableRewardBuff.TunableFactory(), 
         whim_bucks=TunableRewardWhimBucks.TunableFactory(), 
         description=description, **kwargs)


class TunableRandomReward(TunableTuple):

    def __init__(self, description='A list of specific rewards and a weight.', **kwargs):
        super().__init__(reward=(TunableSpecificReward()),
          weight=Tunable(tunable_type=float, default=1),
          description=description)
