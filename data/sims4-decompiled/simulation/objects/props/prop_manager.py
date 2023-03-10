# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\props\prop_manager.py
# Compiled at: 2017-04-26 21:34:57
# Size of source mod 2**32: 1913 bytes
from objects.object_manager import DistributableObjectManager, GameObjectManagerMixin
from objects.system import create_prop
from sims4.utils import classproperty

class PropManager(DistributableObjectManager, GameObjectManagerMixin):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._shared_props = {}

    @classproperty
    def supports_parenting(self):
        return True

    def create_shared_prop(self, key, definition_id):
        if key not in self._shared_props:
            self._shared_props[key] = (
             create_prop(definition_id), 0)
        prop, counter = self._shared_props[key]
        self._shared_props[key] = (prop, counter + 1)
        return prop

    def destroy_prop(self, prop, **kwargs):
        for key, (shared_prop, counter) in self._shared_props.items():
            if shared_prop is not prop:
                continue
            else:
                counter = counter - 1
                if not counter:
                    (prop.destroy)(**kwargs)
                    del self._shared_props[key]
                else:
                    self._shared_props[key] = (
                     prop, counter)
            break
        else:
            (prop.destroy)(**kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/props/prop_manager.pyc
