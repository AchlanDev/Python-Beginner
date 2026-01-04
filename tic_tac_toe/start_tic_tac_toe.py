# Options to ask players whether they want to play against another player or against AI

print("Welcome to Tic Tac Toe!")

opponent = input("Would you like to play against another player or an AI (1 or 2): ")

while not opponent.isdigit() or int(opponent) not in range(1, 3):
                opponent = input("Choose a option (1 or 2): ")

if opponent == '1':
    with open("tic_tac_toe.py") as a:
        code = a.read()
        exec(code)

else:
    with open("ai_tic_tac_toe.py") as b:
        code = b.read()
        exec(code)