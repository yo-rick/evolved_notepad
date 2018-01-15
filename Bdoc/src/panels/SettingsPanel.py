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
|                          |            | minor layout improvement.         |
+--------------------------+------------+-----------------------------------+
"""
import os
import shutil
import wx

import MainFrame
from settings import Settings
from .BasePanel import BasePanel

g_str_SETTINGS = "Instellingen"
g_str_FILE_SETTINGS = "Bestandsinstellingen"
g_str_PREFIX = "Prefix"
g_str_SAVE_FOLDER = "Opslagmap"
g_str_SELECT_FOLDER = "Map selecteren"
g_str_EDIT_SETTINGS = "Bewerkingsinstellingen"
g_str_TAB_LENGTH = "Tab lengte"
g_str_AUTOMATIC_SAVE = "Automatisch opslaan"
g_str_CANCEL = "Annuleren"
g_str_SAVE = "Opslaan"


class SettingsPanel(BasePanel):

    def __init__(self, parent, id):
        super().__init__(parent, id, "Instellingen", "Instellingen")
        self.settings = Settings()
        self.path = self.settings.getSetting('path')
        self.tf_pad_txt = wx.TextCtrl(self, wx.ID_ANY, value=self.path,
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
        self.select_opslagmap.Bind(wx.EVT_BUTTON, self.selectDir)
        self.settings = Settings()

    def cancel(self, event):
        dialog = wx.MessageDialog(self, "Weet je zeker dat je de wijzigingen"
                                  " niet wilt opslaan?", "Info", wx.YES_NO |
                                  wx.ICON_WARNING)
        dialog.SetYesNoLabels("&Ja", "&Nee")
        result = dialog.ShowModal()
        if result == wx.ID_YES:
            self.GetParent().goBack()
        else:
            pass

    def save(self, event):
        self.settings.setSetting(
            "prefix", self.tf_prefix.GetValue())
        self.settings.setSetting("font-family", self.combo_box.GetValue())
        self.settings.setSetting("font-size",
                                 self.spi_font_size_spinner.GetValue())
        self.settings.setSetting("tab-length", self.spi_tab_spinner.GetValue())
        self.settings.setSetting("automatic-save", self.chb_save.GetValue())
        old_path = self.settings.getSetting('path')
        if old_path != self.path:
            for category, comp in self.settings.getSetting('items').items():
                path = os.path.join(old_path, comp['folder'])
                if os.path.isdir(path):
                    shutil.move(path, self.path)

            self.settings.setSetting("path", self.path)
        self.settings.writeToFile()
        self.GetParent().goBack()

    def selectDir(self, event):
        select_dir = wx.DirDialog(self, "Kies een map:",
                                  style=wx.DD_DEFAULT_STYLE)
        if select_dir.ShowModal() == wx.ID_OK:
            self.path = select_dir.GetPath()
            self.tf_pad_txt.SetValue(self.path)
            self.settings.writeToFile()
        select_dir.Destroy()

    def fileSettings(self, id):
        hbox = self.createPrefixAndFolder(id)
        main_mbox_border = wx.StaticBox(self, id, g_str_FILE_SETTINGS)
        main_vbox = wx.StaticBoxSizer(main_mbox_border, wx.VERTICAL)
        main_vbox.Add(hbox, 1, wx.EXPAND)
        main_vbox.Add(self.tf_pad_txt, 1, wx.EXPAND)
        return main_vbox

    def createPrefixAndFolder(self, id):
        prefix_txt = wx.StaticText(self, id, g_str_PREFIX)
        self.tf_prefix = wx.TextCtrl(self)
        save_folder_txt = wx.StaticText(self, id, g_str_SAVE_FOLDER)
        self.select_opslagmap = wx.Button(self, id, g_str_SELECT_FOLDER)
        vbox_left = wx.BoxSizer(wx.VERTICAL)
        vbox_left.AddSpacer(5)
        vbox_left.Add(prefix_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        vbox_left.AddSpacer(13)
        vbox_left.Add(save_folder_txt, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        vbox_right = wx.BoxSizer(wx.VERTICAL)
        vbox_right.Add(self.tf_prefix, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        vbox_right.Add(self.select_opslagmap, 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(vbox_left, 1, wx.EXPAND)
        hbox.AddSpacer(20)
        hbox.Add(vbox_right, 1, wx.EXPAND)
        return hbox

    def createBottomBox(self, id):
        self.btn_anu = wx.Button(self, id, g_str_CANCEL)
        self.btn_ops = wx.Button(self, id, g_str_SAVE)
        version_txt = wx.StaticText(self, id, MainFrame.VERSION_STRING,
                                    style=wx.ALIGN_CENTER)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.btn_anu, 1)
        hbox.Add(version_txt, 3, wx.ALIGN_CENTER)
        hbox.Add(self.btn_ops, 1, wx.ALIGN_RIGHT)
        return hbox

    def createTitle(self, id):
        fnt_title = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)
        title_txt = wx.StaticText(self, id, g_str_SETTINGS)
        title_txt.SetFont(fnt_title)
        return title_txt

    def createEditSettings(self, id):
        vbox_left = self.createEditBoxLeft(id)
        vbox_right = self.createEditBoxRight(id)
        hbox_border = wx.StaticBox(self, id, g_str_EDIT_SETTINGS)
        hbox = wx.StaticBoxSizer(hbox_border, wx.HORIZONTAL)
        hbox.Add(vbox_left, 1, wx.EXPAND)
        hbox.Add(vbox_right, 1, wx.EXPAND)
        return hbox

    def createEditBoxLeft(self, id):
        tab_txt = wx.StaticText(self, id, g_str_TAB_LENGTH)
        save_txt = wx.StaticText(self, id, g_str_AUTOMATIC_SAVE)
        arr_font_choices = ["Default", "Modern", "Roman", "Script",
                            "Swiss", "Teletype"]
        self.combo_box = wx.ComboBox(self, choices=arr_font_choices)
        self.combo_box.SetValue(self.settings.getSetting("font-family"))
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.combo_box, 1,
                 wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        vbox.Add(tab_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        vbox.Add(save_txt, 1, wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL)
        return vbox

    def createEditBoxRight(self, id):
        font_size = self.settings.getSetting('font-size')
        tab_length = self.settings.getSetting('tab-length')
        self.spi_font_size_spinner = wx.SpinCtrl(self, min=5, max=25,
                                                 initial=font_size)
        self.spi_tab_spinner = wx.SpinCtrl(self, min=2, max=8,
                                           initial=tab_length)
        vbox = wx.BoxSizer(wx.VERTICAL)
        expand_center_flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL
        vbox.Add(self.spi_font_size_spinner, 1, expand_center_flag)
        vbox.Add(self.spi_tab_spinner, 1, expand_center_flag)
        self.chb_save = wx.CheckBox(self)
        self.chb_save.SetValue(self.settings.getSetting("automatic-save"))
        vbox.Add(self.chb_save, 1, expand_center_flag)
        return vbox
