import wx

class MyFrame(wx.Frame):
  def __init__(self, parent):
    wx.Frame.__init__(self, parent)

    master_sizer = wx.BoxSizer(wx.VERTICAL)

    sizer1 = wx.BoxSizer(wx.HORIZONTAL)

    self.panel = wx.Panel(self)
    

    button = wx.Button(self.panel, label="Blue")
    self.Bind(wx.EVT_BUTTON, self.OnButton, button)

    sizer1.Add(self.panel, 1, wx.EXPAND)

    master_sizer.Add(sizer1, 1, wx.EXPAND)

    self.SetSizer(master_sizer)

    self.panel.SetBackgroundColour("Red")

  def OnButton(self, evt):
    self.panel.SetBackgroundColour("Blue")
    self.Refresh()

if __name__ == "__main__":
  app = wx.App(False)
  frame = MyFrame(None)
  frame.Show()
  app.MainLoop()
