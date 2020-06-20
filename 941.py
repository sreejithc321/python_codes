'''
Given an array A of integers, return true if and only if it is a valid mountain array.
'''
class Solution:
	def validMountainArray(self, A):

		if len(A) < 3:
			return False

		index = 1
		while(index < len(A) and A[index] > A[index-1]):
			index +=1

		if (index == 1 or index == len(A)):
			return False
			
		while(index < len(A) and A[index] < A[index-1]):
			index +=1

		if index == len(A):
			return True
		else :
			return False
    
def test():
	inp = [1,5,3,10]
	s= Solution()
	result = s.validMountainArray(inp)
	print(result)

if __name__ == '__main__':
	test()
