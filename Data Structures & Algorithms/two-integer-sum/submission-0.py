class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        
        for i,n in enumerate(nums):
            key = target - n
            
            print(key)
            if key in tracker:
                return [tracker[key][0], i]
            else:
                tracker[n] = tracker.get(n, []) + [i]
        return [0, 0]