# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\scheduler_utils.py
# Compiled at: 2019-09-11 18:40:52
# Size of source mod 2**32: 1308 bytes
from sims4.tuning.tunable import TunableSingletonFactory, Tunable
from tunable_time import Days

def convert_string_to_enum(**day_availability_mapping):
    day_availability_dict = {}
    for day in Days:
        name = '{} {}'.format(int(day), day.name)
        available = day_availability_mapping[name]
        day_availability_dict[day] = available

    return day_availability_dict


class TunableAvailableDays(TunableSingletonFactory):
    FACTORY_TYPE = staticmethod(convert_string_to_enum)


def TunableDayAvailability():
    day_availability_mapping = {}
    for day in Days:
        name = '{} {}'.format(int(day), day.name)
        day_availability_mapping[name] = Tunable(bool, False)

    day_availability = TunableAvailableDays(description='Which days of the week to include', **day_availability_mapping)
    return day_availability
# okay decompiling data/sims4-not-yet-decompiled/simulation/scheduler_utils.pyc
