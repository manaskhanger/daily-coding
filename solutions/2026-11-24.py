# Median of Two Sorted Arrays (Hard)

def find_median(a, b):
    nums = sorted(a + b)
    n = len(nums)
    if n % 2:
        return nums[n//2]
    return (nums[n//2 - 1] + nums[n//2]) / 2