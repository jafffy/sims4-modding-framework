# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\bucks\bucks_telemetry.py
# Compiled at: 2020-03-16 19:09:28
# Size of source mod 2**32: 697 bytes
import sims4.telemetry
TELEMETRY_GROUP_BUCKS = 'CRNC'
TELEMETRY_HOOK_BUCKS_GAIN = 'GAIN'
TELEMETRY_HOOK_BUCKS_SPEND = 'SPND'
TELEMETRY_FIELD_BUCKS_TYPE = 'type'
TELEMETRY_FIELD_BUCKS_AMOUNT = 'amnt'
TELEMETRY_FIELD_BUCKS_TOTAL = 'totl'
TELEMETRY_FIELD_BUCKS_SOURCE = 'srce'
bucks_telemetry_writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_BUCKS)
TELEMETRY_GROUP_PERKS = 'PERK'
TELEMETRY_HOOK_PERKS_GAIN = 'GAIN'
TELEMETRY_HOOK_PERKS_REFUND = 'RFND'
perks_telemetry_writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_PERKS)
# okay decompiling data/sims4-not-yet-decompiled/simulation/bucks/bucks_telemetry.pyc
