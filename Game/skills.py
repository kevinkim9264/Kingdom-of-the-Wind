import wx

class BasicAttack:
  def __init__(self):
    self.name = "Basic Attack"
    self.job = ["Warrior", "Magician", "Bowman", "Rogue"]

  def damage_dealt(self, attacker, weapon, defender):
    dealt = attacker.attack_damage - defender.defense
    return dealt if dealt > 0 else 1

  def cost(self, attacker):
    pass

  def is_possible(self, attacker):
    return True

  def impossible_message(self):
    pass

  

class EnergyBolt:
  def __init__(self):
    self.name = "Energy Bolt"
    self.job = ["Magician"]

  def damage_dealt(self, attacker, weapon, defender):
    dealt = attacker.attack_damage + attacker.level * 2 - defender.defense
    return dealt if dealt > 0 else 1

  def is_possible(self, attacker):
    return attacker.mp >= 5

  def cost(self, attacker):
    attacker.mp -= 5

  def impossible_message(self):
    wx.MessageBox("You don't have enough MP to use this move!", "Not enough", wx.OK)


  
