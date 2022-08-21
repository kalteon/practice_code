def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters

        stack.append(i)
    return volume
print(trap([0,1,0,0,2,0,0,0,0,0,0,2]))