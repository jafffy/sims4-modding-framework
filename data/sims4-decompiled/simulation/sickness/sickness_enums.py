# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sickness\sickness_enums.py
# Compiled at: 2017-03-20 17:43:00
# Size of source mod 2**32: 874 bytes
from sims4.tuning.dynamic_enum import DynamicEnum
import enum

class SicknessDiagnosticActionType(enum.Int):
    EXAM = 0
    TREATMENT = 1


class DiagnosticActionResultType(DynamicEnum):
    DEFAULT = 0
    CORRECT_TREATMENT = 1
    INCORRECT_TREATMENT = 2
    FAILED_TOO_STRESSED = 3
# okay decompiling data/sims4-not-yet-decompiled/simulation/sickness/sickness_enums.pyc
