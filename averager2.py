def averager(nums):
	sum = 0
	for num in nums:
		sum += num
	return sum/len(nums)

nums = []
count = int(input("How many numbers should I average? "))
for num in range(count):
	nums.append(float(input(f"Gimme input #{num+1}: ")))
print(f"Your average is {averager(nums)}")