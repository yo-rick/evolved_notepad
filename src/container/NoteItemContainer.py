"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""
from .ItemContainer import ItemContainer


class NoteItemContainer(ItemContainer):

    def __init__(self, noteFolder):
        super().__init__()
        self.noteFolder = noteFolder

    def clickItem(self, item):
        pass

    def createItem(self, item):
        pass

    def deleteItem(self, item):
        pass

    def fillContainer(self):
        pass
