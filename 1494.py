'''
1494. Parallel Courses II
Hard

Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.


Example 1:

Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.

Example 2:

Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.

Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6

Constraints:

    1 <= n <= 15
    1 <= k <= n
    0 <= dependencies.length <= n * (n-1) / 2
    dependencies[i].length == 2
    1 <= xi, yi <= n
    xi != yi
    All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
    The given graph is a directed acyclic graph.

'''

class Solution:
    '''
    First we construct two dictionaries, one tracks all courses must come after key, 
    and the other tracks all courses must come before a key. Then remove all courses
    that depend on others (keys in coursesBefore) to get all the courses that can be 
    taken and store in a set. 

    Then, while available courses are not empty, we pop out k courses from it and remove
    those courses from the values in coursesBefore. If a course no longer depends on others,
    we can put this course into available. 

    Complexity: time O(n^2); space O(n)
    '''

    from math import ceil
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # there is no dependencies
        if not dependencies: 
            return ceil(n / k)

        # a dictionary, courses represent by value must come before that represented by key
        coursesBefore = {}
        for dep in dependencies:
            a, b = dep
            if b in coursesBefore: coursesBefore[b].add(a)
            else: coursesBefore[b] = {a,}

        # a dictionary, courses represent by value must come after that represented by key
        coursesAfter = {}
        for dep in dependencies:
            a, b = dep
            if a in coursesAfter: coursesAfter[a].add(b)
            else: coursesAfter[a] = {b, }

        r = 0
        # courses we can take
        available = set()
        # courses that don't depend on other courses
        for course in range(1, n+1):
            if course not in coursesBefore:
                available.add(course)

        # finish all courses
        while available:
            taken = []
            for _ in range(k):
                if not available: break
                taken.append(available.pop())
            for course in taken:
                if course in coursesAfter:
                    for c in coursesAfter[course]:
                        coursesBefore[c].remove(course)
                        if not coursesBefore[c]: available.add(c)
            r += 1
        return r
