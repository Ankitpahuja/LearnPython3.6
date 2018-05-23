import pygame
# basic drawing shapes
WHITE = (255,255,255)
RED= (255,0,0)
polygonVertices=[(10,20),(450,590),(500,350)]
pygame.init()

window=pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World')

pygame.draw.polygon(window,WHITE,polygonVertices,2)   # draw polygon

pygame.draw.line(window, RED, (500,500), (100,100), 2) # draw line
# circle(Surface, color, pos, radius, width=0)
# ellipse(Surface, color, Rect, width=0)
# arc(Surface, color, Rect, start_angle, stop_angle, width=1)
# lines(Surface, color, closed, pointlist, width=1)

pygame.display.flip()

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

pygame.quit()
