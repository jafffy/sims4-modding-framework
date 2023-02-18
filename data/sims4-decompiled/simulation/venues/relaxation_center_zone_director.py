# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\venues\relaxation_center_zone_director.py
# Compiled at: 2021-06-16 00:14:57
# Size of source mod 2**32: 636 bytes
from situations.complex.yoga_class import YogaClassScheduleMixin
from venues.scheduling_zone_director import SchedulingZoneDirector
from venues.visitor_situation_on_arrival_zone_director_mixin import VisitorSituationOnArrivalZoneDirectorMixin
import sims4
logger = sims4.log.Logger('RelaxationCenterZoneDirector')

class RelaxationCenterZoneDirector(VisitorSituationOnArrivalZoneDirectorMixin, SchedulingZoneDirector):
    pass
# okay decompiling data/sims4-not-yet-decompiled/simulation/venues/relaxation_center_zone_director.pyc
