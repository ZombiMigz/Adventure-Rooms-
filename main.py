#load framework
import framework
framework.console('Functions Loaded')

#gamestartup
import startup




#game
def start():
  framework.output('You meet a villager from a nearby town. He begs you to help him fight off a vampire that is terrorizing his village. Do you accept?','')
  if framework.answer() == True:
    Vampire()
  else:
    Parasite()

def Vampire ():
  framework.output('You walk with the villager to his town. In the town square, you see  the dark shadow of a vampire.','On the ground you see a large sword. Do you pick up the sword?')
  if framework.answer() == True:
    Sword()
  else:
    Shield()
def Parasite ():
  framework.output('You keep walking. In the trees you hear a parasite crawling towards  you.','You are trying to put on your armor when you see a sword lying on the ground. Do you pick up the sword?')
  if framework.answer() == True:
    Sword2()
  else:
    Armor()
    
def Sword ():
  framework.output ('You weild the mighty sword in your hands, ready to fight the vampire.','The vampire runs at you. Do you attack?')
  if framework.answer() == True:
    Attack()
  else:
    Dodge()
def Shield ():
  framework.output ('You pull out your shield, fearing the worst.','Do you stand and wait for the inevitable?')
  if framework.answer() == True:
    Continue()
  else:
    PutDown()
def Sword2():
  framework.output("You grab the sword, feeling it's power. Meanwhile, the parasite has infected a large dog.", 'Do you fight the dog?')
  if framework.answer() == True:
    Fight()
  else:
    Ignore()
def Armor():
  framework.output('You quickly put on the armor and you realize "Hey, I can get the     sword too." so you grab the sword also. You then proceed to rid the  world of the parasite forever','')
  framework.Win()

def Attack ():
  framework.output ('You swing madly with the sword','You miss horribly and the vampire ends your life.')
  framework.Lost()
def Dodge ():
  framework.output ('sword','attack or dodge')
  framework.Lost()
def Continue ():
  framework.output ('You hold the shield in fright as the vampire approaches. The second  he touches it, he dies inexplicably.','The garlic bread you lost 3 weeks ago had been stuck to your shield. How lucky.')
  framework.Win()
def PutDown ():
  framework.output ('You try to run away, dropping your shield. The vampire appears behind you and you become his dinner.','')
  framework.Lost()
def Fight():
  framework.output('You fight the dog desperately, but after awhile you give up. You put your shield down and find dog treats. You throw the dog treats across the Earth and the dog chases after it. You fight the parasite and kill it. You win, but you forgot about the dog and after 2 years later, it infected the whole world.','You failure.')
  framework.Lost()
def Ignore():
  framework.output('You decide to kill the parasite first, then deal with the dog.', 'Good job! The world is safe again.')
start()
