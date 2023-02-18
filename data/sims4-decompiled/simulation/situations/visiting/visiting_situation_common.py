# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\visiting\visiting_situation_common.py
# Compiled at: 2016-10-24 23:40:56
# Size of source mod 2**32: 755 bytes
from situations.situation import Situation
import situations.situation_complex, situations.situation_types

class VisitingNPCSituation(situations.situation_complex.SituationComplexCommon):
    INSTANCE_SUBCLASSES_ONLY = True
    REMOVE_INSTANCE_TUNABLES = Situation.NON_USER_FACING_REMOVE_INSTANCE_TUNABLES

    @classmethod
    def _get_greeted_status(cls):
        return situations.situation_types.GreetedStatus.GREETED
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/visiting/visiting_situation_common.pyc
