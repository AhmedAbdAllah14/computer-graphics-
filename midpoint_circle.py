from turtle import color
import matplotlib.pyplot as plt
import math
def circle (xc,yc,r):
    x = 0
    y = r
    dp = 1-r

    points_x = []
    points_y = []

    while x <= y :
          points_x.extend([
            xc + x, xc - x,
            xc + x, xc - x,
            xc + y, xc - y,
            xc + y, xc - y
        ])

          points_y.extend([
            yc + y, yc + y,
            yc - y, yc - y,
            yc + x, yc + x,
            yc - x, yc - x
        ])

          x = x + 1
          if dp < 0:
              dp = dp + 2*x + 1
          else :
              y = y - 1
              dp = dp + 2*x + 1 - 2*y
    
    points = list(set(zip(points_x, points_y)))

    points.sort(key=lambda point: math.atan2(
       point[1] - yc,
       point[0] - xc
    ))

    points.append(points[0])
    points_x = [point[0] for point in points]
    points_y = [point[1] for point in points]
   

    plt.plot(points_x, points_y, 'ko-')
    plt.axis('equal')
    plt.title("Midpoint Circle Algorithm")
    plt.grid(True)
    plt.show()


   


circle (3,3,10)