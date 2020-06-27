'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

class Solution:
	def maxArea(self, height) :
		start = 0
		end = len(height) - 1
		max_area = 0

		while(start < end):
			w = end - start
			h = min(height[start], height[end])
			area = w*h 
			if area > max_area:
				max_area = area
			if height[start] > height[end]:
				end = end - 1
			else:
				start = start + 1
	        
		return max_area


def test():
	inpt = [1,8,6,2,5,4,8,3,7]
	s = Solution()
	if s.maxArea(inpt) == 49:
		print(True)
	else:
		print(False)

if __name__ == '__main__':
	test()
