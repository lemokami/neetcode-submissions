class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            ans = [0] * (2 * len(nums))
            pt = 0
            for n in nums:
                ans[pt] = n
                pt+= 1
            
            for n in nums:
                ans[pt] = n
                pt+= 1

            return ans