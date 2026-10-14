import matplotlib.pyplot as plt

def midpoint_high_slope(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    dp = 2 * dx - dy

    x = x1
    y = y1
    points_x = []
    points_y = []



    while y <= y2:

        points_x.append(x)
        points_y.append(y)
        y += 1


        if dp <= 0:
            dp = dp + 2*dx
        else:
            dp = dp + 2*dx - 2*dy
            x += 1

       
        
       


    plt.plot(points_x, points_y, 'ro-')
    plt.grid(True)
    plt.axis('equal')
    plt.show()


midpoint_high_slope(2,1,5,12)