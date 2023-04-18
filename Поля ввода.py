import pygame



pygame.init()
screen = pygame.display.set_mode((600, 800)) # flags=pygame.NOFRAME (поставить или убрать крестики)
pygame.display.set_caption("Surprize Game")




running = True
while running:



    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



