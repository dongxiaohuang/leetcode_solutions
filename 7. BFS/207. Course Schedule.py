from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_pre_count = {}
        for prerequisite in prerequisites:
            course = prerequisite[0]
            course_pre_count[course] = course_pre_count.get(course, 0) + 1 
        finished = deque([course for course in range(numCourses) if course not in course_pre_count])
        for course in course_pre_count:
            if course_pre_count[course] == 0:
                finished.append(course)
        while finished:
            finished_course = finished.popleft()
            for prerequisite in prerequisites:
                to_learn_course = prerequisite[0]
                if course_pre_count[to_learn_course] <= 0:
                    continue
                elif finished_course in prerequisite:
                    course_pre_count[to_learn_course] -= 1
                    if course_pre_count[to_learn_course] == 0:
                        finished.append(to_learn_course)
        # print(course_pre_count)
        for course in course_pre_count:
            if course_pre_count[course] != 0:
                return False
        return True