# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\apartments\apartment_zone_director.py
# Compiled at: 2018-07-17 18:14:46
# Size of source mod 2**32: 10981 bytes

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
build_slice3 ::= expr . expr expr BUILD_SLICE_3
build_slice3 ::= expr expr . expr BUILD_SLICE_3
build_slice3 ::= expr expr expr . BUILD_SLICE_3
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
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
continues ::= _stmts . lastl_stmt continue
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= list . 
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
ifstmtl ::= testexpr . _ifstmts_jumpl
jmp_false ::= POP_JUMP_IF_FALSE . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
list ::= BUILD_LIST_0 . 
list_comp ::= BUILD_LIST_0 . list_iter
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
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
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
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
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 191        36  LOAD_CLOSURE             'aspiration_manager'
                  38  BUILD_TUPLE_1         1 
->                40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  42  LOAD_STR                 'ApartmentZoneDirectorPlayer._load_custom_zone_director.<locals>.<dictcomp>'
                  44  MAKE_FUNCTION_8          'closure'
from alarms import add_alarm
from date_and_time import create_time_span, DateAndTime
from objects import ALL_HIDDEN_REASONS
from sims4.tuning.tunable import TunableTuple, TunableList, TunableMapping, TunableReference, TunableSimMinute
from situations.service_npcs.modify_lot_items_tuning import ModifyAllLotItems
from situations.situation_guest_list import SituationGuestList
from tunable_time import TunableTimeOfDay
from venues.scheduling_zone_director import SchedulingZoneDirectorMixin
from venues.zone_director_residential import ZoneDirectorResidentialPlayer, ZoneDirectorResidentialNPC
import services, sims4.log
logger = sims4.log.Logger('Apartments', default_owner='rmccord')

class ApartmentZoneDirectorMixin(SchedulingZoneDirectorMixin):
    COMMON_AREA_CLEANUP = TunableTuple(description='\n        Tuning to clear out objects from the common area to prevent trash\n        and what not from accumulating.\n        ',
      actions=ModifyAllLotItems.TunableFactory(description='\n            Modifications to make to objects on the common area of apartments.\n            '),
      time_of_day=TunableTimeOfDay(description='\n            Time of day to run cleanup.\n            ',
      default_hour=4))
    NEW_TENANT_CLEANUP = ModifyAllLotItems.TunableFactory(description='\n        Modifications to make to objects when a new tenant moves in.\n        Example: We want to fix and reset all apartment problems when new\n        tenants move in.\n        ')

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._common_area_cleanup_alarm_handle = None

    @property
    def forward_ungreeted_front_door_interactions_to_terrain(self):
        return False

    def on_startup(self):
        super().on_startup()
        now = services.time_service().sim_now
        time_span = now.time_till_next_day_time(ApartmentZoneDirectorMixin.COMMON_AREA_CLEANUP.time_of_day)
        repeating_time_span = create_time_span(days=1)
        handle = add_alarm(self, time_span, (lambda _: self._run_common_area_cleanup()), repeating=True,
          repeating_time_span=repeating_time_span)
        self._common_area_cleanup_alarm_handle = handle

    def on_shutdown(self):
        self._common_area_cleanup_alarm_handle.cancel()
        self._common_area_cleanup_alarm_handle = None
        super().on_shutdown()

    def on_cleanup_zone_objects(self):
        super().on_cleanup_zone_objects()
        persistence_service = services.get_persistence_service()
        plex_service = services.get_plex_service()
        plex_zone_ids = plex_service.get_plex_zones_in_group(services.current_zone_id())
        last_save_ticks = None
        for zone_id in plex_zone_ids:
            zone_data = persistence_service.get_zone_proto_buff(zone_id)
            gameplay_zone_data = zone_data.gameplay_zone_data
            if not gameplay_zone_data.HasField('game_time'):
                continue
            if last_save_ticks is None or last_save_ticks < gameplay_zone_data.game_time:
                last_save_ticks = gameplay_zone_data.game_time

        if last_save_ticks is not None:
            last_save_time = DateAndTime(last_save_ticks)
            next_cleanup_time = last_save_time.time_of_next_day_time(ApartmentZoneDirectorMixin.COMMON_AREA_CLEANUP.time_of_day)
            if next_cleanup_time < services.time_service().sim_now:
                self._run_common_area_cleanup()
        owning_household = services.owning_household_of_active_lot()
        if owning_household is not None:
            if not owning_household.has_home_zone_been_active():
                self._run_new_tenant_cleanup()

    def _run_new_tenant_cleanup(self):
        actions = ApartmentZoneDirectorMixin.NEW_TENANT_CLEANUP()
        actions.modify_objects()

    def _run_common_area_cleanup(self):
        actions = ApartmentZoneDirectorMixin.COMMON_AREA_CLEANUP.actions()
        plex_service = services.get_plex_service()

        def object_criteria(obj):
            return plex_service.get_plex_zone_at_position(obj.position, obj.level) is None

        actions.modify_objects(object_criteria=object_criteria)


ASPIRATION_TIMEOUTS = 'aspiration_timeouts'

class ApartmentZoneDirectorPlayer(ApartmentZoneDirectorMixin, ZoneDirectorResidentialPlayer):
    INSTANCE_TUNABLES = {'neighbor_reaction_events': TunableMapping(description='\n            A map of different neighbor reaction event listeners that we want\n            to keep active on the Sims while this zone director is running and\n            the situations to create when those event listeners are completed.\n            ',
                                   key_type=TunableReference(description='\n                The aspiration that we will register on all of the active\n                household Sims that when completed will then trigger the\n                appropriate situation.\n                ',
                                   manager=(services.get_instance_manager(sims4.resources.Types.ASPIRATION)),
                                   class_restrictions='ZoneDirectorEventListener'),
                                   value_type=TunableTuple(description='\n                Extra data for this specific aspiration.\n                ',
                                   timeout=TunableSimMinute(description='\n                    The amount of time in Sim Minutes that will pass from the\n                    completion of the aspiration before we will start the\n                    situation again.\n                    ',
                                   minimum=0,
                                   default=60),
                                   situation=TunableReference(description='\n                    The Situation that we want to start on the completion of\n                    this aspiration.\n                    ',
                                   manager=(services.get_instance_manager(sims4.resources.Types.SITUATION)))))}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._aspiration_timeouts = {}

    def _save_custom_zone_director(self, zone_director_proto, writer):
        aspiration_timeouts = []
        for aspiration, timeout in self._aspiration_timeouts.items():
            aspiration_timeouts.append(aspiration.guid64)
            aspiration_timeouts.append(timeout.absolute_ticks())

        writer.write_uint64s(ASPIRATION_TIMEOUTS, aspiration_timeouts)
        super()._save_custom_zone_director(zone_director_proto, writer)

    def _load_custom_zone_director--- This code section failed: ---

 L. 188         0  LOAD_FAST                'reader'
                2  LOAD_CONST               None
                4  COMPARE_OP               is-not
                6  POP_JUMP_IF_FALSE    82  'to 82'

 L. 189         8  LOAD_FAST                'reader'
               10  LOAD_METHOD              read_uint64s
               12  LOAD_GLOBAL              ASPIRATION_TIMEOUTS
               14  BUILD_LIST_0          0 
               16  CALL_METHOD_2         2  '2 positional arguments'
               18  STORE_FAST               'aspiration_timeouts'

 L. 190        20  LOAD_GLOBAL              services
               22  LOAD_METHOD              get_instance_manager
               24  LOAD_GLOBAL              sims4
               26  LOAD_ATTR                resources
               28  LOAD_ATTR                Types
               30  LOAD_ATTR                ASPIRATION
               32  CALL_METHOD_1         1  '1 positional argument'
               34  STORE_DEREF              'aspiration_manager'

 L. 191        36  LOAD_CLOSURE             'aspiration_manager'
               38  BUILD_TUPLE_1         1 
               40  LOAD_DICTCOMP            '<code_object <dictcomp>>'
               42  LOAD_STR                 'ApartmentZoneDirectorPlayer._load_custom_zone_director.<locals>.<dictcomp>'
               44  MAKE_FUNCTION_8          'closure'

 L. 192        46  LOAD_GLOBAL              zip
               48  LOAD_FAST                'aspiration_timeouts'
               50  LOAD_CONST               None
               52  LOAD_CONST               None
               54  LOAD_CONST               2
               56  BUILD_SLICE_3         3 
               58  BINARY_SUBSCR    

 L. 193        60  LOAD_FAST                'aspiration_timeouts'
               62  LOAD_CONST               1
               64  LOAD_CONST               None
               66  LOAD_CONST               2
               68  BUILD_SLICE_3         3 
               70  BINARY_SUBSCR    
               72  CALL_FUNCTION_2       2  '2 positional arguments'
               74  GET_ITER         
               76  CALL_FUNCTION_1       1  '1 positional argument'
               78  LOAD_FAST                'self'
               80  STORE_ATTR               _aspiration_timeouts
             82_0  COME_FROM             6  '6'

 L. 194        82  LOAD_GLOBAL              super
               84  CALL_FUNCTION_0       0  '0 positional arguments'
               86  LOAD_METHOD              _load_custom_zone_director
               88  LOAD_FAST                'zone_director_proto'
               90  LOAD_FAST                'reader'
               92  CALL_METHOD_2         2  '2 positional arguments'
               94  POP_TOP          

Parse error at or near `LOAD_DICTCOMP' instruction at offset 40

    def on_sim_added_to_skewer(self, sim_info):
        self._register_zone_aspriations_for_sim(sim_info)

    def on_spawn_sim_for_zone_spin_up_completed(self):
        for sim_info in services.active_household():
            self._register_zone_aspriations_for_sim(sim_info)

    def _register_zone_aspriations_for_sim(self, sim_info):
        sim = sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
        if sim is None:
            return
        for aspiration in self.neighbor_reaction_events.keys():
            sim_info.aspiration_tracker.reset_milestone(aspiration)
            aspiration.register_callbacks()
            sim_info.aspiration_tracker.process_test_events_for_aspiration(aspiration)

    def on_zone_director_aspiration_completed(self, completed_aspiration, sim_info):
        sim_info.aspiration_tracker.reset_milestone(completed_aspiration)
        now = services.time_service().sim_now
        if completed_aspiration in self._aspiration_timeouts:
            if now < self._aspiration_timeouts[completed_aspiration]:
                return
        aspiration_data = self.neighbor_reaction_events[completed_aspiration]
        self._aspiration_timeouts[completed_aspiration] = now + create_time_span(minutes=(aspiration_data.timeout))
        guest_list = aspiration_data.situation.get_predefined_guest_list()
        if guest_list is None:
            guest_list = SituationGuestList(invite_only=True)
        services.get_zone_situation_manager().create_situation((aspiration_data.situation), guest_list=guest_list,
          user_facing=False,
          creation_source=(self.instance_name))


class ApartmentZoneDirectorNPC(ApartmentZoneDirectorMixin, ZoneDirectorResidentialNPC):
    pass
