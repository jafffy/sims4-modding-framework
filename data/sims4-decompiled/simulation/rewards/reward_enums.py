# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\rewards\reward_enums.py
# Compiled at: 2019-04-22 23:22:37
# Size of source mod 2**32: 992 bytes
import enum

class RewardDestination(enum.Int):
    SIM = 0
    HOUSEHOLD = 1
    MAILBOX = 2


class RewardType(enum.Int, export=False):
    MONEY = 0
    OBJECT_DEFINITION = 1
    TRAIT = 2
    CAS_PART = 3
    BUILD_BUY_OBJECT = 4
    BUILD_BUY_MAGAZINE_COLLECTION = 5
    DISPLAY_TEXT = 6
    ADDITIONAL_EMPLOYEE_SLOT = 7
    ADDITIONAL_BUSINESS_CUSTOMER_COUNT = 8
    ADDITIONAL_BUSINESS_MARKUP = 9
    SET_CLUB_GATHERING_VIBE = 10
    BUCKS = 11
    BUFF = 12
    WHIM_BUCKS = 13
# okay decompiling data/sims4-not-yet-decompiled/simulation/rewards/reward_enums.pyc
