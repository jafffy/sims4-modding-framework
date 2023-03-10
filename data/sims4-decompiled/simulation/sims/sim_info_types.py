# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\sim_info_types.py
# Compiled at: 2022-04-28 16:47:50
# Size of source mod 2**32: 8431 bytes
from routing.portals.portal_tuning import PortalFlags
from sims4.common import Pack
from sims4.tuning.tunable import TunableEnumEntry, TunableList
from tag import Tag
import enum

class Species(enum.Int):
    INVALID = 0
    HUMAN = 1
    DOG = 2
    CAT = 3
    FOX = 5


class SpeciesExtended(Species):
    SMALLDOG = 4

    @staticmethod
    def get_animation_species_param(value):
        if value == SpeciesExtended.HUMAN:
            return 'human'
        if value == SpeciesExtended.DOG:
            return 'dog'
        if value == SpeciesExtended.CAT:
            return 'cat'
        if value == SpeciesExtended.FOX:
            return 'fox'
        if value == SpeciesExtended.SMALLDOG:
            return 'smalldog'
        return ''

    @staticmethod
    def get_species_from_animation_param(species):
        return SpeciesExtended(species.upper())

    @staticmethod
    def get_species(value):
        if value == SpeciesExtended.SMALLDOG:
            return Species.DOG
        return value

    @staticmethod
    def get_species_extended(value):
        if value == Species.HUMAN:
            return (
             SpeciesExtended.HUMAN,)
        if value == Species.CAT:
            return (
             SpeciesExtended.CAT,)
        if value == Species.DOG:
            return (
             SpeciesExtended.DOG, SpeciesExtended.SMALLDOG)
        if value == Species.FOX:
            return (
             SpeciesExtended.FOX,)
        return (
         value,)

    @staticmethod
    def is_age_valid_for_animation_cache(species, age):
        if species == SpeciesExtended.HUMAN:
            return age in Age.get_ages_for_animation_cache()
        return age in (Age.CHILD, Age.ADULT)

    @staticmethod
    def get_portal_flag(value):
        if value == SpeciesExtended.HUMAN:
            return PortalFlags.SPECIES_HUMAN
        if value == SpeciesExtended.DOG:
            return PortalFlags.SPECIES_DOG
        if value == SpeciesExtended.CAT:
            return PortalFlags.SPECIES_CAT
        if value == SpeciesExtended.FOX:
            return PortalFlags.SPECIES_FOX
        if value == SpeciesExtended.SMALLDOG:
            return PortalFlags.SPECIES_SMALLDOG
        return PortalFlags.DEFAULT

    @staticmethod
    def get_required_pack(value):
        if value == SpeciesExtended.DOG or value == SpeciesExtended.SMALLDOG or value == SpeciesExtended.CAT:
            return Pack.EP04
        if value == SpeciesExtended.FOX:
            return Pack.EP11


class Gender(enum.Int):
    MALE = 4096
    FEMALE = 8192

    @property
    def animation_gender_param(self):
        return self.name.lower()

    @staticmethod
    def get_opposite(value):
        if value == Gender.MALE:
            return Gender.FEMALE
        return Gender.MALE


class Age(enum.Int):
    BABY = 1
    TODDLER = 2
    CHILD = 4
    TEEN = 8
    YOUNGADULT = 16
    ADULT = 32
    ELDER = 64

    @classmethod
    def get_ages_for_animation_cache(cls):
        return (
         cls.ADULT, cls.CHILD, cls.TODDLER)

    @property
    def age_for_animation_cache(self):
        if self <= self.TODDLER:
            return self.TODDLER
        if self <= self.CHILD:
            return self.CHILD
        return self.ADULT

    @property
    def animation_age_param(self):
        return self.name.lower()

    @staticmethod
    def get_age_from_animation_param(age):
        return Age(age.upper())

    @staticmethod
    def get_portal_flag(value):
        if value == Age.TODDLER:
            return PortalFlags.AGE_TODDLER
        if value == Age.CHILD:
            return PortalFlags.AGE_CHILD
        if value in (Age.TEEN, Age.YOUNGADULT, Age.ADULT, Age.ELDER):
            return PortalFlags.AGE_TYAE
        return PortalFlags.DEFAULT


class SimInfoSpawnerTags:
    SIM_SPAWNER_TAGS = TunableList(description='\n        A list of tags for Sims to spawn when traveling and moving on/off lot.\n        Note: Tags are resolved in order until a spawn point has been found that\n        contains the tag.\n        ',
      tunable=TunableEnumEntry(tunable_type=Tag,
      default=(Tag.INVALID)))


class SimSerializationOption(enum.Int, export=False):
    UNDECLARED = 0
    LOT = 1
    OPEN_STREETS = 2


class SimZoneSpinUpAction(enum.Int, export=False):
    NONE = ...
    RESTORE_SI = ...
    PREROLL = ...
    PUSH_GO_HOME = ...
# okay decompiling data/sims4-not-yet-decompiled/simulation/sims/sim_info_types.pyc
