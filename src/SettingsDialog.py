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
| Yorick Bruijne           | 07-01-2017 | Made the butons functional       |
+--------------------------+------------+----------------------------------+
| Yorick Bruijne           | 11-01-2017 | Added a dialog after "Anuleren"  |
|                          |            | select dir shows correct dir     |
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
        c_dial = wx.MessageDialog(self, "Weet je zeker dat je de wijzigingen"
                                  " niet wilt oplsaan?", "Info", wx.YES_NO | wx.ICON_WARNING)
        c_dial.SetYesNoLabels("&Ja", "&Nee") 
        result = c_dial.ShowModal()
        if result == wx.ID_YES:
            self.Destroy()
        else:
            pass

    def select_Dir(self, event):
        print("Select dir")
        sd_dir = wx.DirDialog(self, "kies een map:", style=wx.DD_DEFAULT_STYLE)
        if sd_dir.ShowModal() == wx.ID_OK:
            sd_get_dir = sd_dir.GetPath()
            self.settings.setSetting("path", sd_get_dir)
            if len(sd_get_dir) > 55 and len(sd_get_dir) < 100:
                sd_get_dir = sd_get_dir[0:50] + "\n" + sd_get_dir[50:]
            if len(sd_get_dir) > 105:
                sd_get_dir = sd_get_dir[0:50] + "\n" + sd_get_dir[50:100] \
                             + "\n" + sd_get_dir[100:]
            self.panel.fs_pad_txt.SetLabel(sd_get_dir)
            self.settings.writeToFile()
        sd_dir.Destroy()
    
    def save(self, event):
        self.settings.setSetting("prefix", self.panel.cpaf_prefix_textfield.GetValue())
        self.settings.setSetting("font-family", self.panel.cebl_combo_box.GetValue())
        self.settings.setSetting("font-size", self.panel.cebr_font_size_spinner.GetValue())
        self.settings.setSetting("tab-length", self.panel.cebr_tab_spinner.GetValue())
        self.settings.setSetting("automatic-save", self.panel.cebr_cb.GetValue())
        self.settings.writeToFile()
        self.Destroy()
#        print("klik opslaan")
#        print("prefix", self.panel.cpaf_prefix_textfield.GetValue())
#        print("Lettertype", self.panel.cebl_combo_box.GetValue())
#        print("Letterformaat", self.panel.cebr_font_size_spinner.GetValue())
#        print("tablengte", self.panel.cebr_tab_spinner.GetValue())
#        print("Auto opslaan", self.panel.cebr_cb.GetValue())
