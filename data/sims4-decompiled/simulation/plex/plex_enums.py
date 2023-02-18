# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\plex\plex_enums.py
# Compiled at: 2019-01-30 20:48:32
# Size of source mod 2**32: 606 bytes
import enum
INVALID_PLEX_ID = 0

class PlexBuildingType(enum.Int):
    DEFAULT = 0
    FULLY_CONTAINED_PLEX = 1
    PENTHOUSE_PLEX = 2
    INVALID = 3
    EXPLORABLE = 4
    COASTAL = 5
# okay decompiling data/sims4-not-yet-decompiled/simulation/plex/plex_enums.pyc
