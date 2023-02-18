# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\id_generator.py
# Compiled at: 2013-05-01 03:04:56
# Size of source mod 2**32: 588 bytes
try:
    import _guid
except ImportError:
    _object_count = 0

    class _guid:

        @staticmethod
        def generate_s4guid():
            global _object_count
            _object_count += 1
            return _object_count


def __reload__(old_module_vars):
    pass


def generate_object_id():
    return _guid.generate_s4guid()
# okay decompiling data/sims4-not-yet-decompiled/simulation/id_generator.pyc
