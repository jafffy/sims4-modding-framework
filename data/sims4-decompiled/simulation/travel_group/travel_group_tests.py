# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\travel_group\travel_group_tests.py
# Compiled at: 2020-11-12 15:43:22
# Size of source mod 2**32: 8657 bytes

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
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
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
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4 . 
call_stmt ::= expr . POP_TOP
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
continues ::= lastl_stmt . continue
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= call_kw36 . 
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
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE COME_FROM . 
expr_stmt ::= expr . POP_TOP
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit_come_from . expr
or ::= expr_pjit_come_from expr . 
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
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
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
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= testfalse_not_and . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= and jmp_true . come_froms
testfalse_not_and ::= and jmp_true come_froms . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true COME_FROM . 
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  68        44  LOAD_GLOBAL              TestResult
                  46  LOAD_ATTR                TRUE
->                48  RETURN_VALUE     
import sims4.math
from event_testing.test_base import BaseTest
from event_testing.results import TestResult
from caches import cached_test
from interactions import ParticipantType
from sims4.tuning.tunable import HasTunableSingletonFactory, TunableEnumEntry, AutoFactoryInit, Tunable, TunableVariant, TunableThreshold, TunableRange
from singletons import EMPTY_SET

class _TravelGroupTestVariantBase(HasTunableSingletonFactory, AutoFactoryInit):

    @property
    def additional_expected_args(self):
        return EMPTY_SET

    @property
    def requires_existing_travel_group(self):
        return True

    def _test_travel_group(self, participant, travel_group, tooltip, **kwargs):
        raise NotImplementedError


class _TravelGroupExists(_TravelGroupTestVariantBase):
    FACTORY_TUNABLES = {'exists': Tunable(description='\n            If checked, this test will fail if the Sim is not in a\n            travel group. If unchecked, this test will fail if the Sim\n            is in a travel group.\n            ',
                 tunable_type=bool,
                 default=True)}

    @property
    def requires_existing_travel_group(self):
        return self.exists

    def _test_travel_group--- This code section failed: ---

 L.  65         0  LOAD_FAST                'travel_group'
                2  LOAD_CONST               None
                4  COMPARE_OP               is
                6  POP_JUMP_IF_FALSE    14  'to 14'
                8  LOAD_FAST                'self'
               10  LOAD_ATTR                exists
               12  POP_JUMP_IF_TRUE     28  'to 28'
             14_0  COME_FROM             6  '6'

 L.  66        14  LOAD_FAST                'travel_group'
               16  LOAD_CONST               None
               18  COMPARE_OP               is-not
               20  POP_JUMP_IF_FALSE    44  'to 44'
               22  LOAD_FAST                'self'
               24  LOAD_ATTR                exists
               26  POP_JUMP_IF_TRUE     44  'to 44'
             28_0  COME_FROM            12  '12'

 L.  67        28  LOAD_GLOBAL              TestResult
               30  LOAD_CONST               False
               32  LOAD_STR                 'Participant {} is not in a travel group as expected.'
               34  LOAD_FAST                'participant'
               36  LOAD_FAST                'tooltip'
               38  LOAD_CONST               ('tooltip',)
               40  CALL_FUNCTION_KW_4     4  '4 total positional and keyword args'
               42  RETURN_VALUE     
             44_0  COME_FROM            26  '26'
             44_1  COME_FROM            20  '20'

 L.  68        44  LOAD_GLOBAL              TestResult
               46  LOAD_ATTR                TRUE
               48  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 48


class _TravelGroupAddParticipant(_TravelGroupTestVariantBase):
    FACTORY_TUNABLES = {'participant': TunableEnumEntry(description='\n            The participant to be added.\n            ',
                      tunable_type=ParticipantType,
                      default=(ParticipantType.TargetSim))}

    @property
    def additional_expected_args(self):
        return {'targets': self.participant}

    def _test_travel_group(self, participant, travel_group, tooltip, targets=(), **kwargs):
        if not targets or any((not t.is_sim or not travel_group.can_add_to_travel_group(t) for t in targets)):
            return TestResult(False, 'Target cannot be added to travel group {}', travel_group, tooltip=tooltip)
        return TestResult.TRUE


class _TravelGroupFreeSlots(_TravelGroupTestVariantBase):
    FACTORY_TUNABLES = {'count': TunableThreshold(description='\n            The number of required free slots for the specified\n            travel group.\n            ',
                value=TunableRange(description='\n                The range of required free slots.\n                ',
                tunable_type=int,
                minimum=0,
                default=1),
                default=(sims4.math.Threshold(1, sims4.math.Operator.GREATER_OR_EQUAL.function)))}

    def _test_travel_group(self, participant, travel_group, tooltip, **kwargs):
        free_slot_count = travel_group.free_slot_count
        if not self.count.compare(free_slot_count):
            return TestResult(False, "Travel Group doesn't meet free slot count requirement.", tooltip=tooltip)
        return TestResult.TRUE


class _TravelGroupCanExtendStay(_TravelGroupTestVariantBase):

    def _test_travel_group(self, participant, travel_group, tooltip, **kwargs):
        if travel_group.end_timestamp is None:
            return TestResult(False, 'Travel group {} has no end time set and cannot be extended', travel_group, tooltip=tooltip)
        return TestResult.TRUE


class TravelGroupTest(BaseTest, HasTunableSingletonFactory):
    test_events = ()
    FACTORY_TUNABLES = {'participant':TunableEnumEntry(description='\n            The subject whose travel group is the object of this test.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor), 
     'include_household_travel_group':Tunable(description="\n            If checked, the travel group that any sims in the participant's\n            household will be used in the event that the participant is not\n            actually on vacation.\n            ",
       tunable_type=bool,
       default=False), 
     'test_type':TunableVariant(description="\n            The type of test to determine what about this travel group's size\n            we care about.\n            ",
       in_travel_group=_TravelGroupExists.TunableFactory(description='\n                Use this option when testing to see if the participant exists\n                in the travel group or not.\n                '),
       participant=_TravelGroupAddParticipant.TunableFactory(description="\n                Use this option when you're testing a specific Sim being added\n                to the travel group.\n                "),
       count=_TravelGroupFreeSlots.TunableFactory(description="\n                Use this option when you're testing for a specific number of\n                free slots in the travel group.\n                "),
       can_extend=_TravelGroupCanExtendStay.TunableFactory(description='\n                Use this option to check whether or not a participant can\n                extend their vacation. This test will fail if the participant is\n                not in a travel group or their travel group does not have\n                an end time specified.\n                '),
       default='count')}

    def __init__(self, participant, test_type, include_household_travel_group, **kwargs):
        (super().__init__)(**kwargs)
        self.participant = participant
        self.include_household_travel_group = include_household_travel_group
        self.test_type = test_type
        self._expected_args = {'participants': self.participant}
        if test_type.additional_expected_args:
            self._expected_args.update(test_type.additional_expected_args)

    def get_expected_args(self):
        return self._expected_args

    @cached_test
    def __call__(self, participants=(), targets=()):
        for participant in participants:
            if not participant.is_sim:
                return TestResult(False, 'Participant {} is not a sim.', participant, tooltip=(self.tooltip))
                travel_group = participant.travel_group
                if travel_group is None:
                    if self.include_household_travel_group:
                        travel_group = participant.household.get_travel_group()
                if travel_group is None:
                    if self.test_type.requires_existing_travel_group:
                        return TestResult(False, 'Participant {} is not in a travel group.', participant, tooltip=(self.tooltip))
                test_result = self.test_type._test_travel_group(participant, travel_group, (self.tooltip), targets=targets)
                return test_result or test_result

        return TestResult.TRUE
