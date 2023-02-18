# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\outfits\outfit_generator.py
# Compiled at: 2022-02-02 17:28:41
# Size of source mod 2**32: 2773 bytes
import services, sims4
from sims.outfits.outfit_utils import OutfitGeneratorRandomizationMixin
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, TunableSet, TunableEnumWithFilter
from snippets import define_snippet
from tag import Tag
with sims4.reload.protected(globals()):
    outfit_change_log_enabled = False

class OutfitGenerator(OutfitGeneratorRandomizationMixin, HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'tags': TunableSet(description='\n            The set of tags used to generate the outfit. Parts must match the\n            specified tag in order to be valid for the generated outfit.\n            ',
               tunable=TunableEnumWithFilter(tunable_type=Tag,
               filter_prefixes=('Uniform', 'OutfitCategory', 'Style', 'Situation'),
               default=(Tag.INVALID),
               invalid_enums=(
              Tag.INVALID,),
               pack_safe=True))}

    def __call__(self, *args, outfit_extra_tag_set=None, **kwargs):
        tags = self.tags
        if outfit_extra_tag_set:
            tags = outfit_extra_tag_set.union(self.tags)
        (self._generate_outfit)(args, tag_list=tags, **kwargs)

    @staticmethod
    def generate_outfit(outfit_generator, sim_info, outfit_category, **kwargs):
        (outfit_generator.generator)(sim_info, outfit_category, **kwargs)


TunableOutfitGeneratorReference, TunableOutfitGeneratorSnippet = define_snippet('Outfit', OutfitGenerator.TunableFactory())
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/outfits/outfit_generator.pyc
