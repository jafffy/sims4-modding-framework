# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\objects\components\example.py
# Compiled at: 2013-10-18 00:16:53
# Size of source mod 2**32: 2175 bytes
from sims4.tuning.tunable import Tunable, TunableFactory
from objects.components import Component, componentmethod
from sims4.log import Logger
from objects.components.types import EXAMPLE_COMPONENT
logger = Logger('ExampleComponent')

class ExampleComponent(Component, component_name=EXAMPLE_COMPONENT):

    def __init__(self, owner, example_name):
        super().__init__(owner)
        self.example_name = example_name

    @componentmethod
    def example_component_method(self, prefix=''):
        logger.warn('{}self={} owner={} example_name={}', prefix, self, self.owner, self.example_name)

    def on_location_changed(self, old_location):
        self.example_component_method('on_location_changed: ')


class TunableExampleComponent(TunableFactory):
    FACTORY_TYPE = ExampleComponent

    def __init__(self, description='Example component, do not use on objects!', callback=None, **kwargs):
        (super().__init__)(example_name=Tunable(str, 'No name given.', description='Name to use to distinguish this component'), description=description, **kwargs)
# okay decompiling data/sims4-not-yet-decompiled/simulation/objects/components/example.pyc
