# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\cython_utils.py
# Compiled at: 2021-02-23 21:06:48
# Size of source mod 2**32: 644 bytes
import cython, sims4.log
from postures.posture_specs import cython_log
from sims4.log import Logger
logger = Logger('CythonUtils')
if cython.compiled:
    cython_log.always('CYTHON cython_utils is imported!', color=(sims4.log.LEVEL_WARN))
else:
    cython_log.always('Pure Python cython_utils is imported!', color=(sims4.log.LEVEL_WARN))
if not cython.compiled:
    from cython_utils_ph import *
# okay decompiling data/sims4-not-yet-decompiled/simulation/cython_utils.pyc
