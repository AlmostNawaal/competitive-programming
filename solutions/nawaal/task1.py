def rob_func(nums):
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    max_prev_two = nums[0] 
    
    max_prev_one = max(nums[0], nums[1])
    

    for i in range(2, n):
        max_current = max(max_prev_one, nums[i] + max_prev_two)
        
        max_prev_two = max_prev_one
        max_prev_one = max_current
        
    return max_prev_one



input_data = eval(input("Enter a list of integers:"))
result = rob_func(input_data)

print(result)