#!/usr/bin/python
#-----------------------------------------
#programmeur:   Datum:      Bewerking:
#Joey Nap       19-12-2017  aangemaakt(vrijwel alles visueel klaar)
#Joey Nap	21-12-2017  bestand inladen/opslaan; selectie bold maken.
#-----------------------------------------

import wx

class frm_notities(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Notitie scherm',   
                size=(800, 800))  
        pnl_mainPanel = wx.Panel(self, -1)

#instellingen
        self.str_noteNaam = "TestNotitie"#notitienaam meekrijgen uit vorig scherm? gelijk aan filenaam?
        str_noteInhoud = "Text laden mislukt."#mogelijk met self.invoerVeld.LoadFile(filename="")?
        int_fontSize = 12 #uit instellingenscherm
        
#fonts
        fnt_titel = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)
        self.fnt_boldKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)#self is tijdelijk
        fnt_italicKnop = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        fnt_default = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
#creeër functies
        def textMaker(TM_textLabel, TM_font=fnt_default):
            txt_staticText = wx.StaticText(pnl_mainPanel, -1, TM_textLabel)
            txt_staticText.SetFont(TM_font)
            return txt_staticText

        def buttonMaker(BM_btnLabel, BM_evtNaam, BM_lblFont=fnt_default):
            btn_button = wx.Button(pnl_mainPanel, -1, BM_btnLabel)
            self.Bind(wx.EVT_BUTTON, BM_evtNaam, btn_button)
            btn_button.SetFont(BM_lblFont)
            btn_button.SetDefault()
            return btn_button

        def boxMaker(BxM_itemList, BxM_size, BxM_flagList,
                     BxM_rotatie=wx.HORIZONTAL,
                     BxM_borderList=False):
            if BxM_borderList == False:
                BxM_borderList = [1]*len(BxM_itemList)
            box_newSizer = wx.BoxSizer(BxM_rotatie)
            for Pos in range(0, len(BxM_itemList)):
                box_newSizer.Add(BxM_itemList[Pos], BxM_size[Pos],
                                 flag=BxM_flagList[Pos],
                                 border=BxM_borderList[Pos])
            return box_newSizer
#text
        self.txt_titel = textMaker(self.str_noteNaam, fnt_titel)
        self.txt_versie = textMaker("versie 0.0.1")
#notitieveld
        self.notitieVeld = wx.TextCtrl(pnl_mainPanel, -1,
                                       value=str_noteInhoud,
                                       size=(800,600), style=wx.TE_MULTILINE,
                                       name="Note")
        self.notitieVeld.LoadFile(filename=self.str_noteNaam)
#buttons    
        self.btn_terug = buttonMaker("Terug", self.terugKnop)
        self.btn_opslaan = buttonMaker("Opslaan", self.opslaanKnop)
        self.btn_bold = buttonMaker("Bold", self.boldKnop, self.fnt_boldKnop)
        self.btn_italic = buttonMaker("Italic", self.italicKnop,
                                      fnt_italicKnop)
        
#boxes
        box_titelStyle = boxMaker([self.txt_titel, (0, 0), self.btn_italic,
                                   self.btn_bold], [20, 40, 10, 10],
                                  [wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_notitieVeld = boxMaker([self.notitieVeld], [10], [wx.ALL])
        box_btnsVersie = boxMaker([self.btn_terug, (0, 0), self.txt_versie,
                                   (0, 0), self.btn_opslaan],
                                  [10, 20, 10, 20, 10],
                                  [wx.ALL, wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_mainBox = boxMaker([box_titelStyle, box_notitieVeld,
                                box_btnsVersie], [10, 80, 10],
                               [wx.ALL, wx.ALL, wx.ALIGN_CENTER_HORIZONTAL],
                               wx.VERTICAL, [10,10,10])

        pnl_mainPanel.SetSizer(box_mainBox)

    def italicKnop(self, event):
        #komende tekst wordt italic tot volgende klik
        #wx.TE_RICH bij textctrl met <i></i> en <b></b>?
        #self.notitieVeld.SetDefaultStyle(wx.TextAttr(wx.NullColour, font=<font>))
        self.btn_italic.SetLabel("Clicked")

    def boldKnop(self, event):
        #komende tekst wordt bold tot volgende klik, nu alleen selectie. OPSLAAN WERKT NIET
        tpl_selectPos = self.notitieVeld.GetSelection()
        if tpl_selectPos[0] != tpl_selectPos[1]:
            str_selectie = self.notitieVeld.GetStringSelection()
            self.notitieVeld.SetDefaultStyle(wx.TextAttr(wx.NullColour,font=
                                                         self.fnt_boldKnop))
            self.notitieVeld.Replace(tpl_selectPos[0], tpl_selectPos[1],
                                     str_selectie)
        self.btn_bold.SetLabel("Clicked")

    def terugKnop(self, event):
        #naar vorige scherm
        self.btn_terug.SetLabel("Clicked")

    def opslaanKnop(self, event):
        #zet tekst uit veld in notitie bestand
        self.btn_opslaan.SetLabel("Clicked")
        self.notitieVeld.SaveFile(filename=self.str_noteNaam)

if __name__ == '__main__':  
    app = wx.App()  
    frame = frm_notities()  
    frame.Show()  
    app.MainLoop()
