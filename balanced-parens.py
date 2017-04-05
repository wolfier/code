# Source: Problem Solving with Algorithms and Data Structures

# Balanced parentheses means that each opening symbol has a corresponding
# closing symbol and the pairs of parentheses are properly nested

# Samples of 
# (()()()())
# (((())))
# (()((())()))

def parenCheck(sequence):
	stack = []
	balanced = True
	index = 0
	while index < len(sequence) and balanced:
		char = sequence[index]
		if char == '(':
			stack.append(char)
		else:
			if not stack:
				balanced = False
			else:
				stack.pop()
		index = index + 1

	if balanced and not stack:
		return True
	else:
		return False

print(parenCheck('((()))'))
print(parenCheck('(()'))
