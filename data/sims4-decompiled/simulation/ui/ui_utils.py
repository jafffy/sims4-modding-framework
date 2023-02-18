# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\ui\ui_utils.py
# Compiled at: 2021-11-16 19:15:21
# Size of source mod 2**32: 2010 bytes
from contextlib import contextmanager
import enum, sims4.log
from distributor.ops import ToggleSimInfoPanel
from distributor.system import Distributor
logger = sims4.log.Logger('UIUtils', default_owner='bnguyen')

@contextmanager
def hide_selected_notifications():
    UIUtils._hide_selected_notifications = True
    try:
        yield
    finally:
        UIUtils._hide_selected_notifications = False


class UIUtils:
    _hide_selected_notifications = False

    class SimInfoPanelType(enum.Int):
        SIM_INFO_MOTIVE_PANEL = 0
        SIM_INFO_SKILL_PANEL = 1
        SIM_INFO_RELATIONSHIP_PANEL = 2
        SIM_INFO_CAREER_PANEL = 3
        SIM_INFO_INVENTORY_PANEL = 4
        SIM_INFO_ASPIRATION_PANEL = 5
        SIM_INFO_SUMMARY_PANEL = 6
        SIM_INFO_CLUB_PANEL = 7

    class DynamicSignType(enum.Int):
        DYNAMIC_SIGN_TYPE_DEFAULT = 0
        DYNAMIC_SIGN_TYPE_SCENARIO = 1

    @staticmethod
    def toggle_sim_info_panel(panel_type, stay_open=True):
        op = ToggleSimInfoPanel(panel_type, stay_open)
        Distributor.instance().add_op_with_no_owner(op)

    @staticmethod
    def get_hide_selected_notification_status():
        return UIUtils._hide_selected_notifications
# okay decompiling data/sims4-not-yet-decompiled/simulation/ui/ui_utils.pyc
