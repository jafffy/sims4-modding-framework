# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\sim_spawner_spawn_point_overrides.py
# Compiled at: 2020-06-24 19:46:34
# Size of source mod 2**32: 1241 bytes
from event_testing.resolver import SingleSimResolver
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableEnumWithFilter
from tag import Tag, SPAWN_PREFIX
from tunable_utils.tested_list import TunableTestedList, STOP_PROCESSING_ALWAYS

class TestedSpawnPointOverride(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'tested_list': TunableTestedList(tunable_type=TunableEnumWithFilter(tunable_type=Tag,
                      default=(Tag.INVALID),
                      invalid_enums=(
                     Tag.INVALID,),
                      filter_prefixes=SPAWN_PREFIX),
                      stop_processing_behavior=STOP_PROCESSING_ALWAYS)}

    def get_spawner_tag(self, sim_info):
        resolver = SingleSimResolver(sim_info)
        return next(iter((tag for tag in self.tested_list(resolver=resolver))), None)
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/sim_spawner_spawn_point_overrides.pyc
