# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\fire\fire_sprinkler_head.py
# Compiled at: 2014-06-24 20:04:34
# Size of source mod 2**32: 511 bytes
import objects.game_object

class FireSprinklerHead(objects.game_object.GameObject):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.vfx = None

    def on_remove(self):
        if self.vfx is not None:
            self.vfx.stop()
        super().on_remove()
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/fire/fire_sprinkler_head.pyc
