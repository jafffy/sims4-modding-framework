# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\lot_decoration\lot_decoration_mixins.py
# Compiled at: 2018-03-23 23:59:33
# Size of source mod 2**32: 1180 bytes
from sims4.tuning.tunable import OptionalTunable
from holidays.holiday_tunables import TunableHolidayVariant

class HolidayOrEverydayDecorationMixin:
    FACTORY_TUNABLES = {'_decoration_occasion': OptionalTunable(description='\n            The holiday this applies to.\n            If disabled, applies only to everyday decorations.\n            ',
                               tunable=TunableHolidayVariant(default='active_or_upcoming'),
                               enabled_by_default=True,
                               enabled_name='Holiday',
                               disabled_name='Everyday')}

    def occasion(self):
        if self._decoration_occasion is None:
            return
        return self._decoration_occasion()
# okay decompiling data/sims4-not-yet-decompiled/simulation/lot_decoration/lot_decoration_mixins.pyc
