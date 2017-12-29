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

"""
import os

from .ItemContainer import ItemContainer


class NoteItemContainer(ItemContainer):

    def __init__(self, noteFolder):
        self.noteFolder = noteFolder
        super().__init__()

    def clickItem(self, index):
        super().clickItem(index)

    def createItem(self, new_item):
        pass

    def deleteItem(self, index):
        super().clickItem(index)

    def fillContainer(self):
        pass

    def getCategoryName(self):
        return os.path.basename(self.noteFolder)
