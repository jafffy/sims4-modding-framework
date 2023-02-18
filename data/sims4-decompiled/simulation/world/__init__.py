# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\world\__init__.py
# Compiled at: 2021-05-06 17:56:29
# Size of source mod 2**32: 524 bytes
try:
    import _lot
except ImportError:

    class _lot:

        @staticmethod
        def get_lot_id_from_instance_id(*_, **__):
            return 0

        class Lot:
            pass


get_lot_id_from_instance_id = _lot.get_lot_id_from_instance_id
# okay decompiling data/sims4-not-yet-decompiled/simulation/world/__init__.pyc
