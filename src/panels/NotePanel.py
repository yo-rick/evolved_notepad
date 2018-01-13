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
| Joey Nap                 | 12-01-2018 | Changes to bold/italic functions |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 12-01-2018 | Clean-up file and implement bold |
|                          |            | and italic realtime typing and   |
|                          |            | saving it to a file              |
+--------------------------+------------+----------------------------------+
| Joey Nap                 | 13-01-2018 | Loading files and applying the   |
|                          |            | correct styles.                  |
+--------------------------+------------+----------------------------------+
"""
import os

import wx

import MainFrame
from panels.utils import TextCtrlWrapper
from settings import Settings
from .BasePanel import BasePanel


class NotePanel(BasePanel):

    def __init__(self, parent, id, note_name, note_path):
        super().__init__(parent, id, 'Notitie scherm', note_name)
        self.note_path = note_path
        self.settings = self.getSettings()
        self.fonts = self.createFonts(self.settings)
        self.note_field = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE)
        self.note_field.SetFont(self.fonts['normal'])
        self.note_field_wrapper = TextCtrlWrapper(
            self.note_field, self.settings['tab_length'])
        if not os.path.exists(note_path):
            os.mknod(note_path)
        self.loadFile()
        box_title_row = self.createTitleRow()
        box_note_field = self.boxMaker(
            [self.note_field], [10], [wx.ALL | wx.EXPAND])
        box_bottom_row = self.createBottomRow()
        box_main = self.boxMaker(
            [box_title_row, box_note_field, box_bottom_row], [10, 80, 10],
            [wx.ALL | wx.EXPAND, wx.ALL | wx.EXPAND,
             wx.ALIGN_CENTER_HORIZONTAL], wx.VERTICAL, [10, 10, 10])
        self.SetSizer(box_main)

    def getSettings(self):
        settings = Settings.getInstance()
        settings_font_family = settings.getSetting('font-family').upper()
        font_family = getattr(wx, 'FONTFAMILY_' + settings_font_family,
                              wx.FONTFAMILY_DEFAULT)
        font_size = settings.getSetting('font-size')
        tab_length = settings.getSetting('tab-length')
        automatic_save = settings.getSetting('automatic-save')
        return dict(font_family=font_family, font_size=font_size,
                    tab_length=tab_length, automatic_save=automatic_save)

    def createFonts(self, settings):
        base_font = self.fontMaker(
            FM_size=settings['font_size'], FM_family=settings['font_family'])
        bold_font = base_font.Bold()
        italic_font = base_font.Italic()
        bold_italic_font = bold_font.Italic()
        return dict(normal=base_font, bold=bold_font, italic=italic_font,
                    bold_italic=bold_italic_font)

    def loadStyles(self, italic, start, stop):
        selected_text_style = wx.TextAttr()
        self.note_field.GetStyle(start, selected_text_style)
        is_italic = selected_text_style.GetFontStyle() == wx.FONTSTYLE_ITALIC
        is_bold = selected_text_style.GetFontWeight() == wx.FONTWEIGHT_BOLD
        new_text_style = wx.TextAttr(wx.NullColour)
        self.setFontStyle(
            italic, new_text_style, is_italic, is_bold)
        self.note_field.SetStyle(start, stop, new_text_style)

    def loadFile(self):
        noteFile = open(self.note_path, 'r')
        noteText = noteFile.readlines()
        noteFile.close()
        pos = 0
        for line in noteText:
            for char in line:
                print("pos:", char)
                if char == "\x05":
                    italStart = pos
                elif char == "\x06":
                    self.loadStyles(True, italStart, pos)
                elif char == "\x07":
                    boldStart = pos
                elif char == "\x08":
                    self.loadStyles(False, boldStart, pos)
                else:
                    self.note_field.WriteText(char)
                    pos += 1

    def setFontStyle(self, italic, font_style, is_italic, is_bold):
        if italic:
            if is_italic and is_bold:
                font_style.SetFont(self.fonts['bold'])
            elif is_bold:
                font_style.SetFont(self.fonts['bold_italic'])
            elif is_italic:
                font_style.SetFont(self.fonts['normal'])
            else:
                font_style.SetFont(self.fonts['italic'])
        else:
            if is_italic and is_bold:
                font_style.SetFont(self.fonts['italic'])
            elif is_bold:
                font_style.SetFont(self.fonts['normal'])
            elif is_italic:
                font_style.SetFont(self.fonts['bold_italic'])
            else:
                font_style.SetFont(self.fonts['bold'])

    def italicBoldButton(self, event):
        pressed_italic = event.GetEventObject().GetLabel().lower() == 'italic'
        lst_selection = list(self.note_field.GetSelection())
        if lst_selection[0] == lst_selection[1]:
            font_style = self.note_field.GetDefaultStyle()
            is_italic = font_style.GetFontStyle() == wx.FONTSTYLE_ITALIC
            is_bold = font_style.GetFontWeight() == wx.FONTWEIGHT_BOLD
            self.setFontStyle(pressed_italic, font_style, is_italic, is_bold)
            self.note_field.SetDefaultStyle(font_style)
            self.note_field.SetFocus()
            return
        selected_text_style = wx.TextAttr()
        self.note_field.GetStyle(lst_selection[0], selected_text_style)
        is_italic = selected_text_style.GetFontStyle() == wx.FONTSTYLE_ITALIC
        is_bold = selected_text_style.GetFontWeight() == wx.FONTWEIGHT_BOLD
        new_text_style = wx.TextAttr(wx.NullColour)
        self.setFontStyle(
            pressed_italic, new_text_style, is_italic, is_bold)
        lst_selection.append(new_text_style)
        self.note_field.SetStyle(*lst_selection)

    def backButton(self, event):
        self.GetParent().goBack()

    def saveButton(self, event):
        self.note_field_wrapper.saveToFile(self.note_path)

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

    def createTitleRow(self):
        btn_bold = self.buttonMaker("Bold", self.italicBoldButton,
                                    self.fnt_title.Bold())
        btn_italic = self.buttonMaker("Italic", self.italicBoldButton,
                                      self.fnt_title.Italic())
        txt_title = self.textMaker(self.getPanelTitle(), self.fnt_title)
        return self.boxMaker(
            [txt_title, (0, 0), btn_italic, btn_bold], [20, 40, 10, 10],
            [wx.ALL] * 4)

    def createBottomRow(self):
        btn_back = self.buttonMaker("Terug", self.backButton)
        btn_save = self.buttonMaker("Opslaan", self.saveButton)
        txt_version = self.textMaker(MainFrame.VERSION_STRING)
        return self.boxMaker(
            [btn_back, (0, 0), txt_version, (0, 0), btn_save],
            [10, 20, 10, 20, 10], [wx.ALL] * 5)
