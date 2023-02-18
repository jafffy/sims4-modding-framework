# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\postures\posture_validators.py
# Compiled at: 2016-02-19 01:15:02
# Size of source mod 2**32: 2071 bytes
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableVariant, TunableReference
import services, sims4.resources

class _PostureValidator(HasTunableSingletonFactory, AutoFactoryInit):

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__dict__)


class PostureValidatorTest(_PostureValidator):
    FACTORY_TUNABLES = {'test_set': TunableReference(description="\n            This test set is provided with a DoubleSimResolver. The Actor\n            participant is the transitioning Sim. The Object/TargetSim\n            participant is the posture container we're testing against.\n            \n            Should the test fail, the posture transition is deemed invalid and\n            is discarded.\n            ",
                   manager=(services.get_instance_manager(sims4.resources.Types.SNIPPET)),
                   class_restrictions=('TestSetInstance', ))}

    def __call__(self, resolver):
        return self.test_set(resolver)


class TunablePostureValidatorVariant(TunableVariant):

    def __init__(self, *args, **kwargs):
        (super().__init__)(args, test=PostureValidatorTest.TunableFactory(), 
         default='test', **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/postures/posture_validators.pyc
