# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\pregnancy\pregnancy_client_mixin.py
# Compiled at: 2016-03-30 22:27:02
# Size of source mod 2**32: 881 bytes
from sims4.math import clamp
import distributor.fields, distributor.ops

class PregnancyClientMixin:

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._pregnancy_progress = 0

    @distributor.fields.Field(op=(distributor.ops.SetPregnancyProgress), default=None)
    def pregnancy_progress(self):
        return self._pregnancy_progress

    @pregnancy_progress.setter
    def pregnancy_progress(self, value):
        self._pregnancy_progress = clamp(0, value, 1) if value is not None else None
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/pregnancy/pregnancy_client_mixin.pyc
