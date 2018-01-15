"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Modify the interface so it fits  |
|                          |            | needs of the BaseOverviewPanel.  |
|                          |            | Now uses an index on clickItem   |
|                          |            | and deleteItem with a check      |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Tweaked the size of the frame and|
|                          |            | added a hasItem method.          |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 05-01-2018 | Rename dirs list                 |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 14-01-2018 | Add settings                     |
+--------------------------+------------+----------------------------------+

"""
from settings import Settings


class ItemContainer(object):

    def __init__(self):
        self.arr_container_items = []
        self.path_components = []
        self.main_frame = None
        self.settings = Settings()

    def getItems(self):
        # Copy so nothing can be added to this list
        return list(self.arr_container_items)

    def check_index_bounds(self, index):
        if index < 0 or index >= len(self.arr_container_items):
            raise IndexError

    def clickItem(self, index):
        self.check_index_bounds(index)

    def createItem(self, new_item):
        raise NotImplementedError

    def deleteItem(self, index):
        self.check_index_bounds(index)

    def fillContainer(self):
        raise NotImplementedError

    def hasItem(self, item):
        return item in self.arr_container_items

    def setMainFrame(self, frame):
        self.main_frame = frame

    def reloadSettings(self):
        self.settings = Settings()
