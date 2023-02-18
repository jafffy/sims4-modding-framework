# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\buffs\__init__.py
# Compiled at: 2015-12-09 22:13:40
# Size of source mod 2**32: 729 bytes
import enum

class BuffPolarity(enum.Int):
    NEUTRAL = 0
    NEGATIVE = 1
    POSITIVE = 2


class Appropriateness(enum.Int, export=False):
    DONT_CARE = (0, )
    NOT_ALLOWED = (1, )
    ALLOWED = (2, )
# okay decompiling data/sims4-not-yet-decompiled/simulation/buffs/__init__.pyc
