#########################
## Auto Cannibal Maker ##
##                     ##
## Name: achaturv      ##
#########################
import sys
def ACM(eat):
    a = [eat+'\n',"def ac():", "\tEat(\"a = \"+repr(a)+\"\\n\"+a[0]+\"\\n\"+a[1]+\"\\n\"+a[2]+\"\\n\"+a[3]+\"\\n\\n\")", "ac()"]
    acm = "a = " + repr(a) + "\n" + a[0] + "\n" + a[1] + "\n" + a[2] + "\n" + a[3] + "\n"
    print acm

program = sys.stdin.read()
ACM(program)
