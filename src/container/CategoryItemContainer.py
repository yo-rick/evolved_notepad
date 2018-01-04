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
| Wesley Ameling           | 04-01-2018 | Re-implemented this whole class  |
+--------------------------+------------+----------------------------------+

"""
import os
import shutil
from uuid import uuid4

import wx

import panels
from settings import Settings
from .ItemContainer import ItemContainer
from .NoteItemContainer import NoteItemContainer


class CategoryItemContainer(ItemContainer):

    def __init__(self, categoryFolder):
        self.folder = categoryFolder
        self.settings = Settings.getInstance()
        self.main_frame = None
        self.dirs = []
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
        if not os.path.isdir(self.folder):
            os.mkdir(self.folder)
        folder = str(uuid4())
        path = os.path.join(self.folder, folder)
        os.mkdir(path)
        self.arr_container_items.append(new_item)
        self.dirs.append(folder)
        self.regenerateItemsDict()

    def deleteItem(self, index):
        super().deleteItem(index)
        shutil.rmtree(os.path.join(self.folder, self.dirs[index]), True)
        self.regenerateItemsDict()
        del self.dirs[index]
        del self.arr_container_items[index]

    def fillContainer(self):
        if not os.path.isdir(self.folder):
            return
        items = self.settings.getSetting("items")
        for name, obj in items.items():
            sub_path = os.path.join(self.folder, obj['folder'])
            if not os.path.isdir(sub_path):
                continue
            self.arr_container_items.append(name)
            self.dirs.append(obj['folder'])

    def setMainFrame(self, frame):
        self.main_frame = frame

    def regenerateItemsDict(self):
        items_dict = self.settings.getSetting('items')
        for i in range(len(self.arr_container_items)):
            category = self.arr_container_items[i]
            if category not in items_dict:
                items_dict[category] = dict(folder=self.dirs[i], items=[])
            item_dir = os.path.join(
                self.folder, items_dict[category]['folder'])
            if not os.path.isdir(item_dir):
                del items_dict[category]
        self.settings.setSetting('items', items_dict)
        self.settings.writeToFile()
