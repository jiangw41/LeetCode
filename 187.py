'''
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    '''
    We can use 0, 1, 2, 3 to represent those letters. We need 2 bits for each letter, 
    20 bits for 10 letters. So each 10-letter subsequence can be represented by an int, 
    converted from its corresponding 20-bit binary representation. Starting from index 0, 
    we can slide our 10-letter window one by one and save/lookup a dictionary to keep track 
    of 10-letter subsequences. Bit operations were used in window constructions and 
    reconstruction after sliding one letter. 
    
    Complexity: time O(n), space O(n) where n is the length of DNA sequence
    '''
       def findRepeatedDnaSequences(self, s: str) -> List[str]:
        toNum = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        ans, length = [], len(s)
        if length <= 10: return ans
        visited = {}
        val = 0
        for index in range(10):
            val = (val << 2) | toNum[s[index]]
        visited[val] = 1
        for index, char in enumerate(s[10:], 1):
            
            mask = 0x3ffff
            val = ((val & mask) << 2) | toNum[char]
            if val in visited: 
                if visited[val] != 1: continue
                visited[val] += 1
                candidate = s[index:index+10]
                ans.append(candidate)
            else: visited[val] = 1
        return ans
    '''
    # this method checks every 10-letter string and takes longer time 
    # for string comparison. 
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = {}
        length = len(s)
        end = length - 9
        ans = []
        for index in range(end):
            s1 = s[index:index+10]
            if s1 not in visited: visited[s1] = 1
            else:
                if visited[s1] == 1:
                    visited[s1] = 2
                    ans.append(s1)
        return ans
    '''