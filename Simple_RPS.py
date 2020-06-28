import random
    

def ask_again():
    door = input("Hmmm... i dont't recognise that answer. Feed me again! ")
    return door

def game():
    n = int(input("Give the number of wins "))
    print("So, the first one to win "+str(n)+" times wins!")
    players_wins = 0
    computers_wins = 0
    while players_wins < n and computers_wins < n:
        player = input("Choose: R (Rock), P (Paper), S (Scissors) ")
        while player != "R" and player != "P" and player != "S":
            player = ask_again()
        inte = random.randrange(3)
        if inte == 0: computer = "R"
        if inte == 1: computer = "P"
        if inte == 2: computer = "S"
        if player == computer:print("That's a tie! Noone wins!")
        else:
            if player == "R":
                if computer == "P":
                    print("Paper covers Rock! You lose :(")
                    computers_wins+=1
                if computer == "S":
                    print("Rock smashes Scissor! You win :)")
                    players_wins+=1
            if player == "P":
                if computer == "R":
                    print("Paper covers Rock! You ein :)")
                    players_wins+=1
                if computer == "S":
                    print("Scissors cut Paper! You lose :(")
                    computers_wins+=1
            if player == "S":
                if computer == "R":
                    print("Rock smashes Scissors! You lose :(")
                    computers_wins+=1
                if computer == "P":
                    print("Scissors cut Papers! You win :)")
                    players_wins+=1
    if players_wins == n:print("Congratulations! You won!")
    else:print("I 'm afraid that you lost :(")
    answer = input("Would you like to play again? (Y/N) ")
    while answer != "Y"  and answer != "N":
        answer = ask_again()
    return answer

def main(key):
    if key == "Y":
        ask = game()
        if ask == "Y":main(ask)
        if ask == "N":
            print("Uh...ok. Good afternoon, good evening and goodbye!")
            exit()
        else:
            while ask!= "Y" or ask!="N":
                ask = ask_again()
            if ask == "Y":main()
            else:
                print("Uh...ok. Good afternoon, good evening and goodbye!")
                exit()
    else:
        print("Uh...ok. Good afternoon, good evening and goodbye!")
        exit()

key = input("Hmmmm..., how about a game? (Y/N) ")
while key != "Y" and key != "N":
    key = ask_again()

main(key)
    
    
    
    
