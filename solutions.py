"""
1. Two Sum
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create a dictionary of indices and values
        nums_dict = {}

        # Construct the dictionary as and when so as to avoid repeats
        for (idx, val) in enumerate(nums):

            # Check for a pair match
            if (target - val) in nums_dict:
                return [nums_dict[target - val], idx]

            else:
                nums_dict[val] = idx

"""
2. Add Two Numbers
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        remainder = 0
        sol = ListNode()
        tail = sol

        # While there is a value > 0
        while l1 or l2 or remainder:

            # Account for lists of different lengths
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            # The sum of the 2 nodes plus the remainder, accounting for values > 9
            addition = l1val + l2val + remainder
            addition, remainder = addition % 10, addition // 10

            # Update linked list val and next
            new_node = ListNode(addition)
            tail.next = new_node
            tail = tail.next

            # Move to the next node
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        sol = sol.next
        
        return sol

"""
19: Remove nth Node from End of List
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Find how long the list is
        list_length, dummy_head = 0, head

        while dummy_head:
            list_length += 1
            dummy_head = dummy_head.next
        
        # Edge cases: removing the first element (length 1 and length > 1)
        if n == list_length:
            head = head.next
            return head

        curr, prev = head, head

        # Go to the desired node, keeping track of previous
        for i in range(list_length - n):

            prev = curr
            curr = curr.next
        
        # Unlink previous from desired node, and link to next one
        nxt = curr.next
        prev.next = nxt

        return head

"""
151: Reverse Words in a String
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # A list of the words in s, in reverse order
        rev_split_string = s.split()[::-1]

        sol = ""
        for i in rev_split_string:
            # Add a word and a space
            sol += i + " "
        
        # Don't return the trailing space
        return sol[:-1]

"""
345: Reverse Vowels in a String
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
    
        # Find the vowels
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_s = [i for i in s if i in vowels]
        
        sol = ""
        idx = -1

        # Add normal letters in the normal order and vowels in reverse
        for i in s:
            if i in vowels:
                sol += vowels_in_s[idx]
                idx -= 1
            else:
                sol += i
        
        return sol


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
1071: Greatest Common Divisor of Strings
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Try prefixes starting with the length of the shortest word
        short_string = str1 if len(str1) < len(str2) else str2
        long_string = str2 if len(str1) < len(str2) else str1

        short_len, long_len = len(short_string), len(long_string)

        # The shortest prefix must divide both strings evenly
        prefix_len = short_len

        while True:
            if prefix_len == 1 and long_len % prefix_len != 0: 
                return ""

            if long_len % prefix_len == 0 and short_len % prefix_len == 0: 
                break

            else: 
                prefix_len -= 1
        
        prefix = short_string[:prefix_len]
        
        while prefix_len > 0:

            # The number of chunks to split the string into
            str1_no_splits = int(len(str1) / prefix_len)
            str2_no_splits = int(len(str2) / prefix_len)

            # Separate the strings into a list of parts of length prefix_len
            str1_set = set([str1[i * prefix_len: (i + 1) * prefix_len] for i in range(str1_no_splits)])
            str2_set = set([str2[i * prefix_len: (i + 1) * prefix_len] for i in range(str2_no_splits)])

            # The success criteria for finding a common prefix
            success = len(str1_set) == 1 and str1_set == str2_set

            # If the sets are the same, and their length is equal to 1, return the prefix
            if success: 
                prefix = list(str1_set)[0]
                return prefix

            # If the string length is 1 and no solution is found, return ""
            if prefix_len == 1 and not success: 
                return ""

            # If not, decrease the prefix length, and repeat
            else: 
                prefix_len -= 1
                while True:
                    if prefix_len == 1 and long_len % prefix_len != 0: 
                        return ""

                    if long_len % prefix_len == 0 and short_len % prefix_len == 0:
                        break

                    else: 
                        prefix_len -= 1

"""
1137: Nth Tribonnaci Number
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        
        t_0, t_1, t_2 = 0, 1, 1

        for i in range(n):
            t_next = t_0 + t_1 + t_2
            t_0, t_1, t_2 = t_1, t_2, t_next
        
        return t_0


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
