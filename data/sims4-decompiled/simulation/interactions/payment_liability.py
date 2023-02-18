# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\payment_liability.py
# Compiled at: 2018-09-21 22:30:55
# Size of source mod 2**32: 576 bytes
from interactions.liability import Liability

class PaymentLiability(Liability):
    LIABILITY_TOKEN = 'PaymentLiability'

    def __init__(self, amount, payment_destinations, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.amount = amount
        self.payment_destinations = payment_destinations
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/payment_liability.pyc
