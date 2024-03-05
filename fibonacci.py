# create a program to print fibonacci sequence up 100


loopNum = 100
fTeam = 0
sTeam = 1

print(fTeam)
print(sTeam)

for i in range(2,loopNum):
    tTeam = fTeam + sTeam
    fTeam = sTeam
    sTeam = tTeam
    print(tTeam)

