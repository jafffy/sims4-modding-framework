# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\business\business_situation_mixin.py
# Compiled at: 2017-06-29 22:20:17
# Size of source mod 2**32: 1384 bytes
import services

class BusinessSituationMixin:

    def __init__(self, *arg, **kwargs):
        (super().__init__)(*arg, **kwargs)
        self._business_manager = services.business_service().get_business_manager_for_zone()
        if self._business_manager is not None:
            self._business_manager.on_store_closed.register(self._on_business_closed)

    def _on_business_closed(self):
        for sim in self.all_sims_in_situation_gen():
            if not sim.is_selectable:
                services.get_zone_situation_manager().make_sim_leave(sim)

        self._self_destruct()

    def _destroy(self):
        business_manager = services.business_service().get_business_manager_for_zone()
        if business_manager is not None:
            if self._on_business_closed in business_manager.on_store_closed:
                business_manager.on_store_closed.unregister(self._on_business_closed)
        super()._destroy()
# okay decompiling data/sims4-not-yet-decompiled/simulation/business/business_situation_mixin.pyc
