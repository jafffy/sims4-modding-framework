# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\server\config_service.py
# Compiled at: 2012-05-21 21:22:07
# Size of source mod 2**32: 924 bytes
from sims4.service_manager import Service
from sims4.tuning.tunable import TunableEnumEntry
from sims4.tuning.dynamic_enum import DynamicEnum

class ContentModes(DynamicEnum):
    PRODUCTION = 0
    DEMO = 1


class ConfigService(Service):
    DEFAULT_CONTENT_MODE = TunableEnumEntry(ContentModes, default=(ContentModes.PRODUCTION), description='Content mode that the server starts up in.')

    def __init__(self):
        self.content_mode = self.DEFAULT_CONTENT_MODE
# okay decompiling data/sims4-not-yet-decompiled/simulation/server/config_service.pyc
