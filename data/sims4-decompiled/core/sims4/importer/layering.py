# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\importer\layering.py
# Compiled at: 2013-11-06 00:41:02
# Size of source mod 2**32: 1616 bytes
import caches, paths, sims4.log
logger = sims4.log.Logger('Layering')

@caches.cached
def _get_file_layer(filename):
    if paths.LAYERS is not None:
        for i, v in enumerate(paths.LAYERS):
            if filename.startswith(v):
                return i


def check_import(initiating_file, target_file):
    if initiating_file is None or target_file is None or paths.IS_ARCHIVE:
        return
    initiating_layer = _get_file_layer(initiating_file)
    target_layer = _get_file_layer(target_file)
    if initiating_layer is None or target_layer is None:
        return
    if target_layer > initiating_layer:
        logger.error('LAYERING VIOLATION:\n  {}\nimports\n  {}\n\nThings in\n  {}\\*\nshould not import from\n  {}\\*', initiating_file, target_file, paths.LAYERS[initiating_layer], paths.LAYERS[target_layer])
# okay decompiling data/sims4-not-yet-decompiled/core/sims4/importer/layering.pyc
