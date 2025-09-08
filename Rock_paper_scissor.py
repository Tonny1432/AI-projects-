import random
from sklearn.linear_model import LogisticRegression

print("Welcome to Rock-Paper-Scissors!")
print("Select Your option: Rock, Scissor, Paper")

move_to_number = {"rock": 0, "scissor": 1, "paper": 2}
number_to_move = {0: "rock", 1: "scissor", 2: "paper"}

past_move = []
past_next = []
previous_move = None

while True:
    for i in range (3):
        player = input("Enter your move: ").lower()
        if player not in move_to_number:
           print("Invalid! Enter rock, paper, or scissor.")
           continue

        player_number = move_to_number[player]

        # Save data if previous move exists
        if previous_move is not None:
            past_move.append([previous_move])
            past_next.append(player_number)

        # Train AI if it has data
        if len(set(past_next)) >=2 :
            model = LogisticRegression()
            model.fit(past_move, past_next)
            prediction_number = model.predict([[player_number]])[0]
            prediction_move = number_to_move[prediction_number]
        else:
            prediction_move = random.choice(["rock", "scissor", "paper"])

         # Show moves
        print("Your move:", player)
        print("AI move:", prediction_move)

        # Decide winner
        if player == prediction_move:
            print("It's a tie!")
        elif (player == "paper" and prediction_move == "rock") or (player == "rock" and prediction_move == "scissor") or (player == "scissor" and prediction_move == "paper"):
            print("You win!")
        else:
            print("AI wins!")

    # Update for next round
    previous_move = player_number

    # Continue or exist
    c = input("Do you want to continue? yes/no: ").lower()
    if c == "no":
        print("Thanks for playing!")
        break
