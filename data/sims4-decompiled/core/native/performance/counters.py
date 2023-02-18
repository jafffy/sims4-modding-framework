# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\native\performance\counters.py
# Compiled at: 2014-12-16 00:27:05
# Size of source mod 2**32: 965 bytes
try:
    from _perf_api import set_counter
except:

    def set_counter(name: str, value: int):
        pass


try:
    from _perf_api import add_counter
except:

    def add_counter(name: str, value: int):
        pass


try:
    from _perf_api import subtract_counter
except:

    def subtract_counter(name: str, value: int):
        pass


class CounterIDs:
    AUTONOMY_QUEUE_LENGTH = 'autonomyQueueLength64'
    AUTONOMY_QUEUE_TIME = 'autonomyQueueTime64'
    EVENT_TIME_DEVIATION = 'eventTimeDeviation64'
    NUM_PENDING_EVENTS = 'numPendingEvents64'
    NUM_PRIMITIVES = 'numPrimitives64'
# okay decompiling data/sims4-not-yet-decompiled/core/native/performance/counters.pyc
