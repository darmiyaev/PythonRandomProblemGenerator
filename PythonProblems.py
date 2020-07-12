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
  randomproblem = random.randint(2)
  print(randomproblem)
  if randomproblem == 0:
    tellproblem(randomproblem)
    print('print("Hello World!")')
    ifequals('Hello World!')
  if randomproblem == 1:
    tellproblem(randomproblem)
    print('22 + (10 + 20)')
    ifequals('52')
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
