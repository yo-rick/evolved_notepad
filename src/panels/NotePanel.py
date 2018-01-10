"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 19-12-2017 | Created (everything visually     |
|                          |            | ready                            |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 21-12-2017 | Load file and save it. Also      |
|                          |            | implemented bold text            |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 05-01-2018 | Accept file in constructor,      |
|                          |            | refactor to panel                |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 07-01-2018 | Textctrl to richtextctrl.        |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 09-01-2018 | Reverted back to Textctrl. Also  |
|                          |            | implemented italic to selection. |
+--------------------------+------------+----------------------------------+

"""
import os

import wx

import MainFrame
from .BasePanel import BasePanel


class NotePanel(BasePanel):

    def __init__(self, parent, id, note_name, note_path):
        super().__init__(parent, id, 'Notitie scherm', note_name)
        self.note_path = note_path
#fonts
        boldBtnFont = self.fontMaker(FM_weight=wx.FONTWEIGHT_BOLD)
        italBtnFont = self.fontMaker(FM_style=wx.FONTSTYLE_ITALIC)
        self.settingsFont = self.fontMaker()
#text
        self.txt_titel = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.txt_versie = self.textMaker(MainFrame.VERSION_STRING)
#notitieveld
        self.notitieVeld = wx.TextCtrl(self, -1,
                                       size=(800,600), style=wx.TE_MULTILINE,
                                       name="Note")
        self.notitieVeld.SetFont(self.settingsFont)
        self.bold = False
        if os.path.isfile(self.note_path):
            self.notitieVeld.LoadFile(filename=self.note_path)
#buttons    
        self.btn_terug = self.buttonMaker("Terug", self.terugKnop)
        self.btn_opslaan = self.buttonMaker("Opslaan", self.opslaanKnop)
        self.btn_bold = self.buttonMaker("Bold", self.boldKnop,
                                         boldBtnFont)
        self.btn_italic = self.buttonMaker("Italic", self.italicKnop,
                                           italBtnFont)
#boxes
        box_titelStyle = self.boxMaker([self.txt_titel, (0, 0), self.btn_italic,self.btn_bold], [20, 40, 10, 10],[wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_notitieVeld = self.boxMaker([self.notitieVeld], [10], [wx.ALL])
        box_btnsVersie = self.boxMaker([self.btn_terug, (0, 0), self.txt_versie,(0, 0), self.btn_opslaan],[10, 20, 10, 20, 10],[wx.ALL, wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_mainBox = self.boxMaker([box_titelStyle, box_notitieVeld,box_btnsVersie], [10, 80, 10],[wx.ALL, wx.ALL, wx.ALIGN_CENTER_HORIZONTAL],wx.VERTICAL, [10,10,10])

        self.SetSizer(box_mainBox)

    def boxMaker(self, BxM_itemList, BxM_size, BxM_flagList,
                 BxM_rotatie=wx.HORIZONTAL, BxM_borderList=False):
        if BxM_borderList == False:
            BxM_borderList = [1] * len(BxM_itemList)
        box_newSizer = wx.BoxSizer(BxM_rotatie)
        for Pos in range(0, len(BxM_itemList)):
            box_newSizer.Add(
                BxM_itemList[Pos], BxM_size[Pos], flag=BxM_flagList[Pos],
                border=BxM_borderList[Pos])
        return box_newSizer

    def italicKnop(self, event):
        print("Clicked italic")
        tpl_selectPos = self.notitieVeld.GetSelection()
        if tpl_selectPos[0] != tpl_selectPos[1]:
            self.notitieVeld.SetStyle(tpl_selectPos[0], tpl_selectPos[1],wx.TextAttr(wx.NullColour,font=self.fontMaker(FM_style=wx.FONTSTYLE_ITALIC)))

    def boldKnop(self, event):
        print("Clicked bold")
        tpl_selection = self.notitieVeld.GetSelection()
        if tpl_selection[0] != tpl_selection[1]:
            self.notitieVeld.SetStyle(tpl_selection[0], tpl_selection[1],wx.TextAttr(wx.NullColour,font=self.fontMaker(FM_weight=wx.FONTWEIGHT_BOLD)))

    def terugKnop(self, event):
        print("Clicked Back")
        self.GetParent().goBack()

    def opslaanKnop(self, event):
        print("Clicked save")
        if self.note_path:
            open(self.note_path, 'a').close()
        self.notitieVeld.SaveFile(filename=self.note_path)


if __name__ == '__main__':  
    app = wx.App()  
    frame = NotePanel(None, -1, 'test', 'test')
    frame.Show()  
    app.MainLoop()
