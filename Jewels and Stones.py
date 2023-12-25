class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in stones:
            if i in jewels:
                res += 1
        return res
    
def main():
    solution = Solution()
    print(solution.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
main()
