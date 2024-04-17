"""
605: Can place flowers
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Edge cases
        if n == 0: return True
        if len(flowerbed) == 1 and n == 1:
            if  flowerbed[0] == 0: return True
            else: return False

        # First flower
        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        
        if n == 0: return True

        # Middle flowers
        for i in range(1, len(flowerbed) - 1):

            # Plant flower if the current and surrounding patches are 0
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

            if n == 0: return True
            
        # Last flower
        if flowerbed[-1] == flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        
        if n == 0: return True
        else: return False

"""
1431: Kids with the Greatest Number of Candies
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_el = max(candies)

        sol = [True if i + extraCandies >= max_el else False for i in candies]

        return sol

"""
1768: Merge Strings Alternately
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Deal with edge cases
        if len(word1) == 0: return word2
        if len(word2) == 0: return word1

        # Construct the solution
        sol = ""

        # Determine the longer and shorter word
        long_word = word1 if len(word1) > len(word2) else word2
        short_word = word1 if len(word1) < len(word2) else word2

        # Find the length of the shorter word
        short_len = len(short_word)

        # Alternately add letters until the end of the shortest string
        for i in range(short_len):

            sol += word1[i]
            sol += word2[i]

        # Append the rest of the longer string
        sol += long_word[short_len:]

        return sol
        
"""
1920. Build Array From Permutation
"""
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans
