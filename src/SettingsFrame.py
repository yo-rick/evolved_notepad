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

"""
import wx

import panels


class SettingsFrame(wx.Frame):

    def __init__(self, parent, id):
        super().__init__(parent, id, "Instellingen", size=(450, 400))
        self.panel = panels.SettingsPanel(self, id)
        self.Show(True)
