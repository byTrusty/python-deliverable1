name = input("Welcome to GC Mini Golf! What is your name? ")
value = '0'
game_size = input("Hi " + name + "! Would you like to play 3 or 6 holes today? ")
if game_size == '3':
    hole1 = input("How many putts for hole 1? (par is 3) ")
    hole2 = input("How many putts for hole 2? (par is 3) ")
    hole3 = input("How many putts for hole 3? (par is 3) ")
    par3 = 9
    total_score = int(hole1) + int(hole2) + int(hole3) - int(par3)
    print(f"Good game, {name}! Your total par was {total_score}")
elif game_size == '6':
    hole1 = input("How many putts for hole 1? (par is 3) ")
    hole2 = input("How many putts for hole 2? (par is 3) ")
    hole3 = input("How many putts for hole 3? (par is 3) ")
    hole4 = input("How many putts for hole 4? (par is 3) ")
    hole5 = input("How many putts for hole 5? (par is 3) ")
    hole6 = input("How many putts for hole 6? (par is 3) ")
    par3 = 18
    total_score = int(hole1) + int(hole2) + int(hole3) - int(par3)
    print(f"Good game, {name}! Your total par was {total_score}")
else:
    print(f"Sorry {game_size} was not an option.")
