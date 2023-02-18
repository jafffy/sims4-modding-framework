# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\royalty_commands.py
# Compiled at: 2014-06-24 21:41:50
# Size of source mod 2**32: 843 bytes
from server_commands.argument_helpers import OptionalTargetParam, get_optional_target
import sims4.commands

@sims4.commands.Command('royalty.give_royalties')
def give_royalties(opt_sim: OptionalTargetParam=None, _connection=None):
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        sims4.commands.output('Target Sim could not be found.', _connection)
        return False
    royalty_tracker = sim.sim_info.royalty_tracker
    if royalty_tracker is None:
        sims4.commands.output('Royalty Tracker not found for Sim.', _connection)
        return False
    royalty_tracker.update_royalties_and_get_paid()
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/royalty_commands.pyc
