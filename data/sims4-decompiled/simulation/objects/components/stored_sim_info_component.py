# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\stored_sim_info_component.py
# Compiled at: 2022-05-20 18:44:00
# Size of source mod 2**32: 12463 bytes
import tag
from event_testing.resolver import SingleActorAndObjectResolver
from event_testing.test_events import TestEvent
from objects.object_enums import ResetReason
from protocolbuffers import SimObjectAttributes_pb2 as protocols
from interactions import ParticipantType
from interactions.utils.interaction_elements import XevtTriggeredElement
from interactions.utils.loot_basic_op import BaseTargetedLootOperation, BaseLootOperation
from interactions.utils.loot_ops import RemoveTraitLootOp
from objects.components import Component, types, componentmethod_with_fallback
from sims.sim_info_name_data import SimInfoNameData
from sims4.tuning.tunable import AutoFactoryInit, HasTunableFactory, TunableEnumEntry, OptionalTunable, Tunable, TunableList, TunableVariant, TunableMapping
import services, sims4, zone_types
logger = sims4.log.Logger('Stored Sim Info Component', default_owner='shipark')

class TransferStoredSimInfo(BaseTargetedLootOperation):
    FACTORY_TUNABLES = {'clear_stored_sim_on_subject': Tunable(description='\n            If set to False, the Stored Sim will remain on the subject object. If\n            set to True, the Store Sim will be removed from the subject object.\n            ',
                                      tunable_type=bool,
                                      default=False)}

    def __init__(self, *args, clear_stored_sim_on_subject=None, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._clear_stored_sim_on_subject = clear_stored_sim_on_subject

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject is None:
            logger.error("The Transfer Stored Sim Info loot tuned on: '{}' has a subject participant of None value.", self)
            return
        stored_sim_info = subject.get_component(types.STORED_SIM_INFO_COMPONENT)
        if stored_sim_info is None:
            logger.error("The Transfer Stored Sim Info loot tuned on interaction: '{}' has a subject with no Stored Sim Info Component.", self)
            return
        if target is None:
            logger.error("The Transfer Stored Sim Info loot tuned on interaction: '{}' has a target participant of None value.", self)
            return
        if target.has_component(types.STORED_SIM_INFO_COMPONENT):
            target.remove_component(types.STORED_SIM_INFO_COMPONENT)
        target.add_dynamic_component((types.STORED_SIM_INFO_COMPONENT), sim_id=(stored_sim_info.get_stored_sim_id()))
        if self._clear_stored_sim_on_subject:
            subject.remove_component(types.STORED_SIM_INFO_COMPONENT)


class StoreSimInfoLootOp(BaseTargetedLootOperation):

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject is None or target is None:
            logger.error('Trying to run Store Sim Info loot action with a None Subject and/or Target. subject:{}, target:{}', subject, target)
            return
        else:
            target.is_sim or logger.error('Trying to run Store Sim Info loot action on Subject {} with a non Sim Target {}', subject, target)
            return
        if subject.has_component(types.STORED_SIM_INFO_COMPONENT):
            subject.remove_component(types.STORED_SIM_INFO_COMPONENT)
        subject.add_dynamic_component((types.STORED_SIM_INFO_COMPONENT), sim_id=(target.sim_id))


class RemoveSimInfoLootOp(BaseLootOperation):

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject is None:
            logger.error('Trying to run Remove Stored Sim Info loot action with a None Subject')
            return
        if subject.has_component(types.STORED_SIM_INFO_COMPONENT):
            subject.remove_component(types.STORED_SIM_INFO_COMPONENT)


class StoreSimElement(XevtTriggeredElement, HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'description':'\n            An element that retrieves an interaction participant and attaches\n            its information to another interaction participant using a dynamic\n            StoredSimInfoComponent.\n            ', 
     'source_participant':OptionalTunable(description='\n            Specify what participant to store on the destination participant.\n            ',
       tunable=TunableEnumEntry(description='\n                The participant of this interaction whose Sim Info is retrieved\n                to be stored as a component.\n                ',
       tunable_type=ParticipantType,
       default=(ParticipantType.PickedObject)),
       enabled_name='specific_participant',
       disabled_name='no_participant'), 
     'destination_participant':TunableEnumEntry(description='\n            The participant of this interaction to which a\n            StoredSimInfoComponent is added, with the Sim Info of\n            source_participant.\n            ',
       tunable_type=ParticipantType,
       default=ParticipantType.Object)}

    def _do_behavior(self):
        source = self.interaction.get_participant(participant_type=(self.source_participant)) if self.source_participant is not None else None
        destination = self.interaction.get_participant(participant_type=(self.destination_participant))
        if destination.has_component(types.STORED_SIM_INFO_COMPONENT):
            destination.remove_component(types.STORED_SIM_INFO_COMPONENT)
        if source is not None:
            destination.add_dynamic_component((types.STORED_SIM_INFO_COMPONENT), sim_id=(source.id))


class StoredSimInfoComponent(Component, component_name=types.STORED_SIM_INFO_COMPONENT, allow_dynamic=True, persistence_key=protocols.PersistenceMaster.PersistableData.StoredSimInfoComponent):
    LOOTS_ON_OBJECT_REMOVE = TunableMapping(description='\n        A mapping of object tag to loots. A list of loots will be apply to the object \n        that has the stored sim component when the object is removed.\n        ',
      key_type=TunableEnumEntry(description='\n            what object to run loots.\n            ',
      tunable_type=(tag.Tag),
      default=(tag.Tag.INVALID),
      pack_safe=True),
      value_type=TunableList(description='\n            loots to apply to the object when object is removed.\n            ',
      tunable=TunableVariant(description='\n                A specific loot to apply.\n                ',
      remove_trait=(RemoveTraitLootOp.TunableFactory()))))

    def __init__(self, *args, sim_id=None, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._sim_id = sim_id
        self._sim_info_name_data = None

    def save(self, persistence_master_message):
        persistable_data = protocols.PersistenceMaster.PersistableData()
        persistable_data.type = protocols.PersistenceMaster.PersistableData.StoredSimInfoComponent
        stored_sim_info_component_data = persistable_data.Extensions[protocols.PersistableStoredSimInfoComponent.persistable_data]
        stored_sim_info_component_data.sim_id = self._sim_id
        if self._sim_info_name_data is not None:
            stored_sim_info_component_data.sim_info_name_data = SimInfoNameData.generate_sim_info_name_data_msg((self._sim_info_name_data), use_profanity_filter=False)
        persistence_master_message.data.extend([persistable_data])

    def load(self, persistable_data):
        stored_sim_info_component_data = persistable_data.Extensions[protocols.PersistableStoredSimInfoComponent.persistable_data]
        self._sim_id = stored_sim_info_component_data.sim_id
        if stored_sim_info_component_data.sim_info_name_data:
            sim_info_data = stored_sim_info_component_data.sim_info_name_data
            self._sim_info_name_data = SimInfoNameData(sim_info_data.gender, sim_info_data.first_name, sim_info_data.last_name, sim_info_data.full_name_key)

    def on_add(self, *_, **__):
        services.current_zone().register_callback(zone_types.ZoneState.HOUSEHOLDS_AND_SIM_INFOS_LOADED, self._on_households_loaded)

    def _apply_loots_on_object_remove(self):
        if self.LOOTS_ON_OBJECT_REMOVE is None:
            return
        sim_info = services.sim_info_manager().get(self._sim_id)
        if sim_info is None:
            return
        resolver = SingleActorAndObjectResolver(sim_info, (self.owner), source=self)
        owner_tags = self.owner.get_tags()
        for tag, loots in self.LOOTS_ON_OBJECT_REMOVE.items():
            if tag in owner_tags:
                for loot in loots:
                    loot.apply_to_resolver(resolver)

    def on_reset_component_get_interdependent_reset_records(self, reset_reason, reset_records):
        if reset_reason == ResetReason.BEING_DESTROYED:
            if services.current_zone().is_zone_running:
                self._apply_loots_on_object_remove()

    def _on_households_loaded(self, *_, **__):
        if self._sim_info_name_data is None:
            sim_info = services.sim_info_manager().get(self._sim_id)
            if sim_info is not None:
                self._sim_info_name_data = sim_info.get_name_data()
        self.owner.update_object_tooltip()

    @componentmethod_with_fallback((lambda: None))
    def get_stored_sim_id(self):
        return self._sim_id

    @componentmethod_with_fallback((lambda: None))
    def get_stored_sim_info(self):
        return services.sim_info_manager().get(self._sim_id)

    @componentmethod_with_fallback((lambda: None))
    def get_stored_sim_info_or_name_data(self):
        sim_info = services.sim_info_manager().get(self._sim_id)
        if sim_info is not None:
            return sim_info
        return self._sim_info_name_data

    @componentmethod_with_fallback((lambda: None))
    def get_stored_sim_name_data(self):
        return self._sim_info_name_data

    def has_stored_data(self):
        return self._sim_info_name_data is not None

    def component_interactable_gen(self):
        yield self
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/stored_sim_info_component.pyc
