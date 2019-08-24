'''
question: 

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''
def maxAreabeforehelp(sample_height):

    area_values = []
    for i in range(len(sample_height)):
        area = (len(sample_height)-(i))*sample_height[i]
        area_values.append(area)
    maxbefore = max(area_values)
    return maxbefore

def maxAreaafterhelp(sample_height):
    area_values = []
    for i in range(len(sample_height)):
        area = ((i)*sample_height[i])
        area_values.append(area)
    maxafter = max(area_values)
    return maxafter
    

def maxArea(height):
    max_index = int(height.index(max(height)))
    before = height[:max_index]
    after = height[max_index:]
    print(maxAreabeforehelp(before))
    print(maxAreaafterhelp(after))
    print (max(maxAreabeforehelp(before), maxAreaafterhelp(after)))


maxArea([1,2,1])

            
        