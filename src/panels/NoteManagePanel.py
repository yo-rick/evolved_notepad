"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Add NoteManagePanel              |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 13-01-2018 | Reload settings on launch        |
+--------------------------+------------+----------------------------------+

"""
from .ManagePanel import ManagePanel

NOTE = "Notitie "
NOTES = "Notities"


class NoteManagePanel(ManagePanel):

    def __init__(self, parent, id, item_container):
        super().__init__(parent, id, item_container, NOTE, NOTES)
        item_container.reloadSettings()

