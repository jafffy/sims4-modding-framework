# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\destruction_liability.py
# Compiled at: 2020-06-20 01:55:42
# Size of source mod 2**32: 1064 bytes
from interactions.liability import SharedLiability
DELETE_OBJECT_LIABILITY = 'DeleteObjectLiability'

class DeleteObjectLiability(SharedLiability):

    def __init__(self, obj_list, source_liability=None):
        super().__init__(source_liability=source_liability)
        self._delete_objects = obj_list

    def shared_release(self):
        for obj in self._delete_objects:
            obj.schedule_destroy_asap()

        self._delete_objects.clear()

    def merge(self, interaction, key, new_liability):
        new_liability._delete_objects.extend(self._delete_objects)
        return new_liability

    def create_new_liability(self, interaction):
        return self.__class__((self._delete_objects), source_liability=self)
# okay decompiling data/sims4-not-yet-decompiled/simulation/interactions/utils/destruction_liability.pyc
