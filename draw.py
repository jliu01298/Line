from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0>x1:
        x0,x1=x1,x0
        y0,y1=y1,y0
    x,y=x0,y0
    a=y1-y
    b=x-x1
    d=2*a+b
    if a>0:
        if a<-b:
            while x<=x1:
                plot(screen,color,x,y)
                if d>0:
                    y+=1
                    d+=2*b
                x+=1
                d+=2*a
        else:
            while y<=y1:
                plot(screen,color,x,y)
                if d<0:
                    x+=1
                    d+=2*a
                y+=1
                d+=2*b
    else:
        if b<a:
            while x<=x1:
                plot(screen,color,x,y)
                if d<0:
                    y-=1
                    d-=2*b
                x+=1
                d+=2*a
        else:
            while y>=y1:
                plot(screen,color,x,y)
                if d>0:
                    x+=1
                    d+=2*a
                y-=1
                d-=2*b
