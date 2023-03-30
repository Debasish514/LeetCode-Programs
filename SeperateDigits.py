class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            copy = i
            ans1=[]
            while copy!=0:
                ans1.append(copy%10)
                copy = copy//10
            ans1= reversed(ans1)
            for j in ans1:
                ans.append(j)
        return ans
