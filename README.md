# Python-Stuff
## Copy Master
Copy Master is a simple graphical interface program to copy files and directories
from *source* to *destiny* locally. This version is meant to be executed on a computer
that runs with a Windows 10 OS. User may specify the *source* and *destiny* directory.

***
## Copy Master Linux
Copy Master is a simple graphical interface program to copy files and directories
from *source* to *destiny* locally. This version is meant to be executed on a computer
that runs with any Linux distro. User may specify the *source* and *destiny* directory.

***
## dec_bin
This is a program that can convert a 10-based number (*decimal system*) into a 2-based number
(*binary system*) and viceversa. Therefore, this program has a menu that stands the following
options:

1. Convert from decimal to a binary number
2. Convert from binary to a decimal number

### Converting from decimal to a binary
To convert from decimal to binary I use the successive divission by two method. Also, the program
is able to convert a float decimal number using the successive multiplication by two method for the
decimal part - *after the decimal point* -.

### Converting from binary to decimal
In order to be able to convert a binary number into its decimal equivalent, first thing I do 
is validating the user's input to check if the binary number has only 0's and 1's. I achieve this
by using the search() method from the *re* module. Finally, the converting method that I use is the sum weights' method
