# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\locators\locator.py
# Compiled at: 2018-11-09 21:29:53
# Size of source mod 2**32: 1488 bytes
import build_buy, sims4.math

class LocatorBase:

    def __init__(self, center, footprint_id, rotation, scale, obj_def_guid, lot_id=0, **kwargs):
        (super().__init__)(**kwargs)
        self.transform = sims4.math.Transform(center, rotation)
        self.footprint_id = footprint_id
        self.scale = scale
        self.obj_def_guid = obj_def_guid
        self.lot_id = lot_id
        self._tags = None

    @property
    def position(self):
        return self.transform.translation

    @property
    def rotation(self):
        return self.transform.orientation

    def get_tags(self):
        if self._tags is None:
            self._tags = frozenset(build_buy.get_object_all_tags(self.obj_def_guid))
        return self._tags

    def has_tag(self, tag):
        return tag in self.get_tags()


class LocatorObject(LocatorBase):
    pass
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/locators/locator.pyc
