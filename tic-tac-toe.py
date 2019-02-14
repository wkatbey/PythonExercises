def draw_board(x, y, symbol, n):
    x_coord = 0
    y_coord = 0

    for i in range(n):
        for i in range(n):
            print(" ---", end='')

        print()
        
        for i in range(n+1):
            if x_coord == x and y_coord == y:
                print("|",' ', symbol, end=' ')
            else:
                print("|", end = '   ')
            x_coord += 1

        print()
        
        y_coord += 1

    for i in range(n):
        print(" ---", end='')
    

n = int(input("Enter the number of rows/columns: "))
x = 1
y = 1
draw_board(x,y, 'X', n)
