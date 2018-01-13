"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Reflect changes in the base class|
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 05-01-2018 | Implement methods                |
+--------------------------+------------+----------------------------------+
| Tjardo Maarseveen        | 13-01-2018 | Implementing alphabetical order  |
|                          |            | for items in container           |
+--------------------------+------------+----------------------------------+
"""
import os
from uuid import uuid4

import wx

import panels
from settings import Settings
from .ItemContainer import ItemContainer


class NoteItemContainer(ItemContainer):

    def __init__(self, category):
        self.settings = Settings.getInstance()
        self.category = category
        self.items = self.settings.getSetting('items')
        self.folder = os.path.join(
            self.settings.getSetting('path'),
            self.items[self.category]['folder'])
        super().__init__()

    def clickItem(self, index):
        super().clickItem(index)
        note_name = self.arr_container_items[index]
        note_folder = os.path.join(self.folder, self.path_components[index])
        note_panel = panels.NotePanel(
            self.main_frame, wx.ID_ANY, note_name, note_folder)
        self.main_frame.showPanel(note_panel)

    def createItem(self, new_item):
        file_name = str(uuid4())
        self.arr_container_items.append(new_item)
        self.arr_container_items = sorted(self.arr_container_items)
        self.path_components.append(file_name)
        self.regenerateItemsDict()

    def deleteItem(self, index):
        super().clickItem(index)
        file_path = os.path.join(self.folder, self.path_components[index])
        if os.path.isfile(file_path):
            os.remove(file_path)
        del self.path_components[index]
        del self.arr_container_items[index]
        self.regenerateItemsDict()

    def fillContainer(self):
        item_dict = self.items[self.category]
        for name, note_name in item_dict['items'].items():
            self.arr_container_items.append(name)
            self.path_components.append(note_name)
        self.arr_container_items = sorted(self.arr_container_items)

    def regenerateItemsDict(self):
        items = self.settings.getSetting('items')
        items_dict = items[self.category]['items']
        items_copy = list(self.arr_container_items)
        deleted_keys = []
        for key in items_dict:
            if key in items_copy:
                items_copy[items_copy.index(key)] = None
            else:
                deleted_keys.append(key)
        for key in deleted_keys:
            del items_dict[key]
        for i in range(len(items_copy)):
            if items_copy[i] is None:
                continue
            items_dict[items_copy[i]] = self.path_components[i]
        self.settings.setSetting('items', items)
        self.settings.writeToFile()

    def getCategoryName(self):
        return self.category
