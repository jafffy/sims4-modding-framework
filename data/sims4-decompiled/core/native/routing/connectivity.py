# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\native\routing\connectivity.py
# Compiled at: 2014-12-16 00:27:05
# Size of source mod 2**32: 457 bytes
try:
    from _pathing import connectivity_handle as Handle, connectivity_handle_list as HandleList
except ImportError:

    class Handle:

        def __init__(self, location):
            self.location = location


    class HandleList:

        def __init__(self):
            pass
# okay decompiling data/sims4-not-yet-decompiled/core/native/routing/connectivity.pyc
