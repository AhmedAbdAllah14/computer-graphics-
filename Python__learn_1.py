

import matplotlib.pyplot as plt

def DDA_drawing_line (x1 ,y1,x2,y2):

    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1

  
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        plt.plot([x1, x2], [y1, y2], 'ro-')
        plt.grid(True)
        plt.show()
        return
    slope = dy / dx


    x = x1
    y = y1


    points_x = []
    points_y = []

    if abs(dy) <= abs(dx):

     while x <=x2:
         points_x.append(round(x))
         points_y.append(round(y))

         x = x + 1
         y = y + slope
    else :
       y = y1
       if y1 <= y2 :
        while y <= y2:
          points_x.append(round(x))
          points_y.append(round(y))

          x = x + (1/abs(slope))
          y = y + 1
       else:
           while y >= y2:
            points_x.append(round(x))
            points_y.append(round(y))

            x = x + (1/abs(slope))
            y = y - 1

    

    plt.plot(points_x, points_y, 'bo-')
    plt.grid(True)
    plt.axis('equal')
    plt.show()




DDA_drawing_line(0,0 ,3 ,10 )


