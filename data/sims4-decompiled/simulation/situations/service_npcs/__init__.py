# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\service_npcs\__init__.py
# Compiled at: 2013-11-20 22:52:16
# Size of source mod 2**32: 653 bytes
from sims4.tuning.dynamic_enum import DynamicEnumLocked
import enum

class ServiceNpcEndWorkReason(enum.Int):
    NO_WORK_TO_DO = 0
    FINISHED_WORK = 1
    FIRED = 2
    NOT_PAID = 3
    ASKED_TO_HANG_OUT = 4
    DISMISSED = 5
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/service_npcs/__init__.pyc
