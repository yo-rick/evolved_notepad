"""
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Initial creation, basic version  |
+--------------------------+------------+----------------------------------+

"""

import wx
import wx.lib.scrolledpanel as scrolled

import MainFrame
from panels import BasePanel


MANAGE = "beheren"
DELETE = "Verwijderen"
ADD = "Toevoegen"
BACK = "Terug"
PADDING_FLAG = wx.ALL - wx.TOP


class ManagePanel(BasePanel):

    def __init__(self, parent, id, title, item_container):
        title += " " + MANAGE
        super().__init__(parent, id, title, title)
        self.item_container = item_container
        self.box_container = wx.BoxSizer(wx.VERTICAL)
        self.input_ctrl = wx.TextCtrl(self, style=wx.HSCROLL)
        self.fillBoxContainer()
        self.SetSizer(self.box_container)

    def fillBoxContainer(self):
        title_text = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.box_container.Add(title_text, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createScrollPanel()
        delete_button = self.buttonMaker(DELETE, self.deleteSelection)
        self.box_container.Add(delete_button, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createNewItemSizer()
        add_button = self.buttonMaker(ADD, self.addInput)
        self.box_container.Add(add_button, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createVersionAndBack()

    def createScrollPanel(self):
        scroll_panel = scrolled.ScrolledPanel(
            self, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        scroll_panel.SetAutoLayout(1)
        scroll_panel.SetupScrolling()
        scroll_panel.SetBackgroundColour((255, 255, 255))
        scroll_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        items = self.item_container.getItems()
        for idx in range(len(items)):
            scroll_panel_sizer.Add(
                self.createSizerForItem(scroll_panel, items[idx]),
                0, wx.EXPAND)
        scroll_panel.SetSizer(scroll_panel_sizer)
        self.box_container.Add(scroll_panel, 5, wx.EXPAND | PADDING_FLAG, 10)

    def createSizerForItem(self, scroll_panel, item):
        checkbox = wx.CheckBox(scroll_panel)
        label = wx.TextCtrl(scroll_panel, style=wx.TE_READONLY)
        label.Enable(False)
        label.SetForegroundColour((0, 0, 0))
        label.SetBackgroundColour((255, 255, 255))
        label.SetFont(self.fnt_default)
        label.SetValue(item)
        checkbox.Bind(
            wx.EVT_CHECKBOX, lambda evt: self.updateCheckbox(evt, label))
        simple_sizer = wx.BoxSizer(wx.HORIZONTAL)
        simple_sizer.Add(checkbox, 0, wx.EXPAND | wx.ALL, 5)
        simple_sizer.Add(label, 1, wx.EXPAND | (wx.ALL - wx.LEFT), 5)
        return simple_sizer

    def createNewItemSizer(self):
        lbl = self.textMaker("[TODO]", )
        vertical_wrapper = wx.BoxSizer(wx.HORIZONTAL)
        vertical_wrapper.Add(lbl, 1, wx.ALIGN_CENTER)
        wrapper = wx.BoxSizer(wx.HORIZONTAL)
        wrapper.Add(vertical_wrapper, 0, wx.EXPAND | wx.ALIGN_CENTER)
        wrapper.Add(self.input_ctrl, 1, wx.EXPAND | wx.LEFT, 5)
        self.box_container.Add(wrapper, 1, wx.EXPAND | PADDING_FLAG, 10)

    def createVersionAndBack(self):
        horizontal = wx.BoxSizer(wx.HORIZONTAL)
        horizontal.AddStretchSpacer(1)
        version_txt = self.textMaker(
            MainFrame.VERSION_STRING, style=wx.ALIGN_CENTER)
        vertical_wrapper = wx.BoxSizer(wx.HORIZONTAL)
        vertical_wrapper.Add(version_txt, 1, wx.ALIGN_CENTER)
        horizontal.Add(vertical_wrapper, 1, wx.EXPAND)
        back_button = self.buttonMaker(
            BACK, lambda evt: self.GetParent().Destroy())
        horizontal.Add(back_button, 1, wx.EXPAND)
        self.box_container.Add(horizontal, 1, wx.EXPAND | PADDING_FLAG, 10)

    def addInput(self, evt):
        raise NotImplementedError

    def deleteSelection(self, evt):
        raise NotImplementedError

    def updateCheckbox(self, evt, txt):
        if evt.GetEventObject().GetValue() is True:
            txt.SetBackgroundColour((255, 255, 0))
        else:
            txt.SetBackgroundColour((255, 255, 255))
