# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\whims\whim_loot_ops.py
# Compiled at: 2022-04-28 17:40:53
# Size of source mod 2**32: 3854 bytes
import services, sims4
from interactions.utils.loot_basic_op import BaseLootOperation, BaseTargetedLootOperation
from sims4.tuning.tunable import TunableVariant, TunableEnumSet, HasTunableSingletonFactory, AutoFactoryInit, TunableReference, Tunable
from whims.whims_tracker import WhimType
logger = sims4.log.Logger('WhimLootOperations')

class _RefreshWhimsOperation(HasTunableSingletonFactory, AutoFactoryInit):

    def __call__(self, subject, target, resolver, source_op):
        raise NotImplementedError


class _FilterByWhimType(_RefreshWhimsOperation):
    FACTORY_TUNABLES = {'_types_to_refresh': TunableEnumSet(description='\n            Refresh a subset of whims by their whim type.\n            ',
                            enum_type=WhimType,
                            enum_default=(WhimType.INVALID),
                            invalid_enums=(
                           WhimType.INVALID,),
                            minlength=1)}

    def __call__(self, subject, target, resolver, source_op):
        subject.whim_tracker.refresh_whims((self._types_to_refresh), allow_existing_whims=(source_op.allow_existing_whims))


class _RefreshAll(_RefreshWhimsOperation):

    def __call__(self, subject, target, resolver, source_op):
        subject.whim_tracker.refresh_whims(allow_existing_whims=(source_op.allow_existing_whims))


class RefreshWhimsLootOp(BaseLootOperation):
    FACTORY_TUNABLES = {'operation':TunableVariant(description='\n            The type of refresh operation to perform.\n            ',
       refresh_by_type=_FilterByWhimType.TunableFactory(),
       refresh_all=_RefreshAll.TunableFactory(),
       default='refresh_all'), 
     'allow_existing_whims':Tunable(description='\n            If there is a whim in the slot already, checking this\n            will allow that whim to be picked again when\n            refreshing.\n            ',
       tunable_type=bool,
       default=False)}

    def __init__(self, *args, operation, allow_existing_whims, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.operation = operation
        self.allow_existing_whims = allow_existing_whims

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject is None:
            logger.error('Subject {} is None for the loot {}..', self.subject, self)
            return
        if subject.whim_tracker is None:
            return
        self.operation(subject, target, resolver, source_op=self)


class PushWhimsetLootOp(BaseTargetedLootOperation):
    FACTORY_TUNABLES = {'whimset': TunableReference(description='\n            The whimset to push onto the sim.\n            ',
                  manager=(services.get_instance_manager(sims4.resources.Types.ASPIRATION)),
                  class_restrictions=('ObjectivelessWhimSet', ))}

    def __init__(self, *args, whimset, **kwargs):
        (super().__init__)(*args, **kwargs)
        self.whimset = whimset

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject is None:
            logger.error('Subject {} is None for the loot {}.', self.subject, self)
            return
        if subject.whim_tracker is None:
            return
        subject.whim_tracker.push_whimset(self.whimset, target)
# okay decompiling data/sims4-not-yet-decompiled/simulation/whims/whim_loot_ops.pyc
