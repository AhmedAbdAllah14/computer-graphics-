import matplotlib.pyplot as plt

def midpoint_low_slope(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2

    change1 = 2 * (dy - dx)
    change2 = 2 * dy
    d = 2 * dy - dx

    x = x1
    y = y1
    points_x = []
    points_y = []

    points_x.append(x)
    points_y.append(y)


    while x < x2:
        if d < 0:
            d += change2
        else:
            d += change1
            y += 1

        x += 1
        
        points_x.append(x)
        points_y.append(y)


    plt.plot(points_x, points_y, 'ro-')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

   
midpoint_low_slope(2, 3, 10, 7)

