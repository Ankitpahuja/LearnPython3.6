import pygame

pygame.init()

window=pygame.display.set_mode((800,600))  

pygame.display.set_caption('Hello World')
window.fill((255,255,255))
pygame.display.flip()

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

pygame.quit()





#window=pygame.display.set_mode((800,600))
#window.fill((255,255,255))  # rect can be passed as tuple of two points











# testImg = pygame.image.load('test.jpg')
# window.blit(testImg, (0,0))

# pygame.font.init() 									# I am using this to display x and y position on top left of the screen
# myfont = pygame.font.SysFont('Comic Sans MS', 10)
# textsurface = myfont.render('HELLO WORLD', False, (0, 0, 0))  # antialias
# window.blit(textsurface,(0,0))
# pygame.font.quit()

# if event.type == pygame.MOUSEBUTTONDOWN:
#       pos = pygame.mouse.get_pos()  # will give tuple


