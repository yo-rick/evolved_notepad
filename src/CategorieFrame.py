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
        #texts
        ##scherm titel
        self.txt_titel = wx.StaticText(pnl_mainPanel, -1, "Categorieën")
        fnt_titel = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL
                            , wx.FONTWEIGHT_BOLD)
        self.txt_titel.SetFont(fnt_titel)
        ##versienummer
        self.txt_versie = wx.StaticText(pnl_mainPanel, -1, "versie 0.0.1")
        ##tijdelijk categorielijst
        self.txt_categorie = wx.StaticText(pnl_mainPanel, -1,
                                           "Hier komen categorieën")
        #invoer
        ##zoekbalk
        self.zoekBalk = wx.TextCtrl(pnl_mainPanel, -1,
                                    value="Zoeken in categorieën",
                                    size=(200, 50),
                                    name="zoekterm")
        #buttons
        ##instellingen
        self.btn_instelling = wx.Button(pnl_mainPanel, -1, "Instellingen")  
        self.Bind(wx.EVT_BUTTON, self.instellingenKnop, self.btn_instelling)  
        self.btn_instelling.SetDefault()
        ##beheren
        self.btn_beheren = wx.Button(pnl_mainPanel, -1, "Beheren")
        self.Bind(wx.EVT_BUTTON, self.beherenKnop, self.btn_beheren)  
        self.btn_beheren.SetDefault()
        #boxes
        ##titel en zoekbalk
        box_titelZoeken = wx.BoxSizer(wx.HORIZONTAL)
        box_titelZoeken.Add(self.txt_titel, 10, flag=wx.ALL)
        box_titelZoeken.Add((0, 0), 50, flag=wx.ALL)
        box_titelZoeken.Add(self.zoekBalk, 10, flag=wx.ALL)
        ##categorie lijst
        box_categories = wx.BoxSizer(wx.HORIZONTAL)
        box_categories.Add(self.txt_categorie, flag=wx.ALIGN_CENTER)
        ##knoppen en versienummer
        box_btnsVersie = wx.BoxSizer(wx.HORIZONTAL)
        box_btnsVersie.Add(self.btn_instelling, 10, flag=wx.ALL)
        box_btnsVersie.Add((0, 0), 20, flag=wx.ALL)
        box_btnsVersie.Add(self.txt_versie, 10, flag=wx.ALL)
        box_btnsVersie.Add((0, 0), 20, flag=wx.ALL)
        box_btnsVersie.Add(self.btn_beheren, 10, flag=wx.ALL)
        ##alle boxes samen
        box_mainBox = wx.BoxSizer(wx.VERTICAL)
        box_mainBox.Add(box_titelZoeken, 10, flag=wx.ALL, border=10)
        box_mainBox.Add(box_categories, 80, flag=wx.ALL, border=10)
        box_mainBox.Add(box_btnsVersie, 10, flag=wx.ALL, border=10)
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
