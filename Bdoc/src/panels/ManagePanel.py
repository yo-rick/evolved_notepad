"""
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 04-01-2018 | Initial creation                 |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 14-01-2018 | Edit so this can be used as      |
|                          |            | a regular panel, add unavailable |
|                          |            | message                          |
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
        self.arr_marked_items = []
        self.added_message = False
        # Widgets
        self.input_ctrl = wx.TextCtrl(
            self, style=wx.HSCROLL | wx.TE_PROCESS_ENTER)
        self.input_ctrl.SetMaxLength(35)
        self.sp_manage = scrolled.ScrolledPanel(
            self, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        self.scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        self.btn_delete = self.buttonMaker(DELETE, self.deleteSelection)
        self.unavailable_text = text = self.textMaker(
            "Er zijn geen " + self.text_multiple.lower(),
            parent=self.sp_manage)
        # Draw screen
        self.box_container = wx.BoxSizer(wx.VERTICAL)
        self.fillBoxContainer()
        self.SetSizer(self.box_container)

    def fillBoxContainer(self):
        title_text = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.box_container.Add(title_text, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createScrollPanel()
        self.btn_delete.Enable(bool(len(self.item_container.getItems())))
        self.box_container.Add(
            self.btn_delete, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.createNewItemSizer()
        btn_add = self.buttonMaker(ADD, self.addInput)
        self.box_container.Add(btn_add, 1, wx.EXPAND | PADDING_FLAG, 10)
        self.box_container.AddStretchSpacer(2)
        self.createVersionAndBack()

    def createScrollPanel(self):
        self.sp_manage.SetAutoLayout(1)
        self.sp_manage.SetupScrolling()
        self.sp_manage.SetBackgroundColour((255, 255, 255))
        arr_items = self.item_container.getItems()
        self.scroll_sizer.Add(self.unavailable_text, 1, wx.CENTER, 5)
        for idx in range(len(arr_items)):
            self.scroll_sizer.Add(
                self.createSizerForItem(idx, arr_items[idx]),
                0, wx.EXPAND)
        self.sp_manage.SetSizer(self.scroll_sizer)
        self.box_container.Add(
            self.sp_manage, 5, wx.EXPAND | PADDING_FLAG, 10)
        self.refreshList()

    def createSizerForItem(self, idx, item):
        checkbox = wx.CheckBox(self.sp_manage)
        lbl_manage = wx.TextCtrl(self.sp_manage, style=wx.TE_READONLY)
        lbl_manage.Enable(False)
        lbl_manage.SetForegroundColour((0, 0, 0))
        lbl_manage.SetBackgroundColour((255, 255, 255))
        lbl_manage.SetFont(self.fnt_default)
        lbl_manage.SetValue(item)
        checkbox.Bind(
            wx.EVT_CHECKBOX, lambda evt: self.updateCheckbox(evt, lbl_manage))
        simple_sizer = wx.BoxSizer(wx.HORIZONTAL)
        simple_sizer.Add(checkbox, 0, wx.EXPAND | wx.ALL, 5)
        simple_sizer.Add(lbl_manage, 1, wx.EXPAND | (wx.ALL - wx.LEFT), 5)
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
        overview_panel = self.GetParent().arr_panel_stack[-1]
        btn_back = self.buttonMaker(
            BACK, lambda evt:
            overview_panel.refreshItemList() or self.GetParent().goBack())
        horizontal.Add(btn_back, 1, wx.EXPAND)
        self.box_container.Add(horizontal, 1, wx.EXPAND | PADDING_FLAG, 10)

    def refreshList(self):
        got_items = bool(len(self.item_container.getItems()))
        self.btn_delete.Enable(got_items)
        self.unavailable_text.Show(not got_items)
        self.scroll_sizer.Layout()
        self.sp_manage.Layout()
        self.sp_manage.SetupScrolling(scrollToTop=False)

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
        self.arr_marked_items.sort()
        for idx in self.arr_marked_items[::-1]:
            self.item_container.deleteItem(idx)
            self.scroll_sizer.GetItem(idx + 1).DeleteWindows()
        self.arr_marked_items.clear()
        self.refreshList()

    def updateCheckbox(self, evt, lbl):
        idx = self.item_container.getItems().index(lbl.GetValue())
        if evt.GetEventObject().GetValue() is True:
            lbl.SetBackgroundColour((255, 255, 0))
            self.arr_marked_items.append(idx)
        else:
            lbl.SetBackgroundColour((255, 255, 255))
            self.arr_marked_items.remove(idx)
