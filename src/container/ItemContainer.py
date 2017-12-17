"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""


class ItemContainer(object):

    def __init__(self):
        self.arr_container_items = []

    def clickItem(self, item):
        raise NotImplementedError

    def createItem(self, item):
        raise NotImplementedError

    def deleteItem(self, item):
        raise NotImplementedError

    def fillContainer(self):
        raise NotImplementedError
