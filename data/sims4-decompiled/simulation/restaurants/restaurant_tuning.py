# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\restaurants\restaurant_tuning.py
# Compiled at: 2021-07-16 02:00:41
# Size of source mod 2**32: 32921 bytes
from autonomy.autonomy_preference import TunableAutonomyPreference
from business.business_enums import BusinessAdvertisingType
from business.business_funds import BusinessFundsCategory
from crafting.recipe_enums import RecipeDifficulty
from sims.outfits.outfit_enums import OutfitCategory
from sims4.localization import TunableLocalizedString
from sims4.tuning.dynamic_enum import DynamicEnum
from sims4.tuning.geometric import TunableCurve
from sims4.tuning.tunable import TunableMapping, TunableEnumEntry, TunableSet, TunableReference, TunableList, TunablePackSafeResourceKey, TunableEnumWithFilter, TunableTuple, TunableResourceKey, TunablePackSafeReference, TunablePercent, Tunable, TunableRange
from sims4.tuning.tunable_base import ExportModes, EnumBinaryExportType
from tag import Tag
from ui.ui_dialog_notification import TunableUiDialogNotificationSnippet
import enum, services, sims4

def get_restaurant_zone_director():
    venue_service = services.venue_service()
    return venue_service is None or venue_service.venue_is_type(RestaurantTuning.RESTAURANT_VENUE) or None
    return venue_service.get_zone_director()


class MenuPresets(DynamicEnum):
    CUSTOMIZE = 0


class RestaurantOutfitType(enum.Int, export=False):
    MALE_CHEF = 0
    FEMALE_CHEF = 1
    MALE_WAITSTAFF = 2
    FEMALE_WAITSTAFF = 3
    MALE_HOST = 4
    FEMALE_HOST = 5


class RestaurantIngredientQualityType(DynamicEnum):
    INVALID = 0


class RestaurantTuning:
    MENU_PRESETS = TunableMapping(description='\n        The map to tune preset of menus that player to select to use in\n        restaurant customization.\n        ',
      key_type=TunableEnumEntry(tunable_type=MenuPresets,
      default=(MenuPresets.CUSTOMIZE),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_type=TunableTuple(description='\n            Menu preset contents.\n            ',
      preset_name=TunableLocalizedString(description='\n                Menu preset name that appear in both menu customize UI and in\n                game menu UI.\n                '),
      recipe_map=TunableMapping(description="\n                The map that represent a menu preset. It's organized with courses\n                like drink, appetizer, entree etc, and in each course there are\n                options of recipes.\n                ",
      key_type=TunableEnumWithFilter(tunable_type=Tag,
      filter_prefixes=[
     'recipe_course'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True,
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_type=TunableSet(tunable=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.RECIPE)),
      class_restrictions=('Recipe', ),
      pack_safe=True)),
      key_name='course_tags',
      value_name='recipes',
      tuple_name='MenuCourseMappingTuple'),
      show_in_restaurant_menu=Tunable(description="\n                If this is enabled, this menu preset will show up on restaurant\n                menus. If not, it won't. Currently, only home-chef menus\n                shouldn't show up on restaurant menus.\n                ",
      tunable_type=bool,
      default=True),
      export_class_name='MenuPresetContentTuple'),
      key_name='preset_enum',
      value_name='preset_contents',
      tuple_name='MenuPresetMappingTuple',
      export_modes=(ExportModes.All))
    MENU_TAG_DISPLAY_CONTENTS = TunableMapping(description='\n        The map to tune menu tags to display contents.\n        ',
      key_type=TunableEnumWithFilter(tunable_type=Tag,
      filter_prefixes=[
     'recipe'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True,
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_type=TunableTuple(description='\n            menu tag display contents.\n            ',
      menu_tag_name=(TunableLocalizedString()),
      menu_tag_icon=TunableResourceKey(description='\n                This will display as the filter icon in the course recipe picker UI.\n                ',
      resource_types=(sims4.resources.CompoundTypes.IMAGE)),
      export_class_name='MenuTagDisplayTuple'),
      key_name='menu_tags',
      value_name='menu_tag_display_contents',
      tuple_name='MenuTagDisplayMappingTuple',
      export_modes=(ExportModes.ClientBinary))
    COURSE_SORTING_SEQUENCE = TunableSet(description='\n        This set determines the sorting sequence for courses in both menu\n        customize UI and in game menu UI.\n        ',
      tunable=TunableEnumWithFilter(tunable_type=Tag,
      filter_prefixes=[
     'recipe_course'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True,
      binary_type=(EnumBinaryExportType.EnumUint32)),
      export_modes=(ExportModes.ClientBinary))
    DAILY_SPECIAL_DISCOUNT = TunablePercent(description='\n        The percentage of the base price when an item is the daily special.\n        For example, if the base price is $10 and this is tuned to 80%, the\n        discounted price will be $10 x 80% = $8\n        ',
      default=80)
    INVALID_DAILY_SPECIAL_RECIPES = TunableList(description='\n        A list of recipes that should not be considered for daily specials.\n        i.e. Glass of water.\n        ',
      tunable=TunableReference(description='\n            The recipe to disallow from being a daily special.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.RECIPE)),
      class_restrictions=('Recipe', ),
      pack_safe=True))
    COURSE_TO_FILTER_TAGS_MAPPING = TunableMapping(description='\n        Mapping from course to filter tags for food picker UI.\n        ',
      key_type=TunableEnumWithFilter(description='\n            The course associated with the list of filters.\n            ',
      tunable_type=Tag,
      filter_prefixes=[
     'recipe_course'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True,
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_type=TunableList(description='\n            This list of filter tags for the food picker UI for the course\n            specified.\n            ',
      tunable=TunableEnumWithFilter(tunable_type=Tag,
      filter_prefixes=[
     'recipe_category'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True,
      binary_type=(EnumBinaryExportType.EnumUint32))),
      key_name='course_key',
      value_name='course_filter_tags',
      tuple_name='CourseToFilterTuple',
      export_modes=(ExportModes.ClientBinary))
    CUSTOMER_QUALITY_STAT = TunablePackSafeReference(description='\n        The Customer Quality stat applied to food/drink the restaurant customer\n        eats/drinks. This is how we apply buffs to the Sim at the time they\n        consume the food/drink.\n        \n        The Customer Quality value is determined by multiplying the Final\n        Quality To Customer Quality Multiplier (found in Final Quality State\n        Data Mapping) by the Food Difficulty To Customer Quality Multiplier\n        (found in the Ingredient Quality State Data Mapping).\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)))
    CUSTOMER_VALUE_STAT = TunablePackSafeReference(description='\n        The Customer Value stat applied to food/drink the restaurant customer\n        eats/drinks. This is how we apply buffs to the Sim at the time they\n        consume the food/drink.\n        \n        The Customer Value value is determined by multiplying the Final Quality\n        To Customer Value Multiplier (found in Final Quality State Data Mapping)\n        by the Markup To Customer Value Multiplier (found in the Markup Data\n        Mapping).\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)))
    RECIPE_DIFFICULTY_DATA_MAPPING = TunableMapping(description='\n        A mapping of the recipe difficulty for restaurants to the appropriate\n        data.\n        ',
      key_name='recipe_difficulty',
      key_type=TunableEnumEntry(description="\n            The recipe difficulty for chef's at a restaurant.\n            ",
      tunable_type=RecipeDifficulty,
      default=(RecipeDifficulty.NORMAL)),
      value_name='recipe_difficulty_data',
      value_type=TunableTuple(description='\n            The tuning associated with the provided recipe difficulty.\n            ',
      recipe_difficulty_to_final_quality_adder=Tunable(description='\n                This value is added to the Ingredient Quality To Final Quality Adder\n                and the Cooking Speed To Final Quality Adder to determine the player-\n                facing recipe quality.\n                ',
      tunable_type=float,
      default=0),
      recipe_difficulty_to_customer_quality_multiplier=Tunable(description="\n                This value is multiplied by the Final Quality To Customer\n                Quality Multiplier to determine the customer's perceived quality\n                of the recipe.\n                ",
      tunable_type=float,
      default=1)))
    DEFAULT_INGREDIENT_QUALITY = TunableEnumEntry(description='\n        The default ingredient quality for a restaurant.\n        ',
      tunable_type=RestaurantIngredientQualityType,
      default=(RestaurantIngredientQualityType.INVALID),
      invalid_enums=(
     RestaurantIngredientQualityType.INVALID,))
    INGREDIENT_QUALITY_DATA_MAPPING = TunableMapping(description='\n        The mapping between ingredient enum and the ingredient data for\n        that type.\n        ',
      key_type=TunableEnumEntry(description='\n            The ingredient type. Organic, normal, lousy, etc...\n            ',
      tunable_type=RestaurantIngredientQualityType,
      default=(RestaurantIngredientQualityType.INVALID),
      invalid_enums=(
     RestaurantIngredientQualityType.INVALID,),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_type=TunableTuple(description='\n            Data associated with this type of ingredient.\n            ',
      ingredient_quality_type_name=TunableLocalizedString(description='\n                The localized name of this ingredient used in various places in\n                the UI.\n                '),
      ingredient_quality_to_final_quality_adder=Tunable(description='\n                This value is added to the Recipe Difficulty To Final Quality\n                Adder and the Cooking Speed To Final Quality Adder to determine\n                the player-facing recipe quality.\n                ',
      tunable_type=float,
      default=0),
      ingredient_quality_to_restaurant_expense_multiplier=TunableRange(description='\n                This value is multiplied by the Base Restaurant Price (found in\n                the Recipe tuning) for each recipe served to determine what the\n                cost is to the restaurant for preparing that recipe.\n                ',
      tunable_type=float,
      default=0.5,
      minimum=0),
      export_class_name='IngredientDataTuple'),
      key_name='ingredient_enum',
      value_name='ingredient_data',
      tuple_name='IngredientEnumDataMappingTuple',
      export_modes=(ExportModes.All))
    COOKING_SPEED_DATA_MAPPING = TunableMapping(description='\n        A mapping from chef cooking speed to the data associated with that\n        cooking speed.\n        ',
      key_name='cooking_speed_buff',
      key_type=TunableReference(description='\n            The cooking speed buff that is applied to the chef.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
      pack_safe=True),
      value_name='cooking_speed_data',
      value_type=TunableTuple(description='\n            The data associated with the tuned cooking speed.\n            ',
      cooking_speed_to_final_quality_adder=Tunable(description='\n                This value is added to the Recipe Difficulty To Final Quality\n                Adder and the Ingredient Quality To Final Quality Adder to\n                determine the player-facing recipe quality.\n                ',
      tunable_type=float,
      default=0),
      active_cooking_states_delta=Tunable(description='\n                The amount by which to adjust the number of active cooking\n                states the chef must complete before completing the order. For\n                instance, if a -1 is tuned here, the chef will have to complete\n                one less state than normal. Regardless of how the buffs are\n                tuned, the chef will always run at least one state before\n                completing the order.\n                ',
      tunable_type=int,
      default=(-1))))
    CHEF_SKILL_TO_FOOD_FINAL_QUALITY_ADDER_DATA = TunableTuple(description='\n        Pairs a skill with a curve to determine the additional value to add to\n        the final quality of a food made at an owned restaurant.\n        ',
      skill=TunablePackSafeReference(description='\n            The skill used to determine the adder for the final quality of food.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('Skill', )),
      final_quality_adder_curve=TunableCurve(description="\n            Maps the chef's current level of the tuned skill to a value that\n            will be added to the final quality statistic for food recipes cooked\n            at an owned restaurant.\n            ",
      x_axis_name='Skill Level',
      y_axis_name='Food Final Quality Adder'))
    CHEF_SKILL_TO_DRINK_FINAL_QUALITY_ADDER_DATA = TunableTuple(description='\n        Pairs a skill with a curve to determine the additional value to add to\n        the final quality of a drink made at an owned restaurant.\n        ',
      skill=TunablePackSafeReference(description='\n            The skill used to determine the adder for the final quality of drinks.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.STATISTIC)),
      class_restrictions=('Skill', )),
      final_quality_adder_curve=TunableCurve(description="\n            Maps the chef's current level of the tuned skill to a value that\n            will be added to the final quality statistic for drink recipes\n            cooked at an owned restaurant.\n            ",
      x_axis_name='Skill Level',
      y_axis_name='Food Final Quality Adder'))
    FINAL_QUALITY_STATE_DATA_MAPPING = TunableMapping(description='\n        A mapping of final quality recipe states (Poor, Normal, Outstanding) to\n        the data associated with that recipe quality.\n        ',
      key_name='recipe_quality_state',
      key_type=TunableReference(description='\n            The recipe quality state value.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
      class_restrictions='ObjectStateValue',
      pack_safe=True),
      value_name='recipe_quality_state_value_data',
      value_type=TunableTuple(description='\n            The data associated with the tuned recipe quality state value.\n            ',
      final_quality_to_customer_quality_multiplier=Tunable(description='\n                This value is multiplied by the Recipe Difficulty To Customer\n                Quality Multiplier to determine the Customer Quality State value\n                of the recipe.\n                ',
      tunable_type=float,
      default=1),
      final_quality_to_customer_value_multiplier=Tunable(description='\n                This value is multiplied by the Markup To Customer Value\n                Multiplier to determine the value of the Customer Value Stat\n                value of the recipe.\n                ',
      tunable_type=float,
      default=1)))
    PRICE_MARKUP_DATA_MAPPING = TunableMapping(description='\n        A mapping of the current price markup of the restaurant to the data\n        associated with that markup.\n        ',
      key_name='markup_multiplier',
      key_type=Tunable(description='\n            The markup multiplier. this needs to be in line with the available\n            markups tuned on the restaurant business.\n            ',
      tunable_type=float,
      default=1.5),
      value_name='markup_multiplier_data',
      value_type=TunableTuple(description='\n            The data associated with the tuned markup multiplier.\n            ',
      markup_to_customer_value_multiplier=Tunable(description='\n                ',
      tunable_type=float,
      default=1)))
    BUSINESS_FUNDS_CATEGORY_FOR_COST_OF_INGREDIENTS = TunableEnumEntry(description='\n        When a Chef cooks an order, the restaurant has to pay for the\n        ingredients. This is the category for those expenses.\n        ',
      tunable_type=BusinessFundsCategory,
      default=(BusinessFundsCategory.NONE),
      invalid_enums=(
     BusinessFundsCategory.NONE,))
    ATTIRE = TunableList(description='\n        List of attires player can select to apply to the restaurant.\n        ',
      tunable=TunableEnumEntry(tunable_type=OutfitCategory,
      default=(OutfitCategory.EVERYDAY),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      export_modes=(ExportModes.All))
    UNIFORM_CHEF_MALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit male chef uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    UNIFORM_CHEF_FEMALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit female chef uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    UNIFORM_WAITSTAFF_MALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit waiter uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    UNIFORM_WAITSTAFF_FEMALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit waitress uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    UNIFORM_HOST_MALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit male host uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    UNIFORM_HOST_FEMALE = TunablePackSafeResourceKey(description='\n        The SimInfo file to use to edit female host uniforms.\n        ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,),
      export_modes=(ExportModes.All))
    RESTAURANT_VENUE = TunablePackSafeReference(description='\n        This is a tunable reference to the type of Venue that will describe\n        a Restaurant. To be used for code references to restaurant venue types\n        in code.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.VENUE)))
    HOST_SITUATION = TunablePackSafeReference(description='\n        The situation that Sims working as a Host will have.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.SITUATION)))
    WAITSTAFF_SITUATION = TunablePackSafeReference(description='\n        The situation that Sims working as a Waiter will have.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.SITUATION)))
    CHEF_SITUATION = TunablePackSafeReference(description='\n        The situation that Sims working as a Chef will have.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.SITUATION)))
    HOME_CHEF_SITUATION_TAG = TunableEnumWithFilter(description='\n        Tag that we use on all the home chef situations.\n        ',
      tunable_type=Tag,
      filter_prefixes=[
     'situation'],
      default=(Tag.INVALID),
      invalid_enums=(
     Tag.INVALID,),
      pack_safe=True)
    DINING_SITUATION_TAG = TunableEnumWithFilter(description="\n        The tag used to find dining situations. \n        \n        This shouldn't need to be re-tuned after being set initially. If you\n        need to re-tune this you should probably talk to a GPE first.\n        ",
      tunable_type=Tag,
      filter_prefixes=[
     'situation'],
      default=(Tag.INVALID),
      pack_safe=True)
    TABLE_FOOD_SLOT_TYPE = TunableReference(description='\n        The slot type of the food slot on the dining table.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.SLOT_TYPE)))
    TABLE_DRINK_SLOT_TYPE = TunableReference(description='\n        The slot type of the drink slot on the dining table.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.SLOT_TYPE)))
    FOOD_AUTONOMY_PREFERENCE = TunableAutonomyPreference(description='\n        The Autonomy Preference for the delivered food items.\n        ',
      is_scoring=False)
    DRINK_AUTONOMY_PREFERENCE = TunableAutonomyPreference(description='\n        The Autonomy Preference for the delivered drink items.\n        ',
      is_scoring=False)
    CONSUMABLE_FULL_STATE_VALUE = TunableReference(description='\n        The Consumable_Full state value. Food in restaurants will be set to\n        this value instead of defaulting to Consumable_Untouched to avoid other\n        Sims from eating your own food.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
      class_restrictions=('ObjectStateValue', ))
    CONSUMABLE_EMPTY_STATE_VALUE = TunableReference(description="\n        The Consumable_Empty state value. This is the state we'll use to\n        determine if food/drink is empty or not.\n        ",
      manager=(services.get_instance_manager(sims4.resources.Types.OBJECT_STATE)),
      class_restrictions=('ObjectStateValue', ))
    FOOD_DELIVERED_TO_TABLE_NOTIFICATION = TunableUiDialogNotificationSnippet(description="\n        The notification shown when the food is delivered to the player's table.\n        ")
    FOOD_STILL_ON_TABLE_NOTIFICATION = TunableUiDialogNotificationSnippet(description="\n        The notification that the player will see if the waitstaff try and\n        deliver food but there's still food on the table.\n        ")
    STAND_UP_INTERACTION = TunableReference(description='\n        A reference to sim-stand so that sim-stand can be pushed on every sim\n        that is sitting at a table that is abandoned.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)))
    DEFAULT_MENU = TunableEnumEntry(description='\n        The default menu setting for a brand new restaurant.\n        ',
      tunable_type=MenuPresets,
      default=(MenuPresets.CUSTOMIZE),
      export_modes=(ExportModes.All),
      binary_type=(EnumBinaryExportType.EnumUint32))
    SWITCH_SEAT_INTERACTION = TunableReference(description='\n        This is a reference to the interaction that gets pushed on whichever Sim\n        is sitting in the seat that the Actor is switching to. The interaction \n        will be pushed onto the sseated Sim and will target the Actor Sims \n        current seat before the switch.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)))
    RECOMMENDED_ORDER_INTERACTION = TunableReference(description='\n        This is a reference to the interaction that will get pushed on the active Sim\n        to recommend orders to the Sim AFTER the having gone through the Menu UI.\n        \n        It will continue to retain the previous target.\n        ',
      manager=(services.get_instance_manager(sims4.resources.Types.INTERACTION)),
      pack_safe=True)
    INGREDIENT_PRICE_PERK_MAP = TunableMapping(description='\n        Maps the various ingredient price perks with their corresponding\n        discount.\n        ',
      key_name='Ingredient Price Perk',
      key_type=TunableReference(description='\n            A perk that gives a tunable multiplier to the price of ingredients\n            for restaurants.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.BUCKS_PERK)),
      pack_safe=True),
      value_name='Ingredient Price Multiplier',
      value_type=TunableRange(description='\n            If the household has the corresponding perk, this value will be\n            multiplied by the final cost of each recipe to the restaurant.\n            ',
      tunable_type=float,
      default=1,
      minimum=0))
    CUSTOMERS_ORDER_EXPENSIVE_FOOD_PERK_DATA = TunableTuple(description='\n        The perk that makes customers order more expensive food, and the off-lot\n        multiplier for that perk.\n        ',
      perk=TunablePackSafeReference(description='\n            If the owning household has this perk, customers will pick two dishes to\n            order and then pick the most expensive of the two.\n            ',
      manager=(services.get_instance_manager(sims4.resources.Types.BUCKS_PERK))),
      off_lot_multiplier=TunableRange(description='\n            When calculating off-lot profits, this is applied if the household\n            has this perk.\n            ',
      tunable_type=float,
      default=1.1,
      minimum=1))
    UNOWNED_RESTAURANT_PRICE_MULTIPLIER = TunableRange(description='\n        The amount each item in the menu will be multiplied by on unowned\n        restaurant lots.\n        ',
      tunable_type=float,
      default=1.2,
      minimum=0,
      export_modes=(ExportModes.All))
    CHEF_NOT_SKILLED_ENOUGH_THRESHOLD = Tunable(description='\n        This is the value that a chef must reach when preparing a meal for a\n        customer without displaying the "Chef isn\'t skilled enough to make \n        receiver X" \n        \n        The number that must reach this value is the skill adder\n        of the chef and recipe difficulty adder.\n        ',
      tunable_type=int,
      default=(-30))
    CHEF_NOT_SKILLED_ENOUGH_NOTIFICATION = TunableUiDialogNotificationSnippet(description='\n        The notification shown when the chef is working on a recipe that is \n        too difficult for their skill.\n        ')
    DEFAULT_PROFIT_PER_MEAL_FOR_OFF_LOT_SIMULATION = TunableRange(description='\n        This is used as the default profit for a meal for off-lot simulation. Once\n        enough actual meals have been sold, this value becomes irrelevant and\n        the MEAL_COUNT_FOR_OFF_LOT_PROFIT_PER_MEAL tunable comes into use.\n        ',
      tunable_type=int,
      default=20,
      minimum=1)
    MEAL_COUNT_FOR_OFF_LOT_PROFIT_PER_MEAL = TunableRange(description='\n        The number of meals to keep a running average of for the profit per meal\n        calculations during off lot simulations.\n        ',
      tunable_type=int,
      default=10,
      minimum=2)
    ADVERTISING_DATA_MAP = TunableMapping(description='\n        The mapping between advertising type and the data for that type.\n        ',
      key_name='Advertising_Type',
      key_type=TunableEnumEntry(description='\n            The Advertising Type .\n            ',
      tunable_type=BusinessAdvertisingType,
      default=(BusinessAdvertisingType.INVALID),
      invalid_enums=(
     BusinessAdvertisingType.INVALID,),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_name='Advertising_Data',
      value_type=TunableTuple(description='\n            Data associated with this advertising type.\n            ',
      cost_per_hour=TunableRange(description='\n                How much, per hour, it costs to use this advertising type.\n                ',
      tunable_type=int,
      default=10,
      minimum=0),
      customer_count_multiplier=TunableRange(description='\n                This amount is multiplied by the ideal customer count for owned\n                restaurants.\n                ',
      tunable_type=float,
      default=0.8,
      minimum=0),
      ui_sort_order=TunableRange(description='\n                Value representing how map entries will be sorted in the UI.\n                1 represents the first entry.  Avoid duplicate values\n                within the map.\n                ',
      tunable_type=int,
      minimum=1,
      default=1),
      export_class_name='RestaurantAdvertisingData'),
      tuple_name='RestaurantAdvertisingDataMapping',
      export_modes=(ExportModes.All))
    TODDLER_SENT_TO_DAYCARE_FOR_RESTAURANTS = TunableUiDialogNotificationSnippet(description='\n        The notification shown when a toddler is sent to daycare upon traveling\n        to a restaurant venue.\n        ')
    TIME_OF_DAY_TO_CUSTOMER_COUNT_MULTIPLIER_CURVE = TunableCurve(description='\n        A curve that lets you tune a specific customer count multiplier\n        based on the time of day. Time of day should range between 0 and 23,\n        0 being midnight.\n        ',
      x_axis_name='time_of_day',
      y_axis_name='customer_count_multiplier')
# okay decompiling data/sims4-not-yet-decompiled/simulation/restaurants/restaurant_tuning.pyc
