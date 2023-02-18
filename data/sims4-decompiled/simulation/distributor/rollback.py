# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\distributor\rollback.py
# Compiled at: 2014-12-11 20:07:16
# Size of source mod 2**32: 1176 bytes
from distributor import logger

class ProtocolBufferRollbackExpected(Exception):
    pass


class ProtocolBufferRollback:

    def __init__(self, repeated_field):
        self._repeated_field = repeated_field

    def __enter__(self):
        return self._repeated_field.add()

    def __exit__(self, exc_type, value, tb):
        if exc_type is not None:
            del self._repeated_field[len(self._repeated_field) - 1]
            if exc_type is not ProtocolBufferRollbackExpected:
                logger.exception('Exception occurred while attempting to populate a repeated field:')
        return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/distributor/rollback.pyc
