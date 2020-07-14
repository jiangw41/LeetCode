'''
1344. Angle Between Hands of a Clock
Medium

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

Example 4:

Input: hour = 4, minutes = 50
Output: 155

Example 5:

Input: hour = 12, minutes = 0
Output: 0

Constraints:

    1 <= hour <= 12
    0 <= minutes <= 59
    Answers within 10^-5 of the actual value will be accepted as correct.
'''
class Solution:
    '''
    1 hour (60 minutes represents 360 degrees), so 1 minute represents 6 degrees. 
    Taking 0:00 as the starting point:
    The angle formed by minute hand: 6 * minutes
    The angle formed by hour hand:30 * hour + minutes / 2
    The angle between those two: diff = abs(30 * hour + minutes / 2 - 6 * minutes)
    If it is greater than 180, we need to get the smaller one: ans = 360 - diff
    
    Complexity: time, space O(1)
    '''
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs(6 * minutes - 30 * hour - minutes / 2)
        return diff if diff <= 180 else 360 - diff
