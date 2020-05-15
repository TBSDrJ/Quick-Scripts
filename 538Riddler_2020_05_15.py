# Requires Python 3
# Looking at https://fivethirtyeight.com/features/can-you-find-the-best-dungeons-dragons-strategy/, posted 15th May, 2020.

from random import randrange

def d20 ():
    # Roll a single 20-sided die, return result
    return randrange(1,21)

def adv_dis():
    # Advantage of disadvantage, so roll twice with disadvantage, return higher
    first = min([d20(), d20()])
    second = min([d20(), d20()])
    return max(first, second)

def dis_adv():
    # Disadvantage of advantage, so roll twice with advantage, return lower
    first = max([d20(), d20()])
    second = max([d20(), d20()])
    return min(first, second)

ads = [] # List of all adv_dis rolls
das = [] # List of all dis_adv rolls
dice = [] # List of all single d20 rolls
numTrials = 10000000
for i in range(numTrials):
    ads.append(adv_dis())
    das.append(dis_adv())
    dice.append(d20())
adAvg = sum(ads) / len(ads)
daAvg = sum(das) / len(das)
diceAvg = sum(dice) / len(dice)
print('After', numTrials, 'trials, we see:')
print('Avgs: Adv of Dis:', adAvg, 'Dis of Adv:', daAvg, 'd20 roll:', diceAvg)
for i in range(1, 21):
    numAboveAD = 0
    for roll in ads:
        if roll >= i: numAboveAD += 1
    numAboveDA = 0
    for roll in das:
        if roll >= i: numAboveDA += 1
    numAboveDie = 0
    for roll in dice:
        if roll >= i: numAboveDie += 1
    print('Chance of %d or above: Adv of Dis: %6.4f Dis of Adv: %6.4f d20 roll: %6.4f' %
        (i, numAboveAD / len(ads), numAboveDA / len(das),
        numAboveDie / len(dice)))
