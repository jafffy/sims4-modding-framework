# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\bouncer\bouncer_client.py
# Compiled at: 2013-07-06 01:27:35
# Size of source mod 2**32: 2216 bytes


class IBouncerClient:

    def on_sim_assigned_to_request(self, sim, request):
        raise NotImplementedError

    def on_sim_unassigned_from_request(self, sim, request):
        raise NotImplementedError

    def on_sim_replaced_in_request(self, old_sim, new_sim, request):
        raise NotImplementedError

    def on_failed_to_spawn_sim_for_request(self, request):
        raise NotImplementedError

    def on_tardy_request(self, request):
        raise NotImplementedError

    def on_first_assignment_pass_completed(self):
        raise NotImplementedError
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/bouncer/bouncer_client.pyc
