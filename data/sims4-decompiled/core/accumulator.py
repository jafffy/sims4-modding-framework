# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\accumulator.py
# Compiled at: 2012-10-04 02:04:24
# Size of source mod 2**32: 1468 bytes


class HarmonicMeanAccumulator:

    def __init__(self, seq=None):
        self._fault = False
        self.num_items = 0
        self.total = 0
        if seq is not None:
            for value in seq:
                if not self.fault():
                    self.add(value)

    def add(self, value):
        if value <= 0:
            self._fault = True
            return
        self.num_items += 1
        self.total += 1 / value

    def fault(self):
        return self._fault

    def value(self):
        if self._fault:
            return 0
        return self.num_items / self.total
# okay decompiling data/sims4-not-yet-decompiled/core/accumulator.pyc
