# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lot_decoration\lot_decoration_enums.py
# Compiled at: 2018-03-07 19:29:55
# Size of source mod 2**32: 566 bytes
import enum
from sims4.tuning.dynamic_enum import DynamicEnum

class DecorationLocation(enum.Int):
    FOUNDATIONS = 0
    EAVES = 1
    FRIEZES = 2
    FENCES = 3
    SPANDRELS = 4
    COLUMNS = 5


class DecorationPickerCategory(DynamicEnum):
    ALL = 0


LOT_DECORATION_DEFAULT_ID = 0
# okay decompiling data/sims4-not-yet-decompiled/simulation/lot_decoration/lot_decoration_enums.pyc
