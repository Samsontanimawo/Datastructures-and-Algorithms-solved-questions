class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Construct the graph and calculate indegrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 2: Initialize a queue with nodes having zero indegree
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # Step 3: Perform topological sorting
        while queue:
            course = queue.popleft()
            numCourses -= 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If all courses can be completed, numCourses should be 0
        return numCourses == 0
