import os
from numpy import random
myinput = input('Random problems or select problems (1 or 2)')
def tellproblem(problemnumber):
  print('Your problem number is ' + str(problemnumber))
# Check which random problem it is
'''
Code that needs to be edited starts here:
'''
def check():
  os.system('clear')
  randomproblem = random.randint(6)
  tellproblem(randomproblem)
  if randomproblem == 0:
    print('print("Hello World!")')
    ifequals('Hello World!')
  if randomproblem == 1:
    print('22 + (10 + 20)')
    ifequals('52')
  if randomproblem == 2:
    print('9 ** (2)')
    ifequals('27.0')
  if randomproblem == 3:
    print('Taken from sololearn, thanks, sololearn')
    print('1.25 % 0.5')
    ifequals('0.25')
  if randomproblem == 4:
    print('Taken from sololearn, thanks, sololearn')
    print('Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!\nHow do you prevent an error from happening? (what do you add next the quotes?)')
    ifequals('Sorry this problem is kind of broken, you add a backward slash')
  if randomproblem == 5:
    print('input("")\nDoes this wait for input or find input (1/2)')
    ifequals('1')
'''
Ends here
'''
# Check if equals to correct answer
def ifequals(answer):
  ask = input('Enter your answer:')
  if ask == answer:
    print('Correct!')
    print('The answer was %s' % (answer))
    wait = input('Press enter to continue')
    check()
  else:
    print('Wrong')
    print('The answer was %s' % (answer))
    wait = input('Press enter to continue')
    check()
if myinput == '1':
  check()
elif myinput == '2':
  print('Currently unavailable :(')
  pass
else:
  try:
    int(myinput)
    print('Your answer should be either 1 or 2\nTry again!')
  except:
    print('Your answer is not a number...\ntTry again!')
