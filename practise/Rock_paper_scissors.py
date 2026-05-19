def rps(p1, p2):
    #your code here
    l = ["rock" , "paper" , "scissors"]
    if p1 == p2 :
        return "Draw!"
    elif (p1 == l[0] and p2 == l[2]) or (p1 == l[2] and p2 == l[1]) or (p1 == l[1] and p2 == l[0]) :
        return "Player 1 won!"
    else:
        return "Player 2 won!"

print(rps("rock", "scissors"))