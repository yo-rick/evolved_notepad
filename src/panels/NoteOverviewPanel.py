"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""
from .BaseOverviewPanel import BaseOverviewPanel


class NoteOverviewPanel(BaseOverviewPanel):

    def __init__(self, parent, id, noteItemContainer):
        super().__init__(parent, id, "", noteItemContainer, True)
