from baram_panels import *


class Battle:
  def __init__(self, frame, character, mob):
    self.character = character
    self.mob = mob
    self.battle_panel = BattlePanel(frame, self)


  """ Start of a battle"""
  def start(self):
    wx.MessageBox('A wild %s has appeared!' % self.mob.name, 'Mob', wx.OK | wx.ICON_INFORMATION)
    self.battle_panel.draw()

  def mob_defeated(self):
    return self.mob.hp <= 0

  def user_defeated(self):
    return self.character.hp <= 0

  
  def user_attack(self, move):
    if move.is_possible(self.character):
      damage = move.damage_dealt(self.character, self.character.weapon,
                               self.mob)
      move.cost(self.character)
      self.mob.hp = self.mob.hp - damage
    
      self.battle_panel.user_alert(damage)
      if self.mob_defeated():
        self.mob_defeated_event()
      else:
        self.mob_attack()
    else:
      move.impossible_message()

  def mob_attack(self):
    damage = self.mob.attack_damage - self.character.defense
    damage = 1 if damage <= 0 else damage
    self.character.hp -= damage
    self.battle_panel.mob_alert(damage)
    print self.character.hp
    if self.user_defeated():
      self.character_defeated_event()
      
    else:
      self.battle_panel.draw()

  def mob_defeated_event(self):
    self.battle_panel.victory()

  def character_defeated_event(self):
    self.battle_panel.lost()
