"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Tjardo Maarseveen        | 18-12-2017 | Creating the basic layout of     |
|                          |            | the BaseOverviewPanel            |
+--------------------------+------------+----------------------------------+

"""
import wx
from MainFrame import MainFrame
from panels.BasePanel import BasePanel


class BaseOverviewPanel(BasePanel):

    #   TO DO :
    # Show the contents of the itemContainer
    # Also show the default buttons
    # version_nr -> later globaal

    def __init__(self, parent, id, title, itemContainer, showBackButton=False):
        super().__init__(parent, id, title)
        self.itemContainer = itemContainer
        self.showBackButton = showBackButton
        self.version_nr = wx.StaticText(self, -1, "Versie 1.2")
        self.vbox_overview = wx.BoxSizer(wx.VERTICAL)
        self.btn_settings = wx.Button(self, -1, "Instellingen")
        self.btn_edit = wx.Button(self, -1, "Beheren")
        self.generateTitleBox()
        self.generateScrollPanel()
        self.generateButtonBox()
        self.SetSizer(self.vbox_overview)

    def generateTitleBox(self):
        self.vbox_overview.Add(wx.StaticText(self, -1, ""), .1, wx.LEFT)
        hbox_title = wx.BoxSizer(wx.HORIZONTAL)
        hbox_title.Add(wx.StaticText(self, -1, ""), 1, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, -1, "Categorieen"), 1, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, -1, ""), 8, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, -1, "[Zoekfunctie]"), 1, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, -1, ""), 1, wx.EXPAND)
        self.vbox_overview.Add(hbox_title, 1, wx.CENTRE | wx.ALL)

    def generateScrollPanel(self):
        self.vbox_overview.Add(wx.StaticText(self, -1, ""), .1, wx.LEFT)
        self.vbox_overview.Add(wx.StaticText(self, -1, "[Scroll paneel]"), 4,
                               wx.CENTRE)

    def generateButtonBox(self):
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 1, wx.CENTRE)
        hbox_buttons.Add(self.btn_settings, 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 3, wx.EXPAND)
        hbox_buttons.Add(self.version_nr, 1, wx.CENTRE | wx.BOTTOM)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 3, wx.EXPAND)
        hbox_buttons.Add(self.btn_edit, 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 1, wx.CENTRE)
        self.vbox_overview.Add(hbox_buttons, 1, wx.EXPAND | wx.ALL)

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, -1, "Overzichtscherm")
    paneeltje = BaseOverviewPanel(frame, -1, "Overzichtscherm",  [])
    frame.Show(True)
    app.MainLoop()
