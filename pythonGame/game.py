#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  #You can go south, north, east & west if they have access.
  # Get to the final destination with right items and moves.
  print('''
DEFEAT PYTHON
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' , list(rooms[currentRoom]['item'].keys()))
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : {'key':'Use key to open the door', 'Knife':'Grab a knife enemies'},
                
                },

            'Kitchen' : { 
                  'north' : 'Hall',
                  'item'  : {'monster':'Got you!'},
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Living Room',
                  'item' : {'potion':'It might give you a life line'},
                  'north' : 'Pantry',
               },
        
            'Living Room' : { 
                  'north' : 'Prayer Room',
                  'south' : 'Basement',
                  'east' : 'Study Room',
                  'item'  : {'beer':'Happy Friday'},
                },
            'Prayer Room' : { 
                  'item'  : {'bible':'Keep reading bible because you are stucked here FOREVER'},
                },
            'Basement' : { 
                  'north' : 'Living Room',
                  'item'  : {'grinder':'I hope you are ready for it'},
                },
            'Study Room' : { 
                  'west' : 'Living Room',
                  'item'  : {'magic carpet':'Fly with me'},
                },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : {'cookie':'Life saver'},
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(' got!' + move[1] )
      print(rooms[currentRoom]['item'][move[1]])

      #delete the item from the room
    #   if len(rooms[currentRoom]['item'])<1:
      del rooms[currentRoom]['item'][move[1]]

      if len(rooms[currentRoom]['item'])<1:
          del rooms[currentRoom]['item']
    
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win

  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  elif currentRoom == 'Study Room' and 'magic carpet'in inventory and 'beer' in inventory:
    print('You found Magic Carpet to fly you to the Garden.. YOU WIN!..Enjoy your Chilled Beer in the garden')
    break
  elif currentRoom == 'Kitchen' and 'monster' in rooms[currentRoom] and 'cookie' in inventory:
    print('Monster is more interested in your cookie..He ran with your cookie')
    break

  elif currentRoom == 'Prayer Room':
    print('There are no way out. You are TRAPPED...You LOSE!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
  

  elif 'item' in rooms[currentRoom] and 'grinder' in rooms[currentRoom]['item']:
    print('You got trapped in a room with human grinder. It chopped you into pieces... GAME OVER!')
    break
