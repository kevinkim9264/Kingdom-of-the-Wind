from skills import *
from weapons import *
from helmets import *
from gloves import *
from clothes import *
import wx

class Job(object):

  def __init__(self, userName):
    self.userName = userName
    self.level = 1
    self.level = 1
    self.hp = 20
    self.max_hp = 20
    self.mp = 20
    self.max_mp = 20
    self.money = 1000
    self.experience = 0
    self.required_experience = 30
    self.moves = [BasicAttack()]
    self.potential_moves = {}

    self.required_experiences = self.required_experiences()

    self.equipments = {"weapon": Mokdo(), "helmet": BasicHelmet(),
                       "glove": BasicGlove(), "cloth": BasicCloth()}


    #items = { "Equipment" : [Mokdo, DragonFirst],
    #          "Recipes" : {"Silver Branch" : 3, "Gold Plate" : 2},
    #          "Potions" : {"RedHp10" : 21, "BlueMp10" : 10, "RedHp30" : 20}
    #        }
    self.items = {"Equipment" : [Mokdo(), BasicHelmet()],
                  "Recipe" : {},
                  "Potions" : {"RedHp10" : 5, "BlueMp10" : 5}
                  }

    self.weapon = self.equipments["weapon"]
    self.helmet = self.equipments["helmet"]
    self.glove = self.equipments["glove"]
    self.cloth = self.equipments["cloth"]

    self.update_stats()

  def update_stats(self):
    self.attack_damage = self.weapon.damage + self.helmet.damage + self.glove.damage + self.cloth.damage
    self.defense = self.weapon.defense + self.helmet.defense + self.glove.defense + self.cloth.defense

  def required_experiences(self):
    exp = [0, 0]
    for i in range(2, 200):
      exp.append(i**2 * (i * 100))
    return exp


  def add_move(self):
    if self.level in self.potential_moves:
      self.moves.append(self.potential_moves[self.level])

  def check_level_up(self):
    if self.experience >= self.required_experience:
      self.level_up()

  def level_up(self):
    self.level += 1
    self.required_experience = self.required_experiences[self.level + 1]
    self.update_stats()
    wx.MessageBox("You leveled up to %d !" % self.level, 'Level up!', wx.OK)
    if self.level in self.potential_moves:
      move = self.potential_moves[self.level]
      self.moves.append(move)
      wx.MessageBox("You learned new skill, %s !" % move.name, 'New Skill', wx.OK)


class Rogue(Job):

  def __init__(self, userName):
    super(Rogue, self).__init__(userName)
    self.job = "Rogue"
    self.potential_moves = self.gen_potential_moves()
    
        
  """ Returns potential moves for Rogues job. Hashmap of {Lvl: Skill object}"""
  def gen_potential_moves(self):
    skills = {}
    skills[1] = BasicAttack()
    return skills

  
  

    

class Warrior(Job):
  def __init__(self, userName):
    super(Warrior, self).__init__(userName)
    self.job = "Warrior"
    self.potential_moves = self.gen_potential_moves()

  """ Returns potential moves for Warriors job. Hashmap of {Lvl: Skill object}"""
  def gen_potential_moves(self):
    skills = {}
    skills[1] = BasicAttack()
    return skills


class Bowman(Job):
  def __init__(self, userName):
    super(Bowman, self).__init__(userName)
    self.job = "Bowman"
    self.potential_moves = self.gen_potential_moves()

  """ Returns potential moves for Bowman job. Hashmap of {Lvl: Skill object}"""
  def gen_potential_moves(self):
    skills = {}
    skills[1] = BasicAttack()
    return skills




class Magician(Job):
  def __init__(self, userName):
    super(Magician, self).__init__(userName)
    self.job = "Magician"
    self.potential_moves = self.gen_potential_moves()

  """ Returns potential moves for Magician job. Hashmap of {Lvl: Skill object}"""
  def gen_potential_moves(self):
    skills = {}
    skills[1] = BasicAttack()
    skills[2] = EnergyBolt()
    return skills

