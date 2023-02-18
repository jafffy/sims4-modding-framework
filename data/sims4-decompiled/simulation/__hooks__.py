# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\__hooks__.py
# Compiled at: 2019-02-22 02:35:20
# Size of source mod 2**32: 1365 bytes
RELOADER_ENABLED = False
__enable_gc_callback = True
import gc
try:
    import _profile
except:
    __enable_gc_callback = False

def system_init(gameplay):
    import sims4.importer
    sims4.importer.enable()
    print('Server Startup')
    if __enable_gc_callback:
        gc.callbacks.append(_profile.notify_gc_function)


def system_shutdown():
    global RELOADER_ENABLED
    import sims4.importer
    sims4.importer.disable()
    RELOADER_ENABLED = False
# okay decompiling data/sims4-not-yet-decompiled/simulation/__hooks__.pyc
