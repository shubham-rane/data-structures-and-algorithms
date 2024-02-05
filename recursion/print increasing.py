# print numbers in increasing order up till given number
inp = 5

def rec(n):
	if n == 0:
		return
	rec(n-1)
	print(n)
rec(inp)