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


class CategoryItemContainer(ItemContainer):

    def __init__(self, categoryFolder):
        super().__init__()
        self.folder = categoryFolder

    def clickItem(self, item):
        # create the NoteItemContainer
        # create the NoteOverviewPanel
        # show it using the frame
        pass

    def createItem(self, item):
        pass

    def deleteItem(self, item):
        pass

    def fillContainer(self):
        pass
