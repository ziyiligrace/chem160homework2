from random import choices
ntrials=15000
player1wins=0
for i in range(ntrials) :
    player2=choices(range(1,6) ,k=2)
    if player2[0] == player2[1]:
        continue
    player1=choices(range(1,6) ,k=3)
    player1.sort(reverse=True)
    if player1.count(2) >= 2 :
        continue
    if player1[0] + player1[1] > player2[0] + player2[1]:
        player1wins +=1

print("win ratio=",player1wins/ntrials)