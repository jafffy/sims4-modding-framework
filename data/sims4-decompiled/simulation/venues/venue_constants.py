# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\venues\venue_constants.py
# Compiled at: 2019-11-04 19:47:54
# Size of source mod 2**32: 1532 bytes
from sims4.tuning.dynamic_enum import DynamicEnum
from sims4.tuning.tunable import TunableReference
import enum, services, sims4.resources

class ZoneDirectorRequestType(enum.Int, export=False):
    CAREER_EVENT = ...
    GO_DANCING = ...
    DRAMA_SCHEDULER = ...
    AMBIENT_SUB_VENUE = ...
    AMBIENT_VENUE = ...


class NPCSummoningPurpose(DynamicEnum):
    DEFAULT = 0
    PLAYER_BECOMES_GREETED = 1
    BRING_PLAYER_SIM_TO_LOT = 2
    ZONE_FIXUP = 3
# okay decompiling data/sims4-not-yet-decompiled/simulation/venues/venue_constants.pyc
