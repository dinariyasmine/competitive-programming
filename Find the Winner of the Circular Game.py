class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []
        for friend in range(1,n+1):
            friends.append(friend)
        i = 0
        while len(friends) > 1:
            loser_index = (i + k -1 ) % len(friends)
            print(loser_index)
            friends.pop(loser_index)
            i = loser_index
        return friends[0]


        
