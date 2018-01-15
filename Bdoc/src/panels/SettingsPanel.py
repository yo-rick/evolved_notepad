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
| Yorik Bruijne            | 07-01-2018 | Added "self." to some vars        |
|                          |            | Dropdownbox shows last saved      |
|                          |            | setting                           |
|                          |            | Checkbos shows last saved setting |
|                          |            | Made the buttons functional       |
+--------------------------+------------+-----------------------------------+
| Yorick Bruijne           | 11-01-2018 | Added a dialog after "Anuleren"   |
|                          |            | select dir shows correct dir      |
+--------------------------+------------+-----------------------------------+
| Yorick Bruijne           | 14-01-2018 | Notes can now be moved to an      |
|                          |            | other folder                      |
+--------------------------+------------+-----------------------------------+
| Wesley Ameling           | 14-01-2018 | Improve moving, moving on save and|
|                          |            | minor layout improvement          |
+--------------------------+------------+-----------------------------------+
"""
import os
import shutil

import wx

import MainFrame
from settings import Settings
from .BasePanel import BasePanel
SETTINGS = "Instellingen"
FILE_SETTINGS = "Bestandsinstellingen"
PREFIX = "Prefix"
SAVE_FOLDER = "Opslagmap"
SELECT_FOLDER = "Map selecteren"
EDIT_SETTINGS = "Bewerkingsinstellingen"
TAB_LENGTH = "Tab lengte"
AUTOMATIC_SAVE = "Automatisch opslaan"
CANCEL = "Annuleren"
SAVE = "Opslaan"


class SettingsPanel(BasePanel):

    def __init__(self, parent, id):
        super().__init__(parent, id, "Instellingen", "Instellingen")
        self.settings = Settings()
        self.path = self.settings.getSetting('path')
        self.fs_pad_txt = wx.TextCtrl(self, wx.ID_ANY, value=self.path,
                                      style=wx.TE_READONLY)
        self.IP_vbox = wx.BoxSizer(wx.VERTICAL)
        self.IP_vbox.Add(self.createTitle(id))
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.fileSettings(id), 1, wx.EXPAND)
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.createEditSettings(id), 1, wx.EXPAND)
        self.IP_vbox.AddStretchSpacer(5)
        self.IP_vbox.Add(self.createBottomBox(id), 1, wx.EXPAND)
        self.IP_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.IP_hbox.AddSpacer(20)
        self.IP_hbox.Add(self.IP_vbox, 1, wx.EXPAND)
        self.IP_hbox.AddSpacer(20)
        self.SetSizer(self.IP_hbox)
        self.bindEvents()

    def bindEvents(self):
        self.btn_anu.Bind(wx.EVT_BUTTON, self.cancel)
        self.btn_ops.Bind(wx.EVT_BUTTON, self.save)
        self.btn_select_opslagmap.Bind(wx.EVT_BUTTON, self.selectDir)
        self.settings = Settings()

    def cancel(self, event):
        c_dial = wx.MessageDialog(self, "Weet je zeker dat je de wijzigingen"
                                  " niet wilt opslaan?", "Info", wx.YES_NO |
                                  wx.ICON_WARNING)
        c_dial.SetYesNoLabels("&Ja", "&Nee")
        result = c_dial.ShowModal()
        if result == wx.ID_YES:
            self.GetParent().goBack()
        else:
            pass

    def save(self, event):
        self.settings.setSetting(
            "prefix", self.tf_prefix.GetValue())
        self.settings.setSetting("font-family", self.cebl_combo_box.GetValue())
        self.settings.setSetting(
            "font-size", self.cebr_font_size_spinner.GetValue())
        self.settings.setSetting(
            "tab-length", self.cebr_tab_spinner.GetValue())
        self.settings.setSetting("automatic-save", self.chb_save.GetValue())
        old_path = self.settings.getSetting('path')
        if old_path != self.path:
            for category, comp in self.settings.getSetting('items').items():
                path = os.path.join(old_path, comp['folder'])
                shutil.move(path, self.path)
            self.settings.setSetting("path", self.path)
        self.settings.writeToFile()
        self.GetParent().goBack()

    def selectDir(self, event):
        sd_dir = wx.DirDialog(self, "Kies een map:", style=wx.DD_DEFAULT_STYLE)
        if sd_dir.ShowModal() == wx.ID_OK:
            self.path = sd_dir.GetPath()
            self.fs_pad_txt.SetValue(self.path)
            self.settings.writeToFile()
        self.GetParent().goBack()

    def fileSettings(self, id):
        fs_hbox = self.createPrefixAndFolder(id)
        fs_main_mbox_border = wx.StaticBox(self, id, FILE_SETTINGS)
        fs_main_vbox = wx.StaticBoxSizer(fs_main_mbox_border, wx.VERTICAL)
        fs_main_vbox.Add(fs_hbox, 1, wx.EXPAND)
        fs_main_vbox.Add(self.fs_pad_txt, 1, wx.EXPAND)
        return fs_main_vbox

    def createPrefixAndFolder(self, id):
        cpaf_prefix_txt = wx.StaticText(self, id, PREFIX)
        self.tf_prefix = wx.TextCtrl(self)
        cpaf_save_folder_txt = wx.StaticText(self, id, SAVE_FOLDER)
        self.btn_select_opslagmap = wx.Button(self, id, SELECT_FOLDER)
        cpaf_vbox_left = wx.BoxSizer(wx.VERTICAL)
        cpaf_vbox_left.AddSpacer(5)
        cpaf_vbox_left.Add(
            cpaf_prefix_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        cpaf_vbox_left.AddSpacer(13)
        cpaf_vbox_left.Add(
            cpaf_save_folder_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        cpaf_vbox_right = wx.BoxSizer(wx.VERTICAL)
        cpaf_vbox_right.Add(
            self.tf_prefix, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        cpaf_vbox_right.Add(
            self.btn_select_opslagmap, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        cpaf_hbox = wx.BoxSizer(wx.HORIZONTAL)
        cpaf_hbox.Add(cpaf_vbox_left, 1, wx.EXPAND)
        cpaf_hbox.AddSpacer(20)
        cpaf_hbox.Add(cpaf_vbox_right, 1, wx.EXPAND)
        return cpaf_hbox

    def createBottomBox(self, id):
        self.btn_anu = wx.Button(self, id, CANCEL)
        self.btn_ops = wx.Button(self, id, SAVE)
        cbb_version_txt = wx.StaticText(self, id, MainFrame.VERSION_STRING,
                                       style=wx.ALIGN_CENTER)
        cbb_hbox = wx.BoxSizer(wx.HORIZONTAL)
        cbb_hbox.Add(self.btn_anu, 1)
        cbb_hbox.Add(cbb_version_txt, 3, wx.ALIGN_CENTER)
        cbb_hbox.Add(self.btn_ops, 1, wx.ALIGN_RIGHT)
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
        cebl_font_choices = ["Default", "Modern", "Roman", "Script",
                             "Swiss", "Teletype"]
        self.cebl_combo_box = wx.ComboBox(self, choices=cebl_font_choices)
        self.cebl_combo_box.SetValue(self.settings.getSetting("font-family"))
        cebl_vbox = wx.BoxSizer(wx.VERTICAL)
        cebl_vbox.Add(self.cebl_combo_box, 1,
                      wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        cebl_vbox.Add(cebl_tab_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        cebl_vbox.Add(cebl_save_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        return cebl_vbox

    def createEditBoxRight(self, id):
        cebr_font_size = self.settings.getSetting('font-size')
        cebr_tab_length = self.settings.getSetting('tab-length')
        self.cebr_font_size_spinner = wx.SpinCtrl(self, min=5, max=25,
                                             initial=cebr_font_size)
        self.cebr_tab_spinner = wx.SpinCtrl(self, min=2, max=8,
                                       initial=cebr_tab_length)
        cebr_vbox = wx.BoxSizer(wx.VERTICAL)
        expand_center_flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL
        cebr_vbox.Add(self.cebr_font_size_spinner, 1, expand_center_flag)
        cebr_vbox.Add(self.cebr_tab_spinner, 1, expand_center_flag)
        self.chb_save = wx.CheckBox(self)
        self.chb_save.SetValue(self.settings.getSetting("automatic-save"))
        cebr_vbox.Add(self.chb_save, 1, expand_center_flag)
        return cebr_vbox
