from Equipment import *

class Weapon(Equipment):
  def __init__(self):
    super(Weapon, self).__init__()
    self.name = None
    self.additional = None
    self.upgrade_limit = 5
    self.defense = 0
    self.damage = 0

class Mokdo(Weapon):
  def __init__(self):
    Weapon.__init__(self)
    self.name = "Mokdo"
    self.explanation = "The most basic weapon given to the starter."
    self.damage = 20
