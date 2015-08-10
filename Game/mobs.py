

class Mob:
  @staticmethod
  def mob(level):
    if level == "10-20":
      return Rattat()


class Rattat:
  def __init__(self):
    self.name = "Rattat"
    self.hp = 5
    self.mp = 10
    self.attack_damage = 15
    self.defense = 3
    self.loot = [500]
    self.experience = 10
