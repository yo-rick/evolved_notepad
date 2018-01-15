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
| Wesley Ameling           | 05-01-2018 | Reflect name changes in base clss|
+--------------------------+------------+----------------------------------+
| Tjardo Maarseveen        | 13-01-2018 | Implementing alphabetical order  |
|                          |            | for items in container           |
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
        super().__init__()
        self.folder = categoryFolder

    def clickItem(self, index):
        super().clickItem(index)
        item = self.arr_container_items[index]
        note_item_container = NoteItemContainer(item)
        note_item_container.setMainFrame(self.main_frame)
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
        self.arr_container_items.sort()
        self.path_components.append(folder)
        self.regenerateItemsDict()

    def deleteItem(self, index):
        super().deleteItem(index)
        shutil.rmtree(
            os.path.join(self.folder, self.path_components[index]), True)
        self.regenerateItemsDict()
        del self.path_components[index]
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
            self.path_components.append(obj['folder'])
        self.arr_container_items.sort()

    def regenerateItemsDict(self):
        items_dict = self.settings.getSetting('items')
        for i in range(len(self.arr_container_items)):
            category = self.arr_container_items[i]
            if category not in items_dict:
                items_dict[category] = dict(folder=self.path_components[i],
                                            items=dict())
            item_dir = os.path.join(
                self.folder, items_dict[category]['folder'])
            if not os.path.isdir(item_dir):
                del items_dict[category]
        self.settings.setSetting('items', items_dict)
        self.settings.writeToFile()
