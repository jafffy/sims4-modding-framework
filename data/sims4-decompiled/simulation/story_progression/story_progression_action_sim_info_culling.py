# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\story_progression\story_progression_action_sim_info_culling.py
# Compiled at: 2019-10-26 00:02:21
# Size of source mod 2**32: 37518 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
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
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_OR . 
build_slice2 ::= expr . expr BUILD_SLICE_2
build_slice2 ::= expr expr . BUILD_SLICE_2
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr . expr expr CALL_METHOD_3
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr . expr CALL_METHOD_3
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
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
call_kw36 ::= expr expr LOAD_CONST CALL_FUNCTION_KW_1 . 
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
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
continues ::= _stmts . lastl_stmt continue
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= generator_exp . 
expr ::= get_iter . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
generator_exp ::= load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
generator_exp ::= pos_arg . load_closure load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg . load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg load_genexpr . LOAD_STR MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= pos_arg load_genexpr LOAD_STR . MAKE_FUNCTION_9 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure BUILD_TUPLE_1 . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_3
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_3 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
load_genexpr ::= LOAD_GENEXPR . 
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_9
mkfunc ::= expr load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9 . 
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE . LOAD_STR MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR . MAKE_FUNCTION_8
mkfunc ::= load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_8 . 
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
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
stmt ::= assign . 
stmt ::= function_def . 
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
suite_stmts_opt ::= suite_stmts . 
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
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
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH . POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr SETUP_WITH POP_TOP . suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP . suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP . suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP . suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr SETUP_WITH POP_TOP \e_suite_stmts_opt . COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP \e_suite_stmts_opt . COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP \e_suite_stmts_opt . POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP \e_suite_stmts_opt . POP_BLOCK LOAD_CONST with_suffix
with ::= expr SETUP_WITH POP_TOP suite_stmts_opt . COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP suite_stmts_opt . COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr SETUP_WITH POP_TOP suite_stmts_opt . POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr SETUP_WITH POP_TOP suite_stmts_opt . POP_BLOCK LOAD_CONST with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt COME_FROM_WITH with_suffix
withasstmt ::= expr SETUP_WITH . store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 695       126  LOAD_CLOSURE             'get_score'
                 128  BUILD_TUPLE_1         1 
->               130  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                 132  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.<dictcomp>'
                 134  MAKE_FUNCTION_8          'closure'
                 136  LOAD_DEREF               'sim_info_manager'
                 138  LOAD_METHOD              get_all
                 140  CALL_METHOD_0         0  '0 positional arguments'
                 142  GET_ITER         
                 144  CALL_FUNCTION_1       1  '1 positional argument'
                 146  STORE_FAST               'distances'
from collections import Counter, namedtuple
import itertools
from gsi_handlers.sim_info_culling_handler import CullingArchive, CullingCensus
from objects import ALL_HIDDEN_REASONS
from performance.performance_commands import get_sim_info_creation_sources
from sims.genealogy_tracker import genealogy_caching
from sims.household import Household
from sims.sim_info_lod import SimInfoLODLevel
from sims4.math import MAX_INT32
from sims4.tuning.tunable import TunableRange, TunableTuple, TunablePercent, TunableMapping, TunableEnumEntry, OptionalTunable
from story_progression import StoryProgressionFlags
from story_progression.story_progression_action import _StoryProgressionAction
from story_progression.story_progression_enums import CullingReasons
from tunable_time import TunableTimeOfDay
from uid import UniqueIdGenerator
import gsi_handlers, services, sims4.log, telemetry_helper
logger = sims4.log.Logger('SimInfoCulling', default_owner='manus')
TELEMETRY_GROUP_STORY_PROGRESSION = 'STRY'
TELEMETRY_HOOK_CULL_SIMINFO_BEFORE = 'CSBE'
TELEMETRY_HOOK_CULL_SIMINFO_BEFORE2 = 'CSBT'
TELEMETRY_HOOK_CULL_SIMINFO_AFTER = 'CSAF'
TELEMETRY_CREATION_SOURCE_HOOK_COUNT = 10
TELEMETRY_CREATION_SOURCE_BUFFER_LENGTH = 100
with sims4.reload.protected(globals()):
    telemetry_id_generator = UniqueIdGenerator()
writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_STORY_PROGRESSION)
SimInfoCullingScoreInfo = namedtuple('SimInfoCullingScoreInfo', ('score', 'rel_score',
                                                                 'inst_score', 'importance_score'))
DEFAULT_CULLING_INFO = SimInfoCullingScoreInfo(0, 0, 0, 1.0)

class StoryProgressionActionMaxPopulation(_StoryProgressionAction):
    FACTORY_TUNABLES = {'sim_info_cap_per_lod':TunableMapping(description="\n            The mapping of SimInfoLODLevel value to an interval of sim info cap\n            integer values.\n            \n            NOTE: The ACTIVE lod can't be tuned here because it's being tracked\n            via the Maximum Size tuning in Household module tuning.\n            ",
       key_type=TunableEnumEntry(description='\n                The SimInfoLODLevel value.\n                ',
       tunable_type=SimInfoLODLevel,
       default=(SimInfoLODLevel.FULL),
       invalid_enums=(
      SimInfoLODLevel.ACTIVE,)),
       value_type=TunableRange(description='\n                The number of sim infos allowed to be present before culling\n                is triggered for this SimInfoLODLevel.\n                ',
       tunable_type=int,
       default=210,
       minimum=0)), 
     'time_of_day':TunableTuple(description='\n            Only run this action when it is between a certain time of day.\n            ',
       start_time=TunableTimeOfDay(default_hour=2),
       end_time=TunableTimeOfDay(default_hour=6)), 
     'culling_buffer_percentage':TunablePercent(description='\n            When sim infos are culled due to the number of sim infos exceeding\n            the cap, this is how much below the cap the number of sim infos\n            will be (as a percentage of the cap) after the culling, roughly.\n            The margin of error is due to the fact that we cull at the household\n            level, so the number of sims culled can be a bit more than this value\n            if the last household culled contains more sims than needed to reach\n            the goal. (i.e. we never cull partial households)\n            ',
       default=20), 
     'homeless_played_demotion_time':OptionalTunable(description='\n            If enabled, played Sims that have been homeless for at least this\n            many days will be drops from FULL to BASE_SIMULATABLE lod.\n            ',
       tunable=TunableRange(tunable_type=int,
       default=10,
       minimum=0))}

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self._played_family_tree_distances = {}
        self._precull_telemetry_data = Counter()
        self._precull_telemetry_lod_counts_str = ''
        self._telemetry_id = 0
        self._total_sim_cap = Household.MAXIMUM_SIZE
        self._total_sim_cap += sum(self.sim_info_cap_per_lod.values())
        import sims.sim_info_manager
        sims.sim_info_manager.SimInfoManager.SIM_INFO_CAP = self._total_sim_cap
        sims.sim_info_manager.SIM_INFO_CAP_PER_LOD = self.sim_info_cap_per_lod

    def should_process(self, options):
        current_time = services.time_service().sim_now
        if not current_time.time_between_day_times(self.time_of_day.start_time, self.time_of_day.end_time):
            return False
        return True

    def process_action(self, story_progression_flags):
        try:
            self._pre_cull()
            self._process_full()
            self._process_interacted()
            self._process_base()
            self._process_background()
            self._process_minimum()
            self._post_cull(story_progression_flags)
        finally:
            self._cleanup()

    def _get_cap_level(self, sim_info_lod):
        cap_override = services.sim_info_manager().get_sim_info_cap_override_per_lod(sim_info_lod)
        if cap_override is not None:
            return cap_override
        if sim_info_lod in self.sim_info_cap_per_lod:
            return self.sim_info_cap_per_lod[sim_info_lod]
        return 0

    def _pre_cull(self):
        self._played_family_tree_distances = self._get_played_family_tree_distances()
        self._telemetry_id = telemetry_id_generator()
        self._precull_telemetry_data['scap'] = self._total_sim_cap
        player_households, player_sims, households, sims, lod_counts = self._get_census()
        self._precull_telemetry_data['thob'] = households
        self._precull_telemetry_data['tsib'] = sims
        self._precull_telemetry_data['phob'] = player_households
        self._precull_telemetry_data['psib'] = player_sims
        self._precull_telemetry_lod_counts_str = self._get_lod_counts_str_for_telemetry(lod_counts)
        for sim_info in services.sim_info_manager().get_all():
            sim_info.report_telemetry('pre-culling')

        self._trigger_creation_source_telemetry()

    def _trigger_creation_source_telemetry(self):
        payload = ''
        counter = 0

        def dump_hook():
            hook_name = 'CS{:0>2}'.format(counter)
            with telemetry_helper.begin_hook(writer, hook_name) as (hook):
                hook.write_int('clid', self._telemetry_id)
                hook.write_string('crsr', payload)

        sources = get_sim_info_creation_sources()
        for source, count in sources.most_common():
            if counter >= TELEMETRY_CREATION_SOURCE_HOOK_COUNT:
                break
            delta = '{}${}'.format(source, count)
            if len(payload) + len(delta) <= TELEMETRY_CREATION_SOURCE_BUFFER_LENGTH:
                payload = '{}+{}'.format(payload, delta)
            else:
                dump_hook()
                payload = delta
                counter += 1

        dump_hook()

    def _process_full(self):
        if gsi_handlers.sim_info_culling_handler.is_archive_enabled():
            gsi_archive = CullingArchive('Full Pass')
            gsi_archive.census_before = self._get_gsi_culling_census()
        else:
            gsi_archive = None
        cap = self._get_cap_level(SimInfoLODLevel.FULL)
        sim_infos = services.sim_info_manager().get_sim_infos_with_lod(SimInfoLODLevel.FULL)
        now = services.time_service().sim_now
        mandatory_drops = set()
        scores = {}
        for sim_info in sim_infos:
            if sim_info.is_instanced(allow_hidden_flags=ALL_HIDDEN_REASONS):
                if gsi_archive is not None:
                    gsi_archive.add_sim_info_cullability(sim_info, info='immune -- instanced')
                    continue
                if not sim_info.is_player_sim:
                    if gsi_archive is not None:
                        gsi_archive.add_sim_info_cullability(sim_info, score=0, info='mandatory drop -- non-player')
                    mandatory_drops.add(sim_info)
                    continue
                if sim_info.household.home_zone_id != 0:
                    if gsi_archive is not None:
                        gsi_archive.add_sim_info_cullability(sim_info, info='immune -- player and not homeless')
                        continue
                if self.homeless_played_demotion_time is not None:
                    days_homeless = (now - sim_info.household.home_zone_move_in_time).in_days()
                    if days_homeless < self.homeless_played_demotion_time:
                        if gsi_archive is not None:
                            gsi_archive.add_sim_info_cullability(sim_info, info='immune -- not homeless long enough')
                        elif gsi_archive is not None:
                            gsi_archive.add_sim_info_cullability(sim_info, score=days_homeless, info='homeless for too long')
                    else:
                        scores[sim_info] = days_homeless
                    continue
                if gsi_archive is not None:
                    gsi_archive.add_sim_info_cullability(sim_info, info='immune -- no pressure to drop')

        num_to_cull = self._get_num_to_cull(len(sim_infos) - len(mandatory_drops), cap)
        sorted_sims = sorted((scores.keys()), key=(lambda x: scores[x]), reverse=True)
        culling_service = services.get_culling_service()
        for sim_info in itertools.chain(mandatory_drops, sorted_sims[:num_to_cull]):
            if culling_service.has_sim_interacted_with_active_sim(sim_info.sim_id):
                new_lod = SimInfoLODLevel.INTERACTED
            else:
                new_lod = SimInfoLODLevel.BASE
            if sim_info.request_lod(new_lod):
                if gsi_archive is not None:
                    gsi_archive.add_sim_info_action(sim_info, action=('drop to {}'.format(new_lod)))
                elif gsi_archive is not None:
                    gsi_archive.add_sim_info_action(sim_info, action=('failed to drop to {}'.format(new_lod)))

        if gsi_archive is not None:
            gsi_archive.census_after = self._get_gsi_culling_census()
            gsi_archive.apply()

    def _process_interacted(self):
        if gsi_handlers.sim_info_culling_handler.is_archive_enabled():
            gsi_archive = CullingArchive('Interacted Pass')
            gsi_archive.census_before = self._get_gsi_culling_census()
        else:
            gsi_archive = None
        culling_service = services.get_culling_service()
        cap = self._get_cap_level(SimInfoLODLevel.INTERACTED)
        sim_info_manager = services.sim_info_manager()
        interacted_sim_ids_in_priority_order = culling_service.get_interacted_sim_ids_in_priority_order()
        interacted_count = 0
        for sim_id in interacted_sim_ids_in_priority_order:
            sim_info = sim_info_manager.get(sim_id)
            if sim_info is None or sim_info.lod != SimInfoLODLevel.INTERACTED:
                culling_service.remove_sim_from_interacted_sims(sim_id)
                continue
            else:
                interacted_count += 1
            if cap < interacted_count:
                if gsi_archive is not None:
                    gsi_archive.add_sim_info_cullability(sim_info, score=(interacted_sim_ids_in_priority_order.index(sim_id)),
                      info='last interaction too old')
                if sim_info.request_lod(SimInfoLODLevel.BASE):
                    culling_service.remove_sim_from_interacted_sims(sim_id)
                    interacted_count -= 1
                    if gsi_archive is not None:
                        gsi_archive.add_sim_info_action(sim_info, action='drop to BASE')
                    else:
                        if gsi_archive is not None:
                            gsi_archive.add_sim_info_action(sim_info, action='failed to drop to INTERACTED')
                elif gsi_archive is not None:
                    gsi_archive.add_sim_info_cullability(sim_info, score=(interacted_sim_ids_in_priority_order.index(sim_id)),
                      info='no pressure to drop')

        if gsi_archive is not None:
            gsi_archive.census_after = self._get_gsi_culling_census()
            gsi_archive.apply()

    def _process_base(self):

        def demote_from_base(sim_info, gsi_archive):
            if sim_info.request_lod(SimInfoLODLevel.BACKGROUND):
                if gsi_archive is not None:
                    gsi_archive.add_sim_info_action(sim_info, action='drop to BACKGROUND')
            elif gsi_archive is not None:
                gsi_archive.add_sim_info_action(sim_info, action='failed to drop to BACKGROUND')

        self._process_low(SimInfoLODLevel.BASE, 'Base Pass', demote_from_base)

    def _process_background(self):
        culling_service = services.get_culling_service()
        if gsi_handlers.sim_info_culling_handler.is_archive_enabled():
            gsi_archive = CullingArchive('Background Pass')
            gsi_archive.census_before = self._get_gsi_culling_census()
        else:
            gsi_archive = None
        background_cap = self._get_cap_level(SimInfoLODLevel.BACKGROUND)
        sim_info_manager = services.sim_info_manager()
        sim_infos = sim_info_manager.get_sim_infos_with_lod(SimInfoLODLevel.BACKGROUND)
        households = frozenset((sim_info.household for sim_info in sim_infos))
        num_infos_above_background_lod = sim_info_manager.get_num_sim_infos_with_criteria(lambda sim_info: sim_info.lod > SimInfoLODLevel.BACKGROUND)
        full_and_active_cap = self._get_cap_level(SimInfoLODLevel.FULL) + Household.MAXIMUM_SIZE
        cap_overage = num_infos_above_background_lod - full_and_active_cap
        cap = max(background_cap - cap_overage, 0) if cap_overage > 0 else background_cap
        sim_info_immunity_reasons = {}
        sim_info_scores = {}
        for sim_info in sim_infos:
            immunity_reasons = sim_info.get_culling_immunity_reasons()
            if immunity_reasons:
                sim_info_immunity_reasons[sim_info] = immunity_reasons
                continue
            sim_info_scores[sim_info] = culling_service.get_culling_score_for_sim_info(sim_info)

        household_scores = {}
        immune_households = set()
        for household in households:
            if any((sim_info.lod != SimInfoLODLevel.BACKGROUND or sim_info in sim_info_immunity_reasons for sim_info in household)):
                immune_households.add(household)
                continue
            score = max((sim_info_scores[sim_info].score for sim_info in household))
            household_scores[household] = score

        if gsi_archive is not None:
            for sim_info, immunity_reasons in sim_info_immunity_reasons.items():
                gsi_archive.add_sim_info_cullability(sim_info, info=('immune: {}'.format(', '.join((reason.gsi_reason for reason in immunity_reasons)))))

            for sim_info, score in sim_info_scores.items():
                gsi_archive.add_sim_info_cullability(sim_info, score=(score.score), rel_score=(score.rel_score),
                  inst_score=(score.inst_score),
                  importance_score=(score.importance_score))

            def get_sim_cullability(sim_info):
                if sim_info.lod > SimInfoLODLevel.BACKGROUND:
                    return 'LOD is not BACKGROUND'
                if sim_info in sim_info_immunity_reasons:
                    return ', '.join((reason.gsi_reason for reason in sim_info_immunity_reasons[sim_info]))
                if sim_info in sim_info_scores:
                    return str(sim_info_scores[sim_info].score)
                return ''

            for household in immune_households:
                member_cullabilities = ', '.join(('{} ({})'.format(sim_info.full_name, get_sim_cullability(sim_info)) for sim_info in household))
                gsi_archive.add_household_cullability(household, info=('immune: {}'.format(member_cullabilities)))

            for household, score in household_scores.items():
                member_cullabilities = ', '.join(('{} ({})'.format(sim_info.full_name, get_sim_cullability(sim_info)) for sim_info in household))
                gsi_archive.add_household_cullability(household, score=score, info=member_cullabilities)

        self._precull_telemetry_data['imho'] = len(immune_households)
        self._precull_telemetry_data['imsi'] = len(sim_info_immunity_reasons)
        self._precull_telemetry_data['imsc'] = sum((len(h) for h in immune_households))
        self._precull_telemetry_data.update((reason.telemetry_hook for reason in itertools.chain.from_iterable(sim_info_immunity_reasons.values())))
        for reason in CullingReasons.ALL_CULLING_REASONS:
            if reason not in self._precull_telemetry_data:
                self._precull_telemetry_data[reason.telemetry_hook] = 0

        culling_service = services.get_culling_service()
        sorted_households = sorted(household_scores, key=(household_scores.get))
        num_to_cull = self._get_num_to_cull(len(sim_infos), cap)
        while sorted_households and num_to_cull > 0:
            household = sorted_households.pop(0)
            num_to_cull -= len(household)
            culling_service.cull_household(household, is_important_fn=(self._has_player_sim_in_family_tree), gsi_archive=gsi_archive)

        for sim_info in sim_info_manager.get_all():
            if sim_info.household is None:
                logger.error('Found sim info {} without household during sim culling.', sim_info)

        if gsi_archive is not None:
            gsi_archive.census_after = self._get_gsi_culling_census()
            gsi_archive.apply()

    def _process_minimum(self):

        def demote_from_minimum(sim_info, gsi_archive):
            if gsi_archive is not None:
                gsi_archive.add_sim_info_action(sim_info, action='cull')
            sim_info.remove_permanently()

        self._process_low(SimInfoLODLevel.MINIMUM, 'Minimum Pass', demote_from_minimum)

    def _process_low(self, current_lod, debug_pass_name, demote_fn):
        if gsi_handlers.sim_info_culling_handler.is_archive_enabled():
            gsi_archive = CullingArchive(debug_pass_name)
            gsi_archive.census_before = self._get_gsi_culling_census()
        else:
            gsi_archive = None
        cap = self._get_cap_level(current_lod)
        sim_info_manager = services.sim_info_manager()
        min_lod_sim_infos = sim_info_manager.get_sim_infos_with_lod(current_lod)
        num_min_lod_sim_infos = len(min_lod_sim_infos)
        sorted_sim_infos = sorted(min_lod_sim_infos, key=(lambda x: self._played_family_tree_distances[x.id]), reverse=True)
        if gsi_archive is not None:
            for sim_info in min_lod_sim_infos:
                gsi_archive.add_sim_info_cullability(sim_info, score=(self._played_family_tree_distances[sim_info.id]))

        num_to_cull = self._get_num_to_cull(num_min_lod_sim_infos, cap)
        for sim_info in sorted_sim_infos[:num_to_cull]:
            demote_fn(sim_info, gsi_archive)

        if gsi_archive is not None:
            gsi_archive.census_after = self._get_gsi_culling_census()
            gsi_archive.apply()

    def _post_cull(self, story_progression_flags):
        with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_CULL_SIMINFO_BEFORE) as (hook):
            hook.write_int('clid', self._telemetry_id)
            hook.write_string('rson', self._get_trigger_reason(story_progression_flags))
            for key, value in self._precull_telemetry_data.items():
                hook.write_int(key, value)

        with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_CULL_SIMINFO_BEFORE2) as (hook):
            hook.write_int('clid', self._telemetry_id)
            hook.write_string('lodb', self._precull_telemetry_lod_counts_str)
        player_households, player_sims, households, sims, lod_counts = self._get_census()
        with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_CULL_SIMINFO_AFTER) as (hook):
            hook.write_int('clid', self._telemetry_id)
            hook.write_string('rson', self._get_trigger_reason(story_progression_flags))
            hook.write_int('scap', self._total_sim_cap)
            hook.write_int('thoa', households)
            hook.write_int('tsia', sims)
            hook.write_string('loda', self._get_lod_counts_str_for_telemetry(lod_counts))
            hook.write_int('phoa', player_households)
            hook.write_int('psia', player_sims)

    def _cleanup(self):
        self._played_family_tree_distances.clear()
        self._precull_telemetry_data.clear()

    def _get_played_family_tree_distances--- This code section failed: ---

 L. 606         0  LOAD_GLOBAL              genealogy_caching
                2  CALL_FUNCTION_0       0  '0 positional arguments'
                4  SETUP_WITH          152  'to 152'
                6  POP_TOP          

 L. 607         8  LOAD_GLOBAL              services
               10  LOAD_METHOD              sim_info_manager
               12  CALL_METHOD_0         0  '0 positional arguments'
               14  STORE_DEREF              'sim_info_manager'

 L. 608        16  LOAD_GLOBAL              frozenset
               18  LOAD_GENEXPR             '<code_object <genexpr>>'
               20  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.<genexpr>'
               22  MAKE_FUNCTION_0          'Neither defaults, keyword-only args, annotations, nor closures'
               24  LOAD_DEREF               'sim_info_manager'
               26  LOAD_METHOD              get_all
               28  CALL_METHOD_0         0  '0 positional arguments'
               30  GET_ITER         
               32  CALL_FUNCTION_1       1  '1 positional argument'
               34  CALL_FUNCTION_1       1  '1 positional argument'
               36  STORE_DEREF              'played_sim_infos'

 L. 610        38  LOAD_CLOSURE             'played_sim_infos'
               40  LOAD_CLOSURE             'sim_info_manager'
               42  BUILD_TUPLE_2         2 
               44  LOAD_CODE                <code_object get_sim_ids_with_played_spouses>
               46  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.get_sim_ids_with_played_spouses'
               48  MAKE_FUNCTION_8          'closure'
               50  STORE_FAST               'get_sim_ids_with_played_spouses'

 L. 618        52  LOAD_CLOSURE             'played_sim_infos'
               54  BUILD_TUPLE_1         1 
               56  LOAD_CODE                <code_object get_sim_ids_with_played_siblings>
               58  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.get_sim_ids_with_played_siblings'
               60  MAKE_FUNCTION_8          'closure'
               62  STORE_FAST               'get_sim_ids_with_played_siblings'

 L. 648        64  LOAD_CONST               (False,)
               66  LOAD_CLOSURE             'played_sim_infos'
               68  BUILD_TUPLE_1         1 
               70  LOAD_CODE                <code_object get_played_relative_distances>
               72  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.get_played_relative_distances'
               74  MAKE_FUNCTION_9          'default, closure'
               76  STORE_FAST               'get_played_relative_distances'

 L. 685        78  LOAD_FAST                'get_sim_ids_with_played_spouses'
               80  CALL_FUNCTION_0       0  '0 positional arguments'
               82  LOAD_FAST                'get_sim_ids_with_played_siblings'
               84  CALL_FUNCTION_0       0  '0 positional arguments'
               86  BINARY_OR        
               88  STORE_DEREF              'zero_distance_sim_ids'

 L. 686        90  LOAD_FAST                'get_played_relative_distances'
               92  LOAD_CONST               True
               94  LOAD_CONST               ('up',)
               96  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               98  STORE_DEREF              'ancestor_map'

 L. 687       100  LOAD_FAST                'get_played_relative_distances'
              102  LOAD_CONST               False
              104  LOAD_CONST               ('up',)
              106  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              108  STORE_DEREF              'descendant_map'

 L. 689       110  LOAD_CLOSURE             'ancestor_map'
              112  LOAD_CLOSURE             'descendant_map'
              114  LOAD_CLOSURE             'zero_distance_sim_ids'
              116  BUILD_TUPLE_3         3 
              118  LOAD_CODE                <code_object get_score>
              120  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.get_score'
              122  MAKE_FUNCTION_8          'closure'
              124  STORE_DEREF              'get_score'

 L. 695       126  LOAD_CLOSURE             'get_score'
              128  BUILD_TUPLE_1         1 
              130  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              132  LOAD_STR                 'StoryProgressionActionMaxPopulation._get_played_family_tree_distances.<locals>.<dictcomp>'
              134  MAKE_FUNCTION_8          'closure'
              136  LOAD_DEREF               'sim_info_manager'
              138  LOAD_METHOD              get_all
              140  CALL_METHOD_0         0  '0 positional arguments'
              142  GET_ITER         
              144  CALL_FUNCTION_1       1  '1 positional argument'
              146  STORE_FAST               'distances'

 L. 696       148  LOAD_FAST                'distances'
              150  RETURN_VALUE     
            152_0  COME_FROM_WITH        4  '4'
              152  WITH_CLEANUP_START
              154  WITH_CLEANUP_FINISH
              156  END_FINALLY      

Parse error at or near `LOAD_DICTCOMP' instruction at offset 130

    def _has_player_sim_in_family_tree(self, sim_info):
        if sim_info.id not in self._played_family_tree_distances:
            logger.error('Getting played family tree distance for an unknown Sim Info {}', sim_info)
            return False
        return self._played_family_tree_distances[sim_info.id] < MAX_INT32

    def _get_distance_to_nearest_player_sim_in_family_tree(self, sim_info):
        if sim_info.id not in self._played_family_tree_distances:
            logger.error('Getting played family tree distance for an unknown Sim Info {}', sim_info)
            return MAX_INT32
        return self._played_family_tree_distances[sim_info.id]

    def _get_num_to_cull(self, pop_count, pop_cap):
        if pop_cap < 0:
            logger.error('Invalid pop_cap provided to _get_num_to_cull: {}', pop_cap)
        if pop_count > pop_cap:
            target_pop = pop_cap * (1 - self.culling_buffer_percentage)
            return int(pop_count - target_pop)
        return 0

    def _get_census(self):
        player_households = sum((1 for household in services.household_manager().get_all() if household.is_player_household))
        player_sims = sum((1 for sim_info in services.sim_info_manager().get_all() if sim_info.is_player_sim))
        households = len(services.household_manager())
        sims = len(services.sim_info_manager())
        lod_counts = {lod: services.sim_info_manager().get_num_sim_infos_with_lod(lod) for lod in SimInfoLODLevel}
        return (
         player_households, player_sims, households, sims, lod_counts)

    def _get_lod_counts_str_for_telemetry(self, lod_counts):
        return '+'.join(('{}~{}'.format(lod.name, num) for lod, num in lod_counts.items()))

    def _get_gsi_culling_census(self):
        player_households, player_sims, households, sims, lod_counts = self._get_census()
        return CullingCensus(player_households, player_sims, households, sims, lod_counts)

    @classmethod
    def _get_trigger_reason(cls, flags):
        reason = 'REGULAR_PROGRESSION'
        if flags & StoryProgressionFlags.SIM_INFO_FIREMETER != 0:
            reason = 'FIREMETER'
        return reason
