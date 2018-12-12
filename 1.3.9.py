# -*- coding: utf-8 -*-
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
            print('The rocket is inactive. Needs launch codes.') 
                       
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
            biosphere()
            
        else:
            userAction = raw_input('Can\'t do that.')
        
def cafe():
    global enteredRooms
    print('This is the cafe. Upturned tables and ruptured ketchup packets pepper the floor.')
    print('One of the few tables still standing is a coffee table with a small stack of papers on it.')
    if 'room2' in enteredRooms:
        print('The cafe again. The pools of ketchup ')
    if 'room2' not in enteredRooms:
        enteredRooms += ['room2']
        
def bridge():
    global enteredRooms
    print('You entered Room 3')
    if 'room3' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'room3' not in enteredRooms:
            enteredRooms += ['room3']
#def rocket():

def library():
    global enteredRooms
    global playerItems
    global openedDoors
    exitRoom = False
    if 'library' in enteredRooms:
        print('I see you have returned, with more knowledge to gain, but this is still library.')
    if 'library' not in enteredRooms:
        enteredRooms += ['library']
        print(' This is library, SHHHH!')
        print('You have reached a dead end, there is only one door out, back west(cafe)')
        print('Bookcases tower over you, cobwebs scatter the corners, and a ragged desk sits a middle the room')
        print('There is a worn history book alone on the shelf, gasping to be read')
        print('There is also a darkened bible looking book sitting nonchanlantly in the corner of the room')
    
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'read history book':
            print("The Great War of The Internet Age” stands boldly at the top of the book. It was the date, December 2nd, 2018. T-Series the infamous Indian record company was remarkably close to passing Pewdiepie and becoming theNumber one most subscribed account on the YouTube platform. The 9 year olds were waging the good fight but it wasn’t enough, the gap was closing, and it was an only a matter of hours before the war was lost. It seemed all hope was lost, Mr. Beast had failed, Pewds best friends Jack and Mark had abandoned him. The 9-year-olds regrouped and revitalized their attack strategy. They came out the door swinging gaining a couple thousand subscribers but it wasn’t enough, T-Series was catching up and fast. Greyness loomed over the heads of the 9-year-olds, it seemed that finally that their king would be dethroned, but a miracle happened! Markiplier, Boogie2988, and Jacksepticeye had joined the fight, swinging the tide of battle, the war was not lost, reinforcements had come through this was a major turning point. Markiplier had posted a livestream of him continually talking and not shutting up ever until people subscribed to pewdiepie, and from there the 9-year-olds were off the the races. Jack tweeted a simple but direct poem encouraging his fans, and Davie504 played the Felix’s most hottest song, the T-Series disstrack for 10 hours straight, all collaborations of efforts were pulling through and pewdiepie had regained a comfortable subscriber lead. He ended up pulling 544k subscribers on december 2nd, a very important day in the war of Pewdiepie v. T-Series. Pewds had won this great battle but the war was still not over. Subscribe to Pewdiepie to make a difference again.")
        
        elif userAction.lower() == 'look around':
            print('Only you stand in the library, faced with a daunting task, at the corner of your eye you see a polaroid')
            
        elif userAction.lower() == 'go to desk':
            print('There is a note, "According to the legend, the Devitus that roams this abandoned base, and can be summoned')
            print('You turn the note around, there is a blurred list\n\n\n\n\n\n')
            
            
            
            
            
            print('Step 1: O̴͕͇͕̗̐̀͆n̷̡̢̢̛͉̭̰̭̣͔͔͓̖̳͔̱̺͕̯̮̣̣͙̈́̃̓̇͆̆͌̉̍̉̆̊̋́̎̐̇͂̾͆͘̚ē̷̢̢̛͉̫͎͎͙̫̞̑͗͆͋͗̈́̈́̎̇͆̾̈́͑̂̚̚͠͠͝͠ ̸̛̛̛̤̯̗͓̲̾͒̐͌̄̓͊̂̏̈̂̑͝͠͝͝m̶̛̛̖̰͍̫̯̺͚̤̣̟̫̯̱͎̹̤̝͚͕͙̆͆́̿̒̓̉̍͂̎̐̓͝ͅͅu̵̯̝̠̯̣͎̞̥̘̙͔̥̇͑͆̈̋͐́͒͐͗̿͌̅͆̾̋̂̕͝͝͝s̵̛̰̺͐͌̂̄͐̄͐t̶̹̯̦̮̟̳̮̦̯̞͌́̏̔̓̐̅̈͋̚̚͘͠͝ ̶̡̛̯̞̝̬͍̭̏͌̔̈́̈͆̈́̆̀͊͝͝ͅỉ̵̢̖͍̻̩̱̗̥̘̫̬͔̘̱̘̼ͅn̶̨̢̛̠̮̘̦̦̯̝͎͇̥̞̺͎͚͕͙̏̒̓͗͛͗͐̾́̿̇͒̔̚̚͝f̷̛̯͕̗̩͎͈͓̲̭̥͇͇̝̘̟̬̜̰̬̟̯̗̻̂̃͒̂̏̿̅̊̒̃̔́̀̆̀̎͗̊̈́̀̇́̕ͅͅi̸̢̛̖̫͚̼̞̽̓͂̈́̆̓̇̔̈́̓͋͌́̐̚͘̚̕͜͝͝͝l̴̛̩͓̫̥̲̠̗̝͙͍̪͍̳̗̪̤͉̭̭̮̻̇̃͐̈́̆͆͐̃͆͆̈́͑̔̀̒̂͊̄̾̆̿̕͜͝ͅţ̴̡̧̛͔̟̯̣̪̟̠͔̩̙̹̝̣͚͕̓́̍r̶̗̭̒̔͐̂̅̈́͊̈́̎́̔̋̉̐̑̈́͒͌͜a̷̡̬̲͕̪̻̤̳̤̙̬̘͚͇̳̙̣̳̦̾̀̆̓̏̃̀͛̀̓̓́͋̉́̓̕͘̕͜͝͝t̷̢̛̥̳̽͑͂̑͋̔̓̆̓̈́̊̏͒e̸̢̫̘͓͙̼̭̪͔͙͍̝̥͖͓͎͖͇̙̻͆͛̔̉̒͆̆̽̌̄̒̚͘͜͜͜͠͝ ̷̨̨̮̼̮̼̥͉̼̫̳̻̺̫͚̖̣̯̘̠̠̖͈̽̃̐͛͆̀̏̓̾̈́̀́͠͝ͅț̶̡̧̛̠͎̥̉͊̿̃̔̔͗̀̀́̈́͂̅̂̕͠h̷̝͒̅ȩ̷̛̟͔͍̳̝̗̪͍̱͕̖͉̺͎̗͈̇̂̀͆̌̈́̀͋̔̔̅̿̌̕͝ ̸̼̹̹̻͉̱̭͈̥̟͚̼͕̹͙̱͔̣̓͋̊͊̉͊̉̏̇̇͐̑̈̀̔̋̌̂̂̅́͜͜͜͝ṟ̷̨̛͈̳̣͕̣̱͙̬̬͙͔͓̲̯̖̤͍͆̄̉̒͗o̵͔͕͙̘̙̾ǒ̴̪̝͐͆͆̓͆̓́̃́̄̐͑͘̚͝m̵͚̯͍͎̠̞̲͍̻̥̱̗̘̞̮̠͈̖̣͓̫̹͎͇͂̍̅̑̍̎̐̅̈́̚ ̶̢̲̩͈͖̪̬̮̦̞̬͉͔͚͂̌̈́̎͋̉̒̈́͜͝ẅ̸̧̗̞̘̙̤̰̠͍̼͎̥́̊̏͆̈́͑͗̄̓̑̚̚͜͝͝͝ḫ̶̨̢̪̻̜̩̝̞͖̣̬͎̜̾̉̒e̸̪̙͉̼͉̙̘͕̳̻̘̯̯͛̋̄́̈́͆̍̂̓̈̕̚͝ŗ̷̢̢̛͎̥͕̙̜̯̝̟̙̝̰̻̭̤͉͔̪̖͎̣̮̼̜̿̍̈́̔͐̓̉̅́͛̎̏͠ȇ̴̱͉͕̰̣̪͔̬̦͈̗̦͙̔͛͜ͅ ̶͚̣̦͔̣͇͔͕̣͉͙͙̠̯͇̀̈́̐̃͋͆̉̑́̈̄͘̚c̸͍͉̤̝̤̹̞͔͇̣̬̳͔̪͙͓̑ͅͅḩ̸͉̝̘̹̞̳̟̖̤͈̙̳͙͕͙̹̙͇̭̗̬̿̈́͑͛͂̔̋͊͌͘͝a̶̧͚͖̦̦̯̫̭̳͉̺̥̥͙̱͙̹͚͓͓̮̲̾̈́̃̑̓͌̍̈́̐̉̊͆̊̂̇͑͠͝ͅņ̷̧̛͍̝̬̞̲̟̮̦̮̫͚͕̜̘͓̏͗̌̓͒̃͌͐̕̕͝ͅģ̷̛͚̩͇̙̥̼̼͓̼̙͕͔͔̬̗̬̦͔͖̯͕͇͑͑̀̾̈́̇̽͗̚͜ė̷̢̛͚̖͖̹͕͖̙̅̌͌̔̏͂̓̐̓̍̄̊̌̓̐̔̕ͅs̴͖̀̏̊̊́͛̈́̄̈̎̂̋̈́͛̊̈̌̏̈́̎͝͝ ̴͉̞̺̖̲͉̬̻̟̤̲̻̱̮͍͚͕̗̖̰̥͋͆͒ͅơ̶̹͓͍͇̭̹̩̲̝̟̗̺̮͎̖̻̟̅̂̉̑͂̂̀͌̄̽̿͌̚̕͝ç̷̢̢̨͓͓̭͙̠̙̪͗̾̽̀͗̌͆͂͝c̴̢̰̳̫͎̬͎̤̲̩̟̻͔̩̳̰̀̄̄͗̎͑͂̀̀̈́́̚͜ư̸̢͉͙̤̖̩͇̼̫̍̓̈́̓͛̃̓̋͋̚̕̕͝͠ͅr̸͍̲͑̂̏͌̄.̷̅̂̽̾ \n \n \n \n \n') 
            
            
            
            
            
            print('The rest is too worn to be read.')
            print('Sounds are heard from afar, the scent of AXE brutally and wax brutally invade your nostrils')
            
        elif userAction.lower() == 'look at polaroid' or 'look at photo' or 'look at picture':
            print('You see him, the image has appeared, the Detivus at full might stares blankly into your eyes. Hope escapes you in this moment as the picture of the Detivus overwhelmes all thought.')
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            cafe()
        
        elif userAction.lower() == 'read bible' or 'read bible book' or 'read darkened book' or 'read book 2':
            print('There has been a transcribed passage, it reads: ')
            print('According to the legend, this abandoned lunar base preyed upon by Devitus. He was a great janitor for the crew on shift. But tradegy struck when Devitus missed his armpits with his AXE body spray, shooting it straight into his naked eyeballs. In memoriam the crew placed three candles in secret locations around the lunar home. Legend has it if the three candles are lit, the Devitus can make a grand return.')
            print('The rest is encrypted.')
        else:
            userAction = raw_input('Can\'t do that.')
            
def biosphere():
    global enteredRooms
    global openedDoors
    global playerItems
    exitRoom = False
    if 'biosphere' in enteredRooms:
        print('the birds sing upon your return')
    if 'biosphere' not in enteredRooms:
        enteredRooms += ['biosphere']
        print('You entered the biosphere, trees and lush bombard you, and the scent of flowers penetrate your nose.')
        print('Through the clearing you encounter that the only way out is the way in, back east(hangar)')      
        print('Light flickers from a distance, should you follow, danger awaits.')
    
    while exitRoom == False:
        userAction = raw_input('> ')
        
        if userAction.lower() == 'go west':
            exitRoom = True
        
        elif userAction.lower() == 'follow light' or 'go to light':
            print('You have reached a clearing, wildlife circles around you in almost a satanic way, what appears in front of you is a great unused candle, the light is flickering from above')
            
        elif userAction.lower() == 'light candle' and 'lighter' not in playerItems:
            print('You need a lighter')
            
        elif userAction.lower() == 'light candle' and 'lighter' in playerItems:
            print('The candle is now lit')
            
        elif userAction.lower() == 'look around':
            print('Trees are everywhere, vines hang, birds chirp, however none is to be seen')
            
        elif userAction.lower() == 'climb tree':
            print('Now standing atop the tree you see the entirety of the biosphere, the light flickering before is an old ceiling light giving out')
            
        elif userAction.lower == 'climb vine':
            print('You attempt to climb the vine to reach heaven as that is your only escape but the vine cuts loose and you are sent tumbling to the floor.')
            print('A thump was heard from the distance after your fall')
            
        else:
            userAction = raw_input('Can\'t do that')
        
def lockerroom():
    global enteredRooms
    global openedDoors
    global playerItems
    exitRoom = False
    if 'lockerroom' in enteredRooms:
        print('The luster of the lockers welcome your return')
    if 'lockerroom' not in enteredRooms:
        enteredRooms += ['lockerroom']
        print('You have walked upon another dead end, the only way out is the way you entered, north(bridge)')
        print('Lockers gallantly file the wall of the room, all locked but one remains ajar')
        print('The benches that outline the lockers has been forcefully removed from its hinges and relocated in the center of the room.')
    
    while exitRoom == False:
        userAction = raw_input('> ')
        
        if userAction.lower() == 'go north':
            exitRoom = True
            bridge()
        
        elif userAction.lower() == 'look around':
            print('In an almost satanic way, the locker benches form a table in the middle of the room, with one locker door ajar.')
            
        elif userAction.lower() == 'look in locker' or 'go to locker' or 'check locker' or 'look at locker':
            print('This locker is barren except for a small picture on the top shelf')
            
        elif userAction.lower() == 'look at picture' or 'look at photo' or 'pick up photo' or 'pick up picture':
            print('Just looking at the picture sends gives notions for vomitting, but alas a t-posing Jack Nicholson appears\n, asserting his dominance over Martini whilst on a medical table. A truly cursed image.')
            
        elif userAction.lower() == 'T-pose' or 'tpose' or 't pose':
            print('')
        else:
            userAction = raw_input('Can\'t do that.')
            
def storageroom():
    global playerItems
    global openedDoors
    global enteredRooms
    if 'storageroom' in enteredRooms:
        print('A familiar scent of bleach and windex breezes past you')
    if 'storageroom' not in enteredRooms:
        enteredRooms += ['storageroom']
        print('There are two doors in this room, a secret door, and the way you came - east(cafe)')
        print('Towels and cleaning chemicals scour the area, the mops lay arest on a side door that appears to be locked, with a "Restricted Access" sign above it.')
        print('The room is a mess, there remains one light that shines brillantly into the equipment below.')
    exitRoom = False
    
    while exitRoom == False:
        userAction = raw_input('> ')
        
        if userAction.lower() == 'open door' or 'use key' or 'use secret key' and 'secretKey' in playerItems:
            print('As you shove open the door you fall and land fresh moon surface. Because you are so illfully prepared, oxygen escapes you in the burning temperatures of the moon as you face the sun. \n You collaspe, dead and numb. \n \n GAME OVER')
            break
        
        elif userAction.lower() == 'open door' or 'use key' or 'use secret key' and 'secretKey' not in playerItems:
            print('The door is locked, "RESTRICTED ACCESS" reads across the door, a key is required')
            
        elif userAction.lower() == 'look around':
            print('Clorox wipes and bleach line the shelfs, bottles of windex are scattered across the floor. It feels as if something could be hiding.')
            
        elif userAction.lower() == 'look through shelves' or 'look at shelves':
            print('By removing the bleach and the wipes has led you to find a very important key to the command center')
            playerItems += 'ccKey'
        
        elif userAction.lower() == 'go east':
            exitRoom = True
            cafe()
        
        elif userAction.lower() == 'look through floor' or 'scavenge floor':
            print('Through the mess of cleaning equipment, nothing was found, only a bigger mess was created.')
            
        else:
            userAction = raw_input('Can\'t do that.')
        
            