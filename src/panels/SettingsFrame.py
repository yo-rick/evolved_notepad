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

"""
from InstellingenPanel import InstellingenPanel
import wx


class SettingsFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(460, 300))
        self.panel = InstellingenPanel(self, id)
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    SettingsFrame(None, -1, "Instellingen")
    app.MainLoop()
