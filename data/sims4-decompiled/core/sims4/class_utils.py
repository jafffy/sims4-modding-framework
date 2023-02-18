# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\class_utils.py
# Compiled at: 2017-12-11 22:01:36
# Size of source mod 2**32: 735 bytes
import builtins, sys
from caches import cached
import sims4.log
logger = sims4.log.Logger('Utils')

@cached
def find_class(path, class_name):
    builtins.__import__(path)
    module = sys.modules[path]
    cls = module
    try:
        for attr in class_name.split('.'):
            cls = getattr(cls, attr)

    except AttributeError:
        logger.error('{} object has no attribute {}', cls, attr)
        return
    else:
        return cls
# okay decompiling data/sims4-not-yet-decompiled/core/sims4/class_utils.pyc
