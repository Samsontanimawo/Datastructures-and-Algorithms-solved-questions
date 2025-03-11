class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)  # Directed edge pre -> course

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = fully processed

        def hasCycle(course):
            if visited[course] == 1:  # Cycle detected
                return True
            if visited[course] == 2:  # Already checked, no cycle
                return False
            
            visited[course] = 1  # Mark as visiting
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True  # Cycle found

            visited[course] = 2  # Mark as processed
            return False

        # Check for cycles in all courses
        for i in range(numCourses):
            if visited[i] == 0 and hasCycle(i):
                return False  # Cycle detected

        return True  # No cycles, all courses can be completed

# Example usage
sol = Solution()
print(sol.canFinish(2, [[1,0]]))  # Output: True
print(sol.canFinish(2, [[1,0], [0,1]]))  # Output: False (Cycle)
