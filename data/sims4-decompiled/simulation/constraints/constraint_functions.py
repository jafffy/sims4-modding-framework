# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\constraints\constraint_functions.py
# Compiled at: 2017-08-21 20:13:13
# Size of source mod 2**32: 1334 bytes
from _math import Vector2
import math
from sims4.math import TWO_PI

class ConstraintGoalGenerationFunctionBase:

    def __call__(self):
        return ()


class ConstraintGoalGenerationFunctionIdealRadius(ConstraintGoalGenerationFunctionBase):
    COUNT = 8

    def __init__(self, center, radius):
        self.center = Vector2(center.x, center.z)
        self.radius = radius

    def __call__(self):
        goals = []
        step = TWO_PI / self.COUNT
        for angle in range(self.COUNT):
            angle *= step
            x = math.cos(angle) * self.radius
            y = math.sin(angle) * self.radius
            v = Vector2(x, y)
            v += self.center
            goals.append(v)

        return tuple(goals)
# okay decompiling data/sims4-not-yet-decompiled/simulation/constraints/constraint_functions.pyc
