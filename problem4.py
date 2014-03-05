def isPalindrome(num):
	if str(num) ==str(num)[::-1]:
		return True
	else:
		return False


def Function():
	
	a=[j*i for j in range(100,1000) for i in range(100,1000) if len(str(i*j))>1]
	
	c = [b for b in a if isPalindrome(b)]
	print c
