class Equipment(object):
  item_id = 0 #Each equipment object has unique item_id
  def __init__(self):
    self.item_id = Equipment.item_id
    Equipment.item_id += 1
