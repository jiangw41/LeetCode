'''
739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 
'''
class Solution:
	'''
	As we traverse T, we use a stack to store the indexes of items that have not seen a warmer temperature. Every time we move to a new temperature, we pop out all the items on the stack from the right that are colder than this temperature. 
	Complexity: time O(n*n); space O(n)
	'''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, ans = [], []
        length = len(T)
        for _ in range(length):
            ans.append(0)
        for index in range(length):
            while stack:
                i = stack[-1]
                if T[i] < T[index]:
                    stack.pop()
                    ans[i] = index - i
                else:
                    stack.append(index)
                    break
            if not stack: 
                stack.append(index)
        return ans