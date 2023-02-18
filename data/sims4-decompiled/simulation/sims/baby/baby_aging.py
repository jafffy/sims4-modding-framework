# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\baby\baby_aging.py
# Compiled at: 2017-06-27 01:46:47
# Size of source mod 2**32: 1449 bytes
from interactions.aop import AffordanceObjectPair
from interactions.context import InteractionContext, InteractionSource, QueueInsertStrategy
from interactions.priority import Priority
from sims.aging.aging_element import ChangeAgeElement
import services, sims4.log
logger = sims4.log.Logger('Baby')

def baby_age_up(sim_info):
    bassinet = services.object_manager().get(sim_info.id)
    if bassinet is None:
        return
    middle_bassinet = bassinet.replace_for_age_up()
    if middle_bassinet is None:
        return

    def _on_spawn(sim):
        affordance = bassinet.get_age_up_addordance()
        aop = AffordanceObjectPair(affordance, middle_bassinet, affordance, None, is_baby_age_up=True)
        context = InteractionContext(sim, (InteractionSource.SCRIPT), (Priority.Critical), insert_strategy=(QueueInsertStrategy.NEXT))
        result = aop.test_and_execute(context)
        if not result:
            logger.error('Failed to run baby age up interaction: {}', result, owner='jjacobson')

    ChangeAgeElement.spawn_for_age_up(sim_info, (middle_bassinet.position), spawn_action=_on_spawn, sim_location=(middle_bassinet.location))
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/baby/baby_aging.pyc
