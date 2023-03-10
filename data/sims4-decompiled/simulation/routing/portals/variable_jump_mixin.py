# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\portals\variable_jump_mixin.py
# Compiled at: 2020-02-19 21:54:25
# Size of source mod 2**32: 1629 bytes
import services, sims4
from animation.animation_utils import StubActor
from protocolbuffers import Routing_pb2 as routing_protocols
from sims4.tuning.tunable import TunableReference

class _VariableJumpMixin:
    FACTORY_TUNABLES = {'animation_element': TunableReference(description='\n            The animation to play when a Sim traverses this portal.\n            ',
                            manager=(services.get_instance_manager(sims4.resources.Types.ANIMATION)))}

    def _add_variable_jump_portal_data(self, actor, portal_instance, is_mirrored, walkstyle):
        arb = self._get_arb(actor, portal_instance, is_mirrored=is_mirrored)
        op = routing_protocols.RouteAnimateData()
        op.arb_data = arb._bytes()
        node_data = routing_protocols.RouteNodeData()
        node_data.type = routing_protocols.RouteNodeData.DATA_ANIMATE
        node_data.data = op.SerializeToString()
        return node_data

    def _get_variable_jump_portal_duration(self, portal_instance, is_mirrored, species):
        actor = StubActor(1, species=species)
        arb = self._get_arb(actor, portal_instance, is_mirrored=is_mirrored)
        _, duration, _ = arb.get_timing()
        return duration

    def _get_arb(self, actor, portal_instance, *, is_mirrored):
        raise NotImplementedError
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/portals/variable_jump_mixin.pyc
