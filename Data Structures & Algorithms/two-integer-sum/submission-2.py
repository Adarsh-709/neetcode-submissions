class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_dict:
                return [hash_dict[complement], i]
            hash_dict[nums[i]] = i

