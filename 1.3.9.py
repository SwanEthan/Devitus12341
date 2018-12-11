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
    print(' This is library, SHHHH!')
    print('You have reached a dead end, there is only one door out, back west(cafe)')
    print('Bookcases tower over you, cobwebs scatter the corners, and a ragged desk sits a middle the room')
    print('There is a worn history book alone on the shelf, gasping to be read')
    if 'library' in enteredRooms:
        print('I see you have returned, with more knowledge to gain')
    else:
        enteredRooms += ['library']
    
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'read book':
            print("The Great War of The Internet Age” stands boldly at the top of the book. It was the date, December 2nd, 2018. T-Series the infamous Indian record company was remarkably close to passing Pewdiepie and becoming theNumber one most subscribed account on the YouTube platform. The 9 year olds were waging the good fight but it wasn’t enough, the gap was closing, and it was an only a matter of hours before the war was lost. It seemed all hope was lost, Mr. Beast had failed, Pewds best friends Jack and Mark had abandoned him. The 9-year-olds regrouped and revitalized their attack strategy. They came out the door swinging gaining a couple thousand subscribers but it wasn’t enough, T-Series was catching up and fast. Greyness loomed over the heads of the 9-year-olds, it seemed that finally that their king would be dethroned, but a miracle happened! Markiplier, Boogie2988, and Jacksepticeye had joined the fight, swinging the tide of battle, the war was not lost, reinforcements had come through this was a major turning point. Markiplier had posted a livestream of him continually talking and not shutting up ever until people subscribed to pewdiepie, and from there the 9-year-olds were off the the races. Jack tweeted a simple but direct poem encouraging his fans, and Davie504 played the Felix’s most hottest song, the T-Series disstrack for 10 hours straight, all collaborations of efforts were pulling through and pewdiepie had regained a comfortable subscriber lead. He ended up pulling 544k subscribers on december 2nd, a very important day in the war of Pewdiepie v. T-Series. Pewds had won this great battle but the war was still not over. Subscribe to Pewdiepie to make a difference again.")
        
        elif userAction.lower() == 'look around':
            print('Only you stand in the library, faced with a daunting task, at the corner of your eye you see a polaroid')
            
        elif userAction.lower() == 'go to desk':
            print('There is a note, "According to the legend, the Devitus that roams this abandoned base, and can be summoned')
            print('You turn the note around, there is a blurred list\n\n\n\n\n\n')
            
            
            
            
            
            print('Step 1: O̴͕͇͕̗̐̀͆n̷̡̢̢̛͉̭̰̭̣͔͔͓̖̳͔̱̺͕̯̮̣̣͙̈́̃̓̇͆̆͌̉̍̉̆̊̋́̎̐̇͂̾͆͘̚ē̷̢̢̛͉̫͎͎͙̫̞̑͗͆͋͗̈́̈́̎̇͆̾̈́͑̂̚̚͠͠͝͠ ̸̛̛̛̤̯̗͓̲̾͒̐͌̄̓͊̂̏̈̂̑͝͠͝͝m̶̛̛̖̰͍̫̯̺͚̤̣̟̫̯̱͎̹̤̝͚͕͙̆͆́̿̒̓̉̍͂̎̐̓͝ͅͅu̵̯̝̠̯̣͎̞̥̘̙͔̥̇͑͆̈̋͐́͒͐͗̿͌̅͆̾̋̂̕͝͝͝s̵̛̰̺͐͌̂̄͐̄͐t̶̹̯̦̮̟̳̮̦̯̞͌́̏̔̓̐̅̈͋̚̚͘͠͝ ̶̡̛̯̞̝̬͍̭̏͌̔̈́̈͆̈́̆̀͊͝͝ͅỉ̵̢̖͍̻̩̱̗̥̘̫̬͔̘̱̘̼ͅn̶̨̢̛̠̮̘̦̦̯̝͎͇̥̞̺͎͚͕͙̏̒̓͗͛͗͐̾́̿̇͒̔̚̚͝f̷̛̯͕̗̩͎͈͓̲̭̥͇͇̝̘̟̬̜̰̬̟̯̗̻̂̃͒̂̏̿̅̊̒̃̔́̀̆̀̎͗̊̈́̀̇́̕ͅͅi̸̢̛̖̫͚̼̞̽̓͂̈́̆̓̇̔̈́̓͋͌́̐̚͘̚̕͜͝͝͝l̴̛̩͓̫̥̲̠̗̝͙͍̪͍̳̗̪̤͉̭̭̮̻̇̃͐̈́̆͆͐̃͆͆̈́͑̔̀̒̂͊̄̾̆̿̕͜͝ͅţ̴̡̧̛͔̟̯̣̪̟̠͔̩̙̹̝̣͚͕̓́̍r̶̗̭̒̔͐̂̅̈́͊̈́̎́̔̋̉̐̑̈́͒͌͜a̷̡̬̲͕̪̻̤̳̤̙̬̘͚͇̳̙̣̳̦̾̀̆̓̏̃̀͛̀̓̓́͋̉́̓̕͘̕͜͝͝t̷̢̛̥̳̽͑͂̑͋̔̓̆̓̈́̊̏͒e̸̢̫̘͓͙̼̭̪͔͙͍̝̥͖͓͎͖͇̙̻͆͛̔̉̒͆̆̽̌̄̒̚͘͜͜͜͠͝ ̷̨̨̮̼̮̼̥͉̼̫̳̻̺̫͚̖̣̯̘̠̠̖͈̽̃̐͛͆̀̏̓̾̈́̀́͠͝ͅț̶̡̧̛̠͎̥̉͊̿̃̔̔͗̀̀́̈́͂̅̂̕͠h̷̝͒̅ȩ̷̛̟͔͍̳̝̗̪͍̱͕̖͉̺͎̗͈̇̂̀͆̌̈́̀͋̔̔̅̿̌̕͝ ̸̼̹̹̻͉̱̭͈̥̟͚̼͕̹͙̱͔̣̓͋̊͊̉͊̉̏̇̇͐̑̈̀̔̋̌̂̂̅́͜͜͜͝ṟ̷̨̛͈̳̣͕̣̱͙̬̬͙͔͓̲̯̖̤͍͆̄̉̒͗o̵͔͕͙̘̙̾ǒ̴̪̝͐͆͆̓͆̓́̃́̄̐͑͘̚͝m̵͚̯͍͎̠̞̲͍̻̥̱̗̘̞̮̠͈̖̣͓̫̹͎͇͂̍̅̑̍̎̐̅̈́̚ ̶̢̲̩͈͖̪̬̮̦̞̬͉͔͚͂̌̈́̎͋̉̒̈́͜͝ẅ̸̧̗̞̘̙̤̰̠͍̼͎̥́̊̏͆̈́͑͗̄̓̑̚̚͜͝͝͝ḫ̶̨̢̪̻̜̩̝̞͖̣̬͎̜̾̉̒e̸̪̙͉̼͉̙̘͕̳̻̘̯̯͛̋̄́̈́͆̍̂̓̈̕̚͝ŗ̷̢̢̛͎̥͕̙̜̯̝̟̙̝̰̻̭̤͉͔̪̖͎̣̮̼̜̿̍̈́̔͐̓̉̅́͛̎̏͠ȇ̴̱͉͕̰̣̪͔̬̦͈̗̦͙̔͛͜ͅ ̶͚̣̦͔̣͇͔͕̣͉͙͙̠̯͇̀̈́̐̃͋͆̉̑́̈̄͘̚c̸͍͉̤̝̤̹̞͔͇̣̬̳͔̪͙͓̑ͅͅḩ̸͉̝̘̹̞̳̟̖̤͈̙̳͙͕͙̹̙͇̭̗̬̿̈́͑͛͂̔̋͊͌͘͝a̶̧͚͖̦̦̯̫̭̳͉̺̥̥͙̱͙̹͚͓͓̮̲̾̈́̃̑̓͌̍̈́̐̉̊͆̊̂̇͑͠͝ͅņ̷̧̛͍̝̬̞̲̟̮̦̮̫͚͕̜̘͓̏͗̌̓͒̃͌͐̕̕͝ͅģ̷̛͚̩͇̙̥̼̼͓̼̙͕͔͔̬̗̬̦͔͖̯͕͇͑͑̀̾̈́̇̽͗̚͜ė̷̢̛͚̖͖̹͕͖̙̅̌͌̔̏͂̓̐̓̍̄̊̌̓̐̔̕ͅs̴͖̀̏̊̊́͛̈́̄̈̎̂̋̈́͛̊̈̌̏̈́̎͝͝ ̴͉̞̺̖̲͉̬̻̟̤̲̻̱̮͍͚͕̗̖̰̥͋͆͒ͅơ̶̹͓͍͇̭̹̩̲̝̟̗̺̮͎̖̻̟̅̂̉̑͂̂̀͌̄̽̿͌̚̕͝ç̷̢̢̨͓͓̭͙̠̙̪͗̾̽̀͗̌͆͂͝c̴̢̰̳̫͎̬͎̤̲̩̟̻͔̩̳̰̀̄̄͗̎͑͂̀̀̈́́̚͜ư̸̢͉͙̤̖̩͇̼̫̍̓̈́̓͛̃̓̋͋̚̕̕͝͠ͅr̸͍̲͑̂̏͌̄.̷̅̂̽̾ \n \n \n \n \n') 
            
            
            
            
            
            print('The list is too worn to read')
            
        elif userAction.lower() == 'look at polaroid':
            print('You see him, the image has appeared, the Detivus at full might stares blankly into your eyes. Hope escapes you in this moment as the picture of the Detivus overwhelmes all thought.')
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            cafe()
        
        else:
            userAction = raw_input('Can\'t do that.')
            
def biosphere():
    global enteredRooms
    global openedDoors
    global playerItems
    exitRoom = False
    print('You entered the biosphere, trees and lush bombard you, and the scent of flowers penetrate your nose.')
    print('Through the clearing you encounter that the only way out is the way in, back east(hangar)')      
    print('Light flickers from a distance, should you follow, danger awaits.')
    if 'biosphere' in enteredRooms:
        print('the birds sing upon your return')
    else:
        enteredRooms += ['biosphere']
    
    while exitRoom == False:
        userAction = raw_input('> ')
        
        if userAction.lower() == 'go west':
            exitRoom = True
        
        elif userAction.lower() == 'follow light':
            print('You have reached a clearing, wildlife circles around you in almost a satanic way, what appears in front of you is a great unused candle, the light is flickering from above')
            
        elif userAction.lower() == 'light candle' and lightCandle == False:
            print('You need a lighter')
            
        elif userAction.lower() == 'light candle' and lightCandle == True:
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
        
            
            

        
            