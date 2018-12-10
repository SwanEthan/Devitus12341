def command_control():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    deskItems = ['the launch codes']
    print('You have entered Command Control')
    print('There are no other doors in this room')
    print('There is also a desk with a stack of papers in the center of the room.')
    userAction = raw_input('>')
    while exitRoom == False:
        if userAction == 'look around':
            print('You see some papers on the desk.')
	    print('Maybe it has the rocket launch codes.')
	    userAction = raw_input('What would you like to do now? ')
        elif userAction == 'look at papers':
            print('You shuffle the papers to see the launch codes.')
	    userAction = raw_input('What would you like to do now? ')
        elif userAction == 'grab launch codes':
            print('You picked up', deskItems, 'you can use them to escape with the rocket in the hangar')
            playerItems += deskItems
            deskItems = []
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'go east':
            print('There is a wall here.')
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'go north':
            print('There is a wall here.')
            userAction = raw_input('What would you like to do now? ')
	elif userAction == 'go south':
	    print('There is a wall here.')
	    userAction = raw_input('What would you like to do now? ')
	elif userAction == 'go east':
	    exitRoom = True
	    #defbridge()
        else:
            userAction = raw_input('Not a valid action.  Try Again! ')