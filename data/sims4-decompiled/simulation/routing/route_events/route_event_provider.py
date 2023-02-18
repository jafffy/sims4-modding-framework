# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\route_events\route_event_provider.py
# Compiled at: 2020-11-18 22:32:44
# Size of source mod 2**32: 8541 bytes

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
and ::= expr JUMP_IF_FALSE_OR_POP . expr \e_come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP . expr come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr . come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr \e_come_from_opt . 
and ::= expr JUMP_IF_FALSE_OR_POP expr come_from_opt . 
and ::= expr jifop_come_from . expr
and ::= expr jifop_come_from expr . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
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
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_6
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_stmt ::= expr . POP_TOP
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
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= and . 
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
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
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
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jifop_come_from ::= JUMP_IF_FALSE_OR_POP . come_froms
jifop_come_from ::= JUMP_IF_FALSE_OR_POP come_froms . 
jmp_true ::= POP_JUMP_IF_TRUE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP . return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond . COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM . 
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_expr ::= expr . 
return_expr ::= ret_and . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testtrue . 
testfalse ::= expr . jmp_false
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= and jmp_true . come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  68        24  LOAD_FAST                'route_event_cls'
                  26  LOAD_METHOD              test
                  28  LOAD_FAST                'sim_resolver'
                  30  CALL_METHOD_1         1  '1 positional argument'
                32_0  COME_FROM            22  '22'
->              32_1  COME_FROM             6  '6'
                  32  RETURN_VALUE     
from element_utils import build_critical_section_with_finally
from elements import ParentElement
from event_testing.resolver import SingleObjectResolver, SingleSimResolver
from interactions import ParticipantType
from routing.route_enums import RouteEventType
from routing.route_events.route_event import RouteEvent
from sims4.tuning.tunable import AutoFactoryInit, HasTunableFactory, TunableList, TunableTuple, TunableEnumEntry
import sims4.log
logger = sims4.log.Logger('RouteEventProviders', default_owner='rmccord')

class RouteEventProviderMixin:

    def on_event_executed(self, route_event, sim):
        pass

    def provide_route_events(self, route_event_context, sim, path, failed_types=None, start_time=0, end_time=None, **kwargs):
        raise NotImplementedError

    def can_provide_route_event--- This code section failed: ---

 L.  66         0  LOAD_FAST                'route_event_cls'
                2  LOAD_CONST               None
                4  COMPARE_OP               is-not
                6  JUMP_IF_FALSE_OR_POP    32  'to 32'

 L.  67         8  LOAD_FAST                'failed_types'
               10  LOAD_CONST               None
               12  COMPARE_OP               is
               14  POP_JUMP_IF_TRUE     24  'to 24'
               16  LOAD_FAST                'route_event_cls'
               18  LOAD_FAST                'failed_types'
               20  COMPARE_OP               not-in
               22  JUMP_IF_FALSE_OR_POP    32  'to 32'
             24_0  COME_FROM            14  '14'

 L.  68        24  LOAD_FAST                'route_event_cls'
               26  LOAD_METHOD              test
               28  LOAD_FAST                'sim_resolver'
               30  CALL_METHOD_1         1  '1 positional argument'
             32_0  COME_FROM            22  '22'
             32_1  COME_FROM             6  '6'
               32  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 32_1

    def is_route_event_valid(self, route_event, time, sim, path):
        raise NotImplementedError


class RouteEventProviderRequest(RouteEventProviderMixin, ParentElement, HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'route_events':TunableTuple(description='\n            There are two kinds of route events. One is an that has a chance to\n            play every route at a low priority. One is repeating and gets\n            dispersed throughout the route at a very low priority.\n            ',
       single_events=TunableList(description='\n                Single Route Events to possibly play once on a route while the\n                Sim has this request active.\n                ',
       tunable=RouteEvent.TunableReference(description='\n                    A single route event that may happen once when a Sim is\n                    routing with this request on them.\n                    ',
       pack_safe=True)),
       repeating_events=TunableList(description='\n                Repeating Route Events which can occur multiple times over the\n                course of a route while this request is active.\n                ',
       tunable=RouteEvent.TunableReference(description="\n                    A repeating route event which will be dispersed throughout\n                    a Sim's route while they have this request on them.\n                    ",
       pack_safe=True))), 
     'participant':TunableEnumEntry(description='\n            The participant to which the Route Events will be attached.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Actor)}

    def __init__(self, owner, *args, sequence=(), **kwargs):
        (super().__init__)(*args, **kwargs)
        if hasattr(owner, 'is_super'):
            self._target = next(iter(owner.get_participantsself.participant))
        else:
            self._target = owner
        self._sequence = sequence

    def start(self, *args, **kwargs):
        if self._target.routing_component is None:
            logger.error('Route Event Provider target {} has no routing component.', self._target)
            return
        self._target.routing_component.add_route_event_providerself

    def stop(self, *args, **kwargs):
        if self._target.routing_component is None:
            logger.error('Route Event Provider target {} has no routing component.', self._target)
            return
        self._target.routing_component.remove_route_event_providerself

    def provide_route_events(self, route_event_context, sim, path, failed_types=None, start_time=0, end_time=None, **kwargs):
        if self._target.is_sim:
            resolver = SingleSimResolver(self._target.sim_info)
        else:
            resolver = SingleObjectResolver(self._target)
        for route_event_cls in self.route_events.single_events:
            if self.can_provide_route_event(route_event_cls, failed_types, resolver):
                route_event_context.route_event_already_scheduledroute_event_cls or route_event_context.route_event_already_fully_considered(route_event_cls, self) or route_event_context.add_route_event(RouteEventType.LOW_SINGLE, route_event_cls(provider=self, provider_required=True))

        for route_event_cls in self.route_events.repeating_events:
            if self.can_provide_route_event(route_event_cls, failed_types, resolver):
                route_event_context.route_event_already_fully_considered(route_event_cls, self) or route_event_context.add_route_event(RouteEventType.LOW_REPEAT, route_event_cls(provider=self, provider_required=True))

    def is_route_event_valid(self, route_event, time, sim, path):
        return True

    def _run(self, timeline):
        sequence = build_critical_section_with_finally(self.start, self._sequence, self.stop)
        return timeline.run_childsequence
