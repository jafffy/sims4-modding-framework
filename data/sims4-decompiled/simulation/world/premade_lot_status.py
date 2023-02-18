# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\world\premade_lot_status.py
# Compiled at: 2015-02-12 00:32:15
# Size of source mod 2**32: 535 bytes
import enum

class PremadeLotStatus(enum.Int):
    NOT_TRACKED = 0
    IS_PREMADE = 1
    NOT_PREMADE = 2
    export = False
# okay decompiling data/sims4-not-yet-decompiled/simulation/world/premade_lot_status.pyc
