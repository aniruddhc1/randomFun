def makeChange(total):
	coins = [2,5,10]
	amount = [0] * (total+1)
	amount[0] = 0

	for i in xrange(1, total+1):
		amount[i] = 99999
		temp = 99999

		for coin in coins:
			if(coin <= i):
				tempAmt = 1 + amount[i - coin]
				if(tempAmt < temp):
					temp = tempAmt
					amount[i] = temp
	print "change for amount ", total, " is : ", amount[total]
	return

print makeChange(10000)
print makeChange(2)
print makeChange(6)
print makeChange(8)
print makeChange(9)
print makeChange(13)
print makeChange(18)
print makeChange(21)
print makeChange(4)
print makeChange(10)


# def test():
# 	for i in xrange(1, 5+1):
# 		print i

# print test()