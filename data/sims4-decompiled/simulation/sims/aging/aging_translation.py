# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\aging\aging_translation.py
# Compiled at: 2021-09-13 21:15:06
# Size of source mod 2**32: 555 bytes


def sim_days_to_age_progress(sim_days, age_duration):
    return sim_days / age_duration


def age_progress_to_sim_days(age_progress, age_duration):
    return age_progress * age_duration
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/aging/aging_translation.pyc
