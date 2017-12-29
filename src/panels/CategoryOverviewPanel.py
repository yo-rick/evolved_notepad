"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Add constants for interface      |
|                          |            | strings and add a new panel title|
+--------------------------+------------+----------------------------------+

"""
from container import CategoryItemContainer
from settings import Settings
from .BaseOverviewPanel import BaseOverviewPanel


OVERVIEW_SCREEN = "Overzicht scherm"
CATEGORIES = "Categorieën"


class CategoryOverviewPanel(BaseOverviewPanel):

    def __init__(self, parent, id):
        directory_path = Settings.getInstance().getSetting('path')
        category_item_container = CategoryItemContainer(directory_path)
        category_item_container.setMainFrame(parent)
        super().__init__(parent, id, OVERVIEW_SCREEN, CATEGORIES,
                         category_item_container, False)
