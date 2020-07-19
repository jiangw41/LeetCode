'''
210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

'''
class Solution:
    '''
    First we define father and child. If course A is a prerequisite of course B, we say A is father and B is child. We use the following data structures:
1. a dictionary (fatherOf) where key is a father and value is its children 
2. another dictionary (childOf) where key is a child and value is the number of fathers
3. a set (toVisit) of courses that have no prerequisites or the prerequisites have been taken
4. a list (r) as the answer (the order of courses to take)
At the beginning, we go through prerequisites to construct fatherOf and childOf. Then we go over all the courses. If a course is not in childOf, it means it has no prerequisites and we can add it to toVisit. After that, we can repeat the following procedure:
1. pop one course from toVisit and add it to answer
2. delete this course from fatherOf if it is in 
3. for all its children, if it is in childOf, we decrease their value in childOf. If a child's value is 0 after decreasing, delete it from childOf and add it to toVisit. 
In the end, we check the length of answer, return it if the length equals to numCourses, otherwise return []

Complexity: time O(V+E); space O(V) where V is numCourses and E is the length of prerequisites.

    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0: return []
        if numCourses == 1: return [0]
        fatherOf, childOf, r, toVisit = {}, {}, [], set()
        for child, father in prerequisites:
            if father in fatherOf:
                fatherOf[father].append(child)
            else: fatherOf[father] = [child]
            if child in childOf:
                childOf[child] += 1
            else: childOf[child] = 1
        for num in range(numCourses):
            if num not in childOf: toVisit.add(num)
        while toVisit:
            course = toVisit.pop()
            r.append(course)
            if course in fatherOf:
                for child in fatherOf[course]:
                    if child in childOf:
                        childOf[child] -= 1
                        if not childOf[child]:
                            del childOf[child]
                            toVisit.add(child)
                del fatherOf[course]
        if len(r) == numCourses: return r
        return []
        