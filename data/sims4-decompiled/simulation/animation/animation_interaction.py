# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\animation\animation_interaction.py
# Compiled at: 2017-02-02 23:54:50
# Size of source mod 2**32: 1448 bytes
from interactions.base.super_interaction import SuperInteraction
from interactions.base.tuningless_interaction import create_tuningless_superinteraction

class AnimationInteraction(SuperInteraction):
    INSTANCE_SUBCLASSES_ONLY = True

    def __init__(self, *args, hide_unrelated_held_props=True, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._hide_unrelated_held_props = hide_unrelated_held_props

    @property
    def animation_context(self):
        animation_liability = self.get_animation_context_liability()
        return animation_liability.animation_context

    def clear_animation_liability_cache(self):
        animation_liability = self.get_animation_context_liability()
        for posture, key_list in animation_liability.cached_asm_keys.items():
            for key in key_list:
                posture.remove_from_cache(key)

        animation_liability.cached_asm_keys.clear()


create_tuningless_superinteraction(AnimationInteraction)
# okay decompiling data/sims4-not-yet-decompiled/simulation/animation/animation_interaction.pyc
