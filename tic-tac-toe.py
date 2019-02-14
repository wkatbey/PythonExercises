def draw_board(x, y, symbol, n):
    x_coord = 1
    y_coord = 1

    for i in range(n):
        x_coord = 1 

        for j in range(n):
            print(" ---", end='')

        print()
        
        for j in range(n+1):
            if x_coord == x and y_coord == y:
                print("|", symbol, end=' ')
            else:
                print("|", end = '   ')

            if j != n:
                x_coord += 1
            
        y_coord += 1
        print()
        
    for i in range(n):
        print(" ---", end='')

  
    

n = int(input("Enter the number of rows/columns: "))
symbol = input("Enter the symbol: ")
x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))
draw_board(x,y, symbol, n)
