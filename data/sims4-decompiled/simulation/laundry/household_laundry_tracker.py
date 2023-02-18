# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\laundry\household_laundry_tracker.py
# Compiled at: 2019-01-22 20:35:45
# Size of source mod 2**32: 7117 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
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
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
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
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
subscript ::= expr . expr BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  51        18  LOAD_CLOSURE             'now'
                  20  LOAD_CLOSURE             'timeout'
                  22  BUILD_TUPLE_2         2 
->                24  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  26  LOAD_STR                 'HouseholdLaundryTracker._update_finished_laundry_conditions.<locals>.<dictcomp>'
                  28  MAKE_FUNCTION_8          'closure'
                  30  LOAD_FAST                'self'
                  32  LOAD_ATTR                _finished_laundry_conditions
                  34  LOAD_METHOD              items
                  36  CALL_METHOD_0         0  '0 positional arguments'
                  38  GET_ITER         
                  40  CALL_FUNCTION_1       1  '1 positional argument'
                  42  LOAD_FAST                'self'
import random
from date_and_time import DateAndTime
from distributor.rollback import ProtocolBufferRollback
from event_testing.resolver import SingleSimResolver
from households.household_tracker import HouseholdTracker
from laundry.laundry_tuning import LaundryTuning
import services, sims4
logger = sims4.log.Logger('Laundry', default_owner='mkartika')

class HouseholdLaundryTracker(HouseholdTracker):

    def __init__(self, household):
        self._owner = household
        self._last_unload_laundry_time = None
        self._finished_laundry_conditions = {}

    @property
    def owner(self):
        return self._owner

    @property
    def last_unload_laundry_time(self):
        return self._last_unload_laundry_time

    @property
    def finished_laundry_conditions(self):
        return self._finished_laundry_conditions

    def _update_finished_laundry_conditions--- This code section failed: ---

 L.  49         0  LOAD_GLOBAL              LaundryTuning
                2  LOAD_ATTR                PUT_AWAY_FINISHED_LAUNDRY
                4  LOAD_ATTR                laundry_condition_timeout
                6  STORE_DEREF              'timeout'

 L.  50         8  LOAD_GLOBAL              services
               10  LOAD_METHOD              time_service
               12  CALL_METHOD_0         0  '0 positional arguments'
               14  LOAD_ATTR                sim_now
               16  STORE_DEREF              'now'

 L.  51        18  LOAD_CLOSURE             'now'
               20  LOAD_CLOSURE             'timeout'
               22  BUILD_TUPLE_2         2 
               24  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               26  LOAD_STR                 'HouseholdLaundryTracker._update_finished_laundry_conditions.<locals>.<dictcomp>'
               28  MAKE_FUNCTION_8          'closure'
               30  LOAD_FAST                'self'
               32  LOAD_ATTR                _finished_laundry_conditions
               34  LOAD_METHOD              items
               36  CALL_METHOD_0         0  '0 positional arguments'
               38  GET_ITER         
               40  CALL_FUNCTION_1       1  '1 positional argument'
               42  LOAD_FAST                'self'
               44  STORE_ATTR               _finished_laundry_conditions

Parse error at or near `LOAD_DICTCOMP' instruction at offset 24

    def _apply_laundry_rewards(self, sim):
        self._update_finished_laundry_conditions
        if self._finished_laundry_conditions:
            chosen_condition = random.choice(list(self._finished_laundry_conditions.values))
            loot_reward = LaundryTuning.PUT_AWAY_FINISHED_LAUNDRY.conditions_and_rewards_map[chosen_condition[1]]
            resolver = SingleSimResolver(sim.sim_info)
            loot_reward.apply_to_resolver(resolver)

    def apply_laundry_effect(self, sim):
        if self._last_unload_laundry_time is None:
            return
        else:
            elapsed_time = (services.time_service.sim_now - self._last_unload_laundry_time).in_minutes
            if elapsed_time >= LaundryTuning.NOT_DOING_LAUNDRY_PUNISHMENT.timeout:
                resolver = SingleSimResolver(sim.sim_info)
                LaundryTuning.NOT_DOING_LAUNDRY_PUNISHMENT.loot_to_apply.apply_to_resolver(resolver)
                self._finished_laundry_conditions.clear
            else:
                self._apply_laundry_rewards(sim)

    def update_last_unload_laundry_time(self):
        self._last_unload_laundry_time = services.time_service.sim_now

    def update_finished_laundry_condition(self, resolver):
        target = resolver.interaction.target
        if target is None:
            logger.error('Failed to update finished laundry condition from interaction {} because the target is None.', resolver.interaction)
        sim_now = services.time_service.sim_now
        condition_states = LaundryTuning.PUT_AWAY_FINISHED_LAUNDRY.laundry_condition_states.condition_states
        excluded_states = LaundryTuning.PUT_AWAY_FINISHED_LAUNDRY.laundry_condition_states.excluded_states
        for state_type in condition_states:
            val = target.get_state(state_type)
            if val in excluded_states:
                self._finished_laundry_conditions.pop(val.state, None)
            else:
                self._finished_laundry_conditions[val.state] = (
                 sim_now, val)

    def reset(self):
        self._last_unload_laundry_time = None
        self._finished_laundry_conditions.clear

    def household_lod_cleanup(self):
        self.reset

    def save_data(self, household_msg):
        if self._last_unload_laundry_time is None:
            if household_msg.laundry_data.laundry_conditions:
                logger.error("Household {} has Laundry Conditions {} while Last Unload Laundry is None. Bad tracker data, Laundry Conditions won't be saved.", self.owner, self._finished_laundry_conditions)
            return
        household_msg.laundry_data.last_unload_time = self._last_unload_laundry_time.absolute_ticks
        for timestamp, state_value in self._finished_laundry_conditions.values:
            with ProtocolBufferRollback(household_msg.laundry_data.laundry_conditions) as (msg):
                msg.timestamp = timestamp.absolute_ticks
                msg.state_value_name_hash = state_value.guid64

    def load_data(self, household_proto):
        if household_proto.laundry_data.last_unload_time == 0:
            if household_proto.laundry_data.laundry_conditions:
                logger.error("Household {} has Laundry Conditions {} while Last Unload Laundry is None. Laundry Conditions won't be loaded.", self.owner, household_proto.laundry_data.laundry_conditions)
            return
        self._last_unload_laundry_time = DateAndTime(household_proto.laundry_data.last_unload_time)
        object_state_manager = services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)
        for laundry_condition in household_proto.laundry_data.laundry_conditions:
            timestamp = DateAndTime(laundry_condition.timestamp)
            state_value = object_state_manager.get(laundry_condition.state_value_name_hash)
            if state_value is None:
                logger.warn('Failed to load an invalid laundry object state value {} on household {}.', laundry_condition.state_value_name_hash, self.owner)
                continue
            self._finished_laundry_conditions[state_value.state] = (
             timestamp, state_value)
