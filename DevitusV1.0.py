# -*- coding: utf-8 -*-
from __future__ import print_function
#import random



litCandles = []
playerItems = []
enteredRooms = []
unlockedDoors = []
rocketOn = False



hasSmCnd, hasBgCnd, hasScCnd, hasCcKey, hasSecKey, hasLighter = False

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
    global litCandles
    exitRoom = False
    print('(Hangar)')    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        if userAction.lower() == 'look rocket':
            print('The rocket is innactive. Needs launch codes.') 
                       
        elif userAction.lower() == 'look around':
            print('\nThe hangar is barren. There\'s not a soul in sight.')
            print('There are four doors in this room.  One to the north(cafe), one to the east(bridge),')
            print('one to the south(boiler room), and one to the west(bioshpere).')
            print('There is a rocket ship behind where you\'re standing, but it doesn\'t seem to be functional at the moment.')
            
        elif userAction.lower() == 'enter rocket' and rocketOn == True:
            exitRoom = True
            #rocket()            
            
        elif userAction.lower() == 'enter rocket' and rocketOn == False:
            print('You can\'t enter the rocket without the launch codes.')
            
            
        elif userAction.lower() == 'go north':
            exitRoom = True
            cafe()
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            boiler()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            biosphere()
            
        else:
            print('Can\'t do that.')
        
def cafe():
    global enteredRooms
    global playerItems
    global litCandles
    exitRoom = False
    if 'room2' in enteredRooms:
        print('The cafe again. The pools of ketchup have dried a little.')
    if 'room2' not in enteredRooms:
        enteredRooms += 'room2'
        print('\nThis is the cafe. Upturned tables and ruptured ketchup packets pepper the floor.')        
        print('\nOne of the few tables still standing is a coffee table with a small stack of papers on it, and a deli bar light is flickering on and off.') 
               
    while exitRoom == False:
        userAction = raw_input('\n> ')
        if userAction.lower() == 'look table' or userAction.lower() == 'look coffee table':
            print('\nThe table doesn\'t have much on it besides lunch lists...')
            print('\nAnd a piece of paper that says "Flip to other side."') 
                       
        elif userAction.lower() == 'look around':
            print('\nThe cafe seems to have been abandoned in a hurry. The place is a mess.')
            
        elif userAction.lower() == 'flip paper' or userAction.lower() == 'flip page':
            print('\nYou flip the page over. The other side says "Flip to other side."')
            for i in range(10):
                print('\nYou flip the page.')
            print('\nYou get dizzy and stop.')
            
        elif userAction.lower() == 'look bar' or userAction.lower() == 'look deli' or userAction.lower() == 'look deli bar':
            print('\nAll the food is gone but there\'s a lighter sitting where the corn bread should be.')
            
        elif userAction.lower() == 'take lighter' and 'lighter' not in playerItems:
            print('\nYou pick up the old grill lighter and give is a test click. It still works.')
            playerItems += 'lighter'
            
        elif userAction.lower() == 'take bread' or userAction.lower() == 'take corn bread' and 'lighter' not in playerItems:
            print('\nYou went to get some bread but alas you got a lighter instead.')
            playerItems += 'lighter'
            
        
            
        elif userAction.lower() == 'go north':
            print('Only a wall that way.')
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            hangar()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            library()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            storageroom()
            
        else:
            print('Can\'t do that.')    
    
            
def bridge():
    global enteredRooms
    global litCandles
    exitRoom = False
    
    if 'bridge' in enteredRooms:
        print('The bridge again.')
    if 'bridge' not in enteredRooms:
        print('You entered the bridge. There\'s a massive circular door on the east side of the room, and on the south side is a smaller door with a sign that says "Locker Room"')
        enteredRooms += 'bridge'
            
    while exitRoom == False:
        userAction = raw_input('\n> ')
        if userAction.lower() == 'look rocket':
            print('The rocket is innactive. Needs launch codes.') 
                       
        elif userAction.lower() == 'look around':
            print('The bridge appears directed towards a large circular door. "Command Center," according to the sign')            
            
        elif userAction.lower() == 'go north':
            print('\nYou went north until you hit a huge wall. Which was only a few meters away, so you\'re still in the bridge.')
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            lockerroom()
            
            
        elif userAction.lower() == 'go east' and 'ccKey' in playerItems:
            exitRoom = True
            commandCenter()
            
        elif userAction.lower() == 'go east' and 'ccKey' not in playerItems:
            print('It\'s useless trying to open that gigantic door without a key.')    
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            hangar()
            
        else:
            print('Can\'t do that.')
            
def rocket():    
    global playerItems
    exitShip = False
    print('You board the ship. The only things you can do are take off to escape back to Earth, or exit the ship.')    
    while exitShip == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'take off':
            print('')
        elif userAction.lower() == 'exit ship':
            exitShip = True
            hangar()
            
def commandCenter():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    deskItems = ['the launch codes']
    if 'cc' in enteredRooms:
        print('The command center has not gotten tidier.')
    else:
        print('You have entered Command Control')
        print('There are no other doors in this room besides the one you entered (west)')
        print('There is a circular table with a pile of important looking papers on it in the center of the room.')
        print('But perhaps more notably there is a gigantic mess written on the east wall in purple slime that looks like: ')
        
        print('\n\n\n\n\n\n')
        
        
        
        print('D̷̹͍̎̆́͘ͅͅE̵̛͙̭͖̥͖̳̠̗̦̮̒̀͊͐͋̽̀̀͒̾͝ͅḶ̸̛͔͑̅̅͌̋̔̅̔̉̈́̊͛͊͜͝ͅE̵̳̯͖̱̳̱͛T̵̢̞̳͉͉̫̱̹̿̿̀̍̌̎̃̽͑̉̅̃͝Ư̵̢͉̪͚̼͌̑͌͐̓̊̽̋͛͆̚͝͠Ş̸̗̗̹̿̾̀̄̔͛͋͝ ̴̳̩̠̪̒͒̀͂̽̅̚ͅD̶̢̒̓͋̉̍̓̽̓̾̆̇̈́̕͠͝Ȇ̵̳̯̠̬͈̺͈̬̜̞̎͑͒̈̓͒͑͋͆͜͝V̶̢̢̧̢̦̥͓͖͖̤̬͎̖̝͉̉͛̂̊̽͛̈̐̈́̀̔̓̄͘I̴̧̢̼͔̘̳̬̣̫̬͂̋̀͆͛T̷̰͚̻̐̎̎̀́̋̑̓̿̀̄́́̑Ủ̶̡͇̪͚͖̪̥̍͆̌͐̈̈̌͜Ş̷̛̰͙̣͖̲̙͉̰̗̫̮͖̗̈̉̎͠')
        
        
        
        print('You can almost read it if you squint... Deletus Devitus... interesting.')
        
        enteredRooms += 'cc'
    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        if userAction == 'look around':
            print('There\'s a des.')
	    
        elif userAction == 'look papers':
            print('You shuffle the papers to see the launch codes.')
	    
        elif userAction == 'take launch codes':
            print('You picked up the launch codes. Your rocket should work now.')
            playerItems += deskItems
            deskItems = []
            
            
        elif userAction == 'go east':
            print('This is already the eastest point of the entire base.')
            
        elif userAction == 'go north':
            print('You decided not to on account of the wall in the way.')
            
	elif userAction == 'go south':
	    print('No way south from here.')
	    
	elif userAction == 'go west':
	    exitRoom = True
	    bridge()
        else:
            print('Can\'t do that.')

def library():
    global enteredRooms
    global playerItems
    global openedDoors
    global litCandles
    roomItems = ['smallCandle']
    dvHist = False
    exitRoom = False
    print('\nThis is library.')
    print('\nYou have reached a dead end, there is only one door out, back west(cafe)')
    print('\nBookcases tower precariously over you, cobwebs scatter the corners, and a ragged desk sits at the center of the room.')
    print('\nThere is also a worn history book alone on a shelf off to the side with a faded red triangle on the cover.')
    if 'library' in enteredRooms:
        print('The book cases seem even closer to falling than before')
    else:
        enteredRooms += ['library']
    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        if userAction.lower() == 'read book':
            print("The Great War of The Internet Age” stands boldly at the top of the book. It was the date, December 2nd, 2018. T-Series the infamous Indian record company was remarkably close to passing Pewdiepie and becoming theNumber one most subscribed account on the YouTube platform. The 9 year olds were waging the good fight but it wasn’t enough, the gap was closing, and it was an only a matter of hours before the war was lost. It seemed all hope was lost, Mr. Beast had failed, Pewds best friends Jack and Mark had abandoned him. The 9-year-olds regrouped and revitalized their attack strategy. They came out the door swinging gaining a couple thousand subscribers but it wasn’t enough, T-Series was catching up and fast. Greyness loomed over the heads of the 9-year-olds, it seemed that finally that their king would be dethroned, but a miracle happened! Markiplier, Boogie2988, and Jacksepticeye had joined the fight, swinging the tide of battle, the war was not lost, reinforcements had come through this was a major turning point. Markiplier had posted a livestream of him continually talking and not shutting up ever until people subscribed to pewdiepie, and from there the 9-year-olds were off the the races. Jack tweeted a simple but direct poem encouraging his fans, and Davie504 played the Felix’s most hottest song, the T-Series disstrack for 10 hours straight, all collaborations of efforts were pulling through and pewdiepie had regained a comfortable subscriber lead. He ended up pulling 544k subscribers on december 2nd, a very important day in the war of Pewdiepie v. T-Series. Pewds had won this great battle but the war was still not over. Subscribe to Pewdiepie to make a difference again. \n*This is not related to the game*")
        
        elif userAction.lower() == 'look around':
            print('The bookshelves seem to go up forever.')
            
        elif userAction.lower() == 'go to desk' or userAction.lower() == 'look desk':
            if dvHist:
                if raw_input('Do you want to read about the Devitus? Y/N\n> ').lower() == 'y':
                    print('\nThere is a note, "According to the legend, the Devitus that roams this abandoned base can be summoned and excorcised."')
                    print('\nYou turn the note around, there is a smudged list') 
                    print('\nStep 1: Summoning the Devitus requires three(3) open flames. Candles will do. Gather and light these.')
                    print('\nStep 2: Bring the candles to the location of the death of the demon\'s body.') 
                    print('\nStep 3: To complete the ritual, one must perform a "T-Pose" to assert dominance over spirit.')
                    print('This act will force it out of hiding.')           
                    print('\nStep 4: To exorcise the Devitus, must say an incantation in its presence. This i..-.')
                    print('\nThe rest of the note is smudged beyond legibility.')
                    print('A small candle is taped to the bottom of the page with a polaroid.')
        elif userAction.lower() == 'look polaroid':
            print('\nYou see him. The Detivus at full might stares blankly into your eyes. Hope escapes you in this moment as the picture of the Detivus overwhelmes all thought.')
            print('\nYou quickly put the picture down before you get too caught up.')
        
        elif userAction.lower() == 'take candle' and 'smallCandle' not in playerItems:
            print('\nYou took the small candle.')
            playerItems += 'smallCandle'
            roomItems -= 'smallCandle'
        
        elif userAction.lower() == 'go north':
            print('\nNowhere to go that way')
            
        elif userAction.lower() == 'go south':
            print('\nThere\'s probably a spider that way. You stay where you are.')            
            
        elif userAction.lower() == 'go east':
            print('\nYou can\'t traverse deeper into the library.')
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            cafe()
        
        else:
            print('Can\'t do that.')
            
def biosphere():
    global enteredRooms
    global openedDoors
    global playerItems
    global litCandles
    roomItems = ['bigCandle']
    vineClimbed = False
    exitRoom = False
    print('You entered the biosphere, trees and lush bombard you, and the scent of flowers penetrates your nose.')
    print('Through the clearing you encounter that the only way out is the way in, back east(hangar)')      
    print('Light flickers from a distance, a path to follow it is clear. What awaits, however, is not.')
    if 'biosphere' in enteredRooms:
        print('The birds sing upon your return. The followable light is still ahead.')
    else:
        enteredRooms += ['biosphere']        
        print('You entered the biosphere, trees and lush bombard you, and the scent of flowers penetrates your nose.')
        print('Through the clearing you encounter that the only way out is the way in, back east(hangar)')      
        print('Light flickers from a distance, a path to follow it is clear. What awaits, however, is not.')
    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        
        if userAction.lower() == 'go east':
            exitRoom = True
            hangar()
            
        elif userAction.lower() == 'go north' or userAction.lower() == 'go south' or userAction.lower() == 'go west':
            print('Nothing that way but thick foliage and the dome wall.')
        
        elif userAction.lower() == 'follow light':
            print('You have reached a clearing, wildlife circles around you. What appears in front of you is a great unused candle, the light is flickering from above')
        
        elif userAction.lower() == 'take candle' and 'bigCandle' not in playerItems:
            print('You grab the candle and shake some mulch off it.')    
            playerItems += 'bigCandle'
            roomItems -= 'bigCandle'
            
        elif userAction.lower() == 'look around':
            print('Trees are everywhere, vines hang, birds chirp, however none is to be seen')
            
        elif userAction.lower() == 'climb tree':
            print('Now standing atop the tree you see the entirety of the biosphere, the light flickering before is an old ceiling light giving out')
            
        elif userAction.lower == 'climb vine' and vineClimbed == False:
            print('You attempt to climb the vine to reach heaven as that is your only escape but the vine cuts loose and you are sent tumbling to the floor.')
            print('A percussive thump fills the air when you land.')
        
        elif userAction.lower == 'climb vine' and vineClimbed == True:
            print('Better not.')    
            
        else:
            print('Can\'t do that')
            
def boiler():
    global playerItems
    global enteredRooms
    global openedDoors
    global litCandles
    exitRoom = False
    
    print('\nIt\'s warm and dry in here. Smells like a swimming pool if it was recently boiled. Yup, this is the boiler room.')
    print('\nThe only door in this room is the way you came in(north).')
    print('\nThere\'s some kind of candle down in the corner, and you can see a metallic glint under the boiler.')
    
    while exitRoom == False:
       userAction = raw_input('\n> ')
       
       if userAction.lower() == 'look around':
           print('It\'s a confined space. The green glow of LED status lights from the boiler units are all that light this room.')
           
       elif userAction.lower() == 'look boiler' or userAction.lower() == 'look under boiler':
            print('You spy a single key tucked under the cast metal boiler.')
            
       elif userAction.lower() == 'take key' and 'secretKey' not in playerItems:
            print('You took the key.')
            hasSecKey = True
            
       elif userAction.lower() == 'take candle' and 'scentedCandle' not in playerItems:
            print('You took the candle. Seems to be... maple syrup scented. Nice(?)')
            playerItems += 'scentedCandle'
       
       elif userAction.lower() == 'go north':
            exitRoom = True
            hangar()
            
       elif userAction.lower() == 'go south':
            print('You\'re as far south as you can get. Content with your southerliness, you stay put.')
            
            
       elif userAction.lower() == 'go east':
            print('No way through that wall.')
            
       elif userAction.lower() == 'go west':
            print('No way wester.')
        
       else:
            print('Can\'t do that.')     
                   
def lockerroom():
    global enteredRooms
    global openedDoors
    global playerItems
    exitRoom = False
    if 'lockerroom' in enteredRooms:
        print('The luster of the lockers welcome your return.')
    if 'lockerroom' not in enteredRooms:
        enteredRooms += 'lockerroom'
        print('You have walked upon another dead end, the only way out is the way you entered, north(bridge)')
        print('Lockers gallantly file along the wall of the room, all locked except one that remains ajar')
        print('The benches that once ran parallel to the lockers have been forcefully removed from their hinges and relocated in the center of the room.')
    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        
        if userAction.lower() == 'go north':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go east' or userAction.lower() == 'go south' or userAction.lower() == 'go west':
            print('Can\'t go through lockers.')
        
        elif userAction.lower() == 'look around':
            print('In an almost satanic way, the locker benches form a table in the middle of the room, with one locker door ajar.')
            
        elif userAction.lower() == 'look at locker' or userAction.lower() == 'check locker' or userAction.lower() == 'look locker':
            print('This locker is barren except for a small picture on the top shelf')
            
        elif userAction.lower() == 'look picture' or userAction.lower() == 'look photo':
            print('Just looking at the picture sends gives notions for vomitting, but alas a t-posing Jack Nicholson appears\n, asserting his dominance over Martini whilst on a medical table. A truly cursed image.')
            
        elif userAction.lower() == 't-pose' or userAction.lower() == 'tpose' or userAction.lower() == 't pose':
            print('')
            
        else:
            print('Can\'t do that.')
            
def storageroom():
    global playerItems
    global openedDoors
    global enteredRooms
    if 'storageroom' in enteredRooms:
        print('A familiar scent of bleach and windex breezes past you')
    if 'storageroom' not in enteredRooms:
        enteredRooms += 'storageroom'
        print('There are two doors in this room. The secret door, and the way you came - east(cafe)')
        print('Towels and cleaning chemicals scour the area, the mops lay arest on a side door that appears to be locked, with a "Restricted Access" sign above it.')
        print('Shelves of cleaning supplies are still somewhat organized.')
    exitRoom = False
    
    while exitRoom == False:
        userAction = raw_input('\n> ')
        
        if (userAction.lower() == 'open door' and 'secretKey' in playerItems) or (userAction.lower() == 'use key' and 'secretKey' in playerItems) or (userAction.lower() == 'use secret key' and 'secretKey' in playerItems):
            print('After a loud wooosh, all sound is gone. \nAs you shove open the door you fall and land on fresh moon surface, oxygen escapes you in the burning temperatures of the moon as you face the sun. \n You collaspe, dead and numb. \n \n GAME OVER')
            break
        
        elif userAction.lower() == 'open door' and 'secretKey' not in playerItems:
            print('The door is locked. "RESTRICTED ACCESS" reads across the door, a key is required.')
            
        elif userAction.lower() == 'look around':
            print('Clorox wipes and bleach line the shelfs, bottles of windex are scattered across the floor. It feels as if something could be hiding.')
            
        elif (userAction.lower() == 'look through shelves' and 'ccKey' not in playerItems) or (userAction.lower() ==  'look shelves' and 'ccKey' not in playerItems):
            print('By removing the bleach and the wipes has led you to find a key card labelled "COMMAND CENTER" in bold font.')
         
        elif (userAction.lower() == 'look through shelves' and 'ccKey' in playerItems) or (userAction.lower() ==  'look shelves' and 'ccKey' in playerItems):
            print('Nothing of interest.')
            
        elif userAction.lower() == 'take card' or userAction.lower() == 'take key card' or userAction.lower() == 'take key':
            print('You took the key card.')
            playerItems += 'ccKey'
        
        elif userAction.lower() == 'go east':
            exitRoom = True
            cafe()
        
        elif userAction.lower() == 'look through floor' or 'scavenge floor':
            print('Through the mess of cleaning equipment, nothing was found, only a bigger mess was created.')
            
        else:
            print('Can\'t do that.')                      
                                 
                                        
                                               
                                                      
                                                                    