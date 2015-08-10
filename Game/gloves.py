from Equipment import *

class Glove(Equipment):
  def __init__(self):
    super(Glove, self).__init__()
    self.name = None
    self.additional = None
    self.upgrade_limit = 5
    self.defense = 0
    self.damage = 0

class BasicGlove(Glove):
  def __init__(self):
    Glove.__init__(self)
    self.name = "Basic Glove"
    self.explanation = "The most basic glove given to the starter."
    self.defense = 3
