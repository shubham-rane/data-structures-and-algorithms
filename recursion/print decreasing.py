# print numbers in decreasing order

inp = 5

def rec(n):
	if n == 0:
		return
	print(n)
	rec(n-1)
rec(inp)