"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Implement clickItem for a        |
|                          |            | category                         |
+--------------------------+------------+----------------------------------+

"""
import os

import wx

import panels
from .ItemContainer import ItemContainer
from .NoteItemContainer import NoteItemContainer


class CategoryItemContainer(ItemContainer):

    def __init__(self, categoryFolder):
        self.folder = categoryFolder
        self.main_frame = None
        super().__init__()

    def clickItem(self, index):
        super().clickItem(index)
        item = self.arr_container_items[index]
        note_item_container = NoteItemContainer(
            os.path.join(self.folder, item))
        panel = panels.NoteOverviewPanel(
            self.main_frame, wx.ID_ANY, note_item_container)
        self.main_frame.showPanel(panel)

    def createItem(self, new_item):
        pass

    def deleteItem(self, index):
        super().deleteItem(index)

    def fillContainer(self):
        self.arr_container_items.append('Beheren doet het nog niet :S')

    def setMainFrame(self, frame):
        self.main_frame = frame
