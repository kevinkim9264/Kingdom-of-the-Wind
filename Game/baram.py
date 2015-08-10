import wx
from jobs import *
from battle import *
from baram_panels import *
from mobs import *

class MyFrame(wx.Frame):
  def __init__(self, parent, ID, title):
    wx.Frame.__init__(self, parent, ID, title, size=(800, 600))
    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.SetSizer(self.sizer)
    
   
    

    dlg = wx.TextEntryDialog(None, "Type your wished username", "User Name", "")
    if dlg.ShowModal() == wx.ID_OK:
      self.userName = dlg.GetValue()

    dlg = wx.SingleChoiceDialog(None, "Which job are ou going to play?", "job",
                                ["Rogue", "Warrior", "Magician", "Bowman"])
    if dlg.ShowModal() == wx.ID_OK:
      self.job = dlg.GetStringSelection()


    self.initGame()

  
  def initGame(self):
    self.character = self.createCharacter(self.userName, self.job)

    # Initialize all the necessary panels
    self.basicPanel = BasicPanel(self)
    self.sizer.Add(self.basicPanel, 1, wx.EXPAND)
    self.basicPanel.Hide()

    self.statusPanel = StatusPanel(self)
    self.sizer.Add(self.statusPanel, 1, wx.EXPAND)
    self.statusPanel.Hide()

    self.equipmentPanel = EquipmentPanel(self)
    self.sizer.Add(self.equipmentPanel, 1, wx.EXPAND)
    self.equipmentPanel.Hide()

    self.storePanel = StorePanel(self)
    self.sizer.Add(self.storePanel, 1, wx.EXPAND)
    self.storePanel.Hide()

    self.itemPanel = ItemPanel(self)
    self.sizer.Add(self.itemPanel, 1, wx.EXPAND)
    self.itemPanel.Hide()

    
    print self.character
    


    
    tutorial = wx.MessageDialog(None, "Do you need tutorial?", "tutorial", wx.YES_NO | wx.ICON_QUESTION)
    
    if tutorial.ShowModal() == wx.ID_YES:
      self.tutorial()
    else:
      self.startGame()
    
  def createCharacter(self, userName, job):
    if (job == "Rogue"):
      return Rogue(self.userName)
    elif (job == "Warrior"):
      return Warrior(self.userName)
    elif (job == "Bowman"):
      return Bowman(self.userName)
    elif (job == "Magician"):
      return Magician(self.userName)

  def tutorial(self):
    tutPanel = TutorialPanel(self)
    tutPanel.Show()
    

  def startGame(self):
    
    self.basicPanel.Show()
    self.Layout()

  def status(self):
    self.statusPanel.Update()
    self.statusPanel.Show()
    self.Layout()

  def equipment(self):
    self.equipmentPanel.Update()
    self.equipmentPanel.Show()
    self.Layout()

  def item(self):
    self.itemPanel.Update()
    self.itemPanel.Show()
    self.Layout()

  def battle(self, mob_level):
    mob = Mob.mob(mob_level) #mob_level = "10-20", etc
    
    battle = Battle(self, self.character, mob)
    battle.start()
    
  def healCharacter(self):
    self.character.hp = self.character.max_hp

if __name__ == '__main__':
  app = wx.App(False)
  frame = MyFrame(None, -1, "Baram")
  frame.Show(True)
  app.MainLoop()
