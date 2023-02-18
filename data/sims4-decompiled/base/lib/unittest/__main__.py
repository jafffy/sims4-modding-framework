# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\unittest\__main__.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 490 bytes
import sys
if sys.argv[0].endswith('__main__.py'):
    import os.path
    executable = os.path.basename(sys.executable)
    sys.argv[0] = executable + ' -m unittest'
    del os
__unittest = True
from .main import main
main(module=None)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/unittest/__main__.pyc
