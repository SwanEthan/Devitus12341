from __future__ import print_function
#import random

playerItems = ['picture of target']
enteredRooms = []
unlockedDoors = []
rocketOn = False

def startGame():
    print('')
    print('Alarms are blaring. The Earth looms in the skylight above you.')
    print('You can\'t quite place the feeling, but something is very wrong here.')
    raw_input('Press enter to step into the hangar.')
    hangar()
    

def hangar():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    print('The hangar is barren. There\'s not a soul in sight.')
    print('There are two doors in this room.  One to the north(cafe), one to the east(bridge),')
    print('one to the south(boiler room), and one to the west(bioshpere).')
    print('There is a rocket ship behind where you\'re standing, but it doesn\'t seem to be functional at the moment.')
    
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'look rocket':
            print('The rocket is innactive. Needs launch codes.') 
                       
        elif userAction.lower() == 'look around':
            print('The hangar is abandoned.')
            
        elif userAction.lower() == 'enter rocket' and rocketOn == True:
            exitRoom = True
            rocket()            
            
        elif userAction.lower() == 'enter rocket' and rocketOn == False:
            print('You can\'t enter the rocket without the launch codes.')
            
        elif userAction.lower() == 'look picture' or 'look at picture' or 'look at photo':
            print('You examine the picture of your target. Though shrewd in stature, the Devitus is a remarkable foe.')
            print('The demon\'s smile creeps you out, so you put the photo away.')
            
        elif userAction.lower() == 'go north':
            exitRoom = True
            cafe()
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            boilerroom()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            biospere()
            
        else:
            userAction = raw_input('Can\'t do that.')
        
def cafe():
    global enteredRooms
    global playerItems
    exitRoom = False
    if 'room2' in enteredRooms:
        print('The cafe again. The pools of ketchup have dried a little.')
    if 'room2' not in enteredRooms:
        enteredRooms += ['room2']
        print('This is the cafe. Upturned tables and ruptured ketchup packets pepper the floor.')        
        print('One of the few tables still standing is a coffee table with a small stack of papers on it, and a deli bar light is flickering on and off.') 
               
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'look table' or userAction.lower() == 'look coffee table':
            print('The table doesn\'t have much on it besides lunch lists...')
            print('And a piece of paper that says "Flip to other side."') 
                       
        elif userAction.lower() == 'look around':
            print('The cafe seems to have been abandoned in a hurry. The place is a mess.')
            
        elif userAction.lower() == 'flip paper' or userAction.lower() == 'flip page':
            print('You flip the page over. The other side says "Flip to other side."')
            for i in range(10):
                print('You flip the page.')
            print('You get dizzy and stop.')
            
        elif userAction.lower() == 'look bar' or userAction.lower() == 'look deli' or userAction.lower() == 'look deli bar':
            print('All the food is gone but there\'s a lighter sitting where the corn bread should be.')
            
        elif userAction.lower() == 'take lighter':
            print('You pick up the old grill lighter and give is a test click. It still works.')
            playerItems += 'lighter'
            
        elif userAction.lower() == 'take bread' or userAction.lower() == 'take corn bread':
            print('You went to get some bread but alas you got a lighter instead.')
            playerItems += 'lighter'
            
        elif userAction.lower() == 'look picture' or 'look at picture' or 'look at photo':
            print('You examine the picture of your target. Though shrewd in stature, the Devitus is a remarkable foe.')
            print('The demon\'s smile creeps you out, so you put the photo away.')
            
        elif userAction.lower() == 'go north':
            exitRoom = True
            cafe()
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            boilerroom()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            biospere()
            
        else:
            userAction = raw_input('Can\'t do that.')    
    
            
def bridge():
    global enteredRooms
    exitRoom = False
    print('You entered the bridge. There\'s a massive circular door on the east side of the room, and on the south side is a smaller door with a sign that says "Locker Room"')
    if 'room3' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'room3' not in enteredRooms:
            enteredRooms += ['room3']
            
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'look rocket':
            print('The rocket is innactive. Needs launch codes.') 
                       
        elif userAction.lower() == 'look around':
            print('The hangar is abandoned.')
            
        elif userAction.lower() == 'enter rocket' and rocketOn == True:
            exitRoom = True
            rocket()            
            
        elif userAction.lower() == 'enter rocket' and rocketOn == False:
            print('You can\'t enter the rocket without the launch codes.')
            
        elif userAction.lower() == 'look picture' or 'look at picture' or 'look at photo':
            print('You examine the picture of your target. Though shrewd in stature, the Devitus is a remarkable foe.')
            print('The demon\'s smile creeps you out, so you put the photo away.')
            
        elif userAction.lower() == 'go north':
            exitRoom = True
            cafe()
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            boilerroom()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            biospere()
            
        else:
            userAction = raw_input('Can\'t do that.')
#def rocket():
    










