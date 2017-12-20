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

"""
import wx


class BasePanel(wx.Panel):

    def __init__(self, parent, id, title):
        super().__init__(parent, id)
        self.title = title
        self.version = "Versie 1.2"
        # fonts
        self.fnt_title = wx.Font(18, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.fnt_default = wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

    def textMaker(self, TM_textLabel, TM_font):
        txt_staticText = wx.StaticText(self, -1, TM_textLabel)
        txt_staticText.SetFont(TM_font)
        return txt_staticText

    def buttonMaker(self, BM_btnLabel, BM_evtNaam,
                        BM_lblFont):
        btn_button = wx.Button(self, -1, BM_btnLabel)
        self.Bind(wx.EVT_BUTTON, BM_evtNaam, btn_button)
        btn_button.SetFont(BM_lblFont)
        btn_button.SetDefault()
        return btn_button

    def getTitle(self):
        return self.title


