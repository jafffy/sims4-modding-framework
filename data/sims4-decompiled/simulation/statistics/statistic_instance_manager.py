# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\statistics\statistic_instance_manager.py
# Compiled at: 2021-12-01 20:30:48
# Size of source mod 2**32: 1111 bytes
from sims4.tuning.instance_manager import InstanceManager
import sims4.log
logger = sims4.log.Logger('StatisticInstanceManager')

class StatisticInstanceManager(InstanceManager):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._skills = []

    def register_tuned_class(self, instance, resource_key):
        super().register_tuned_class(instance, resource_key)
        if instance.is_skill:
            self._skills.append(instance)

    def create_class_instances(self):
        self._skills = []
        super().create_class_instances()

        def key(cls):
            return cls.__name__.lower()

        self._skills = tuple(sorted((self._skills), key=key))

    def all_skills_gen(self):
        yield from self._skills
        if False:
            yield None
# okay decompiling data/sims4-not-yet-decompiled/simulation/statistics/statistic_instance_manager.pyc
