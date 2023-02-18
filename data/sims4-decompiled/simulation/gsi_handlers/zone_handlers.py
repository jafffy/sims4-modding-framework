# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gsi_handlers\zone_handlers.py
# Compiled at: 2014-04-14 22:29:07
# Size of source mod 2**32: 623 bytes
import services
from sims4.gsi.dispatcher import GsiHandler
from sims4.gsi.schema import GsiSchema
zone_view_schema = GsiSchema()
zone_view_schema.add_field('zoneId')

@GsiHandler('zone_view', zone_view_schema)
def generate_zone_view_data():
    zone_list = []
    for zone in services._zone_manager.objects:
        if zone.is_instantiated:
            zone_list.append({'zoneId':hex(zone.id),  'zoneName':'ZoneName'})

    return zone_list
# okay decompiling data/sims4-not-yet-decompiled/simulation/gsi_handlers/zone_handlers.pyc
