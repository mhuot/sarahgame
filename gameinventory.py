def additem(item, inventory):
  inventory.add(item)
  return inventory

def printlist(inventory):
  if not inventory:
    print("You aren't carrying anything")
  else:
    print("You are carrying - ")
    for entry in inventory:
      print(entry)

def dropall(inventory):
  return set([])

def dropitem(item, inventory):
  newinventory = set([])
  for entry in inventory:
    # print(f"Checking {entry}")
    if entry != item:
      newinventory.add(entry)
    #   print(f"Readding {entry}")
    # else:
    #   print(f"Dropping {entry}")
  return newinventory

def checkitem(item, inventory):
  for entry in inventory:
    if entry == item:
      return True
  return False