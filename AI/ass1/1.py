def seq(color, n):
	if color=='Red':
		return [i for i in range(1,n+1,2)]
	elif color=='Green':
		return [i for i in range(0,n+1,2)]
	else:
		pass


print(seq(input("Enter COlor: "), int(input("Enter N: "))))


