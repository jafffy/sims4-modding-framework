# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\zone_types.py
# Compiled at: 2021-06-14 20:41:53
# Size of source mod 2**32: 957 bytes
import enum

class ZoneState(enum.Int, export=False):
    ZONE_INIT = 0
    OBJECTS_LOADED = 1
    CLIENT_CONNECTED = 2
    HOUSEHOLDS_AND_SIM_INFOS_LOADED = 3
    ALL_SIMS_SPAWNED = 4
    HITTING_THEIR_MARKS = 5
    RUNNING = 6
    SHUTDOWN_STARTED = 7
# okay decompiling data/sims4-not-yet-decompiled/simulation/zone_types.pyc
