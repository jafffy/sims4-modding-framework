# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\global_flags\global_flag_service.py
# Compiled at: 2021-06-01 21:43:27
# Size of source mod 2**32: 736 bytes
from sims4.service_manager import Service

class GlobalFlagService(Service):

    def __init__(self):
        self._flags = 0

    def add_flag(self, flag):
        self._flags |= flag

    def remove_flag(self, flag):
        self._flags &= ~flag

    def has_any_flag(self, flags):
        return bool(self._flags & flags)
# okay decompiling data/sims4-not-yet-decompiled/simulation/global_flags/global_flag_service.pyc
