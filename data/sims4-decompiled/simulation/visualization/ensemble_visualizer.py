# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\visualization\ensemble_visualizer.py
# Compiled at: 2015-09-02 18:25:58
# Size of source mod 2**32: 1825 bytes
import math
from debugvis import Context
from sims4.color import pseudo_random_color
import services

class EnsembleVisualizer:

    def __init__(self, layer):
        self.layer = layer
        self._start()

    def _start(self):
        services.ensemble_service().on_ensemble_center_of_mass_changed.append(self._on_update)
        self._on_update()

    def stop(self):
        services.ensemble_service().on_ensemble_center_of_mass_changed.remove(self._on_update)

    def _on_update(self):
        with Context(self.layer) as (layer):
            for ensemble in services.ensemble_service().get_all_ensembles():
                color = pseudo_random_color(ensemble.guid)
                if ensemble.last_center_of_mass is None:
                    continue
                layer.add_circle((ensemble.last_center_of_mass), radius=(math.sqrt(ensemble.max_ensemble_radius)),
                  color=color)
                for sim in ensemble:
                    layer.add_circle((sim.position), radius=0.3,
                      color=color)
# okay decompiling data/sims4-not-yet-decompiled/simulation/visualization/ensemble_visualizer.pyc
