"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 29-12-2017 | Implement skeleton of this file  |
|                          |            | and launch the frame when ran    |
|                          |            | from the command line. Also added|
|                          |            | a global version string.         |
+--------------------------+------------+----------------------------------+

"""
import wx


VERSION = "1.0"
VERSION_STRING = "Versie " + VERSION


class MainFrame(wx.Frame):

    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(800, 800))
        self.container_box = wx.BoxSizer(wx.VERTICAL)
        self.panel_stack = []
        self.SetSizer(self.container_box)

    def showPanel(self, panel):
        if len(self.panel_stack):
            last_panel = self.panel_stack[-1]
            last_panel.Hide()
        self.panel_stack.append(panel)
        self.container_box.Add(panel, 1, wx.EXPAND)
        self.updateLayout(panel.getFrameTitle())

    def goBack(self):
        if len(self.panel_stack) > 1:
            self.container_box.Remove(len(self.panel_stack) - 1)
            self.panel_stack.pop().Hide()
            last_panel = self.panel_stack[-1]
            last_panel.Show()
            self.updateLayout(last_panel.getFrameTitle())

    def updateLayout(self, title=None):
        if title is not None:
            self.SetTitle(title)
        self.container_box.Layout()
        self.Layout()


if __name__ == "__main__":
    from panels import CategoryOverviewPanel

    app = wx.App()
    frame = MainFrame(None, wx.ID_ANY, "")
    frame.showPanel(CategoryOverviewPanel(frame, wx.ID_ANY))
    frame.Show(True)
    app.MainLoop()
