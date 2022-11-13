def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # list[(column, height)]

    for i, height in enumerate(([0] + heights + [0])):  # append zero heights at both ends
        while stack and stack[-1][1] > height:
            rect_right = i
            rect_height = stack.pop()[1]
            rect_left = stack[-1][0]
            area = (rect_right - rect_left - 1) * rect_height
            maxArea = max(area, maxArea)

        stack.append((i, height))

    return maxArea


arr = [2,1,5,6,2,3]
print(largestRectangleArea(arr))