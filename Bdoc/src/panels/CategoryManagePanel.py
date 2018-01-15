"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Add CategoryManagePanel          |
+--------------------------+------------+----------------------------------+

"""
from .ManagePanel import ManagePanel

CATEGORY = "Categorie"
CATEGORIES = "Categorieën"


class CategoryManagePanel(ManagePanel):

    def __init__(self, parent, id, item_container):
        super().__init__(parent, id, item_container, CATEGORY, CATEGORIES)
