# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\global_policies\global_policy_enums.py
# Compiled at: 2019-01-17 01:35:04
# Size of source mod 2**32: 440 bytes
import enum

class GlobalPolicyProgressEnum(enum.Int):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class GlobalPolicyTokenType(enum.Int):
    NAME = 0
    PROGRESS = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/global_policies/global_policy_enums.pyc
