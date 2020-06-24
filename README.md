#This is a simple number guessing game in python. With configurable settings.
I have made it give options(play, change settings, or quit), repeating until a valid option is given.
I have added the ability to change the range and max guesses allowed
I have exception handling to ensure expected int inputs to be valid integers. Only other input would be user name, which can be any valid input.
I have added the interpreter line and set the file permissions to executable

Plans: Exception catching from termination/interrupt signals (how would a graceful ctrl+c exit work, instead of a python error message)
The only other thing I would add to this would be further checking of out of range guesses, and penalties for repeated invalid guesses.
