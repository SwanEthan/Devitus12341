def boiler():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    roomItems = ['key2', 'candle']
    print('You have entered the foyer')
    print('There is one door in this room. It is on the south wall.')
    print('There is also an unlit candle in this room.')
    print('You see a metallic glint under the boiler')
    userAction = raw_input('>')
    while exitRoom == False:
        if userAction == 'go south':
            print('There is a door here')
            openedDoors += ['door1']
            exitRoom = True
        elif userAction == 'light candle' and 'lighter' in playerItems:
            print('You lit the candle.')
        elif userAction == 'grab keys':
            print
        elif userAction == 'grab keys':
            print('You picked up', roomItems)
            playerItems += roomItems
            roomItems = []
