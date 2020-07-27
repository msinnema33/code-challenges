def containsDuplicate(self, nums: List[int]) -> bool:
## solution with sets
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

## solution without sets
# def no_set_Dups(self, nums: List[int]) -> bool:
#     seen = {}
#     for item in nums:
#         if seen.get(item):
#             print("duplicate found")
#             return True
#         else:
#             seen[item] = True
#     print("success")