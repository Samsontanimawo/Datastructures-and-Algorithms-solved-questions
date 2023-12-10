class Solution(object):
    def addOperators(self, num, target):
        def dfs(index, path, current, last_operand):
            if index == len(num):
                if current == target:
                    result.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                operand = num[index:i]
                operand_val = int(operand)

                if index == 0:
                    dfs(i, operand, operand_val, operand_val)
                else:
                    dfs(i, path + '*' + operand, current - last_operand + last_operand * operand_val, last_operand * operand_val)
                    dfs(i, path + '+' + operand, current + operand_val, operand_val)
                    dfs(i, path + '-' + operand, current - operand_val, -operand_val)

                if num[index] == '0':
                    break  # Avoid leading zeros

        result = []
        dfs(0, "", 0, 0)
        return result