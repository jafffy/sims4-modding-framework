# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\complex\village_vendor_situation.py
# Compiled at: 2021-04-20 22:17:35
# Size of source mod 2**32: 2239 bytes
from situations.ambient.tend_object_situation import TendObjectSituation
from situations.bouncer.bouncer_types import RequestSpawningOption, BouncerRequestPriority
from situations.situation_guest_list import SituationGuestList, SituationGuestInfo
import services, sims4
logger = sims4.log.Logger('VillageVendorSituation', default_owner='yozhang')

class VillageVendorSituation(TendObjectSituation):
    pass


class VillageVendorSpecificSimSituation(VillageVendorSituation):

    @classmethod
    def get_predefined_guest_list(cls):
        guest_list = SituationGuestList(invite_only=True)
        active_sim_info = services.active_sim_info()
        filter_result = services.sim_filter_service().submit_matching_filter(sim_filter=(cls.tendor_job_and_role_state.job.filter), callback=None,
          requesting_sim_info=active_sim_info,
          allow_yielding=False,
          allow_instanced_sims=True,
          gsi_source_fn=(cls.get_sim_filter_gsi_name))
        if not filter_result:
            logger.error('Failed to find/create any sims for {}.', cls)
            return guest_list
        guest_list.add_guest_info(SituationGuestInfo(filter_result[0].sim_info.sim_id, cls.tendor_job_and_role_state.job, RequestSpawningOption.DONT_CARE, BouncerRequestPriority.EVENT_VIP))
        return guest_list
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/complex/village_vendor_situation.pyc
