# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\contour.py
# Compiled at: 2016-04-29 00:25:11
# Size of source mod 2**32: 8053 bytes

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
alias ::= IMPORT_NAME . attributes store
alias ::= IMPORT_NAME . store
alias ::= IMPORT_NAME store . 
alias ::= IMPORT_NAME_ATTR . attributes store
alias ::= IMPORT_NAME_ATTR . store
alias ::= IMPORT_NAME_ATTR store . 
alias37 ::= IMPORT_NAME . store
alias37 ::= IMPORT_NAME store . 
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_MULTIPLY . 
binary_operator ::= BINARY_TRUE_DIVIDE . 
build_class ::= LOAD_BUILD_CLASS . mkfunc expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc . expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr . CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr CALL_FUNCTION_2 . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdef ::= build_class . store
classdef ::= build_class store . 
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
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
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
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
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
import ::= LOAD_CONST LOAD_CONST . alias
import ::= LOAD_CONST LOAD_CONST alias . 
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST . importlist37 store POP_TOP
import_as37 ::= LOAD_CONST LOAD_CONST importlist37 . store POP_TOP
import_cont ::= LOAD_CONST . LOAD_CONST alias
import_cont ::= LOAD_CONST LOAD_CONST . alias
import_cont ::= LOAD_CONST LOAD_CONST alias . 
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST . importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST IMPORT_NAME . importlist POP_TOP
import_from ::= LOAD_CONST LOAD_CONST importlist . POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR importlist37 POP_TOP
import_from37 ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR . importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_as37 ::= LOAD_CONST LOAD_CONST . import_from_attr37 store POP_TOP
import_from_attr37 ::= IMPORT_NAME_ATTR . IMPORT_FROM
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST . IMPORT_NAME_ATTR IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST IMPORT_NAME . IMPORT_STAR
import_from_star ::= LOAD_CONST LOAD_CONST IMPORT_NAME_ATTR . IMPORT_STAR
import_one ::= importlists . ROT_TWO IMPORT_FROM
import_one ::= importlists . ROT_TWO POP_TOP IMPORT_FROM
importattr37 ::= IMPORT_NAME_ATTR . IMPORT_FROM
importlist ::= alias . 
importlist ::= importlist . alias
importlist37 ::= alias37 . 
importlist37 ::= importlist37 . alias37
importlists ::= importlist37 . 
importlists ::= importlists . importlist37
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
importmultiple ::= LOAD_CONST LOAD_CONST . alias imports_cont
importmultiple ::= LOAD_CONST LOAD_CONST alias . imports_cont
importmultiple ::= LOAD_CONST LOAD_CONST alias imports_cont . 
imports_cont ::= import_cont . 
imports_cont ::= imports_cont . import_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
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
stmt ::= classdef . 
stmt ::= function_def . 
stmt ::= import . 
stmt ::= importmultiple . 
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr BUILD_TUPLE_2 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  28        64  LOAD_FAST                'index'
->                66  RETURN_VALUE     
import math, sims4.math
HEIGHT = math.sqrt(3) / 2
POS_INF = float('inf')
NEG_INF = float('-inf')
EVEN_DELTAS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))
ODD_DELTAS = ((1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1))
DELTAS = (EVEN_DELTAS, ODD_DELTAS)

def _delta_to_ix--- This code section failed: ---

 L.  23         0  LOAD_FAST                'ix'
                2  LOAD_FAST                'dx'
                4  BINARY_ADD       
                6  STORE_FAST               'jx'

 L.  24         8  LOAD_FAST                'iy'
               10  LOAD_FAST                'dy'
               12  BINARY_ADD       
               14  STORE_FAST               'jy'

 L.  25        16  LOAD_FAST                'jx'
               18  LOAD_CONST               0
               20  COMPARE_OP               <
               22  POP_JUMP_IF_TRUE     48  'to 48'
               24  LOAD_FAST                'jx'
               26  LOAD_FAST                'nx'
               28  COMPARE_OP               >=
               30  POP_JUMP_IF_TRUE     48  'to 48'
               32  LOAD_FAST                'jy'
               34  LOAD_CONST               0
               36  COMPARE_OP               <
               38  POP_JUMP_IF_TRUE     48  'to 48'
               40  LOAD_FAST                'jy'
               42  LOAD_FAST                'ny'
               44  COMPARE_OP               >=
               46  POP_JUMP_IF_FALSE    52  'to 52'
             48_0  COME_FROM            38  '38'
             48_1  COME_FROM            30  '30'
             48_2  COME_FROM            22  '22'

 L.  26        48  LOAD_CONST               None
               50  RETURN_VALUE     
             52_0  COME_FROM            46  '46'

 L.  27        52  LOAD_FAST                'jx'
               54  LOAD_FAST                'jy'
               56  LOAD_FAST                'nx'
               58  BINARY_MULTIPLY  
               60  BINARY_ADD       
               62  STORE_FAST               'index'

 L.  28        64  LOAD_FAST                'index'
               66  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_VALUE' instruction at offset 66


def _edge_intercept(vt, vf, value, values, points):
    delta = values[vt] - values[vf]
    delta_t = values[vt] - value
    tf = delta_t / delta
    pt = sims4.math.interpolate(points[vt], points[vf], tf)
    return pt


class HeightField:

    def __init__(self, fn, bounding_rect, spacing):
        self.fn = fn
        self.bounding_rect = bounding_rect
        self.spacing = spacing
        size = self.bounding_rect.b - self.bounding_rect.a
        nx = 1 + math.floor(size.x / spacing)
        ny = 1 + math.floor(size.y / (spacing * HEIGHT))
        self._size = (nx, ny)
        self._points = [
         None] * (nx * ny)
        self._values = [0] * (nx * ny)
        self._min_value = POS_INF
        self._max_value = NEG_INF
        self._edge_ix = {}
        self._edges = []
        for iy in range(ny):
            for ix in range(nx):
                index = ix + iy * nx
                deltas = DELTAS[iy % 2]
                adj = [_delta_to_ix(ix, iy, dx, dy, nx, ny) for dx, dy in deltas]
                for i in range(3):
                    index2 = adj[i]
                    if index2 is None:
                        continue
                    cw = adj[(i + 1) % len(adj)]
                    ccw = adj[(i + len(adj) - 1) % len(adj)]
                    self._edge_ix[(index, index2)] = len(self._edges)
                    self._edge_ix[(index2, index)] = len(self._edges)
                    self._edges.append([index, index2, cw, ccw])

        self._sample_points()

    def isolines(self, value):
        edges = [
         None] * len(self._edges)
        segments = {}
        for a, b, cw, ccw in self._edges:
            pa = self._values[a] <= value
            pb = self._values[b] <= value
            if pa != pb:
                edge1 = self._edge_ix[(a, b)]
                if pa:
                    c, vt, vf = cw, a, b
                else:
                    c, vt, vf = ccw, b, a
                if edges[edge1] is None:
                    pt = _edge_intercept(vt, vf, value, self._values, self._points)
                    edges[edge1] = pt
                if c is not None:
                    pc = self._values[c] <= value
                    v = vf if pc else vt
                    edge2 = self._edge_ix[(v, c)]
                    segments[edge1] = edge2

        pending = {}
        while segments:
            e1, e2 = segments.popitem()
            pending[e1] = (e2, [edges[e1], edges[e2]])

        tails = {}
        lines = []
        while pending:
            e1, (e2, points) = pending.popitem()
            if e1 == e2:
                points.append(points[0])
                lines.append(points)
            elif e2 in pending:
                e3, points2 = pending.pop(e2)
                pending[e1] = (e3, points + points2)
            elif e2 in tails:
                e3, points2 = tails.pop(e2)
                tails[e1] = (e3, points + points2)
            else:
                tails[e1] = (
                 e2, points)

        for _, points in tails.values():
            lines.append(points)

        return lines

    def all_isolines(self, spacing=1.0, max_values=10):
        start, stop = math.ceil(self._min_value + 0.1), math.floor(self._max_value - 0.1)
        if start > stop:
            return []
        num_values = 1 + math.floor((stop - start) / spacing)
        if num_values > max_values:
            spacing = math.ceil((stop - start) / max_values)
            num_values = 1 + math.floor((stop - start) / spacing)
        result = []
        for i in range(num_values):
            value = start + i * spacing
            for isoline in self.isolines(value):
                result.append((value, isoline))

        return result

    def _sample_points(self):
        half_spacing = self.spacing * 0.5
        y_spacing = self.spacing * HEIGHT
        y_offset = self.bounding_rect.a.y
        nx, ny = self._size
        for iy in range(ny):
            y = y_offset + y_spacing * iy
            x_offset = self.bounding_rect.a.x + half_spacing * (iy % 2)
            for ix in range(nx):
                x = x_offset + self.spacing * ix
                point = sims4.math.Vector2(x, y)
                value = self.fn(point)
                index = ix + iy * nx
                self._points[index] = point
                self._values[index] = value
                self._max_value = max(self._max_value, value)
                self._min_value = min(self._min_value, value)
