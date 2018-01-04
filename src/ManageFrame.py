"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Add ManagePanel                  |
+--------------------------+------------+----------------------------------+

"""
import wx

import panels
from container import CategoryItemContainer


class ManageFrame(wx.Frame):

    def __init__(self, parent, id, title, item_container):
        super().__init__(parent, id, title, size=(450, 420))
        self.item_container = item_container
        self.panel = panels.ManagePanel(self, -1, "Notities",
                                        CategoryItemContainer(''))
        self.Show(True)
