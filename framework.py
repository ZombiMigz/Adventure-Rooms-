#print functions
def asterisk(output):
    print('*' + output + '*')
def printclear(output):
    print(output)
def printunknown(output):
    print('[???]: ' + output)
def console(output):
  print('[Console]: ' + output)
def guide(output):
  print('[Guide]: ' + output)
def clear():
  i = 0
  while i < 30:
      print ('\n')
      i += 1 

def answer():
  choice = input('**************************************\n type: y/n\n')
  if choice == 'y':
    return True
  else:
    return False

def ask(option1,option2):
  if answer() == True:
    option1
  else:
    option2

def output(result,choice):
  print ('**************************************\n' + result + '\n')
  print ('**************************************\n' + choice)

def Lost():
  print('YOU LOST')
def Win():
  print('YOU WIN')



#output (temporary)
def room():
  output('You meet a villager from a nearby town. He begs you to help him fight off a vampire that is terrorizing his village. Do you accept?','')
  if framework.answer() == True:
    Vampire()
  else:
    Parasite()






















    