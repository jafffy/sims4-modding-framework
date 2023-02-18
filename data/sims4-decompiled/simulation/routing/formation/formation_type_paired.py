# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\routing\formation\formation_type_paired.py
# Compiled at: 2018-10-24 16:56:03
# Size of source mod 2**32: 707 bytes
from protocolbuffers import Routing_pb2
from routing.formation.formation_type_base import FormationTypeBase, FormationRoutingType
from sims4.utils import classproperty

class FormationTypePaired(FormationTypeBase):

    @classproperty
    def routing_type():
        return FormationRoutingType.PARIED

    @property
    def slave_attachment_type(self):
        return Routing_pb2.SlaveData.SLAVE_PAIRED_CHILD
# okay decompiling data/sims4-not-yet-decompiled/simulation/routing/formation/formation_type_paired.pyc
