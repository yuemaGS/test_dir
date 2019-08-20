fib = [1, 1]
while i < 20:
	fib.append(fib[i]+fib[i+1])
	i += 1
print(fib)
