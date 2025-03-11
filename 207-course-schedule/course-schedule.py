from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build adjacency list and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)  # Directed edge pre -> course
            in_degree[course] += 1     # Increment in-degree for course

        # Step 2: Initialize queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0

        # Step 3: Process courses in order
        while queue:
            current = queue.popleft()
            completed_courses += 1  # Count completed courses

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1  # Reduce in-degree
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # Add to queue when prerequisites are met
        
        # Step 4: Check if all courses are completed
        return completed_courses == numCourses

# Example usage
sol = Solution()
print(sol.canFinish(2, [[1,0]]))  # Output: True
print(sol.canFinish(2, [[1,0], [0,1]]))  # Output: False (Cycle)
