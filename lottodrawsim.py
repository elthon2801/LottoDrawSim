import random
from typing import List, Any
while True:
    print("enter number of draws to bet on: ", end=' ')
    no_entries = int(input())
    print("enter your numbers: ")
    winning = []
    for a in range(0,6):
        print('enter # ', a+1, ' of 6: ', end =' ')
        winning.append(int(input()))
    entries = []
    for a in range(0,no_entries):
        rl = random.sample(range(1,58),6)
        entries.append(rl)
    for a in range(0, len(entries)):
        print((a+1),'. ',entries[a])

    correct_1 = 0
    correct_2 = 0
    correct_3 = 0
    correct_4 = 0
    correct_5 = 0
    correct_6 = 0
    print('')
    print('***MY NUMBERS*** --- ',winning)
    print('')
    for a in range(0,len(entries)):
        correct = 0
        for b in range(0,6):
            for c in range(0,6):
                if entries[a][b] == winning[c]:
                    correct += 1
        if correct == 6:
            correct_6 += 1
        elif correct == 5:
            correct_5 += 1
        elif correct == 4:
            correct_4 += 1
        elif correct == 3:
            correct_3 += 1
        elif correct == 2:
            correct_2 += 1
        elif correct == 1:
            correct_1 += 1
    print('6 NUMBERS MATCHED = ',correct_6)
    print('5 NUMBERS MATCHED = ',correct_5)
    print('4 NUMBERS MATCHED = ',correct_4)
    print('3 NUMBERS MATCHED = ',correct_3)
    print('2 NUMBERS MATCHED = ',correct_2)
    print('1 NUMBER MATCHED = ',correct_1)
    print('')
    print('NO. OF DRAWS:', no_entries)
    print('')
