class Solution(object):
    def kClosest(self, points, k):
        def distance(point):
            return math.sqrt(point[0]**2 + point[1]**2)

        def partition(start, end):
            pivot_distance = distance(points[end])
            i = start
            for j in range(start, end):
                if distance(points[j]) <= pivot_distance:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[end] = points[end], points[i]
            return i

        def quickSelect(start, end, k):
            if start <= end:
                pivot_index = partition(start, end)
                if pivot_index == k:
                    return
                elif pivot_index < k:
                    quickSelect(pivot_index + 1, end, k)
                else:
                    quickSelect(start, pivot_index - 1, k)

        quickSelect(0, len(points) - 1, k - 1)
        return points[:k]


