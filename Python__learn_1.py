

import matplotlib.pyplot as plt

def DDA_drawing_line (x1 ,y1,x2,y2):

    dx = x2 - x1
    dy = y2 - y1
   
    steps = max (abs (dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    points_x = []
    points_y = []
    for i in range (steps+1):

         points_x.append(round(x))
         points_y.append(round(y))

         x = x + x_increment
         y = y + y_increment

    plt.plot(points_x, points_y, 'bo-')
    plt.grid(True)
    plt.axis('equal')
    plt.show()




DDA_drawing_line(3,3 ,8,8 )


