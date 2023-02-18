# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\postures\generic_posture_node.py
# Compiled at: 2018-10-29 23:13:01
# Size of source mod 2**32: 520 bytes
from objects.proxy import ProxyObject

class SimPostureNode(ProxyObject):

    def __str__(self):
        return 'Generic Sim Node ' + str(self._proxied_obj)

    @property
    def sim_proxied(self):
        return self._proxied_obj
# okay decompiling data/sims4-not-yet-decompiled/simulation/postures/generic_posture_node.pyc
