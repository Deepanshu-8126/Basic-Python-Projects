
nums = [int(x) for x in input("Enter numbers: ").split()]

largest = max(nums)
nums.remove(largest)
second = max(nums)

print("Second largest number is:", second)
