# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\gardening\gardening_component_shoot.py
# Compiled at: 2018-02-01 22:40:39
# Size of source mod 2**32: 804 bytes
from protocolbuffers import SimObjectAttributes_pb2 as protocols
from objects.gardening.gardening_component import _GardeningComponent
import objects.components.types

class GardeningShootComponent(_GardeningComponent, component_name=objects.components.types.GARDENING_COMPONENT, persistence_key=protocols.PersistenceMaster.PersistableData.GardeningComponent):

    @property
    def is_shoot(self):
        return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/gardening/gardening_component_shoot.pyc
