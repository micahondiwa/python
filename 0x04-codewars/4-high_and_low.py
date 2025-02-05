def high_and_low(numbers):
    numbers = numbers.replace(" ","")
    nums =[]
    for char in numbers.strip():
        nums.append(int(char))

    for i in range(len(nums)):
        low = nums[0]
        if nums[i] < low:
            low = nums[i]
        elif nums[i] > low:
            high = nums[i]
    return ((f'"{high} {low}"'))

nums = "19 27 3 4 5"
print(high_and_low(nums))
