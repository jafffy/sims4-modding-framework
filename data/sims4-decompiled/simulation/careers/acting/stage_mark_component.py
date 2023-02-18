# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\careers\acting\stage_mark_component.py
# Compiled at: 2018-04-26 01:20:19
# Size of source mod 2**32: 664 bytes
from objects.components import Component, types

class StageMarkComponent(Component, allow_dynamic=True, component_name=types.STAGE_MARK_COMPONENT):

    def __init__(self, *args, performance_interactions=(), **kwargs):
        (super().__init__)(*args, **kwargs)
        self._performance_interactions = performance_interactions

    def component_super_affordances_gen(self, **kwargs):
        yield from self._performance_interactions
        if False:
            yield None
# okay decompiling data/sims4-not-yet-decompiled/simulation/careers/acting/stage_mark_component.pyc
