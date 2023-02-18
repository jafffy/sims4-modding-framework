# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\bills_enums.py
# Compiled at: 2020-01-14 22:00:10
# Size of source mod 2**32: 664 bytes
import enum
from sims4.tuning.dynamic_enum import DynamicEnum

class AdditionalBillSource(DynamicEnum):
    Miscellaneous = 0


class UtilityEndOfBillAction(enum.Int, export=False):
    SELL = 0
    STORE = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/bills_enums.pyc
