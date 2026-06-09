class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2
        res = []

        for i in range(n):
            for i in nums:
                res.append(i)

        return res