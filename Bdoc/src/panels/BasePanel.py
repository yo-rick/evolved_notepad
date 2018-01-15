"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Tjardo Maarseveen        | 20-12-2017 | Adding the textMaker and         |
|                          |            | buttonMaker methods to the       |
|                          |            | Basepanel                        |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 03-01-2018 | Replaced -1 with proper ID's,    |
|                          |            | added default fonts              |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 10-01-2018 | Added fontMaker method.          |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 14-01-2018 | Add parent parameter in textmaker|
+--------------------------+------------+----------------------------------+

"""
import wx


class BasePanel(wx.Panel):

    def __init__(self, parent, id, frame_title, panel_title):
        super().__init__(parent=parent, id=id)
        self.frame_title = frame_title
        self.panel_title = panel_title
        self.fnt_title = self.fontMaker(18, FM_weight=wx.FONTWEIGHT_BOLD)
        self.fnt_default = self.fontMaker()

    def textMaker(self, TM_textLabel, TM_font=None, style=0, parent=None):
        if TM_font is None:
            TM_font = self.fnt_default
        if parent is None:
            parent = self
        txt_staticText = wx.StaticText(
            parent, wx.ID_ANY, TM_textLabel, style=style)
        txt_staticText.SetFont(TM_font)
        return txt_staticText

    def buttonMaker(self, BM_btnLabel, BM_evtNaam, BM_lblFont=None):
        if BM_lblFont is None:
            BM_lblFont = self.fnt_default
        btn_button = wx.Button(self, wx.ID_ANY, BM_btnLabel)
        self.Bind(wx.EVT_BUTTON, BM_evtNaam, btn_button)
        btn_button.SetFont(BM_lblFont)
        btn_button.SetDefault()
        return btn_button

    def fontMaker(self, FM_size=10, FM_family=wx.FONTFAMILY_DEFAULT,
                  FM_style=wx.FONTSTYLE_NORMAL,
                  FM_weight=wx.FONTWEIGHT_NORMAL):
        return wx.Font(FM_size, FM_family, FM_style, FM_weight)

    def getFrameTitle(self):
        return self.frame_title

    def getPanelTitle(self):
        return self.panel_title


