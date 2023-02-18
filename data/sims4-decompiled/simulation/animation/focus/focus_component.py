# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\animation\focus\focus_component.py
# Compiled at: 2016-07-25 19:29:27
# Size of source mod 2**32: 2177 bytes
from animation.focus.focus_ops import SetFocusScore
from animation.focus.focus_score import TunableFocusScoreVariant
from objects.components import Component, types, componentmethod
from sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit
from sims4.tuning.tunable_hash import TunableStringHash32
import distributor.fields

class FocusComponent(Component, HasTunableFactory, AutoFactoryInit, component_name=types.FOCUS_COMPONENT):
    FACTORY_TUNABLES = {'_focus_bone':TunableStringHash32(description='\n            The bone Sims direct their attention towards when focusing on an\n            object.\n            ',
       default='_focus_'), 
     '_focus_score':TunableFocusScoreVariant()}

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._current_focus_score = self._focus_score

    @distributor.fields.ComponentField(op=SetFocusScore)
    def focus_score(self):
        return self._current_focus_score

    @focus_score.setter
    def focus_score(self, value):
        self._current_focus_score = value

    @componentmethod
    def get_focus_bone(self):
        return self._focus_bone
# okay decompiling data/sims4-not-yet-decompiled/simulation/animation/focus/focus_component.pyc
