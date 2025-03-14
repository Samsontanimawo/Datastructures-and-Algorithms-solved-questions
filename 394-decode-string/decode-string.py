class Solution:
    def decodeString(self, s):
        num, stack = 0, ['']
        for char in s:
            if char.isdigit():
                
                num = num * 10 + int(char)
                
            elif char == "[":
                stack.append(num)
                num = 0
                stack.append('')
                
            elif char == "]":
                pattern = stack.pop()
                repeat = stack.pop()
                prefix = stack.pop()
                stack.append(prefix + pattern * repeat)
            else:
                stack[-1] += char

        return ''.join(stack)