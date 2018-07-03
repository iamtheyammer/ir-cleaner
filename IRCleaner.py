## IR Cleaner Python Script
## By GitHub @iamtheyammer
## Licensed under GNU GPLv3
## https://github.com/iamtheyammer/ir-cleaner

## Just run this script, paste in your dirty IR codes and let this clean them for you!
## Under the hood, this script is just rounding numbers to the nearest hundred, and arraying them for you.
## Enjoy!

import math

## OUTPUT VARIABLE

## 0) Unformatted list (array). Example: [34534700, 64600, 100, 400, 100, 0, 0, 547200]

## 1) Arduino: this will format it for use with an arduino, starting with unsigned int cleanedIR[] = { and ending with a closed curly brace and a semicolon. Example: unsigned int cleanedIR[] = {100,5600,0,346500,0,0,100,700,563500,57500};

## 2) LIRC (linux infrared remote control): For use with LIRC on any linux machine, like a raspberry pi. Assumes that a number like -1242 is a space and that a number like 1242 is a pulse. (if you don't know what that last sentence means, don't worry about it!)

output = 2

## Now, onto the code:
# Begin definitions

def roundUp(x):
  return int(math.ceil(x / 100.0)) * 100

def roundDown(x):
  return int(math.floor(x / 100.0)) * 100

def round(x):
  x = abs(x) # remove the negativeness, if it exists by using absolute value 
  if int(str(x)[-2:]) < 50: # choose whether to round up or down based on whether the number is below 50
    return roundDown(x)
  else:
    return roundUp(x)

def listToString(list):
   string = ','.join(str(e) for e in list)
   return string

# End definitons; begin main code block, output agnostic

if output == 0: # display the output format when running
  toClean = input('What is the IR string to clean? Paste it in, comma seperated. [Output format: Not formatted]\n')
elif output == 1:
  toClean = input('What is the IR string to clean? Paste it in, comma seperated. [Output format: Arduino]\n')
elif output == 2:
  toClean = input('What is the IR string to clean? Paste it in, comma seperated. [Output format: LIRC]\n')
else:
  raise Exception('[FATAL] Your output variable is set to an invalid value. Please set it to 0, 1 or 2.')


if toClean[-1:] == ',': # check user unput
  print('[WARN] Your input ends with a comma. Please avoid this in the future.')
  toClean = toClean[:-1] # remove that ending comma
elif toClean[-1:].isdigit() == False or toClean[:1].isdigit() == False:
  raise Exception('[FATAL] Your string does not start/end with a number.')

toClean = toClean.split(',') # turn the text input to an array (python says a dictionary or list)

cleaned = []

for i in range(0, len(toClean)): # this for loop does the work of taking the dirty data and cleaning it
  if toClean[i][-2:] == '00': # if the number ends in 00 it's already a multiple of a hundred
    continue
  cleaned.append(round(int(toClean[i])))

# End main code block; starting the customised output

if output == 0: # basically just print the array
  print('\nOutput (not formatted):\n\n' + str(cleaned) + '\n\n\n')
elif output == 1: # print the array surrounded in static text, for arduino
  print('')
  print('\nOutput (formatted for Arduino):\n\nunsigned int cleanedIR[] = {' + listToString(cleaned) + '}; // cleaned ir signal by https://github.com/iamtheyammer/ir-cleaner\n\n\n')
elif output == 2: # alternate between space and pulse
  print('\nOutput (formatted for LIRC):\n\n')
  final = '' # init the final string
  if int(toClean[0]) < 0: # check if we should start with a space or pulse by seeing if the first number was negative
    counter = 1
  else:
    counter = 0
  for i in range(0, len(cleaned)): # for the length of the cleaned data, concatenate it
    if counter == 0: 
      final += 'space ' + str(cleaned[i]) + '\n'
      counter += 1
    elif counter == 1:
      final += 'pulse ' + str(cleaned[i]) + '\n'
      counter = 0
  print(final)

# End output
