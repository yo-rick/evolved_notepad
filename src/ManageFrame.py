"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""
import wx


class ManageFrame(wx.Frame):

    def __init__(self, parent, id, title, itemContainer):
        super().__init__(parent, id, title)
        self.itemContainer = itemContainer

    # Create a panel which uses this itemContainer
    # test
