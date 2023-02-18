# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\puddles\puddle_commands.py
# Compiled at: 2015-05-07 00:55:29
# Size of source mod 2**32: 1671 bytes
from objects.puddles import create_puddle, PuddleSize, PuddleLiquid
from objects.puddles.puddle import Puddle
from server_commands.argument_helpers import OptionalTargetParam, get_optional_target, RequiredTargetParam
import sims4.commands

@sims4.commands.Command('puddles.create')
def puddle_create(count: int=1, size: PuddleSize=PuddleSize.MediumPuddle, liquid=PuddleLiquid.WATER, obj: OptionalTargetParam=None, _connection=None):
    obj = get_optional_target(obj, _connection)
    if obj is None:
        return False
    for _ in range(count):
        puddle = create_puddle(size, liquid)
        if puddle is None:
            return False
        puddle.place_puddle(obj, max_distance=8)

    return True


@sims4.commands.Command('puddles.evaporate')
def puddle_evaporate(obj_id: RequiredTargetParam, _connection=None):
    obj = obj_id.get_target()
    if obj is None:
        return False
    else:
        return isinstance(obj, Puddle) or False
    obj.evaporate(None)
    return True


@sims4.commands.Command('puddles.grow')
def puddle_grow(obj_id: RequiredTargetParam, _connection=None):
    obj = obj_id.get_target()
    if obj is None:
        return False
    else:
        return isinstance(obj, Puddle) or False
    obj.try_grow_puddle()
    return True
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/puddles/puddle_commands.pyc
