# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\decimal.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 331 bytes
try:
    from _decimal import *
    from _decimal import __doc__
    from _decimal import __version__
    from _decimal import __libmpdec_version__
except ImportError:
    from _pydecimal import *
    from _pydecimal import __doc__
    from _pydecimal import __version__
    from _pydecimal import __libmpdec_version__
# okay decompiling data/sims4-not-yet-decompiled/base/lib/decimal.pyc
