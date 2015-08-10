import wx
from battle import *

class TutorialPanel(wx.Panel):
  def __init__(self, parent):
    super(TutorialPanel, self).__init__(parent)
    #wx.Panel.__init__(self, parent)
    self.parent = parent
    self.SetBackgroundColour("White")

    self.label_1 = wx.StaticText(self, -1, "Tutorial \n blaghblagh", style=wx.ALIGN_CENTRE)
    self.button_1 = wx.Button(self, label="Next", size=(50,50))
    self.Bind(wx.EVT_BUTTON, self.OnStartGame, self.button_1)

    sizer_0 = wx.BoxSizer(wx.VERTICAL)

    sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

    sizer_1.Add(self.label_1, 1, wx.EXPAND)
    sizer_2.Add(self.button_1, 2, wx.EXPAND)

    
    sizer_0.Add(sizer_1, 3, wx.EXPAND)
    sizer_0.Add(sizer_2, 1, wx.EXPAND)  
    


    self.SetSizer(sizer_0)

    parent.sizer.Add(self, 1, wx.EXPAND)


  def OnStartGame(self, evt):
    self.Hide()
    self.parent.startGame()
    
    

class BasicPanel(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)

    border_width = 10

    self.parent = parent
    self.SetBackgroundColour("White")

    button_10_20 = wx.Button(self, label="Battle 10 - 20")
    button_20_30 = wx.Button(self, label="Battle 20 - 30")
    button_30_40 = wx.Button(self, label="Battle 30 - 40")
    button_40_50 = wx.Button(self, label="Battle 40 - 50")

    button_store = wx.Button(self, label="Store", size=(60, 60))
    button_equip = wx.Button(self, label="Equip", size=(60, 60))
    button_item = wx.Button(self, label="Item", size=(60, 60))
    button_status = wx.Button(self, label="Status", size=(60, 60))
    button_upgrade = wx.Button(self, label="Upgrade", size=(60, 60))
    

    self.Bind(wx.EVT_BUTTON, self.OnBattle_10_20, button_10_20)

    self.Bind(wx.EVT_BUTTON, self.OnStore, button_store)
    self.Bind(wx.EVT_BUTTON, self.OnStatus, button_status)
    self.Bind(wx.EVT_BUTTON, self.OnEquip, button_equip)
    self.Bind(wx.EVT_BUTTON, self.OnItem, button_item)
    
    sizer_0 = wx.BoxSizer(wx.VERTICAL)

    battle_sizer = wx.BoxSizer(wx.VERTICAL)
    button_sizer = wx.BoxSizer(wx.HORIZONTAL)


    battle_sizer.Add(button_10_20, 1, wx.EXPAND)
    battle_sizer.Add(button_20_30, 1, wx.EXPAND)
    battle_sizer.Add(button_30_40, 1, wx.EXPAND)
    battle_sizer.Add(button_40_50, 1, wx.EXPAND)
    
    button_sizer.Add(button_store, 1)
    button_sizer.Add(button_equip, 1)
    button_sizer.Add(button_status, 1)
    button_sizer.Add(button_upgrade, 1)
    button_sizer.Add(button_item, 1)

    

    sizer_0.Add(battle_sizer, 3, wx.EXPAND)
    sizer_0.Add(button_sizer, 1, wx.EXPAND)
    
    self.SetSizer(sizer_0)

    #parent.sizer.Add(self, 1, wx.EXPAND)

   
  def OnStore(self, evt):
    self.Hide()
    self.parent.startGame()

  def OnStatus(self, evt):
    self.Hide()
    self.parent.status()

  def OnEquip(self, evt):
    self.Hide()
    self.parent.equipment()

  def OnItem(self, evt):
    self.Hide()
    self.parent.item()

  def OnBattle_10_20(self, evt):
    self.Hide()
    self.parent.battle("10-20")





    

class StatusPanel(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)
    self.SetBackgroundColour("White")
    self.parent = parent
    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.SetSizer(self.sizer)
    #self.parent.sizer.Add(self, 1, wx.EXPAND)
    
    
  def OnBack(self, evt):
    self.Hide()
    self.parent.startGame()

  def Update(self):
    sizer = self.sizer
    
    sizer.DeleteWindows()
    
    stats = wx.BoxSizer(wx.VERTICAL)
    button_sizer = wx.BoxSizer(wx.HORIZONTAL)
    
    name_label = wx.StaticText(self, -1, "Name: %s" % self.parent.character.userName, style=wx.ALIGN_CENTRE)
    job_label = wx.StaticText(self, -1, "Job: %s" % self.parent.character.job, style=wx.ALIGN_CENTRE)
    hp_label = wx.StaticText(self, -1, "HP: %d" % self.parent.character.hp, style=wx.ALIGN_CENTRE)
    mp_label = wx.StaticText(self, -1, "MP: %d" % self.parent.character.mp, style=wx.ALIGN_CENTRE)
    level_label = wx.StaticText(self, -1, "Lvl: %d" % self.parent.character.level, style=wx.ALIGN_CENTRE)
    money_label = wx.StaticText(self, -1, "Money: %d" % self.parent.character.money, style=wx.ALIGN_CENTRE)
    experience_label = wx.StaticText(self, -1, "Exp: {0}  ({1}exp for next level)".format(self.parent.character.experience,self.parent.character.required_experience), style=wx.ALIGN_CENTRE)
    
    button = wx.Button(self, label="Back", size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.OnBack, button)
    button_sizer.Add(button, 1, wx.EXPAND)


    stats.Add(name_label, 1)
    stats.Add(job_label, 1)
    stats.Add(hp_label, 1)
    stats.Add(mp_label, 1)
    stats.Add(level_label, 1)
    stats.Add(experience_label, 1)
    stats.Add(money_label, 1)

    sizer.Add(stats, 4)
    sizer.Add(button_sizer, 1, wx.EXPAND)

    self.parent.Layout()


class EquipmentPanel(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)
    self.SetBackgroundColour("White")
    self.parent = parent
    
    
    self.master_sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.SetSizer(self.master_sizer)
    #self.parent.sizer

  def Update(self):
    equipments = self.parent.character.equipments
    weapon = equipments['weapon']
    helmet = equipments['helmet']
    cloth = equipments['cloth']
    glove = equipments['glove']
    VERTICAL = wx.VERTICAL
    HORIZONTAL = wx.HORIZONTAL
    
    # Zero tier (top level)
    self.master_sizer.DeleteWindows()

    # second level
    equips_sizer = wx.BoxSizer(VERTICAL)
    self.info_sizer = wx.BoxSizer(VERTICAL)
    info_sizer = self.info_sizer
    # third level
    helmet_sizer = wx.BoxSizer(HORIZONTAL)
    cloth_sizer = wx.BoxSizer(HORIZONTAL)
    weapon_sizer = wx.BoxSizer(HORIZONTAL)
    glove_sizer = wx.BoxSizer(HORIZONTAL)

    self.helmet_info_sizer = wx.BoxSizer(VERTICAL)
    self.cloth_info_sizer = wx.BoxSizer(VERTICAL)
    self.weapon_info_sizer = wx.BoxSizer(VERTICAL)
    self.glove_info_sizer = wx.BoxSizer(VERTICAL)

    # fourth level (actual widgets)
    helmet_label = wx.StaticText(self, -1, "Helmet: %s" % helmet.name, style=wx.ALIGN_CENTRE)
    helmet_info_button = wx.Button(self, label="info", size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.OnHelmetInfo, helmet_info_button)

    cloth_label = wx.StaticText(self, -1, "Cloth: %s" % cloth.name, style=wx.ALIGN_CENTRE)
    cloth_info_button = wx.Button(self, label="info", size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.OnClothInfo, cloth_info_button)

    weapon_label = wx.StaticText(self, -1, "Weapon: %s" % weapon.name, style=wx.ALIGN_CENTRE)
    weapon_info_button = wx.Button(self, label="info", size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.OnWeaponInfo, weapon_info_button)

    glove_label = wx.StaticText(self, -1, "Glove: %s" % glove.name, style=wx.ALIGN_CENTRE)
    glove_info_button = wx.Button(self, label="info", size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.OnGloveInfo, glove_info_button)
    
    helmet_sizer.Add(helmet_label, 3, wx.EXPAND)
    helmet_sizer.Add(helmet_info_button, 1, wx.EXPAND)
    cloth_sizer.Add(cloth_label, 3, wx.EXPAND)
    cloth_sizer.Add(cloth_info_button, 1, wx.EXPAND)
    weapon_sizer.Add(weapon_label, 3, wx.EXPAND)
    weapon_sizer.Add(weapon_info_button, 1, wx.EXPAND)
    glove_sizer.Add(glove_label, 3, wx.EXPAND)
    glove_sizer.Add(glove_info_button, 1, wx.EXPAND)


    back_to_normal_button = wx.Button(self, label="Back")
    self.Bind(wx.EVT_BUTTON, self.OnBackToNormal, back_to_normal_button)
    equips_sizer.AddMany([
      (helmet_sizer, 2, wx.EXPAND),
      (cloth_sizer, 2, wx.EXPAND),
      (weapon_sizer, 2, wx.EXPAND),
      (glove_sizer, 2, wx.EXPAND),
      (back_to_normal_button, 1, wx.EXPAND)
      ])

    # fourth level for helmet,cloth,weapon,glove_info sizers
    helmet_name_label = wx.StaticText(self, -1, helmet.name, style=wx.ALIGN_CENTRE)
    helmet_defense_label = wx.StaticText(self, -1, "Defense: %s" % str(helmet.defense), style=wx.ALIGN_CENTRE)
    helmet_damage_label = wx.StaticText(self, -1, "Damage: %s" % str(helmet.damage), style=wx.ALIGN_CENTRE)
    helmet_back_button = wx.Button(self, label="Back")
    self.Bind(wx.EVT_BUTTON, self.OnHelmetBack, helmet_back_button)

    
    cloth_name_label = wx.StaticText(self, -1, cloth.name, style=wx.ALIGN_CENTRE)
    cloth_defense_label = wx.StaticText(self, -1, "Defense: %s" % str(cloth.defense), style=wx.ALIGN_CENTRE)
    cloth_damage_label = wx.StaticText(self, -1, "Damage: %s" % str(cloth.damage), style=wx.ALIGN_CENTRE)
    cloth_back_button = wx.Button(self, label="Back")
    self.Bind(wx.EVT_BUTTON, self.OnClothBack, cloth_back_button)

    weapon_name_label = wx.StaticText(self, -1, weapon.name, style=wx.ALIGN_CENTRE)
    weapon_defense_label = wx.StaticText(self, -1, "Defense: %s" % str(weapon.defense), style=wx.ALIGN_CENTRE)
    weapon_damage_label = wx.StaticText(self, -1, "Damage: %s" % str(weapon.damage), style=wx.ALIGN_CENTRE)
    weapon_back_button = wx.Button(self, label="Back")
    self.Bind(wx.EVT_BUTTON, self.OnWeaponBack, weapon_back_button)

    glove_name_label = wx.StaticText(self, -1, glove.name, style=wx.ALIGN_CENTRE)
    glove_defense_label = wx.StaticText(self, -1, "Defense: %s" % str(glove.defense), style=wx.ALIGN_CENTRE)
    glove_damage_label = wx.StaticText(self, -1, "Damage: %s" % str(glove.damage), style=wx.ALIGN_CENTRE)
    glove_back_button = wx.Button(self, label="Back")
    self.Bind(wx.EVT_BUTTON, self.OnGloveBack, glove_back_button)
    
    self.helmet_info_sizer.AddMany([
      (helmet_name_label, 1, wx.EXPAND),
      (helmet_defense_label, 1, wx.EXPAND),
      (helmet_damage_label, 1, wx.EXPAND),
      (helmet_back_button, 1, wx.EXPAND)
      ])
    
    
    self.cloth_info_sizer.AddMany([
      (cloth_name_label, 1, wx.EXPAND),
      (cloth_defense_label, 1, wx.EXPAND),
      (cloth_damage_label, 1, wx.EXPAND),
      (cloth_back_button, 1, wx.EXPAND)
      ])

    self.weapon_info_sizer.AddMany([
      (weapon_name_label, 1, wx.EXPAND),
      (weapon_defense_label, 1, wx.EXPAND),
      (weapon_damage_label, 1, wx.EXPAND),
      (weapon_back_button, 1, wx.EXPAND)
      ])

    self.glove_info_sizer.AddMany([
      (glove_name_label, 1, wx.EXPAND),
      (glove_defense_label, 1, wx.EXPAND),
      (glove_damage_label, 1, wx.EXPAND),
      (glove_back_button, 1, wx.EXPAND)
      ])

    info_sizer.AddMany([
      (self.helmet_info_sizer, 1, wx.EXPAND),
      (self.cloth_info_sizer, 1, wx.EXPAND),
      (self.weapon_info_sizer, 1, wx.EXPAND),
      (self.glove_info_sizer, 1, wx.EXPAND)
      ])


    self.master_sizer.Add(equips_sizer, 1, wx.EXPAND)
    self.master_sizer.Add(info_sizer, 1, wx.EXPAND)
    self.master_sizer.Hide(info_sizer)

    self.parent.Layout()


  def OnHelmetBack(self, evt):
    self.info_sizer.Hide(self.helmet_info_sizer)
    self.parent.Layout()
    

  def OnHelmetInfo(self, evt):
    self.info_sizer.Show(self.helmet_info_sizer)
    self.parent.Layout()

  def OnClothBack(self, evt):
    self.info_sizer.Hide(self.cloth_info_sizer)
    self.parent.Layout()

  def OnClothInfo(self, evt):
    self.info_sizer.Show(self.cloth_info_sizer)
    self.parent.Layout()

  def OnWeaponBack(self, evt):
    self.info_sizer.Hide(self.weapon_info_sizer)
    self.parent.Layout()

  def OnWeaponInfo(self, evt):
    self.info_sizer.Show(self.weapon_info_sizer)
    self.parent.Layout()

  def OnGloveBack(self, evt):
    self.info_sizer.Hide(self.glove_info_sizer)
    self.parent.Layout()
  
  def OnGloveInfo(self, evt):
    self.info_sizer.Show(self.glove_info_sizer)
    self.parent.Layout()

  def OnBackToNormal(self, evt):
    self.Hide()
    self.parent.startGame()
    

class BattlePanel(wx.Panel):
  def __init__(self, parent, battle):
    wx.Panel.__init__(self, parent)
    self.SetBackgroundColour("White")
    self.parent = parent
    self.battle = battle
    self.character = battle.character
    self.mob = battle.mob

    self.master_sizer = wx.BoxSizer(wx.VERTICAL)
    self.infos_sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

    self.master_sizer.Add(self.infos_sizer, 4, wx.EXPAND)
    self.master_sizer.Add(self.buttons_sizer, 1, wx.EXPAND)
    self.SetSizer(self.master_sizer)
    self.parent.sizer.Add(self, 1, wx.EXPAND)

    

  def draw(self):     
    self.drawStats()
    self.drawButtons()
 
    self.parent.Layout() 

  def drawStats(self):
    
    
    self.infos_sizer.DeleteWindows()
    user_sizer = wx.BoxSizer(wx.VERTICAL)
    mob_sizer = wx.BoxSizer(wx.VERTICAL)
    
    name_label = wx.StaticText(self, -1, "Name: %s" % self.character.userName, style=wx.ALIGN_CENTRE)
    job_label = wx.StaticText(self, -1, "Job: %s" % self.character.job, style=wx.ALIGN_CENTRE)
    hp_label = wx.StaticText(self, -1, "HP: %d" % self.character.hp, style=wx.ALIGN_CENTRE)
    mp_label = wx.StaticText(self, -1, "MP: %d" % self.character.mp, style=wx.ALIGN_CENTRE)
    level_label = wx.StaticText(self, -1, "Lvl: %d" % self.character.level, style=wx.ALIGN_CENTRE)

    mob_name_label = wx.StaticText(self, -1, "Name: %s" % self.mob.name, style=wx.ALIGN_CENTRE)
    mob_hp_label = wx.StaticText(self, -1, "HP: %d" % self.mob.hp, style=wx.ALIGN_CENTRE)
    mob_mp_label = wx.StaticText(self, -1, "MP: %d" % self.mob.mp, style=wx.ALIGN_CENTRE)
      
    user_sizer.Add(hp_label, 1)
    user_sizer.Add(mp_label, 1)
    user_sizer.Add(job_label, 1)
    user_sizer.Add(name_label, 1)
    user_sizer.Add(level_label, 1)

    mob_sizer.Add(mob_name_label, 1)
    mob_sizer.Add(mob_hp_label, 1)
    mob_sizer.Add(mob_mp_label, 1)

    self.infos_sizer.Add(user_sizer, 1, wx.EXPAND)
    self.infos_sizer.Add(mob_sizer, 1, wx.EXPAND)

  def drawButtons(self):
    self.buttons_sizer.DeleteWindows()
    self.skill_buttons = []
    for i in self.character.moves:
      self.skill_buttons.append(self.createButton(i))

    
    
    button_escape = wx.Button(self, label="Escape", size=(60, 60))

    
    self.Bind(wx.EVT_BUTTON, self.OnEscapeButton, button_escape)

    
    for i in self.skill_buttons:
      self.buttons_sizer.Add(i, 1, wx.EXPAND)
    self.buttons_sizer.Add(button_escape, 1)


  def createButton(self, move):
    button = wx.Button(self, label=move.name)
    self.Bind(wx.EVT_BUTTON, self.OnMove, button)
    return button

  def user_alert(self, damage):
    wx.MessageBox("You dealt %d damage!" % damage, 'Damage', wx.OK | wx.ICON_INFORMATION)

  def mob_alert(self, damage):
    wx.MessageBox("{0} dealt {1} damage!".format(self.battle.mob.name, damage), 'Damage', wx.OK | wx.ICON_INFORMATION)

  def victory(self):
    money = self.battle.mob.loot[0]
    experience = self.battle.mob.experience
    wx.MessageBox("You've defeated {0}! Gained {1} exp, {2} Coins!".format(self.battle.mob.name, experience, money))
    self.character.money += money
    self.character.experience += experience
    self.character.check_level_up()
    self.Hide()
    self.parent.startGame()

  def lost(self):
    money_lost = min(self.character.money, 3000)
    wx.MessageBox("You fainted! Lost %d coins!" % money_lost, 'Lost', wx.OK)
    self.character.money -= money_lost
    self.Hide()
    self.parent.healCharacter()
    self.parent.startGame()
    
  def OnMove(self, evt):
    button = evt.GetEventObject()
    self.battle.user_attack(self.find_by_name(button.Label))

  def find_by_name(self, name):
    for i in self.character.moves:
      if i.name == name:
        return i

  
  def OnEscapeButton(self, evt):
    self.Hide()
    self.parent.chracter = self.character
    self.parent.startGame()
    



class ItemPanel(wx.Panel):
  def __init__(self, parent):
    super(ItemPanel, self).__init__(parent)
    self.parent = parent
    self.master_sizer = wx.BoxSizer(wx.VERTICAL)
    self.character = parent.character
    self.SetBackgroundColour("White")
    
    self.Update()

    self.SetSizer(self.master_sizer)
  def Update(self):
    self.master_sizer.DeleteWindows()
    top_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
       
    equip_button = wx.Button(self, label="Equips")
    potion_button = wx.Button(self, label="Potions")
    recipe_button = wx.Button(self, label="Recipes")
    scroll_button = wx.Button(self, label="Scrolls")

    self.Bind(wx.EVT_BUTTON, self.OnShowEquip, equip_button)
    self.Bind(wx.EVT_BUTTON, self.OnShowPotion, potion_button)
    self.Bind(wx.EVT_BUTTON, self.OnShowRecipe, recipe_button)
    self.Bind(wx.EVT_BUTTON, self.OnShowScroll, scroll_button)

    top_buttons_sizer.AddMany([
      (equip_button, 1, wx.EXPAND),
      (potion_button, 1, wx.EXPAND),
      (recipe_button, 1, wx.EXPAND),
      (scroll_button, 1, wx.EXPAND)
      ])

    self.master_sizer.Add(top_buttons_sizer, 1, wx.EXPAND)
    

    self.equip_update()
    #self.potion_update()
    #self.recipe_update()
    #self.scroll_update()    
  


  def equip_update(self):
    self.equip_sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.equip_icon_sizer = wx.GridSizer(10, 3, 20, 20)
    self.equip_explanation_sizer = wx.BoxSizer(wx.VERTICAL)

    equips = self.character.items["Equipment"]
    print equips
    for i in equips:
      
      button = wx.Button(self, label= i.name + " " + str(i.item_id))
      self.Bind(wx.EVT_BUTTON, self.OnEquipButton, button)
      self.equip_icon_sizer.Add(button)

    self.equip_sizer.Add(self.equip_icon_sizer, 2, wx.EXPAND)
    self.equip_sizer.Add(self.equip_explanation_sizer, 3, wx.EXPAND)
    
    self.master_sizer.Add(self.equip_sizer, 4, wx.EXPAND)
    
    self.parent.Layout()

  def OnEquipButton(self, evt):
    self.equip_explanation_sizer.DeleteWindows()
    
    obj = evt.GetEventObject()
    name = obj.Label
    splits = name.split()
    item_id = int(splits[-1])
    equip = self.find_equip_by_id(self.character.items["Equipment"], int(item_id))
    name = equip.name
    explanation = equip.explanation
    attack = equip.damage
    defense = equip.defense
    #additional = equip.additional.name
    #upgrade = equip.upgrade
    
    name_label = wx.StaticText(self, -1, "Name:  %s" % name, style=wx.ALIGN_CENTRE)
    explanation_label = wx.StaticText(self, -1, "Explanaton:  %s" % explanation, style=wx.ALIGN_CENTRE)
    attack_label = wx.StaticText(self, -1, "Attack:  %s" % str(attack), style=wx.ALIGN_CENTRE)
    defense_label = wx.StaticText(self, -1, "Defense:  %s" % str(defense), style=wx.ALIGN_CENTRE)
    #additional_label = wx.StaticText(self, -1, additional, style=wx.ALIGN_CENTRE)
    #upgrade_label = wx.StaticText(self, -1, upgrade, style=wx.ALIGN_CENTRE)

    self.equip_explanation_sizer.Add(name_label, 1, wx.EXPAND)
    self.equip_explanation_sizer.Add(explanation_label, 1, wx.EXPAND)
    self.equip_explanation_sizer.Add(attack_label, 1, wx.EXPAND)
    self.equip_explanation_sizer.Add(defense_label, 1, wx.EXPAND)

    
    
    self.parent.Layout()


  def OnShowEquip(self, evt):
    self.master_sizer.Show(self.equip_sizer)

  def OnShowPotion(self, evt):
    self.master_sizer.Hide(self.equip_sizer)

  def OnShowRecipe(self, evt):
    self.equip_sizer.Hide()

  def OnShowScroll(self, evt):
    self.equip_sizer.Hide()
    
  def find_equip_by_id(self, equips, item_id):
    for i in equips:
      if i.item_id == item_id:
        return i
      
    
class StorePanel(wx.Panel):
  def __init__(self, parent):
    super(StorePanel, self).__init__(parent)
    
    
    
