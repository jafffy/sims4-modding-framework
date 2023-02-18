# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\pools\pool_utils.py
# Compiled at: 2021-02-03 00:19:39
# Size of source mod 2**32: 832 bytes
from _weakrefset import WeakSet
import services, sims4.log, sims4.reload
logger = sims4.log.Logger('Pool Utils', default_owner='skorman')
with sims4.reload.protected(globals()):
    cached_pool_objects = WeakSet()
POOL_LANDING_SURFACE = 'Water'

def get_main_pool_objects_gen():
    yield from cached_pool_objects
    if False:
        yield None


def get_pool_by_block_id(block_id):
    for pool in get_main_pool_objects_gen():
        if pool.block_id == block_id:
            return pool

    logger.error('No Pool Matching block Id: {}', block_id, owner='camilogarcia')
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/pools/pool_utils.pyc
