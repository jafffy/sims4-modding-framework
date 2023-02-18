# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\statistic_commands.py
# Compiled at: 2021-12-09 21:59:48
# Size of source mod 2**32: 45760 bytes

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
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
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
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
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
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
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
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
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
expr_stmt ::= expr POP_TOP . 
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
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
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
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
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
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . expr expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
lambda_body ::= expr expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . expr expr LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfunc ::= expr expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
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
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
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
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
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
   
 L. 361        62  LOAD_GLOBAL              _set_skill_level
                  64  LOAD_FAST                'stat_type'
                  66  LOAD_FAST                'level'
                  68  LOAD_FAST                'sim'
                  70  LOAD_FAST                '_connection'
->                72  CALL_FUNCTION_4       4  '4 positional arguments'

-- Stacks of completed symbols:
START ::= |- stmts . 
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
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_BACK
_ifstmts_jumpl ::= COME_FROM c_stmts . JUMP_FORWARD
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
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr expr expr expr . CALL_METHOD_3
call ::= expr expr expr expr CALL_METHOD_3 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_9
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_9 . 
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
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= list . 
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
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr . expr expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
lambda_body ::= expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_5
lambda_body ::= expr expr . expr LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
lambda_body ::= expr expr expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_7
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr BUILD_LIST_1 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr . expr expr LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfunc ::= expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_5
mkfunc ::= expr expr . expr LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfunc ::= expr expr expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_7
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
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
returns ::= _stmts return . 
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
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts ::= returns . 
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
-> 
 L. 506        44  FOR_ITER             64  'to 64'
                  46  STORE_FAST               'stat_type'
from collections import Counter
import collections, random, weakref
from autonomy.autonomy_request import AutonomyPostureBehavior
from interactions import priority
from interactions.aop import AffordanceObjectPair
from interactions.context import InteractionContext, InteractionBucketType
from server_commands.argument_helpers import OptionalTargetParam, get_optional_target, TunableInstanceParam, OptionalSimInfoParam
from sims.sim_info import SimInfo
from statistics.commodity import Commodity
from statistics.continuous_statistic import ContinuousStatistic
from statistics.skill import Skill
import autonomy.autonomy_modes, autonomy.autonomy_modifier, services, sims4.commands, statistics.skill
logger = sims4.log.Logger('SimStatistics')

@sims4.commands.Command('stats.show_stats')
def show_statistics(display_skill_only=False, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        for stat in sim.statistics_gen():
            if not display_skill_only or isinstance(stat, statistics.skill.Skill):
                s = 'Statistic: {}, Value: {},  Level: {}.'.format(stat.__class__.__name__, stat.get_value(), stat.get_user_value())
                sims4.commands.output(s, _connection)


@sims4.commands.Command('stats.show_commodities', command_type=(sims4.commands.CommandType.Automation))
def show_commodities(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None and sim and sim.statistic_tracker is not None:
        sim.commodity_tracker.debug_output_all(_connection)
        sim.statistic_tracker.debug_output_all(_connection)
    else:
        sims4.commands.output('No target for stats.show_commodities.', _connection)


@sims4.commands.Command('stats.show_static_commodities')
def show_static_commodities(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None and sim.static_commodity_tracker is not None:
        sim.static_commodity_tracker.debug_output_all(_connection)
    else:
        sims4.commands.output('No target for stats.show_static_commodities.', _connection)


@sims4.commands.Command('qa.stats.show_commodities', command_type=(sims4.commands.CommandType.Automation))
def show_commodities_automation(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        if sim.commodity_tracker is not None:
            sim.commodity_tracker.debug_output_all_automation(_connection)
    sims4.commands.automation_output('CommodityInfo; Type:END', _connection)


@sims4.commands.Command('mood.show_active_mood_type')
def show_active_mood_type(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        mood_type = sim.get_mood()
        sims4.commands.output("{0}'s active mood type is {1}".format(sim, mood_type), _connection)
        return True
    sims4.commands.output('No target for mood.show_active_mood_type', _connection)
    return False


@sims4.commands.Command('stats.show_all_statistics')
def show_all_statistics(opt_sim: OptionalTargetParam=None, _connection=None):
    sim_or_obj = get_optional_target(opt_sim, _connection)
    if sim_or_obj is not None:
        show_commodities(opt_sim=opt_sim, _connection=_connection)
        if sim_or_obj.is_sim:
            show_statistics(opt_sim=opt_sim, _connection=_connection)


@sims4.commands.Command('stats.show_change')
def show_change(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None and stat_type is not None:
        tracker = sim.get_tracker(stat_type)
        stat = tracker.get_statistic(stat_type)
        if stat is None:
            sims4.commands.output("Couldn't find stat on sim: {}".format(stat_type), _connection)
            return
        if not isinstance(stat, ContinuousStatistic):
            sims4.commands.output('{} is not a continuous statistic'.format(stat), _connection)
            return
        sims4.commands.output('\tDecay: {}\n\tChange: {}\n\tTotal Delta: {}'.format(stat.get_decay_rate(), stat._get_change_rate_without_decay(), stat.get_change_rate()), _connection)
    else:
        sims4.commands.output('No sim or stat type for stats.show_change.', _connection)


@sims4.commands.Command('stats.fill_commodities', command_type=(sims4.commands.CommandType.Cheat))
def set_commodities_to_best_values(opt_sim: OptionalTargetParam=None, visible_only: bool=True, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        sims4.commands.output('Setting all motives on the current sim to full.', _connection)
        if sim.commodity_tracker is not None:
            sim.commodity_tracker.set_all_commodities_to_best_value(visible_only=visible_only)


@sims4.commands.Command('stats.fill_commodities_household', command_type=(sims4.commands.CommandType.Cheat))
def set_commodities_to_best_values_household(visible_only: bool=True, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    sims4.commands.output('Setting all motives on all household sims to full.', _connection)
    for sim_info in tgt_client.selectable_sims:
        if sim_info.commodity_tracker is not None:
            sim_info.commodity_tracker.set_all_commodities_to_best_value(visible_only=visible_only)


@sims4.commands.Command('stats.tank_commodities')
def tank_commodities(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is not None:
        if sim.commodity_tracker is not None:
            sims4.commands.output('Setting all motives on the current sim to min.', _connection)
            sim.commodity_tracker.debug_set_all_to_min()


@sims4.commands.Command('stats.set_stat', 'stats.set_commodity', command_type=(sims4.commands.CommandType.Cheat))
def set_statisitic(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), value: float=None, opt_sim: OptionalSimInfoParam=None, opt_target_type=None, _connection=None):
    if stat_type is None:
        sims4.commands.output('Invalid stat type used for stats.set_stat.', _connection)
        return
    elif value is None:
        sims4.commands.output('Invalid value set for stats.set_stat.', _connection)
        return
        if opt_target_type is not None:
            target_object = None
            if opt_target_type == 'Lot':
                current_zone = services.current_zone()
                target_object = current_zone.lot
        else:
            target_object = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection, notify_failure=False)
            if target_object is None:
                target_object = get_optional_target((OptionalTargetParam(str(opt_sim.target_id))), _connection=_connection, notify_failure=False)
        if target_object is not None:
            tracker = target_object.get_tracker(stat_type)
            tracker.set_value(stat_type, value)
    else:
        sims4.commands.output('No target found with ID:{} stats.set_stat.'.format(opt_sim.target_id), _connection)


@sims4.commands.Command('stats.set_lot_level_stat')
def set_lot_level_statistic(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), value: float=None, level: int=None, _connection=None):
    if stat_type is not None and value is not None and level is not None:
        lot = services.active_lot()
        lot_level = lot.get_lot_level_instance(level)
        if lot_level is None:
            sims4.commands.output('Invalid level: {}.'.format(level), _connection)
            return
        tracker = lot_level.get_tracker(stat_type)
        tracker.set_value(stat_type, value)
    else:
        sims4.commands.output('Invalid arguments. Params: stat_name, value, level', _connection)


@sims4.commands.Command('fillmotive', command_type=(sims4.commands.CommandType.Cheat))
def fill_motive(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), _connection=None):
    if stat_type is not None:
        tgt_client = services.client_manager().get(_connection)
        tracker = tgt_client.active_sim.get_tracker(stat_type)
        tracker.set_value(stat_type, stat_type.max_value)
        return True
    return False


@sims4.commands.Command('stats.add_to_stat', 'stats.add_to_commodity')
def add_value_to_statistic(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), value: float=None, opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None and stat_type is not None and value is not None:
        tracker = target.get_tracker(stat_type)
        tracker.add_value(stat_type, value)
    else:
        sims4.commands.output('No target for stats.add_to_stat. Params: stat_name, value, optional target', _connection)


@sims4.commands.Command('stats.add_stat_to_tracker', 'stats.add_commodity_to_tracker')
def add_statistic_to_tracker(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None and stat_type is not None:
        tracker = target.get_tracker(stat_type)
        stat = tracker.add_statistic(stat_type)
        if stat is None:
            sims4.commands.output('Stat not added to tracker', _connection)
    else:
        sims4.commands.output('No target for stats.add_stat_to_tracker. Params: stat_name, optional target', _connection)


@sims4.commands.Command('stats.remove_stat', 'stats.remove_commodity')
def remove_statistic(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None and stat_type is not None:
        tracker = target.get_tracker(stat_type)
        tracker.remove_statistic(stat_type)
    else:
        sims4.commands.output('No target for stats.remove_stat. Params: stat_name, optional target', _connection)


@sims4.commands.Command('stats.add_static_commodity_to_tracker')
def add_static_commodity_to_tracker(static_commodity: TunableInstanceParam(sims4.resources.Types.STATIC_COMMODITY), opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None:
        tracker = target.get_tracker(static_commodity)
        tracker.add_statistic(static_commodity)
    else:
        sims4.commands.output('No target for stats.add_static_commodity_to_tracker. Params: stat_name, optional target', _connection)


@sims4.commands.Command('stats.remove_static_commodity_from_tracker')
def remove_static_commodity_from_tracker(static_commodity: TunableInstanceParam(sims4.resources.Types.STATIC_COMMODITY), opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None:
        tracker = target.get_tracker(static_commodity)
        tracker.remove_statistic(static_commodity)
    else:
        sims4.commands.output('No target for stats.remove_static_commodity_from_tracker. Params: stat_name, optional target', _connection)


@sims4.commands.Command('stats.set_modifier', command_type=(sims4.commands.CommandType.Live))
def set_modifier(stat_type: TunableInstanceParam(sims4.resources.Types.STATISTIC), level: float=None, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None or stat_type is None or level is None:
        sims4.commands.output('Unable to set modifier - invalid arguments.', _connection)
        return
    stat = sim.get_statistic(stat_type)
    if stat is None:
        stat = sim.add_statistic(stat_type)
    stat.add_statistic_modifier(level)
    if isinstance(stat, Skill):
        sim.sim_info.current_skill_guid = stat.guid64


@sims4.commands.Command('stats.remove_modifier', command_type=(sims4.commands.CommandType.Live))
def remove_modifier(stat_type: TunableInstanceParam(sims4.resources.Types.STATISTIC), level: float=None, opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None or stat_type is None or level is None:
        sims4.commands.output('Unable to remove modifier - invalid arguments.', _connection)
        return
    stat = sim.get_statistic(stat_type)
    if stat is None:
        return
    stat.remove_statistic_modifier(level)
    if isinstance(stat, Skill):
        if stat._statistic_modifier <= 0:
            if sim.sim_info.current_skill_guid == stat.guid64:
                sim.sim_info.current_skill_guid = 0


def _set_skill_level(stat_type, level, sim, _connection):
    stat = sim.commodity_tracker.get_statistic(stat_type)
    if stat is None:
        stat = sim.commodity_tracker.add_statistic(stat_type)
        if stat is None:
            sims4.commands.output('Unable to add Skill due to entitlement restriction {}.'.format(stat_type), _connection)
            return
    if not isinstance(stat, statistics.skill.Skill):
        sims4.commands.output('Unable to set Skill level - statistic {} is a {}, not a skill.'.format(stat_type, type(stat)), _connection)
        return
    sims4.commands.output('Setting Skill {0} to level {1}'.format(stat_type, level), _connection)
    sim.commodity_tracker.set_user_value(stat_type, level)


@sims4.commands.Command('stats.set_skill_level', command_type=(sims4.commands.CommandType.Cheat))
def set_skill_level--- This code section failed: ---

 L. 356         0  LOAD_GLOBAL              get_optional_target
                2  LOAD_FAST                'opt_sim'
                4  LOAD_FAST                '_connection'
                6  CALL_FUNCTION_2       2  '2 positional arguments'
                8  STORE_FAST               'sim'

 L. 357        10  LOAD_FAST                'sim'
               12  LOAD_CONST               None
               14  COMPARE_OP               is
               16  POP_JUMP_IF_TRUE     44  'to 44'
               18  LOAD_FAST                'stat_type'
               20  LOAD_CONST               None
               22  COMPARE_OP               is
               24  POP_JUMP_IF_TRUE     44  'to 44'
               26  LOAD_FAST                'level'
               28  LOAD_CONST               None
               30  COMPARE_OP               is
               32  POP_JUMP_IF_TRUE     44  'to 44'
               34  LOAD_FAST                'sim'
               36  LOAD_ATTR                commodity_tracker
               38  LOAD_CONST               None
               40  COMPARE_OP               is
               42  POP_JUMP_IF_FALSE    62  'to 62'
             44_0  COME_FROM            32  '32'
             44_1  COME_FROM            24  '24'
             44_2  COME_FROM            16  '16'

 L. 358        44  LOAD_GLOBAL              sims4
               46  LOAD_ATTR                commands
               48  LOAD_METHOD              output
               50  LOAD_STR                 'Unable to set Skill level - invalid arguments or sim info has no commodity tracker.'
               52  LOAD_FAST                '_connection'
               54  CALL_METHOD_2         2  '2 positional arguments'
               56  POP_TOP          

 L. 359        58  LOAD_CONST               None
               60  RETURN_VALUE     
             62_0  COME_FROM            42  '42'

 L. 361        62  LOAD_GLOBAL              _set_skill_level
               64  LOAD_FAST                'stat_type'
               66  LOAD_FAST                'level'
               68  LOAD_FAST                'sim'
               70  LOAD_FAST                '_connection'
               72  CALL_FUNCTION_4       4  '4 positional arguments'
               74  POP_TOP          

Parse error at or near `CALL_FUNCTION_4' instruction at offset 72


@sims4.commands.Command('stats.set_all_skills_max', command_type=(sims4.commands.CommandType.Automation))
def set_skills_to_max_level(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None or sim.commodity_tracker is None:
        sims4.commands.output('Unable to max skills - invalid sim or sim info has no commodity tracker.', _connection)
        return
    skill_types = set()
    skill_manager = services.get_instance_manager(sims4.resources.Types.STATISTIC)
    for skill_type in skill_manager.all_skills_gen():
        if skill_type.can_add(sim):
            skill_types.add(skill_type)

    while len(skill_types) != 0:
        new_skill_types = set()
        for skill_type in skill_types:
            _set_skill_levelskill_typeskill_type.max_levelsim_connection
            for unlockable_skill_type in skill_type.skill_unlocks_on_max:
                if sim.commodity_tracker.get_user_value(unlockable_skill_type) != skill_type.max_level:
                    new_skill_types.add(unlockable_skill_type)

        skill_types = new_skill_types


@sims4.commands.Command('stats.clear_skill')
def clear_skill(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Invalid Sim id: {}'.format(opt_sim), _connection)
        return
    tracker = sim.commodity_tracker
    if tracker is None:
        sims4.commands.output('Unable to clear_skill - sim info has no commodity tracker.', _connection)
        return
    statistics = list(tracker)
    stats_removed = []
    for stat in statistics:
        if stat.is_skill:
            stat_type = type(stat)
            stats_removed.append(stat_type)
            tracker.remove_statistic(stat_type)

    sims4.commands.output('Removed {} skills from {}'.format(len(stats_removed), sim), _connection)


@sims4.commands.Command('stats.solve_motive', command_type=(sims4.commands.CommandType.Live))
def solve_motive(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None or stat_type is None:
        sims4.commands.output('Unable to identify Sim or Motive - invalid arguments.', _connection)
        return
    if sim.commodity_tracker is None:
        sims4.commands.output('Unable to solve motive - sim info has no commodity tracker.', _connection)
        return
    stat = sim.commodity_tracker.get_statistic(stat_type)
    if stat is None:
        sims4.commands.output('Unable to solve motive {} on the Sim .'.format(stat_type), _connection)
        return
    if not sim.queue.can_queue_visible_interaction():
        sims4.commands.output('Interaction queue is full, cannot add anymore interactions.', _connection)
        return
    context = InteractionContext(sim, (InteractionContext.SOURCE_AUTONOMY), (priority.Priority.High),
      bucket=(InteractionBucketType.DEFAULT))
    autonomy_request = autonomy.autonomy_request.AutonomyRequest(sim, autonomy_mode=(autonomy.autonomy_modes.FullAutonomy), commodity_list=[
     stat],
      context=context,
      consider_scores_of_zero=True,
      posture_behavior=(AutonomyPostureBehavior.IGNORE_SI_STATE),
      is_script_request=True,
      allow_opportunity_cost=False,
      autonomy_mode_label_override='AutoSolveMotive')
    selected_interaction = services.autonomy_service().find_best_action(autonomy_request)
    if selected_interaction is None:
        commodity_interaction = stat_type.commodity_autosolve_failure_interaction
        if commodity_interaction is None:
            return
        if not sim.queue.has_duplicate_super_affordance(commodity_interaction, sim, None):
            failure_aop = AffordanceObjectPaircommodity_interactionNonecommodity_interactionNone
            failure_aop.test_and_execute(context)
        sims4.commands.output('Could not find a good interaction to solve {}.'.format(stat_type), _connection)
        return
    if sim.queue.has_duplicate_super_affordance(selected_interaction.affordance, sim, selected_interaction.target):
        sims4.commands.output('Duplicate Interaction in the queue.', _connection)
        return
    if not AffordanceObjectPair.execute_interaction(selected_interaction):
        sims4.commands.output('Failed to execute SI {}.'.format(selected_interaction), _connection)
        return
    sims4.commands.output('Successfully executed SI {}.'.format(selected_interaction), _connection)


def _randomize_motive(stat_type, sim, min_value, max_value):
    if min_value is None or min_value < stat_type.min_value:
        min_value = stat_type.min_value
    if max_value is None or max_value > stat_type.max_value:
        max_value = stat_type.max_value
    random_value = random.uniform(min_value, max_value)
    sim.set_stat_value(stat_type, random_value)


@sims4.commands.Command('stats.randomize_motives')
def randomize_motives--- This code section failed: ---

 L. 500         0  LOAD_FAST                'opt_sim'
                2  LOAD_CONST               None
                4  COMPARE_OP               is-not
                6  POP_JUMP_IF_FALSE    68  'to 68'

 L. 501         8  LOAD_GLOBAL              get_optional_target
               10  LOAD_FAST                'opt_sim'
               12  LOAD_FAST                '_connection'
               14  CALL_FUNCTION_2       2  '2 positional arguments'
               16  STORE_FAST               'sim'

 L. 502        18  LOAD_FAST                'sim'
               20  LOAD_CONST               None
               22  COMPARE_OP               is
               24  POP_JUMP_IF_FALSE   124  'to 124'

 L. 503        26  LOAD_GLOBAL              sims4
               28  LOAD_ATTR                commands
               30  LOAD_METHOD              output
               32  LOAD_STR                 'Unable to identify Sim - invalid arguments.'
               34  LOAD_FAST                '_connection'
               36  CALL_METHOD_2         2  '2 positional arguments'
               38  POP_TOP          

 L. 504        40  LOAD_CONST               None
               42  RETURN_VALUE     

 L. 506        44  FOR_ITER             64  'to 64'
               46  STORE_FAST               'stat_type'

 L. 507        48  LOAD_GLOBAL              _randomize_motive
               50  LOAD_FAST                'stat_type'
               52  LOAD_FAST                'sim'
               54  LOAD_FAST                'min_value'
               56  LOAD_FAST                'max_value'
               58  CALL_FUNCTION_4       4  '4 positional arguments'
               60  POP_TOP          
               62  JUMP_BACK            44  'to 44'
               64  POP_BLOCK        
               66  JUMP_FORWARD        124  'to 124'
             68_0  COME_FROM             6  '6'

 L. 509        68  SETUP_LOOP          124  'to 124'
               70  LOAD_GLOBAL              services
               72  LOAD_METHOD              sim_info_manager
               74  CALL_METHOD_0         0  '0 positional arguments'
               76  LOAD_METHOD              instanced_sims_gen
               78  CALL_METHOD_0         0  '0 positional arguments'
               80  GET_ITER         
               82  FOR_ITER            122  'to 122'
               84  STORE_FAST               'sim'

 L. 510        86  SETUP_LOOP          120  'to 120'
               88  LOAD_FAST                'sim'
               90  LOAD_ATTR                sim_info
               92  LOAD_METHOD              get_initial_commodities
               94  CALL_METHOD_0         0  '0 positional arguments'
               96  GET_ITER         
               98  FOR_ITER            118  'to 118'
              100  STORE_FAST               'stat_type'

 L. 511       102  LOAD_GLOBAL              _randomize_motive
              104  LOAD_FAST                'stat_type'
              106  LOAD_FAST                'sim'
              108  LOAD_FAST                'min_value'
              110  LOAD_FAST                'max_value'
              112  CALL_FUNCTION_4       4  '4 positional arguments'
              114  POP_TOP          
              116  JUMP_BACK            98  'to 98'
              118  POP_BLOCK        
            120_0  COME_FROM_LOOP       86  '86'
              120  JUMP_BACK            82  'to 82'
              122  POP_BLOCK        
            124_0  COME_FROM_LOOP       68  '68'
            124_1  COME_FROM            66  '66'
            124_2  COME_FROM            24  '24'

Parse error at or near `FOR_ITER' instruction at offset 44


@sims4.commands.Command('stats.set_convergence')
def set_convergence(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), convergence: float=None, opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None and stat_type is not None and convergence is not None:
        tracker = target.get_tracker(stat_type)
        tracker.set_convergence(stat_type, convergence)
    else:
        sims4.commands.output('No target for stats.set_convergence.', _connection)


@sims4.commands.Command('stats.reset_convergence')
def reset_convergence(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_target: OptionalTargetParam=None, _connection=None):
    target = get_optional_target(opt_target, _connection)
    if target is not None and stat_type is not None:
        tracker = target.get_tracker(stat_type)
        tracker.reset_convergence(stat_type)
    else:
        sims4.commands.output('No target for stats.reset_convergence.', _connection)


def _set_stat_percent(stat, tracker, percent, _connection=0):
    stat_range = stat.max_value_tuning - stat.min_value_tuning
    stat_value = percent * stat_range + stat.min_value_tuning
    sims4.commands.output('Setting Statistic {0} to {1}'.format(stat.__name__, stat_value), _connection)
    tracker.set_value(stat, stat_value)


def _set_overall_ranked_stat_percent(ranked_stat_type, tracker, percent, _connection):
    ranked_stat = tracker.get_statistic(ranked_stat_type)
    min_points = ranked_stat.min_value
    max_points = ranked_stat.max_value
    stat_range = max_points - min_points
    stat_value = percent * stat_range + min_points
    sims4.commands.output('Setting Statistic {0} to {1}'.format(ranked_stat, stat_value), _connection)
    tracker.set_value(ranked_stat_type, stat_value)


def _set_ranked_stat_percent(ranked_stat_type, tracker, percent, _connection):
    ranked_stat = tracker.get_statistic(ranked_stat_type)
    rank = ranked_stat.rank_level
    min_points = ranked_stat.points_to_rank(rank)
    max_points = ranked_stat.points_to_rank(rank + 1)
    stat_range = max_points - min_points
    stat_value = percent * stat_range + min_points
    sims4.commands.output('Setting Statistic {0} to {1}'.format(ranked_stat, stat_value), _connection)
    tracker.set_value(ranked_stat_type, stat_value)


@sims4.commands.Command('stats.set_commodity_percent')
def set_commodity_percent(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), value: float=None, opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('No valid target for stats.set_commodity_percent.', _connection)
        return
    tracker = sim_info.get_tracker(stat_type)
    if stat_type is not None:
        if value is not None and tracker is not None:
            if stat_type.is_ranked:
                _set_overall_ranked_stat_percent(stat_type, tracker, value, _connection=_connection)
        else:
            _set_stat_percent(stat_type, tracker, value, _connection=_connection)
    else:
        sims4.commands.output('Unable to set Commodity - invalid arguments or sim info has no commodity tracker.', _connection)


@sims4.commands.Command('stats.set_ranked_commodity_percent_of_current_rank')
def set_commodity_percent_of_current_rank(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), value: float=None, opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('No valid target for stats.set_ranked_commodity_percent_of_current_rank.', _connection)
        return
    tracker = sim_info.get_tracker(stat_type)
    if stat_type is not None:
        if value is not None and tracker is not None:
            if stat_type.is_ranked:
                _set_ranked_stat_percent(stat_type, tracker, value, _connection=_connection)
        else:
            sims4.commands.output('Stat type for {0} is not ranked, use stats.set_commodity_percent instead'.format(stat_type), _connection)
    else:
        sims4.commands.output('Unable to set Commodity - invalid arguments or sim info has no commodity tracker.', _connection)


@sims4.commands.Command('stats.set_commodity_best_value')
def set_commodity_best_value(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim_info is None:
        sims4.commands.output('No valid target for stats.set_commodity_best_value.', _connection)
        return
    tracker = sim_info.get_tracker(stat_type)
    if stat_type is not None and tracker is not None:
        tracker.set_value(stat_type, stat_type.best_value)
    else:
        sims4.commands.output('Unable to set commodity for stats.set_commodity_best_value', _connection)


@sims4.commands.Command('stats.set_all_sim_commodities_best_value_except', 'stats.fill_all_sim_commodities_except')
def set_all_sim_commodities_best_value_except(stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), opt_sim: OptionalTargetParam=None, _connection=None):
    if stat_type is not None:
        if opt_sim is not None:
            sim = get_optional_target(opt_sim, _connection)
            if sim is None:
                sims4.commands.output('No valid target for stats.set_all_sim_commodities_best_value_except.', _connection)
                return
            tracker = sim.get_tracker(stat_type)
            if tracker is None:
                sims4.commands.output('No tracker on target for stats.set_all_sim_commodities_best_value_except.', _connection)
                return
            tracker.debug_set_all_to_best_except(stat_type)
        else:
            for sim in services.sim_info_manager().instanced_sims_gen():
                tracker = sim.get_tracker(stat_type)
                tracker.debug_set_all_to_best_except(stat_type)

    else:
        sims4.commands.output('Unable to set Commodity - commodity {} not found.'.format(stat_type.lower()), _connection)


with sims4.reload.protected(globals()):
    autonomy_handles = collections.defaultdict(weakref.WeakKeyDictionary)

@sims4.commands.Command('stats.enable_commodities', command_type=(sims4.commands.CommandType.Cheat))
def enable_commodities(opt_sim: OptionalTargetParam=None, *stat_types: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), _connection=None):
    global autonomy_handles
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No valid target for stats.enable_commodities', _connection)
        return
    for stat_type in stat_types:
        if sim in autonomy_handles[stat_type]:
            sim.remove_statistic_modifier(autonomy_handles[stat_type][sim])
            del autonomy_handles[stat_type][sim]


@sims4.commands.Command('stats.enable_all_commodities', command_type=(sims4.commands.CommandType.Cheat))
def enable_all_commodities(opt_sim: OptionalTargetParam=None, _connection=None):
    if opt_sim is not None:
        sim = get_optional_target(opt_sim, _connection)
        if sim is None:
            sims4.commands.output('No valid target for stats.enable_all_commodities', _connection)
            return
        for sim_handle_dictionary in autonomy_handles.values():
            if sim in sim_handle_dictionary:
                sim.remove_statistic_modifier(sim_handle_dictionary[sim])
                del sim_handle_dictionary[sim]

    else:
        for sim_handle_dictionary in autonomy_handles.values():
            for sim, handle in sim_handle_dictionary.items():
                sim.remove_statistic_modifier(handle)

            sim_handle_dictionary.clear()


def _disable_commodities(sim, commodities_to_lock=[]):
    for commodity in commodities_to_lock:
        if sim in autonomy_handles[commodity]:
            return
        modifier = autonomy.autonomy_modifier.AutonomyModifier(decay_modifiers={commodity: 0})
        handle = sim.add_statistic_modifier(modifier)
        autonomy_handles[commodity][sim] = handle


@sims4.commands.Command('stats.disable_commodities', command_type=(sims4.commands.CommandType.Cheat))
def disable_commodities(opt_sim: OptionalTargetParam=None, *stat_types: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True), _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('No valid target for stats.disable_commodities', _connection)
        return
    _disable_commodities(sim, stat_types)


@sims4.commands.Command('stats.disable_all_commodities', command_type=(sims4.commands.CommandType.Cheat))
def disable_all_commodities(opt_sim: OptionalTargetParam=None, _connection=None):
    if opt_sim is not None:
        sim = get_optional_target(opt_sim, _connection)
        if sim is None:
            sims4.commands.output('No valid target for stats.disable_sim_commodities', _connection)
            return
        _disable_commodities(sim, sim.sim_info.get_initial_commodities())
    else:
        for sim in services.sim_info_manager().instanced_sims_gen():
            _disable_commodities(sim, sim.sim_info.get_initial_commodities())


@sims4.commands.Command('stats.enable_autosatisfy_curves', command_type=(sims4.commands.CommandType.Cheat))
def enable_autosatisfy_curves(_connection=None):
    Commodity.use_autosatisfy_curve = True


@sims4.commands.Command('stats.disable_autosatisfy_curves', command_type=(sims4.commands.CommandType.Cheat))
def disable_autosatisfy_curves(_connection=None):
    Commodity.use_autosatisfy_curve = False


@sims4.commands.Command('stats.publish_ranked_stat_progress', command_type=(sims4.commands.CommandType.Live))
def publish_ranked_stat_progress(opt_sim: OptionalSimInfoParam=None, stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True)=None, _connection=None):
    sim = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim is None:
        sims4.commands.output('No Sim specified, you must specify a Sim to get the rank.', _connection)
        return
    if not hasattr(stat_type, 'rank_level'):
        sims4.commands.output('The specified statistic is not a Ranked Statistic and therefore has no Rank, please specify a Ranked Statistic.', _connection)
        return
    commodity_tracker = sim.commodity_tracker
    stat = commodity_tracker.get_statistic(stat_type)
    if stat is None:
        sims4.commands.output("Sim doesn't have the specified statistic.", _connection)
        return
    stat.create_and_send_commodity_update_msg(is_rate_change=False, allow_npc=True)


@sims4.commands.Command('stats.set_rank', command_type=(sims4.commands.CommandType.Live))
def ranked_stat_set_rank(opt_sim: OptionalSimInfoParam=None, stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True)=None, rank: int=1, _connection=None):
    sim = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim is None:
        sims4.commands.output('No Sim specified, you must specify a Sim to set the rank on.', _connection)
        return
    elif not hasattr(stat_type, 'rank_level'):
        sims4.commands.output('The specified statistic is not a Ranked Statistic and therefore has no Rank, please specify a Ranked Statistic.', _connection)
        return
        commodity_tracker = sim.commodity_tracker
        stat = commodity_tracker.get_statistic(stat_type)
        if stat.rank_level == rank:
            return
        stat.set_value(stat.points_to_rank(rank))
        if stat.rank_level == rank:
            sims4.commands.output('Success.', _connection)
    else:
        sims4.commands.output('Failure, sim is now set to rank {}'.format(stat.rank_level), _connection)


@sims4.commands.Command('stats.get_rank', command_type=(sims4.commands.CommandType.Automation))
def ranked_stat_get_rank(opt_sim: OptionalSimInfoParam=None, stat_type: TunableInstanceParam((sims4.resources.Types.STATISTIC), exact_match=True)=None, _connection=None):
    sim = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim is None:
        sims4.commands.output('No Sim specified, you must specify a Sim.', _connection)
        sims4.commands.automation_output('RankedStat; Status:Failed', _connection)
        return
    if not hasattr(stat_type, 'rank_level'):
        sims4.commands.output('The specified statistic is not a Ranked Statistic and therefore has no Rank, please specify a Ranked Statistic.', _connection)
        sims4.commands.automation_output('RankedStat; Status:Failed', _connection)
        return
    commodity_tracker = sim.commodity_tracker
    stat = commodity_tracker.get_statistic(stat_type)
    sims4.commands.automation_output('RankedStat; Status:Success, RankLevel:{}'.format(stat.rank_level), _connection)


@sims4.commands.Command('stats.count_commodities')
def count_commodities(_connection=None):
    counter = Counter()
    sim_info_manager = services.sim_info_manager()
    for sim_info in sim_info_manager.values():
        commodity_tracker = sim_info.commodity_tracker
        for commodity in commodity_tracker:
            counter[commodity.stat_type] += 1

    sorted_counter = list(counter.items())
    sorted_counter.sort(key=(lambda item: item[1]))
    for commodity_type, count in sorted_counter:
        sims4.commands.output('Commodity Type: {} : Count: {}'.format(commodity_type, count), _connection)


@sims4.commands.Command('stats.reset_daily_cap')
def reset_daily_caps(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim is None:
        sims4.commands.output('No Sim to reset the trait statistic daily caps.', _connection)
        return
    sim.sim_info.trait_statistic_tracker.reset_daily_caps()


@sims4.commands.Command('stats.perform_end_of_day_behavior')
def reset_daily_caps(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    if sim is None:
        sims4.commands.output('No Sim to reset the trait statistic daily caps.', _connection)
        return
    sim.sim_info.trait_statistic_tracker.on_day_end()


@sims4.commands.Command('lifestyles.set_lifestyles_effects_enabled', command_type=(sims4.commands.CommandType.Live))
def set_lifestyles_effects_enabled(enabled: bool=True, _connection=None):
    services.lifestyle_service().set_lifestyles_enabled(enabled)
