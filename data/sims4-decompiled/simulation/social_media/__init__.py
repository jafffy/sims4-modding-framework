# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\social_media\__init__.py
# Compiled at: 2022-02-09 17:50:29
# Size of source mod 2**32: 923 bytes
import enum

class SocialMediaNarrative(enum.Int):
    FRIENDLY = 0
    FLIRTY = 1
    MEAN = 2
    PROUD = 3
    EMBARRASSED = 4
    EXCITED = 5
    HAPPY = 6
    SAD = 7
    STRESSED = 8
    FUNNY = 9
    UNCOMFORTABLE = 10
    PRANK = 11


class SocialMediaPostType(enum.Int):
    DEFAULT = 0
    DIRECT_MESSAGE = 1
    FRIEND_REQUEST = 2
    FOLLOWERS_UPDATE = 3
    PUBLIC_POST = 4


class SocialMediaPolarity(enum.Int):
    POSITIVE = 0
    NEGATIVE = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/social_media/__init__.pyc
