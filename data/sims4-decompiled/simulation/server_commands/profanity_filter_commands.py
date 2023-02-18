# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server_commands\profanity_filter_commands.py
# Compiled at: 2014-10-10 01:04:49
# Size of source mod 2**32: 1511 bytes
import collections, itertools, random, weakref, sims4.commands, sims4.zone_utils, _profanity_filter

@sims4.commands.Command('profanity_filter.check_text', command_type=(sims4.commands.CommandType.Live))
def profanity_check_text(text_to_check, _connection=None):
    ret_tuple = _profanity_filter.check(text_to_check)
    sims4.commands.output('check_text for string {} found {} violations -- replacement string is {}'.format(text_to_check, ret_tuple[0], ret_tuple[1]), _connection)
    return ret_tuple


@sims4.commands.Command('profanity_filter.scan_text', command_type=(sims4.commands.CommandType.Live))
def profanity_scan_text(text_to_check, _connection=None):
    num_violations = _profanity_filter.scan(text_to_check)
    sims4.commands.output('check_text for string {} found {} violations'.format(text_to_check, num_violations), _connection)
    return num_violations
# okay decompiling data/sims4-not-yet-decompiled/simulation/server_commands/profanity_filter_commands.pyc
