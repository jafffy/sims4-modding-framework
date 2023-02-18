# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\priority.py
# Compiled at: 2017-07-28 22:37:42
# Size of source mod 2**32: 1404 bytes
import enum

class Priority(enum.Int):
    Low = 1
    High = 2
    Critical = 3


class PriorityExtended(Priority, export=False):
    SubLow = 0


def can_priority_displace(priority_new, priority_existing, allow_clobbering=False):
    if priority_new is None:
        return False
    if allow_clobbering:
        return priority_new >= priority_existing
    return priority_new > priority_existing


def can_displace(interaction_new, interaction_existing, allow_clobbering=False):
    if not can_priority_displace((interaction_new.priority), (interaction_existing.priority), allow_clobbering=allow_clobbering):
        return False
    return not interaction_existing.is_cancel_aop
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/priority.pyc
