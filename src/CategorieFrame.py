#!/usr/bin/python
#-----------------------------------------
#programmeur:   Bewerking:      Datum:
#Joey Nap       Begin           19-12-2017
#-----------------------------------------

import wx

class frm_notities(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Overzicht scherm',   
                size=(800, 800))  
        pnl_mainPanel = wx.Panel(self, -1)

#fonts
        fnt_titel = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)
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

#texts
        self.txt_titel = textMaker("Categorieën", fnt_titel)
        self.txt_versie = textMaker("versie 0.0.1")
        self.txt_categorie = textMaker("Hier komen categorieën")#tijdelijk
        
        self.zoekBalk = wx.TextCtrl(pnl_mainPanel, -1,
                                    value="Zoeken in categorieën",
                                    size=(200, 50),
                                    name="zoekterm")
#buttons
        self.btn_instelling = buttonMaker("Instellingen",
                                          self.instellingenKnop)
        self.btn_beheren = buttonMaker("Beheren", self.beherenKnop)
#boxes
        box_titelZoeken = boxMaker([self.txt_titel, (0, 0), self.zoekBalk],
                                   [10, 50, 10], [wx.ALL, wx.ALL, wx.ALL])
        box_categories = boxMaker([self.txt_categorie], [10],
                                  [wx.ALIGN_CENTER])
        box_btnsVersie = boxMaker([self.btn_instelling, (0, 0),
                                   self.txt_versie,(0, 0), self.btn_beheren],
                                  [10, 20, 10, 20, 10],
                                  [wx.ALL, wx.ALL, wx.ALL, wx.ALL, wx.ALL])
        box_mainBox = boxMaker([box_titelZoeken, box_categories,
                                box_btnsVersie], [10, 80, 10],
                               [wx.ALL,wx.ALL,wx.ALL], wx.VERTICAL,
                               [10, 10, 10])
        
        pnl_mainPanel.SetSizer(box_mainBox)

    def instellingenKnop(self, event):
        #naar instellingen scherm
        self.btn_instelling.SetLabel("Clicked")

    def beherenKnop(self, event):
        #naar beheren scherm
        self.btn_beheren.SetLabel("Clicked")

if __name__ == '__main__':  
    app = wx.App()  
    frame = frm_notities()  
    frame.Show()  
    app.MainLoop()
