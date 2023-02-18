# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\temple\temple_utils.py
# Compiled at: 2022-05-09 23:29:46
# Size of source mod 2**32: 837 bytes
import services

class TempleUtils:

    @classmethod
    def get_temple_zone_director(cls):
        venue_service = services.venue_service()
        if venue_service is None:
            return
        zone_director = venue_service.get_zone_director()
        if hasattr(zone_director, '_temple_data'):
            return zone_director
# okay decompiling data/sims4-not-yet-decompiled/simulation/temple/temple_utils.pyc
