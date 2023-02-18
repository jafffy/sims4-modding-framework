# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\gardening\gardening_component_variant.py
# Compiled at: 2021-01-22 00:19:43
# Size of source mod 2**32: 1287 bytes
from objects.gardening.gardening_component_crop_fruit import GardeningCropFruitComponent
from objects.gardening.gardening_component_crop_plant import GardeningCropPlantComponent
from objects.gardening.gardening_component_fruit import GardeningFruitComponent
from objects.gardening.gardening_component_plant import GardeningPlantComponent
from objects.gardening.gardening_component_shoot import GardeningShootComponent
from sims4.tuning.tunable import TunableVariant

class TunableGardeningComponentVariant(TunableVariant):

    def __init__(self, **kwargs):
        (super().__init__)(fruit_component=GardeningFruitComponent.TunableFactory(), 
         plant_component=GardeningPlantComponent.TunableFactory(), 
         crop_fruit_component=GardeningCropFruitComponent.TunableFactory(), 
         crop_plant_component=GardeningCropPlantComponent.TunableFactory(), 
         shoot=GardeningShootComponent.TunableFactory(), 
         locked_args={'disabled': None}, 
         default='disabled', **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/gardening/gardening_component_variant.pyc
