# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lunar_cycle\lunar_cycle_commands.py
# Compiled at: 2022-02-24 22:30:51
# Size of source mod 2**32: 2827 bytes
import services, sims4.commands
from lunar_cycle.lunar_cycle_enums import LunarPhaseType, LunarCycleLengthOption, LunarPhaseLockedOption
from server_commands.argument_helpers import OptionalSimInfoParam, get_optional_target

@sims4.commands.Command('lunar_cycle.set_phase')
def set_lunar_phase(phase: LunarPhaseType, _connection=None):
    services.lunar_cycle_service().set_phase(phase)
    return True


@sims4.commands.Command('lunar_cycle.set_cycle_length', command_type=(sims4.commands.CommandType.Live))
def set_lunar_cycle_length(length_option: LunarCycleLengthOption, _connection=None):
    services.lunar_cycle_service().set_cycle_length(length_option)
    return True


@sims4.commands.Command('lunar_cycle.set_lunar_effects_disabled', command_type=(sims4.commands.CommandType.Live))
def set_lunar_effects_disabled(disable_effects: bool, _connection=None):
    services.lunar_cycle_service().set_lunar_effects_disabled(disable_effects)
    return True


@sims4.commands.Command('lunar_cycle.set_locked_phase', command_type=(sims4.commands.CommandType.Live))
def set_locked_lunar_phase(locked_phase: LunarPhaseLockedOption, _connection=None):
    services.lunar_cycle_service().set_locked_phase(locked_phase)
    return True


@sims4.commands.Command('lunar_cycle.request_lunar_effect_tooltip', command_type=(sims4.commands.CommandType.Live))
def request_lunar_effect_tooltip(opt_sim: OptionalSimInfoParam=None, _connection=None):
    sim_info = get_optional_target(opt_sim, target_type=OptionalSimInfoParam, _connection=_connection)
    services.lunar_cycle_service().send_lunar_effects_tooltip_data(sim_info)
    return True


@sims4.commands.Command('lunar_cycle.request_forecast', command_type=(sims4.commands.CommandType.Live))
def request_lunar_forecast(num_days: int=1, _connection=None):
    services.lunar_cycle_service().populate_forecasts(num_days)
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/lunar_cycle/lunar_cycle_commands.pyc
