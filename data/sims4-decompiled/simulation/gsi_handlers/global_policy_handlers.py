# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\gsi_handlers\global_policy_handlers.py
# Compiled at: 2019-01-10 23:00:34
# Size of source mod 2**32: 1424 bytes
from sims4.gsi.dispatcher import GsiHandler
from sims4.gsi.schema import GsiGridSchema
import services
global_policy_archive_schema = GsiGridSchema(label='Global Policy Log', auto_refresh=True)
global_policy_archive_schema.add_field('policy', label='Global Policy')
global_policy_archive_schema.add_field('progress_value', label='Progress Value')
global_policy_archive_schema.add_field('decay_days', label='Decay Days')
global_policy_archive_schema.add_field('progress_state', label='Progress State')

@GsiHandler('global_policy_log', global_policy_archive_schema)
def generate_global_policy_data():
    policy_data = []
    for policy in services.global_policy_service().get_global_policies():
        entry = {'policy':repr(policy).split('sims4.tuning.instances.', 1)[1].split('object', 1)[0], 
         'progress_value':str(policy.progress_value) + '/' + str(policy.progress_max_value), 
         'decay_days':0 if policy.decay_handler is None or policy.decay_handler.when is None else str(policy.decay_handler.when - services.time_service().sim_now), 
         'progress_state':str(policy.progress_state)}
        policy_data.append(entry)

    return policy_data
# okay decompiling data/sims4-not-yet-decompiled/simulation/gsi_handlers/global_policy_handlers.pyc
