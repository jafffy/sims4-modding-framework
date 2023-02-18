# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\omega.py
# Compiled at: 2012-10-02 23:05:18
# Size of source mod 2**32: 729 bytes
try:
    import _omega
except ImportError:

    class _omega:

        @staticmethod
        def send(session_id, msg_id, data):
            return True


_send = _omega.send

def send(session_id, msg_id, data):
    if not _send(session_id, msg_id, data):
        raise KeyError('Failed to find ZoneSessionContext for [ZoneSessionId: 0x{:016x}]'.format(session_id))
# okay decompiling data/sims4-not-yet-decompiled/simulation/omega.pyc
