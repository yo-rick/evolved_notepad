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


class BasePanel(wx.Panel):

    def __init__(self, parent, id, title):
        super().__init__(parent, id)
        self.title = title

    def getTitle(self):
        return self.title
