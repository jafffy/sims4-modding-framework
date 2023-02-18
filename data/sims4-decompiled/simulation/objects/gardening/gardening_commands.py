# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\gardening\gardening_commands.py
# Compiled at: 2021-06-01 20:44:42
# Size of source mod 2**32: 2495 bytes
from objects.components import types
from objects.components.types import GARDENING_COMPONENT
from objects.gardening.gardening_component_fruit import _GardeningBaseFruitComponent, GardeningFruitComponent
from sims4.commands import CommandType
import services, sims4.commands

@sims4.commands.Command('gardening.cleanup_gardening_objects')
def cleanup_gardening_objects(_connection=None):
    for obj in services.object_manager().get_all_objects_with_component_gen(GARDENING_COMPONENT):
        gardening_component = obj.get_component(types.GARDENING_COMPONENT)
        if not isinstance(gardening_component, GardeningFruitComponent):
            continue
        if obj.parent is None:
            obj.is_in_inventory() or obj.is_on_active_lot() or sims4.commands.output('Destroyed object {} on open street was found without a parent at position {}, parent_type {}.'.format(obj, obj.position, obj.parent_type), _connection)
            obj.destroy(source=obj, cause='Fruit/Flower with no parent on open street')

    sims4.commands.output('Gardening cleanup complete', _connection)
    return True


@sims4.commands.Command('gardening.remove_all_fruits', command_type=(CommandType.Automation))
def remove_all_fruits(_connection=None):
    objs_to_delete = []
    for obj in services.object_manager().get_all_objects_with_component_gen(GARDENING_COMPONENT):
        gardening_component = obj.get_component(types.GARDENING_COMPONENT)
        if not isinstance(gardening_component, _GardeningBaseFruitComponent):
            continue
        objs_to_delete.append(obj)

    for obj in objs_to_delete:
        sims4.commands.output('Destroyed object {} at position {}, parent_type {}.'.format(obj, obj.position, obj.parent_type), _connection)
        obj.destroy(source=obj, cause='Destroyed by cheat command gardening.remove_all_fruits')

    sims4.commands.output('Gardening cleanup complete', _connection)
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/gardening/gardening_commands.pyc
