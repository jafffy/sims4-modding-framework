# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\reservation\reservation_handler_interlocked.py
# Compiled at: 2016-11-04 18:10:38
# Size of source mod 2**32: 2986 bytes
from reservation.reservation_handler import _ReservationHandler
from reservation.reservation_handler_uselist import ReservationHandlerUseList
from reservation.reservation_result import ReservationResult
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableVariant, TunableSet, TunableReference
import services, sims4.resources

class ReservationHandlerInterlocked(_ReservationHandler):

    class ReservationInterlockInteraction(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'affordance_whitelist': TunableSet(description='\n                The affordances that this reservation handler is compatible\n                with.\n                ',
                                   tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION))))}

        def allows_reservation(self, other_reservation_handler):
            if other_reservation_handler.reservation_interaction is None:
                return ReservationResult(False, '{} has no reserve interaction to interlock', other_reservation_handler,
                  result_obj=(other_reservation_handler.sim))
            affordance = other_reservation_handler.reservation_interaction.get_interaction_type()
            if affordance not in self.affordance_whitelist:
                return ReservationResult(False, '{} is not an allowed interlock affordance', (other_reservation_handler.reservation_interaction),
                  result_obj=(other_reservation_handler.sim))
            return ReservationResult.TRUE

    FACTORY_TUNABLES = {'interlock': TunableVariant(description='\n            Define how this handler interlocks with other reservation handlers.\n            ',
                    interaction=(ReservationInterlockInteraction.TunableFactory()),
                    default='interaction')}

    def allows_reservation(self, other_reservation_handler):
        if self.sim is other_reservation_handler.sim:
            return ReservationResult.TRUE
        if isinstance(other_reservation_handler, ReservationHandlerUseList):
            return ReservationResult.TRUE
        reserve_result = self.interlock.allows_reservation(other_reservation_handler)
        return reserve_result
# okay decompiling data/sims4-not-yet-decompiled/simulation/reservation/reservation_handler_interlocked.pyc
