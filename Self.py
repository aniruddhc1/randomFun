a = ['#15-251\n#Simple Eat function that just prints out\n#its argument.  Very good for debugging!\n\nimport string\n\ndef Eat(Self):\n    print len(Self)\n\n', 'def ac():', '\tEat("a = "+repr(a)+"\\n"+a[0]+"\\n"+a[1]+"\\n"+a[2]+"\\n"+a[3]+"\\n\\n")', 'ac()']
#15-251
#Simple Eat function that just prints out
#its argument.  Very good for debugging!

import string

def Eat(Self):
    print len(Self)


def ac():
	Eat("a = "+repr(a)+"\n"+a[0]+"\n"+a[1]+"\n"+a[2]+"\n"+a[3]+"\n\n")
ac()

