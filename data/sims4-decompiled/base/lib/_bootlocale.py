# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\_bootlocale.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1847 bytes
import sys, _locale
if sys.platform.startswith('win'):

    def getpreferredencoding(do_setlocale=True):
        if sys.flags.utf8_mode:
            return 'UTF-8'
        return _locale._getdefaultlocale()[1]


else:
    try:
        _locale.CODESET
    except AttributeError:
        if hasattr(sys, 'getandroidapilevel'):

            def getpreferredencoding(do_setlocale=True):
                return 'UTF-8'


        else:

            def getpreferredencoding(do_setlocale=True):
                if sys.flags.utf8_mode:
                    return 'UTF-8'
                import locale
                return locale.getpreferredencoding(do_setlocale)


    else:

        def getpreferredencoding(do_setlocale=True):
            if sys.flags.utf8_mode:
                return 'UTF-8'
            result = _locale.nl_langinfo(_locale.CODESET)
            if not result:
                if sys.platform == 'darwin':
                    result = 'UTF-8'
            return result
# okay decompiling data/sims4-not-yet-decompiled/base/lib/_bootlocale.pyc
