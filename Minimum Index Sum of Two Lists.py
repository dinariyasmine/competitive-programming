from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_index_sum = float('inf') 
        common_restaurants = []
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:  
                    index_sum = i + j
                    if index_sum < least_index_sum:
                        least_index_sum = index_sum
                        common_restaurants = [list1[i]]
                    elif index_sum == least_index_sum:
                        common_restaurants.append(list1[i])

        return common_restaurants
