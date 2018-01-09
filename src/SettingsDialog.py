"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Yorick Bruijne           | 28-12-2017 | making the frame                 |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Added default title and removed  |
|                          |            | ability to launch this frame     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 03-01-2018 | Tweaked the size of the frame    |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Change to a dialog instead of a  |
|                          |            | panel                            |
+--------------------------+------------+----------------------------------+

"""
import wx
import sys
import panels

from settings import Settings


class SettingsDialog(wx.Dialog):

    def __init__(self, parent, id):
        super().__init__(parent, id, "Instellingen", size=(450, 420))
        self.panel = panels.SettingsPanel(self, id)
        self.panel.cbb_button_anu.Bind(wx.EVT_BUTTON, self.cancel)
        self.panel.cbb_button_ops.Bind(wx.EVT_BUTTON, self.save)
        self.panel.cpaf_select_opslagmap.Bind(wx.EVT_BUTTON, self.select_Dir)
        self.settings = Settings.getInstance()
        self.ShowModal()

    def cancel(self, event):
        self.Destroy() # moet nog gekoppeld worden

    def select_Dir(self, event):
        print("Select dir")
        sd_dir = wx.DirDialog(self, "kiez een map:", style=wx.DD_DEFAULT_STYLE)
        if sd_dir.ShowModal() == wx.ID_OK:
            sd_get_dir = sd_dir.GetPath()
            self.settings.setSetting("path", sd_get_dir)
            self.settings.writeToFile()
        sd_dir.Destroy()
    
    def save(self, event):
        self.settings.setSetting("prefix", self.panel.cpaf_prefix_textfield.GetValue())
        self.settings.setSetting("font-family", self.panel.cebl_combo_box.GetValue())
        self.settings.setSetting("font-size", self.panel.cebr_font_size_spinner.GetValue())
        self.settings.setSetting("tab-length", self.panel.cebr_tab_spinner.GetValue())
        self.settings.setSetting("automatic-save", self.panel.cebr_cb.GetValue())
        self.settings.writeToFile()
#        print("klik opslaan")
#        print("prefix", self.panel.cpaf_prefix_textfield.GetValue())
#        print("Lettertype", self.panel.cebl_combo_box.GetValue())
#        print("Letterformaat", self.panel.cebr_font_size_spinner.GetValue())
#        print("tablengte", self.panel.cebr_tab_spinner.GetValue())
#        print("Auto opslaan", self.panel.cebr_cb.GetValue())
