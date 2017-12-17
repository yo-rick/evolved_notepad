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


class SettingsFrame(wx.Frame):

    def __init__(self, parent, id, title):
        super().__init__(parent, id, title)

    # Create a panel which shows the settings
