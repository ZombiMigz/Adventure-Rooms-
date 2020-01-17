


#player framework
class player:
    def __init__(self):
        pass

player = player()
player.maxhealth = 100
player.health = 100

#startup
def startup():
    import framework
    import main
    framework.printunknown("Hello, what's your name?")
    framework.guide('Type your name, then hit ENTER')
    player.name = input('')
    framework.printunknown("Hi " + player.name + ".")
    framework.console('Player name set to ' + player.name)

#class selection
def classSelection():
    framework.printunknown("Please pick a class")
    while True:
        print('<<MAGE>> <<BESERKER>> <<KNIGHT>> <<ARCHER>>')
        player.playerClass = input('')
        if player.playerClass == ("MAGE" or "BESERKER" or "KNIGHT" or "ARCHER"):
            print("Are you sure you want to be a " + player.playerClass + "?")
            if input('') == 'y':
                framework.console("class set to " + player.playerClass)
                framework.printunknown("Ok! You are now a " + player.playerClass)
                break
            if input('') == 'n':
                framework.printclear('')
                continue
            else:
                print("I'm sorry, I didn't understand.")
                framework.guide('Type the character y or n, then hit enter.')
