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
| Tjardo Maarseveen        | 20-12-2017 | Updated layout and added Scroll- |
|                          |            | panel with buttons               |
+--------------------------+------------+----------------------------------+

"""
import wx
import wx.lib.scrolledpanel as scrolled
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

        pnl_scroll = scrolled.ScrolledPanel(self, -1, size=(780, 500),
                                        pos=(10, 100), style=wx.SIMPLE_BORDER)
        pnl_scroll.SetupScrolling()
        pnl_scroll.SetBackgroundColour('#FFFFFF')

        button1 = wx.Button(pnl_scroll, label="Categorie 1", pos=(0, 50),
                            size=(750, 75))
        button2 = wx.Button(pnl_scroll, label="Categorie 2", pos=(0, 100),
                            size=(750, 75))
        button3 = wx.Button(pnl_scroll, label="Categorie 3", pos=(0, 150),
                            size=(750, 75))
        button4 = wx.Button(pnl_scroll, label="Categorie 4", pos=(0, 200),
                            size=(750, 75))
        button5 = wx.Button(pnl_scroll, label="Categorie 5", pos=(0, 250),
                            size=(750, 75))
        button6 = wx.Button(pnl_scroll, label="Categorie 6", pos=(0, 300),
                            size=(750, 75))
        button7 = wx.Button(pnl_scroll, label="Categorie 7", pos=(0, 350),
                            size=(750, 75))
        button8 = wx.Button(pnl_scroll, label="Categorie 8", pos=(0, 400),
                            size=(750, 75))

        bSizer = wx.BoxSizer(wx.VERTICAL)
        bSizer.Add(button1, 0, wx.ALL, 5)
        bSizer.Add(button2, 0, wx.ALL, 5)
        bSizer.Add(button3, 0, wx.ALL, 5)
        bSizer.Add(button4, 0, wx.ALL, 5)
        bSizer.Add(button5, 0, wx.ALL, 5)
        bSizer.Add(button6, 0, wx.ALL, 5)
        bSizer.Add(button7, 0, wx.ALL, 5)
        bSizer.Add(button8, 0, wx.ALL, 5)
        pnl_scroll.SetSizer(bSizer)

        self.txt_title = self.textMaker("Categorieën", self.fnt_title)
        self.txt_version = self.textMaker(self.version, self.fnt_default)
        self.vbox_overview = wx.BoxSizer(wx.VERTICAL)
        self.btn_settings = self.buttonMaker("Instellingen",
                                self.instellingenKnop, self.fnt_default)
        self.btn_edit = self.buttonMaker("Beheren", self.beherenKnop,
                                self.fnt_default)
        self.searchbar = wx.TextCtrl(self, -1, value="Zoeken in categorieën",
                                size=(200, 50), name="zoekterm")
        self.generateTitleBox()
        self.generateScrollPanel()
        self.generateButtonBox()
        self.SetSizer(self.vbox_overview)

    def generateTitleBox(self):
        self.vbox_overview.Add(wx.StaticText(self, -1, ""), .1, wx.LEFT)
        hbox_title = wx.BoxSizer(wx.HORIZONTAL)
        hbox_title.Add(wx.StaticText(self, -1, ""), 1, wx.EXPAND)
        hbox_title.Add(self.txt_title, 1, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, -1, ""), 8, wx.EXPAND)
        hbox_title.Add(self.searchbar, 1, wx.TOP)
        hbox_title.Add(wx.StaticText(self, -1, ""), 1, wx.EXPAND)
        self.vbox_overview.Add(hbox_title, 1, wx.CENTRE | wx.ALL)

    def generateScrollPanel(self):
        self.vbox_overview.Add(wx.StaticText(self, -1, ""), .1, wx.LEFT)
        self.vbox_overview.Add(wx.StaticText(self, -1, ""), 4,
                               wx.CENTRE)

    def generateButtonBox(self):
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 1, wx.CENTRE)
        hbox_buttons.Add(self.btn_settings, 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 3, wx.EXPAND)
        hbox_buttons.Add(self.txt_version, 1, wx.CENTRE | wx.BOTTOM)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 3, wx.EXPAND)
        hbox_buttons.Add(self.btn_edit, 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, -1, ""), 1, wx.CENTRE)
        self.vbox_overview.Add(hbox_buttons, 1, wx.EXPAND | wx.ALL)

    def instellingenKnop(self, event):
        #naar instellingen scherm
        self.btn_settings.SetLabel("Clicked")

    def beherenKnop(self, event):
        #naar beheren scherm
        self.btn_edit.SetLabel("Clicked")

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, -1, "Overzichtscherm")
    paneeltje = BaseOverviewPanel(frame, -1, "Overzichtscherm",  [])
    frame.Show(True)
    app.MainLoop()
