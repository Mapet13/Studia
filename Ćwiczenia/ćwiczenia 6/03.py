def ferryCheck(ferry, cars):
    score = [[[0 for i in range(ferry)] for j in range(ferry)] for k in range(len(cars))]
    item = [[1 for i in range(ferry)] for j in range(ferry)]
    score.insert(0, item)

    for i in range(1, len(cars) + 1):
        for j in range(ferry):
            for k in range(ferry):
                if j - cars[i - 1] >= 0 and score[i - 1][j - cars[i - 1]][k]:
                    score[i][j][k] = 1
                elif k - cars[i - 1] >= 0 and score[i - 1][j][k - cars[i - 1]]:
                    score[i][j][k] = 1
    
    return score[len(cars)][ferry - 1][ferry - 1]

ferry = 8
cars = [4, 6, 1, 1, 4]
print(ferryCheck(ferry, cars))