'''
949. Largest Time for Given Digits
Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

 

Note:

    A.length == 4
    0 <= A[i] <= 9

Accepted
48,272
Submissions
126,236
'''
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ""
        A.sort()
        if A[0] >= 3: return ans
        if A[0] == 2: 
            if A[1] > 3 or A[2] > 5: return ans
            if A[3] <= 3:
                return "2"+str(A[3])+":"+str(A[2])+str(A[1])
            if A[3] < 6: 
                if A[2] < 4: 
                    return str(A[0])+str(A[2])+":"+str(A[3])+str(A[1])
                return str(A[0])+str(A[1])+":"+str(A[3])+str(A[2])
            # A[3] > 5
            if A[2] < 4:
                return str(A[0])+str(A[2])+":"+str(A[1])+str(A[3])
            return "2"+str(A[1])+":"+str(A[2])+str(A[3])
        else:
            if A[3] == 2:
                return "2"+str(A[2])+":"+str(A[1])+str(A[0])
            if A[2] == 2:
                if A[3] == 3:
                    return "23:"+str(A[1])+str(A[0])
                if A[3] < 6:
                    return "2"+str(A[1])+":"+str(A[3])+str(A[0])
                else: 
                    return "2"+str(A[1])+":"+str(A[0])+str(A[3])
            if A[1] == 2:
                if A[2] > 5: 
                    return str(A[0])+str(A[3])+":"+str(A[1])+str(A[2])
                if A[2] == 3:
                    if A[3] < 6: return "23:"+str(A[3])+str(A[0])
                    return "23:"+str(A[0])+str(A[3])
                return str(A[1])+str(A[0])+":"+str(A[2])+str(A[3])
            if A[1] > 5: 
                return ans
            if A[3] < 2: 
                return str(A[3])+str(A[2])+":"+str(A[1])+str(A[0])
            if A[3] < 6: 
                if A[2] < 2:
                    return str(A[2])+str(A[3])+":"+str(A[1])+str(A[0])
                if A[1] < 2: 
                    return str(A[1])+str(A[3])+":"+str(A[2])+str(A[0])
                return str(A[0])+str(A[3])+":"+str(A[2])+str(A[1])
            #A[3] > 5
            if A[2] > 5:
                if A[1] < 2: 
                    return str(A[1])+str(A[3])+":"+str(A[0])+str(A[2])
                return str(A[0])+str(A[3])+":"+str(A[1])+str(A[2]) 
            #A[2] < 6
            if A[2] < 2:
                return str(A[2])+str(A[3])+":"+str(A[1])+str(A[0])
            if A[1] < 2:
                return str(A[1])+str(A[3])+":"+str(A[2])+str(A[0])
            return str(A[0])+str(A[3])+":"+str(A[2])+str(A[1])
            
            
            