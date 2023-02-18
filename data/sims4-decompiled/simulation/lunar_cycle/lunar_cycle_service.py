# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lunar_cycle\lunar_cycle_service.py
# Compiled at: 2022-04-13 00:26:10
# Size of source mod 2**32: 30122 bytes

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
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_stmt ::= expr . POP_TOP
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
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= if_exp . 
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
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
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
if_exp_true ::= expr JUMP_FORWARD . expr COME_FROM
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
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
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
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= expr . STORE_ATTR
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
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 596        34  LOAD_CLOSURE             'test'
                  36  LOAD_CLOSURE             'today'
                  38  BUILD_TUPLE_2         2 
->                40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  42  LOAD_STR                 'LunarCycleService._trim_current_forecasts.<locals>.<dictcomp>'
                  44  MAKE_FUNCTION_8          'closure'
                  46  LOAD_FAST                'self'
                  48  LOAD_ATTR                _forecasts
                  50  LOAD_METHOD              items
                  52  CALL_METHOD_0         0  '0 positional arguments'
                  54  GET_ITER         
                  56  CALL_FUNCTION_1       1  '1 positional argument'
                  58  LOAD_FAST                'self'
import functools, operator
from _weakrefset import WeakSet
from math import floor
from protocolbuffers import GameplaySaveData_pb2
import game_services, persistence_error_types, services, sims4.log
from alarms import AlarmHandle
from date_and_time import create_date_and_time, DateAndTime, create_time_span, TimeSpan, sim_ticks_per_day
from distributor.system import Distributor
from lunar_cycle.lunar_cycle_enums import LunarPhaseType, LunarCycleLengthOption, LunarPhaseLockedOption
from lunar_cycle.lunar_cycle_ops import MoonPhaseUpdateOp, LunarEffectTooltipUpdateOp, MoonForecastUpdateOp
from lunar_cycle.lunar_cycle_tuning import LunarCycleTuning
from objects import ALL_HIDDEN_REASONS_EXCEPT_UNINITIALIZED
from scheduling import Timeline
from sims4.callback_utils import CallableList
from sims4.service_manager import Service
from sims4.utils import classproperty
logger = sims4.log.Logger('LunarCycleService', default_owner='jdimailig')

def phase_change_time_for_day(absolute_days):
    return create_date_and_time(days=(floor(absolute_days)), hours=(LunarCycleTuning.PHASE_CHANGE_TIME_OF_DAY))


class LunarCycleService(Service):

    def __init__(self, *_, **__):
        self._current_phase = None
        self._current_phase_tuning = None
        self._start_of_phase = None
        self._cycle_length_selected = None
        self._lunar_effects_disabled = None
        self._phase_lock = None
        self._lunar_cycle_timeline = None
        self._daily_phase_check_handler = None
        self._region_supports_lunar_cycle = False
        self._active_effects = {}
        self._effect_alarms = {}
        self._lunar_phase_aware_objects = WeakSet()
        self._forecasts = {}

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_LUNAR_CYCLE_SERVICE

    def setup(self, save_slot_data=None, **__):
        if save_slot_data.gameplay_data.HasField('lunar_cycle_service'):
            persisted_lunar_cycle_service = save_slot_data.gameplay_data.lunar_cycle_service
            self._set_current_phase_and_start_time(persisted_lunar_cycle_service.current_phase, persisted_lunar_cycle_service.phase_start_time)

    def save(self, save_slot_data=None, **__):
        if self._current_phase is None:
            return
        lunar_cycle_proto = GameplaySaveData_pb2.PersistableLunarCycleService()
        lunar_cycle_proto.current_phase = self._current_phase.value
        lunar_cycle_proto.phase_start_time = self._start_of_phase
        save_slot_data.gameplay_data.lunar_cycle_service = lunar_cycle_proto

    def load_options(self, options_proto):
        self._cycle_length_selected = LunarCycleLengthOption(options_proto.lunar_cycle_length)
        self._lunar_effects_disabled = options_proto.disable_lunar_effects
        self._phase_lock = LunarPhaseLockedOption(options_proto.lunar_phase_lock)

    def save_options(self, options_proto):
        options_proto.lunar_cycle_length = self._cycle_length_selected.value
        options_proto.disable_lunar_effects = self._lunar_effects_disabled
        options_proto.lunar_phase_lock = self._phase_lock.value

    def on_zone_load(self):
        self._set_region_lunar_cycle_supported()
        sim_now = services.time_service().sim_now
        today_in_absolute_days = sim_now.absolute_days()
        if self._current_phase is None:
            phase_start = phase_change_time_for_day(today_in_absolute_days)
            self._set_initial_phase(phase_start)
        if self._lunar_cycle_timeline is None:
            self._lunar_cycle_timeline = Timeline(sim_now)
        if self._daily_phase_check_handler is None:
            one_day = TimeSpan(sim_ticks_per_day())
            next_alarm_time = phase_change_time_for_day(today_in_absolute_days)
            if sim_now.hour() >= LunarCycleTuning.PHASE_CHANGE_TIME_OF_DAY:
                next_alarm_time = next_alarm_time + one_day
            self._daily_phase_check_handler = AlarmHandle(self, (self._on_daily_phase_check),
              (self._lunar_cycle_timeline),
              next_alarm_time,
              repeating=True,
              repeat_interval=one_day,
              cross_zone=True)
        self._distribute_to_client()
        if not game_services.service_manager.is_traveling:
            self._lunar_effect_setup()

    def on_teardown(self):
        self._lunar_phase_aware_objects.clear()

    def update(self):
        now = services.time_service().sim_now
        if self._lunar_cycle_timeline is None:
            self._lunar_cycle_timeline = Timeline(now)
        self._lunar_cycle_timeline.simulate(now)

    @property
    def current_phase(self):
        return self._current_phase

    @property
    def current_phase_start(self):
        return self._start_of_phase

    @property
    def lunar_effects_disabled(self):
        return self._lunar_effects_disabled

    def set_cycle_length(self, cycle_length):
        self._cycle_length_selected = cycle_length
        self._cancel_scheduled_effects()
        self._trim_current_forecasts()
        self._lunar_effect_setup(setup_callback=(self._schedule_upcoming_effects))

    def set_lunar_effects_disabled(self, disable_effects):
        self._lunar_effects_disabled = disable_effects
        self._active_effects.clear()
        if disable_effects:
            self._cancel_scheduled_effects()
        else:
            self._lunar_effect_setup()
            self._apply_immediate_effects()

    def set_locked_phase(self, locked_phase_type):
        self._phase_lock = locked_phase_type
        self._cancel_scheduled_effects()
        self._trim_current_forecasts()
        self._lunar_effect_setup(setup_callback=(self._schedule_upcoming_effects))

    def get_phase_length(self, phase_type):
        return LunarCycleTuning.LUNAR_PHASE_MAP[phase_type].get_phase_length(self._cycle_length_selected)

    def set_phase(self, phase_type):
        if phase_type == self._current_phase:
            return
        phase_start_time = phase_change_time_for_day(self._lunar_cycle_timeline.now.absolute_days())
        self._set_current_phase_and_start_time(phase_type, phase_start_time)
        self._cancel_scheduled_effects()
        self._trim_current_forecasts()
        self._distribute_to_client()
        self._active_effects.clear()
        self._lunar_effect_setup()
        self._apply_immediate_effects()
        self._update_lunar_phase_aware_objects()

    def apply_active_lunar_effects_to_sim(self, sim_info):
        if not self._lunar_effects_disabled:
            return self._region_supports_lunar_cycle or None
        else:
            lunar_effect_tracker = sim_info.lunar_effect_tracker
            if lunar_effect_tracker is None:
                return
            lunar_effect_tracker.prune_stale_effects(services.time_service().sim_now)
            return self._active_effects or None
        for active_effect, start_time in self._active_effects.items():
            active_effect.apply_lunar_effect(lunar_effect_tracker, start_time)

    def register_lunar_phase_aware_object(self, lunar_phase_aware_component):
        self._lunar_phase_aware_objects.add(lunar_phase_aware_component.owner)
        lunar_phase_aware_component.on_lunar_phase_set(self._current_phase)

    def deregister_lunar_phase_aware_object(self, lunar_phase_aware_component):
        self._lunar_phase_aware_objects.discard(lunar_phase_aware_component.owner)

    def send_lunar_effects_tooltip_data(self, sim_info):
        lunar_effect_tooltip_update_op = LunarEffectTooltipUpdateOp(self._current_phase)

        def send_lunar_effect_tooltip_data():
            Distributor.instance().send_op_with_no_owner_immediate(lunar_effect_tooltip_update_op)

        if sim_info is None:
            send_lunar_effect_tooltip_data()
            return
        lunar_effect_tracker = sim_info.lunar_effect_tracker
        if lunar_effect_tracker is None:
            send_lunar_effect_tooltip_data()
            return
        tooltip = lunar_effect_tracker.find_active_effect_tooltip()
        if tooltip is not None:
            lunar_effect_tooltip_update_op.set_tooltip(tooltip)
        send_lunar_effect_tooltip_data()

    def _set_initial_phase(self, phase_start):
        self._set_current_phase_and_start_time(LunarCycleTuning.INITIAL_LUNAR_PHASE, phase_start)

    def _set_current_phase_and_start_time(self, phase_type, start_time):
        self._current_phase = LunarPhaseType(phase_type)
        self._start_of_phase = DateAndTime(start_time)
        self._current_phase_tuning = LunarCycleTuning.LUNAR_PHASE_MAP[self._current_phase]

    def _on_daily_phase_check(self, handle):
        phase_length = self._current_phase_tuning.get_phase_length(self._cycle_length_selected)
        end_of_phase = self._start_of_phase + phase_length
        timeline_now = handle.timeline.now
        require_phase_change = self._will_phase_change_occur(self._current_phase, end_of_phase, timeline_now)
        absolute_days = timeline_now.absolute_days()
        self._trim_current_forecasts(keep_today_only=False)
        if require_phase_change:
            next_phase = self._determine_next_phase(self._current_phase)
            next_phase_start_time = phase_change_time_for_day(absolute_days)
            self._set_current_phase_and_start_time(next_phase, next_phase_start_time)
            self._distribute_to_client()
            self._update_lunar_phase_aware_objects()
        self._lunar_effect_setup()
        self._apply_immediate_effects()

    def _will_phase_change_occur(self, phase_type, end_of_phase, test_time):
        lunar_cycle_locked = self._phase_lock != LunarPhaseLockedOption.NO_LUNAR_PHASE_LOCK
        if lunar_cycle_locked:
            return self._phase_lock != phase_type
        return test_time >= end_of_phase

    def _set_region_lunar_cycle_supported(self):
        region = services.current_region()
        self._region_supports_lunar_cycle = False if region is None else region.supports_lunar_cycle

    def _lunar_effect_setup(self, setup_callback=None):
        if self._lunar_effects_disabled:
            return
        else:
            if setup_callback is None:
                setup_callback = CallableList((self._track_effects_if_active, self._schedule_upcoming_effects))
            sim_now = services.time_service().sim_now
            today_in_absolute_days = sim_now.absolute_days()
            if sim_now.hour() < LunarCycleTuning.PHASE_CHANGE_TIME_OF_DAY:
                today_in_absolute_days -= 1
                if today_in_absolute_days < 0:
                    return
        todays_phase_start_time = phase_change_time_for_day(today_in_absolute_days)
        for effects_by_hour_offset in self._todays_effects_gen(todays_phase_start_time):
            for hour_offset, lunar_effect_list in effects_by_hour_offset.items():
                effect_start_time = todays_phase_start_time + create_time_span(hours=hour_offset)
                setup_callback(effect_start_time, lunar_effect_list, sim_now)

    def _todays_effects_gen(self, todays_phase_start_time):
        effects_by_hour_offset = self._current_phase_tuning.effects_by_hour_offset
        yield effects_by_hour_offset
        if self._current_phase == self._phase_lock:
            return
        phase_length = self._current_phase_tuning.get_phase_length(self._cycle_length_selected)
        end_of_phase = self._start_of_phase + phase_length
        if todays_phase_start_time + TimeSpan(sim_ticks_per_day()) <= end_of_phase:
            next_phase = self._determine_next_phase(self._current_phase)
            next_phase_tuning = LunarCycleTuning.LUNAR_PHASE_MAP[next_phase]
            pre_phase_effects_by_hour_offset = next_phase_tuning.pre_phase_effects_by_hour_offset
            yield pre_phase_effects_by_hour_offset

    def _track_effects_if_active(self, effect_start_time, lunar_effect_list, sim_now):
        if sim_now < effect_start_time:
            return
        for lunar_effect in lunar_effect_list:
            if not lunar_effect.is_tracked_effect:
                continue
            effect_end_time = effect_start_time + create_time_span(minutes=(lunar_effect.effect_duration))
            if effect_end_time <= sim_now:
                continue
            self._active_effects[lunar_effect] = effect_start_time

    def _apply_immediate_effects(self):
        for sim in services.sim_info_manager().instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS_EXCEPT_UNINITIALIZED):
            self.apply_active_lunar_effects_to_sim(sim.sim_info)

    def _schedule_upcoming_effects(self, effect_start_time, lunar_effect_list, sim_now):
        if effect_start_time < sim_now:
            return
        alarm_key = (effect_start_time, lunar_effect_list)
        if alarm_key in self._effect_alarms:
            return
        alarm_callback = functools.partial(self._on_effect_handler_alarm, effect_start_time, lunar_effect_list)
        alarm_key = (effect_start_time, lunar_effect_list)
        self._effect_alarms[alarm_key] = AlarmHandle(self, alarm_callback, (self._lunar_cycle_timeline), effect_start_time,
          cross_zone=True)

    def _on_effect_handler_alarm(self, effect_start_time, lunar_effect_list, _alarm_handle):
        if self._lunar_effects_disabled:
            return
        sim_now = services.time_service().sim_now
        for lunar_effect, start_time in tuple(self._active_effects.items()):
            if start_time + create_time_span(minutes=(lunar_effect.effect_duration)) <= sim_now:
                del self._active_effects[lunar_effect]

        alarm_key = (
         effect_start_time, lunar_effect_list)
        if alarm_key in self._effect_alarms:
            del self._effect_alarms[alarm_key]
        if self._region_supports_lunar_cycle:
            for sim in services.sim_info_manager().instanced_sims_gen(allow_hidden_flags=ALL_HIDDEN_REASONS_EXCEPT_UNINITIALIZED):
                lunar_effect_tracker = sim.sim_info.lunar_effect_tracker
                if lunar_effect_tracker is None:
                    continue
                lunar_effect_tracker.prune_stale_effects(sim_now)
                for lunar_effect in lunar_effect_list:
                    lunar_effect.apply_lunar_effect(lunar_effect_tracker, effect_start_time)

        for lunar_effect in lunar_effect_list:
            if lunar_effect.is_tracked_effect:
                self._active_effects[lunar_effect] = effect_start_time

    def _cancel_scheduled_effects(self):
        for alarm_key, effect_alarm in tuple(self._effect_alarms.items()):
            effect_alarm.cancel()
            del self._effect_alarms[alarm_key]

    def _distribute_to_client(self):
        skip_environment_changes = not self._region_supports_lunar_cycle
        op = MoonPhaseUpdateOp(self._current_phase, skip_environment_changes)
        Distributor.instance().add_op_with_no_owner(op)

    def _update_lunar_phase_aware_objects(self):
        for lunar_phase_aware_object in tuple(self._lunar_phase_aware_objects):
            lunar_phase_aware_object.on_lunar_phase_set(self._current_phase)

    def _determine_next_phase(self, phase):
        if self._phase_lock != LunarPhaseLockedOption.NO_LUNAR_PHASE_LOCK:
            return LunarPhaseType(self._phase_lock)

        def next_phase_type(p):
            return LunarPhaseType((p.value + 1) % len(LunarPhaseType))

        next_phase = next_phase_type(phase)
        phase_type_to_tuning = LunarCycleTuning.LUNAR_PHASE_MAP
        while phase_type_to_tuning[next_phase].get_phase_length(self._cycle_length_selected) <= TimeSpan.ZERO:
            next_phase = next_phase_type(next_phase)

        return next_phase

    def _set_initial_forecasts(self, today_in_absolute_days):
        today = int(today_in_absolute_days)
        self._forecasts = {}
        phase_end_time = self._start_of_phase + self._current_phase_tuning.get_phase_length(self._cycle_length_selected)
        if not self._will_phase_change_occur(self._current_phase, phase_end_time, phase_change_time_for_day(today_in_absolute_days)):
            self._forecasts[today] = self._current_phase
        else:
            self._forecasts[today] = self._determine_next_phase(self._current_phase)

    def _trim_current_forecasts--- This code section failed: ---

 L. 593         0  LOAD_GLOBAL              int
                2  LOAD_GLOBAL              services
                4  LOAD_METHOD              time_service
                6  CALL_METHOD_0         0  '0 positional arguments'
                8  LOAD_ATTR                sim_now
               10  LOAD_METHOD              absolute_days
               12  CALL_METHOD_0         0  '0 positional arguments'
               14  CALL_FUNCTION_1       1  '1 positional argument'
               16  STORE_DEREF              'today'

 L. 594        18  LOAD_FAST                'keep_today_only'
               20  POP_JUMP_IF_FALSE    28  'to 28'
               22  LOAD_GLOBAL              operator
               24  LOAD_ATTR                eq
               26  JUMP_FORWARD         32  'to 32'
             28_0  COME_FROM            20  '20'
               28  LOAD_GLOBAL              operator
               30  LOAD_ATTR                ge
             32_0  COME_FROM            26  '26'
               32  STORE_DEREF              'test'

 L. 596        34  LOAD_CLOSURE             'test'
               36  LOAD_CLOSURE             'today'
               38  BUILD_TUPLE_2         2 
               40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               42  LOAD_STR                 'LunarCycleService._trim_current_forecasts.<locals>.<dictcomp>'
               44  MAKE_FUNCTION_8          'closure'
               46  LOAD_FAST                'self'
               48  LOAD_ATTR                _forecasts
               50  LOAD_METHOD              items
               52  CALL_METHOD_0         0  '0 positional arguments'
               54  GET_ITER         
               56  CALL_FUNCTION_1       1  '1 positional argument'
               58  LOAD_FAST                'self'
               60  STORE_ATTR               _forecasts

Parse error at or near `LOAD_DICTCOMP' instruction at offset 40

    def populate_forecasts(self, num_days):
        sim_now = services.time_service().sim_now
        today = int(sim_now.absolute_days())
        if self._forecasts:
            self._trim_current_forecasts(keep_today_only=False)
        else:
            self._set_initial_forecasts(today)
        existing_forecasts = self._forecasts
        num_days = num_days - len(existing_forecasts)
        if self._phase_lock != LunarPhaseLockedOption.NO_LUNAR_PHASE_LOCK:
            if num_days > 0:
                for i in range(num_days):
                    existing_forecasts[today + i] = LunarPhaseType(self._phase_lock)

                num_days = 0
        if num_days > 0:
            one_day = TimeSpan(sim_ticks_per_day())
            last_phase_type = phase_type = self._forecasts[today]
            forecast_day = today
            forecasted_time = phase_change_time_for_day(forecast_day)
            phase_start = self._start_of_phase
            for phase_type in self._forecasts.values():
                if phase_type != last_phase_type:
                    phase_start = forecasted_time
                    last_phase_type = phase_type
                forecasted_time += one_day
                forecast_day += 1

            while num_days > 0:
                phase_tuning = LunarCycleTuning.LUNAR_PHASE_MAP[phase_type]
                phase_length = phase_tuning.get_phase_length(self._cycle_length_selected)
                end_of_phase = phase_start + phase_length
                if self._will_phase_change_occur(phase_type, end_of_phase, forecasted_time):
                    phase_type = self._determine_next_phase(phase_type)
                    phase_start = forecasted_time
                existing_forecasts[forecast_day] = phase_type
                forecasted_time += one_day
                forecast_day += 1
                num_days -= 1

        self._send_ui_lunar_forecast()

    def _send_ui_lunar_forecast(self):
        op = MoonForecastUpdateOp(self._forecasts.values())
        Distributor.instance().add_op_with_no_owner(op)
