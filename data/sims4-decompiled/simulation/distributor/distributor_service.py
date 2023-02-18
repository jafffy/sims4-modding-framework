# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\distributor\distributor_service.py
# Compiled at: 2014-06-09 07:06:26
# Size of source mod 2**32: 951 bytes
from sims4.service_manager import Service
import distributor.system

class DistributorService(Service):

    def start(self):
        import animation.arb
        animation.arb.set_tag_functions(distributor.system.get_next_tag_id, distributor.system.get_current_tag_set)
        distributor.system._distributor_instance = distributor.system.Distributor()

    def stop(self):
        distributor.system._distributor_instance = None

    def on_tick(self):
        distributor.system._distributor_instance.process()
# okay decompiling data/sims4-not-yet-decompiled/simulation/distributor/distributor_service.pyc
