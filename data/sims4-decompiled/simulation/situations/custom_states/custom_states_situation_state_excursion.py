# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\custom_states\custom_states_situation_state_excursion.py
# Compiled at: 2020-04-10 03:07:21
# Size of source mod 2**32: 620 bytes
from situations.custom_states.custom_states_situation_states import CustomStatesSituationState
from snippets import define_snippet, EXCURSION_SITUATION_STATE

class ExcursionSituationState(CustomStatesSituationState):
    pass


TunableExcursionSituationStateReference, TunableExcursionSituationStateSnippet = define_snippet(EXCURSION_SITUATION_STATE, ExcursionSituationState.TunableFactory())
# okay decompiling data/sims4-not-yet-decompiled/simulation/situations/custom_states/custom_states_situation_state_excursion.pyc
