import random


def roll_dice(dice_number):
    dice_number = random.randint(1,6)
    return dice_number


def roll(roll_dice, dices):
    #first roll:roll1 = []
    for i in range(0, len(dices)):
        dices[i] = roll_dice(dices[i])
    print ("First roll: " + str(dices))
    #second roll:roll2 = []
    roll2 = [int(item2) for item2 in input("Witch dices do you want to reroll? : ").split()]
    for i in range(len(roll2)):
        roll2[i] = roll2[i] -1
    print (roll2)
    for i in roll2:
        dices[i] = roll_dice(dices[i])
    print ("Second roll: " + str(dices))
    #third roll:roll3 = []
    roll3 = [int(item3) for item3 in input("Witch dices do you want to reroll? : ").split()]
    for i in range(len(roll3)):
        roll3[i] = roll3[i] -1
    print (roll3)
    for i in roll3:
        dices[i] = roll_dice(dices[i])
    print ("Final roll: " + str(dices))


def one(dices):
    points = dices.count(1)*1
    return points


def two(dices):
    points = dices.count(2)*2
    return points


def three(dices):
    points = dices.count(3)*3
    return points


def four(dices):
    points = dices.count(4)*4
    return points


def five(dices):
    points = dices.count(5)*5
    return points


def six(dices):
    points = dices.count(6)*6
    return points


def one_pair(dices):
    dices2 = sorted(dices)
    for i in reversed(range(0, 4)):
        if dices2[i] == dices2[i+1]:
            points = dices2[i]*2
            return points
    points = 0
    return points


def two_pair(dices):
    dices2 = sorted(dices)
    for i in range (0, 2):
        if dices2[i] == dices2[i+1] and dices2[i+1] == dices2[i+2] and dices2[i+2] == dices2[i+3]:
            points = 0
            return points
    if dices2[0] == dices2[1] and dices2[2] == dices2[3]:
        points = dices2[0]+dices2[1]+dices2[2]+dices2[3]
        return points
    elif dices2[0] == dices2[1] and dices2[3] == dices2[4]:
        points = dices2[0]+dices2[1]+dices2[3]+dices2[4]
        return points
    elif dices2[1] == dices2[2] and dices2[3] == dices2[4]:
        points = dices2[1]+dices2[2]+dices2[3]+dices2[4]
        return points
    points = 0
    return points


def three_of_a_kind(dices):
    dices2 = sorted(dices)
    for i in range (0, 3):
        if dices2[i] == dices2[i+1] and dices2[i+1] == dices2[i+2]:
            points = dices2[i+2]*3
            return points
    points = 0
    return points


def four_of_a_kind(dices):
    dices2 = sorted(dices)
    for i in range (0, 2):
        if dices2[i] == dices2[i+1] and dices2[i+1] == dices2[i+2] and dices2[i+2] == dices2[i+3]:
            points = dices2[i+2]*4
            return points
    points = 0
    return points


def small_stright(dices):
    dices2 = sorted(dices)
    if dices2[0] == 1 and dices2[1] == 2 and dices2[2] == 3 and dices2[3] == 4 and dices2[4] == 5:
        points = 15
        return points
    points = 0
    return points


def large_stright(dices):
    dices2 = sorted(dices)
    if dices2[0] == 2 and dices2[1] == 3 and dices2[2] == 4 and dices2[3] == 5 and dices2[4] == 6:
        points = 20
        return points
    points = 0
    return points


def house(dices):
    dices2 = sorted(dices)
    if (dices2[0] and dices2[1] == dices2[2]) and (dices2[3] == dices2[4]) or (dices2[0] == dices2[1]) and (dices2[2] and dices2[3] == dices2[4]):
        points = sum(dices2)
        return points
    points =0
    return points


def chance(dices):
    points = sum(dices)
    return points


def yatzy(dices):
    dices2 = sorted(dices)
    if dices2[0] and dices2[1] and dices2[2] and dices2[3] == dices2[4]:
        points = 100
        return points
    points = 0
    return points


def printPlayerScorePlayer1(playerScore, units):
    print ("Player 1, here is your points: ")
    print (" ")
    for i in range (0, 6):
        #print (units[i] + ": " + playerScore[i])
        print (units[i], playerScore[i])
    print ("----------------------------")
    for i in range (6, 8):
        #print (units[i] + ": " + playerScore[i])
        print (units[i], playerScore[i])
    print ("----------------------------")
    for i in range (8, 17):
        #print (units[i] + ": " + playerScore[i])
        print (units[i], playerScore[i])
    print ("----------------------------")
    for i in range (17, 18):
        #print (units[i] + ": " + playerScore[i])
        print (units[i], playerScore[i])
    print ("----------------------------")

def printThisRollPoints(units, points):
    for i in range (0, len(thisRollPoints)):
        count = str(i +1)
        print (count + ": " +units[i], points[i])


if __name__ == '__main__':
    dices = [0,0,0,0,0]
    player1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    thisRollPoints = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    units = [
        "one", "two", "three", "four", "five", "six", "sum1", "bonus",
        "one pair", "two pair", "three of a kind", "four of a kind",
        "small stright", "large stright", "house", "chance", "yatzy", "sum"
    ]

    for n in range(len(player1)-5):
        roll(roll_dice, dices)
        
        thisRollPoints[0] = one(dices)
        thisRollPoints[1] = two(dices)
        thisRollPoints[2] = three(dices)
        thisRollPoints[3] = four(dices)
        thisRollPoints[4] = five(dices)
        thisRollPoints[5] = six(dices)
        thisRollPoints[8] = one_pair(dices)
        thisRollPoints[9] = two_pair(dices)
        thisRollPoints[10] = three_of_a_kind(dices)
        thisRollPoints[11] = four_of_a_kind(dices)
        thisRollPoints[12] = small_stright(dices)
        thisRollPoints[13] = large_stright(dices)
        thisRollPoints[14] = house(dices)
        thisRollPoints[15] = chance(dices)
        thisRollPoints[16] = yatzy(dices)

        printThisRollPoints(units, thisRollPoints)

        write = int(input("Where do you want to write this turn?"))
        write_index = write -1
        player1[write_index] = thisRollPoints[write_index]

        #regn ut delsum
        sum1 = []
        for i in range(0,6):
            sum1.append(player1[i])
        player1[6] = sum(sum1)

        #bonus
        if player1[6] >= 62:
            player1[7] = 50
        else:
            player1[7] = 0

        #regn ut sum
        sum2 = []
        for i in range(6,16):
            sum2.append(player1[i])
        player1[17] = sum(sum2)
        
        printPlayerScorePlayer1(player1, units)

    print ("Your final score is: " + player1[17])

#Hei Thomas :)