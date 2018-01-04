"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Add ManageDialog                 |
+--------------------------+------------+----------------------------------+

"""
import wx

import panels
from container import CategoryItemContainer


class ManageDialog(wx.Dialog):

    def __init__(self, parent, id, item_container, category=True):
        super().__init__(parent, id, "", size=(450, 420))
        self.item_container = item_container
        self.category = category
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        if self.category:
            panel = panels.CategoryManagePanel(
                self, wx.ID_ANY, self.item_container)
        else:
            panel = panels.NoteManagePanel(
                self, wx.ID_ANY, self.item_container)
        self.sizer.Clear()
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetTitle(panel.getFrameTitle())
        self.ShowModal()
