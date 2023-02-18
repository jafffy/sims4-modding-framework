# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\traits\preference_enums.py
# Compiled at: 2021-04-07 19:49:52
# Size of source mod 2**32: 638 bytes
from traits.trait_type import TraitType
import enum

class PreferenceTypes(enum.Int):
    LIKE = TraitType.LIKE
    DISLIKE = TraitType.DISLIKE


class PreferenceSubject(enum.Int):
    OBJECT = 0
    DECOR = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/traits/preference_enums.pyc
