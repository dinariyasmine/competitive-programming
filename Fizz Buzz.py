class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        vector = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                vector.append("FizzBuzz")
            elif i % 3 == 0:
                vector.append("Fizz")
            elif i % 5 == 0:
                vector.append("Buzz")
            else:
                vector.append(str(i))
        return vector