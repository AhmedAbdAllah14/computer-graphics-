import matplotlib.pyplot as plt

def midpoint_low_slope(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    dp = 2 * dy - dx

    x = x1
    y = y1
    points_x = []
    points_y = []


    while x <= x2:

        points_x.append(x)
        points_y.append(y)

        x += 1
        if dp <= 0:
            dp = dp + 2*dy
        else:
            dp = dp + 2*dy - 2*dx
            y += 1

       


    plt.plot(points_x, points_y, 'ro-')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

   
midpoint_low_slope(2, 3, 10, 7)

