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
  randomproblem = random.randint(28)
  tellproblem(randomproblem)
  if randomproblem == 0:
    print('print("Hello World!")')
    ifequals('Hello World!')
  if randomproblem == 1:
    print('22 + (10 + 20)')
    ifequals('52')
  if randomproblem == 2:
    print('9 ** (2)')
    ifequals('81.0')
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
  if randomproblem == 6:
    print('"1" + "3"')
    ifequals('13')
  if randomproblem == 7:
    print('"1" * 3')
    ifequals('111')
  if randomproblem == 8:
    print('float("10")')
    ifequals('10')
  if randomproblem == 9:
    print('type(10j)')
    ifequals('complex')
  if randomproblem == 10:
    print('x = 10\nprint(x)')
    ifequals('10')
  if randomproblem == 11:
    print('x = 15\nx *= 10')
    ifequals('150')
  if randomproblem == 12:
    print('2 == 3')
    ifequals('False')
  if randomproblem == 13:
    print('1 != 1')
    ifequals('False')
  if randomproblem == 14:
    print('if 1 >= 1:\n print("Hello")\nprint("Done")\nDoes it print Hello and Done or only Hello or Only Done (1/3)')
    ifequals('1')
  if randomproblem == 15:
    print('myvar = 100\nothervar = myvar * 10\nif othervar < myvar:\n print("")')
  if randomproblem == 16:
    print('x = 10\nif x > 11:\n print("higher")\nelif x == 10:\n print("elif")\nelse:\n print("else")')
    ifequals('elif')
  if randomproblem == 17:
    print('1 == 2 or 112183 == 112183')
    ifequals('True')
  if randomproblem == 18:
    print('False == (False or True)')
    ifequals('False')
  if randomproblem == 19:
    print('i = 2\n while i > 1:\n i = i - 1\n print(i)')
    ifequals('1')
  if randomproblem == 20:
    print('x = 3\nwhile x > 1\n x = x - 1\n if x == 2:\n  print("Done")\n  break')
    ifequals('Done')
  if randomproblem == 21:
    print('x = 2\nwhile x > 1:\n x = x - 1\n if x = 1:\n  continue\n  if x < 2:\n   print("Done!"')
    ifequals('')
  if randomproblem == 22:
    print('numbers = [1, 2, 3]\nprint(numbers[1])')
    ifequals('2')
  if randomproblem == 23:
    print('mylist = []\nprint(mylist)')
    ifequals('[]')
  if randomproblem == 24:
    print('string = "Hello World!"\nprint(string[1])')
    ifequals('e')
  if randomproblem == 25:
    print('mylist = [1, 2, 3]\nmylist[1] = "2"\nprint(mylist)')
    ifequals('[1, 2, 3]')
  if randomproblem == 26:
    print('mylist = [1, 2, 3]\nprint(num + [4, 5, 6])')
    ifequals('1, 2, 3, 4, 5, 6')
  if randomproblem == 27:
    print('words = ["hello", "?", "hi"]\nprint("hello" in words)')
    ifequals('True')
  if randomproblem == 27:
    print('mynumbers = [4, 6, 2, 1]\nprint(not 2 in mynumbers)')
    ifequals('False')
  if randomproblem == 28:
    print('mynumbers = [4, 2, 5, 6]\nmynumbers.append(8)\nprint(mynumbers)')
    ifequals('[4, 2, 5, 6, 8]')
  if randomproblem == 29:
    print('nums = [1, 2, 3, 4, 4]\nprint(len(num))')
    ifequals('5')
  if randomproblem == 30:
    print('words = ["Python", "is"]\nwords.insert(2, "good")\nprint(words)')
    ifequals('["Python", "is", "good"]')
  if randomproblem == 31:
    print('greet = ["hi", "hello", "good morning"]\nprint(greet.index("hi"))')
    ifequals('0')
  if randomproblem == 32:
    print('mylist = [1, 60, 2, 50, 74, 52, 100, 10]\nprint(max(mylist))')
    ifequals('100')
  if randomproblem == 33:
    print('mylist = [1, 2, 3, 4, 5, 6]\nprint(min(mylist))\nprint(max(mylist))\nmylist = [1, 1, 2, 3, 4, 6]\nprint(mylist.count(1))\nmylist = [1, 1, 2, 2]\nmylist.remove(1)\nprint(mylist)\nmylist.reverse()\nprint(mylist)')
    ifequals('1, 6, 2, [1, 2, 2], [2, 2, 1]')
  if randomproblem == 34:
    print('numbers = list[range(4)]\nprint(numbers)')
    ifequals('[0, 1, 2, 3]')
  if randomproblem == 35:
    print('numbers = list(range(1, 5))\nprint(numbers)')
    ifequals('1, 2, 3 ,4')
  if randomproblem == 36:
    print('numbers = list(range(1, 11, 2))\nprint(numbers)')
    ifequals('[1, 3, 5, 7, 9]')
  if randomproblem == 37:
    print('x = 2\nwhile: x < 4: \n x = x + 1\n print(x)')
    ifequals('3')
  if randomproblem == 38:
    print('mylist = ["Hello", "World", "!"]\nfor iterate in mylist:\n print(mylist[iterate])')
    ifequals('HelloWorld!')
  if randomproblem == 39:
    print('')
    ifequals('')
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
