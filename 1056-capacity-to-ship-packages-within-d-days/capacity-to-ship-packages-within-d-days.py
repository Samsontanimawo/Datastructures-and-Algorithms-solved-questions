class Solution(object):
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            curr_weight = 0
            curr_days = 1

            for weight in weights:
                if curr_weight + weight > mid:
                    curr_days += 1
                    curr_weight = 0

                curr_weight += weight

            if curr_days > days:
                left = mid + 1
            else:
                right = mid

        return left
