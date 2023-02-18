# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\aspirations\aspiration_instance_manager.py
# Compiled at: 2018-06-11 20:26:46
# Size of source mod 2**32: 753 bytes
from aspirations.aspiration_types import AspriationType
from sims4.tuning.instance_manager import InstanceManager
import sims4.log
logger = sims4.log.Logger('Aspirations')

class AspirationInstanceManager(InstanceManager):

    def all_whim_sets_gen(self):
        for aspiration in self.types.values():
            if aspiration.aspiration_type == AspriationType.WHIM_SET:
                yield aspiration
# okay decompiling data/sims4-not-yet-decompiled/simulation/aspirations/aspiration_instance_manager.pyc
