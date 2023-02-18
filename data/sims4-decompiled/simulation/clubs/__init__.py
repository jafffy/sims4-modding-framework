# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\clubs\__init__.py
# Compiled at: 2018-08-21 21:23:05
# Size of source mod 2**32: 656 bytes
import services

class UnavailableClubError(Exception):
    pass


class UnavailableClubCriteriaError(Exception):
    pass


def on_sim_killed_or_culled(sim_info):
    club_service = services.get_club_service()
    if club_service is not None:
        club_service.on_sim_killed_or_culled(sim_info)
# okay decompiling data/sims4-not-yet-decompiled/simulation/clubs/__init__.pyc
