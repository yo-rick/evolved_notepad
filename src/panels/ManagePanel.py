"""
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Initial creation                 |
+--------------------------+------------+----------------------------------+

"""

import wx
import wx.lib.scrolledpanel as scrolled

import MainFrame
from .BasePanel import BasePanel
from .BaseOverviewPanel import BaseOverviewPanel


MANAGE = "beheren"
DELETE = "Verwijderen"
ADD = "Toevoegen"
BACK = "Terug"
NAME = "naam"
NAME_TOO_SHORT = "De {}naam moet minimaal 3 en maximaal 35 tekens bevatten."
DUPLICATE_NAME = "Deze {} bestaat al"
PADDING_FLAG = wx.ALL - wx.TOP


class ManagePanel(BasePanel):

    def __init__(self, parent, id, item_container, singular, multiple):
        title = "{} {}".format(multiple, MANAGE)
        super().__init__(parent, id, title, title)
        item_container.reloadSettings()
        self.text_singular = singular
        self.text_multiple = multiple
        self.item_container = item_container
        self.marked_items = []
        # Widgets
        self.input_ctrl = wx.TextCtrl(
            self, style=wx.HSCROLL | wx.TE_PROCESS_ENTER)
        self.input_ctrl.SetMaxLength(35)
        self.scroll_panel = scrolled.ScrolledPanel(
            self, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        self.scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        self.delete_button = self.buttonMaker(DELETE, self.deleteSelection)
        # Draw screen
        self.box_container = wx.BoxSizer(wx.VERTICAL)
        self.fillBoxContainer()
        self.SetSizer(self.box_container)

    def fillBoxContainer(self):
        title_text = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.box_container.Add(title_text, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createScrollPanel()
        self.delete_button.Enable(bool(len(self.item_container.getItems())))
        self.box_container.Add(
            self.delete_button, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createNewItemSizer()
        add_button = self.buttonMaker(ADD, self.addInput)
        self.box_container.Add(add_button, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createVersionAndBack()

    def createScrollPanel(self):
        self.scroll_panel.SetAutoLayout(1)
        self.scroll_panel.SetupScrolling()
        self.scroll_panel.SetBackgroundColour((255, 255, 255))
        items = self.item_container.getItems()
        for idx in range(len(items)):
            self.scroll_sizer.Add(
                self.createSizerForItem(idx, items[idx]),
                0, wx.EXPAND)
        self.scroll_panel.SetSizer(self.scroll_sizer)
        self.box_container.Add(
            self.scroll_panel, 5, wx.EXPAND | PADDING_FLAG, 10)

    def createSizerForItem(self, idx, item):
        checkbox = wx.CheckBox(self.scroll_panel)
        label = wx.TextCtrl(self.scroll_panel, style=wx.TE_READONLY)
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
        lbl = self.textMaker("{}{}".format(self.text_singular, NAME))
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

    def refreshList(self):
        self.scroll_sizer.Layout()
        self.scroll_panel.Layout()
        self.scroll_panel.SetupScrolling(scrollToTop=False)
        self.delete_button.Enable(
            bool(len(self.item_container.getItems())))
        stack = self.GetParent().GetParent().panel_stack
        if stack and isinstance(stack[-1], BaseOverviewPanel):
            stack[-1].refreshItemList()

    def addInput(self, evt):
        text = self.input_ctrl.GetValue()
        if len(text) < 3:
            text = NAME_TOO_SHORT.format(self.text_singular.lower())
            wx.MessageDialog(self, text).ShowModal()
        elif self.item_container.hasItem(text):
            text = DUPLICATE_NAME.format(self.text_singular.lower())
            wx.MessageDialog(self, text).ShowModal()
        else:
            self.item_container.createItem(text)
            item_sizer = self.createSizerForItem(
                len(self.item_container.getItems()), text)
            self.scroll_sizer.Add(item_sizer, 0, wx.EXPAND)
            self.refreshList()

    def deleteSelection(self, evt):
        self.marked_items.sort()
        for idx in self.marked_items[::-1]:
            self.item_container.deleteItem(idx)
            self.scroll_sizer.GetItem(idx).DeleteWindows()
        self.marked_items.clear()
        self.refreshList()

    def updateCheckbox(self, evt, lbl):
        idx = self.item_container.getItems().index(lbl.GetValue())
        if evt.GetEventObject().GetValue() is True:
            lbl.SetBackgroundColour((255, 255, 0))
            self.marked_items.append(idx)
        else:
            lbl.SetBackgroundColour((255, 255, 255))
            self.marked_items.remove(idx)
