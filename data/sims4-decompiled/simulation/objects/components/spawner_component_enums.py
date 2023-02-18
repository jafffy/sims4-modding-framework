# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\spawner_component_enums.py
# Compiled at: 2020-08-11 16:25:53
# Size of source mod 2**32: 333 bytes
import enum

class SpawnerType(enum.Int):
    GROUND = 0
    SLOT = 1
    INTERACTION = 2


class SpawnLocation(enum.Int):
    SPAWNER = 0
    PORTAL = 1
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/spawner_component_enums.pyc
