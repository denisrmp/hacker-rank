import random

moves = 'sprlk'
PAIRINGS = {
    'sp': 'Scissors cut paper. ',
    'pr': 'Paper covers rock. ',
    'rl': 'Rock crushes lizard. ',
    'lk': 'Lizard poisons Spock. ',
    'ks': 'Spock smashes scissors. ',
    'sl': 'Scissors decapitate lizard. ',
    'lp': 'Lizard eats paper. ',
    'pk': 'Paper disproves Spock. ',
    'kr': 'Spock vaporizes rock. ',
    'rs': 'Rock crushes scissors. '}


def check_winning_move(p1, p2):
    return (p1 + 1) % len(moves) == p2 or (p1 + 3) % len(moves) == p2


def print_outcome(outcome, winner='', loser=''):
    if winner + loser in PAIRINGS:
        outcome = PAIRINGS[winner + loser] + outcome
    print outcome


def main():
    wins = 0
    loses = 0
    ties = 0
    games = 0.0

    while True:
        print 'Enter your move or (q) to quit'
        print 'Choose (r)ock, (p)aper, (s)cissors, (l)izard or Spoc(k):'

        player_input = raw_input()
        player_move = moves.find(player_input)
        if player_move != -1:
            cpu_move = random.randint(0, 4)
            games = games + 1
            if check_winning_move(cpu_move, player_move):
                print_outcome('Computer Wins!', moves[cpu_move], player_input)
                loses = loses + 1
            elif check_winning_move(player_move, cpu_move):
                print_outcome('Player Wins!', player_input, moves[cpu_move])
                wins = wins + 1
            else:
                print_outcome("It's a Tie!")
                ties = ties + 1
        elif player_input == 'q':
            print 'Game Over!'
            print 'Player wins:', wins, '(', (wins/games)*100, '%)'
            print 'Computer wins:', loses, '(', (loses/games)*100, '%)'
            print 'Ties:', ties, '(', (ties/games)*100, '%)'
            break
        else:
            print 'Invalid Move!'
