"""
Log
+--------------------------+------------+-----------------------------------+
| Who                      | When       | What                              |
+--------------------------+------------+-----------------------------------+
| Yorick Bruijne           | 28-12-2017 | making the file, panel and widgets|
+--------------------------+------------+-----------------------------------+
| Wesley Ameling           | 29-12-2017 | Minor refactoring, translating    |
|                          |            | into English and made the GUI more|
|                          |            | flexible.                         |
+--------------------------+------------+-----------------------------------+
| Wesley Ameling           | 03-01-2018 | Removed panel size                |
+--------------------------+------------+-----------------------------------+

"""

import wx

import MainFrame
from settings import Settings


SETTINGS = "Instellingen"
FILE_SETTINGS = "Bestandsinstellingen"
PREFIX = "Prefix"
SAVE_FOLDER = "Opslagmap"
SELECT_FOLDER = "Map selecteren"
EDIT_SETTINGS = "Bewerkingsinstellingen"
TAB_LENGTH = "Tab lengte"
AUTOMATIC_SAVE = "Automatisch opslaan"
CANCEL = "Anuleren"
SAVE = "Opslaan"


class SettingsPanel(wx.Panel):

    def __init__(self, parent, id):
        super().__init__(parent, id)
        self.settings = Settings.getInstance()
        self.IP_vbox = wx.BoxSizer(wx.VERTICAL)
        self.IP_vbox.Add(self.createTitle(id))
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.fileSettings(id), 1, wx.EXPAND)
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.createEditSettings(id), 1, wx.EXPAND)
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.createBottomBox(id), 1, wx.EXPAND)
        self.IP_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.IP_hbox.AddSpacer(20)
        self.IP_hbox.Add(self.IP_vbox, 1, wx.EXPAND)
        self.IP_hbox.AddSpacer(20)
        self.SetSizer(self.IP_hbox)

    def fileSettings(self, id):
        fs_pad = self.settings.getSetting("path")
        fs_pad_txt = wx.StaticText(self, id, fs_pad)
        fs_hbox = self.createPrefixAndFolder(id)
        fs_main_mbox_border = wx.StaticBox(self, id, FILE_SETTINGS)
        fs_main_vbox = wx.StaticBoxSizer(fs_main_mbox_border, wx.VERTICAL)
        fs_main_vbox.Add(fs_hbox, 1, wx.EXPAND)
        fs_main_vbox.Add(fs_pad_txt, 1, wx.EXPAND)
        return fs_main_vbox

    def createPrefixAndFolder(self, id):
        cpaf_prefix_txt = wx.StaticText(self, id, PREFIX)
        cpaf_prefix_textfield = wx.TextCtrl(self)
        cpaf_save_folder_txt = wx.StaticText(self, id, SAVE_FOLDER)
        cpaf_select_opslagmap = wx.Button(self, id, SELECT_FOLDER)
        cpaf_vbox_left = wx.BoxSizer(wx.VERTICAL)
        cpaf_vbox_left.AddSpacer(5)
        cpaf_vbox_left.Add(
            cpaf_prefix_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        cpaf_vbox_left.AddSpacer(13)
        cpaf_vbox_left.Add(
            cpaf_save_folder_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        cpaf_vbox_right = wx.BoxSizer(wx.VERTICAL)
        cpaf_vbox_right.Add(
            cpaf_prefix_textfield, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        cpaf_vbox_right.Add(
            cpaf_select_opslagmap, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        cpaf_hbox = wx.BoxSizer(wx.HORIZONTAL)
        cpaf_hbox.Add(cpaf_vbox_left, 1, wx.EXPAND)
        cpaf_hbox.AddSpacer(20)
        cpaf_hbox.Add(cpaf_vbox_right, 1, wx.EXPAND)
        return cpaf_hbox

    def createBottomBox(self, id):
        cbb_button_anu = wx.Button(self, id, CANCEL)
        cbb_button_ops = wx.Button(self, id, SAVE)
        cbb_version_txt = wx.StaticText(self, id, MainFrame.VERSION_STRING,
                                       style=wx.ALIGN_CENTER)
        cbb_hbox = wx.BoxSizer(wx.HORIZONTAL)
        cbb_hbox.Add(cbb_button_anu, 1)
        cbb_hbox.Add(cbb_version_txt, 3, wx.ALIGN_CENTER)
        cbb_hbox.Add(cbb_button_ops, 1, wx.ALIGN_RIGHT)
        return cbb_hbox

    def createTitle(self, id):
        t_fnt_title = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)
        t_title_txt = wx.StaticText(self, id, SETTINGS)
        t_title_txt.SetFont(t_fnt_title)
        return t_title_txt

    def createEditSettings(self, id):
        ces_vbox_left = self.createEditBoxLeft(id)
        ces_vbox_right = self.createEditBoxRight(id)
        ces_hbox_border = wx.StaticBox(self, id, EDIT_SETTINGS)
        ces_hbox = wx.StaticBoxSizer(ces_hbox_border, wx.HORIZONTAL)
        ces_hbox.Add(ces_vbox_left, 1, wx.EXPAND)
        ces_hbox.Add(ces_vbox_right, 1, wx.EXPAND)
        return ces_hbox

    def createEditBoxLeft(self, id):
        cebl_tab_txt = wx.StaticText(self, id, TAB_LENGTH)
        cebl_save_txt = wx.StaticText(self, id, AUTOMATIC_SAVE)
        cebl_font_choices = ["een", "twee", "Dit_is_een_lange_fam_naam"]
        cebl_combo_box = wx.ComboBox(self, choices=cebl_font_choices)
        cebl_vbox = wx.BoxSizer(wx.VERTICAL)
        cebl_vbox.Add(cebl_combo_box, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        cebl_vbox.Add(cebl_tab_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        cebl_vbox.Add(cebl_save_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        return cebl_vbox

    def createEditBoxRight(self, id):
        cebr_font_size = self.settings.getSetting('font-size')
        cebr_tab_length = self.settings.getSetting('tab-length')
        cebr_font_size_spinner = wx.SpinCtrl(self, min=5, max=25,
                                             initial=cebr_font_size)
        cebr_tab_spinner = wx.SpinCtrl(self, min=2, max=8,
                                       initial=cebr_tab_length)
        cebr_vbox = wx.BoxSizer(wx.VERTICAL)
        expand_center_flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL
        cebr_vbox.Add(cebr_font_size_spinner, 1, expand_center_flag)
        cebr_vbox.Add(cebr_tab_spinner, 1, expand_center_flag)
        cebr_cb = wx.CheckBox(self)
        cebr_vbox.Add(cebr_cb, 1, expand_center_flag)
        return cebr_vbox
