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
"""


class ItemContainer(object):

    def __init__(self):
        self.arr_container_items = []
        self.fillContainer()

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
