def productExceptSelf(nums: list[int]) -> list[int]:
    result = []
    temp = 1
    for i in range(len(nums)):
        result.append(temp)
        temp = temp * nums[i]
    temp = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        result[i] = result[i] * temp
        temp = temp * nums[i]
    return result

print(productExceptSelf([1,2,3,4]))