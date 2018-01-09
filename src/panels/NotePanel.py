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
| Joey Nap                 | 09-01-2018 | Reverted back to Textctrl.       |
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
        int_fontSize = 12 #uit instellingenscherm
#fonts
        fnt_settings = wx.Font(int_fontSize, wx.FONTFAMILY_DEFAULT,
                                  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.fnt_boldKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)#self is tijdelijk
        fnt_italicKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
#text
        self.txt_titel = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.txt_versie = self.textMaker(MainFrame.VERSION_STRING)
#notitieveld
        self.notitieVeld = wx.TextCtrl(self, -1,
                                       size=(800,600), style=wx.TE_MULTILINE,
                                       name="Note")
        if os.path.isfile(self.note_path):
            self.notitieVeld.LoadFile(filename=self.note_path)
#buttons    
        self.btn_terug = self.buttonMaker("Terug", self.terugKnop)
        self.btn_opslaan = self.buttonMaker("Opslaan", self.opslaanKnop)
        self.btn_bold = self.buttonMaker("Bold", self.boldKnop,
                                         self.fnt_boldKnop)
        self.btn_italic = self.buttonMaker("Italic", self.italicKnop,
                                      fnt_italicKnop)
        
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
        #komende tekst wordt italic tot volgende klik
        #self.notitieVeld.SetDefaultStyle(wx.TextAttr(wx.NullColour, font=<font>))
        print("Clicked italic")

    def boldKnop(self, event):
        #komende tekst wordt bold tot volgende klik, nu alleen selectie. OPSLAAN WERKT NIET
        print("Clicked bold")
        tpl_selectPos = self.notitieVeld.GetSelection()
        if tpl_selectPos[0] != tpl_selectPos[1]:
            str_selectie = self.notitieVeld.GetStringSelection()
            self.notitieVeld.SetDefaultStyle(wx.TextAttr(wx.NullColour,font=
                                                         self.fnt_boldKnop))
            self.notitieVeld.Replace(tpl_selectPos[0], tpl_selectPos[1],
                                     str_selectie)

    def terugKnop(self, event):
        print("Clicked Back")
        self.GetParent().goBack()

    def opslaanKnop(self, event):
        #zet tekst uit veld in notitie bestand
        print("Clicked save")
        if self.note_path:
            open(self.note_path, 'a').close()
        self.notitieVeld.SaveFile(filename=self.note_path)


if __name__ == '__main__':  
    app = wx.App()  
    frame = NotePanel(None, -1, 'test', 'test')
    frame.Show()  
    app.MainLoop()
