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
| Wesley Ameling           | 29-12-2017 | Moved starting to the MainFrame, |
|                          |            | implement ItemContainer usage,   |
|                          |            | improved the GUI for flexibility,|
|                          |            | added the back button and added  |
|                          |            | action for the settings button.  |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 03-01-2018 | Remove unnecessary Layout        |
+--------------------------+------------+----------------------------------+

"""
import wx
import wx.lib.scrolledpanel as scrolled

import MainFrame
from SettingsFrame import SettingsFrame
from panels.BasePanel import BasePanel


SETTINGS = "Instellingen"
MANAGE = "Beheren"
SEARCH_TEXT = "Zoeken in "
CATEGORIES = "categorieën"
BACK = "Terug"


class BaseOverviewPanel(BasePanel):

    def __init__(self, parent, id, frame_title, panel_title, item_container,
                 show_back_button=False):
        super().__init__(parent, id, frame_title, panel_title)
        self.item_container = item_container
        self.show_back_button = show_back_button
        # Layout
        self.pnl_scroll = scrolled.ScrolledPanel(
            self, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        self.txt_title = self.textMaker(panel_title, self.fnt_title)
        self.vbox_overview = wx.BoxSizer(wx.VERTICAL)
        search_bar_text = SEARCH_TEXT + (
            panel_title if show_back_button else CATEGORIES)
        self.searchbar = wx.TextCtrl(
            self, wx.ID_ANY, value=search_bar_text, size=(200, 50))
        self.searchbar.Bind(wx.EVT_KEY_UP, self.onUpdateField)
        self.generateTitleBox()
        self.setupScrollPanel()
        self.generateButtonBox()
        self.SetSizer(self.vbox_overview)

    def updateItemList(self, search_term):
        children = self.pnl_scroll.GetChildren()
        for idx in range(len(children)):
            child = children[idx]
            if search_term in child.GetLabel():
                child.SetPosition((0, 50 + 50 * idx))
                self.bSizer.Show(child)
            else:
                self.bSizer.Hide(child)
        self.pnl_scroll.SetSizer(self.bSizer)
        self.pnl_scroll.Layout()

    def generateTitleBox(self):
        self.vbox_overview.Add(wx.StaticText(self, wx.ID_ANY, ""), .1, wx.LEFT)
        hbox_title = wx.BoxSizer(wx.HORIZONTAL)
        hbox_title.Add(wx.StaticText(self, wx.ID_ANY, ""), 1, wx.EXPAND)
        hbox_title.Add(self.txt_title, 1, wx.EXPAND)
        hbox_title.Add(wx.StaticText(self, wx.ID_ANY, ""), 8, wx.EXPAND)
        hbox_title.Add(self.searchbar, 1, wx.TOP)
        hbox_title.Add(wx.StaticText(self, wx.ID_ANY, ""), 1, wx.EXPAND)
        self.vbox_overview.Add(hbox_title, 1, wx.CENTRE | wx.ALL)

    def setupScrollPanel(self):
        self.pnl_scroll.SetupScrolling()
        self.pnl_scroll.SetBackgroundColour((255, 255, 255))
        self.bSizer = wx.BoxSizer(wx.VERTICAL)
        items = self.item_container.getItems()
        for idx in range(len(items)):
            btn_item = wx.Button(self.pnl_scroll, label=items[idx],
                                 pos=(0, 50 + 50 * idx), size=(0, 40))
            btn_item.Bind(wx.EVT_BUTTON,
                          lambda event, idx=idx: self.itemButton(event, idx))
            self.bSizer.Add(btn_item, 0, wx.EXPAND | wx.ALL, 5)
        self.pnl_scroll.SetSizer(self.bSizer)
        flags = wx.EXPAND | wx.LEFT | wx.RIGHT
        self.vbox_overview.Add(self.pnl_scroll, 7, flags, 10)

    def generateButtonBox(self):
        txt_version = self.textMaker(
            MainFrame.VERSION_STRING, self.fnt_default)
        btn_settings = self.buttonMaker(
            SETTINGS, self.settingsButton, self.fnt_default)
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        hbox_buttons.Add(wx.StaticText(self, wx.ID_ANY, ""), 1, wx.CENTRE)
        hbox_buttons.Add(btn_settings, 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, wx.ID_ANY, ""), 3, wx.EXPAND)
        hbox_buttons.Add(txt_version, 1, wx.CENTRE | wx.BOTTOM)
        hbox_buttons.Add(wx.StaticText(self, wx.ID_ANY, ""), 3, wx.EXPAND)
        hbox_buttons.Add(self.generateManageButton(), 5, wx.CENTRE)
        hbox_buttons.Add(wx.StaticText(self, wx.ID_ANY, ""), 1, wx.CENTRE)
        self.vbox_overview.Add(hbox_buttons, 1, wx.EXPAND | wx.ALL)

    def generateManageButton(self):
        vbox_manage = wx.BoxSizer(wx.VERTICAL)
        btn_manage = self.buttonMaker(
            MANAGE, self.manageButton, self.fnt_default)
        vbox_manage.Add(btn_manage, 1, wx.EXPAND)
        if self.show_back_button:
            btn_back = self.buttonMaker(
                BACK, self.backButton, self.fnt_default)
            vbox_manage.Add(btn_back, 1, wx.EXPAND)
        return vbox_manage


    def settingsButton(self, event):
        SettingsFrame(self.GetParent(), wx.ID_ANY)

    def manageButton(self, event):
        #naar beheren scherm
        print(MANAGE)

    def backButton(self, event):
        self.GetParent().goBack()

    def itemButton(self, event, id):
        self.item_container.clickItem(id)

    def onUpdateField(self, event):
        self.updateItemList(self.searchbar.GetValue())
        event.Skip()
