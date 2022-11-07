
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29

import random


def run():
    win_points = 20
    aborted = False
    welcome_msg(win_points)
    players = get_players()
    print_players(players)
    random.shuffle(players)
    status_msg(players)
    current = players[0]
    winner = round_of_pig(current, players, win_points)
    game_over_msg(winner, aborted)


class Player:
    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


def round_of_pig(current, players, win_points):
    round_in_progress = True
    while round_in_progress:
        choice = get_player_choice(current)
        if choice == "r":
            roll = random.randint(1, 6)
            if roll > 1:
                current.roundPts += roll
                print(f"Got {roll}, running total is {current.roundPts}")
                if current.roundPts + current.totalPts >= win_points:
                    return current
            else:
                print("Got 1 lost it all!")
                current.roundPts = 0
                status_msg(players)
                current = next_player(current, players)
        elif choice == "n":
            current.totalPts += current.roundPts
            current.roundPts = 0
            status_msg(players)
            current = next_player(current, players)
        elif choice == "q":
            return


def next_player(current, players):
    index = players.index(current) + 1
    if index >= len(players):
        return players[0]
    return players[index]


# ---- IO Methods --------------
def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")


def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")


def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")


def get_player_choice(player):
    choice = input(f"Player is {player.name}. Commands are: r = roll , n = next, q = quit > ")
    return choice


def get_players():
    the_players = []
    player_amount = int(input("How many players want to participate the game? > "))
    for i in range(player_amount):
        player_name = input("Enter a player name > ")
        player = Player(player_name)
        the_players.append(player)
    return the_players


def print_players(the_players):
    player_list_string = ""
    for player in the_players:
        player_list_string = player_list_string + player.name + ", "
    print(f"The players in this game are {player_list_string}. Let the game begin!")


if __name__ == "__main__":
    run()
