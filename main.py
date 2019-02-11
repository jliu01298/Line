from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
draw_line(0,250,499,250,screen,color)
draw_line(250,0,250,499,screen,color)
draw_line(125,499,374,0,screen,color)
draw_line(0,125,499,374,screen,color)
draw_line(125,0,374,499,screen,color)
draw_line(0,374,499,125,screen,color)
draw_line(0,0,499,499,screen,color)
draw_line(0,499,499,0,screen,color)
display(screen)
save_extension(screen, 'img.png')
