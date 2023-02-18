# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\autonomy_marker_component.py
# Compiled at: 2019-09-24 01:22:29
# Size of source mod 2**32: 529 bytes
from objects.components import Component, types
from sims4.tuning.tunable import HasTunableFactory
import services

class AutonomyMarkerComponent(Component, HasTunableFactory, component_name=types.AUTONOMY_MARKER_COMPONENT):

    def on_remove(self):
        services.current_zone().clear_autonomy_area()
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/autonomy_marker_component.pyc
