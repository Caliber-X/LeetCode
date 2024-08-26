class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            temp_now = temperatures[i]
            
            if temp_now > stack[-1][1]:
                while len(stack)>0 and temp_now > stack[-1][1]:
                    idx, _ = stack.pop()
                    ans[idx] = i - idx
                stack.append((i, temp_now))
            
            else:
                stack.append((i, temp_now))
        
        return ans
            

            