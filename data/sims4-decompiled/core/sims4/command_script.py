# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\command_script.py
# Compiled at: 2013-10-11 18:21:02
# Size of source mod 2**32: 1865 bytes
import os, paths, sims4.commands, sims4.log
logger = sims4.log.Logger('Commands')

def run_script(filename, _connection=None):
    filename = os.path.join(paths.APP_ROOT, filename)
    if not os.path.isfile(filename):
        logger.error("Could not find file '{}'", filename)
        return False
    with open(filename) as (fd):
        for line in fd:
            command = line.split('#', 1)[0].strip()
            if command.startswith('|'):
                command = command[1:]
                to_server = True
            else:
                to_server = False
            if not command:
                continue
            if to_server:
                sims4.commands.execute(command, _connection)
            elif _connection:
                sims4.commands.client_cheat(command, _connection)
            else:
                logger.error('Cannot send client command without a connection')

    return True
# okay decompiling data/sims4-not-yet-decompiled/core/sims4/command_script.pyc
