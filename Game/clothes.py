from Equipment import *

class Cloth(Equipment):
  def __init__(self):
    super(Cloth, self).__init__()
    self.name = None
    self.additional = None
    self.upgrade_limit = 5
    self.defense = 0
    self.damage = 0

class BasicCloth(Cloth):
  def __init__(self):
    Cloth.__init__(self)
    self.name = "Basic Cloth"
    self.explanation = "The most basic armor given to the starter."
    self.defense = 5
