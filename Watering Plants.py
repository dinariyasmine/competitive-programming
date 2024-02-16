class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        watering_can = capacity
        steps = 0
        n = len(plants)
        for i in range(n):
            steps += 1
            if watering_can < plants[i]:
                steps += i * 2
                watering_can = capacity
            watering_can -= plants[i]
        return steps
