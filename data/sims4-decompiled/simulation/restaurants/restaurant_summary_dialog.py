# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\restaurants\restaurant_summary_dialog.py
# Compiled at: 2017-04-11 17:35:05
# Size of source mod 2**32: 2085 bytes
from business.business_summary_dialog import BusinessSummaryDialog, BusinessSummaryLineItemType
from restaurants.restaurant_tuning import RestaurantTuning
import sims4
logger = sims4.log.Logger('Business', default_owner='jdimailig')

class RestaurantSummaryDialog(BusinessSummaryDialog):

    def __init__(self, *args, **kwargs):
        (super().__init__)(*args, **kwargs)
        self._advertising_cost = 0
        self._food_profit = 0
        self._employee_wages = 0

    def _calculated_profit(self):
        return self._food_profit - self._employee_wages - self._advertising_cost

    def _add_line_entries(self):
        self._add_daily_revenue_line_entry()
        cost_of_ingredients = self._business_manager.get_cost_from_tracker(RestaurantTuning.BUSINESS_FUNDS_CATEGORY_FOR_COST_OF_INGREDIENTS)
        self._food_profit = self._business_manager.daily_revenue - cost_of_ingredients
        self._add_line_entry(self._business_tuning.summary_dialog_cost_of_ingredients_header, BusinessSummaryLineItemType.ENTRY_LINE_ITEM, self._business_tuning.summary_dialog_cost_of_ingredients_text(int(-cost_of_ingredients)))
        self._add_line_entry(self._business_tuning.summary_dialog_food_profit_header, BusinessSummaryLineItemType.SUB_TOTAL_LINE_ITEM, self._business_tuning.summary_dialog_food_profit_text(int(self._food_profit)))
        self._add_employee_wages_line_entry()
        self._add_advertising_costs()
        self._employee_wages = self._business_manager.get_total_employee_wages()
        self._advertising_cost = self._business_manager.get_current_advertising_cost()
# okay decompiling data/sims4-not-yet-decompiled/simulation/restaurants/restaurant_summary_dialog.pyc
