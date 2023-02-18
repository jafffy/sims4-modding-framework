# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\primitives\persistence_primitives.py
# Compiled at: 2014-12-16 20:20:24
# Size of source mod 2**32: 610 bytes
try:
    import _persistence_primitives
except ImportError:

    class _persistence_primitives:
        PersistVersion = 0


class PersistVersion:
    UNKNOWN = 0
    kPersistVersion_Implementation = 1
    SaveObjectDepreciation = 2
    SaveObjectCreateFromLotTemplate = 3
    SaveLoadSIFirstPass = 4
    GlobalSaveData = 5
# okay decompiling data/sims4-not-yet-decompiled/simulation/primitives/persistence_primitives.pyc
