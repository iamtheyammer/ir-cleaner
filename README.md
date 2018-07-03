# ir-cleaner
A simple python script to clean IR codes so that they work better. Basically, it just rounds your numbers and formats them.

With some effort and help from @AnalysIR, I realised that the codes I was getting from my Arduino weren't working because they weren't cleaned. @AnalysIR cleaned them for me, and this script does that same cleaning process. (after the cleaning, my air conditioner turned on and off at the Uno's command!)

Every time I plan on using raw IR codes, I will definitely clean them and I reccommend you do too.

## Install/Usage
0. Capture a raw IR code. For most devices, I'd try [this](https://github.com/z3t0/Arduino-IRremote/blob/master/examples/IRrecvDumpV2/IRrecvDumpV2.ino) script, from the [IRLib/Arduino-IRremote library](https://github.com/z3t0/Arduino-IRremote), and using the hex code (starts with `0x`) from it (effectively skipping the use of this tool). The hex codes don't always work, and if they don't I'd reccomend you try the following air conditioner instructions. If you're trying to control an air conditoner or something odd, use [this](https://www.analysir.com/blog/wp-content/uploads/2014/03/Arduino_Record_Long_AirConditioner_Infrared_Signals_10.txt) script on an arduino (seems to only work on an Uno), and that's where this tool really comes in handy. If you're using the script in the previous sentence, and you've got some data, let's clean it!
1. Download the script. There's a little clone/download button on the homepage for this repository, so click that and download ZIP.
2. Open the script in a text editor and set the output variable as follows:
  - 0) Unformatted list (array). Example: [34534700, 64600, 100, 400, 100, 0, 0, 547200]
  - 1) Arduino: this will format it for use with an arduino, starting with unsigned int cleanedIR[] = { and ending with a closed curly brace and a semicolon. Example: unsigned int cleanedIR[] = {100,5600,0,346500,0,0,100,700,563500,57500};
  - 2) LIRC (linux infrared remote control): For use with LIRC on any linux machine, like a raspberry pi. Assumes that a number like -1242 is a space and that a number like 1242 is a pulse. (if you don't know what that last sentence means, don't worry about it!)
3. Run the script, in pretty much any python compiler. (Open, then F5 in IDLE, or on a mac `python3 ./IRCleaner.py`)
4. Enjoy your cleaned code!

## Issues or questions?
Open an issue on this repository, and maybe (just maybe!) tag @AnalysIR in said issue.

## Protocol Support
If you've got another protocol that you'd like custom output for, either code it in yourself and open a pull request or open an issue and maybe I'll add it. No guarantees on that though.


## Credits

Thank you to @AnalysIR for demonstrating the effect cleaning IR signals can do and their help solving [my issue](https://github.com/z3t0/Arduino-IRremote/issues/579) when trying to control my air conditioner.

I wrote this script, though.