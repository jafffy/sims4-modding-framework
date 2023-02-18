# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\global_policies\global_policy_commands.py
# Compiled at: 2019-02-20 22:31:10
# Size of source mod 2**32: 581 bytes
from server_commands.argument_helpers import TunableInstanceParam
import services, sims4

@sims4.commands.Command('global_policy.set_progress', command_type=(sims4.commands.CommandType.Automation))
def set_global_policy_progress(policy: TunableInstanceParam(sims4.resources.Types.SNIPPET), progress_amount: int, _connection=None):
    services.global_policy_service().add_global_policy_progress(policy, progress_amount)
# okay decompiling data/sims4-not-yet-decompiled/simulation/global_policies/global_policy_commands.pyc
