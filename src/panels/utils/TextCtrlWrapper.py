"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 12-01-2018 | Create this file, implement key  |
|                          |            | handling for TextCtrls           |
+--------------------------+------------+----------------------------------+
"""
import wx


class TextCtrlWrapper(object):

    def __init__(self, text_ctrl, tab_length=4):
        self.ctrl = text_ctrl
        self.tab = ' ' * tab_length
        self.key_code = None
        self.current_position = None
        self.last_position = None
        self.current_position_xy = None
        self.last_position_xy = None
        self.ctrl.Bind(wx.EVT_CHAR, self.handleCharacter)

    def getStyleAtPosition(self, pos):
        text_style = wx.TextAttr()
        self.ctrl.GetStyle(pos, text_style)
        is_italic = text_style.GetFontStyle() == wx.FONTSTYLE_ITALIC
        is_bold = text_style.GetFontWeight() == wx.FONTWEIGHT_BOLD
        return is_italic, is_bold

    def writeByteFlag(self, out, on_tag, off_tag, previous, now):
        if now and not previous:
            print("1")
            out.write(on_tag)
        elif not now and previous:
            print("2")
            out.write(off_tag)

    def saveToFile(self, file_path):
        with open(file_path, 'w') as out:
            self.last_position = self.ctrl.GetLastPosition()
            was_bold = False
            was_italic = False
            for i in range(self.last_position):
                is_italic, is_bold = self.getStyleAtPosition(i)
                self.writeByteFlag(out, '\x05', '\x06', was_italic, is_italic)
                self.writeByteFlag(out, '\x07', '\x08', was_bold, is_bold)
                was_italic, was_bold = is_italic, is_bold
                char = self.ctrl.GetRange(i, i + 1)
                out.write(char)

    def handleCharacter(self, evt):
        evt.Skip(False)
        self.key_code = evt.GetKeyCode()
        self.current_position = self.ctrl.GetInsertionPoint()
        self.last_position = self.ctrl.GetLastPosition()
        self.handleAsciiCharacters()
        self.handleDeleteCharacters()
        self.handleArrowCharacters()
        self.handleWhiteSpaceCharacters()
        self.handlePasting()

    def getXYPosition(self):
        _, x, y = self.ctrl.PositionToXY(self.current_position)
        self.current_position_xy = (x, y)
        _, x, y = self.ctrl.PositionToXY(self.last_position)
        self.last_position_xy = (x, y)

    def handleAsciiCharacters(self):
        if 32 <= self.key_code <= 126:
            self.ctrl.WriteText(chr(self.key_code))

    def handleDeleteCharacters(self):
        if self.key_code == wx.WXK_BACK:
            self.ctrl.Remove(self.current_position - 1, self.current_position)
        elif ((self.key_code == wx.WXK_DELETE
               or self.key_code == wx.WXK_NUMPAD_DELETE)
              and self.current_position != self.last_position):
            self.ctrl.Remove(self.current_position, self.current_position + 1)

    def handleArrowCharacters(self):
        self.getXYPosition()
        if self.key_code == wx.WXK_LEFT or self.key_code == wx.WXK_RIGHT:
            offset = (-1 if self.key_code == wx.WXK_LEFT else 1)
            offset_position = self.current_position + offset
            if 0 <= offset_position <= self.last_position:
                self.ctrl.SetInsertionPoint(offset_position)
        elif self.key_code == wx.WXK_UP or self.key_code == wx.WXK_DOWN:
            offset = -1 if self.key_code == wx.WXK_UP else 1
            offsetY = self.current_position_xy[1] + offset
            if 0 <= offsetY <= self.last_position_xy[1]:
                pos = self.ctrl.XYToPosition(
                    self.current_position_xy[0], offsetY)
                if pos == -1:
                    x = self.ctrl.GetLineLength(offsetY)
                    pos = self.ctrl.XYToPosition(x, offsetY)
                self.ctrl.SetInsertionPoint(pos)

    def handleWhiteSpaceCharacters(self):
        if (self.key_code == wx.WXK_NUMPAD_ENTER
                or self.key_code == wx.WXK_CONTROL_M):
            self.ctrl.WriteText(chr(self.key_code))
        elif self.key_code == wx.WXK_TAB or self.key_code == wx.WXK_NUMPAD_TAB:
            self.ctrl.WriteText(self.tab)
        elif (self.key_code == wx.WXK_HOME
              or self.key_code == wx.WXK_NUMPAD_HOME):
            self.getXYPosition()
            pos = self.ctrl.XYToPosition(0, self.current_position_xy[1])
            self.ctrl.SetInsertionPoint(pos)
        elif (self.key_code == wx.WXK_END
              or self.key_code == wx.WXK_NUMPAD_END):
            self.getXYPosition()
            max_len = self.ctrl.GetLineLength(self.current_position_xy[1])
            pos = self.ctrl.XYToPosition(max_len, self.current_position_xy[1])
            self.ctrl.SetInsertionPoint(pos)

    def handlePasting(self):
        if self.key_code == wx.WXK_CONTROL_V:
            text_data = wx.TextDataObject()
            got_text = False
            if wx.TheClipboard.Open():
                got_text = wx.TheClipboard.GetData(text_data)
                wx.TheClipboard.Close()
            if got_text:
                self.ctrl.WriteText(text_data.GetText())
        elif (self.key_code == wx.WXK_CONTROL_C
              or self.key_code == wx.WXK_CONTROL_X):
            selection = self.ctrl.GetSelection()
            if selection[0] != selection[1]:
                text = self.ctrl.GetRange(*selection)
                if wx.TheClipboard.Open():
                    wx.TheClipboard.SetData(wx.TextDataObject(text))
                    wx.TheClipboard.Close()
                if self.key_code == wx.WXK_CONTROL_X:
                    self.ctrl.Remove(*selection)
