import random
from game_data import data
from art import logo, vs


# TODO 2 Format account data into printable format.
def format_data(account):
    """Format account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# TODO 4.2 Use if Statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a" ## if a_followers is greater than b_followers AND guess is 'A' return True else, return False.
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
# TODO 1 Generate a random account from the game data.
account_b = random.choice(data)

# TODO 7 Make game repeatable.
while game_should_continue:

    # TODO 8 Make B become the next A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.\n")
    print("VS.\n")
    print(f"Against B: {format_data(account_b)}.\n")

    # TODO 3 Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # TODO 4 Check if user is correct.
    # TODO 4.1 Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # TODO 10 Clear screen between rounds.
    print("\n"*25)
    print(logo)
    # TODO 5 Feedback.
    if is_correct:
    # TODO 6 Score Keeping.
        score += 1
        print("You're right!")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final sore: {score}.")

