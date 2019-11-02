import pygame

pygame.init()

#BIlt drwaws the imgage to the screen
def car(carImg,x,y):
    gameDisplay.blit(carImg, (x, y))

display_width = 1600
display_height = 900

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')



x = (display_width * 0.3)
y = (display_height * 0.3)
x_change = 0
y_change = 0
car_speed = 0

car_width = 728

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    x += x_change
    y += y_change

    gameDisplay.fill(white)
    car(carImg,x,y)

    if x > display_width - car_width or x < 0:
        crashed = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()