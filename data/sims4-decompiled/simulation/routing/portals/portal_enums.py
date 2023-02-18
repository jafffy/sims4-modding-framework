# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\portals\portal_enums.py
# Compiled at: 2020-02-21 21:24:37
# Size of source mod 2**32: 1852 bytes
import enum
from animation import animation_constants

class PathSplitType(enum.Int, export=False):
    PathSplitType_DontSplit = 0
    PathSplitType_Split = 1
    PathSplitType_LadderSplit = 2


class PortalAlignment(enum.Int):
    PA_FRONT = 0
    PA_LEFT = 1
    PA_RIGHT = 2

    @staticmethod
    def get_asm_parameter_string(alignment):
        if alignment is PortalAlignment.PA_FRONT:
            return animation_constants.ASM_LADDER_PORTAL_ALIGNMENT_FRONT
        if alignment is PortalAlignment.PA_LEFT:
            return animation_constants.ASM_LADDER_PORTAL_ALIGNMENT_LEFT
        if alignment is PortalAlignment.PA_RIGHT:
            return animation_constants.ASM_LADDER_PORTAL_ALIGNMENT_RIGHT
        return

    @staticmethod
    def get_bit_flag(alignment):
        return 1 << alignment


class LadderType(enum.Int, export=False):
    LADDER_OCEAN = 0
    LADDER_BUILD = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/portals/portal_enums.pyc
