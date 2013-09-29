CFLAGS =
CC = python

Check : Self.py Eater.py
	/bin/rm -f Self.out
	/bin/rm -f Eat.out
	python Self.py > Self.out
	python Eater.py < Self.py > Eat.out
	if cmp Self.out Eat.out; then echo;echo;echo 'Looks good!';echo;echo; else \
	echo;echo;echo 'Uh oh! Better try again!'; echo;echo; fi

Self.py : Eat.py ACM.py
	/bin/rm -f Self.py
	python ACM.py < Eat.py > Self.py
	python Self.py -o Self

clean :
	/bin/rm -f core Self.py Self.out Eat.out *.pyc
