# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\postures\posture_errors.py
# Compiled at: 2018-02-20 23:22:03
# Size of source mod 2**32: 1046 bytes


class PostureGraphError(Exception):
    pass


class PostureGraphBoundaryConditionError(PostureGraphError):
    pass


class PostureGraphMiddlePathError(PostureGraphError):
    pass
# okay decompiling data/sims4-not-yet-decompiled/simulation/postures/posture_errors.pyc
