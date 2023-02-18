# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\payment\payment_info.py
# Compiled at: 2016-06-09 21:53:47
# Size of source mod 2**32: 858 bytes
import enum

class PaymentInfo:

    def __init__(self, amount, resolver):
        self.amount = amount
        self.resolver = resolver


class BusinessPaymentInfo(PaymentInfo):

    def __init__(self, *args, revenue_type, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.revenue_type = revenue_type


class PaymentBusinessRevenueType(enum.Int):
    ITEM_SOLD = 0
    SEED_MONEY = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/payment/payment_info.pyc
