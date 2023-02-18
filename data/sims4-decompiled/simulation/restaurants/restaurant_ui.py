# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\restaurants\restaurant_ui.py
# Compiled at: 2018-04-18 21:08:22
# Size of source mod 2**32: 384 bytes
from distributor.ops import Op, protocol_constants

class ShowMenu(Op):

    def __init__(self, show_menu_message):
        super().__init__()
        self.op = show_menu_message

    def write(self, msg):
        self.serialize_op(msg, self.op, protocol_constants.RESTAURANT_SHOW_MENU)
# okay decompiling data/sims4-not-yet-decompiled/simulation/restaurants/restaurant_ui.pyc
