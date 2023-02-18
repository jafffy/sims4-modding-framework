# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\automation\automation_commands.py
# Compiled at: 2017-05-26 21:30:18
# Size of source mod 2**32: 651 bytes
from automation import automation_utils
import sims4.commands

@sims4.commands.Command('qa.automation.enable_events', command_type=(sims4.commands.CommandType.Automation))
def automation_events(enabled: bool=True, _connection=None):
    automation_utils.dispatch_automation_events = enabled
# okay decompiling data/sims4-not-yet-decompiled/simulation/automation/automation_commands.pyc
