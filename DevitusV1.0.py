# -*- coding: utf-8 -*-
from __future__ import print_function
#import random



litCandles = []
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
    global litCandles
    exitRoom = False
    if hangar not in enteredRooms:
        print('\nThe hangar is barren. There\'s not a soul in sight.')
        print('\nThere are four doors in this room.  One to the north(cafe), one to the east(bridge),')
        print('\none to the south(boiler room), and one to the west(bioshpere).')
        print('\nThere is a rocket ship behind where you\'re standing, but it doesn\'t seem to be functional at the moment.')
    else:
        print('Back in the hangar. The rocket hasn\'t left without you.')
    
    while exitRoom == False:
        userAction = raw_input('> ')
        if userAction.lower() == 'look rocket':
            print('The rocket is innactive. Needs launch codes.') 
                       
        elif userAction.lower() == 'look around':
            print('The hangar is entirely abandoned besides you and the rocket.')
            
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
        userAction = raw_input('> ')
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
            
        elif userAction.lower() == 'take lighter':
            print('\nYou pick up the old grill lighter and give is a test click. It still works.')
            playerItems += 'lighter'
            
        elif userAction.lower() == 'take bread' or userAction.lower() == 'take corn bread':
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
            #storage()
            
        else:
            print('Can\'t do that.')    
    
            
def bridge():
    global enteredRooms
    global litCandles
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
            #rocket()            
            
        elif userAction.lower() == 'enter rocket' and rocketOn == False:
            print('You can\'t enter the rocket without the launch codes.')
            
            
        elif userAction.lower() == 'go north':
            print('\nYou went north until you hit a huge wall. Which was only a few meters away, so you\'re still in the bridge.')
            
        elif userAction.lower() == 'go south':
            exitRoom = True
            #lockers()
            
            
        elif userAction.lower() == 'go east':
            exitRoom = True
            bridge()
            
        elif userAction.lower() == 'go west':
            exitRoom = True
            hangar()
            
        else:
            print('Can\'t do that.')
#def rocket():


def library():
    global enteredRooms
    global playerItems
    global openedDoors
    global litCandles
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
        userAction = raw_input('> ')
        if userAction.lower() == 'read book':
            print("The Great War of The Internet Age” stands boldly at the top of the book. It was the date, December 2nd, 2018. T-Series the infamous Indian record company was remarkably close to passing Pewdiepie and becoming theNumber one most subscribed account on the YouTube platform. The 9 year olds were waging the good fight but it wasn’t enough, the gap was closing, and it was an only a matter of hours before the war was lost. It seemed all hope was lost, Mr. Beast had failed, Pewds best friends Jack and Mark had abandoned him. The 9-year-olds regrouped and revitalized their attack strategy. They came out the door swinging gaining a couple thousand subscribers but it wasn’t enough, T-Series was catching up and fast. Greyness loomed over the heads of the 9-year-olds, it seemed that finally that their king would be dethroned, but a miracle happened! Markiplier, Boogie2988, and Jacksepticeye had joined the fight, swinging the tide of battle, the war was not lost, reinforcements had come through this was a major turning point. Markiplier had posted a livestream of him continually talking and not shutting up ever until people subscribed to pewdiepie, and from there the 9-year-olds were off the the races. Jack tweeted a simple but direct poem encouraging his fans, and Davie504 played the Felix’s most hottest song, the T-Series disstrack for 10 hours straight, all collaborations of efforts were pulling through and pewdiepie had regained a comfortable subscriber lead. He ended up pulling 544k subscribers on december 2nd, a very important day in the war of Pewdiepie v. T-Series. Pewds had won this great battle but the war was still not over. Subscribe to Pewdiepie to make a difference again. \n*This is not related to the game*")
        
        elif userAction.lower() == 'look around':
            print('The bookshelves seem to go up forever.')
            
        elif userAction.lower() == 'go to desk' or userAction.lower() == 'look desk':
            if dvHist:
                if raw_input('Do you want to read about the Devitus again? Y/N\n> ').lower() == 'y':
                    print('\nThere is a note, "According to the legend, the Devitus that roams this abandoned base can be summoned and excorcised."')
                    print('\nYou turn the note around, there is a smudged list') 
                    print('\nStep 1: Summoning the Devitus requires three(3) open flames. Candles will do. Gather and light these.')
                    print('\nStep 2: Bring the candles to the location of the death of the demon\'s body.') 
                    print('\nStep 3: To complete the ritual, one must perform a "T-Pose" to assert dominance over spirit.')
                    print('This act will force it out of hiding.')           
                    print('\nStep 4: To exorcise the Devitus, must say an incantation in its presence. This i..-.')
                    print('\nThe rest of the note is smudged beyond legibility.')
                    print('A small candle is taped to the bottom of the page.')
            else:
                print('\nThere is a note, "According to the legend, the Devitus that roams this abandoned base can be summoned and excorcised."')
                print('"[STORY EXPLANATION]"')
                print('\nYou turn the note around, there is a smudged list')      
                    
                    
                    
                    
                print('\nStep 1: Summoning the Devitus requires three(3) open flames. Candles will do. Gather and light these.')
                print('\nStep 2: Bring the candles to the location of the death of the demon\'s body.') 
                print('\nStep 3: To complete the ritual, one must perform a "T-Pose" to assert dominance over spirit.')
                print('This act will force it out of hiding.')           
                print('\nStep 4: To exorcise the Devitus, must say an incantation in its presence. This i..-.')
                print('\nThe rest of the note is smudged beyond legibility.')
                dvHist = True
        elif userAction.lower() == 'look polaroid':
            print('\nYou see him. The Detivus at full might stares blankly into your eyes. Hope escapes you in this moment as the picture of the Detivus overwhelmes all thought.')
            print('\nYou quickly put the picture down before you get too caught up.')
        
        elif userAction.lower() == 'take candle':
            print('\nYou took the candle.')
            playerItems += 'smallCandle'
        
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
        userAction = raw_input('> ')
        
        if userAction.lower() == 'go west':
            exitRoom = True
            hangar()
        
        elif userAction.lower() == 'follow light':
            print('You have reached a clearing, wildlife circles around you in almost a satanic way, what appears in front of you is a great unused candle, the light is flickering from above')
        
        elif userAction.lower() == 'take candle':
            print('You grab the candle and shake some mulch off it.')    
            playerItems += 'bioCandle'
            
        elif userAction.lower() == 'light candle' and "lighter" not in playerItems:
            print('You need a lighter')
            
        elif userAction.lower() == 'light candle' and 'lighter' in playerItems:
            print('The candle is now lit')
            
        elif userAction.lower() == 'light candle' and 'lighter' in playerItems and 'bioCandle' in litCandles:
            print('The candle is already lit')
            
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
    #roomItems = ['', 'candle']
    print('\nIt\'s warm and dry in here. Smells like a swimming pool if it was recently boiled. Yup, this is the boiler room.')
    print('\nThe only door in this room is the way you came in(north).')
    print('\nThere\'s some kind of candle down in the corner, and you can see a metallic glint under the boiler.')
    
    while exitRoom == False:
       userAction = raw_input('> ')
       
       if userAction.lower() == 'look around':
           print('It\'s a confined space. The green glow of LED status lights from the boiler units are all that light this room.')
           
       elif userAction.lower() == 'look boiler' or userAction.lower() == 'look under boiler':
            print('You spy a single key tucked under the cast metal boiler.')
            
       elif userAction.lower() == 'take key':
            print('You took the key.')
            playerItems += 'secretKey' 
       
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
                   
                          
                                 
                                        
                                               
                                                      
                                                                    