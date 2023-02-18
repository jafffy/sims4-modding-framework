# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\buffs\buff_element.py
# Compiled at: 2020-11-17 00:04:31
# Size of source mod 2**32: 2026 bytes
from buffs.tunable import TunablePackSafeBuffReference
from interactions import ParticipantTypeSim
from interactions.utils.interaction_elements import XevtTriggeredElement
import sims4.log
from sims4.tuning.tunable import TunableEnumEntry
logger = sims4.log.Logger('Buffs')

class BuffFireAndForgetElement(XevtTriggeredElement):

    @staticmethod
    def _verify_tunable_callback(cls, tunable_name, source, buff, participant, success_chance, timing):
        if buff.buff_type is None:
            return
        if buff.buff_type._temporary_commodity_info is None:
            logger.error('BuffFireAndForgetElement: {} has a buff element with a buff {} without a temporary commodity tuned.', cls, buff.buff_type)

    FACTORY_TUNABLES = {'buff':TunablePackSafeBuffReference(description='\n            A buff to be added to the Sim.\n            '), 
     'participant':TunableEnumEntry(description='\n            The Sim(s) to give the buff to.\n            ',
       tunable_type=ParticipantTypeSim,
       default=ParticipantTypeSim.Actor), 
     'verify_tunable_callback':_verify_tunable_callback}

    def _do_behavior(self, *args, **kwargs):
        if self.buff.buff_type is None:
            return
        participants = self.interaction.get_participants(self.participant)
        if not participants:
            logger.error('Got empty participants trying to run a BuffFireAndForgetElement element. Buff: {} Participant:{}', self, self.participant)
        for participant in participants:
            participant.add_buff_from_op((self.buff.buff_type), buff_reason=(self.buff.buff_reason))
# okay decompiling data/sims4-not-yet-decompiled/simulation/buffs/buff_element.pyc
