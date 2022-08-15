def two_sum_value(nums: list[int], target: int) -> list[int]:
    nums.sort()
    for i, value in enumerate(nums):
        if value > target:
            nums = nums[0 : i]
    left, right = 0, len(nums) -1
    while left < right and nums[left] + nums[right] != target:
        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return [nums[left], nums[right]]

def two_sum_index1(nums: list[int], target: int) -> list[int]:
    for i, value in enumerate(nums):
        complement = target - value
        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + i + 1]

def two_sum_index2(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, value in enumerate(nums):
        nums_map[value] = i
    for i, value in enumerate(nums):
        complement = target - value
        if complement in nums_map and i != nums_map[complement]:
            return [i, nums_map[complement]]

case = list(map(int, input("input nums").split()))
target = int(input("input target"))
print(two_sum_value(case, target))
print(two_sum_index1(case, target))
print(two_sum_index2(case, target))