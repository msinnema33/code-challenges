def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

#solution with a set
# def findDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)