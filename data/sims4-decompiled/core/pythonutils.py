# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\pythonutils.py
# Compiled at: 2015-01-29 18:25:40
# Size of source mod 2**32: 525 bytes
try:
    import _pythonutils
except ImportError:

    class _pythonutils:

        @staticmethod
        def try_highwater_gc():
            return False


try_highwater_gc = _pythonutils.try_highwater_gc
# okay decompiling data/sims4-not-yet-decompiled/core/pythonutils.pyc
