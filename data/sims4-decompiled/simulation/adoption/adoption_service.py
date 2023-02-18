# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\adoption\adoption_service.py
# Compiled at: 2018-04-28 02:25:47
# Size of source mod 2**32: 11649 bytes

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
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
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
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
jmp_false ::= POP_JUMP_IF_FALSE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
listcomp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
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
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
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
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr BUILD_TUPLE_3 . 
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
   
 L. 131        76  LOAD_CLOSURE             'trait_manager'
                  78  BUILD_TUPLE_1         1 
->                80  LOAD_SETCOMP             '<code_object <setcomp>>'
                  82  LOAD_STR                 'AdoptionService.add_sim_info.<locals>.<setcomp>'
                  84  MAKE_FUNCTION_8          'closure'
                  86  LOAD_DEREF               'sim_info'
                  88  LOAD_ATTR                trait_ids
                  90  GET_ITER         
                  92  CALL_FUNCTION_1       1  '1 positional argument'
                  94  STORE_FAST               'traits'
from _collections import defaultdict
from contextlib import contextmanager
import itertools
from protocolbuffers import GameplaySaveData_pb2
from cas.cas import generate_random_siminfo
from date_and_time import DateAndTime
from distributor.rollback import ProtocolBufferRollback
from distributor.system import Distributor
from sims.pets.breed_tuning import get_random_breed_tag, try_conform_sim_info_to_breed
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims.sim_spawner import SimSpawner, SimCreator
from sims4.service_manager import Service
from sims4.tuning.tunable import TunableSimMinute, TunableList, TunableTuple, Tunable
from sims4.utils import classproperty
from traits.traits import Trait
import persistence_error_types, services, sims4

class AdoptionService(Service):
    PET_ADOPTION_CATALOG_LIFETIME = TunableSimMinute(description='\n        The amount of time in Sim minutes before a pet Sim is removed from the adoption catalog.\n        ',
      default=60,
      minimum=0)
    PET_ADOPTION_GENDER_OPTION_TRAITS = TunableList(description='\n        List of gender option traits from which one will be applied to generated\n        Pets based on the tuned weights.\n        ',
      tunable=TunableTuple(description='\n            A weighted gender option trait that might be applied to the\n            generated Pet.\n            ',
      weight=Tunable(description='\n                The relative weight of this trait.\n                ',
      tunable_type=float,
      default=1),
      trait=Trait.TunableReference(description='\n                A gender option trait that might be applied to the generated\n                Pet.\n                ',
      pack_safe=True)))

    def __init__(self):
        self._sim_infos = defaultdict(list)
        self._real_sim_ids = None
        self._creation_times = {}

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_ADOPTION_SERVICE

    def timeout_real_sim_infos(self):
        sim_now = services.time_service().sim_now
        for sim_id in tuple(self._creation_times.keys()):
            elapsed_time = (sim_now - self._creation_times[sim_id]).in_minutes()
            if elapsed_time > self.PET_ADOPTION_CATALOG_LIFETIME:
                del self._creation_times[sim_id]

    def save(self, save_slot_data=None, **kwargs):
        self.timeout_real_sim_infos()
        adoption_service_proto = GameplaySaveData_pb2.PersistableAdoptionService()
        for sim_id, creation_time in self._creation_times.items():
            with ProtocolBufferRollback(adoption_service_proto.adoptable_sim_data) as (msg):
                msg.adoptable_sim_id = sim_id
                msg.creation_time = creation_time.absolute_ticks()

        save_slot_data.gameplay_data.adoption_service = adoption_service_proto

    def on_all_households_and_sim_infos_loaded(self, _):
        save_slot_data = services.get_persistence_service().get_save_slot_proto_buff()
        sim_info_manager = services.sim_info_manager()
        for sim_data in save_slot_data.gameplay_data.adoption_service.adoptable_sim_data:
            sim_info = sim_info_manager.get(sim_data.adoptable_sim_id)
            if sim_info is None:
                continue
            self._creation_times[sim_data.adoptable_sim_id] = DateAndTime(sim_data.creation_time)

    def stop(self):
        self._sim_infos.clear()
        self._creation_times.clear()

    def add_sim_info--- This code section failed: ---

 L. 120         0  LOAD_FAST                'age'
                2  LOAD_FAST                'gender'
                4  LOAD_FAST                'species'
                6  BUILD_TUPLE_3         3 
                8  STORE_FAST               'key'

 L. 122        10  LOAD_GLOBAL              SimInfoBaseWrapper
               12  LOAD_FAST                'age'
               14  LOAD_FAST                'gender'
               16  LOAD_FAST                'species'
               18  LOAD_CONST               ('age', 'gender', 'species')
               20  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               22  STORE_DEREF              'sim_info'

 L. 124        24  LOAD_GLOBAL              generate_random_siminfo
               26  LOAD_DEREF               'sim_info'
               28  LOAD_ATTR                _base
               30  CALL_FUNCTION_1       1  '1 positional argument'
               32  POP_TOP          

 L. 126        34  LOAD_GLOBAL              get_random_breed_tag
               36  LOAD_FAST                'species'
               38  CALL_FUNCTION_1       1  '1 positional argument'
               40  STORE_FAST               'breed_tag'

 L. 127        42  LOAD_FAST                'breed_tag'
               44  LOAD_CONST               None
               46  COMPARE_OP               is-not
               48  POP_JUMP_IF_FALSE    60  'to 60'

 L. 128        50  LOAD_GLOBAL              try_conform_sim_info_to_breed
               52  LOAD_DEREF               'sim_info'
               54  LOAD_FAST                'breed_tag'
               56  CALL_FUNCTION_2       2  '2 positional arguments'
               58  POP_TOP          
             60_0  COME_FROM            48  '48'

 L. 130        60  LOAD_GLOBAL              services
               62  LOAD_METHOD              get_instance_manager
               64  LOAD_GLOBAL              sims4
               66  LOAD_ATTR                resources
               68  LOAD_ATTR                Types
               70  LOAD_ATTR                TRAIT
               72  CALL_METHOD_1         1  '1 positional argument'
               74  STORE_DEREF              'trait_manager'

 L. 131        76  LOAD_CLOSURE             'trait_manager'
               78  BUILD_TUPLE_1         1 
               80  LOAD_SETCOMP             '<code_object <setcomp>>'
               82  LOAD_STR                 'AdoptionService.add_sim_info.<locals>.<setcomp>'
               84  MAKE_FUNCTION_8          'closure'
               86  LOAD_DEREF               'sim_info'
               88  LOAD_ATTR                trait_ids
               90  GET_ITER         
               92  CALL_FUNCTION_1       1  '1 positional argument'
               94  STORE_FAST               'traits'

 L. 135        96  LOAD_DEREF               'sim_info'
               98  LOAD_ATTR                is_pet
              100  POP_JUMP_IF_FALSE   152  'to 152'

 L. 136       102  LOAD_CLOSURE             'sim_info'
              104  BUILD_TUPLE_1         1 
              106  LOAD_LISTCOMP            '<code_object <listcomp>>'
              108  LOAD_STR                 'AdoptionService.add_sim_info.<locals>.<listcomp>'
              110  MAKE_FUNCTION_8          'closure'
              112  LOAD_FAST                'self'
              114  LOAD_ATTR                PET_ADOPTION_GENDER_OPTION_TRAITS
              116  GET_ITER         
              118  CALL_FUNCTION_1       1  '1 positional argument'
              120  STORE_FAST               'gender_option_traits'

 L. 139       122  LOAD_GLOBAL              sims4
              124  LOAD_ATTR                random
              126  LOAD_METHOD              weighted_random_item
              128  LOAD_FAST                'gender_option_traits'
              130  CALL_METHOD_1         1  '1 positional argument'
              132  STORE_FAST               'selected_trait'

 L. 140       134  LOAD_FAST                'selected_trait'
              136  LOAD_CONST               None
              138  COMPARE_OP               is-not
              140  POP_JUMP_IF_FALSE   152  'to 152'

 L. 141       142  LOAD_FAST                'traits'
              144  LOAD_METHOD              add
              146  LOAD_FAST                'selected_trait'
              148  CALL_METHOD_1         1  '1 positional argument'
              150  POP_TOP          
            152_0  COME_FROM           140  '140'
            152_1  COME_FROM           100  '100'

 L. 143       152  LOAD_DEREF               'sim_info'
              154  LOAD_ATTR                set_trait_ids_on_base
              156  LOAD_GLOBAL              list
              158  LOAD_GENEXPR             '<code_object <genexpr>>'
              160  LOAD_STR                 'AdoptionService.add_sim_info.<locals>.<genexpr>'
              162  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
              164  LOAD_FAST                'traits'
              166  GET_ITER         
              168  CALL_FUNCTION_1       1  '1 positional argument'
              170  CALL_FUNCTION_1       1  '1 positional argument'
              172  LOAD_CONST               ('trait_ids_override',)
              174  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              176  POP_TOP          

 L. 146       178  LOAD_GLOBAL              SimSpawner
              180  LOAD_METHOD              get_random_first_name
              182  LOAD_FAST                'gender'
              184  LOAD_FAST                'species'
              186  CALL_METHOD_2         2  '2 positional arguments'
              188  LOAD_DEREF               'sim_info'
              190  STORE_ATTR               first_name

 L. 149       192  LOAD_GLOBAL              services
              194  LOAD_METHOD              sim_info_manager
              196  CALL_METHOD_0         0  '0 positional arguments'
              198  LOAD_DEREF               'sim_info'
              200  STORE_ATTR               manager

 L. 150       202  LOAD_GLOBAL              Distributor
              204  LOAD_METHOD              instance
              206  CALL_METHOD_0         0  '0 positional arguments'
              208  LOAD_METHOD              add_object
              210  LOAD_DEREF               'sim_info'
              212  CALL_METHOD_1         1  '1 positional argument'
              214  POP_TOP          

 L. 151       216  LOAD_FAST                'self'
              218  LOAD_ATTR                _sim_infos
              220  LOAD_FAST                'key'
              222  BINARY_SUBSCR    
              224  LOAD_METHOD              append
              226  LOAD_DEREF               'sim_info'
              228  CALL_METHOD_1         1  '1 positional argument'
              230  POP_TOP          

Parse error at or near `LOAD_SETCOMP' instruction at offset 80

    def add_real_sim_info(self, sim_info):
        self._creation_times[sim_info.sim_id] = services.time_service().sim_now

    def get_sim_info(self, sim_id):
        for sim_info in itertools.chain.from_iterable(self._sim_infos.values()):
            if sim_info.sim_id == sim_id:
                return sim_info

        for adoptable_sim_id in self._creation_times.keys():
            if sim_id == adoptable_sim_id:
                return services.sim_info_manager().get(adoptable_sim_id)

    @contextmanager
    def real_sim_info_cache(self):
        self.timeout_real_sim_infos()
        self._real_sim_ids = defaultdict(list)
        sim_info_manager = services.sim_info_manager()
        for sim_id in self._creation_times.keys():
            sim_info = sim_info_manager.get(sim_id)
            key = (sim_info.age, sim_info.gender, sim_info.species)
            self._real_sim_ids[key].append(sim_id)

        try:
            yield
        finally:
            self._real_sim_ids.clear()
            self._real_sim_ids = None

    def get_sim_infos(self, interval, age, gender, species):
        key = (
         age, gender, species)
        real_sim_count = len(self._real_sim_ids[key]) if self._real_sim_ids is not None else 0
        entry_count = len(self._sim_infos[key]) + real_sim_count
        if entry_count < interval.lower_bound:
            while entry_count < interval.upper_bound:
                self.add_sim_info(age, gender, species)
                entry_count += 1

        real_sim_infos = []
        if self._real_sim_ids is not None:
            sim_info_manager = services.sim_info_manager()
            for sim_id in tuple(self._real_sim_ids[key]):
                sim_info = sim_info_manager.get(sim_id)
                if sim_info is not None:
                    real_sim_infos.append(sim_info)

        return tuple(itertools.chainself._sim_infos[key]real_sim_infos)

    def remove_sim_info(self, sim_info):
        for sim_infos in self._sim_infos.values():
            if sim_info in sim_infos:
                sim_infos.remove(sim_info)

        if sim_info.sim_id in self._creation_times:
            del self._creation_times[sim_info.sim_id]

    def create_adoption_sim_info(self, sim_info, household=None, account=None, zone_id=None):
        sim_creator = SimCreator(age=(sim_info.age), gender=(sim_info.gender),
          species=(sim_info.extended_species),
          first_name=(sim_info.first_name),
          last_name=(sim_info.last_name))
        sim_info_list, new_household = SimSpawner.create_sim_infos((sim_creator,), household=household,
          account=account,
          zone_id=0,
          creation_source='adoption')
        SimInfoBaseWrapper.copy_physical_attributessim_info_list[0]sim_info
        sim_info_list[0].pelt_layers = sim_info.pelt_layers
        sim_info_list[0].breed_name_key = sim_info.breed_name_key
        sim_info_list[0].load_outfits(sim_info.save_outfits())
        sim_info_list[0].resend_physical_attributes()
        return (
         sim_info_list[0], new_household)

    def convert_base_sim_info_to_full(self, sim_id):
        current_sim_info = self.get_sim_info(sim_id)
        if current_sim_info is None:
            return
        new_sim_info, new_household = self.create_adoption_sim_info(current_sim_info)
        new_household.set_to_hidden()
        self.remove_sim_info(current_sim_info)
        self.add_real_sim_info(new_sim_info)
        return new_sim_info
