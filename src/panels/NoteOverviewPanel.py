"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Add string constant and add      |
|                          |            | panel title for the category     |
+--------------------------+------------+----------------------------------+

"""
from .BaseOverviewPanel import BaseOverviewPanel


CATEGORY_SCREEN = "Categorie scherm"


class NoteOverviewPanel(BaseOverviewPanel):

    def __init__(self, parent, id, note_item_container):
        super().__init__(
            parent, id, CATEGORY_SCREEN,
            note_item_container.getCategoryName(), note_item_container, True)
