"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""
from container import CategoryItemContainer
from settings import Settings
from .BaseOverviewPanel import BaseOverviewPanel


class CategoryOverviewPanel(BaseOverviewPanel):

    def __init__(self, parent, id):
        directoryPath = Settings.getInstance().getSetting('path')
        categoryItemContainer = CategoryItemContainer(directoryPath)
        super().__init__(parent, id, "", categoryItemContainer, False)
