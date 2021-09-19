from gameinventory import printlist,checkitem,dropitem,additem

rusty = True
outside = True
doorclosed = True
haveoil = False
inside = False
quit = False
inv = set([])

outsidedesc = "You are standing outside the front of a house with boarded up windows. All the plants are dead around the door. The brown paint on the outside is chipping."
print(outsidedesc)
while outside and not quit:
  rawcommand = input("What would you like to do? ")
  command = rawcommand.lower().replace('the ', '').replace('at ', '')
  if command == "look door" or command == "look the door" :
    print("You look at the door, the door's hinges are very rusty. The door has a lock on it.")
  elif command == "go north" or command == "go inside" or command == "go in":
    if doorclosed:
      print("The door is closed in front of you.")
    else:
      print("You enter the room. This is the end...for now.")
      outside = False
      inside = True
  elif command == "go south" or command == "go east" or command == "go west":
    print("You can't go that way.")
  elif command == "look plants" or command == "look plant" or command == "look in plants" or command == "look in plant":
    if checkitem("oil", inv):
      print("The plants are dead.")
    else:
      print("The plants are dead. You see something shiny, it's an oil can.")
  elif command == "look hinges":
    print("The hinges are rusty.")
  elif command == "get oil" or command == "get oil can" or command == "take oil" or command == "take oil can":
    print("You now have the oil can.")
    inv = additem("oil", inv)
  elif command == "use oil" or command == "use oil can" or command == "oil hinges":
    if checkitem("oil", inv):
      print("You have oiled the hinges.")
      rusty = False
    else:
      print("You don't have oil.")
  elif command == "look paint":
    print("The paint is chipped.")
  elif command == "look lock":
    print("The lock looks unlocked.")
  elif command == "look around":
    print(outsidedesc)
    if not checkitem("oil", inv):
      print("You think you see something in the plants.")
    if doorclosed:
      print("The door is closed.")
    else:
      print("The door is open.")     
  elif command == "look window" or command == "look windows":
    print("The windows are boarded up.") #cracks?
  elif command == "open door":
    if rusty:
      print("The hinges are too rusty.")
      doorclosed = True
    else:
      print("The door swings open.")
      doorclosed = False
  elif command == "quit":
    print("OK!")
    quit = True
  elif command == "room1":
    outside=False
    inside=True
  else:
    print(f"I can't \"{command}\"...yet?")

roomchair = "on the wall opposite of you there is a rocking chair"
roomdesk = "there is something on the desk that you can't quite make out in the dim light"
room1first = "When you walk in the door it locks behind you. All that you can see in the room is the door that you just came through,"
room1desc = f"{room1first} a desk in one corner, and {roomchair} and {roomdesk}. Everything is very dusty."
#room1desc = "When you walk in the door locks behind you. Inside the room there is a desk in one corner. On the wall opposite of you there is a rocking chair and something you can't quite make out in the dim light. There are four doors. one to your left, one to your right, and one in front of you,as well as the door that you just came through"

if not quit: 
  print(room1desc)

dark = True
draweropen = False
chairbroken = False

while inside and not quit:
  lookchair =  ["look rocking chair", "examine rocking chair", "search rocking chair" ]
  rockingdesc = "The chair looks like it might fall apart at any minute. It is old and very dusty"
  sitchair = ["sit rocking chair", "sit chair"]
  chairsit = "The chair makes a loud creaking noise as you sit in it. As your weight is fully in the chair, it falls to pieces and you land on the ground with a great thud. OUCH!"
  rawcommand = input("What would you like to do? ")
  room1first = "There is"
  room1desc = f"{room1first} a desk in one corner, and {roomchair} and {roomdesk}. Everything is very dusty."
  command = rawcommand.lower().replace('the ', '').replace('at ', '')
  if command == "look around" or command == "look room":
    print(room1desc)
  elif command in lookchair:
    print(rockingdesc)
  elif command in sitchair:
    print(chairsit)
    chairbroken = True
    rockingdesc = "The old rocking chair is now just a pile of broken wood."
    roomchair = "on the wall opposite of you there WAS a rocking chair"
    # room1desc = f"{room1first} a desk in one corner, and {roomchair} and {roomdesk}. Everything is very dusty."
  elif command == "look desk":
    print("You look at the desk you notice that it has a drawer.")
  elif command == "get note" or command == "take note" or command == "grab note" :
    print("you now have the note.")
    additem("note",inv)
  elif command == "open drawer":
    print("You open the drawer there is a note inside.")
    draweropen = True
  elif command == "look table" or command == "look desk":
    print("You look at the desk and see a shiny object hanging from the silhoutte.")
  elif command == "get object" or command == "take object":
    if dark:
      print("you try to take the object and it turns on a lamp to reveal two doors on either side of the room a blue door and a red door.")
      dark = False
      roomdesk = "on the desk is a lamp with a pull cord that is now lighting the room with the red and blue doors on either side of the room"
      # room1desc = f"{room1first} a desk in one corner, and {roomchair} and {roomdesk}. Everything is very dusty."
    else:
      print("You try to pull what you thought was an item but is actually a pull cord to the lamp but the light stays on.")
  elif command == "read note" and checkitem("note", inv):
    print("You read the note it has the numbers 351264 on it.")
  elif command == "quit":
    print("OK!")
    quit = True
  else:
    print(f"I can't \"{command}\"...yet?")

print("Goodbye!!")