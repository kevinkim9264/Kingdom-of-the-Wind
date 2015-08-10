from Equipment import *

class Helmet(Equipment):
  def __init__(self):
    super(Helmet, self).__init__()
    self.name = None
    self.additional = None
    self.upgrade_limit = 5
    self.defense = 0
    self.damage = 0


class BasicHelmet(Helmet):
  def __init__(self):
    Helmet.__init__(self)
    self.name = "Basic Helmet"
    self.explanation = "The most basic helmet given to the starter."
    self.defense = 5

    
