# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\clans\__init__.py
# Compiled at: 2022-03-23 21:56:46
# Size of source mod 2**32: 377 bytes
import services

def on_sim_killed_or_culled(sim_info):
    clan_service = services.clan_service()
    if clan_service is not None:
        clan_service.on_sim_killed_or_culled(sim_info)
# okay decompiling data/sims4-not-yet-decompiled/simulation/clans/__init__.pyc
