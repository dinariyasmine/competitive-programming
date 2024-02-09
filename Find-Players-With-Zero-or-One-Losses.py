from ast import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    
        wins = {}
        losses = {}

        # Count wins and losses for each player
        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        
        players_no_losses = []
        players_one_loss = []
        
        
        for player in wins:
            if player not in losses:
                players_no_losses.append(player)

       
        for player, loss_count in losses.items():
            if loss_count == 1:
                players_one_loss.append(player)

        # Sort the lists in increasing order
        players_no_losses.sort()
        players_one_loss.sort()

        return [players_no_losses, players_one_loss]


