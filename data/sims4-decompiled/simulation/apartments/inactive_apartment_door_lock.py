# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\apartments\inactive_apartment_door_lock.py
# Compiled at: 2018-08-20 18:33:09
# Size of source mod 2**32: 1049 bytes
from objects.components.portal_lock_data import LockData, LockResult
from objects.components.portal_locking_enums import LockPriority, LockSide, LockType

class InactiveApartmentDoorLockData(LockData):

    def __init__(self, door):
        super().__init__(lock_type=(LockType.INACTIVE_APARTMENT_DOOR),
          lock_priority=(LockPriority.SYSTEM_LOCK),
          lock_sides=(LockSide.LOCK_FRONT),
          should_persist=True)
        self._door = door

    def test_lock(self, sim):
        if self._door.get_household_owner_id() == sim.household_id:
            return LockResult(False, self.lock_type, self.lock_priority, self.lock_sides)
        return LockResult(True, self.lock_type, self.lock_priority, self.lock_sides)
# okay decompiling data/sims4-not-yet-decompiled/simulation/apartments/inactive_apartment_door_lock.pyc
