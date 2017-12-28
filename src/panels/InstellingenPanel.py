"""
Log
+--------------------------+------------+-----------------------------------+
| Who                      | When       | What                              |
+--------------------------+------------+-----------------------------------+
| Yorick Bruijne           | 28-12-2017 | making the file, panel and widgets|
+--------------------------+------------+-----------------------------------+
"""

import wx

class InstellingenPanel(wx.Panel):
    def __init__(self, parent, id):
        super().__init__(parent, id, size = (600, 400))
        self.IP_vbox = wx.BoxSizer(wx.VERTICAL)
        self.IP_vbox.Add(self.titel(id))
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.bestandsInstellingen(id))
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.bewerkInstellingen(id))
        self.IP_vbox.AddSpacer(10)
        self.IP_vbox.Add(self.bottomBox(id))
        self.IP_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.IP_hbox.AddSpacer(20)
        self.IP_hbox.Add(self.IP_vbox)
        self.IP_hbox.AddSpacer(20)
        self.SetSizer(self.IP_hbox)

    def bestandsInstellingen(self, id):
        bi_pad = "/home/dit/is/lang/geleden/notepad"
        bi_pad_txt = wx.StaticText(self, id, bi_pad)
        bi_hbox = self.preEnMap(id)
        bi_main_mbox_border = wx.StaticBox(self, id, "Bestandsinstellingen")
        bi_main_vbox = wx.StaticBoxSizer(bi_main_mbox_border, wx.VERTICAL)
        bi_main_vbox.Add(bi_hbox)
        bi_main_vbox.Add(bi_pad_txt)
        return bi_main_vbox

    def preEnMap(self, id):
        pem_prefix = "Prefix"
        pem_prefix_txt = wx.StaticText(self, id, pem_prefix)
        pem_prefix_textfield = wx.TextCtrl(self)
        pem_opslagmap = "Opslagmap"
        pem_opslagmap_txt = wx.StaticText(self, id, pem_opslagmap)
        pem_select_opslagmap = wx.Button(self, id, "Map selecteren")
        pem_vbox1 = wx.BoxSizer(wx.VERTICAL)
        pem_vbox1.AddSpacer(5)
        pem_vbox1.Add(pem_prefix_txt, wx.EXPAND, wx.ALIGN_CENTER_VERTICAL)
        pem_vbox1.AddSpacer(13)
        pem_vbox1.Add(pem_opslagmap_txt, wx.EXPAND, wx.ALIGN_CENTER_VERTICAL)
        pem_vbox2 = wx.BoxSizer(wx.VERTICAL)
        pem_vbox2.Add(pem_prefix_textfield, wx.EXPAND, wx.ALIGN_RIGHT)
        pem_vbox2.Add(pem_select_opslagmap, wx.EXPAND, wx.ALIGN_RIGHT)
        pem_hbox = wx.BoxSizer(wx.HORIZONTAL)
        pem_hbox.Add(pem_vbox1)
        pem_hbox.AddSpacer(20)
        pem_hbox.Add(pem_vbox2)
        return(pem_hbox)

    def bottomBox(self, id):
        bb_knop_anu = wx.Button(self, id, "Anuleren")
        bb_knop_ops = wx.Button(self, id, "Opslaan")
        bb_versie = "versie 2.1"
        bb_versie_txt = wx.StaticText(self, id, bb_versie, style=wx.ALIGN_CENTER)
        bb_hbox = wx.BoxSizer(wx.HORIZONTAL)
        bb_hbox.Add(bb_knop_anu, 1)
        bb_hbox.Add(bb_versie_txt, 3, wx.ALIGN_CENTER)
        bb_hbox.Add(bb_knop_ops, 1, wx.ALIGN_RIGHT)
        return bb_hbox

    def titel(self, id):
        t_titel = "Instellingen"
        t_fnt_titel = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD)
        t_titel_txt = wx.StaticText(self, id, t_titel)
        t_titel_txt.SetFont(t_fnt_titel)
        return t_titel_txt

    def bewerkInstellingen(self, id):
        bi_vbox1 = self.bewerkBoxLinks(id)
        bi_vbox2 = self.bewerkBoxRechts(id)
        bi_hbox_border = wx.StaticBox(self, id, "Bewerkingsinstellingen")
        bi_hbox = wx.StaticBoxSizer(bi_hbox_border, wx.HORIZONTAL)
        bi_hbox.Add(bi_vbox1)
        bi_hbox.Add(bi_vbox2)
        return(bi_hbox)

    def bewerkBoxRechts(self, id):
        bbr_letter_spinner = wx.SpinCtrl(self, min=5, max=25, initial=10)
        bbr_tab_spinner = wx.SpinCtrl(self, min=2, max=8, initial=4)
        bbr_vbox = wx.BoxSizer(wx.VERTICAL)
        bbr_vbox.Add(bbr_letter_spinner, wx.EXPAND, wx.ALIGN_CENTRE_VERTICAL)
        bbr_vbox.Add(bbr_tab_spinner, wx.EXPAND, wx.ALIGN_CENTRE_VERTICAL)
        bbr_cb = wx.CheckBox(self)
        bbr_vbox.Add(bbr_cb, wx.EXPAND, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
        return(bbr_vbox)

    def bewerkBoxLinks(self, id):
        bbl_tab = "Tab lengte"
        bbl_tab_txt = wx.StaticText(self, id, bbl_tab)
        bbl_opslaan = "Automatisch opslaan"
        bbl_opslaan_txt = wx.StaticText(self, id, bbl_opslaan)
        bbl_keuze = ["een", "twee", "Dit_is_een_lange_fam_naam"]
        bbl_combo = wx.ComboBox(self, choices = bbl_keuze)
        bbl_vbox = wx.BoxSizer(wx.VERTICAL)
        bbl_vbox.Add(bbl_combo, wx.EXPAND, wx.ALIGN_CENTRE_VERTICAL)
        bbl_vbox.Add(bbl_tab_txt, wx.EXPAND, wx.ALIGN_CENTRE_VERTICAL)
        bbl_vbox.Add(bbl_opslaan_txt, wx.EXPAND, wx.ALIGN_CENTRE_VERTICAL)
        return(bbl_vbox)


