"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 19-12-2017 | Created (everything visually     |
|                          |            | ready)                           |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 21-12-2017 | Load file and save it. Also      |
|                          |            | implemented bold text            |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 05-01-2018 | Accept file in constructor,      |
|                          |            | refactor to panel                |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 07-01-2018 | Textctrl naar richtextctrl.      |
+--------------------------+------------+----------------------------------+

"""
import os

import wx
import wx.richtext
from .BasePanel import BasePanel


class NotePanel(BasePanel):

    def __init__(self, parent, id, note_name, note_path):
        super().__init__(parent, id, 'Notitie scherm', note_name)
        self.note_path = note_path + note_name
        int_fontSize = 12 #uit instellingenscherm?
        
#fonts
        fnt_settings = wx.Font(int_fontSize, wx.FONTFAMILY_DEFAULT,
                                  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.fnt_boldKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)#self is tijdelijk
        fnt_italicKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
#text
        self.txt_titel = self.textMaker(self.getPanelTitle(), self.fnt_title)
        self.txt_versie = self.textMaker("versie 0.0.1")
#notitieveld
##        self.notitieVeld = wx.TextCtrl(self, -1,
##                                       size=(800,600), style=wx.TE_MULTILINE,
##                                       name="Note")
        self.notitieVeld = wx.richtext.RichTextCtrl(self, -1,
                                                    size=wx.Size(800,600))
        if os.path.isfile(self.note_path):
            self.notitieVeld.LoadFile(filename=self.note_path)
        self.notitieVeld.BeginFont(fnt_settings)
#buttons    
        self.btn_terug = self.buttonMaker("Terug", self.terugKnop)
        self.btn_opslaan = self.buttonMaker("Opslaan", self.opslaanKnop)
        self.btn_bold = self.buttonMaker("Bold", self.boldKnop, self.fnt_boldKnop)
        self.btn_italic = self.buttonMaker("Italic", self.italicKnop,
                                      fnt_italicKnop)
        
#boxes
        box_titelStyle = self.boxMaker([self.txt_titel, (0, 0), self.btn_italic,
                                   self.btn_bold], [20, 40, 10, 10],
                                  [wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_notitieVeld = self.boxMaker([self.notitieVeld], [10], [wx.ALL])
        box_btnsVersie = self.boxMaker([self.btn_terug, (0, 0), self.txt_versie,
                                   (0, 0), self.btn_opslaan],
                                  [10, 20, 10, 20, 10],
                                  [wx.ALL, wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_mainBox = self.boxMaker([box_titelStyle, box_notitieVeld,
                                box_btnsVersie], [10, 80, 10],
                               [wx.ALL, wx.ALL, wx.ALIGN_CENTER_HORIZONTAL],
                               wx.VERTICAL, [10,10,10])

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
        print("Italic button pressed.")
        self.notitieVeld.ApplyItalicToSelection()
        self.notitieVeld.BeginItalic()

    def boldKnop(self, event):
        #komende tekst wordt bold tot volgende klik, nu alleen selectie. OPSLAAN WERKT NIET
        print("Bold button pressed.")
        self.notitieVeld.ApplyBoldToSelection()
        self.notitieVeld.BeginBold()

    def terugKnop(self, event):
        print("Back button pressed.")
        self.GetParent().goBack()

    def opslaanKnop(self, event):
        #zet tekst uit veld in notitie bestand
        print("Save button pressed.")
        self.notitieVeld.DoSaveFile(file=self.note_path)


if __name__ == '__main__':  
    app = wx.App()  
    frame = NotePanel(None, -1, 'test', 'test')
    frame.Show()  
    app.MainLoop()
