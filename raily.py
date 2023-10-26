# python code to implement Josephus problem 

# Josephus function which will take 
# two parameter N and K, number of people and positions respectively
# return the position of person survives
def Josephus(n, k):

	# initialize two variables i and ans
	i = 1
	ans = 0
	while(i <= n):

		# update the value of ans
		ans = (ans + k) % i
		i += 1
	
	# returning the required answer
	return ans + 1

# driver code
# let 
n = 14
k = 2

result = Josephus(n, k)
print(result)

# This code is contributed by sarveshc111.
