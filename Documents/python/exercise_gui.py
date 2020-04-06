picture = [
    [0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],

]
for i in picture:
    for j in i:
        if j is 0:
            # By default print in python will print newline also end='\n'. To avoid this , assign end=' ' to print with space
            print(' ', end=' ')

        else:
            print('*', end=' ')
    print('\n')
