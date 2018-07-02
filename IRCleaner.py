## IR Cleaner Python Script
## By GitHub @iamtheyammer
## Licensed under GNU GPLv3
## https://github.com/iamtheyammer/ir-cleaner

## Just run this script, paste in your dirty IR codes and let this clean them for you!
## Under the hood, this script is just rounding numbers to the nearest hundred, and arraying them for you.
## Enjoy!

import math

def roundUp(x):
  return int(math.ceil(x / 100.0)) * 100

def roundDown(x):
  return int(math.floor(x / 100.0)) * 100

def round(x):
  x = abs(x)
  if int(str(x)[-2:]) < 50:
    return roundDown(x)
  else:
    return roundUp(x)

def listToString(list):
  return string = ''.join(str(e) for e in list)

toClean = input('What is the IR string to clean? Paste it in, comma seperated.')
toClean = toClean.split(',')
#print(toClean)

cleaned = []
for i in range(0, len(toClean)):
  cleaned.append(round(int(toClean[i])))

print(cleaned);
