'''
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)
'''

class Solution:
    def numRescueBoats(self, people, limit) :

        sort_weights = sorted(people)
        left = 0
        right = len(people) - 1
        number_of_boats = 0
        
        while(left <= right ):
            
            if (left == right):
                number_of_boats +=1
                break
        
            if  sort_weights[left] + sort_weights[right] <= limit:
                left += 1
            
            number_of_boats +=1
            right -=1
            
        return number_of_boats


def test():
    s = Solution()
    people = [3,2,1]
    limit = 3
    result = s.numRescueBoats(people, limit)
    if(result== 2):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    test()
