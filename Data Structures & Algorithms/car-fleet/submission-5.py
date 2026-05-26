class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        a = sorted([(pos, speed[i]) for i, pos in enumerate(position)], reverse=True)
        print(a)
        for pos, spd in a: 
            time = (target - pos) / spd
            print("time:", time, "start pos", pos, "speed", spd)
            if not stack:
                stack.append([time])
                continue
            if time <= stack[-1][0]: 
                stack[-1].append(time)
            else: 
                stack.append([time])
        print("final times", stack)
        return len(stack)