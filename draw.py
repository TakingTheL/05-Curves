from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while (t <= step):
        x = r * math.cos(2 * math.pi * t / step) + cx
        y = r * math.sin(2 * math.pi * t / step) + cy
        z = cz
        if t != 0 and t != step:
            add_point( points, x, y, z)
        add_point(points, x, y, z)
        t += 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    x = generate_curve_coefs(x0,x1,x2,x3, curve_type)
    y = generate_curve_coefs(y0,y1,y2,y3, curve_type)
    ax = x[0][0]
    bx = x[0][1]
    cx = x[0][2]
    dx = x[0][3]
    ay = y[0][0]
    by = y[0][1]
    cy = y[0][2]
    dy = y[0][3]
    while (t <= step):
        time = float(t)/ step
        x = ax * math.pow(time, 3) + bx * math.pow(time, 2) + cx * time + dx
        y = ay * math.pow(time, 3) + by * math.pow(time, 2) + cy * time + dy
        z = 0
        if t != 0 and t != step:
            add_point(points,x,y,z)
        add_point(points, x, y, z)
        t += 1

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
