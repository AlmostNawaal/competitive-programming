def count_above_median(nums):
    nums.sort()
    
    n = len(nums)
    
    mid = n // 2
    
    if n % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid - 1] + nums[mid]) / 2.0 

    count = 0
    for i in range(n): 
        if nums[i] > median: 
            count = count + 1

    return count



n = int(input())
arr = list(map(int, input().split()))

print(count_above_median(arr))
