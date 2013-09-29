#15-251
#
# Simple driver for the Eat function. Reads a program from the
# standard in, and then calls Eat on the program.
# 
# You SHOULD not modify this file.

import sys
from Eat import Eat

program = sys.stdin.read()
Eat(program)
