import random


def roll():
    return random.randint(1, 6)


def get_num_players():
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Must be between 2 - 4 players")
        else:
            print("Invalid input. Please enter a number.")


def player_turn(player_idx):
    print("_" * 15)
    print("\nPlayer", player_idx + 1, "'s turn has just started!\n")
    current_score = 0

    while True:
        should_roll = input("Would you like to roll (y/n)? ").lower()
        if should_roll != "y":
            break

        value = roll()
        print("You rolled a:", value)

        if value == 1:
            print("You rolled a 1! Turn done.")
            current_score = 0
            break
        else:
            current_score += value
            print("Your score is:", current_score)

    print("Your total score is:", current_score)
    return current_score


def main():
    players = get_num_players()
    max_score = 50
    player_scores = [0] * players

    while max(player_scores) < max_score:
        for player_idx in range(players):
            player_scores[player_idx] += player_turn(player_idx)

    # Determine the winner
    winner_idx = player_scores.index(max(player_scores)) + 1
    print("\nPlayer", winner_idx, "wins with a score of", max(player_scores), "!")


if __name__ == "__main__":
    main()
