class Solution(object):
    def exclusiveTime(self, n, logs):
        exclusive_times = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(':')
            function_id, timestamp = int(function_id), int(timestamp)

            if action == 'start':
                if stack:
                    # Update the exclusive time for the function at the top of the stack
                    exclusive_times[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:  # action == 'end'
                exclusive_times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return exclusive_times