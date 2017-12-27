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
| Tjardo Maarseveen        | 22-12-2017 | Creating a working search bar    |
|                          |            | with event                       |
+--------------------------+------------+----------------------------------+
| Tjardo Maarseveen        | 27-12-2017 | Making it possible to filter item|
|                          |            | list with search bar             |
+--------------------------+------------+----------------------------------+

"""
import wx
import wx.lib.scrolledpanel as scrolled
from MainFrame import MainFrame
from panels.BasePanel import BasePanel

class BaseOverviewPanel(BasePanel):

    #   TO DO :
    # Show the contents of the itemContainer
    # Krijg GTK critical bij scrollen in gefilterde lijst (met zoekterm)

    def __init__(self, parent, id, title, itemContainer, showBackButton=False):
        super().__init__(parent, id, title)
        self.itemContainer = itemContainer
        self.showBackButton = showBackButton
        self.makeScrollPanel(itemContainer)
        self.txt_title = self.textMaker(title, self.fnt_title)
        self.txt_version = self.textMaker(self.version, self.fnt_default)
        self.vbox_overview = wx.BoxSizer(wx.VERTICAL)
        self.btn_settings = self.buttonMaker("Instellingen",
                                self.instellingenKnop, self.fnt_default)
        self.btn_edit = self.buttonMaker("Beheren", self.beherenKnop,
                                self.fnt_default)
        self.searchbar = wx.TextCtrl(self, -1, value="Zoeken in categorieën",
                                size=(200, 50), name="zoekterm")
        self.searchbar.Bind(wx.EVT_KEY_UP, self.onUpdateField)
        self.generateTitleBox()
        self.generateScrollPanel()
        self.generateButtonBox()
        self.SetSizer(self.vbox_overview)

    def makeScrollPanel(self, itemContainer):
        self.pnl_scroll = scrolled.ScrolledPanel(self, -1, size=(780, 500),
                                            pos=(10, 100),
                                            style=wx.SIMPLE_BORDER)
        self.pnl_scroll.SetupScrolling()
        self.pnl_scroll.SetBackgroundColour('#FFFFFF')
        self.generateItemList(itemContainer)


    def generateItemList(self, itemContainer):
        self.bSizer = wx.BoxSizer(wx.VERTICAL)
        for x in range(len(itemContainer)):
            btn_item = wx.Button(self.pnl_scroll, label=itemContainer[x],
                                 pos=(0, 50 + 50 * x), size=(750, 75))
            btn_item.Bind(wx.EVT_BUTTON,
                          lambda event, temp=x: self.itemKnop(event, temp))
            self.bSizer.Add(btn_item, 0, wx.ALL, 5)
        self.pnl_scroll.SetSizer(self.bSizer)
        self.pnl_scroll.Layout()

    def updateItemList(self, search_term):
        children = self.pnl_scroll.GetChildren()
        teller = 0
        for child in children:
            if (search_term.lower() ==
                    child.GetLabel()[:len(search_term)].lower()):
                child.SetPosition((0, 50 + 50 * teller))
                self.bSizer.Show(child)
            else :
                self.bSizer.Hide(child)
            teller += 1
        self.pnl_scroll.SetSizer(self.bSizer)
        self.pnl_scroll.Layout()


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

    def itemKnop(self, event, id):
        # naar item scherm (categorie/ notitie)
        print(self.itemContainer[id])

    def onUpdateField(self, event):
        self.updateItemList(self.searchbar.GetValue())
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, -1, "Overzichtscherm")
    paneeltje = BaseOverviewPanel(frame, -1, "Categorieën",
                                  ["Categorie1", "Categorie2", "Categorie3",
                                   "Categorie4", "Categorie5", "Groep6",
                                   "Groep7"])
    # uiteindelijk self.arr_container_items meegeven aan paneeltje
    frame.Show(True)
    app.MainLoop()
