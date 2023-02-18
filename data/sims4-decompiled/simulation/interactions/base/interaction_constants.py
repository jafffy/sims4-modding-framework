# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\base\interaction_constants.py
# Compiled at: 2019-02-05 19:05:58
# Size of source mod 2**32: 327 bytes
import enum

class InteractionQueuePreparationStatus(enum.Int, export=False):
    FAILURE = 0
    SUCCESS = 1
    NEEDS_DERAIL = 2
    PUSHED_REPLACEMENT = 3
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/base/interaction_constants.pyc
